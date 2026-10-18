# DuckDB: đọc CSV, JSON và ghi Parquet

Không phải lúc nào cũng cần import file vào một bảng trước khi hỏi một câu SQL. DuckDB có các hàm đọc file; schema vẫn cần được quy định thay vì tin mọi kiểu dữ liệu suy luận đều đúng.

## Đầu vào nhỏ có hợp đồng

Dùng [môi trường DuckDB]({{< relref "/wiki/technologies/duckdb/overview.md" >}}). Mỗi dòng CSV là một đơn; mã đơn dạng chuỗi để giữ số 0 đầu. Giá trị tiền trống là chưa biết, không phải 0. Chỉ trạng thái paid được tính. Ngày nghiệp vụ chưa xuất hiện trong ví dụ này.

Code tự tạo file trong thư mục tạm rồi xóa khi xong:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import duckdb

con = duckdb.connect()
try:
    with TemporaryDirectory() as tmp:
        base = Path(tmp)
        csv_file = base / "orders.csv"
        csv_file.write_text("""order_id,shop,amount_dong,status
001,A,40000,paid
002,A,35000,paid
003,B,50000,paid
004,B,,pending
""", encoding="utf-8")
        con.execute("""CREATE TEMP TABLE orders AS
            SELECT * FROM read_csv(?, header=true, auto_detect=false,
              columns={'order_id':'VARCHAR','shop':'VARCHAR','amount_dong':'BIGINT','status':'VARCHAR'})""", [str(csv_file)])
        print(con.execute("SELECT order_id FROM orders ORDER BY order_id LIMIT 1").fetchall())
        print(con.execute("SELECT COUNT(*) FROM orders WHERE amount_dong IS NULL").fetchone())
        output = base / "paid.parquet"
        con.execute("COPY (SELECT * FROM orders WHERE status='paid') TO ? (FORMAT PARQUET)", [str(output)])
        print(con.execute("SELECT shop, SUM(amount_dong) FROM read_parquet(?) GROUP BY shop ORDER BY shop", [str(output)]).fetchall())
        json_file = base / "extra.jsonl"
        json_file.write_text('''{"order_id":"005","amount_dong":10000}
''', encoding="utf-8")
        print(con.execute("SELECT order_id, amount_dong FROM read_json_auto(?)", [str(json_file)]).fetchall())
finally:
    con.close()
```

Kết quả lần lượt: `[('001',)]`, `(1,)`, `[('A', 75000), ('B', 50000)]`, `[('005', 10000)]`. Tổng paid là 125000, không gồm đơn pending thiếu tiền. Có một dòng JSON nên suy luận ở đó chỉ để minh họa; production cần schema và kiểm tra lỗi riêng.

## File vẫn có thể sai

Nếu cột tiền có `bốn mươi nghìn`, parser BIGINT có thể từ chối. Không bật bỏ qua lỗi rồi dùng tổng thiếu như dữ liệu hoàn chỉnh. Đếm dòng lỗi, giữ file gốc và quy định cách sửa/reject.

Khi đọc wildcard nhiều file, một đơn xuất hiện hai lần vẫn có thể cộng hai lần. Kiểm tra uniqueness trước tổng hợp; đọc file không tạo ràng buộc khóa như bảng PRIMARY KEY. Cũng không gọi `union_by_name` là cách tự giải quyết schema evolution: cùng tên nhưng khác ý nghĩa vẫn sai.

Parquet giữ kiểu dữ liệu và có thể giúp engine bỏ qua cột/phần dữ liệu không cần; tốc độ thực tế phụ thuộc file và truy vấn. Ví dụ nhỏ này không phải benchmark.

## Tài liệu gốc

[CSV](https://duckdb.org/docs/lts/data/csv/overview), [JSON](https://duckdb.org/docs/lts/data/json/overview) và [Parquet](https://duckdb.org/docs/lts/data/parquet/overview) của DuckDB 1.4 LTS mô tả đọc file, schema và xuất Parquet.

