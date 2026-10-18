# Partition trong Spark: chia việc và chia file

Job có tám core nhưng chỉ một task đang chạy. Có thể phần việc đó chỉ có một partition; thêm core chưa chắc giúp được. Partition trong Spark là đơn vị chia dữ liệu để task xử lý, không đồng nghĩa với một máy hay một cửa hàng.

## Hai nghĩa thường bị lẫn

**Execution partition** chia dữ liệu của RDD/DataFrame cho các task. **Partition trên storage** thường là thư mục theo giá trị cột, chẳng hạn `business_date=2026-10-01/`. Một thư mục có thể chứa nhiều file và được đọc thành nhiều execution partition. Số thư mục không phải số task của mọi stage.

## Đổi số partition

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}).

```python
from pyspark.sql import SparkSession

spark = (SparkSession.builder.master("local[2]").appName("partition-v1")
         .config("spark.sql.adaptive.enabled", "false").getOrCreate())
source = spark.range(0, 8, 1, 4)
print(source.rdd.getNumPartitions())
print(source.coalesce(2).rdd.getNumPartitions())
print(source.repartition(3).rdd.getNumPartitions())
print(source.repartition(3).count())
spark.stop()
```

Kết quả lần lượt: `4`, `2`, `3`, `8`. Đổi partition không thay đổi số dòng. `repartition` thực hiện shuffle để phân phối lại; `coalesce` thường giảm partition mà không shuffle, nhưng có thể làm các phần việc mất cân đối. Dùng `coalesce(1)` trước write có thể khiến một task gánh toàn bộ output.

AQE có thể thay đổi số partition sau shuffle lúc runtime. Ví dụ tắt AQE để số partition dễ kiểm chứng. Trong production, đọc kế hoạch cuối và task metrics thay vì suy ra từ cấu hình ban đầu.

## Chọn số partition bằng quan sát

Quá ít partition có thể gây task lớn, spill hoặc thiếu song song. Quá nhiều partition nhỏ gây chi phí lập lịch và nhiều file nhỏ. Không có số partition tối ưu chung cho mọi dataset. Nhìn kích thước input/output, phân bố key, thời gian task và tài nguyên thực tế.

Nếu partition theo `shop` mà 95% dòng thuộc A, dữ liệu A vẫn có thể dồn vào một phần việc lớn. Tăng số partition không tự chia được một key nặng. Đó là skew; cần xem thuật toán tổng hợp, join và phân bố dữ liệu.

`write.partitionBy("business_date")` có ích khi truy vấn thường lọc ngày nghiệp vụ đã được định nghĩa rõ múi giờ. Partition storage theo ID gần như duy nhất có thể tạo hàng triệu thư mục nhỏ. Hãy xem [shuffle]({{< relref "/wiki/technologies/spark/shuffle.md" >}}) trước khi dùng repartition như một thao tác mặc định ở mọi bước.

## Tài liệu gốc

[Performance tuning 3.5.6](https://spark.apache.org/docs/3.5.6/sql-performance-tuning.html) mô tả partition, coalesce hints và AQE. [DataFrame.coalesce](https://spark.apache.org/docs/3.5.6/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.coalesce.html) ghi rõ giới hạn khi giảm mạnh số partition. Đối chiếu ngày 1/10/2026.

