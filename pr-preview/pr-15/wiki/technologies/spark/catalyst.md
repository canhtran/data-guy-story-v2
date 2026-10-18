# Catalyst: từ câu SQL đến kế hoạch thực thi Spark

Bạn viết `select` rồi `filter`, nhưng Spark có thể lọc sớm hơn khi điều đó giữ nguyên ý nghĩa truy vấn. Catalyst là bộ máy phân tích và tối ưu kế hoạch của Spark SQL. Nó làm việc với thông tin cột, kiểu dữ liệu và biểu thức; không hiểu tùy ý mọi hàm Python bạn đưa vào.

## Các bước để đọc explain

Một kế hoạch bắt đầu từ yêu cầu logic: đọc nguồn, lọc dòng, chọn cột. Bước phân tích kiểm tra cột và kiểu. Bước tối ưu biến đổi kế hoạch tương đương, chẳng hạn loại cột không dùng hoặc đẩy bộ lọc xuống vị trí phù hợp. Kế hoạch vật lý chọn operator để thực thi.

Đây là cách đọc tổng quát; tên và bố cục operator có thể thay đổi theo phiên bản, source và cấu hình. Thấy `Filter` không đủ để khẳng định bộ lọc đã được đẩy xuống nơi lưu trữ. Với file source, xem thêm `PushedFilters`, `PartitionFilters` và schema đọc.

## Một kế hoạch nhỏ

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}).

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[2]").appName("plan-v1").getOrCreate()
source = spark.range(0, 6).withColumn("double_id", F.col("id") * 2)
result = source.filter(F.col("id") >= 3).select("id")
result.explain("extended")
print([r.id for r in result.orderBy("id").collect()])
spark.stop()
```

Kết quả là `[3, 4, 5]`. Trong optimized plan, biểu thức tạo `double_id` không còn cần thiết vì output không dùng cột này. Các section parsed/analyzed/optimized/physical giúp bạn phân biệt “mình viết gì” và “engine quyết định chạy thế nào”. Đây không phải benchmark hiệu năng.

## Catalyst không kiểm tra nghiệp vụ giúp bạn

Nếu JOIN nhân bản đơn do bảng giá có hai dòng cùng key, Catalyst có thể chạy truy vấn đó rất hiệu quả nhưng tổng doanh thu vẫn sai. Kiểm tra grain, uniqueness và expected output trước khi tối ưu.

Python UDF có thể cần worker Python và không lộ ý nghĩa phép biến đổi như các hàm dựng sẵn. Tránh UDF để làm một phép cộng hoặc xử lý NULL mà API đã có sẵn. Khi UDF thực sự cần thiết, đo chi phí, quy định input/output type và kiểm tra dữ liệu lỗi.

AQE có thể điều chỉnh kế hoạch vật lý trong lúc chạy dựa trên thống kê runtime. Vì vậy, kế hoạch trước action có thể khác kế hoạch cuối. Không chọn cấu hình production chỉ từ một ảnh chụp explain trên ba dòng dữ liệu.

Nếu báo cột không tồn tại, xem schema và tên cột sau JOIN/alias trước. Đó là lỗi phân tích kế hoạch, không phải dấu hiệu thiếu executor.

## Tài liệu gốc

[EXPLAIN 3.5.6](https://spark.apache.org/docs/3.5.6/sql-ref-syntax-qry-explain.html) mô tả các dạng plan. [Performance tuning](https://spark.apache.org/docs/3.5.6/sql-performance-tuning.html#adaptive-query-execution) giải thích AQE. Đối chiếu ngày 1/10/2026.

