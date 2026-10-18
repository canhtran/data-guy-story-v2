# dbt tests: build xanh chưa chắc doanh thu đúng

Trong [project quán cà phê]({{< relref "overview.md" >}}), nếu một đơn bị chép hai lần thì SQL vẫn chạy. Báo cáo có thể tăng tiền mà không có lỗi cú pháp nào. Mình cần viết rõ điều kiện dữ liệu phải thỏa, rồi cố tình làm sai để xem kiểm tra có bắt được không.

Dùng môi trường và bốn đơn hàng nguyên bản của bài trước. Ví dụ đã chạy trên dbt Core 1.10.18 / dbt-duckdb 1.10.0 / DuckDB 1.4.3, Python 3.12, macOS Intel. Không cần cài package test bên ngoài.

## Kiểm tra khóa và tiền

Tạo file `models/schema.yml`:

```yaml
version: 2
models:
  - name: stg_orders
    description: Một dòng cho một đơn hàng của fixture quán cà phê.
    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
      - name: amount_vnd
        data_tests:
          - not_null
```

Tạo file `tests/no_negative_amount.sql`:

```sql
select order_id, amount_vnd
from {{ ref('stg_orders') }}
where amount_vnd < 0
```

SQL của singular test trả về những dòng vi phạm. Không có dòng là đạt. Tiền NULL không bị điều kiện `< 0` bắt, nên mình có thêm `not_null`. Bốn test trên không kiểm tra mọi quy tắc kinh doanh: status sai chính tả hay ngày bị thiếu vẫn cần điều kiện riêng.

```bash
dbt build --profiles-dir .
```

Với fixture nguyên bản, bốn test đều PASS, báo cáo vẫn là 100.000 và 50.000.

## Cố tình làm dữ liệu sai

Thêm đúng một dòng sau vào cuối `seeds/orders.csv`:

```csv
3,2026-09-02,50000,paid
```

Chạy lại `dbt build --profiles-dir .`. Kiểm tra unique của `stg_orders.order_id` phải FAIL, và model `daily_revenue` phía sau bị SKIP. Đây là lỗi dữ liệu có chủ đích, không phải cài đặt hỏng. Xóa dòng vừa thêm rồi build lại; mọi test phải PASS.

Tiếp theo đổi tiền của đơn 3 từ `50000` thành `-50000`, giữ nguyên các dòng khác. Build phải báo `no_negative_amount` FAIL. Phục hồi thành `50000`, build lại rồi chạy `python inspect_revenue.py` để xác nhận kết quả ban đầu.

Không nên chỉ nhìn dòng cuối terminal. Tìm tên test thất bại, mở SQL tương ứng và hỏi: dòng nào vi phạm quy tắc nào? Nếu nhờ AI, gửi fixture giả này cùng lỗi và yêu cầu nó giải thích trước khi đề xuất sửa dữ liệu.

## Test không phải transaction cho toàn pipeline

Trong bài, model `stg_orders` đã có dữ liệu lỗi trước khi test chạy. Build thất bại không có nghĩa mọi bảng đã quay về trạng thái cũ. Báo cáo phía sau có thể vẫn chứa kết quả lần chạy trước vì lần này bị bỏ qua. Người dùng báo cáo cần biết độ mới của dữ liệu, không chỉ thấy bảng vẫn tồn tại.

`dbt run` chạy model, không thay cho `dbt test`. Với luồng bài này, dùng `dbt build` để chạy tài nguyên và test theo phụ thuộc. Cũng đừng hiểu `unique` là ràng buộc database ngăn mọi lần ghi: đây là truy vấn kiểm tra tại thời điểm chạy.

## Giữ bằng chứng lần chạy

Mở `target/run_results.json` để xem trạng thái các tài nguyên của lệnh vừa chạy; `logs/dbt.log` giữ chi tiết chẩn đoán. Các lần chạy sau có thể ghi đè artifacts trong target, nên sao chép chúng ra thư mục riêng trước khi thử sửa nếu cần so sánh. Không đăng log chứa thông tin kết nối thật lên diễn đàn.

Bài tập: với đơn trùng, giải thích vì sao chỉ thêm `distinct` vào báo cáo là chưa đủ. Nếu hai dòng cùng mã đơn nhưng khác tiền, mình cần quy tắc chọn bản ghi hoặc chặn dữ liệu để điều tra; xóa trùng tùy tiện có thể làm mất thay đổi hợp lệ.

Bộ bài hiện chưa có incremental model, snapshot, source freshness hay lịch chạy. Hai bài này đủ để dựng project và kiểm tra dữ liệu nhỏ; chưa phải quy trình vận hành warehouse hoàn chỉnh.

## Tài liệu gốc

- [Data tests](https://docs.getdbt.com/docs/build/data-tests).
- [Hành vi dbt build khi test thất bại](https://docs.getdbt.com/reference/commands/build).

