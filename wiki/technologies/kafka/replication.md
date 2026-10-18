# Replication trong Kafka: leader, follower và ISR

Partition P0 có ba bản sao trên broker B1, B2 và B3. B1 làm leader, các follower sao chép log. Nếu B1 mất, Kafka cần chọn leader mới phù hợp để tiếp tục. Có ba replica không tự bảo đảm mọi record đã xác nhận đều sống sót qua mọi loại lỗi.

## ISR là tập replica theo kịp

ISR (in-sync replicas) là tập replica được coi là đủ đồng bộ theo tiêu chí Kafka. Replica quá chậm có thể rời ISR. Replication factor là số bản sao cấu hình; số replica trong ISR là trạng thái hiện tại. Hai con số có thể khác nhau.

Ví dụ kiểm tra bằng tay: replication factor 3, `min.insync.replicas=2`, producer `acks=all`.

| Trạng thái | ISR | Kỳ vọng ghi |
| --- | --- | --- |
| Ba replica theo kịp | B1, B2, B3 | Có thể xác nhận khi điều kiện ghi đáp ứng |
| B3 chậm và rời ISR | B1, B2 | Vẫn đủ mức tối thiểu |
| Chỉ B1 còn trong ISR | B1 | Ghi acks=all bị từ chối vì dưới mức tối thiểu |

Cấu hình ưu tiên độ bền có thể làm hệ thống tạm ngừng ghi thay vì chấp nhận record chỉ còn một bản sao. Ứng dụng phải xử lý lỗi và backlog, không bỏ sự kiện khi broker từ chối.

## Chọn leader và giới hạn

Chọn replica không đồng bộ làm leader có thể khôi phục khả dụng nhưng mất phần log mà nó chưa nhận. Quyết định này phụ thuộc cấu hình và phiên bản. Không bật unclean leader election chỉ để mất cảnh báo mà chưa hiểu rủi ro dữ liệu.

Phân bố replica trên nhiều broker nhưng cùng một máy, đĩa hoặc vùng lỗi vẫn tạo rủi ro chung. Replication không thay backup: xóa topic, retention sai hoặc lỗi nghiệp vụ có thể tác động mọi bản sao.

## Quan sát và phục hồi

Theo dõi under-replicated partitions, offline partitions, thay đổi ISR, dung lượng đĩa và lỗi producer. Nếu follower tụt lại, kiểm tra đĩa, network và tải broker. Nếu ISR giảm cùng lúc ở nhiều partition, tìm nguyên nhân chung trước khi tăng retry client.

[Ví dụ một broker]({{< relref "/wiki/technologies/kafka/overview.md" >}}) có replication factor 1 nên không kiểm chứng failover. Bảng trên là mô hình để đọc cấu hình, chưa phải bài lab mất broker. Muốn chứng minh cam kết durability, phải thử cluster nhiều node và kiểm tra record sau lỗi ở các ranh giới xác nhận.

## Tài liệu gốc

[Kafka design: replication](https://kafka.apache.org/40/design/design/#replication) và [Broker configs 4.0](https://kafka.apache.org/40/configuration/broker-configs/) giải thích ISR, min ISR và lựa chọn leader. Đối chiếu ngày 1/10/2026.

