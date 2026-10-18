# Đọc CSV và JSON: đọc được chưa có nghĩa đúng kiểu

Một file CSV có ô `40000`, nhưng khi đọc bằng `csv.DictReader`, giá trị thường là chuỗi. Nếu cộng mà chưa kiểm tra kiểu, chương trình có thể lỗi hoặc thực hiện một việc khác với phép cộng tiền.

CSV mô tả các trường trên dòng; dấu phân cách, quoting và encoding phải được thống nhất. JSON biểu diễn object, array, số, boolean và null, nhưng đọc JSON thành công không chứng minh schema nghiệp vụ đúng.

## Một vòng đọc và ghi trên máy

Ví dụ dùng Python 3.12, thư viện chuẩn, đã chạy kiểm tra. Lưu thành `doc_file.py`, chạy như [bài đầu]({{< relref "/wiki/nen-tang/python/overview.md" >}}). Script tạo thư mục tạm riêng, ghi fixture, đọc lại và dọn thư mục khi kết thúc; không ghi đè file của bạn.

Mỗi dòng là một đơn, mã duy nhất, trạng thái `paid` hoặc `cancelled`. Số tiền là đồng nguyên không âm.

```python
import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory

fixture = "order_id,status,amount_vnd\n1,paid,40000\n2,cancelled,50000\n3,paid,60000\n"
with TemporaryDirectory(prefix="cafe-files-") as folder:
    source = Path(folder) / "orders.csv"
    source.write_text(fixture, encoding="utf-8")
    total = 0
    seen = set()
    with source.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["order_id", "status", "amount_vnd"]:
            raise ValueError("Header không đúng hợp đồng")
        for row in reader:
            order_id = int(row["order_id"])
            amount = int(row["amount_vnd"])
            if order_id in seen or amount < 0:
                raise ValueError("Trùng khóa hoặc số tiền âm")
            if row["status"] not in {"paid", "cancelled"}:
                raise ValueError("Trạng thái không hợp lệ")
            seen.add(order_id)
            if row["status"] == "paid":
                total += amount
    report = {"cửa_hàng": "Quán nhỏ", "revenue_vnd": total}
    output = Path(folder) / "report.json"
    output.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
    restored = json.loads(output.read_text(encoding="utf-8"))
    print(restored["cửa_hàng"], restored["revenue_vnd"])
```

Đầu ra: **Quán nhỏ 100000**. `newline=""` để module CSV xử lý newline; `encoding="utf-8"` làm rõ cách giải mã. `ensure_ascii=False` giữ chữ Việt dễ đọc trong file JSON, không thay đổi ý nghĩa dữ liệu.

## Thử ca hỏng

Đổi số tiền đơn 3 thành `sáu mươi`: `int` phải báo lỗi, không biến thành 0. Đổi mã đơn 3 thành 1: kiểm tra khóa trùng phải từ chối. Đổi `paid` thành `PAID`: ví dụ từ chối vì chưa có quy tắc chuẩn hóa. Nếu nguồn cho phép cả hai, sửa hợp đồng rồi mới sửa code.

Ví dụ nhỏ chưa kiểm tra hết số cột thừa/thiếu trên mỗi dòng, BOM, kích thước lớn hoặc mọi định dạng số. Khi áp dụng cho file ngoài, cần bổ sung kiểm tra cấu trúc dòng và giới hạn input. Không dùng `split(',')` thay parser khi trường có thể chứa dấu phẩy trong dấu nháy.

Nguồn: [Python csv](https://docs.python.org/3/library/csv.html), [Python json](https://docs.python.org/3/library/json.html). Xem tiếp [xử lý lỗi]({{< relref "/wiki/nen-tang/python/errors-and-logging.md" >}}).

