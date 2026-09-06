---
title: "Data đi qua một hệ thống như thế nào?"
description: "Theo dấu data của một đơn hàng từ Source System đến khi xuất hiện trên dashboard."
draft: false
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

Sơ đồ dưới đây là đường đi chúng ta sẽ theo trong bài:

```mermaid
flowchart TD
    A["1. Source System<br/>App tạo ra data"]
    B["2. Data Ingestion<br/>Đưa data về một nơi"]
    C["3. Data Storage<br/>Lưu data"]
    D["4. Data Transformation<br/>Làm sạch và kết hợp"]
    E["5. Data Serving<br/>Đưa data cho người dùng"]
    F["6. Retention / Deletion<br/>Lưu giữ hoặc xoá"]
    A --> B --> C --> D --> E --> F
```

## Data Generation

**Data Generation** (quá trình data được tạo ra) bắt đầu khi đơn hàng được đặt. Hệ thống có thể ghi lại mã đơn, nhà hàng, món ăn, giá tiền, phương thức thanh toán và thời gian tạo đơn. Trong lúc giao hàng, nó tiếp tục nhận vị trí tài xế và các lần thay đổi trạng thái.

Data này không nhất thiết nằm cùng một chỗ. Đơn hàng có thể nằm trong một database như MySQL. Kết quả thanh toán nằm trong hệ thống thanh toán, còn trạng thái giao hàng nằm trong hệ thống của tài xế.

Đây là các **Source System** (hệ thống nguồn). Chúng được xây để ứng dụng hoạt động, chứ không phải để trả lời mọi câu hỏi phân tích của công ty.

Khi bạn đặt món, application có thể thêm một row vào bảng `orders` trong MySQL:

| order_id | restaurant_id | status | total_amount | created_at |
| --- | --- | --- | ---: | --- |
| ORD-1042 | RES-18 | created | 120,000 | 2026-09-06 12:02:10 |

Khi nhà hàng nhận đơn hoặc tài xế giao hàng thành công, row này có thể được cập nhật sang trạng thái mới. Đây là data phục vụ hoạt động của application. Nó chưa được chuẩn bị để trả lời những câu hỏi như “Hôm nay có bao nhiêu đơn giao trễ?”.

## Data Ingestion

Đội vận hành muốn biết hôm nay có bao nhiêu đơn giao trễ. Đội tài chính cần đối soát thanh toán. Nhà hàng muốn xem món nào bán chạy. Nếu tất cả cùng truy vấn thẳng vào database của ứng dụng, họ có thể làm chậm hệ thống đang phục vụ khách hàng.

Vì vậy, data được sao chép từ các Source System về một nơi dành cho việc xử lý và phân tích. Quá trình này được gọi là **Data Ingestion** (thu thập và đưa data vào hệ thống).

Cùng một đơn hàng có thể đi vào nền tảng data qua nhiều đường:

| Source System | Data cần lấy | Khi nào lấy? |
| --- | --- | --- |
| MySQL của application | Đơn hàng và nhà hàng | Mỗi 5 phút |
| Hệ thống thanh toán | Kết quả thanh toán | Mỗi 15 phút |
| Hệ thống giao hàng | Trạng thái giao hàng | Mỗi 5 phút |

Sau Data Ingestion, mỗi nguồn vẫn cần giữ `order_id`. Nhờ đó, pipeline biết giao dịch thanh toán và chuyến giao hàng nào thuộc về `ORD-1042`.

## Data Storage

**Data Storage** (lưu trữ data) cho data một nơi để sống lâu hơn Source System. Tuỳ nhu cầu, nó có thể được lưu trong **Data Warehouse** (kho dữ liệu), **Data Lake** (hồ dữ liệu) hoặc **Lakehouse** (kiến trúc kết hợp Data Warehouse và Data Lake).

Ở thời điểm này, data chưa chắc đã dễ dùng. Tên nhà hàng có thể nằm trong một bảng, thông tin đơn hàng nằm ở bảng khác, còn data thanh toán dùng một mã định danh khác hoàn toàn.

Data của `ORD-1042` có thể được lưu ở ba lớp:

| Lớp | Ví dụ data | Mục đích |
| --- | --- | --- |
| Raw | Bản sao các row từ Source System | Giữ lại bản gốc để kiểm tra hoặc xử lý lại |
| Cleaned | Các row đúng cấu trúc, không trùng, thời gian đã chuẩn hoá | Tạo đầu vào ổn định cho các pipeline khác |
| Curated | Một row đơn hàng đã ghép thanh toán, nhà hàng và giao hàng | Phục vụ phân tích và sản phẩm data |

Không phải hệ thống nào cũng gọi ba lớp này bằng cùng một cái tên. Điều cần nhớ là data gốc và data đã qua xử lý thường được tách ra để tránh ghi đè lên nhau.

