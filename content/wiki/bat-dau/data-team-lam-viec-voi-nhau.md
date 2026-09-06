---
title: "Một data team làm việc với nhau như thế nào?"
description: "Data Engineer phối hợp với Analyst, Scientist, Backend, Platform và business trong công việc thực tế."
draft: true
contentType: "concept"
weight: 4
level: "beginner"
topics: ["bat-dau", "data-team"]
prerequisites: ["data-engineer-la-gi"]
related: []
---

Sơ đồ tổ chức thường vẽ mỗi vai trò trong một ô riêng. Công việc thực tế lại diễn ra ở khoảng trống giữa các ô đó.

Giả sử công ty muốn biết vì sao tỷ lệ huỷ đơn tăng trong tuần vừa rồi. Đây không chỉ là việc của Data Analyst. Để trả lời được, nhiều người phải cùng góp một phần.

## Business nói rõ câu hỏi

Đội vận hành biết “đơn bị huỷ” có thể mang nhiều nghĩa: khách tự huỷ, nhà hàng từ chối, không tìm được tài xế hoặc hệ thống tự đóng đơn. Họ cũng biết quyết định nào sẽ được đưa ra sau khi có kết quả.

Nếu không làm rõ từ đầu, data team có thể dành vài ngày để tạo một con số đúng về kỹ thuật nhưng không trả lời được câu hỏi thật.

## Backend Engineer tạo dữ liệu ở nguồn

Backend Engineer xây luồng đặt và huỷ đơn trong application. Họ biết event được tạo ở đâu, trạng thái nào có thể xảy ra và database thay đổi ra sao.

Data Engineer cần làm việc với backend khi bổ sung event, thay đổi schema hoặc phát hiện dữ liệu nguồn có vấn đề. Một data contract rõ ràng sẽ giúp hai bên thống nhất tên trường, ý nghĩa và cách xử lý thay đổi.

## Data Engineer chuẩn bị dữ liệu đáng tin

Data Engineer đưa dữ liệu đơn hàng và trạng thái huỷ về nền tảng dữ liệu, xử lý các event trùng hoặc đến muộn, rồi tạo ra bảng mà người phân tích có thể sử dụng.

Họ cũng thêm kiểm tra để biết dữ liệu có bị thiếu và theo dõi thời điểm pipeline hoàn tất. Nếu dữ liệu hôm nay mới chỉ về một nửa, dashboard cần thể hiện điều đó thay vì lặng lẽ đưa ra kết quả sai.

## Data Analyst biến câu hỏi thành phân tích

Data Analyst thống nhất cách tính tỷ lệ huỷ, tìm xu hướng theo nhà hàng, khu vực và thời gian, rồi đặt kết quả vào bối cảnh kinh doanh.

Trong quá trình làm, Analyst có thể phát hiện cần thêm một thuộc tính chưa có trong bảng. Hai bên sẽ cùng quyết định nên bổ sung vào mô hình dùng chung hay chỉ xử lý trong một phân tích riêng.

## Data Scientist và Machine Learning Engineer

Nếu công ty muốn dự đoán đơn nào có nguy cơ bị huỷ, Data Scientist có thể thử nghiệm mô hình từ dữ liệu lịch sử. Machine Learning Engineer giúp đưa mô hình vào production, theo dõi chất lượng dự đoán và phục vụ kết quả cho application.

Data Engineer thường chuẩn bị feature hoặc pipeline đầu vào. Ranh giới giữa các vai trò tuỳ thuộc vào cách công ty tổ chức team.

## Platform, DevOps và Security

Các team này cung cấp hạ tầng, quy trình triển khai, monitoring, phân quyền và tiêu chuẩn bảo mật. Ở công ty nhỏ, Data Engineer có thể tự làm khá nhiều phần trong số đó. Ở công ty lớn, trách nhiệm được chia rõ hơn nhưng vẫn cần phối hợp thường xuyên.

Ví dụ, việc đưa dữ liệu cá nhân vào warehouse không chỉ là một task ingestion. Team còn phải thống nhất ai được truy cập, dữ liệu được giữ bao lâu và thông tin nào cần che đi.

## Ai sở hữu dữ liệu?

Đây thường là câu hỏi khó hơn chuyện chọn Kafka hay Spark. Backend team hiểu dữ liệu nguồn nhưng không phải lúc nào cũng biết nó được dùng ở đâu. Data team tạo bảng phân tích nhưng không thể tự quyết định mọi định nghĩa business.

Một cách làm thực tế là phân chia rõ:

- Ai chịu trách nhiệm cho dữ liệu ở nguồn.
- Ai duy trì pipeline và bảng dữ liệu.
- Ai định nghĩa chỉ số business.
- Ai cần được báo khi dữ liệu thay đổi hoặc gặp sự cố.

Một data team làm việc tốt không phải vì mỗi người ở đúng một ô trong sơ đồ. Họ làm việc tốt vì cùng hiểu dữ liệu đang phục vụ quyết định nào, trách nhiệm chuyển giao ở đâu và phải tìm ai khi có vấn đề.
