---
title: "Structured Streaming: micro-batch, checkpoint và output"
description: "Đọc file tăng dần, kiểm tra restart và hiểu điều kiện để tránh output trùng."
draft: false
contentType: "concept"
weight: 9
level: "beginner"
topics: ["spark"]
prerequisites: []
related: []
---

Mỗi vài giây có file đơn mới. Bạn muốn cập nhật kết quả mà không đọc lại tất cả file đã xử lý. Structured Streaming dùng các phép biến đổi DataFrame trên dữ liệu đến dần; chế độ micro-batch xử lý các lô nhỏ và ghi nhận tiến độ.

Bài này dùng file JSON đến dần, không kết nối Kafka. Ví dụ chỉ kiểm tra tiến độ nguồn và file sink sau restart, không mô phỏng lỗi cluster giữa lúc commit.

## Một input, một checkpoint, một output

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}). Mỗi dòng là một đơn, ID duy nhất. Chưa có phép tổng hợp theo thời gian nên không cần watermark. Ba thư mục được tạo trong vùng tạm và xóa sau khi kết thúc.

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[2]").appName("stream-v1").getOrCreate()
with TemporaryDirectory() as tmp:
    base = Path(tmp)
    source = base / "input"
    source.mkdir()
    output = str(base / "output")
    checkpoint = str(base / "checkpoint")
    def add_file(name, row):
        (source / name).write_text(json.dumps(row) + "\n", encoding="utf-8")
    def run_once():
        stream = spark.readStream.schema("order_id long, amount_dong long").json(str(source))
        query = (stream.writeStream.format("parquet").outputMode("append")
                 .option("path", output).option("checkpointLocation", checkpoint)
                 .trigger(availableNow=True).start())
        query.awaitTermination()
    add_file("batch1.json", {"order_id": 101, "amount_dong": 40000})
    run_once()
    add_file("batch2.json", {"order_id": 102, "amount_dong": 35000})
    run_once()
    run_once()  # Không thêm file: không được ghi lại hai đơn cũ.
    result = spark.read.parquet(output).orderBy("order_id")
    print([(r.order_id, r.amount_dong) for r in result.collect()])
spark.stop()
```

Kết quả: `[(101, 40000), (102, 35000)]`. `availableNow` xử lý input sẵn có rồi kết thúc, tiện kiểm tra hữu hạn; muốn chạy liên tục cần chọn trigger phù hợp. File nguồn thực tế phải được đưa vào hoàn chỉnh, thường bằng rename nguyên tử trên filesystem hỗ trợ; không để query đọc file đang ghi dở.

## Checkpoint không phải tùy chọn trang trí

Checkpoint chứa tiến độ và, với truy vấn stateful, trạng thái xử lý. Mỗi query có checkpoint riêng trên storage bền vững mà các lần chạy sau truy cập được. Ví dụ dùng vùng tạm để học nên không bảo vệ dữ liệu qua lần chạy script mới.

Nếu xóa checkpoint, query có thể đọc lại nguồn. Nếu đổi schema hoặc phép xử lý stateful, không mặc định checkpoint cũ tương thích. Lập kế hoạch migration và replay với kiểm tra output; không xóa checkpoint production chỉ để hết lỗi.

## Event time, watermark và bảo đảm đầu cuối

Event time là thời điểm sự kiện xảy ra, khác lúc Spark nhận được. Khi tổng hợp cửa sổ, bạn cần định nghĩa timestamp/múi giờ và chính sách dữ liệu đến muộn. Watermark giúp giới hạn state; nó không sửa timestamp sai và không có nghĩa mọi sự kiện muộn đều sẽ được giữ.

Khả năng tránh output trùng còn tùy source có replay được và sink có commit phù hợp. `foreachBatch` mặc định có thể gọi lại cùng batch; cần dùng batch ID hoặc khóa nghiệp vụ để ghi idempotent. Checkpoint không làm một HTTP API bất kỳ trở thành exactly-once. Khi ID đơn xuất hiện trong hai file khác nhau, ví dụ trên vẫn ghi hai dòng: theo dõi file không phải deduplicate nghiệp vụ.

Nếu query đứng lâu, xem `lastProgress`, input rate, processing rate, thời gian batch và lỗi sink. Kiểm tra storage/checkpoint trước khi tăng executor.

## Tài liệu gốc

[Structured Streaming guide 3.5.6](https://spark.apache.org/docs/3.5.6/structured-streaming-programming-guide.html) mô tả file source, triggers, checkpoint, output modes và bảo đảm theo từng sink. Đối chiếu ngày 1/10/2026.
