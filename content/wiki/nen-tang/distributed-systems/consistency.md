---
title: "Tính nhất quán dữ liệu"
description: "Consistency: lời hứa nào cho một lần đọc?"
draft: false
contentType: "concept"
weight: 4
level: "beginner"
topics: ["distributed-systems"]
prerequisites: ["/wiki/nen-tang/distributed-systems/overview"]
related: []
---

Bạn đổi tên cửa hàng thành “Cà phê Góc Phố”, màn hình báo thành công, nhưng lần tải trang tiếp theo lại hiện tên cũ. Dữ liệu có thể đã ghi đúng ở một nơi và chưa tới nơi phục vụ lượt đọc. Nói hệ thống “nhất quán” cần chỉ rõ nó hứa điều gì với người đọc.

Đừng nhầm tính nhất quán giữa các bản sao với consistency trong [ACID]({{< relref "/wiki/nen-tang/database/acid.md" >}}), nơi mình nói về ràng buộc và trạng thái hợp lệ của giao dịch.

## Ba câu hỏi khác nhau

- Sau khi chính mình ghi, mình có đọc được thay đổi đó không? Đây là **read-your-writes**.
- Các lần đọc của mình có tránh đi lùi về phiên bản cũ hơn không? Đây là **monotonic reads**.
- Một lượt đọc bắt đầu sau khi một lượt ghi đã hoàn thành có phản ánh lượt ghi đó hoặc một ghi sau nó không? Đây là một hệ quả quan trọng của **linearizability**.

Hai đảm bảo đầu thường được xét trong một phiên người dùng. Chúng không tự đảm bảo mọi client cùng nhìn một trạng thái mới nhất.

## Kiểm tra một lịch đọc bằng tay

Giả sử chỉ có một lần ghi từ tên cũ sang tên mới, không có ghi cạnh tranh:

| Thời điểm | Việc xảy ra |
| --- | --- |
| 1 | A ghi tên mới, nhận thành công |
| 2 | A đọc replica chậm, thấy tên cũ |
| 3 | B đọc replica đã cập nhật, thấy tên mới |

Lịch này vi phạm read-your-writes của A và không phù hợp với linearizable register. Nó vẫn có thể phù hợp với eventual consistency nếu các bản sao cuối cùng hội tụ khi không có ghi mới và hệ thống truyền, giải quyết thay đổi như thiết kế.

Eventual consistency không tự nói “trong 5 giây”. Nếu cần độ cũ tối đa, phải đặt một cam kết và đo riêng. Hệ thống cũng cần cách xử lý các cập nhật cạnh tranh; “chờ một lúc” không tự chọn được phiên bản đúng.

## Chọn theo tác động tới người dùng

Một trang thống kê lượt xem có thể chấp nhận dữ liệu cũ. Kiểm tra tồn kho hoặc trạng thái vừa thanh toán có thể cần lời hứa mạnh hơn. Có thể đọc từ leader, truyền phiên bản cần thấy hoặc chờ replica bắt kịp, tùy hệ thống. Mỗi cách có ảnh hưởng tới độ trễ và khả năng phục vụ khi lỗi.

Không nên suy ra linearizability chỉ vì đọc từ leader: implementation còn phải bảo đảm leader có thẩm quyền và phản ánh các ghi đã commit.

Tham khảo định nghĩa linearizability trong [Gilbert và Lynch, mục 2.1](https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf), và một thiết kế xử lý các bản sao trong [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf). Đọc tiếp [CAP]({{< relref "/wiki/nen-tang/distributed-systems/cap-theorem.md" >}}).
