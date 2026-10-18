# Khả năng chịu lỗi

Một worker bị dừng giữa lúc xử lý file. Pipeline có thể chạy lại, nhưng báo cáo sau đó có đúng không? Chịu lỗi không chỉ là tự khởi động lại tiến trình; còn là khôi phục trạng thái và kiểm soát những việc đã thực hiện.

## Đặt ranh giới lỗi trước

Ví dụ tổng tiền ba file là 40000 + 60000 + 50000 = **150000**. Với mỗi nhiệm vụ, thử bốn điểm lỗi:

| Điểm dừng | Cần kiểm tra |
| --- | --- |
| Trước khi đọc | Nhiệm vụ có được giao lại không? |
| Sau khi tính, trước khi lưu | Có tính lại mà không mất file không? |
| Sau khi lưu, trước khi xác nhận | Kết quả có bị cộng hai lần không? |
| Sau khi xác nhận | Kết quả có còn tồn tại khi khôi phục không? |

Đây là bài tập bằng tay để tìm ranh giới commit. Nếu có mã nhiệm vụ và một kết quả được chấp nhận mỗi mã, chạy lại có thể tránh cộng trùng. Nhưng cần bảo vệ trạng thái nhiệm vụ cùng nơi lưu kết quả; hai thao tác tách rời vẫn có khoảng lỗi.

## Checkpoint và replay cần tương thích

Checkpoint ghi vị trí và trạng thái để tiếp tục. Nguồn phải còn dữ liệu cần đọc lại; sink phải xử lý được các kết quả được gửi lại. Nếu checkpoint cũ hơn việc ghi sink, replay có thể tạo trùng. Nếu đánh dấu đã đọc trước khi ghi sink thành công, có thể mất kết quả.

Vì thế phải hỏi “đúng một lần” áp dụng cho trạng thái bên trong hay cả kết quả bên ngoài. Đọc [idempotency]({{< relref "/wiki/data-engineering/idempotency.md" >}}) và [retry]({{< relref "/wiki/data-engineering/retry.md" >}}) để thấy hai phần này phối hợp thế nào.

## Quorum cũng có giới hạn

Ví dụ Raft dùng đa số để duy trì log được đồng thuận. Trong cụm 3 node, đa số là 2; mất một node vẫn có thể tiến triển nếu hai node còn lại liên lạc được. Mất liên lạc với đa số có thể khiến hệ thống ngừng tiến triển để giữ an toàn. Các giả định và cơ chế xem trong [Raft paper](https://raft.github.io/raft.pdf); không áp công thức này cho mọi hệ replication.

Ba container trên cùng laptop không bảo vệ khỏi laptop mất điện. Replication cũng không thay backup chống xóa nhầm. Cần xác định lỗi nào mình muốn chịu và phần nào có chung điểm hỏng.

## Phục hồi là một thứ cần thử

Đo lượng dữ liệu có thể mất và thời gian khôi phục; ghi rõ người hoặc hệ thống nào thực hiện. Với ví dụ nhỏ, kết quả cuối phải là 150000 sau từng ca lỗi và chạy lại. Với hệ thống thật, còn cần kiểm tra dữ liệu trùng, bị thiếu, quyền truy cập và tác động tới người dùng.

Một hệ thống tự chạy lại mãi nhưng không báo nguyên nhân lỗi chưa phải dễ vận hành. Hãy để log chỉ ra nhiệm vụ, checkpoint và trạng thái cuối mà người trực có thể đối chiếu.

