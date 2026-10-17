---
title: "Watermark trong Flink: khi nào cửa sổ được tiến lên?"
description: "Hiểu tiến độ event time, input im lặng và dữ liệu đến muộn."
draft: false
contentType: "concept"
weight: 9
level: "beginner"
topics: ["flink"]
prerequisites: []
related: []
---

Cửa sổ 10:00–10:05 đã qua trên đồng hồ máy nhưng Flink chưa xuất kết quả. Một input có thể chưa phát watermark đủ cao. Event-time processing cần một tín hiệu tiến độ từ dữ liệu, không chỉ từ đồng hồ máy.

## Watermark không phải lời hứa không còn dữ liệu muộn

Watermark biểu diễn tiến độ event time theo chính sách ứng dụng/source. Ví dụ chiến lược cho phép out-of-orderness hai phút tạo tiến độ dựa trên timestamp lớn nhất đã thấy trừ khoảng chờ. Dữ liệu cũ vẫn có thể đến sau đó; ứng dụng phải chọn nhận cập nhật, đưa sang side output hoặc loại theo chính sách.

## Input chậm giữ watermark chung

Bài tập minh họa, giả sử operator có hai input đang hoạt động:

| Input | Watermark |
| --- | --- |
| P0 | 10:08 |
| P1 | 10:03 |

Watermark downstream lấy mức chậm nhất là 10:03. Chỉ P0 tiến lên 10:10 vẫn chưa kéo downstream vượt P1. Nếu P1 im lặng, cấu hình idleness phù hợp có thể loại input idle khỏi phép lấy minimum; khi dữ liệu của P1 quay lại, các record cũ có thể bị coi là muộn.

## Window và allowed lateness

Với cửa sổ `[10:00,10:05)`, khi watermark vượt qua timestamp cuối cửa sổ, event-time trigger có thể phát kết quả. Với allowed lateness dương, một số state còn được giữ thêm để nhận cập nhật. Kết quả ban đầu không nhất thiết là kết quả cuối.

Giả sử cửa sổ đã emit tổng 40000 và chính sách vẫn chấp nhận một đơn muộn 35000. Tổng cập nhật là 75000; sink cần hiểu đó là cập nhật, không cộng thêm một “cửa sổ mới” 75000 vào tổng cũ. Nếu state đã bị dọn, chính sách có thể đưa record sang luồng late-data thay vì sửa tổng.

## Chẩn đoán

Theo dõi watermark của source/operator, timestamp cực trị, input idle và tốc độ ingest. Một record timestamp ở tương lai xa có thể làm watermark tiến sai và khiến dữ liệu hợp lệ bị muộn. Tăng allowed lateness làm state giữ lâu hơn; không miễn phí về bộ nhớ.

Bài này đối chiếu Flink 1.20.3, dùng watermark minh họa có thể kiểm tra bằng tay; không mô phỏng thuật toán phát watermark theo chu kỳ hay độ lệch một mili giây ở runtime.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — generating_watermarks](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/event-time/generating_watermarks/) là nguồn đối chiếu cơ chế trong bài.

[Windows và allowed lateness](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/operators/windows/) mô tả trigger, cleanup và xử lý dữ liệu muộn.
