# DataFrame trong Spark: schema, lọc và tổng hợp

Một DataFrame có các cột có tên và kiểu dữ liệu, nhưng không phải toàn bộ bảng đã nằm trong RAM laptop. Nó biểu diễn dữ liệu và kế hoạch xử lý; Spark thực thi khi có action. Nếu quen SQL, bạn có thể dùng DataFrame API và SQL cho cùng bài toán.

## Schema là thỏa thuận đầu vào

Mỗi dòng sau là một đơn hàng; `order_id` là khóa nghiệp vụ. Spark không tự áp đặt uniqueness hay foreign key cho DataFrame. `amount_dong` là số nguyên đồng, `NULL` nghĩa là chưa biết tiền, không phải đơn có giá trị bằng 0.

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}).

```python
from tempfile import TemporaryDirectory
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[2]").appName("schema-v1").getOrCreate()
orders = spark.createDataFrame(
    [(101, "A", 40000, "paid"), (102, "A", 35000, "paid"),
     (103, "B", 50000, "paid"), (104, "B", None, "pending")],
    "order_id long, shop string, amount_dong long, status string",
)
paid = orders.filter(F.col("status") == "paid")
summary = paid.groupBy("shop").agg(F.sum("amount_dong").alias("total_dong"))
print([(r.shop, r.total_dong) for r in summary.orderBy("shop").collect()])
print(orders.filter(F.col("amount_dong").isNull()).count())
with TemporaryDirectory() as tmp:
    summary.write.mode("overwrite").parquet(tmp + "/summary")
    print(spark.read.parquet(tmp + "/summary").count())
spark.stop()
```

Ba kết quả lần lượt là `[('A', 75000), ('B', 50000)]`, `1`, `2`. Thư mục tạm chỉ chứa output của ví dụ; thao tác overwrite không chạm dữ liệu khác. Parquet output là một thư mục chứa các part file, không đảm bảo một file có tên do bạn chọn.

## Những lỗi dễ lọt qua

`amount_dong == None` không thay thế `isNull()`. So sánh SQL với NULL không cho kết quả true; filter có thể loại dòng mà bạn tưởng sẽ giữ lại. `sum` bỏ qua NULL, vì vậy tổng có vẻ hợp lý vẫn có thể thiếu đơn. Theo dõi số dòng thiếu riêng và định nghĩa chính sách trước khi điền bằng 0.

Khi đọc CSV, suy luận schema trên mẫu có thể không phù hợp dữ liệu ngày sau. Chọn schema rõ ràng, kiểm tra các dòng parse lỗi và quy định cách xử lý. DataFrame không có thứ tự mặc định: dùng `orderBy` nếu kết quả cần thứ tự để kiểm tra; sort toàn bộ bảng có chi phí.

## SQL và API

Bạn có thể tạo temporary view bằng `orders.createOrReplaceTempView("orders")` rồi truy vấn với `spark.sql(...)`. View này thuộc session, không tự tạo bảng bền vững trong một database. Dùng API nào dễ đọc hơn, nhưng giữ cùng schema, logic NULL và kiểm tra output.

Ưu tiên hàm dựng sẵn như `sum`, `when`, `to_timestamp` trước Python UDF. Hàm dựng sẵn cho engine nhiều thông tin hơn để tối ưu; UDF còn có chi phí chuyển dữ liệu và thực thi Python.

Đọc tiếp [Catalyst]({{< relref "/wiki/technologies/spark/catalyst.md" >}}) để hiểu vì sao hai cách viết có thể dẫn đến kế hoạch tương tự.

## Tài liệu gốc

[Spark SQL getting started 3.5.6](https://spark.apache.org/docs/3.5.6/sql-getting-started.html), [NULL semantics](https://spark.apache.org/docs/3.5.6/sql-ref-null-semantics.html) và [Parquet](https://spark.apache.org/docs/3.5.6/sql-data-sources-parquet.html) là các tài liệu cho schema/API, giá trị thiếu và đọc ghi file. Đối chiếu ngày 1/10/2026.

