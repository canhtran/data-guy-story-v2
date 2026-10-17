"""Run published dbt fixture in an isolated directory; use the pinned dbt venv."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import duckdb

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'content/wiki/technologies/dbt'

def files_from_article(name):
    text = (ARTICLE / name).read_text()
    return re.findall(r'(?:File|file) `([^`]+)`:\n\n```\w+\n(.*?)\n```', text, re.S)

with tempfile.TemporaryDirectory(prefix='wiki-dbt-') as tmp:
    work = Path(tmp)
    for name in ('overview.md', 'data-tests.md'):
        for filename, body in files_from_article(name):
            dest = work / filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body + '\n')
    dbt = str(Path(sys.executable).parent / 'dbt')
    env = dict(os.environ, DBT_SEND_ANONYMOUS_USAGE_STATS='false')
    def run(command, success=True):
        p = subprocess.run([dbt, command, '--profiles-dir', '.'], cwd=work,
                           env=env, text=True, capture_output=True)
        assert (p.returncode == 0) == success, p.stdout + p.stderr
        if command == 'build':
            return json.loads((work / 'target/run_results.json').read_text())['results']
    def revenue(expected):
        with duckdb.connect(str(work / 'cafe.duckdb'), read_only=True) as con:
            got = con.sql('select revenue_vnd from daily_revenue order by business_date').fetchall()
            assert got == [(x,) for x in expected], got
    run('debug')
    results = run('build')
    assert sum(x['status'] == 'pass' for x in results) == 4
    revenue([100000, 50000])
    run('build')
    revenue([100000, 50000])
    seed = work / 'seeds/orders.csv'
    original = seed.read_text()
    seed.write_text(original + '3,2026-09-02,50000,paid\n')
    failed = run('build', False)
    assert any(x['status'] == 'fail' and 'unique' in x['unique_id'] for x in failed)
    assert any(x['status'] == 'skipped' and 'daily_revenue' in x['unique_id'] for x in failed)
    revenue([100000, 50000])
    seed.write_text(original.replace('50000', '-50000'))
    failed = run('build', False)
    assert any(x['status'] == 'fail' and 'no_negative_amount' in x['unique_id'] for x in failed)
    seed.write_text(original.replace('50000', '55000'))
    run('build')
    revenue([100000, 55000])
    seed.write_text(original)
    run('build')
    revenue([100000, 50000])
    print('PASS: exact article files; baseline, rerun, duplicate FAIL/SKIP, negative FAIL, correction and recovery')
