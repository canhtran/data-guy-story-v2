# dbt

Một câu SQL chạy đúng hôm nay vẫn cần cách chạy lại và kiểm tra dữ liệu ngày mai. Hai bài dưới đây dùng bốn đơn hàng để thực hành công việc đó, không cần cloud hay dịch vụ trả phí.

1. [Project đầu tiên]({{< relref "overview.md" >}}): cài môi trường riêng, seed, ref, hai model và đọc báo cáo.
2. [Kiểm tra dữ liệu]({{< relref "data-tests.md" >}}): cố tình tạo đơn trùng, tiền âm, đọc FAIL/SKIP rồi khôi phục.
3. [Incremental model]({{< relref "incremental.md" >}}): nạp đơn mới, sửa bản ghi mới nhất, nhận diện dữ liệu cũ bị bỏ sót và chạy full refresh.
4. [Snapshots]({{< relref "snapshots.md" >}}): lưu hai phiên bản trạng thái đơn và phân biệt lịch sử quan sát với CDC.

Đã kiểm tra bằng dbt Core 1.10.18, dbt-duckdb 1.10.0, DuckDB 1.4.3 trên Python 3.12/macOS Intel. Chưa kiểm thử Windows/Linux. Source freshness, tài liệu hóa project và vận hành theo lịch còn đang biên soạn; adapter PostgreSQL và Iceberg chưa được kiểm tra trong bộ bài này.

