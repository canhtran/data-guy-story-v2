---
title: "Data Engineer xây những hệ thống gì?"
description: "Bức tranh tổng quan về pipeline, kho dữ liệu, nền tảng streaming và lớp dữ liệu phục vụ người dùng."
draft: true
contentType: "concept"
weight: 3
level: "beginner"
topics: ["bat-dau", "data-platform"]
prerequisites: ["du-lieu-di-qua-he-thong-nhu-the-nao"]
related: ["data-warehouse", "data-lake", "stream-processing", "orchestration"]
---

Nếu xem một Data Engineer như người xây hệ thống, câu hỏi tiếp theo sẽ là: hệ thống nào?

Câu trả lời thay đổi theo từng công ty. Một cửa hàng nhỏ chưa cần nền tảng streaming chạy hàng triệu event mỗi giây. Một công ty công nghệ lớn lại không thể vận hành mọi thứ bằng vài file CSV và một cron job. Dù quy mô khác nhau, phần lớn hệ thống dữ liệu vẫn có một số mảnh ghép quen thuộc.

## Pipeline đưa dữ liệu về

Pipeline kết nối hệ thống nguồn với nền tảng dữ liệu. Nguồn có thể là database của ứng dụng, API của đối tác, file do khách hàng gửi hoặc event từ Kafka.

Có pipeline chạy theo lịch, ví dụ lấy dữ liệu doanh thu vào mỗi đêm. Có pipeline xử lý liên tục vì kết quả cần xuất hiện trong vài giây. Việc chọn batch hay streaming phụ thuộc vào nhu cầu sử dụng, không phải công nghệ nào nghe hiện đại hơn.

Một pipeline dùng được lâu dài cần biết cách xử lý dữ liệu đến trễ, chạy lại sau khi lỗi và tránh tạo bản ghi trùng.

## Nơi lưu trữ dữ liệu

Data warehouse phù hợp với dữ liệu đã được tổ chức để truy vấn và báo cáo. Data lake có thể giữ khối lượng lớn dữ liệu ở nhiều định dạng. Lakehouse kết hợp một số đặc điểm của cả hai.

Tên gọi dễ làm mọi thứ có vẻ phức tạp. Câu hỏi thực tế hơn là:

- Dữ liệu nào cần được lưu?
- Ai sẽ dùng nó và họ truy vấn bằng cách nào?
- Cần giữ trong bao lâu?
- Mức độ chính xác và thời gian cập nhật ra sao?
- Chi phí lưu trữ và tính toán có chấp nhận được không?

Trả lời được những câu này rồi mới chọn kiến trúc và công nghệ.

## Lớp biến đổi và mô hình dữ liệu

Dữ liệu thô thường phản ánh cách application được xây, không phản ánh cách business đặt câu hỏi. Một hệ thống đơn hàng có thể chia thông tin qua hàng chục bảng, trong khi người phân tích chỉ cần một bảng doanh thu rõ ràng.

Data Engineer và Analytics Engineer viết các bước biến đổi để chuẩn hoá dữ liệu, thống nhất cách tính và tạo ra các mô hình dễ sử dụng. Đây cũng là nơi những khái niệm như ETL, ELT, fact và dimension xuất hiện.

## Hệ thống điều phối

Khi chỉ có hai pipeline, bạn có thể nhớ cái nào chạy trước. Khi có hai trăm pipeline, cần một hệ thống điều phối để biết job nào phụ thuộc job nào, chạy lúc nào và phải làm gì khi thất bại.

Airflow và Dagster là những ví dụ quen thuộc, nhưng công cụ không phải phần quan trọng nhất. Giá trị của lớp điều phối nằm ở việc làm cho quá trình xử lý có thứ tự, quan sát được và có thể chạy lại.

## Nền tảng streaming

Một số bài toán không thể chờ đến cuối ngày. Phát hiện giao dịch bất thường, cập nhật vị trí tài xế hay theo dõi hệ thống production thường cần dữ liệu gần thời gian thực.

Nền tảng streaming tiếp nhận và xử lý event liên tục. Kafka thường được dùng để vận chuyển và lưu giữ event; Flink hoặc Spark Structured Streaming có thể xử lý các luồng đó. Đổi lại, team phải giải quyết thêm những vấn đề như event đến sai thứ tự, xử lý trùng và quản lý state.

## Lớp phục vụ dữ liệu

Dữ liệu cuối cùng phải đến được nơi có người hoặc hệ thống sử dụng nó. Đầu ra có thể là bảng cho BI, dataset cho machine learning, API cho một sản phẩm nội bộ hoặc chỉ số dùng để cảnh báo.

Nếu không biết đầu ra phục vụ ai, team rất dễ xây một nền tảng nhiều công nghệ nhưng ít người dùng.

## Phần ít được nhìn thấy

Ngoài các luồng xử lý chính còn có monitoring, data quality, lineage, phân quyền, bảo mật và quản lý chi phí. Người mới thường ít nghe về chúng vì demo vẫn chạy được khi thiếu những phần này. Production thì không dễ tính như vậy.

Data Engineer không nhất thiết tự xây tất cả các hệ thống kể trên. Công việc có thể chỉ tập trung vào một vài phần. Tuy nhiên, hiểu chúng kết nối với nhau thế nào sẽ giúp bạn biết đoạn code mình đang viết nằm ở đâu trong bức tranh chung.
