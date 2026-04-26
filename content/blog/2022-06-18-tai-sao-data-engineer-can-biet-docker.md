---
title: Tại sao data engineer cần biết Docker
date: 2022-06-18
authors:
  - name: Cảnh
    link: https://www.dataguystory.com/tui/
    image: https://avatars.githubusercontent.com/u/3214379?v=4
tags:
  - Chuyện nghề
---

Bữa nay tui kể thêm một kĩ năng nữa cần phải biết của mấy bạn Data Engineer. Tiêu đề là Docker nhưng bài viết có nhắc đến Terraform, Kubernetes, Infrastructure as Code (cho ai lười đọc thích kiếm từ khóa tự Google).

<!--more-->

## Tại sao vậy?

Đa số các công ty đều sử dụng dịch vụ cloud và áp dụng kiến trúc microservices. Mà đã đụng đến microservices rồi thì chắc chắn sẽ là Docker, Terraform chưa kể đến Kubernetes. Còn nếu mà những công ty đặc thù xài on-premise thì người ta ít hay nhiều cũng áp dụng kiến trúc microservices và sử dụng docker để triển khai hệ thống. Thời buổi giờ ít ai mà cài đặt thủ công vào server lắm. Bạn không biết thì bạn thành “người tối cổ” chắc luôn.

Data Engineer là một ngành rất đặc thù, nó pha trộn giữa Software Engineer và Data. Chính vì vậy mà những bạn devops rất khó hỗ trợ cho Data Engineer, triển khai một phần mềm nó khác với triển khai platform lắm. Vậy nên thông thường, các bạn Data Engineer sẽ là người làm tất cả mọi thứ từ triển khai các tool, cài đặt Data Warehouse, cài đặt Spark… vân vân và mây mây. 

Ví dụ một bạn Data Engineer mà không có kiến thức Devops, không biết docker, terraform, không biết infrastructure as code thì làm sao làm được. Các bạn cài đặt thủ công rồi không đảm bảo stable, scalable rồi lỡ có chuyện gì xảy ra không restore lại được bay luôn data thì lúc đó trời cứu :))

Giả sử trường hợp mà công ty đó có team Data Platform Engineer hoặc các bạn Devops xịn sẵn sàng hỗ trợ để triển khai hệ thống thì Data Engineer vẫn cần phải biết ít nhất là Docker. Ví dụ bạn cần thay đổi cấu hình hệ thống thì phải viết Terraform để thay đổi theo ý mình chứ ai cho các bạn vào trực tiếp hệ thống mà thay đổi, vậy đâu có đảm bảo. Hoặc khi bạn xây dựng một cái API để ETL data thì cũng phải biết cách để triển khai chứ, không lẽ ngồi chờ Devops, lâu quá sếp đuổi mất.

## Tóm lại

Vậy khi nào bạn nên học mấy kĩ năng này? Đương nhiên là sau khi học xong kiến thức về Data Engineer rồi. Mà thậm chí trong lúc học Data Engineer á, bạn thử triển khai Hadoop, Spark bằng Docker đi, cũng đáng chớ bộ.
