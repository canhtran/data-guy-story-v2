## Buổi học đầu tiên: từ bốn đơn đến một con số tin được

Dành khoảng 30–45 phút. Bạn cần Python 3 có thư viện `sqlite3`; không cần tài khoản database hay thư viện trả phí. SQLite dùng ở buổi khởi động để bạn thử SQL ngay. Dự án chính của lộ trình vẫn dùng PostgreSQL, và buổi này chưa thay thế lab PostgreSQL.

### Checkpoint 0 — Mở được Python

Mở Terminal trên macOS/Linux hoặc PowerShell trên Windows. Chạy một lệnh phù hợp:

```sh
# macOS / Linux
python3 --version
```

```powershell
# Windows
py -3 --version
```

Bạn cần thấy `Python 3.x.x`. Nếu không có lệnh, dùng [trang cài Python](https://www.python.org/downloads/) và [hướng dẫn theo hệ điều hành](https://docs.python.org/3/using/index.html), rồi mở lại terminal. Gửi mentor hệ điều hành và lỗi cụ thể; đừng thử cài nhiều phiên bản cùng lúc. Các bước cài đặt khác nhau theo máy; ví dụ bên dưới đã được kiểm tra bằng Python và SQLite, chưa được chạy trên mọi hệ điều hành.

### Checkpoint 1 — Tự tính trước

Dữ liệu giả lập `notebook-cafe-v1`, mỗi dòng là một đơn, `order_id` là khóa. Ngày kinh doanh đã được quy về giờ Việt Nam. Tiền là số nguyên đồng; chỉ đơn `paid` được tính doanh thu.

| order_id | business_date | amount_vnd | status |
| --- | --- | ---: | --- |
| 101 | 2026-09-01 | 40000 | paid |
| 102 | 2026-09-01 | 60000 | paid |
| 103 | 2026-09-02 | 50000 | paid |
| 104 | 2026-09-02 | 30000 | cancelled |

Trước khi chạy: ngày 01/09 có bao nhiêu đơn được tính? Ngày 02/09 thì sao? Nếu bỏ điều kiện trạng thái, số nào thay đổi?

### Checkpoint 2 — Chạy truy vấn đầu tiên

Tạo một thư mục học riêng bằng trình quản lý file. Tạo file văn bản **`buoi_dau.py`**, dán đoạn dưới và lưu UTF-8. Kiểm tra tên không bị thành `buoi_dau.py.txt`.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.executescript("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    business_date TEXT NOT NULL,
    amount_vnd INTEGER NOT NULL CHECK (amount_vnd >= 0),
    status TEXT NOT NULL CHECK (status IN ('paid', 'cancelled'))
);
INSERT INTO orders VALUES
    (101, '2026-09-01', 40000, 'paid'),
    (102, '2026-09-01', 60000, 'paid'),
    (103, '2026-09-02', 50000, 'paid'),
    (104, '2026-09-02', 30000, 'cancelled');
""")

query = """
SELECT business_date, COUNT(*) AS order_count,
       SUM(amount_vnd) AS revenue_vnd
FROM orders
WHERE status = 'paid'
GROUP BY business_date
ORDER BY business_date;
"""
for row in connection.execute(query):
    print(*row, sep=" | ")
connection.close()
```

Mở terminal tại thư mục chứa file. Nếu cần di chuyển thư mục, dùng `cd "đường dẫn thư mục của bạn"`. Chạy `python3 buoi_dau.py` trên macOS/Linux hoặc `py -3 buoi_dau.py` trên Windows.

Kết quả để đối chiếu **sau khi đã dự đoán**:

```text
2026-09-01 | 2 | 100000
2026-09-02 | 1 | 50000
```

Database nằm trong bộ nhớ. Mỗi lần chạy script tạo một bản mới; đóng script thì dữ liệu này mất. Điều đó giúp buổi thử chạy lại dễ dàng, nhưng **không chứng minh** pipeline lưu trữ lâu dài đã có idempotency.

### Checkpoint 3 — Thử làm kết quả sai rồi sửa

1. Bỏ dòng `WHERE status = 'paid'`, chạy lại. Ngày 02/09 trở thành **2 đơn, 80000 đồng**. Giải thích vì sao.
2. Khôi phục điều kiện, đổi đơn 103 từ 50000 thành 55000. Ngày 02/09 phải thành **1 đơn, 55000 đồng**.
3. Thay `WHERE status = 'paid'` bằng `WHERE status = 'missing'`. Kết quả không có dòng nào, vì không còn nhóm để tổng hợp. Báo cáo “không có dữ liệu” khác với một dòng doanh thu 0 như thế nào?
4. Khôi phục dữ liệu và query ban đầu, chạy hai lần. Hai đầu ra phải giống nhau.

### Khi bị lỗi

| Dấu hiệu | Kiểm tra tiếp |
| --- | --- |
| `can't open file` | Terminal có ở đúng thư mục không? Tên file có đuôi `.txt` không? |
| `SyntaxError` | Có sao chép cả dấu ``` vào file không? Dấu nháy ba có đủ không? |
| `no such table: orders` | Có giữ phần tạo bảng trước truy vấn và cùng connection không? |
| `No module named sqlite3` | Gửi mentor nguồn cài Python và phiên bản; kiểm tra bản Python chính thức có SQLite. |
| Số đúng nhưng thứ tự khác sau khi sửa query | Kiểm tra `ORDER BY`; không dựa vào thứ tự tình cờ. |

Không sửa lỗi bằng cách xóa thư mục hoặc cài thêm thư viện ngẫu nhiên. Dùng prompt “Gỡ lỗi” và gửi nguyên lệnh cùng phần lỗi liên quan.

### Bằng chứng để kết thúc buổi

Gửi mentor phiên bản Python, code đang dùng, đầu ra ban đầu và đầu ra của một ca thay đổi. Tự giải thích vì sao `WHERE` ảnh hưởng số đơn, mỗi dòng kết quả đại diện cho gì và vì sao chạy script lần hai không thêm bản ghi vào lần đầu. Lưu nhật ký rồi chuyển sang bài JOIN trong nguồn.

## Các chặng tiếp theo và tiêu chí cần đạt

Đây là bản đồ làm việc với mentor. **Buổi đầu ở trên chạy được; các lab PostgreSQL và pipeline đầy đủ vẫn đang biên soạn.** Bạn có thể học các bài Wiki đã có, nhưng mentor không được tự tuyên bố những lab còn thiếu đã sẵn sàng.

| Chặng | Việc thực hiện | Bằng chứng cần có |
| --- | --- | --- |
| 1. Hiểu dữ liệu và môi trường | Hoàn thành buổi đầu | Phiên bản, số liệu tính tay, query và ca sai đã sửa |
| 2. SQL | JOIN đơn với payment, giải thích nhân dòng | Grain trước/sau JOIN, số liệu đối chiếu, ca hai payment |
| 3. Python đọc file | Đọc CSV, kiểm tra trường thiếu và giá trị sai | Dòng hợp lệ, dòng bị loại và lý do cụ thể |
| 4. Pipeline PostgreSQL | Nạp dữ liệu và xuất báo cáo theo ngày | Chạy một ngày từ đầu vào tới đầu ra, log từng bước |
| 5. Chạy lại và phục hồi | Sửa một ngày, chạy lại, thử một lỗi | Không nhân đôi dữ liệu, kết quả sửa đúng, cách phục hồi |
| 6. Dự án tự làm | Áp dụng vào tình huống mới | Brief, dữ liệu giả lập, code, kiểm tra và phần giải thích |

## Dự án tự làm

Chọn một tình huống: **chi tiêu cá nhân**, **đơn mua hàng online** hoặc **điện sinh hoạt**. Các lựa chọn này là brief để phát triển dự án, chưa có bộ lab/dataset cuối khóa chính thức.

Bắt đầu bằng 5–10 bản ghi giả lập bạn tính tay được. Ví dụ chi tiêu: mỗi dòng là một giao dịch có mã duy nhất, ngày, số tiền nguyên đồng, nhóm chi tiêu và trạng thái; xác định riêng hoàn tiền, không âm thầm gộp vào khoản chi. Chọn hai câu hỏi như “mỗi ngày chi bao nhiêu?” và “nhóm nào chi nhiều nhất?”. Với điện sinh hoạt, phân biệt chỉ số công tơ lũy kế với lượng điện tiêu thụ; chưa tính tiền nếu chưa định nghĩa biểu giá.

Brief cần có grain/khóa, đơn vị, thời gian, metric, quy tắc cho dữ liệu thiếu/trùng/sửa lại và kết quả mong đợi của bộ nhỏ. Sản phẩm bàn giao gồm dữ liệu, code, hướng dẫn chạy cục bộ, báo cáo, ít nhất ba ca kiểm tra và một lỗi đã điều tra. Mentor giúp phản biện từng phần; bạn cần tự giải thích và chạy được sản phẩm.
