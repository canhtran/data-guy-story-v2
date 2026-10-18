# OLTP và OLAP

Lúc khách đặt cà phê, ứng dụng cần ghi một đơn thật nhanh. Cuối tháng, người quản lý cần cộng doanh thu của tất cả cửa hàng, so với tháng trước và phân tích từng sản phẩm. Cùng là dữ liệu bán hàng, nhưng hai công việc đòi hỏi cách phục vụ khác nhau.

**OLTP** — online transaction processing — phục vụ các giao dịch của ứng dụng. **OLAP** — online analytical processing — phục vụ việc phân tích. Đây là cách phân loại workload, không phải hai loại sản phẩm hoàn toàn tách biệt.

## Nhìn từ câu hỏi

| | Đặt một đơn | Báo cáo doanh thu quý |
| --- | --- | --- |
| Dữ liệu cần đụng tới | Một số dòng liên quan | Rất nhiều dòng trong kỳ |
| Việc chính | Đọc và ghi giao dịch | Lọc, JOIN, tổng hợp |
| Quan tâm | Phản hồi nhanh, cập nhật đúng | Số liệu đúng, truy vấn lớn hiệu quả |
| Người dùng | Ứng dụng và khách hàng | Người phân tích, quản lý, mô hình ML |

Đừng hiểu OLTP chỉ ghi và OLAP chỉ đọc. Ứng dụng giao dịch đọc rất nhiều; hệ phân tích vẫn cần ingest, sửa dữ liệu và cập nhật bảng.

## Thử trên cùng một database nhỏ

Dùng SQLite và [cafe-v1]({{< relref "/wiki/nen-tang/sql/overview.md" >}}):

```sql
SELECT order_id, status FROM orders WHERE order_id = 101;

SELECT business_date, SUM(amount_vnd) AS revenue_vnd
FROM orders
WHERE status = 'paid'
GROUP BY business_date
ORDER BY business_date;
```

Câu đầu tìm đúng một đơn: **101, paid**. Câu sau tạo hai dòng báo cáo: **2026-09-01, 100000** và **2026-09-02, 50000**. Với bốn dòng, cả hai đều nhanh. Khác biệt trở nên rõ khi có hàng triệu đơn và nhiều người dùng cùng lúc.

## Vì sao thường tách hệ phân tích?

Một báo cáo quét lịch sử dài có thể tranh CPU, bộ nhớ và I/O với ứng dụng đang nhận đơn. Hệ phân tích riêng giúp tổ chức dữ liệu theo nhu cầu đọc, giữ lịch sử và gom nhiều nguồn. Đổi lại, dữ liệu phải được chuyển qua pipeline và có độ trễ; con số trên báo cáo có thể chưa phản ánh giao dịch vừa xảy ra.

Replica đọc có thể giảm tải một phần, nhưng không tự giải quyết việc mô hình hóa dữ liệu hay hợp nhất nguồn. Một warehouse cũng không tự biến mọi truy vấn thành nhanh. Cần kiểm tra workload thật và độ mới mà người dùng chấp nhận.

Nếu mới có một ứng dụng nhỏ, chạy báo cáo đơn giản ngay trên database có thể đủ. Khi báo cáo ảnh hưởng ứng dụng hoặc cần lịch sử nhiều nguồn, mới có lý do rõ ràng để tách.

Đọc thêm [data warehouse]({{< relref "/wiki/data-engineering/data-warehouse.md" >}}) và [tối ưu SQL]({{< relref "/wiki/nen-tang/sql/query-optimization.md" >}}). Cú pháp ví dụ: [SQLite SELECT](https://www.sqlite.org/lang_select.html).

