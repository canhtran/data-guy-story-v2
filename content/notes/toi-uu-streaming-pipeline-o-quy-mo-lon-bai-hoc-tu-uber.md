---
title: "Tối ưu Streaming Pipeline ở quy mô lớn: Bài học từ Uber"
date: 2026-10-25
draft: false
description: "Phân tích cách Uber tối ưu Apache Flink pipeline để xử lý dữ liệu demand và supply gần thời gian thực, từ backpressure, memory đến sliding window."
tags:
  - Apache Flink
  - Stream Processing
  - Data Engineering
contentType: note
note_type: analysis
original_title: "Building Scalable Streaming Pipelines for Near Real-Time Features"
source_url: "https://www.uber.com/us/en/blog/building-scalable-streaming-pipelines/"
source_publisher: "Uber Engineering"
source_author: "Feng Xu và Gang Zhao"
source_published: "24/08/2021"
---

Bài viết mẫu này dựa trên bài viết kỹ thuật của Uber Engineering: [Building Scalable Streaming Pipelines for Near Real-Time Features](https://www.uber.com/us/en/blog/building-scalable-streaming-pipelines/).

Mục tiêu là tìm hiểu cách một hệ thống streaming xử lý khối lượng dữ liệu lớn, vì sao pipeline ban đầu gặp vấn đề về hiệu năng và những hướng tối ưu mà đội ngũ Uber đã áp dụng.

> **Lưu ý:** Đây là bài phân tích mẫu dùng để thử nghiệm giao diện Notes. Phần nhận xét và câu hỏi cuối bài là nội dung gợi ý, cần được kiểm tra và chỉnh sửa trước khi xuất bản chính thức.

## 1. Bài toán Uber đang giải quyết

Uber sử dụng dữ liệu gần thời gian thực để hỗ trợ các mô hình machine learning, chẳng hạn như dự báo nhu cầu và nguồn cung trong hệ thống marketplace.

Một phần của hệ thống này sử dụng Apache Kafka để tiếp nhận sự kiện và Apache Flink để tính toán các feature trước khi lưu trữ, phục vụ những hệ thống phía sau.

Bài toán không chỉ là đếm sự kiện. Pipeline còn phải tổng hợp dữ liệu theo vị trí địa lý, loại sản phẩm và nhiều khoảng thời gian khác nhau.

Một số con số được đề cập trong bài viết gốc:

| Chỉ số | Giá trị |
| --- | ---: |
| Tốc độ dữ liệu Kafka đầu vào trung bình | 120.000 events/giây |
| Số lượng hexagon được quản lý | 5 triệu |
| Số lượng thành phố | 1.500 |
| Số khoảng thời gian cần tính toán | 6 |
| Khoảng thời gian dài nhất | 32 phút |
| Số feature tạo ra cho mỗi hexagon mỗi phút | 54 |

Với quy mô này, chi phí xử lý dữ liệu trung gian, trao đổi dữ liệu giữa các operator và quản lý state đều có thể trở thành vấn đề đáng kể.

## 2. Pipeline ban đầu gặp vấn đề gì?

Đội ngũ Uber triển khai phiên bản đầu tiên theo logical DAG của thuật toán. Tuy nhiên, pipeline không chạy ổn định do các vấn đề như **backpressure** và **out-of-memory (OOM)**.

Mục tiêu là giữ độ trễ ở mức dưới 5 phút, nên chỉ tăng tài nguyên chưa chắc đã giải quyết được toàn bộ vấn đề.

Điều đáng chú ý là một pipeline có logic tính toán đúng vẫn có thể không phù hợp để chạy ở quy mô lớn.

Ví dụ, nếu nhiều operator liên tục tạo ra các bản ghi trung gian lớn, hệ thống phải tiêu tốn thêm CPU và network để serialize, truyền và deserialize chúng. Nếu một operator xử lý chậm hơn các operator phía trước, dữ liệu có thể tích tụ và tạo ra backpressure.

Đây là lý do cần xem xét cả cách tổ chức pipeline lẫn chi phí xử lý của từng bước.

## 3. Các hướng tối ưu đáng chú ý

### 3.1. Giảm lượng dữ liệu trước khi tăng tài nguyên

Một hướng tối ưu là giảm kích thước và số lượng message mà pipeline phải xử lý.

Uber áp dụng một số kỹ thuật:

- **Loại bỏ field không cần thiết:** lọc các field không được sử dụng ngay từ đầu pipeline.
- **Tối ưu kiểu dữ liệu:** thay đổi kiểu dữ liệu trung gian từ `Double` sang `Integer` khi phù hợp với phép tính.
- **Tối ưu key:** mã hóa một số giá trị UUID thành biểu diễn nhỏ hơn trong quá trình xử lý.
- **Giảm overhead của object:** tận dụng object reuse khi phù hợp.

Theo bài viết, việc thay đổi kiểu dữ liệu giúp kích thước message giảm từ 451 bytes xuống 237 bytes.

Mức giảm này có ý nghĩa vì dữ liệu trung gian có thể được truyền qua nhiều operator. Một tối ưu nhỏ trên mỗi message có thể tạo ra tác động đáng kể khi số lượng message rất lớn.

### 3.2. Dedup trước bước tính toán tốn kém

Trong pipeline này, bước Kring Smooth thực hiện phép tổng hợp theo các hexagon lân cận. Đây là một bước tính toán tốn kém.

Uber bổ sung bước dedup theo rider trong cửa sổ một phút trước khi thực hiện Kring Smooth. Theo bài viết, tốc độ message đi vào bước tính toán này giảm từ khoảng 120.000 xuống còn 8.000 message/giây.

Tuy nhiên, tối ưu này có một đánh đổi: cửa sổ dedup bổ sung khoảng một phút độ trễ.

Đây là ví dụ rõ ràng cho thấy tối ưu streaming không chỉ là làm cho một operator chạy nhanh hơn. Cần xem xét cả số lượng dữ liệu, độ trễ đầu ra và yêu cầu của ứng dụng.

### 3.3. Thay đổi cách triển khai sliding window

Pipeline cần tạo feature cho sáu khoảng thời gian: 1, 2, 4, 8, 16 và 32 phút.

Trong thiết kế ban đầu, các cửa sổ lớn hơn một phút là sliding window, trượt theo từng phút. Vì vậy, một sự kiện có thể tham gia vào nhiều cửa sổ thời gian khác nhau.

Cách triển khai này tạo ra nhiều công việc và dữ liệu trung gian.

Sau khi tối ưu, Uber thay các window operator lớn bằng một **customized sliding window**, được triển khai thông qua `FlatMap` và state trong bộ nhớ.

Thay vì dựa hoàn toàn vào nhiều window operator riêng biệt, cách triển khai tùy chỉnh giúp đội ngũ kiểm soát tốt hơn cách lưu trữ và cập nhật dữ liệu cho các cửa sổ.

Đây là một hướng tối ưu đáng tìm hiểu khi xử lý streaming ở quy mô lớn. Tuy nhiên, custom operator cũng làm tăng độ phức tạp trong việc triển khai, kiểm thử và bảo trì.

### 3.4. Tối ưu cả network, CPU và memory

Uber sử dụng một framework tối ưu hiệu năng tập trung vào ba nhóm tài nguyên chính:

| Nhóm | Những vấn đề cần kiểm tra |
| --- | --- |
| Network | Kích thước message, serialization, partitioning và dữ liệu truyền giữa các operator |
| CPU | Chi phí thuật toán, boxing/unboxing, cách truy cập dữ liệu và overhead của object |
| Memory | Kích thước state, object allocation, garbage collection và parallelism |

Cách tiếp cận này giúp tránh việc chỉ nhìn vào một chỉ số, chẳng hạn CPU utilization, rồi tăng parallelism mà chưa xác định đúng bottleneck.

Ví dụ, nếu partitioning là nút thắt, tăng số lượng worker chưa chắc giải quyết được vấn đề. Nếu lượng dữ liệu trung gian quá lớn, giảm kích thước message có thể hiệu quả hơn việc tiếp tục tăng tài nguyên.

## 4. Những bài học rút ra

### Bài học 1: Tối ưu data movement có thể quan trọng ngang với tối ưu thuật toán

Khi dữ liệu đi qua nhiều operator, chi phí serialize, deserialize và truyền message có thể tích lũy nhanh chóng.

Vì vậy, giảm số lượng message và kích thước mỗi message là những hướng cần xem xét sớm.

### Bài học 2: Tìm bottleneck trước khi tăng parallelism

Tăng parallelism có thể giúp tăng throughput, nhưng cũng có thể làm tăng chi phí quản lý state, trao đổi dữ liệu và tài nguyên.

Trước khi điều chỉnh cấu hình, cần xác định vấn đề nằm ở CPU, network, memory, partitioning hay hệ thống bên ngoài.

### Bài học 3: Đôi khi cần thay đổi cách biểu diễn thuật toán

Nếu cách triển khai trực tiếp theo logical DAG tạo ra quá nhiều overhead, có thể cần thiết kế lại cách xử lý dữ liệu trung gian.

Custom operator là một lựa chọn, nhưng chỉ nên áp dụng khi lợi ích hiệu năng đủ lớn để bù cho chi phí phát triển và bảo trì.

### Bài học 4: Kiểm thử tính đúng đắn trong suốt quá trình tối ưu

Uber đề cập đến việc sử dụng end-to-end integration test trước khi thực hiện các vòng tối ưu hiệu năng.

Điều này đặc biệt quan trọng khi thay đổi cách tính window, quản lý state hoặc gộp nhiều bước xử lý. Pipeline chạy nhanh hơn nhưng tạo ra kết quả sai thì không phải là một tối ưu thành công.

## 5. Những câu hỏi đáng tìm hiểu thêm

Nếu muốn đào sâu hơn vào bài toán này, có thể bắt đầu với các câu hỏi sau:

1. Trong Apache Flink, làm thế nào để phân biệt backpressure do CPU, network hay một operator xử lý chậm?
2. Custom sliding window cần quản lý state như thế nào để xử lý checkpoint và recovery an toàn?
3. Khi tự triển khai window logic, cần kiểm tra những trường hợp nào liên quan đến event time, late events và dữ liệu đến không đúng thứ tự?
4. Làm thế nào để đo lường tác động thực tế của object reuse và thay đổi kiểu dữ liệu?
5. Khi nào custom operator đáng để sử dụng thay vì các window operator có sẵn của Flink?

Đây cũng là những câu hỏi hữu ích khi đọc một bài viết tối ưu hiệu năng: không chỉ ghi nhớ giải pháp, mà còn hiểu vấn đề nào khiến giải pháp đó trở nên cần thiết.

## Nguồn tham khảo

- Feng Xu và Gang Zhao, Uber Engineering — [Building Scalable Streaming Pipelines for Near Real-Time Features](https://www.uber.com/us/en/blog/building-scalable-streaming-pipelines/), 24/08/2021.

---
