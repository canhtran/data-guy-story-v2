---
title: "Python: bắt đầu từ một script tính doanh thu"
description: "Hiểu biến, vòng lặp và hàm qua dữ liệu ba đơn hàng."
draft: false
contentType: concept
weight: 1
level: beginner
topics: [python]
prerequisites: []
related: []
---

Bạn đã tính doanh thu bằng SQL. Python hữu ích khi cần đọc nhiều file, kiểm tra từng bản ghi hoặc gọi các bước xử lý theo thứ tự. Mình bắt đầu bằng một script nhỏ để thấy rõ dữ liệu đi qua code thế nào.

## Chạy ở đâu?

Ví dụ đã kiểm tra trên Python 3.12, dùng thư viện chuẩn, không cần cài package. Kiểm tra `python3 --version` trên macOS/Linux hoặc `py -3 --version` trên Windows. Nếu thiếu, dùng [trang tải chính thức](https://www.python.org/downloads/) và hướng dẫn đúng hệ điều hành. Windows chưa được kiểm thử trong đợt này.

Lưu code vào file UTF-8 tên `doanh_thu.py` trong thư mục học riêng, mở terminal ở thư mục đó và chạy `python3 doanh_thu.py` hoặc `py -3 doanh_thu.py`.

## Từ bản ghi tới tổng

Mỗi dictionary là một đơn có mã duy nhất. Tiền là số nguyên đồng; chỉ trạng thái `paid` được tính. Ví dụ chưa xử lý hoàn tiền hoặc nhiều đơn vị tiền tệ.

```python
orders = [
    {"order_id": 1, "status": "paid", "amount_vnd": 40000},
    {"order_id": 2, "status": "cancelled", "amount_vnd": 50000},
    {"order_id": 3, "status": "paid", "amount_vnd": 60000},
]

def paid_revenue(rows):
    total = 0
    for row in rows:
        if row["status"] == "paid":
            total += row["amount_vnd"]
    return total

print(paid_revenue(orders))
print(paid_revenue([]))
```

Kết quả là **100000**, rồi **0**. `orders` là list các dòng; `row` nhận từng dòng trong vòng lặp. Hàm nhận dữ liệu qua tham số, trả kết quả bằng `return`. Thụt đầu dòng xác định phần thuộc vòng lặp và điều kiện, không chỉ để trang trí.

## Chạy được chưa đủ

Thêm một bản sao đơn 1, tổng thành 140000. Hàm chưa biết khóa bị trùng; chính mình phải xác định quy tắc nhận diện và kiểm tra trùng. Đổi `amount_vnd` thành chuỗi `"40000"` cũng khác với số 40000: dữ liệu từ CSV cần chuyển kiểu trước khi cộng.

Nếu gặp `KeyError`, một dòng có thể thiếu cột cần dùng. Nếu gặp `TypeError`, kiểm tra kiểu của các giá trị tham gia phép toán. Không bắt mọi lỗi rồi trả 0, vì báo cáo sẽ trông hợp lệ dù dữ liệu hỏng.

Với list rỗng, hàm trả 0 vì đó là hợp đồng mình vừa viết. Trong một pipeline thật, “không nhận được file” có thể là lỗi, khác với “file hợp lệ và không có đơn”. Quyết định ở bước đọc dữ liệu trước khi gọi hàm.

Đọc tiếp [CSV và JSON]({{< relref "/wiki/nen-tang/python/files-and-json.md" >}}). Tham khảo cú pháp tại [Python tutorial](https://docs.python.org/3/tutorial/controlflow.html).
