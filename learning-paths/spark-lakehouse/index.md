# Data Engineering nâng cao: Spark & Lakehouse

<span class="dgs-status">Lên kế hoạch · chưa mở bài học</span>

{{< learning-free-note >}}

Bạn sẽ xử lý dữ liệu bán lẻ nhiều kênh bằng Spark và các bảng Iceberg, rồi tìm nguyên nhân khi job chậm hoặc chạy lại cho kết quả sai.

## Phù hợp với ai?

Bạn đã vận hành được một pipeline batch và hiểu dữ liệu thay đổi, mô hình phân tích, kiểm tra chất lượng. [Data Engineering thực chiến]({{< relref "/learning-paths/data-engineering-thuc-chien/_index.md" >}}) là bước chuẩn bị trực tiếp; kinh nghiệm tương đương cũng phù hợp.

## Bạn sẽ làm được gì?

Đọc kế hoạch thực thi Spark; giải thích task, partition, shuffle và skew; xây bảng lakehouse có lịch sử; xử lý dữ liệu sửa về sau; so kết quả tăng dần với chạy lại toàn bộ; đo và giải thích một cải thiện hiệu năng.

**Nhịp học dự kiến:** 8 tuần, 8–10 giờ mỗi tuần, gồm 6 chặng dẫn đường và 2 tuần dự án cuối khóa.

## Dự án dẫn đường

Một nhà bán lẻ kết hợp giao dịch tại cửa hàng, đơn web, hàng trả, lịch sử sản phẩm và sự kiện khách hàng. Bạn tạo dữ liệu bronze, silver và gold trên object storage cục bộ. Spark master và nhiều worker cùng chạy trên một máy; mô hình này giúp quan sát cách Spark chia việc, nhưng không mô phỏng sức chứa của cluster nhiều máy. AI hướng dẫn cài đặt, kiểm tra dịch vụ và debug từng bước.

## Các chặng học

1. Cài đặt cục bộ và chạy một job nhỏ.
2. Biến đổi phân tán và đọc shuffle.
3. Tạo bảng Iceberg và báo cáo có lịch sử.
4. Xử lý dữ liệu đến muộn, sửa dữ liệu và chạy lại.
5. Đo hiệu năng, điều tra skew và phục hồi job lỗi.
6. Đóng gói, theo dõi và giải thích lựa chọn kiến trúc.
7–8. Tự xây và kiểm chứng một dự án mới.

## Dự án cuối khóa

Chọn **mượn sách thư viện**, **chuyến xe đạp đô thị** hoặc **thương mại workshop**. Mỗi lựa chọn có dữ liệu sửa về sau và một bài toán hiệu năng để bạn tự đo, kiểm chứng và bảo vệ quyết định.

## Tình trạng học liệu

Bài học, bộ dữ liệu và cấu hình tương thích đang được thử nghiệm trên máy cá nhân. Chưa có lab hoàn chỉnh để bắt đầu.

[Trở lại danh sách lộ trình]({{< relref "/learning-paths/_index.md" >}})

## Học cùng NotebookLM

{{< notebook-link path="spark-lakehouse" >}}

