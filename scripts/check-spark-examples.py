"""Execute the exact published Python blocks with independent output/plan checks.
Requires PySpark 3.5.6, Python 3.12 and JDK 17; see the Spark overview.
Run with the same interpreter as PYSPARK_PYTHON. Scratch output is temporary.
"""
from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'overview': ["[('A', 75000), ('B', 50000)]"],
    'architecture': ['[(0, 4), (1, 4)]'],
    'dataframe': ["[('A', 75000), ('B', 50000)]", '1', '2'],
    'rdd': ["[('A', 75000), ('B', 50000)]", '2'],
    'partition': ['4', '2', '3', '8'],
    'shuffle': ["[('A', 75000), ('B', 50000)]"],
    'catalyst': ['[3, 4, 5]'],
    'join-strategies': ["[(101, 'Trung tâm'), (102, 'Trung tâm'), (103, 'Bến xe')]" ] * 2,
    'structured-streaming': ['[(101, 40000), (102, 35000)]'],
}
PLANS = {'architecture': ['Exchange'], 'shuffle': ['Exchange'],
         'join-strategies': ['BroadcastHashJoin', 'SortMergeJoin']}
for slug, expected in EXPECTED.items():
    article = ROOT / 'content/wiki/technologies/spark' / (slug + '.md')
    blocks = re.findall(r'```python\n(.*?)```', article.read_text(), re.S)
    assert len(blocks) == 1, (slug, len(blocks))
    with tempfile.TemporaryDirectory(prefix='dgs-spark-check-') as tmp:
        script = Path(tmp) / 'example.py'
        script.write_text(blocks[0])
        env = dict(os.environ, SPARK_LOCAL_IP='127.0.0.1', PYSPARK_PYTHON=sys.executable)
        run = subprocess.run([sys.executable, str(script)], cwd=tmp, env=env,
                             capture_output=True, text=True, timeout=180)
        if run.returncode:
            raise AssertionError((slug, run.stdout, run.stderr[-6000:]))
        lines = run.stdout.splitlines()
        actual = [line for line in lines if line in expected]
        assert actual == expected, (slug, run.stdout, expected)
        for operator in PLANS.get(slug, []):
            assert operator in run.stdout, (slug, operator, run.stdout)
        if slug == 'catalyst':
            optimized = run.stdout.split('== Optimized Logical Plan ==')[1].split('== Physical Plan ==')[0]
            assert 'double_id' not in optimized, optimized
    print('PASS', slug, flush=True)
print('All nine exact article examples passed; local checks are not cluster fault tests.')
