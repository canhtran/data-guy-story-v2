# Công nghệ

Bạn đã hiểu một pipeline cần làm gì; phần này đi vào cách các công cụ cụ thể thực hiện công việc đó. Mỗi hub cho biết phạm vi bài đã có, phiên bản đối chiếu và ví dụ nào đã được kiểm tra.

## Xử lý dữ liệu

- [Apache Spark]({{< relref "/wiki/technologies/spark/_index.md" >}}): 9 bài về DataFrame/RDD, thực thi, partition, shuffle, JOIN và Structured Streaming. Có ví dụ local đã kiểm tra bằng PySpark 3.5.6.
- [Apache Flink]({{< relref "/wiki/technologies/flink/_index.md" >}}): 11 bài khái niệm về kiến trúc, state, event time, watermark và phục hồi. Ví dụ là bài tập kiểm tra bằng tay; lab local còn đang biên soạn.

## Truyền sự kiện và tích hợp

[Apache Kafka]({{< relref "/wiki/technologies/kafka/_index.md" >}}): 9 bài về topic/partition, producer, consumer group, offset, replication và transaction. Ví dụ một broker Kafka 4.0.2 đã được kiểm tra gửi/đọc, replay bằng group khác và giữ dữ liệu qua restart. Các tình huống nhiều broker và transaction là giải thích cơ chế, chưa phải fault test.

## Cơ sở dữ liệu và truy vấn

- [DuckDB]({{< relref "/wiki/technologies/duckdb/_index.md" >}}): 4 bài và ví dụ đã chạy với DuckDB 1.4.3/Python 3.12, gồm CSV/JSON/Parquet, transaction, chạy lại và xử lý lỗi tài nguyên.
- **PostgreSQL — đang biên soạn:** cần môi trường thực hành, nhập/xuất dữ liệu, quyền truy cập và sao lưu/khôi phục.

## Biến đổi dữ liệu

- [dbt]({{< relref "/wiki/technologies/dbt/_index.md" >}}): 4 bài về project local, data test, incremental và snapshot với DuckDB. Adapter PostgreSQL, source freshness và vận hành theo lịch còn đang biên soạn.

## Các nhóm đang biên soạn

- **Điều phối và biến đổi:** Airflow; cần bài về mô hình thực thi, lịch chạy và vận hành.
- **Lưu trữ:** HDFS, MinIO và Iceberg; cần kiến trúc, thao tác đọc/ghi, quyền truy cập và phục hồi.
- **Môi trường và hạ tầng:** Docker, cấu hình dịch vụ, log/metric và công cụ platform; cần ví dụ có thể tái hiện trên máy người học.

Các mục này chưa có bộ bài hoàn chỉnh. Chưa tạo hub rỗng để thay cho hướng dẫn; bài sẽ được bổ sung sau khi có nội dung và kiểm tra phù hợp.

## Trước khi chọn công cụ

Xem [Nền tảng]({{< relref "/wiki/nen-tang/_index.md" >}}) nếu cần SQL, transaction hoặc partitioning. Xem [Data Engineering]({{< relref "/wiki/data-engineering/_index.md" >}}) để chọn kiểu pipeline và hiểu idempotency, retry, storage trước khi đi vào cấu hình sản phẩm.

