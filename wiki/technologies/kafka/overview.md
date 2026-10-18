# Kafka là gì? Một log sự kiện cho nhiều hệ thống

Một đơn vừa thanh toán cần xuất hiện trong báo cáo, hệ thống giao hàng và kiểm tra gian lận. Nếu ứng dụng bán hàng gọi trực tiếp cả ba hệ thống, một bên chậm có thể kéo theo request bán hàng. Kafka cho phép ứng dụng ghi sự kiện vào một log, rồi các hệ thống đọc theo tiến độ riêng.

Kafka lưu record trong **topic**, chia topic thành **partition**. Producer gửi record; consumer đọc record. Broker phục vụ dữ liệu; controller quản lý metadata và điều phối cluster. Kafka 4.0 dùng KRaft, không dùng hướng dẫn ZooKeeper cũ để cài phiên bản này.

Đọc không xóa record khỏi log. Retention quyết định dữ liệu còn giữ bao lâu hoặc bao nhiêu; consumer chậm quá có thể mất cơ hội replay. Kafka cũng không tự suy ra trạng thái thanh toán đúng từ các sự kiện trùng hoặc sai.

## Thử một broker cục bộ

Ví dụ dùng **Kafka 4.0.2, JDK 17, macOS Intel**, kiểm tra ngày 1/10/2026. Đây là môi trường học một node, không có TLS/xác thực hay khả năng chịu lỗi nhiều broker. Linux/WSL chưa được kiểm thử trong đợt này. Cài JDK 17 và đặt `JAVA_HOME` tới JDK trước; chạy `java -version` để kiểm tra.

Tải bản binary `kafka_2.13-4.0.2.tgz` từ [kho Apache](https://archive.apache.org/dist/kafka/4.0.2/) và giải nén vào thư mục thực hành riêng. Sau đó mở terminal tại thư mục `kafka_2.13-4.0.2`. Tạo file `config/cafe-local.properties` với nội dung sau. Hai listener chỉ nghe trên máy bạn; storage riêng trong `cafe-data-v1`. Nếu thư mục đã có dữ liệu từ bài khác, chọn tên mới thay vì format lại.

```properties
process.roles=broker,controller
node.id=1
controller.quorum.bootstrap.servers=localhost:19093
listeners=PLAINTEXT://127.0.0.1:19092,CONTROLLER://127.0.0.1:19093
advertised.listeners=PLAINTEXT://localhost:19092,CONTROLLER://localhost:19093
controller.listener.names=CONTROLLER
listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
inter.broker.listener.name=PLAINTEXT
log.dirs=./cafe-data-v1
num.partitions=1
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1
```

Tạo ID cho cluster:

```bash
bin/kafka-storage.sh random-uuid
```

Copy UUID nhận được vào lệnh format bên dưới. Chỉ format storage mới dành riêng cho ví dụ, không chạy trên cluster đang có dữ liệu.

```bash
bin/kafka-storage.sh format --standalone -t UUID_VUA_TAO -c config/cafe-local.properties
bin/kafka-server-start.sh config/cafe-local.properties
```

Giữ terminal broker mở. Terminal khác, tại cùng thư mục, chạy:

```bash
bin/kafka-topics.sh --bootstrap-server localhost:19092 --create --topic cafe-v1 --partitions 1 --replication-factor 1
bin/kafka-console-producer.sh --bootstrap-server localhost:19092 --topic cafe-v1
```

Nhập hai dòng, mỗi dòng là một sự kiện; `event_id` là ID sự kiện, `order_id` là ID đơn, tiền là đồng nguyên:

```json
{"event_id":"E1","order_id":101,"amount_dong":40000}
{"event_id":"E2","order_id":102,"amount_dong":35000}
```

Kết thúc producer bằng Ctrl-C rồi đọc bằng group thực hành mới:

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:19092 --topic cafe-v1 --group cafe-reader-v1 --from-beginning --max-messages 2
```

Kết quả là hai dòng JSON vừa nhập, theo thứ tự ghi trong partition duy nhất. Kafka coi value là byte; không tự kiểm tra JSON schema. Nếu chạy lại producer, topic sẽ có thêm record: Kafka không tự loại trùng `event_id`.

Dừng broker bằng Ctrl-C. Khởi động lại với cùng config/storage để giữ dữ liệu; không format lại. Nếu topic đã tồn tại, dùng topic mới hoặc tiếp tục đọc topic cũ và không kỳ vọng chỉ có hai record. Nếu cổng 19092 hoặc 19093 bị chiếm, dừng broker thực hành trước đó hoặc đổi cả listener, advertised listener và địa chỉ client cho phù hợp. Không xóa storage của dịch vụ khác.

## Khi nào cần Kafka?

Kafka hữu ích khi nhiều hệ thống cần cùng luồng sự kiện, cần tách tốc độ xử lý và replay. Nếu chỉ chuyển một file mỗi ngày giữa hai ứng dụng, một pipeline batch có thể đơn giản hơn. Vận hành Kafka thêm chi phí theo dõi lag, dung lượng, replication, bảo mật và schema.

Đọc [topic/partition]({{< relref "/wiki/technologies/kafka/topic-partition.md" >}}) rồi [consumer group]({{< relref "/wiki/technologies/kafka/consumer-group.md" >}}).

## Tài liệu gốc

[Quick Start 4.0](https://kafka.apache.org/40/getting-started/quickstart/) mô tả bootstrap KRaft và console tools. [Kafka design](https://kafka.apache.org/40/design/design/) giải thích mô hình log, retention và replay. Đối chiếu ngày 1/10/2026.

