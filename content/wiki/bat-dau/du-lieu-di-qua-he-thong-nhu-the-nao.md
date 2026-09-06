---
title: "Data đi qua một hệ thống như thế nào?"
description: "Theo dấu data của một đơn hàng từ Source System đến khi xuất hiện trên dashboard."
draft: true
contentType: "concept"
weight: 2
level: "beginner"
topics: ["bat-dau", "data-lifecycle"]
prerequisites: ["data-engineer-la-gi"]
related: ["etl-elt", "batch-processing", "stream-processing"]
aliases:
  - "/docs/foundation/vong-doi-cua-data/"
---

Giả sử bạn vừa đặt một phần cơm trên ứng dụng giao đồ ăn. Bạn bấm **Đặt món**, ứng dụng báo thành công, rồi khoảng ba mươi phút sau tài xế xuất hiện trước cửa.

Với bạn, giao dịch đó đã kết thúc. Với hệ thống data, nó chỉ vừa bắt đầu.

## Data Generation

Khi đơn hàng được đặt, hệ thống có thể ghi lại mã đơn, nhà hàng, món ăn, giá tiền, phương thức thanh toán và thời gian tạo đơn. Trong lúc giao hàng, nó tiếp tục nhận vị trí tài xế và các lần thay đổi trạng thái.

Data này không nhất thiết nằm cùng một chỗ. Đơn hàng có thể ở PostgreSQL, thanh toán đến từ một dịch vụ khác, còn vị trí tài xế được gửi liên tục qua event stream.

Đây là các **Source System**. Chúng được xây để ứng dụng hoạt động, chứ không phải để trả lời mọi câu hỏi phân tích của công ty.

## Data Ingestion

Đội vận hành muốn biết hôm nay có bao nhiêu đơn giao trễ. Đội tài chính cần đối soát thanh toán. Nhà hàng muốn xem món nào bán chạy. Nếu tất cả cùng truy vấn thẳng vào database của ứng dụng, họ có thể làm chậm hệ thống đang phục vụ khách hàng.

Vì vậy, data được đưa ra khỏi các Source System. Có nguồn được lấy theo lịch, chẳng hạn mỗi giờ một lần. Có nguồn gửi event ngay khi thay đổi xảy ra. Quá trình này được gọi là **Data Ingestion**.

## Data Storage

Sau **Data Ingestion**, data cần một nơi để sống lâu hơn Source System. Tuỳ nhu cầu, nó có thể được lưu trong **Data Warehouse**, **Data Lake** hoặc **Lakehouse**.

Ở thời điểm này, data chưa chắc đã dễ dùng. Tên nhà hàng có thể nằm trong một bảng, thông tin đơn hàng nằm ở bảng khác, còn data thanh toán dùng một mã định danh khác hoàn toàn.

## Data Processing và Data Transformation

Các pipeline sẽ kiểm tra, làm sạch và kết hợp data. Ví dụ, một pipeline có thể:

1. Loại những lần cập nhật bị gửi trùng.
2. Chuẩn hoá tất cả thời gian về cùng múi giờ.
3. Ghép đơn hàng với nhà hàng và giao dịch thanh toán.
4. Tính thời gian từ lúc đặt món đến lúc giao thành công.
5. Tạo một bảng chỉ gồm các chỉ số mà đội vận hành cần.

Nếu bước này sai, dashboard phía sau có thể vẫn trông rất đẹp nhưng con số không còn đáng tin.

## Data Serving

Khi data đã ở dạng ổn định, Data Analyst có thể làm dashboard, Data Scientist có thể xây mô hình dự đoán thời gian giao hàng, còn một dịch vụ nội bộ có thể dùng nó để cảnh báo nhà hàng đang quá tải.

Cùng một data ban đầu có thể phục vụ nhiều nhu cầu. Data Engineer không quyết định thay tất cả những người dùng đó, nhưng cần hiểu họ cần gì để thiết kế data phù hợp.

## Data Retention và Data Deletion

Theo thời gian, một phần data sẽ ít được truy cập hơn. Công ty có thể chuyển nó sang nơi lưu trữ rẻ hơn, đặt **Retention Period** hoặc xoá theo quy định về quyền riêng tư.

Ngoài ra còn có **Metadata**: data đến từ đâu, ai sở hữu, pipeline nào đã thay đổi nó và dashboard nào đang sử dụng nó. Khi hệ thống lớn lên, những thông tin này giúp mọi người lần ngược được một con số thay vì đoán.

## Bức tranh cần nhớ

Một data flow thường đi qua các bước:

**Source System → Data Ingestion → Data Storage → Data Transformation → Data Serving → Data Retention hoặc Data Deletion**

Ngoài đời, đường đi hiếm khi thẳng và gọn như sơ đồ này. Pipeline có thể chạy lỗi, data đến muộn, schema thay đổi hoặc người dùng cần một cách tính mới. Phần lớn công việc Data Engineering nằm ở việc xử lý những tình huống đó.
