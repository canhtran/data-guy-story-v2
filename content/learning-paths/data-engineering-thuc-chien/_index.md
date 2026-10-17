---
title: Data Engineering thực chiến
description: Xây kho dữ liệu phân tích nhiều nguồn trên máy của bạn.
draft: false
type: docs
sidebar:
  hide: true
contentType: learning-path
weight: 2
cascade:
  type: docs
---

<span class="dgs-status">Lên kế hoạch · chưa mở bài học</span>

{{< learning-free-note >}}

Bạn sẽ biến nhiều nguồn dữ liệu thay đổi thành một kho dữ liệu phân tích có thể kiểm tra và phục hồi. Đây là bước tiếp theo sau [Nhập môn Data Engineering]({{< relref "/learning-paths/nhap-mon-data-engineering/_index.md" >}}).

## Phù hợp với ai?

Bạn đã xây được một pipeline nhỏ bằng SQL và Python, biết kiểm tra số liệu và chạy lại một ngày dữ liệu. Người có kinh nghiệm tương đương có thể làm bài kiểm tra đầu vào khi học liệu được phát hành.

## Bạn sẽ làm được gì?

Xác định chỉ số từ yêu cầu nghiệp vụ; thu thập thay đổi từ nhiều nguồn; mô hình bảng fact, dimension và lịch sử; điều phối job; kiểm tra chất lượng; điều tra số liệu lệch và phục hồi sau lỗi.

**Nhịp học dự kiến:** 8 tuần, 8–10 giờ mỗi tuần, gồm 6 chặng dẫn đường và 2 tuần dự án cuối khóa. Thời lượng sẽ được kiểm chứng bằng thử nghiệm với người học.

## Dự án dẫn đường

Một chuỗi cà phê ba cửa hàng có dữ liệu bán hàng, thanh toán, hoàn tiền và lịch sử cửa hàng. Bạn xây kho dữ liệu để trả lời “Hôm qua bán bao nhiêu, tiền thu có khớp không, và số nào vẫn đang chờ dữ liệu?” PostgreSQL, dbt và Airflow chạy trên máy của bạn. AI hướng dẫn cài đặt từng bước và giúp debug bằng lệnh, log, kết quả bạn chia sẻ.

## Các chặng học

1. Từ yêu cầu đến metric, grain và bản báo cáo đầu tiên.
2. Thu thập dữ liệu thay đổi và chạy lại an toàn.
3. Mô hình fact, dimension và lịch sử cửa hàng.
4. Kiểm tra chất lượng, xử lý dữ liệu đến muộn và backfill.
5. Điều phối, theo dõi độ mới và phục hồi job.
6. Đóng gói, triển khai cục bộ và bàn giao cách vận hành.
7–8. Chọn dự án cuối khóa, xây và bảo vệ kết quả.

## Dự án cuối khóa

Chọn **cửa hàng online**, **vận hành giao hàng** hoặc **workshop**. AI giúp xác định brief; bạn tự xây pipeline, kiểm chứng số liệu, thử một tình huống lỗi và giải thích quyết định thiết kế.

## Tình trạng học liệu

Đề cương đã có, nhưng bài học, bộ dữ liệu, lệnh cài đặt và gói nguồn AI đang được biên soạn. Trang này là bản giới thiệu, chưa phải nút bắt đầu học.

[Trở lại danh sách lộ trình]({{< relref "/learning-paths/_index.md" >}})

## Học cùng NotebookLM

{{< notebook-link path="data-engineering-thuc-chien" >}}
