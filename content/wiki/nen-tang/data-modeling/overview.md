---
title: "Mô hình hóa dữ liệu là gì?"
description: "Mô hình hóa dữ liệu: chọn mỗi dòng đại diện cho điều gì"
draft: false
contentType: "concept"
weight: 1
level: "beginner"
topics: ["data-modeling"]
prerequisites: []
related: []
---

Người quản lý hỏi “món nào bán tốt nhất?”. Nếu bảng chỉ có tổng tiền mỗi đơn, mình không trả lời được số ly từng món. Trước khi chọn tên bảng hay kiểu dữ liệu, cần biết những câu hỏi hệ thống phải trả lời và nguồn có đủ chi tiết không.

Mô hình hóa dữ liệu là cách tổ chức dữ liệu, quan hệ và quy tắc để phục vụ việc sử dụng. Bài này tập trung mô hình cho phân tích, không thay thế thiết kế database của ứng dụng.

## Bắt đầu từ grain

Grain nghĩa là **mỗi dòng đại diện cho điều gì**. Ví dụ giả lập: một đơn 501 có hai dòng hàng:

| order_id | line_no | product | quantity | net_amount_vnd |
| --- | --- | --- | --- | --- |
| 501 | 1 | Cà phê đen | 2 | 40000 |
| 501 | 2 | Latte | 1 | 35000 |

Mỗi dòng là một dòng sản phẩm trong đơn, khóa `(order_id, line_no)`. Tổng đơn là **75000 đồng**, số ly là **3**, số đơn là **1**. `COUNT(*)` trả 2 dòng hàng, không phải 2 đơn.

Nếu thêm `order_total_vnd = 75000` vào cả hai dòng rồi cộng, báo cáo thành 150000. Một cột có thể đúng trên từng dòng nhưng không phù hợp để cộng ở grain này.

## Từ câu hỏi đến cấu trúc

Mình thường ghi bốn điều trước: hoạt động nào cần theo dõi, mỗi dòng là gì, dùng thuộc tính nào để phân nhóm, và đo lường nào cần tính. Với bán hàng, thuộc tính có thể là món, cửa hàng, ngày; đo lường là số lượng và tiền sau giảm giá.

Cần viết thêm quy tắc: có tính đơn hủy không, hoàn tiền vào ngày nào, giảm giá cấp đơn chia xuống dòng hàng thế nào? Schema không tự trả lời những câu hỏi này. Thống nhất với người dùng báo cáo trước khi code giúp tránh “truy vấn đúng nhưng định nghĩa sai”.

## Chi tiết và bảng tổng hợp

Dữ liệu theo dòng hàng trả lời được nhiều câu hỏi hơn tổng mỗi ngày, nhưng lớn hơn và cần kiểm soát quyền. Bảng tổng hợp giúp đọc nhanh, song không thể khôi phục chi tiết đã bỏ mất. Có thể giữ cả hai khi cần, với một quy trình đối chiếu để tổng không lệch.

Một bài tập nhỏ: nếu bảng chỉ còn một dòng ngày 01/09 với doanh thu 75000, bạn có tính được số ly Latte không? Không, vì thông tin sản phẩm đã mất.

Đọc tiếp [fact và dimension]({{< relref "/wiki/nen-tang/data-modeling/fact-and-dimension.md" >}}). Tham khảo: [Kimball: four-step design process](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/four-4-step-design-process/).
