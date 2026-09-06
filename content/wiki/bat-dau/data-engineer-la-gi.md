---
title: "Data Engineer là gì?"
description: "Data Engineer làm gì, chịu trách nhiệm cho phần nào của hệ thống dữ liệu và khác Data Analyst, Data Scientist ra sao?"
draft: false
contentType: "concept"
weight: 1
level: "beginner"
topics: ["bat-dau"]
prerequisites: []
related: ["data-pipeline", "data-warehouse", "data-quality"]
aliases:
  - "/docs/foundation/data-engineer-la-gi/"
---

Data Engineer là người xây dựng và vận hành hệ thống đưa dữ liệu từ nơi nó được tạo ra đến nơi nó có thể được sử dụng.

Nói vậy vẫn hơi chung chung. Thử lấy một ứng dụng đặt đồ ăn làm ví dụ. Mỗi ngày ứng dụng này sinh ra đơn hàng, thanh toán, vị trí tài xế, thông tin nhà hàng và log từ nhiều hệ thống khác nhau. Dữ liệu có rồi, nhưng nằm rải rác như vậy thì đội phân tích chưa thể dùng ngay được.

Data Engineer sẽ lo phần đường đi ở giữa: lấy dữ liệu từ các hệ thống nguồn, kiểm tra và biến đổi nó, đưa về nơi lưu trữ chung, rồi chuẩn bị dữ liệu ở dạng mà người khác có thể tin tưởng để sử dụng.

## Công việc cụ thể gồm những gì?

Tuỳ công ty, phạm vi công việc sẽ khác nhau. Nhưng một Data Engineer thường dành thời gian cho những việc sau:

- **Xây data pipeline:** đưa dữ liệu từ application, database, API hoặc event stream về hệ thống dữ liệu.
- **Thiết kế nơi lưu trữ:** tổ chức dữ liệu trong data warehouse, data lake hoặc lakehouse để có thể tìm và sử dụng lại.
- **Biến đổi dữ liệu:** chuẩn hoá định dạng, kết hợp nhiều nguồn và tạo ra các bảng dữ liệu phục vụ phân tích.
- **Kiểm tra chất lượng:** phát hiện dữ liệu thiếu, trùng, sai định dạng hoặc thay đổi bất thường.
- **Vận hành hệ thống:** theo dõi pipeline, xử lý lỗi, chạy lại dữ liệu và đảm bảo dữ liệu đến đúng thời điểm.
- **Quản lý hiệu năng và chi phí:** một pipeline chạy đúng nhưng quá chậm hoặc quá đắt vẫn chưa phải là một pipeline tốt.

Phần khó của công việc thường không nằm ở chuyện kéo dữ liệu từ A sang B. Nó nằm ở những câu hỏi xảy ra sau đó: Nếu pipeline chạy lỗi giữa chừng thì sao? Nếu schema của hệ thống nguồn thay đổi thì sao? Làm thế nào để chạy lại dữ liệu mà không tạo bản ghi trùng? Vì sao con số doanh thu hôm nay khác hôm qua?

## Một ngày làm việc có thể trông như thế nào?

Buổi sáng, bạn nhận cảnh báo một pipeline xử lý đơn hàng chạy trễ. Sau khi xem log, bạn phát hiện một bảng ở hệ thống nguồn vừa thêm cột mới làm job bị lỗi. Bạn sửa phần đọc dữ liệu, chạy bù khoảng thời gian còn thiếu và kiểm tra xem dashboard đã nhận đủ số liệu chưa.

Buổi chiều, bạn làm cùng Data Analyst để bổ sung cách tính khách hàng quay lại. Sau đó, bạn xem lại một pipeline Spark đang tốn quá nhiều tài nguyên và trao đổi với backend team về event mới họ chuẩn bị đưa lên Kafka.

Không phải ngày nào cũng giống vậy, nhưng ví dụ này cho thấy Data Engineer vừa viết code, vừa hiểu dữ liệu, vừa phải quan tâm đến cách hệ thống hoạt động khi có sự cố.

## Khác Data Analyst và Data Scientist ở đâu?

Ba vai trò cùng làm việc với dữ liệu nhưng thường chịu trách nhiệm cho những phần khác nhau:

| Vai trò | Câu hỏi thường gặp | Sản phẩm thường tạo ra |
| --- | --- | --- |
| **Data Engineer** | Làm sao để dữ liệu đầy đủ, đúng và đến đúng lúc? | Pipeline, bảng dữ liệu, nền tảng dữ liệu |
| **Data Analyst** | Dữ liệu đang cho thấy điều gì về hoạt động kinh doanh? | Phân tích, dashboard, báo cáo |
| **Data Scientist** | Có thể dùng dữ liệu để dự đoán hoặc tự động hoá quyết định không? | Mô hình thống kê, thí nghiệm, mô hình machine learning |

Đây là cách phân chia để dễ hình dung, không phải ranh giới cứng. Ở một công ty nhỏ, một người có thể vừa xây pipeline vừa làm dashboard. Ở công ty lớn, công việc còn có thể được tách thêm thành Analytics Engineer, Machine Learning Engineer hoặc Data Platform Engineer.

Tên chức danh đôi khi không nói hết được công việc. Khi đọc một job description, hãy nhìn vào hệ thống bạn sẽ xây, dữ liệu bạn sẽ chịu trách nhiệm và người sẽ sử dụng đầu ra của bạn.

## Data Engineer cần biết gì?

SQL và một ngôn ngữ lập trình, thường là Python hoặc Java, là điểm bắt đầu. Sau đó bạn sẽ cần hiểu database, data modeling, cách xử lý batch và streaming, cùng những kiến thức cơ bản về cloud và distributed systems.

Bạn không cần học hết mọi công cụ trước khi bắt đầu. Kafka, Spark, Flink hay Airflow chỉ giải quyết những nhóm vấn đề nhất định. Hiểu dữ liệu đi từ đâu, sẽ được dùng thế nào và có thể hỏng ở đâu quan trọng hơn việc nhớ thật nhiều tên công nghệ.

## Tóm lại

Data Engineer xây phần hạ tầng và luồng xử lý giúp dữ liệu có thể được sử dụng một cách ổn định. Công việc không chỉ là di chuyển dữ liệu, mà còn là giữ cho nó đúng, dễ hiểu, đến đúng lúc và có thể vận hành lâu dài.

Nếu bạn đang cân nhắc theo nghề này, hãy đọc tiếp [Học Data Engineering từ đâu?]({{< relref "/wiki/bat-dau/hoc-data-engineering-tu-dau.md" >}}).
