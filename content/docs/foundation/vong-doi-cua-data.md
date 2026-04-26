---
title: "3. Vòng đời của Data"
weight: 3
---

Ở bài trước, chúng ta đã chốt với nhau: công ty giống như một cái nhà hàng, data là nguyên liệu, Data Engineer là đội vận chuyển và xây kho, còn Data Analyst là bếp trưởng.

Vậy thì, một mớ "nguyên liệu" đó từ lúc sinh ra đến lúc biến thành "món ăn" (báo cáo) trên bàn sếp sẽ trải qua những bước nào? Dân trong ngành gọi đó là **Vòng đời của dữ liệu (Data Lifecycle)**.

Thực ra nó cũng giống y chang hành trình của một mớ rau từ nông trại đến bàn ăn thôi. Cùng xem nhé:

### 1. Sinh ra (Generation) - *Trồng rau, nuôi cá*

Mọi thứ đều phải có khởi đầu. Dữ liệu được sinh ra liên tục mỗi giây:
- Khi bạn click vào một cái áo trên Shopee.
- Khi bạn quẹt thẻ mua ly cafe.
- Khi một cái cảm biến nhiệt độ gửi tín hiệu về điện thoại.

Tất cả những hành động đó tạo ra "nguyên liệu thô" ở khắp nơi.

### 2. Thu thập (Ingestion) - *Xe tải chở hàng về kho*

Nguyên liệu rải rác khắp nơi thì không dùng được, phải gom lại. Data Engineer sẽ xây dựng những đường ống (Data Pipeline) giống như một đội xe tải. Đội xe này ngày đêm chạy đến các "nông trại" (App, Web, Database của công ty) để gom hết data chở về một chỗ.

### 3. Lưu trữ (Storage) - *Cất vào kho*

Chở hàng về rồi thì phải có chỗ cất. Dữ liệu được đổ vào các hệ thống lưu trữ khổng lồ như **Data Lake** (kho chứa đồ tả pín lù chưa phân loại), **Data Warehouse** (kho đã chia ngăn kệ rõ ràng), hoặc hiện đại hơn là **Data Lakehouse** (sự lai tạo hoàn hảo: vừa có sức chứa lớn của Lake, vừa được tổ chức ngăn nắp như Warehouse).

### 4. Xử lý & Làm sạch (Processing / Transformation) - *Sơ chế, nhặt lá sâu*

Đây là bước cực kỳ quan trọng. Hàng chở về chắc chắn sẽ có rau bị sâu, cá bị ươn, hoặc củ khoai tây dính đầy bùn đất (dữ liệu rác, lỗi, thiếu sót).
Data Engineer sẽ viết các đoạn code để "rửa sạch" dữ liệu: Xóa các thông tin bị lỗi, sửa lại định dạng cho chuẩn, gộp các thông tin giống nhau lại. Đảm bảo nguyên liệu lúc này đã sạch sẽ, thái sẵn, sẵn sàng cho việc nấu nướng.

### 5. Phân tích (Analytics) - *Bếp trưởng xào nấu*

Lúc này, nguyên liệu đã sạch sẽ và được cất ngăn nắp. Các bác bếp trưởng (Data Analyst) sẽ mở kho, lấy đồ ra xào nấu thành các báo cáo (Report), biểu đồ (Dashboard) đẹp mắt để ban giám đốc "thưởng thức" và ra quyết định kinh doanh.

### 6. Lưu trữ lạnh (Archiving) - *Cất tủ đông sâu*

Sau một vài năm, dữ liệu cũ (ví dụ lịch sử mua hàng từ 5 năm trước) không còn ai buồn xem nữa. Nhưng công ty vẫn không dám xóa vì sợ lỡ sau này cần đối soát. Thế là họ gói ghém đống data đó lại, cất vào những nơi lưu trữ siêu rẻ (giống như nhét xuống tận đáy tủ đông) để tiết kiệm chi phí.

---

### Tóm lại cho dễ nhớ

| Bước trong Vòng đời | Thuật ngữ (Tiếng Anh) | Ví von thực tế |
|-------------------|----------------------|-------------------------|
| 1. Sinh ra | Generation | Hành động trồng rau, nuôi cá |
| 2. Thu thập | Ingestion | Đội xe tải gom hàng |
| 3. Lưu trữ | Storage | Cất vào nhà kho lớn |
| 4. Xử lý & Làm sạch | Processing / Transformation | Rửa rau, nhặt lá sâu, sơ chế |
| 5. Phân tích | Analytics | Bếp trưởng xào nấu lên mâm |
| 6. Lưu trữ lạnh | Archiving | Gói lại cất tủ đông sâu |

---

Bài sau mình sẽ kể tiếp: **Các loại dữ liệu: Đâu là sự khác biệt giữa có cấu trúc, bán cấu trúc và phi cấu trúc?**