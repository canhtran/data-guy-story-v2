# Savepoint trong Flink: mang state sang lần triển khai mới

Bạn muốn đổi phiên bản job nhưng giữ tổng doanh thu và tiến độ đọc. Savepoint là snapshot được quản lý theo thao tác vận hành, thường dùng để dừng có kế hoạch, nâng cấp hoặc chuyển deployment. Nó không bảo đảm mọi code mới đọc được state cũ.

## Checkpoint và savepoint

Checkpoint phục vụ phục hồi tự động theo cấu hình job; vòng đời thường do hệ thống quản lý. Savepoint phục vụ điểm chuyển giao do người vận hành chủ động quản lý. Externalized checkpoint có thể được giữ lại và dùng trong một số thao tác, nên không phân biệt hai loại chỉ bằng “một loại nằm trên disk”.

## Ánh xạ state tới operator

Gán UID ổn định cho operator stateful giúp ánh xạ snapshot vào graph mới. Thay đổi graph làm UID tự sinh khác có thể khiến state không tìm được chỗ restore. UID đúng vẫn chưa đủ: serializer, schema state, max parallelism và semantics mới phải tương thích.

Bài tập kiểm tra bằng tay: phiên bản cũ lưu `total_dong=75000` dạng integer theo key A. Phiên bản mới đổi nghĩa thành `total_usd` nhưng giữ tên state/UID. Dù dữ liệu có đọc được về mặt kiểu, tổng nghiệp vụ vẫn sai. Migration phải kiểm tra cả ý nghĩa và encoding.

## Kế hoạch nâng cấp

Trước khi chuyển: tạo snapshot hoàn tất, ghi đường dẫn/phiên bản/config và giữ input replay được. Khôi phục bản mới trong môi trường kiểm tra, đối chiếu vài key, tiến độ source và output. Lập ranh giới sink để hai job không cùng ghi cạnh tranh. Xác định cách quay lại bản cũ nếu đã có output mới.

Stop-with-savepoint và tùy chọn drain có ảnh hưởng tới event-time timers/window; không mặc định mọi cách dừng cho cùng kết quả. Đối chiếu command và connector của phiên bản đang chạy trước khi thao tác production.

Nếu restore báo state không ánh xạ, kiểm tra UID/graph và metadata snapshot. Cho phép bỏ state không restore được có thể làm mất lịch sử, không phải cách sửa an toàn mặc định. Chỉ xóa snapshot khi hết nhu cầu rollback/khôi phục và hiểu quyền sở hữu các file liên quan.

Bài này đối chiếu Flink 1.20.3, chưa chạy migration job thật; không đưa lệnh vận hành có thể bị hiểu là đã kiểm thử.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/savepoints/) là nguồn đối chiếu cơ chế trong bài.

