# Nhập môn Data Engineering

<span class="dgs-status">Đang biên soạn</span>

{{< learning-free-note >}}

Bạn sẽ xây một pipeline nhỏ: đọc dữ liệu đơn hàng, kiểm tra lỗi, lưu vào PostgreSQL, viết SQL tính các chỉ số, rồi tạo một bản tin buổi sáng. AI đồng hành từ buổi đầu tiên: hướng dẫn cài đặt trên máy của bạn, hỏi từng bước, giúp debug theo lệnh và kết quả bạn gửi. Bạn vẫn tự chạy, kiểm tra và giải thích kết quả.

> **Chưa mở học đầy đủ:** Bộ bài học theo tuần, dữ liệu dự án đầy đủ và bài kiểm tra đang được chuẩn bị. Trang nguồn NotebookLM bên dưới đã có bản dùng thử để đọc và trao đổi với mentor. Trang này cho bạn xem trước cấu trúc học, không phải lời hứa rằng toàn bộ bài học đã sẵn sàng.

## Phù hợp với ai?

Người mới bắt đầu. Bạn chưa cần biết SQL, Python hay database. Nếu đã có kinh nghiệm, bạn có thể chứng minh kỹ năng ở các checkpoint tương ứng khi học liệu được phát hành.

## Kết quả sau lộ trình

- Giải thích mỗi dòng dữ liệu đại diện cho điều gì và các chỉ số được tính ra sao.
- Dùng SQL và Python để biến file đầu vào thành báo cáo có kiểm tra chất lượng.
- Chạy lại dữ liệu an toàn, tìm và sửa một lỗi, rồi bàn giao cách vận hành.

**Nhịp học dự kiến:** 6 tuần, 6–8 giờ mỗi tuần, gồm 5 chặng dẫn đường và 1 tuần dự án cuối khóa. Con số này cần được thử nghiệm với người mới trước khi cam kết thời lượng.

## Dự án dẫn đường: Bản tin quán cà phê mỗi sáng

Một quán cà phê xuất file đơn hàng hằng ngày. Chủ quán muốn biết doanh thu, số đơn, món bán chạy và liệu số liệu có đáng tin. Bạn đi từ vài dòng có thể tính tay đến một pipeline tạo báo cáo CSV/HTML. Mọi công cụ dữ liệu chạy trên máy của bạn.

## Hành trình sáu chặng

1. **Gặp mentor và khám phá dữ liệu.** AI giúp kiểm tra môi trường, cài công cụ từng bước, rồi cùng bạn đọc vài đơn hàng.
2. **Trả lời bằng SQL.** Tính chỉ số và kiểm tra một phép JOIN làm tăng số liệu.
3. **Đọc file bằng Python.** Nhận diện dòng lỗi và ghi rõ nguyên nhân.
4. **Ghép thành pipeline.** Nạp, biến đổi và xuất bản tin đầu tiên.
5. **Kiểm chứng và chạy lại.** Sửa dữ liệu, kiểm tra số liệu và phục hồi sau lỗi.
6. **Chọn dự án cuối khóa.** Chọn chi tiêu cá nhân, mua hàng online hoặc điện sinh hoạt; cùng AI xác định brief và tự kiểm chứng kết quả.

{{< learning-module-link page="/learning-paths/nhap-mon-data-engineering/tuan-1" >}}

## Học cùng AI

Bạn có thể thêm trang nguồn bên dưới vào NotebookLM và dùng prompt mentor để bắt đầu đọc, làm bài thử. Bộ lab theo tuần sẽ được bổ sung sau. AI hỏi về hệ điều hành, các công cụ đã có và checkpoint hiện tại; sau mỗi lệnh cài đặt, AI chờ kết quả kiểm tra của bạn trước khi tiếp tục. Bạn cũng có thể đọc [Wiki]({{< relref "/wiki/_index.md" >}}) trực tiếp.

## Dự án cuối khóa

Bạn chọn một trong ba tình huống mới, xác định hai hoặc ba câu hỏi, rồi tạo báo cáo và chứng minh kết quả đúng. AI có thể hỗ trợ lên ý tưởng, code và debug; bằng chứng chạy trên máy và phần giải thích của bạn quyết định việc hoàn thành.

## Học cùng NotebookLM

{{< notebook-link path="nhap-mon-data-engineering" >}}

