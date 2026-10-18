# DuckDB: đọc kế hoạch và xử lý lỗi tài nguyên

Truy vấn trên file nhỏ xong rất nhanh; sang dữ liệu thật thì hết bộ nhớ. Không chỉ kích thước file quyết định RAM: JOIN, sort, aggregation và việc đưa output về Python đều có thể giữ dữ liệu.

## Quan sát trước khi chỉnh

Dùng môi trường trong [tổng quan]({{< relref "/wiki/technologies/duckdb/overview.md" >}}). Code sau dùng dữ liệu tổng hợp 100000 dòng, không chứa thông tin thật:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import duckdb

con = duckdb.connect()
try:
    with TemporaryDirectory() as tmp:
        con.execute("SET threads = 2")
        con.execute("SET memory_limit = '256MB'")
        con.execute("SET temp_directory = ?", [str(Path(tmp) / "spill")])
        query = "SELECT SUM(i) FROM range(100000) AS t(i) WHERE i < 10"
        print(con.execute(query).fetchone())
        plan = con.execute("EXPLAIN " + query).fetchall()
        print("plan available" if plan and plan[0][1] else "no plan")
        print(con.execute("SELECT current_setting('threads'), current_setting('memory_limit')").fetchone()[0])
finally:
    con.close()
```

Kết quả: `(45,)`, `plan available`, `2`. Tổng độc lập là 0+1+…+9=45. Muốn xem toàn bộ operator, thay dòng kiểm tra bằng `print(plan[0][1])`. Ví dụ chỉ kiểm tra API/config và số liệu, không khẳng định đã spill hay nhanh hơn với hai thread.

## EXPLAIN và EXPLAIN ANALYZE

EXPLAIN cho kế hoạch mà không chạy toàn bộ truy vấn lấy kết quả. EXPLAIN ANALYZE thực thi truy vấn để lấy metrics; không dùng tùy tiện cho câu lệnh thay đổi dữ liệu nếu chưa hiểu tác động. Đọc số row vào/ra JOIN trước: kế hoạch nhanh không sửa được JOIN nhân đôi doanh thu.

Nếu quét Parquet, xem cột/bộ lọc cần thiết có được đưa vào scan. Với CSV, engine còn cần parse text; đổi sang Parquet có thể phù hợp cho dữ liệu được đọc lại nhiều lần, nhưng cần đo với query và file đại diện.

## Xử lý lỗi có căn cứ

`OutOfMemoryException`: giảm số tác vụ đồng thời, kiểm tra join cardinality, sort và output materialization. `memory_limit` không phải trần tuyệt đối cho toàn process; một số bộ nhớ ở ngoài buffer manager. Một số phép xử lý có thể spill, không phải mọi workload đều tự chạy được trên disk.

Lỗi temp directory: kiểm tra dung lượng và quyền ghi. Lỗi file không tồn tại: kiểm tra working directory và đường dẫn trước khi đổi SQL. Lỗi khóa file: kiểm tra process đang mở database, không xóa file database để “mở khóa”.

`fetchall()` đưa toàn bộ kết quả về Python; ví dụ chỉ có một row. Với output lớn, cân nhắc ghi trực tiếp ra file hoặc đọc từng batch phù hợp API.

## Tài liệu gốc

[Tuning workloads 1.4 LTS](https://duckdb.org/docs/lts/guides/performance/how_to_tune_workloads) và [EXPLAIN](https://duckdb.org/docs/lts/guides/meta/explain) là nguồn cho chẩn đoán kế hoạch/tài nguyên. Không có benchmark production trong bài này.

