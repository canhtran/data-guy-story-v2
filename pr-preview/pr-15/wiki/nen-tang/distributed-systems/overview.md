# Hệ thống phân tán là gì?

Một pipeline đọc nhiều file, chia việc cho vài worker rồi gom kết quả. Nhìn từ bên ngoài đó là một hệ thống; bên trong có nhiều tiến trình trao đổi qua mạng và có thể lỗi độc lập. Đây là điểm xuất phát của hệ thống phân tán.

Không nhất thiết phải thuê cloud. Bạn có thể chạy nhiều tiến trình hoặc container trên máy mình để học. Nhưng chúng cùng phụ thuộc một máy, nên không mô phỏng đầy đủ việc một máy hỏng hay một vùng mất điện.

## Ba worker và một file bị đếm hai lần

Giả sử có ba file với tổng tiền lần lượt 40000, 60000 và 50000 đồng. Bộ điều phối giao mỗi file cho một worker. Tổng đúng là **150000**.

Worker B tính xong 60000 và gửi kết quả, nhưng phản hồi nhận kết quả bị mất. Bộ điều phối giao lại file B. Nếu cộng cả hai lần trả kết quả, tổng thành **210000**. Retry giúp hoàn thành công việc nhưng có thể tạo trùng nếu kết quả không gắn với mã nhiệm vụ.

Một cách thiết kế là lưu một kết quả cho mỗi `task_id`, chỉ cập nhật trạng thái theo quy tắc rõ ràng. Khi đủ ba mã nhiệm vụ, mới tổng hợp. Đây là ví dụ bằng tay, không phải cam kết một thuật toán tổng quát đã chịu mọi lỗi.

## Timeout không cho biết điều gì đã xảy ra

Khi không nhận phản hồi, tiến trình kia có thể đã chết, đang chậm, hoặc đã làm xong nhưng mạng mất phản hồi. Mình chỉ biết không nhận được câu trả lời trong khoảng chờ. Vì thế các quyết định retry, chọn leader và commit phải tính đến sự không chắc chắn này.

Thời gian trên các máy cũng không tự đồng bộ hoàn hảo. Không nên lấy timestamp từ hai máy rồi khẳng định sự kiện nhỏ hơn luôn xảy ra trước về mặt nhân quả. [Lamport: Time, Clocks, and the Ordering of Events](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) phân biệt thứ tự nhân quả với đồng hồ vật lý.

## Được thêm tài nguyên, phải phối hợp nhiều hơn

Chia việc giúp sử dụng nhiều CPU hoặc storage. Đổi lại, truyền dữ liệu, phối hợp trạng thái, xử lý lỗi và quan sát hệ thống đều khó hơn. Với dữ liệu nhỏ, một tiến trình thường dễ vận hành hơn và có thể nhanh hơn do không tốn phối hợp.

Thử ca worker chết sau khi ghi kết quả nhưng trước khi báo xong: bạn sẽ xác định file đó đã được xử lý dựa trên điều gì? Câu trả lời nên dựa trên trạng thái có thể kiểm tra, không chỉ log “đã bắt đầu”.

Đọc tiếp [partitioning]({{< relref "/wiki/nen-tang/distributed-systems/partitioning.md" >}}), [replication]({{< relref "/wiki/nen-tang/distributed-systems/replication.md" >}}) và [idempotency]({{< relref "/wiki/data-engineering/idempotency.md" >}}).

