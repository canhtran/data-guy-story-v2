---
title: "dbt: từ file SQL đến một báo cáo chạy lại được"
description: "Dựng project dbt Core với DuckDB trên máy cá nhân, từ CSV đến doanh thu theo ngày."
draft: false
contentType: concept
weight: 1
---

Bạn đã viết được câu SQL tính doanh thu. Tuần sau có thêm dữ liệu, một đồng nghiệp muốn sửa quy tắc lọc đơn, và bạn không còn nhớ phải chạy file nào trước. Bài này thử tổ chức công việc đó thành một project nhỏ: dữ liệu mẫu → đơn hàng đã chuẩn hóa → doanh thu theo ngày.

Mình dùng dbt Core để quản lý các phép biến đổi; DuckDB thực thi SQL và lưu kết quả. Toàn bộ bài chạy local, miễn phí, không cần tài khoản cloud. dbt không thay thế bước lấy dữ liệu từ API hay hệ thống bán hàng. CSV ở đây chỉ giúp mình tập trung vào phần biến đổi.

## Chuẩn bị môi trường

Ví dụ đã kiểm tra với Python 3.12, dbt Core 1.10.18, dbt-duckdb 1.10.0, DuckDB 1.4.3 trên macOS Intel ngày 2/10/2026. Đây là bộ phiên bản của bài, không phải khẳng định về bản mới nhất. Chưa kiểm thử Windows/Linux. Cần biết SELECT, WHERE, GROUP BY và cách tạo file bằng trình soạn thảo.

Trong terminal macOS, tạo thư mục học mới:

```bash
mkdir cafe-dbt
cd cafe-dbt
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install dbt-core==1.10.18 dbt-duckdb==1.10.0 duckdb==1.4.3
python -m pip check
dbt --version
mkdir models seeds tests
```

Nếu máy chưa có Python 3.12, dừng ở đây và nhờ AI hướng dẫn cài theo hệ điều hành. Gửi tên hệ điều hành và lỗi dạng chữ, không gửi mật khẩu. Prompt có thể dùng: “Mình muốn học dbt local. Hãy kiểm tra Python 3.12 và môi trường ảo cùng mình, từng bước một; sau mỗi lệnh hãy nói kết quả mong đợi. Đừng tự đổi phiên bản package trong bài khi chưa giải thích nguyên nhân.”

Các file dưới đây đều nằm trong `cafe-dbt`. Giữ khoảng trắng trong YAML; không dùng tab.

File `dbt_project.yml`:

```yaml
name: cafe_wiki
version: '1.0'
config-version: 2
profile: cafe_wiki
model-paths: [models]
seed-paths: [seeds]
test-paths: [tests]
models:
  cafe_wiki:
    +materialized: table
```

File `profiles.yml`:

```yaml
cafe_wiki:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: cafe.duckdb
      schema: main
      threads: 1
```

Tên `profile` phải khớp khóa đầu trong `profiles.yml`. Bài luôn truyền `--profiles-dir .` để dùng cấu hình tại thư mục hiện tại. File `cafe.duckdb` sẽ chứa dữ liệu thực hành; không cần database server.

## Ba bước của báo cáo

File `seeds/orders.csv`:

```csv
order_id,business_date,amount_vnd,status
1,2026-09-01,60000,paid
2,2026-09-01,40000,paid
3,2026-09-02,50000,paid
4,2026-09-02,30000,cancelled
```

Một dòng là một đơn hàng. Tiền dùng số nguyên VND. Seed phù hợp với fixture nhỏ trong bài; đừng coi việc đưa dữ liệu khách hàng thật vào Git là cách nạp dữ liệu mặc định.

File `models/stg_orders.sql`:

```sql
select
    cast(order_id as bigint) as order_id,
    cast(business_date as date) as business_date,
    cast(amount_vnd as bigint) as amount_vnd,
    status
from {{ ref('orders') }}
```

File `models/daily_revenue.sql`:

```sql
select business_date, sum(amount_vnd) as revenue_vnd
from {{ ref('stg_orders') }}
where status = 'paid'
group by business_date
```

`ref` vừa trỏ đến relation vừa khai báo phụ thuộc. dbt biết phải có `orders` trước `stg_orders`, rồi mới đến `daily_revenue`. Trong ví dụ, hai model materialize thành bảng; mỗi lần chạy sẽ tính lại toàn bộ. Chưa có xử lý incremental.

Chạy tại thư mục có `dbt_project.yml`:

```bash
dbt debug --profiles-dir .
dbt build --profiles-dir .
```

Build đầu tiên tạo một seed và hai model. Bài tiếp theo mới thêm test, nên build thành công lúc này chưa chứng minh dữ liệu hợp lệ. Đóng các kết nối khác đến `cafe.duckdb`, rồi tạo file `inspect_revenue.py`:

```python
import duckdb
with duckdb.connect('cafe.duckdb', read_only=True) as con:
    for day, amount in con.sql(
        'select * from daily_revenue order by business_date'
    ).fetchall():
        print(day, amount)
```

```bash
python inspect_revenue.py
dbt build --profiles-dir .
python inspect_revenue.py
```

Cả hai lần phải in `2026-09-01 100000` và `2026-09-02 50000`. Đơn hủy 30.000 không được tính. Việc chạy lại không nhân đôi báo cáo vì model được xây lại, không phải vì mọi pipeline dbt đều tự chống trùng.

## Khi chạy không được

- `dbt: command not found`: kích hoạt lại `.venv`; kiểm tra `python -m pip show dbt-core` trong đúng môi trường.
- Không tìm thấy profile: kiểm tra thư mục hiện tại, tên file và `--profiles-dir .`.
- Lỗi cast: kiểm tra giá trị CSV vừa sửa. Đừng đổi thành bỏ qua dòng lỗi chỉ để build xanh.
- Lỗi khóa file: đóng Python session hoặc ứng dụng đang mở database; tránh chạy hai dbt process ghi cùng file.
- YAML parse error: nhìn dòng được báo và khoảng trắng của khóa cha trước khi sửa SQL.

Giữ lại câu lệnh, phiên bản và phần lỗi đầu tiên để nhờ AI giải thích. Đừng xóa database để chữa mọi lỗi: bạn sẽ mất bằng chứng và có thể che nguyên nhân.

Bài tập: đổi đơn 3 thành 55.000, build lại và dự đoán ngày nào thay đổi. Đáp án là ngày 2/9 thành 55.000, ngày 1/9 vẫn 100.000. Sau đó phục hồi fixture trước khi sang [kiểm tra dữ liệu]({{< relref "data-tests.md" >}}).

## Đọc thêm

- [dbt-duckdb: cấu hình adapter](https://github.com/duckdb/dbt-duckdb). README hiện tại có thể nói về phiên bản khác; bài này cố định bộ phiên bản ở trên.
- [ref và dependency](https://docs.getdbt.com/reference/dbt-jinja-functions/ref).
- [Seeds](https://docs.getdbt.com/docs/build/seeds) và [dbt build](https://docs.getdbt.com/reference/commands/build).
