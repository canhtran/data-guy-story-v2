"""Verify the authored foundation examples against hand-calculated answers.
Run from the repository root: python3 scripts/check-wiki-examples.py
Each article starts with a fresh cafe-v1 fixture; databases are in memory.
"""
from pathlib import Path
import re
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
CAFE = (ROOT / 'static/examples/wiki/sql/cafe.sql').read_text()
EXPECTED = {
    'sql/overview': [[('2026-09-01', 2, 100000), ('2026-09-02', 1, 50000)]],
    'sql/join': [[(101, 'An', 40000), (102, 'An', 60000), (103, 'Bình', 50000), (104, None, 30000)], [(190000,)], [(150000,)]],
    'sql/window-function': [[(101, 1, 40000, 100000), (102, 1, 60000, 100000), (103, 2, 50000, 50000)], [(101, 1, 40000), (102, 1, 100000), (103, 2, 50000)], [(102, 1), (103, 2)]],
    'sql/cte': [[('An', 100000)]],
    'database/oltp-vs-olap': [[(101, 'paid')], [('2026-09-01', 100000), ('2026-09-02', 50000)]],
    'database/transaction': [[('paid',)], [('cancelled',)], [('paid',)], [(1,)]],
    'data-modeling/star-schema': [[('Cà phê', 40000), ('Cà phê sữa', 35000)]],
    'data-modeling/snowflake-schema': [[('Cà phê', 40000), ('Cà phê sữa', 35000)]],
    'data-modeling/slowly-changing-dimension': [[(1, 11, 'Bắc'), (2, 12, 'Trung')]],
}

def statements(article):
    text = (ROOT / 'content/wiki/nen-tang' / (article + '.md')).read_text()
    for block in re.findall(r'```sql\n(.*?)```', text, re.S):
        for statement in block.split(';'):
            if statement.strip():
                yield statement

for article, expected in EXPECTED.items():
    with sqlite3.connect(':memory:') as connection:
        connection.executescript(CAFE)
        actual = []
        for statement in statements(article):
            cursor = connection.execute(statement)
            if cursor.description:
                actual.append(cursor.fetchall())
        assert actual == expected, (article, actual, expected)
    print('PASS', article)

# Intentional bad input must be rejected and leave the fixture unchanged.
with sqlite3.connect(':memory:') as connection:
    connection.executescript(CAFE)
    errors = 0
    for statement in statements('database/overview'):
        try:
            connection.execute(statement)
        except sqlite3.IntegrityError as error:
            assert 'FOREIGN KEY' in str(error)
            errors += 1
    assert errors == 1
    assert connection.execute('SELECT COUNT(*) FROM payments').fetchone() == (4,)
    assert connection.execute('SELECT COUNT(*), COUNT(customer_id) FROM orders').fetchone() == (4, 3)
    # A second order with the same amount must still count as another sale.
    connection.execute("INSERT INTO orders VALUES (105,1,'2026-09-02',40000,'paid')")
    connection.execute("INSERT INTO payments VALUES (5,105,'success')")
    exists_query = list(statements('sql/join'))[-1]
    assert connection.execute(exists_query).fetchone() == (190000,)
print('PASS foreign key, NULL, duplicate-price cases')

for article in ('sql/query-optimization', 'database/database-index'):
    with sqlite3.connect(':memory:') as connection:
        connection.executescript(CAFE)
        plans = []
        for statement in statements(article):
            cursor = connection.execute(statement)
            if cursor.description:
                plans.append(' '.join(str(row[-1]) for row in cursor.fetchall()))
        assert len(plans) == 2
        assert 'SCAN orders' in plans[0], plans
        assert 'orders_customer_idx' in plans[1], plans
    print('PASS', article)

print('SQLite version:', sqlite3.sqlite_version)
