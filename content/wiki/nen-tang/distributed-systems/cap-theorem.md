---
title: "Định lý CAP"
description: "CAP: điều gì xảy ra khi các node mất liên lạc?"
draft: false
contentType: "concept"
weight: 5
level: "beginner"
topics: ["distributed-systems"]
prerequisites: ["/wiki/nen-tang/distributed-systems/overview"]
related: []
---

Hai node giữ trạng thái một đơn hàng. Mạng giữa chúng bị ngắt, nhưng mỗi node vẫn nhận yêu cầu từ client. Node A chấp nhận đổi trạng thái sang `paid`. Node B không nhận được thay đổi. Nếu B vẫn phải trả lời lượt đọc, nó biết gì để trả đúng trạng thái mới?

CAP nêu một giới hạn: trong mô hình có thể bị network partition, không thể đồng thời đảm bảo linearizable consistency và availability cho mọi yêu cầu tại node không lỗi. Xem định nghĩa và chứng minh trong [Gilbert và Lynch](https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf).

## Dùng ví dụ để nhìn lựa chọn

Với trạng thái ban đầu `pending`, không có ghi khác:

- A đã xác nhận ghi `paid`; sau đó client đọc ở B.
- Nếu B trả `pending`, lượt đọc không phù hợp với linearizability.
- Nếu B chờ trao đổi với A, lượt đọc có thể không hoàn thành khi mạng vẫn bị chia cắt.

Trả lỗi “không thể đọc lúc này” có thể là hành vi sản phẩm hợp lý, nhưng không phải một lượt đọc thành công đáp ứng availability theo ý nghĩa của định lý. Availability trong CAP cũng không phải con số uptime 99.9% mà mình dùng cho vận hành.

## “Chọn hai trong ba” dễ làm mình hiểu sai

Network partition là một kiểu lỗi phải tính đến, không phải một tính năng có thể tắt để database được cả C và A trong mọi tình huống. Câu hỏi hữu ích là hệ thống ưu tiên điều gì **khi mất liên lạc**, và phần nào vẫn phục vụ được.

Một hệ thống có thể có quy tắc khác nhau cho các thao tác. Có thể vẫn cho đọc dữ liệu cũ phục vụ thống kê nhưng ngừng một số thao tác cần đảm bảo mạnh. Đừng dán một nhãn CP hoặc AP cho toàn bộ sản phẩm rồi suy ra mọi truy vấn hành xử giống nhau.

## CAP không chọn database thay bạn

Nó không định lượng tốc độ truy vấn, dung lượng, chi phí hoặc độ dễ vận hành. Ngay khi mạng bình thường, chờ phối hợp vẫn có chi phí độ trễ. Và C ở đây khác với consistency trong ACID.

Bài tập: đổi yêu cầu sản phẩm thành “trạng thái có thể cũ tối đa 10 giây”. Khi partition kéo dài một phút, chỉ phục vụ dữ liệu cũ có đáp ứng yêu cầu không? Không. Bạn vẫn cần quy tắc dừng hoặc báo trạng thái không đủ mới, không chỉ một nhãn kiến trúc.

Đọc trước [consistency]({{< relref "/wiki/nen-tang/distributed-systems/consistency.md" >}}) và [replication]({{< relref "/wiki/nen-tang/distributed-systems/replication.md" >}}).
