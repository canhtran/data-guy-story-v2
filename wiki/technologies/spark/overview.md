# Spark là gì? Xử lý dữ liệu bằng nhiều task

Một file doanh thu vài nghìn dòng có thể xử lý bằng SQL hoặc Python trên laptop. Nhưng khi dữ liệu nằm trong hàng nghìn file và một máy không đủ thời gian hay bộ nhớ, bạn cần chia công việc. Apache Spark là một engine xử lý dữ liệu có thể thực thi các phần việc song song trên nhiều máy.

Spark không phải nơi lưu dữ liệu lâu dài. Nó đọc từ hệ thống lưu trữ, biến đổi dữ liệu rồi ghi kết quả ra ngoài. Chạy Spark cũng không tự biến một phép JOIN sai thành đúng: bạn vẫn phải biết mỗi dòng đại diện cho điều gì.

## Một bài toán nhỏ

Quán cà phê có ba đơn đã thanh toán: cửa hàng A nhận 40.000 và 35.000 đồng, cửa hàng B nhận 50.000 đồng. Ta muốn tổng tiền theo cửa hàng. Spark có thể đọc các phần dữ liệu độc lập, tính tổng cục bộ, chuyển các tổng cùng cửa hàng về một nơi rồi cộng lần cuối.

Với ba dòng, chi phí khởi động Spark lớn hơn lợi ích song song. Ví dụ nhỏ giúp nhìn rõ cơ chế; nó không chứng minh Spark nhanh hơn database.

## Môi trường thực hành

Bộ bài này dùng **Spark/PySpark 3.5.6, Python 3.12, JDK 17**, chạy `local[2]` trên macOS Intel. Đây là phiên bản cố định để tái hiện ví dụ, không phải tuyên bố về phiên bản mới nhất. Linux và Windows/WSL chưa được kiểm thử trong đợt này. `local[2]` dùng hai luồng thực thi trên một máy, không dựng cluster hai máy.

Trước khi chạy, cài Python 3.12 và JDK 17 từ nhà phân phối phù hợp hệ điều hành. `JAVA_HOME` phải trỏ tới thư mục JDK chứa `bin/java`; trên macOS, nếu JDK đã đăng ký với hệ thống, có thể dùng lệnh dưới đây. Nếu giải nén JDK riêng, đặt đường dẫn thực tế thay thế.

```bash
java -version
python3.12 --version
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
python3.12 -m venv .venv-spark
source .venv-spark/bin/activate
python -m pip install pyspark==3.5.6
export PYSPARK_PYTHON="$VIRTUAL_ENV/bin/python"
export SPARK_LOCAL_IP=127.0.0.1
```

Các bài tiếp theo cho code Python hoàn chỉnh. Lưu vào file rồi chạy `python ten_file.py` trong môi trường vừa tạo. Chỉ cài thêm pandas/Arrow nếu bài thực sự dùng các API đó.

## Ví dụ đầu tiên

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[2]").appName("cafe-v1").getOrCreate()
orders = spark.createDataFrame(
    [(101, "A", 40000), (102, "A", 35000), (103, "B", 50000)],
    "order_id long, shop string, amount_dong long",
)
result = orders.groupBy("shop").agg(F.sum("amount_dong").alias("total_dong"))
print([(r.shop, r.total_dong) for r in result.orderBy("shop").collect()])
spark.stop()
```

Kết quả: `[('A', 75000), ('B', 50000)]`. Mỗi dòng nguồn là một đơn, `order_id` duy nhất; tiền là số nguyên đồng. Chỉ dùng `collect()` vì kết quả có hai dòng, không áp dụng cách này cho bảng lớn.

## Khi nào dùng, khi nào cân nhắc công cụ khác?

Spark phù hợp với xử lý file lớn, nhiều bước biến đổi và hệ thống đã có tài nguyên phân tán. Nếu dữ liệu vừa một máy, DuckDB hoặc database thường đơn giản hơn. Nếu cần trả lời từng request trong vài mili giây, Spark batch không phải lựa chọn mặc định.

Lỗi `JAVA_GATEWAY_EXITED` thường cần kiểm tra JDK và `JAVA_HOME` trước. Nếu Python worker không khởi động, kiểm tra driver và worker dùng cùng phiên bản Python. Không tăng RAM ngẫu nhiên khi thông báo lỗi đang chỉ ra đường dẫn sai.

Đọc tiếp [kiến trúc Spark]({{< relref "/wiki/technologies/spark/architecture.md" >}}) để biết driver giao việc cho ai.

## Tài liệu gốc

[Hướng dẫn cài PySpark 3.5.6](https://spark.apache.org/docs/3.5.6/api/python/getting_started/install.html) quy định phụ thuộc Python/Java và cách cài bằng pip. [Spark SQL](https://spark.apache.org/docs/3.5.6/sql-programming-guide.html) mô tả DataFrame và engine dùng chung cho SQL/API. Đối chiếu ngày 1/10/2026.

