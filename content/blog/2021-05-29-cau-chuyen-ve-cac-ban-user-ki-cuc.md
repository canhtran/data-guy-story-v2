---
title: Câu chuyện về các bạn user kì cục
date: 2021-05-29
authors:
  - name: Cảnh
    link: https://www.dataguystory.com/tui/
    image: https://avatars.githubusercontent.com/u/3214379?v=4
tags:
  - Chuyện đi làm
---

<!--more--> 

Mấy tuần rồi tui có tham gia vào một dự án mới, chủ yếu là xây dựng hệ thống data pipeline. Hệ thống thì không có gì để bàn nên tui sẽ không kể chi tiết ở đây. Điều mà tui muốn đề cập là độ phức tạp của dự án, nó là thành quả kết hợp của nhiều team khác nhau, mỗi team nắm giữ một phần quan trọng trong Workflow (luồng làm việc).

## Sơ lược

![user workflow](/blog/cau-chuyen-ve-user-ki-cuc/user-workflow.png)

Để dễ hình dung thì quy trình có thể diễn tả như vầy:

- Team R là team business, không biết về kĩ thuật, nhưng nắm vững kiến thức chuyên ngành. Họ dựa theo kiến thức này mà đặt ra một bộ quy ước (rules).
- Team B dùng data và dựa vào bộ quy ước để phát triển mô hình dữ liệu dành cho việc dự đoán.
- Team A là team tạo ra input data cho team B sử dụng và cũng là owner (chủ sở hữu) của data.

Cuối cùng, quan trọng nhất trong quy trình này là tui, người kết hợp output (thành quả) của tất cả các team lại với nhau thành một hệ thống chỉnh chu.

Do có liên quan đến nhiều team, chín người mười ý nên sau khi họp bàn mọi người đã thống nhất hệ thống phải được tự động hoàn toàn ở tất cả các khâu, tránh sự can thiệp của người dùng càng nhiều càng tốt.

## User thật là kì cục

Nhiều bạn sẽ nghĩ: “Ủa nếu hệ thống tự động hoàn toàn thì dính zì tới user, mắc gì kêu mấy người đó kì cục?!”. Vậy mà có mới hay đó nha!

### Sai kết quả

Trong quá trình vận hành, một ngày đẹp trời tự nhiên kết quả không ra như ý muốn. Thế là tui “được” réo tên, vì sao kết quả ra sai, thay vì 0 lại ra 1. Ủa ủa, tui đâu biết gì đâu, kết quả dựa vào bộ quy ước của team R và cách xây dựng mô hình dữ liệu của team B mà :((

### Thiếu input

Lại một ngày “đẹp” trời khác, tự nhiên tất cả các team đều gọi tên tui: “Tại sao hệ thống không có kết quả ???”. Chuyện động trời rồi đây. Tui lập tức mở slack lên thì thấy ngay dòng cảnh báo của con bot: “không có data để mô hình dữ liệu xử lý!”. Hóa ra là hệ thống riêng của team A bị lỗi, không tạo ra được input data. Và ngạc nhiên là không ai chịu đọc cảnh báo bên slack…

### Những yêu cầu và câu hỏi vô lý

Và đây chính là team R, hầu như họ nhắn riêng cho tui mỗi ngày với những câu hỏi chung chung về hệ thống, ví dụ như: Mô hình dữ liệu hoạt động thế nào? Sao data lại là kiểu Double mà không phải Integer? Thỉnh thoảng họ còn nhờ tui debug code python nữa !? Ủa ủa, đây đâu phải lớp học và tui đâu phải là thầy giáo.

## Và đây là cách tui “xử” họ

### Sử dụng Jira hay bất kì hệ thống quản lý nào

Jira là một ứng dụng theo dõi và quản lý lỗi, vấn đề và dự án, được phát triển để làm quy trình này trở nên dễ dàng hơn cho mọi tổ chức. JIRA đã được thiết kế với trọng tâm vào kết quả công việc, có thể sử dụng ngay và linh hoạt khi sử dụng.

Khi được đưa vào sử dụng, bất cứ yêu cầu nào cũng phải tạo một “ticket”. Tui chỉ dựa theo yêu cầu trên ticket mà làm việc. Yêu cầu đó phải được chấp thuận từ tất cả team để đồng bộ với nhau. Ví dụ một thay đổi nhỏ về data của team A có thể ảnh hưởng đến logic của team R và mô hình dữ liệu của team B. Việc chấp thuận này tránh được sự không đồng bộ giữa các team và những yêu cầu vô lý từ một team nào đó.

### Liên lạc trên những kênh chính thức

Đối với những tin nhắn riêng, tui đều khuyến khích họ đăng trên kênh chung để mọi người cùng thảo luận, biết đâu ai đó sẽ có cùng thắc mắc. Lý do thứ hai là tui có nhiều dự án khác phải làm, trả lời tin nhắn từng người là hết 8 tiếng làm việc rồi. Thêm vào đó, nó cũng giúp tui tránh được những yêu cầu vô lý như debug code hoặc những câu hỏi do người dùng không chịu đọc thông tin dự án.

### Tạo quy trình chuẩn

Cái quy trình này có tên tiếng anh là SOP - Standard operating procedure. Đại loại là lập một thoả thuận giữa các team về quy trình thay đổi, trách nhiệm của từng team khi có thay đổi, thời gian thay đổi… Ngoài ra, quy trình này cũng kèm theo mô tả những lỗi cơ bản và cách giải quyết (Khi có lỗi thì nên liên lạc với team nào, cách thức liên hệ ra sao, ai là người chịu trách nhiệm chính…)

## Tóm lại

Đây là những thứ mà hiện tại tui đang áp dụng và nó cũng có hiệu quả một phần nào đó. Điều quan trọng nhất là mình phải luôn luôn giao tiếp với người dùng, đặt mình vào hoản cảnh của họ, thảo luận giữa các bên để tìm ra quy trình tối ưu nhất. Nếu không dù bạn viết một quy trình mà bạn “tự thấy” rất hay nhưng sau tất cả bạn phát hiện chỉ có mình mình nghĩ như vậy 😏
