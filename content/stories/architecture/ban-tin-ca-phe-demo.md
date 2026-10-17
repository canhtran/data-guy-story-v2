---
title: "Khi bản tin quán cà phê đếm doanh thu hai lần"
description: "Một câu chuyện minh họa về phép JOIN, sự tin cậy của báo cáo và cách một team nhỏ tìm ra vấn đề."
draft: true
contentType: story
sidebar:
  hide: true
source_publisher: "Tình huống giả lập · bản xem trước"
topics: ["data-quality", "data-modeling"]
technologies: ["SQL", "PostgreSQL"]
---

> **Bài mẫu để xem giao diện.** Câu chuyện, nhân vật và số liệu dưới đây đều được tạo để minh họa. Đây là một tình huống giả lập, không phải nội dung từ engineering blog hay một sự cố có thật.

Sáng thứ Hai, chị chủ quán mở bản tin và thấy doanh thu hôm qua tăng gần gấp đôi. Nhưng quán không đông hơn, số ly bán ra cũng bình thường. Chị nhắn cho team: “Số này có đúng không vậy?”

Đó là lúc một query SQL tưởng như đơn giản trở thành câu chuyện về cách mình tin vào dữ liệu.

## Một báo cáo, hai nguồn dữ liệu

Quán có hai hệ thống: hệ thống bán hàng lưu đơn, còn hệ thống thanh toán lưu từng lần khách trả tiền. Team muốn đưa chúng về một bảng để chủ quán xem doanh thu và tình trạng thanh toán cùng lúc.

Trong ví dụ nhỏ này, bảng đơn hàng có hai dòng:

| order_id | amount_vnd |
| --- | ---: |
| O-01 | 100.000 |
| O-02 | 60.000 |

Tổng giá trị đơn là **160.000 VND**. Nhưng đơn O-01 có hai lần thanh toán: lần đầu thất bại, lần sau thành công.

| payment_id | order_id | status | amount_vnd |
| --- | --- | --- | ---: |
| P-01 | O-01 | failed | 100.000 |
| P-02 | O-01 | succeeded | 100.000 |
| P-03 | O-02 | succeeded | 60.000 |

## Một phép JOIN làm thay đổi số dòng

Team ghép bảng thanh toán vào đơn hàng bằng `order_id`, rồi cộng số tiền của đơn:

```sql
SELECT SUM(o.amount_vnd) AS order_value_vnd
FROM orders o
JOIN payments p ON p.order_id = o.order_id;
```

Sau JOIN, đơn O-01 xuất hiện hai lần. Kết quả trở thành **260.000 VND**: 100.000 + 100.000 + 60.000.

Query chạy thành công. Database không báo lỗi. Vấn đề nằm ở điều mỗi dòng đại diện: một dòng trong `orders` là một đơn, còn một dòng trong `payments` là một lần thanh toán.

## Team sửa từ câu hỏi nghiệp vụ

Thay vì chỉ thêm `DISTINCT`, team xác định hai chỉ số riêng:

- **Giá trị đơn:** cộng ở bảng đơn hàng, mỗi đơn một lần.
- **Tiền thu thành công:** cộng các giao dịch thành công ở bảng thanh toán.

```sql
SELECT SUM(amount_vnd) AS order_value_vnd
FROM orders;

SELECT SUM(amount_vnd) AS collected_vnd
FROM payments
WHERE status = 'succeeded';
```

Trong fixture này, cả hai đều bằng 160.000 VND. Điều đó không có nghĩa chúng luôn phải bằng nhau: một đơn chưa trả tiền hoặc một khoản hoàn tiền sẽ tạo ra chênh lệch cần giải thích.

Nếu cần một bảng báo cáo theo đơn, team tổng hợp thanh toán về một dòng mỗi đơn trước khi ghép. Họ cũng thêm một kiểm tra dùng chính fixture nhỏ này để phát hiện việc doanh thu bị nhân lên.

## Góc nhìn của mình

Điểm mình thấy đáng nhớ là một job chạy xanh chưa đủ để nói số liệu đúng. Câu hỏi “mỗi dòng đại diện cho điều gì?” thường giúp mình tìm lỗi nhanh hơn việc nhìn một query dài và sửa từng dòng.

Mình cũng sẽ giữ một vài ví dụ đủ nhỏ để tính tay. Khi AI gợi ý một query mới, mình có thể dùng chúng để kiểm tra xem lời giải thích có khớp với kết quả thực thi không.

Trong một hệ thống thật, mình còn cần biết cách nguồn biểu diễn hoàn tiền, thanh toán nhiều lần và cập nhật trạng thái. Ví dụ ở đây chưa bao phủ các trường hợp đó.

## Đọc tiếp trong Sổ tay

- [Data Engineer là gì?]({{< relref "/wiki/bat-dau/data-engineer-la-gi.md" >}}) — có ví dụ về grain và ghép dữ liệu từ nhiều hệ thống.
- [Chất lượng dữ liệu]({{< relref "/wiki/data-engineering/data-quality.md" >}}) — vì sao cần kiểm tra đầu ra, dù pipeline đã chạy xong.

## Về nguồn của bài mẫu

Đây là nội dung hư cấu phục vụ kiểm tra giao diện. Khi có bài thật, phần này sẽ ghi bài gốc, tác giả, đơn vị xuất bản, ngày và đường dẫn tham khảo.
