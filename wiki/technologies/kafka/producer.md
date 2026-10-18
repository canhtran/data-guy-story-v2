# Kafka producer: gửi thành công nghĩa là gì?

Ứng dụng gọi `send` rồi trả “thành công”, nhưng broker vẫn chưa xác nhận record. Producer thường gom record và gửi bất đồng bộ; việc đưa record vào buffer client khác với việc broker đã nhận theo yêu cầu durability.

## Theo dõi một lần gửi

Producer serialize key/value, chọn partition, gom batch rồi gửi tới leader. Kết quả gửi được trả qua future/callback theo API client. Ứng dụng cần quan sát lỗi gửi và lỗi khi kết thúc, không bỏ qua callback rồi coi dữ liệu đã bền vững.

| `acks` | Producer chờ gì? |
| --- | --- |
| `0` | Không chờ xác nhận broker |
| `1` | Leader ghi nhận record |
| `all` | Các replica trong ISR hiện tại xác nhận theo cơ chế broker |

`acks=all` không có nghĩa mọi broker đều giữ record, cũng không yêu cầu tất cả replica cấu hình luôn online. Kết hợp `min.insync.replicas` để quy định số replica đồng bộ tối thiểu khi chấp nhận ghi.

## Retry có thể tạo duplicate ở đâu?

Ví dụ kiểm tra bằng tay: broker nhận E1, nhưng response mất. Client không biết E1 đã được ghi, nên retry. Idempotent producer giúp broker nhận diện retry trong phạm vi cơ chế producer, tránh ghi duplicate do lần gửi đó.

Nhưng nếu ứng dụng đọc lại đơn rồi gọi `send` lần nữa với E1 như một sự kiện mới, Kafka không tự deduplicate theo `event_id` trong JSON. Consumer hoặc sink vẫn cần khóa nghiệp vụ nếu yêu cầu không ghi trùng.

Với Java producer 4.0, idempotence yêu cầu `acks=all`, retries lớn hơn 0 và `max.in.flight.requests.per.connection` không quá 5. Kiểm tra cấu hình client thực tế; tên/default của thư viện Python hay ngôn ngữ khác có thể khác.

## Batching và lỗi

Batch lớn và thời gian chờ gom batch có thể giảm overhead, nhưng đổi latency. Không sao chép cấu hình throughput cao nếu ứng dụng cần phản hồi nhanh. Khi timeout, kiểm tra broker còn truy cập được, advertised listener, metadata, quyền ghi và ISR trước khi tăng mọi timeout.

Console producer trong [bài tổng quan]({{< relref "/wiki/technologies/kafka/overview.md" >}}) chỉ kiểm chứng gửi/đọc hai record local. Kịch bản mất response ở đây là lập luận về cơ chế, chưa phải fault-injection test. Muốn chứng minh durability phải kiểm tra nhiều broker và lỗi tại ranh giới xác nhận.

## Tài liệu gốc

[Producer configs 4.0](https://kafka.apache.org/40/configuration/producer-configs/) quy định acks, idempotence, retry và batching. [Broker configs](https://kafka.apache.org/40/configuration/broker-configs/) quy định `min.insync.replicas`. Đối chiếu ngày 1/10/2026.

