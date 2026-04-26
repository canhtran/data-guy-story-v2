---
title: "2. Data Engineer là gì?"
weight: 2
---

Ở bài trước, anh em mình đã chốt với nhau: Data thực ra chỉ giống như **mấy tờ giấy đi chợ**.

Nếu mỗi ngày chỉ có 1 tờ giấy, bạn vứt luôn vào túi quần là xong. Nhưng thử nghĩ xem, nếu bạn là sếp của chuỗi siêu thị Aeon, mỗi giây trôi qua có hàng ngàn tờ giấy đi chợ bay về từ khắp các chi nhánh trên cả nước thì sao?

Lúc này cái túi quần chịu không nổi nữa rồi. Bạn bắt buộc phải có một **hệ thống**:
1. Một mạng lưới **băng chuyền tự động** để thu gom hết đống giấy tờ kia về đúng một chỗ.
2. Một cái **nhà kho khổng lồ**, chia sẵn kệ nào ra kệ nấy: Kệ rau củ, kệ thịt cá, kệ đồ khô... để cất giấy cho dễ tìm.
3. Có bộ phận lọc, chuyên vứt đi mấy tờ rách nát hay bị ghi sai chữ không đọc được.

Người đứng ra nhận thiết kế, xây dựng và bảo trì cái băng chuyền và nhà kho đó, dân trong ngành gọi là **Data Engineer (Kỹ sư dữ liệu)**.

### Vậy công việc thực tế của Data Engineer là làm gì?

Trong thế giới IT thực sự, mấy "tờ giấy đi chợ" đó chính là dữ liệu người dùng, lịch sử quẹt thẻ, log hệ thống... Công việc hàng ngày của một Data Engineer sẽ xoay quanh mấy món này:
- Xây **Data Pipeline (Băng chuyền dữ liệu)**: Viết code để hút dữ liệu từ app, web, database... rồi kéo tất cả về một cục.
- Xây **Data Warehouse / Data Lake (Nhà kho dữ liệu)**: Thiết lập chỗ lưu trữ an toàn, gọn gàng, chia khu vực rõ ràng để chứa cái đống dữ liệu khổng lồ kia.
- **Làm sạch dữ liệu**: Chạy tool để lọc bỏ những dữ liệu bị rác, bị thiếu, hay trùng lặp nhau.

### Khoan, thế họ khác gì Data Analyst với Data Scientist?

Để dễ hình dung nhất, cứ coi công ty của bạn là một cái nhà hàng:
- **Data Engineer** là mấy bác nông dân và tài xế chở hàng: Họ đi gom nguyên liệu (thịt, cá, rau), đóng thùng cẩn thận rồi chở về nhập đầy kho cho nhà hàng. Họ chả cần biết món ăn nấu lên ngon dở ra sao, miễn là kho luôn đầy và nguyên liệu không bị mốc.
- **Data Analyst (Chuyên viên phân tích)** là ông bếp trưởng: Ông này mở cửa kho, nhặt nguyên liệu ra xào nấu thành các món ăn (các bản báo cáo, biểu đồ) rồi bưng lên cho ban giám đốc "thưởng thức".
- **Data Scientist (Nhà khoa học dữ liệu)** giống như chuyên gia ẩm thực: Dùng mớ nguyên liệu đó để chế ra công thức món ăn mới tinh, hoặc dựa vào thời tiết để dự đoán xem ngày mai khách sẽ gọi món gì nhiều nhất (ứng dụng AI, Machine Learning để dự đoán).

### Tại sao nhiều người nhầm?

Bởi vì trong các công ty nhỏ hoặc startup, một người có thể làm cả 3 vai. Bạn có thể thấy bạn DE nhưng cũng phải viết report, thậm chí dự báo đơn giản. Nhưng khi công ty lớn lên, mỗi người sẽ chuyên sâu. Và DE là nền tảng – **không có pipeline sạch thì DA/DS chỉ có "rác vào, rác ra"**.

### Tạm kết:

| Chức danh | Đóng vai gì ở ngoài đời | Suốt ngày nói về cái gì ở công ty |
|---------|---------------------|--------------|
| Data Engineer | Người gom nguyên liệu, xây kho | Data Pipeline, Data Warehouse, ETL |
| Data Analyst | Đầu bếp xào nấu nguyên liệu | Dashboard, Report, Visualize |
| Data Scientist | Chuyên gia ẩm thực, đoán khẩu vị | AI, Machine Learning, Predict |

---

Bài sau mình sẽ kể tiếp: **Vòng đời của dữ liệu – từ khi sinh ra đến khi được phân tích**