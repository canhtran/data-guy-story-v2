# Pandas: báo cáo đơn hàng quán cà phê

Nguồn demo 0.1 · 02/10/2026 · Khoảng 30–45 phút. Đây là một buổi thử độc lập, không phải toàn bộ khóa Data Engineering.

## Mục tiêu và hợp đồng dữ liệu

Tự tạo môi trường Python, chạy pandas DataFrame, lọc đơn hoàn tất, tính doanh thu theo cửa hàng và xuất CSV. Mỗi dòng là **một đơn hàng**, `order_id` duy nhất. `amount_vnd` là số nguyên VND của cả đơn, không phải đơn giá. Chỉ `completed` được tính doanh thu; `cancelled` bị loại. Chưa xét hoàn tiền, thuế, chiết khấu, dữ liệu lỗi hay múi giờ.

## Cách thử cùng NotebookLM

Upload file Markdown này bằng Add sources; hoặc nhập URL của trang demo khi đã xuất bản công khai. Localhost không dùng được. Kiểm tra nguồn có phiên bản 0.1, bảng năm đơn và code Python. Nhập nguồn không tự cấu hình mentor: sao chép prompt mentor từ trang demo vào Configure Chat → Custom (nếu có), hoặc dán vào chat, rồi gửi “Bắt đầu demo pandas”.

## Checkpoint 1 — Kiểm tra Python

Mentor hỏi hệ điều hành trước. macOS/Linux chạy `python3 --version`; Windows PowerShell chạy `py --version`. Dùng Python **3.11–3.14** với pandas **3.0.6** trong demo này. Nếu chưa có Python, cài từ https://www.python.org/downloads/, mở terminal mới và kiểm tra lại. Windows có thể cần bật tùy chọn thêm Python vào PATH; nếu `py` không có nhưng `python --version` đúng, dùng `python` thay `py` ở bước tạo môi trường. Linux thiếu `venv`: hỏi bản phân phối và lỗi cụ thể trước khi chọn gói cài đặt. Không gõ code Python trực tiếp vào terminal shell.

Checkpoint đạt khi gửi được lệnh và phiên bản thực tế. Mentor chờ kết quả trước khi bước tiếp.

## Checkpoint 2 — Tạo môi trường riêng và cài pandas

macOS/Linux, chạy từng lệnh:

```sh
mkdir pandas-cafe-demo
cd pandas-cafe-demo
python3 -m venv .venv
.venv/bin/python -m pip install pandas==3.0.6
.venv/bin/python -c "import pandas as pd; print(pd.__version__)"
```

Windows PowerShell, chạy từng lệnh:

```powershell
mkdir pandas-cafe-demo
cd pandas-cafe-demo
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pandas==3.0.6
.\.venv\Scripts\python.exe -c "import pandas as pd; print(pd.__version__)"
```

Dùng trực tiếp Python trong `.venv`, không cần activate. Cài thư viện cần Internet. Nếu thư mục đã tồn tại, vào thư mục đó hoặc chọn tên mới; không xóa dữ liệu cũ. Checkpoint đạt khi in `3.0.6`.

## Checkpoint 3 — Tạo và chạy DataFrame đầu tiên

Trong thư mục vừa tạo, dùng trình soạn thảo lưu file **demo.py** (không phải `demo.py.txt` hay `pandas.py`). Nhập đoạn dưới:

```python
import pandas as pd

orders = pd.DataFrame([
    {"order_id": "O001", "store": "A", "status": "completed", "amount_vnd": 40000},
    {"order_id": "O002", "store": "A", "status": "cancelled", "amount_vnd": 50000},
    {"order_id": "O003", "store": "A", "status": "completed", "amount_vnd": 60000},
    {"order_id": "O004", "store": "B", "status": "completed", "amount_vnd": 30000},
    {"order_id": "O005", "store": "B", "status": "completed", "amount_vnd": 70000},
])
print(orders.to_string(index=False))
print("Rows:", len(orders))
print("Columns:", list(orders.columns))
```