## Data Processing and Transformation

Trong bước này, **Data Processing** (xử lý data) và **Data Transformation** (biến đổi data) được dùng để kiểm tra, làm sạch và kết hợp data. Ví dụ, một pipeline có thể:

1. Loại những lần cập nhật bị gửi trùng.
2. Chuẩn hoá tất cả thời gian về cùng múi giờ.
3. Ghép đơn hàng với nhà hàng và giao dịch thanh toán.
4. Tính thời gian từ lúc đặt món đến lúc giao thành công.
5. Tạo một bảng chỉ gồm các chỉ số mà đội vận hành cần.

Nếu bước này sai, dashboard phía sau có thể vẫn trông rất đẹp nhưng con số không còn đáng tin.

Ví dụ, pipeline nhận được ba row sau:

| order_id | status | updated_at | delivery_fee |
| --- | --- | --- | ---: |
| ORD-1042 | delivered | 12:32:18 +08:00 | 18,000 |
| ORD-1042 | delivered | 12:32:18 +08:00 | 18,000 |
| ORD-1043 | delivered | 04:41:02 UTC | 22,000 |

Hai row đầu là cùng một lần cập nhật bị sao chép hai lần. Row cuối dùng UTC thay vì giờ Singapore. Sau khi loại trùng và chuẩn hoá timezone, pipeline mới tính được:

| delivery_date | delivered_orders | total_delivery_fee |
| --- | ---: | ---: |
| 2026-09-06 | 2 | 40,000 |

Nếu bỏ qua bước loại trùng, dashboard sẽ báo ba đơn và `58,000` tiền giao hàng dù thực tế chỉ có hai đơn.

## Data Serving

**Data Serving** (cung cấp data cho người dùng hoặc hệ thống khác) bắt đầu khi data đã ở dạng ổn định. Data Analyst có thể dùng nó để làm dashboard, Data Scientist có thể xây mô hình dự đoán thời gian giao hàng, còn một dịch vụ nội bộ có thể dùng nó để cảnh báo nhà hàng đang quá tải.

Cùng một data ban đầu có thể phục vụ nhiều nhu cầu. Data Engineer không quyết định thay tất cả những người dùng đó, nhưng cần hiểu họ cần gì để thiết kế data phù hợp.

Từ row của `ORD-1042`, các đầu ra có thể rất khác nhau:

| Người hoặc hệ thống sử dụng | Data được phục vụ |
| --- | --- |
| Operations dashboard | Số đơn giao trễ theo khu vực và nhà hàng |
| Finance report | Tổng tiền hàng, delivery fee và trạng thái đối soát |
| ETA model | Thời gian chuẩn bị món, quãng đường và thời gian giao thực tế |
| Alert service | Thông báo khi một đơn chờ tài xế quá lâu |

Data Serving vì vậy không chỉ có dashboard. Đầu ra cũng có thể là table, file hoặc API cho một hệ thống khác.

## Data Retention and Deletion

Theo thời gian, một phần data sẽ ít được truy cập hơn. **Data Retention** (lưu giữ data) quy định data cần được giữ trong bao lâu. Công ty có thể chuyển data cũ sang nơi lưu trữ rẻ hơn hoặc thực hiện **Data Deletion** (xoá data) theo quy định về quyền riêng tư.

Ngoài ra còn có **Metadata** (siêu dữ liệu): data đến từ đâu, ai sở hữu, pipeline nào đã thay đổi nó và dashboard nào đang sử dụng nó. Khi hệ thống lớn lên, những thông tin này giúp mọi người lần ngược được một con số thay vì đoán.

Ví dụ, công ty có thể áp dụng các quy tắc khác nhau cho từng loại data:

| Data | Retention | Sau thời hạn đó |
| --- | --- | --- |
| Vị trí chi tiết của tài xế | 30 ngày | Xoá |
| Lịch sử trạng thái đơn hàng | 1 năm | Chuyển sang storage rẻ hơn |
| Data tài chính cần đối soát | 7 năm | Archive theo quy định |

Metadata của bảng đơn hàng cũng có thể ghi rõ team nào chịu trách nhiệm, pipeline nào tạo ra bảng và dashboard nào đang sử dụng nó. Khi pipeline thay đổi, team biết cần kiểm tra những đầu ra nào.

## Bức tranh cần nhớ

Một data flow thường đi qua các bước:

**Source System → Data Ingestion → Data Storage → Data Transformation → Data Serving → Data Retention / Data Deletion**

Ngoài đời, đường đi hiếm khi thẳng và gọn như sơ đồ này. Pipeline có thể chạy lỗi, data đến muộn, schema thay đổi hoặc người dùng cần một cách tính mới. Phần lớn công việc Data Engineering nằm ở việc xử lý những tình huống đó.
