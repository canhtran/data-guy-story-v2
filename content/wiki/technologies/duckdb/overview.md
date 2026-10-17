---
title: "DuckDB: phân tích dữ liệu ngay trong một script"
description: "Cài DuckDB và chạy truy vấn đầu tiên mà không dựng database server."
draft: false
contentType: concept
weight: 1
level: beginner
topics: [duckdb]
prerequisites: []
related: []
---

Bạn nhận file doanh thu và muốn dùng SQL ngay trên laptop. DuckDB là database phân tích chạy trong process của ứng dụng; ví dụ Python dưới đây không cần dịch vụ riêng hay cổng kết nối. Nó phù hợp với quét/tổng hợp dữ liệu cục bộ, không tự trở thành hệ thống chia sẻ cho nhiều ứng dụng ghi đồng thời.

## Môi trường thực hành

Bộ bài dùng **DuckDB 1.4.3, Python 3.12, macOS Intel**, kiểm tra ngày 1/10/2026. Đây là phiên bản cố định cho ví dụ, không khẳng định là bản mới nhất. Linux và Windows chưa được kiểm thử. Cần biết SQL SELECT/GROUP BY và cách chạy script Python.

Trong thư mục học riêng, tạo môi trường rồi cài package:

```bash
python3.12 -m venv .venv-duckdb
source .venv-duckdb/bin/activate
python -m pip install duckdb==1.4.3
python -c "import duckdb; print(duckdb.__version__)"
```

Kết quả kiểm tra phiên bản: `1.4.3`. Trên Windows, lệnh activate khác; chưa coi đoạn shell này là hướng dẫn Windows.

## Một truy vấn đầu tiên

Lưu code vào `duckdb_first.py`, chạy `python duckdb_first.py`. Mỗi dòng là một đơn đã thanh toán; ID duy nhất, tiền nguyên đồng.

```python
import duckdb

con = duckdb.connect(":memory:")
try:
    con.execute("CREATE TABLE orders(order_id BIGINT PRIMARY KEY, shop VARCHAR, amount_dong BIGINT)")
    con.executemany("INSERT INTO orders VALUES (?, ?, ?)",
                    [(101, "A", 40000), (102, "A", 35000), (103, "B", 50000)])
    print(con.execute("SELECT shop, SUM(amount_dong) FROM orders GROUP BY shop ORDER BY shop").fetchall())
finally:
    con.close()
```

Kết quả: `[('A', 75000), ('B', 50000)]`. `:memory:` tạo database tạm trong bộ nhớ; đóng connection thì không còn bảng này. Nếu cần giữ bảng qua lần chạy, dùng một đường dẫn file và quản lý vòng đời file rõ ràng.

## Khi nào cần công cụ khác?

Nếu nhiều dịch vụ cần ghi giao dịch vào một database chung, xem database server như PostgreSQL. Nếu dữ liệu/công việc cần tài nguyên phân tán, xem Spark. Đừng chọn chỉ dựa vào số gigabyte: phép JOIN, memory, disk và concurrency đều ảnh hưởng.

Nếu `ModuleNotFoundError`, kiểm tra package đã cài vào đúng interpreter dùng chạy script. Không cài lại vào Python hệ thống khi đang dùng venv khác. Đọc tiếp [truy vấn file]({{< relref "/wiki/technologies/duckdb/query-files.md" >}}).

## Tài liệu gốc

[Python API, DuckDB 1.4 LTS](https://duckdb.org/docs/lts/clients/python/overview) mô tả connection trong memory/file và API thực thi. Phiên bản runtime của ví dụ được pin riêng ở trên.