Chạy macOS/Linux: `.venv/bin/python demo.py`. Windows: `.\.venv\Scripts\python.exe demo.py`.

DataFrame là bảng có hàng và cột. Một cột như `orders["status"]` là Series. `len(orders)` đếm hàng, không cộng tiền. Kết quả: 5 hàng; các cột `order_id`, `store`, `status`, `amount_vnd`. Gửi đầu ra và giải thích một hàng đại diện cho gì.

## Checkpoint 4 — Tự viết báo cáo

Thêm code sau đoạn tạo DataFrame. Thử từng yêu cầu, chạy lại và gửi kết quả:

1. Giữ các dòng có `status` bằng `completed` trong biến `completed`.
2. In số đơn hoàn tất và tổng `amount_vnd` của chúng.
3. Tạo DataFrame `report`: mỗi dòng một `store`, gồm `order_count` và `revenue_vnd`.
4. Xuất `report` ra `daily_report.csv` không kèm cột index. Đọc lại CSV để kiểm tra.

Gợi ý cấp 1: tạo điều kiện so sánh từ cột status rồi dùng nó để chọn hàng. Gợi ý cấp 2: `orders.loc[orders["status"].eq("completed")].copy()`. Tổng tiền dùng `.sum()`. Theo cửa hàng dùng `.groupby("store", as_index=False).agg(...)`, với phép tổng cho tiền và đếm đơn. Xuất dùng `.to_csv("daily_report.csv", index=False)`; đọc dùng `pd.read_csv("daily_report.csv")`.

Đối chiếu sau khi thử: 4 đơn hoàn tất, doanh thu **200000 VND**. Cửa hàng A: 2 đơn, 100000 VND; B: 2 đơn, 100000 VND. Cộng cả đơn hủy sẽ ra 250000 VND và sai hợp đồng. CSV nằm trong thư mục đang chạy lệnh; chạy lại sẽ ghi đè chính file báo cáo này.

Checkpoint chỉ đạt khi gửi code, kết quả tổng và nội dung CSV đọc lại; giải thích vì sao bỏ đơn O002. Thứ tự hàng hoặc khoảng trắng khi in không quan trọng.

## Checkpoint 5 — Thử một thay đổi

Đổi O002 từ `cancelled` sang `completed`. Dự đoán trước khi chạy: số đơn, doanh thu tổng và cửa hàng nào thay đổi? Sau đó chạy để đối chiếu. Khôi phục dữ liệu gốc trước khi lưu báo cáo cuối buổi. Mentor yêu cầu giải thích, không chỉ nhận đáp số.

## Gỡ lỗi theo bằng chứng

- `ModuleNotFoundError: pandas`: gửi lệnh đang chạy; kiểm tra có dùng đúng Python trong `.venv` không, rồi chạy lại lệnh kiểm tra phiên bản.
- Không tìm thấy `demo.py`: gửi thư mục hiện tại (`pwd` hoặc `Get-Location`) và danh sách file (`ls` hoặc `Get-ChildItem`); kiểm tra tên file.
- `KeyError`: gửi `list(orders.columns)` và dòng lỗi; tên cột phân biệt chữ hoa/thường.
- Lỗi import khi đặt tên `pandas.py`: đổi tên file demo, rồi thử lại.
- Doanh thu 250000: kiểm tra bảng sau lọc và điều kiện status trước khi sửa phép tổng.

Mentor hỏi một kiểm tra mỗi lần, chờ đầu ra rồi mới kết luận.

## Nhật ký kết thúc

Phiên bản demo: 0.1. Hệ điều hành / Python / pandas: … Checkpoint đã chứng minh: … Lệnh và đầu ra: … Vì sao phải lọc đơn hủy: … CSV ở đâu: … Điều còn kẹt: … Bước tiếp theo: … Lưu nhật ký và dán lại khi tiếp tục.

## Tài liệu tham khảo

- Cài pandas trong môi trường riêng: https://pandas.pydata.org/docs/getting_started/install.html
- DataFrame: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
- Đọc/ghi CSV: https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
