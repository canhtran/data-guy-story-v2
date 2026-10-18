# Streaming Engineering

<span class="dgs-status">Lên kế hoạch · chưa mở bài học</span>

{{< learning-free-note >}}

Bạn sẽ theo dõi đơn giao hàng qua các sự kiện đến liên tục và học cách giữ kết quả đúng khi sự kiện bị trùng, đến trễ hoặc job dừng giữa chừng.

## Phù hợp với ai?

Bạn đã xây và chạy lại một pipeline batch, hiểu khóa bản ghi, thời gian và kiểm tra dữ liệu. Có thể chuẩn bị qua [Data Engineering thực chiến]({{< relref "/learning-paths/data-engineering-thuc-chien/_index.md" >}}) hoặc chứng minh kỹ năng tương đương.

## Bạn sẽ làm được gì?

Thiết kế event ID và state của đơn; dùng event time và watermark; quy định cách xử lý dữ liệu đến muộn; khôi phục job từ checkpoint; giải thích lag, backpressure và giới hạn của cách ghi kết quả.

**Nhịp học dự kiến:** 8 tuần, 8–10 giờ mỗi tuần, gồm 6 chặng dẫn đường và 2 tuần dự án cuối khóa.

## Dự án dẫn đường

Một dịch vụ giao hàng phát các sự kiện tạo đơn, nhận đơn, lấy hàng, giao và hủy. Bạn dùng Kafka và Flink cài trên máy để tạo bảng trạng thái hiện tại và báo cáo đơn trễ. AI hướng dẫn cài đặt, đọc log và tìm nguyên nhân lỗi theo kết quả bạn chạy.

## Các chặng học

1. Cài đặt, gửi và đọc sự kiện đầu tiên.
2. Nhận diện sự kiện trùng và theo dõi trạng thái đơn.
3. Tính theo event time và xử lý sự kiện đến muộn.
4. Kiểm tra checkpoint, fail và restart.
5. Điều tra lag, backpressure và thay đổi job an toàn.
6. Tạo góc nhìn vận hành có độ mới và cảnh báo.
7–8. Xây và bảo vệ một pipeline sự kiện mới.

## Dự án cuối khóa

Chọn **check-in workshop**, **trạng thái trạm xe đạp** hoặc **ủy quyền thanh toán**. Bạn xác định quy tắc thời gian và state, rồi kiểm chứng với sự kiện trùng, sai thứ tự và một lần khôi phục.

## Tình trạng học liệu

Lab Kafka/Flink, event fixture và yêu cầu phần cứng đang được chuẩn bị; hiện chưa có bài học hoàn chỉnh để bắt đầu.

[Trở lại danh sách lộ trình]({{< relref "/learning-paths/_index.md" >}})

## Học cùng NotebookLM

{{< notebook-link path="streaming-engineering" >}}

