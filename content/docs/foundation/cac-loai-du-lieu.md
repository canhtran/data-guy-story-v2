---
title: "4. Các loại dữ liệu"
weight: 4
---

Sau khi hiểu được vòng đời của dữ liệu đi từ nông trại đến lúc lên mâm, có một câu hỏi tiếp theo: **Vậy cái đống nguyên liệu (data) đó trông như thế nào?**

Thực tế thì data có muôn hình vạn trạng. Có cái ngăn nắp như một cái tủ hồ sơ, có cái lộn xộn như một cái phòng trọ sinh viên cuối tháng. Để dễ quản lý, người ta chia data làm 3 loại chính:

### 1. Dữ liệu có cấu trúc (Structured Data) - *Tủ quần áo gọn gàng*

Đây là "con nhà người ta" trong thế giới data. 

**Nó là gì?** Nó là những dữ liệu được sắp xếp cực kỳ rõ ràng, chia thành các hàng và cột. Giống như bạn mở một file Excel ra, cột nào là Tên, cột nào là Tuổi, cột nào là Địa chỉ đều rành rành ra đó.

**Đặc điểm:** Rất dễ tìm kiếm. Bạn muốn tìm "Những ai trên 25 tuổi ở Hà Nội"? Chỉ cần lướt qua cột Tuổi và cột Địa chỉ là xong.
**Lưu trữ ở đâu:** Thường được cất trong các Cơ sở dữ liệu quan hệ (Relational Database) – sẽ được nói kỹ ở các bài sau.

### 2. Dữ liệu phi cấu trúc (Unstructured Data) - *Nhà kho thập cẩm*

Trái ngược hoàn toàn với người anh em ở trên, đây là "đứa con ngỗ nghịch".

**Nó là gì?** File ghi âm cuộc gọi của khách hàng phàn nàn, cái video Tiktok bạn vừa xem, tấm ảnh meme bạn gửi trong group chat, hay một đoạn văn bản dài ngoằng không theo quy luật nào. 

**Đặc điểm:** Không có hàng có cột nào ở đây cả. Rất khó để máy tính "đọc hiểu" và tìm kiếm trực tiếp. Ví dụ, bạn có 1000 video và muốn tìm "video nào có hình con mèo" thì không thể dùng file Excel để lọc được, mà phải nhờ đến các hệ thống AI phân tích hình ảnh. Loại này chiếm tới hơn 80% dữ liệu trên toàn thế giới hiện nay!
**Lưu trữ ở đâu:** Thường vứt thẳng vào các **Data Lake** (một cái kho mênh mông chứa đủ thứ hầm bà lằng chưa qua phân loại).

### 3. Dữ liệu bán cấu trúc (Semi-structured Data) - *Vali du lịch chia ngăn*

Đây là đứa con lai nằm giữa hai loại trên.

**Nó là gì?** Ví dụ dễ thấy nhất là **Email**. Nó có những cấu trúc rõ ràng: Người gửi (From), Người nhận (To), Tiêu đề (Subject). Nhưng phần Nội dung (Body) thì bạn viết hươu viết vượn gì cũng được – đây chính là phần phi cấu trúc. Hoặc những file có định dạng như JSON, XML mà lập trình viên hay xài.

**Đặc điểm:** Có quy tắc, có đánh dấu (tag), nhưng không cứng nhắc phải thành hàng thành cột cố định như Excel. Giống như bạn xếp vali đi du lịch, có túi zip riêng cho đồ lót, túi riêng cho áo thun, nhưng trong túi thì nhét đồ thế nào tùy bạn.
**Lưu trữ ở đâu:** Thường được lưu trong các hệ thống NoSQL.

---

### Tóm lại cho dễ nhớ

| Loại dữ liệu | Structured (Có cấu trúc) | Semi-structured (Bán cấu trúc) | Unstructured (Phi cấu trúc) |
|--------------|-------------------------|-------------------------------|----------------------------|
| **Ví dụ** | Bảng tính Excel, Database | Email, File JSON, XML | Hình ảnh, Video, File ghi âm |
| **Mức độ ngăn nắp** | Rất cao (Có hàng, cột) | Trung bình (Có nhãn/tag) | Rất thấp (Không quy luật) |
| **Độ khó xử lý** | Dễ nhất | Khá dễ | Khó nhất |
| **Ví von** | Tủ quần áo chia ngăn nắp | Vali du lịch có túi zip riêng | Nhà kho vứt đồ lung tung |

---

Bài sau mình sẽ kể tiếp: **Lưu trữ dữ liệu: file, thư mục, và tại sao người ta lại đẻ ra cái gọi là "Database"?**
