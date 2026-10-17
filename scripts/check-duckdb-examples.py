"""Run exact article blocks against explicit independently calculated expectations.
Requires Python 3.12 and duckdb==1.4.3. All examples use temporary/in-memory data.
"""
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import duckdb
assert duckdb.__version__ == '1.4.3', duckdb.__version__
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
 'overview': ["[('A', 75000), ('B', 50000)]"],
 'query-files': ["[('001',)]", '(1,)', "[('A', 75000), ('B', 50000)]", "[('005', 10000)]"],
 'python-pipeline': ['(2, 75000)', 'duplicate rejected', '(2, 75000)', '(2, 75000)'],
 'performance-and-errors': ['(45,)', 'plan available', '2'],
}
for slug, expected in EXPECTED.items():
 article = ROOT/'content/wiki/technologies/duckdb'/f'{slug}.md'
 blocks = re.findall(r'```python\n(.*?)```', article.read_text(), re.S)
 assert len(blocks) == 1, (slug, len(blocks))
 with tempfile.TemporaryDirectory() as tmp:
  script = Path(tmp)/'example.py'; script.write_text(blocks[0])
  result = subprocess.run([sys.executable, str(script)], cwd=tmp, capture_output=True, text=True, timeout=30)
  assert result.returncode == 0, (slug, result.stderr)
  assert result.stdout.splitlines() == expected, (slug, result.stdout, expected)
 print('PASS', slug)
# Independent boundary probes: malformed money must fail, not silently disappear;
# SQL SUM ignores missing input, so count missing values separately.
con = duckdb.connect()
try:
 con.execute('CREATE TABLE money(v BIGINT NOT NULL CHECK(v>=0))')
 for bad in [None, -1]:
  try: con.execute('INSERT INTO money VALUES (?)', [bad])
  except duckdb.ConstraintException: pass
  else: raise AssertionError(('accepted invalid amount', bad))
 try: con.execute("SELECT CAST('forty thousand' AS BIGINT)")
 except duckdb.ConversionException: pass
 else: raise AssertionError('accepted malformed money')
 assert con.execute('SELECT COUNT(*) FROM money').fetchone() == (0,)
 assert con.execute('SELECT SUM(v), COUNT(*)-COUNT(v) FROM (VALUES (40000), (NULL)) t(v)').fetchone() == (40000, 1)
finally: con.close()
print('PASS invalid money and NULL boundaries')
