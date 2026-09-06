---
title: "Học Data Engineering từ đâu?"
description: "Cách chọn điểm bắt đầu, thứ tự kiến thức và một số điều chưa cần học ngay khi bước vào Data Engineering."
draft: true
contentType: "concept"
weight: 6
level: "beginner"
topics: ["bat-dau"]
prerequisites: ["data-engineer-la-gi", "du-lieu-di-qua-he-thong-nhu-the-nao"]
related: ["data-engineer-foundation"]
---

Người mới tìm hiểu Data Engineering rất dễ mở cùng lúc mười tab: Python, SQL, Docker, Airflow, Spark, Kafka, AWS, Kubernetes… Sau một hồi, thứ rõ ràng nhất lại là cảm giác mình không biết gì.

Bạn không cần học tất cả những thứ đó để bắt đầu. Điều cần trước tiên là một thứ tự hợp lý.

## Bắt đầu bằng SQL

Phần lớn công việc với dữ liệu vẫn quay về chuyện đọc, kết hợp, tổng hợp và kiểm tra các bảng. SQL vì thế là kỹ năng có ích sớm nhất.

Ở giai đoạn đầu, hãy học chắc:

- `SELECT`, `WHERE`, `GROUP BY` và các hàm tổng hợp.
- Các kiểu `JOIN` và điều gì xảy ra khi khoá không duy nhất.
- CTE và window function.
- Cách đọc execution plan ở mức cơ bản.
- Cách kiểm tra kết quả thay vì chỉ thấy query chạy thành công.

Bạn chưa cần thuộc mọi cú pháp. Mục tiêu là nhìn một bộ dữ liệu và biết cách đặt câu hỏi bằng SQL.

## Học một ngôn ngữ lập trình đủ dùng

Python là lựa chọn dễ bắt đầu vì được dùng rộng rãi trong data tooling. Java hoặc Scala trở nên quan trọng hơn ở một số hệ thống lớn, nhưng không cần học cả ba cùng lúc.

Với Python, hãy tập trung vào những phần phục vụ công việc:

- Đọc và ghi file, gọi API, kết nối database.
- Hàm, module, package và quản lý dependency.
- Xử lý lỗi và ghi log.
- Viết test cho logic biến đổi quan trọng.
- Làm việc với cấu trúc dữ liệu và dữ liệu lớn hơn bộ nhớ ở mức khái niệm.

Một project nhỏ chạy từ đầu đến cuối có giá trị hơn nhiều notebook rời rạc.

## Hiểu database trước khi học hệ thống dữ liệu lớn

Hãy biết dữ liệu được lưu trong bảng như thế nào, transaction giải quyết vấn đề gì, index giúp gì và vì sao một query có thể chậm. Những kiến thức này tiếp tục xuất hiện trong warehouse, pipeline và distributed systems dưới nhiều hình thức khác nhau.

Bạn có thể thực hành với PostgreSQL trên máy cá nhân. Một database nhỏ đủ để học phần lớn khái niệm nền tảng.

## Tự xây một pipeline đơn giản

Chọn một API công khai hoặc một file dữ liệu, viết chương trình lấy dữ liệu về, kiểm tra nó rồi lưu vào PostgreSQL. Sau đó viết vài query để trả lời một câu hỏi cụ thể.

Project đầu tiên chỉ cần có:

1. Một nguồn dữ liệu.
2. Một bước thu thập.
3. Một vài quy tắc làm sạch.
4. Một nơi lưu trữ.
5. Một đầu ra có người đọc được.

Sau khi chạy được, hãy thử chạy lần hai. Nếu data bị nhân đôi, pipeline chưa có **Idempotency** (khả năng chạy lại nhiều lần mà không tạo thêm kết quả ngoài ý muốn). Thử làm API lỗi giữa chừng, thay đổi một cột hoặc gửi data thiếu. Đây là lúc project bắt đầu dạy bạn cách pipeline thật sự vận hành.

## Học data modeling và chất lượng dữ liệu

Đưa dữ liệu vào database mới là nửa đầu công việc. Người khác còn phải hiểu và tin được nó.

Hãy học cách tách dữ liệu thô khỏi dữ liệu đã xử lý, chọn grain cho một bảng, hiểu fact và dimension, rồi thêm các kiểm tra như khoá không được rỗng, giá trị phải nằm trong khoảng hợp lệ hoặc số bản ghi không giảm bất thường.

## Chỉ thêm công cụ khi project cần

Khi có nhiều job và dependency, hãy tìm hiểu một orchestrator như Airflow. Khi dữ liệu không còn xử lý tốt trên một máy, hãy học Spark. Khi bài toán cần event liên tục và độ trễ thấp, hãy tìm hiểu Kafka và Flink.

Học theo vấn đề giúp bạn hiểu vì sao công cụ tồn tại. Nếu bắt đầu từ việc cài một stack thật lớn, bạn có thể chạy được demo nhưng khó biết nên dùng nó lúc nào.

## Cloud, Docker và distributed systems

Bạn nên biết Docker cơ bản để tạo môi trường có thể chạy lại. Cloud cũng đáng học vì nhiều hệ thống dữ liệu được triển khai ở đó. Tuy vậy, đừng biến chứng chỉ cloud thành điều kiện để bắt đầu viết pipeline đầu tiên.

Distributed systems là phần cần học dần. Replication, partitioning, consistency và fault tolerance sẽ dễ hiểu hơn khi bạn đã gặp giới hạn của một database hoặc một máy xử lý.

## Một thứ tự gợi ý

Nếu cần một danh sách ngắn, hãy đi theo thứ tự này:

1. SQL.
2. Python và Git.
3. Database.
4. Một pipeline nhỏ chạy end-to-end.
5. Data modeling và data quality.
6. Orchestration và cloud cơ bản.
7. Batch processing, streaming và distributed systems khi bài toán yêu cầu.

Đây là định hướng để chọn điểm bắt đầu. Phần **Lộ trình học** sẽ chia nội dung thành từng chặng và liên kết đến các bài tương ứng trong Sổ tay.
