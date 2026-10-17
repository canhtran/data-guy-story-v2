"""Verify the published dbt snapshot example with an isolated DuckDB database."""
import os, re, subprocess, sys, tempfile
from pathlib import Path
import duckdb
ROOT=Path(__file__).resolve().parents[1]
ARTICLE=ROOT/'content/wiki/technologies/dbt'
def extract(article, pattern):
    match=re.search(pattern,(ARTICLE/article).read_text(),re.S)
    assert match, f'missing snippet in {article}'
    return match.group(1)
with tempfile.TemporaryDirectory(prefix='wiki-dbt-snapshot-') as tmp:
    w=Path(tmp)
    for f in ('models','seeds','tests','snapshots'): (w/f).mkdir()
    (w/'dbt_project.yml').write_text(extract('overview.md',r'File `dbt_project.yml`:\n\n```yaml\n(.*?)\n```')+'\n')
    (w/'profiles.yml').write_text(extract('overview.md',r'File `profiles.yml`:\n\n```yaml\n(.*?)\n```')+'\n')
    (w/'seeds/orders.csv').write_text(extract('overview.md',r'File `seeds/orders.csv`:\n\n```csv\n(.*?)\n```')+'\n')
    (w/'models/stg_orders.sql').write_text(extract('overview.md',r'File `models/stg_orders.sql`:\n\n```sql\n(.*?)\n```')+'\n')
    (w/'snapshots/orders_history.yml').write_text(extract('snapshots.md',r'Tạo `snapshots/orders_history.yml`:\n\n```yaml\n(.*?)\n```')+'\n')
    dbt=str(Path(sys.executable).parent/'dbt'); env=dict(os.environ,DBT_SEND_ANONYMOUS_USAGE_STATS='false')
    def run(*args):
        p=subprocess.run([dbt,*args,'--profiles-dir','.'],cwd=w,env=env,text=True,capture_output=True)
        assert p.returncode==0,p.stdout+p.stderr
    def rows():
        with duckdb.connect(str(w/'cafe.duckdb'),read_only=True) as con:
            return con.sql('select status,dbt_valid_to from main_snapshots.orders_history where order_id=5 order by dbt_valid_from').fetchall()
    with (w/'seeds/orders.csv').open('a') as f: f.write('5,2026-09-03,25000,pending\n')
    run('seed','--select','orders'); run('run','--select','stg_orders'); run('snapshot')
    assert len(rows())==1 and rows()[0][0]=='pending' and rows()[0][1] is None,rows()
    run('snapshot'); assert len(rows())==1
    seed=w/'seeds/orders.csv'; seed.write_text(seed.read_text().replace('5,2026-09-03,25000,pending','5,2026-09-03,25000,paid'))
    run('seed','--select','orders'); run('run','--select','stg_orders'); run('snapshot')
    history=rows(); assert len(history)==2 and history[0][0]=='pending' and history[0][1] is not None and history[1][0]=='paid' and history[1][1] is None,history
    run('snapshot'); assert len(rows())==2
    print('PASS: first capture, unchanged rerun, changed version, valid_to boundary, idempotent snapshot rerun')
