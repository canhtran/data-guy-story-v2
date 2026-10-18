# Job, operator, task và subtask trong Flink

Trong code có ba phép biến đổi nhưng UI chỉ hiện hai khối. Có thể Flink đã chain nhiều operator vào một task để giảm chi phí trao đổi. Số dòng API không phải số process, cũng không phải số slot.

## Từ logic tới thực thi

**Job** là chương trình được gửi để thực thi. **Operator** là bước logic như map, filter hoặc keyed aggregation. **Task** có thể chứa một operator hoặc một chain. **Subtask** là một instance song song của task/operator ở mức graph đang xem.

Ví dụ logic: source → parse → keyBy(shop) → tổng tiền → sink. Source và parse có thể chain nếu điều kiện phù hợp. `keyBy` phân phối record theo key và tạo ranh giới trao đổi; nó không tự là một hàm tổng hợp.

## Bài tập đếm

Giả sử có hai task chain: source+parse parallelism 2, aggregate+sink parallelism 3. Số instance thực thi của hai task là 2+3=5. Điều đó không có nghĩa cần đúng năm slot: slot sharing và nhóm tài nguyên quyết định cách bố trí.

Nếu nhìn một operator aggregate có parallelism 3, bạn đang xem ba instance, mỗi instance nhận một phần key. Các record của cùng key phải về instance quản lý key đó; không được cộng tổng A độc lập ở mọi subtask rồi mặc định đã có tổng A chung.

## Khi graph khác dự kiến

Chaining phụ thuộc điều kiện như parallelism, partitioning và cấu hình. Thay parallelism hoặc tắt chaining có thể làm graph khác; không so throughput chỉ theo số ô UI. Xem số record vào/ra từng subtask để xác định operator lọc bỏ dữ liệu hay bị nghẽn.

Nếu parse ném exception ở một record, task có thể restart theo chính sách job. Ghi rõ xử lý record lỗi: dừng, đưa sang luồng lỗi hay bỏ với metric. Bắt mọi exception rồi trả NULL có thể làm job “xanh” nhưng mất dữ liệu âm thầm.

Ví dụ là mô hình kiểm tra bằng tay theo Flink 1.20.3, chưa phải graph đã chạy. Đọc [parallelism]({{< relref "/wiki/technologies/flink/parallelism.md" >}}) để nối số instance với phân bố key.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — flink-architecture](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/flink-architecture/) là nguồn đối chiếu cơ chế trong bài.

