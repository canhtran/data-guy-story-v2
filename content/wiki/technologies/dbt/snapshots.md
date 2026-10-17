---
title: "dbt snapshots: giữ lại các lần đổi trạng thái"
description: "Theo dõi lịch sử một dòng nguồn với snapshot strategy check trên DuckDB."
draft: false
contentType: tutorial
weight: 4
---

Bảng đơn hàng thường chỉ giữ trạng thái hiện tại. Nếu đơn 5 chuyển từ `pending` sang `paid`, báo cáo ngày mai cần giá trị mới, nhưng đôi khi mình còn cần trả lời: trước đó nó ở trạng thái nào, và thay đổi được ghi nhận khi nào?

Snapshot lưu lại các phiên bản mà dbt quan sát được khi chạy. Nó không phải bản sao liên tục của mọi sự kiện: nếu một đơn chuyển `pending → review → paid` giữa hai lần chạy, snapshot chỉ thấy trạng thái có mặt ở lần kiểm tra tiếp theo. Bài dùng chiến lược `check`, phù hợp khi không có cột `updated_at` đáng tin cậy.

Đã kiểm tra với dbt Core 1.10.18, dbt-duckdb 1.10.0, DuckDB 1.4.3 / Python 3.12 trên macOS Intel. Bắt đầu từ project [cafe-dbt]({{< relref "overview.md" >}}), dùng seed giả lập. Snapshot theo adapter có thể khác; chưa kiểm tra PostgreSQL hay các hệ khác.

## Khai báo những cột cần theo dõi

Thêm hai dòng sau vào seed `seeds/orders.csv` (thêm cột `updated_at` thì không cần cho chiến lược `check`):

```csv
5,2026-09-03,25000,pending
```

Tạo `snapshots/orders_history.yml`:

```yaml
snapshots:
  - name: orders_history
    relation: ref('stg_orders')
    config:
      schema: snapshots
      unique_key: order_id
      strategy: check
      check_cols:
        - amount_vnd
        - status
```

`order_id` là khóa nhận diện một đơn. Các cột trong `check_cols` là những thay đổi cần tạo phiên bản mới. Nếu bỏ `status` khỏi danh sách, chuyển `pending` sang `paid` sẽ không làm snapshot tạo phiên bản khác. Thêm cột mới vào mô hình cũng không tự động có nghĩa là cột đó được theo dõi.

Chạy seed, model rồi snapshot:

```bash
dbt seed --profiles-dir . --select orders
dbt run --profiles-dir . --select stg_orders
dbt snapshot --profiles-dir .
```

Mở DuckDB và đọc các cột cần thiết:

```python
import duckdb
with duckdb.connect('cafe.duckdb', read_only=True) as con:
    print(con.sql('''
        select order_id, amount_vnd, status, dbt_valid_from, dbt_valid_to
        from main_snapshots.orders_history
        where order_id = 5
        order by dbt_valid_from
    ''').fetchall())
```

Lần đầu có một phiên bản của đơn 5 với trạng thái `pending` và `dbt_valid_to` rỗng. Chạy `dbt snapshot --profiles-dir .` thêm lần nữa mà không đổi seed: vẫn chỉ một phiên bản. Thời điểm `dbt_valid_from` phụ thuộc lúc chạy nên không so sánh nó với một timestamp cố định.

## Thử thay đổi rồi khôi phục

Sửa status của đơn 5 trong CSV thành `paid`. Chạy lại theo thứ tự:

```bash
dbt seed --profiles-dir . --select orders
dbt run --profiles-dir . --select stg_orders
dbt snapshot --profiles-dir .
```

Truy vấn lịch sử lần này trả về hai phiên bản: `pending` có `dbt_valid_to` được đặt; `paid` có `dbt_valid_to` rỗng. Chạy snapshot lại mà không đổi dữ liệu không tạo phiên bản thứ ba.

Nếu cần thử lại từ đầu, dùng một bản sao thư mục học hoặc xóa bảng snapshot **chỉ trong database giả lập** rồi chạy snapshot lần đầu. Không xóa bảng lịch sử thật để xử lý một lỗi khác nếu chưa xác định tác động.

## Giới hạn cần nhớ

Snapshot chỉ nhìn thấy dữ liệu tại các lần chạy và chỉ theo dõi khóa duy nhất ổn định. Nếu nguồn xóa hẳn một dòng, cần chọn rõ chính sách hard delete; mặc định không nên giả định rằng dòng bị xóa sẽ biến mất hoặc được đánh dấu giống quy trình nghiệp vụ của bạn. Hãy kiểm tra cấu hình phiên bản dbt đang dùng trước khi chọn `hard_deletes`.

Cột `dbt_valid_from`/`dbt_valid_to` mô tả khoảng phiên bản snapshot coi là hợp lệ, không nhất thiết là thời gian nghiệp vụ hiệu lực. Muốn xem lịch sử “khách hàng đổi địa chỉ lúc nào trong thực tế” cần nguồn cung cấp thời điểm đúng hoặc một sự kiện có timestamp. Snapshot cũng không thay CDC, backup hay event log.

## Tài liệu gốc

- [Snapshots trong dbt](https://docs.getdbt.com/docs/build/snapshots): chiến lược timestamp/check và cấu hình.
- [Lựa chọn incremental hay snapshot](https://docs.getdbt.com/best-practices/how-we-handle-cdc/2-choosing-incremental-or-snapshots): trường hợp sử dụng và giới hạn.
