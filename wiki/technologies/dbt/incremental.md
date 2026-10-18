# dbt incremental: nạp thêm mà không nhân đôi đơn

Khi bảng lớn, dựng lại mọi dòng sau mỗi lần chạy tốn thời gian. Incremental model giúp chỉ xử lý một phần dữ liệu, nhưng lúc đó bạn phải tự trả lời: phần nào là mới, bản ghi sửa thì sao, bản ghi đến muộn có bị bỏ sót không?

Bài dùng project và fixture trong [bài dbt đầu tiên]({{< relref "overview.md" >}}). Hãy tạo một bản sao thư mục `cafe-dbt` hoặc bắt đầu từ đầu bằng các file ở đó; không sửa project gốc nếu bạn muốn giữ nguyên bài trước. Cấu hình dưới đây đã được kiểm tra bằng dbt Core 1.10.18, dbt-duckdb 1.10.0 và DuckDB 1.4.3 trên Python 3.12/macOS Intel. Incremental strategy phụ thuộc adapter; không áp dụng nguyên cấu hình này cho PostgreSQL hay warehouse khác.

## Thêm model incremental

Tạo file `models/incremental_orders.sql`:

```sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='delete+insert'
) }}

select
    cast(order_id as bigint) as order_id,
    cast(business_date as date) as business_date,
    cast(amount_vnd as bigint) as amount_vnd,
    status
from {{ ref('orders') }}
{% if is_incremental() %}
where cast(order_id as bigint) >= (
    select coalesce(max(order_id), 0) from {{ this }}
)
{% endif %}
```

Lần đầu `is_incremental()` là false, nên model lấy đủ seed. Những lần sau truy vấn chỉ lấy `order_id` bằng hoặc lớn hơn khóa lớn nhất đang có. Dùng `>=` để có thể nạp lại bản ghi ở ranh giới; `unique_key` cùng chiến lược delete+insert thay bản ghi cũ thay vì chèn thêm hàng trùng.

Chạy lần đầu:

```bash
dbt run --profiles-dir . --select incremental_orders
```

Kiểm tra bằng DuckDB CLI nếu đã cài, hoặc Python:

```python
import duckdb
with duckdb.connect('cafe.duckdb', read_only=True) as con:
    print(con.sql('select order_id, amount_vnd from incremental_orders order by order_id').fetchall())
```

Bạn sẽ thấy bốn khóa 1–4. Chạy lại không làm số dòng tăng, nhưng seed vẫn được đọc và lọc. Incremental không tự biến một nguồn CSV thành CDC hay tự biết mọi thay đổi.

## Thêm đơn, sửa đơn mới nhất

Thêm dòng 5 vào `seeds/orders.csv`:

```csv
5,2026-09-03,25000,paid
```

Chạy theo thứ tự để seed được cập nhật trước model:

```bash
dbt seed --profiles-dir . --select orders
dbt run --profiles-dir . --select incremental_orders
```

Bảng có khóa 1–5. Bây giờ sửa tiền của khóa 5 thành `27000`, chạy lại hai lệnh trên. Khóa 5 được chọn lại vì nó bằng `max(order_id)`, và `unique_key` thay số tiền 25.000 bằng 27.000. Số dòng vẫn là năm.

## Dữ liệu cũ đến muộn

Sửa tiền khóa 1 từ `60000` thành `61000`, rồi chạy lại seed và model. Bảng incremental vẫn giữ 60.000 cho khóa 1: truy vấn chỉ lấy khóa từ 5 trở lên nên bản sửa cũ không được đọc. Đây là đánh đổi của cửa sổ nạp; không có test nào tự phát hiện nếu bạn không đối soát nguồn và đích.

Để lấy lại toàn bộ dữ liệu sau khi quy tắc lọc thay đổi hoặc có backfill lịch sử:

```bash
dbt seed --profiles-dir . --select orders
dbt run --profiles-dir . --select incremental_orders --full-refresh
```

Full refresh dựng lại bảng từ đầu; sau đó 61.000 phải xuất hiện. Trong pipeline thật, có thể dùng cửa sổ thời gian trễ, CDC, hoặc lịch backfill riêng. Chọn theo cam kết về dữ liệu muộn và chi phí đọc lại; chỉ tăng lookback cũng không giải quyết cập nhật đến trễ hơn cửa sổ đó.

Incremental là một giao kèo do nhóm dữ liệu thiết kế, không phải công tắc tăng tốc an toàn mặc định. Ghi lại grain/khóa, cách nhận diện thay đổi, thời gian trễ cho phép, cách xóa bản ghi nguồn và lệnh khôi phục. Thử các tình huống này trên bản sao trước khi đưa vào lịch chạy.

## Tham khảo

- [Incremental models trong dbt](https://docs.getdbt.com/docs/build/incremental-models): điều kiện `is_incremental`, lọc dòng và khóa duy nhất.
- [dbt-duckdb](https://github.com/duckdb/dbt-duckdb): adapter và chiến lược materialization. README có thể mô tả phiên bản mới hơn bộ pin trong bài.

