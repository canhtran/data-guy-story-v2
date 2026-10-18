# JOIN trong Spark: broadcast hay phân phối hai bên?

Bảng đơn có hàng tỷ dòng, bảng cửa hàng chỉ vài trăm dòng. Nếu mỗi executor giữ một bản bảng cửa hàng, nhiều phép JOIN có thể thực hiện ngay bên cạnh dữ liệu đơn. Đó là ý tưởng của broadcast join. Nhưng trước khi chọn thuật toán, cần chắc kết quả JOIN đúng.

## Đừng để một key nhân đôi doanh thu

Mỗi đơn có một `shop_id`; bảng cửa hàng phải có đúng một dòng cho mỗi `shop_id` trong ví dụ. Nếu A có hai dòng tên cửa hàng, mỗi đơn A sẽ JOIN thành hai dòng. Broadcast không loại duplicate này. Nếu bảng lưu lịch sử, bạn phải bổ sung điều kiện thời gian hoặc chọn phiên bản phù hợp nghiệp vụ.

## So hai kế hoạch

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}). Tiền là số nguyên đồng; ID đơn duy nhất.

```python
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.master("local[2]").appName("join-v1")
         .config("spark.sql.adaptive.enabled", "false")
         .config("spark.sql.autoBroadcastJoinThreshold", "-1")
         .config("spark.sql.shuffle.partitions", "2").getOrCreate())
orders = spark.createDataFrame([(101, "A", 40000), (102, "A", 35000), (103, "B", 50000)],
                               "order_id long, shop_id string, amount_dong long")
shops = spark.createDataFrame([("A", "Trung tâm"), ("B", "Bến xe")],
                              "shop_id string, shop_name string")
broadcast_join = orders.join(F.broadcast(shops), "shop_id")
merge_join = orders.hint("merge").join(shops.hint("merge"), "shop_id")
broadcast_join.explain()
merge_join.explain()
for result in (broadcast_join, merge_join):
    print([(r.order_id, r.shop_name) for r in result.orderBy("order_id").collect()])
spark.stop()
```

Cả hai cho `[(101, 'Trung tâm'), (102, 'Trung tâm'), (103, 'Bến xe')]`. Kế hoạch đầu có `BroadcastHashJoin`, kế hoạch sau có `SortMergeJoin`. Ta tắt auto broadcast và AQE để đối chiếu; hint là yêu cầu ưu tiên, không bảo đảm mọi loại JOIN đều hỗ trợ thuật toán đó.

## Chi phí khác nhau

Broadcast hash join chuyển bên nhỏ đến executor, cần đủ bộ nhớ và thời gian broadcast. Không ép broadcast một bảng lớn chỉ để né shuffle. Sort-merge join thường phân phối theo key và sort hai bên; nó phù hợp với nhiều equi-join lớn nhưng có chi phí trao đổi/sắp xếp.

Spark còn có shuffled hash join và các chiến lược cho điều kiện khác equality. Optimizer dựa vào loại JOIN, thống kê, kích thước và cấu hình; AQE có thể đổi chiến lược khi đã có thống kê runtime.

Nếu một task JOIN rất chậm, kiểm tra skew và multiplicity của key. Với A chiếm phần lớn đơn, repartition theo `shop_id` vẫn có thể giữ A chung một partition. Nếu timeout broadcast, kiểm tra kích thước thật và tài nguyên trước khi tăng timeout.

Ví dụ này kiểm chứng cùng kết quả và hai operator, không chứng minh chiến lược nào nhanh hơn trên dữ liệu production.

## Tài liệu gốc

[Join strategy hints và AQE 3.5.6](https://spark.apache.org/docs/3.5.6/sql-performance-tuning.html) mô tả ưu tiên hint, broadcast và chuyển chiến lược runtime. Đối chiếu ngày 1/10/2026.

