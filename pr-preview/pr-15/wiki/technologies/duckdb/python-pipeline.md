# DuckDB trong Python: transaction và chạy lại một lô

Script hôm nay chạy xong nhưng người vận hành không nhận được thông báo, nên chạy lại. Nếu lần nào cũng INSERT, số đơn có thể tăng gấp đôi. Với một lô đầy đủ theo ngày, ta có thể thay thế toàn bộ ngày đó trong một transaction.

## Điều kiện để thay thế đúng

Mỗi dòng là một đơn, ID duy nhất toàn bảng, tiền không âm và không thiếu. `business_date` đã được nguồn xác định theo Asia/Ho_Chi_Minh; script không tự suy từ đồng hồ máy. Lô phải chứa **đủ dữ liệu của ngày**, không phải một vài thay đổi mới. Nếu input thiếu, không được xóa dữ liệu cũ rồi thay bằng phần thiếu.

Dùng môi trường trong [tổng quan]({{< relref "/wiki/technologies/duckdb/overview.md" >}}):

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import duckdb

with TemporaryDirectory() as tmp:
    db = str(Path(tmp) / "cafe.duckdb")
    con = duckdb.connect(db)
    con.execute("""CREATE TABLE orders(order_id BIGINT PRIMARY KEY, business_date DATE,
                 amount_dong BIGINT NOT NULL CHECK(amount_dong >= 0))""")
    def replace_day(day, rows):
        con.execute("BEGIN TRANSACTION")
        try:
            con.execute("DELETE FROM orders WHERE business_date = ?", [day])
            con.executemany("INSERT INTO orders VALUES (?, ?, ?)", [(i, day, amount) for i, amount in rows])
            con.execute("COMMIT")
        except Exception:
            con.execute("ROLLBACK")
            raise
    try:
        replace_day("2026-10-01", [(101, 40000), (102, 35000)])
        replace_day("2026-10-01", [(101, 40000), (102, 35000)])
        print(con.execute("SELECT COUNT(*), SUM(amount_dong) FROM orders").fetchone())
        try:
            replace_day("2026-10-01", [(101, 40000), (101, 35000)])
        except duckdb.ConstraintException:
            print("duplicate rejected")
        print(con.execute("SELECT COUNT(*), SUM(amount_dong) FROM orders").fetchone())
    finally:
        con.close()
    check = duckdb.connect(db, read_only=True)
    try:
        print(check.execute("SELECT COUNT(*), SUM(amount_dong) FROM orders").fetchone())
    finally:
        check.close()
```

Kết quả: `(2, 75000)`, `duplicate rejected`, `(2, 75000)`, `(2, 75000)`. Lô lỗi không để ngày bị trống sau DELETE. Mở lại file cũng giữ được hai đơn. File ở vùng tạm, xóa sau script; khi làm thật cần đường dẫn bền vững và backup.

## Giới hạn

Transaction này bảo vệ bảng DuckDB, không rollback file output hay HTTP request. Muốn xuất file, ghi vào vùng staging rồi công bố theo cơ chế riêng. Parameter `?` dùng cho value, không phải tùy ý tên bảng/cột; không nội suy input người dùng thành câu SQL.

Nếu chạy nhiều process ghi cùng file, không giả định có mô hình server điều phối giống PostgreSQL. Thiết kế một writer hoặc chọn hệ thống phù hợp concurrency. Batch lớn cũng không nên biến thành hàng triệu vòng INSERT Python nếu có thể đọc file hoặc dùng ingestion API phù hợp.

## Tài liệu gốc

[Python DB API](https://duckdb.org/docs/lts/clients/python/dbapi), [transactions](https://duckdb.org/docs/lts/sql/statements/transactions) và [concurrency](https://duckdb.org/docs/lts/connect/concurrency) mô tả tham số, commit/rollback và giới hạn truy cập file.

