"""Run the published dbt incremental model through insert/update/backfill cases."""
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import duckdb

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'content/wiki/technologies/dbt'
def extract(path, pattern):
    text = path.read_text()
    match = re.search(pattern, text, re.S)
    assert match, f'could not extract {path}'
    return match.group(1)

with tempfile.TemporaryDirectory(prefix='wiki-dbt-incremental-') as tmp:
    work = Path(tmp)
    for folder in ('models', 'seeds', 'tests'):
        (work / folder).mkdir()
    overview = (ARTICLE / 'overview.md').read_text()
    project = extract(ARTICLE / 'overview.md', r'File `dbt_project.yml`:\n\n```yaml\n(.*?)\n```')
    profile = extract(ARTICLE / 'overview.md', r'File `profiles.yml`:\n\n```yaml\n(.*?)\n```')
    seed = extract(ARTICLE / 'overview.md', r'File `seeds/orders.csv`:\n\n```csv\n(.*?)\n```')
    model = extract(ARTICLE / 'incremental.md', r'Tạo file `models/incremental_orders.sql`:\n\n```sql\n(.*?)\n```')
    (work/'dbt_project.yml').write_text(project+'\n')
    (work/'profiles.yml').write_text(profile+'\n')
    (work/'seeds/orders.csv').write_text(seed+'\n')
    (work/'models/incremental_orders.sql').write_text(model+'\n')
    dbt = str(Path(sys.executable).parent / 'dbt')
    env = dict(os.environ, DBT_SEND_ANONYMOUS_USAGE_STATS='false')
    def run(*args):
        p = subprocess.run([dbt, *args, '--profiles-dir', '.'], cwd=work, env=env, text=True, capture_output=True)
        assert p.returncode == 0, p.stdout + p.stderr
    def read():
        with duckdb.connect(str(work/'cafe.duckdb'), read_only=True) as con:
            return con.sql('select order_id, amount_vnd from incremental_orders order by order_id').fetchall()
    run('seed','--select','orders')
    run('run','--select','incremental_orders')
    assert read() == [(1,60000),(2,40000),(3,50000),(4,30000)]
    run('run','--select','incremental_orders')
    assert len(read()) == 4
    with (work/'seeds/orders.csv').open('a') as f: f.write('5,2026-09-03,25000,paid\n')
    run('seed','--select','orders'); run('run','--select','incremental_orders')
    assert read()[-1] == (5,25000) and len(read()) == 5
    seed_path = work/'seeds/orders.csv'
    seed_path.write_text(seed_path.read_text().replace('5,2026-09-03,25000,paid','5,2026-09-03,27000,paid'))
    run('seed','--select','orders'); run('run','--select','incremental_orders')
    assert read()[-1] == (5,27000) and len(read()) == 5
    seed_path.write_text(seed_path.read_text().replace('1,2026-09-01,60000,paid','1,2026-09-01,61000,paid'))
    run('seed','--select','orders'); run('run','--select','incremental_orders')
    assert read()[0] == (1,60000)
    run('run','--select','incremental_orders','--full-refresh')
    assert read()[0] == (1,61000) and read()[-1] == (5,27000)
    print('PASS: full load, repeat, append, latest-key correction, old-key miss and full-refresh backfill')
