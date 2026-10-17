---
title: "Shuffle trong Spark: vì sao dữ liệu phải đổi chỗ?"
description: "Theo dõi tổng tiền theo key, Exchange, spill và cách giảm dữ liệu trao đổi."
draft: false
contentType: "concept"
weight: 6
level: "beginner"
topics: ["spark"]
prerequisites: []
related: []
---

Partition 1 chứa đơn A trị giá 40.000 và B trị giá 50.000. Partition 2 chứa đơn A trị giá 35.000. Để có một dòng tổng cho A, Spark phải kết hợp thông tin từ hai partition. **Shuffle** là quá trình phân phối lại dữ liệu giữa các partition để thực hiện phép xử lý cần thông tin chung.

## Không phải mọi transformation đều shuffle

`filter` thường xử lý từng partition độc lập. Tổng hợp theo key, sắp xếp toàn cục và nhiều kiểu JOIN cần phân phối lại dữ liệu. Kế hoạch DataFrame thường thể hiện ranh giới đó bằng `Exchange`; không suy ra chỉ từ tên hàm Python.

Shuffle có chi phí serialize, chuyển dữ liệu và đọc/ghi trung gian. Trên cluster, dữ liệu thường qua mạng; trên local vẫn có chi phí và file shuffle. Nếu bộ nhớ không đủ, Spark có thể spill ra đĩa, khiến task chậm hơn.

## Nhìn một Exchange

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}).

```python
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.master("local[2]").appName("shuffle-v1")
         .config("spark.sql.adaptive.enabled", "false")
         .config("spark.sql.shuffle.partitions", "2").getOrCreate())
orders = spark.createDataFrame([("A", 40000), ("B", 50000), ("A", 35000)],
                               "shop string, amount_dong long")
result = orders.groupBy("shop").agg(F.sum("amount_dong").alias("total_dong"))
result.explain()
print([(r.shop, r.total_dong) for r in result.orderBy("shop").collect()])
spark.stop()
```

Kết quả: `[('A', 75000), ('B', 50000)]`. Kế hoạch có tổng hợp cục bộ trước `Exchange` và tổng hợp cuối sau đó. Không nhất thiết mọi dòng nguồn phải được chuyển nguyên vẹn: với tổng tiền, Spark có thể chuyển các tổng trung gian.

## Tối ưu từ câu hỏi dữ liệu

Lọc các đơn không cần thiết và chỉ chọn cột cần dùng trước phép xử lý lớn. Với JOIN bảng nhỏ, xem khả năng broadcast; với tổng hợp, dùng phép tổng hợp thay vì gom danh sách toàn bộ giá trị. Giảm dữ liệu được trao đổi thường có ích hơn đổi một con số cấu hình khi chưa đo.

Một task lâu bất thường có thể do key nặng, file lớn, đĩa chậm hoặc retry. Trong Spark UI, so số byte shuffle read/write, spill và thời gian task giữa các task cùng stage. Chỉ từ việc thấy shuffle không thể kết luận job được viết sai: nhiều bài toán cần shuffle để cho kết quả đúng.

Nếu bị `FetchFailed`, tìm executor đã mất, log trước lỗi và tình trạng đĩa/mạng. Retry có thể giúp lỗi tạm thời; nó không sửa hết đĩa hoặc input key quá lệch.

Đọc [các chiến lược JOIN]({{< relref "/wiki/technologies/spark/join-strategies.md" >}}) để thấy trường hợp đổi cách trao đổi dữ liệu.

## Tài liệu gốc

[RDD guide: shuffle](https://spark.apache.org/docs/3.5.6/rdd-programming-guide.html#shuffle-operations) giải thích chi phí và spill. [SQL performance tuning](https://spark.apache.org/docs/3.5.6/sql-performance-tuning.html) mô tả AQE và tối ưu trao đổi dữ liệu. Đối chiếu ngày 1/10/2026.
