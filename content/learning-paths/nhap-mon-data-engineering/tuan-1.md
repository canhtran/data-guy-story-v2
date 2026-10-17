---
title: "Chặng 1: Gặp mentor và khám phá dữ liệu quán cà phê"
description: "Bản nháp trải nghiệm học theo tuần."
draft: true
type: docs
sidebar:
  hide: true
contentType: learning-module
weight: 1
---

<span class="dgs-status">Bản xem trước · chưa phải bài học hoàn chỉnh</span>

**Câu hỏi của chủ quán:** “Hôm qua quán bán được bao nhiêu, và vì sao em tin con số đó?”

Trong chặng đầu, bạn sẽ xem vài đơn hàng nhỏ, tự tính kết quả, sau đó dùng SQL để đối chiếu. AI hướng dẫn cài đặt và giải thích đúng lúc bạn cần. Bộ dữ liệu, lệnh cài đặt theo hệ điều hành và bài kiểm tra tự động chưa được phát hành; trang này trình bày trải nghiệm dự kiến.

## AI bắt đầu từ môi trường của bạn

Mentor hỏi bạn đang dùng hệ điều hành nào, đã cài Python và PostgreSQL chưa, rồi chọn hướng dẫn đã kiểm thử tương ứng. Mỗi lần, mentor đưa một thao tác, một lệnh kiểm tra và chờ kết quả trước khi đi tiếp. Nếu lỗi, bạn gửi lệnh và thông báo lỗi đã bỏ thông tin bí mật; mentor giúp kiểm tra nguyên nhân từng bước.

**Checkpoint cài đặt dự kiến:** ghi lại phiên bản công cụ và chứng minh có thể kết nối đến database cục bộ. Khi chưa có bộ lab chính thức, đừng dùng trang này như hướng dẫn cài đặt.

## Thử suy nghĩ trên một dữ liệu nhỏ

| order_id | status | amount_vnd |
| --- | --- | ---: |
| O-01 | completed | 40.000 |
| O-02 | cancelled | 50.000 |
| O-03 | completed | 60.000 |

Nếu doanh thu chỉ tính đơn hoàn tất, ba dòng này cho kết quả **100.000 VND từ 2 đơn**. Hãy tự tính trước khi nhìn đáp án. Nếu mỗi đơn có nhiều món, bạn còn cần biết mỗi dòng trong bảng món đại diện cho điều gì trước khi JOIN.

Bài Wiki có thể dùng khi trao đổi với mentor: [Data Engineer là gì?]({{< relref "/wiki/bat-dau/data-engineer-la-gi.md" >}}) và [Dữ liệu đi qua một hệ thống như thế nào?]({{< relref "/wiki/bat-dau/du-lieu-di-qua-he-thong-nhu-the-nao.md" >}}).

## Minh chứng hoàn thành dự kiến

Khi lab được phát hành, bạn sẽ chạy fixture và truy vấn cục bộ, giải thích vì sao đơn hủy không được tính, và ghi một điểm chưa rõ vào nhật ký học. AI xem kết quả bạn cung cấp, không tự tuyên bố đã chạy code trên máy bạn.

[Quay lại tổng quan lộ trình]({{< relref "/learning-paths/nhap-mon-data-engineering/_index.md" >}})
