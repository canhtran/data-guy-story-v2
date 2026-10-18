# Học Data Engineering từ đâu?

Người mới tìm hiểu Data Engineering rất dễ mở cùng lúc mười tab: Python, SQL, Docker, Airflow, Spark, Kafka, AWS, Kubernetes… Sau một hồi, thứ rõ ràng nhất lại là cảm giác mình không biết gì.

Bạn không cần học tất cả những thứ đó để bắt đầu. Điều cần trước tiên là một thứ tự hợp lý.

## Bắt đầu bằng SQL

Phần lớn công việc với dữ liệu vẫn quay về chuyện đọc, kết hợp, tổng hợp và kiểm tra các bảng. SQL vì thế là kỹ năng có ích sớm nhất.

Ở giai đoạn đầu, hãy học chắc:

- `SELECT`, `WHERE`, `GROUP BY` và các hàm tổng hợp.
- Các kiểu `JOIN` và điều gì xảy ra khi khoá không duy nhất.
- CTE và window function.
- Cách kiểm tra kết quả thay vì chỉ thấy query chạy thành công.

Sau SQL cơ bản, học đọc execution plan (kế hoạch database dùng để thực thi query) khi bắt đầu tìm hiểu vì sao truy vấn chậm.

Bạn chưa cần thuộc mọi cú pháp. Mục tiêu là nhìn một bộ dữ liệu và biết cách đặt câu hỏi bằng SQL.

## Học một ngôn ngữ lập trình đủ dùng

Python là lựa chọn dễ bắt đầu vì được dùng rộng rãi trong data tooling. Java hoặc Scala trở nên quan trọng hơn ở một số hệ thống lớn, nhưng không cần học cả ba cùng lúc.

Với Python, hãy tập trung vào những phần phục vụ công việc:

- Đọc và ghi file, gọi API, kết nối database.
- Hàm, module, package và quản lý dependency.
- Xử lý lỗi và ghi log.
- Viết test cho logic biến đổi quan trọng.
- Làm việc với cấu trúc dữ liệu và dữ liệu lớn hơn bộ nhớ ở mức khái niệm.

Một project nhỏ chạy từ đầu đến cuối có giá trị hơn nhiều notebook rời rạc.

## Hiểu database trước khi học hệ thống dữ liệu lớn

Hãy biết dữ liệu được lưu trong bảng như thế nào, transaction giải quyết vấn đề gì, index giúp gì và vì sao một query có thể chậm. Những kiến thức này tiếp tục xuất hiện trong warehouse, pipeline và distributed systems dưới nhiều hình thức khác nhau.

Bạn có thể thực hành với PostgreSQL trên máy cá nhân. Một database nhỏ đủ để học phần lớn khái niệm nền tảng.

## Tự xây một pipeline đơn giản

Chọn một API công khai hoặc một file dữ liệu, viết chương trình lấy dữ liệu về, kiểm tra nó rồi lưu vào PostgreSQL. Sau đó viết vài query để trả lời một câu hỏi cụ thể.

Project đầu tiên chỉ cần có:

1. Một nguồn dữ liệu.
2. Một bước thu thập.
3. Một vài quy tắc làm sạch.
4. Một nơi lưu trữ.
5. Một đầu ra có người đọc được.

Sau khi chạy được, hãy thử chạy lần hai. Nếu data bị nhân đôi, pipeline chưa có Idempotency (khả năng chạy lại nhiều lần mà không tạo thêm kết quả ngoài ý muốn). Thử làm API lỗi giữa chừng, thay đổi một cột hoặc gửi data thiếu. Đây là lúc project bắt đầu dạy bạn cách pipeline thật sự vận hành.

## Học data modeling và chất lượng dữ liệu

Đưa dữ liệu vào database mới là nửa đầu công việc. Người khác còn phải hiểu và tin được nó.

Hãy học cách tách dữ liệu thô khỏi dữ liệu đã xử lý, chọn grain cho một bảng, hiểu fact và dimension, rồi thêm các kiểm tra như khoá không được rỗng, giá trị phải nằm trong khoảng hợp lệ hoặc số bản ghi không giảm bất thường.

## Chỉ thêm công cụ khi project cần

Khi có nhiều job và dependency, hãy tìm hiểu một orchestrator như Airflow. Khi dữ liệu không còn xử lý tốt trên một máy, hãy học Spark. Khi bài toán cần event liên tục và độ trễ thấp, hãy tìm hiểu Kafka và Flink.

Học theo vấn đề giúp bạn hiểu vì sao công cụ tồn tại. Nếu bắt đầu từ việc cài một stack thật lớn, bạn có thể chạy được demo nhưng khó biết nên dùng nó lúc nào.

## Cloud, Docker và distributed systems

Bạn nên biết Docker cơ bản để tạo môi trường có thể chạy lại. Cloud cũng đáng học vì nhiều hệ thống dữ liệu được triển khai ở đó. Tuy vậy, đừng biến chứng chỉ cloud thành điều kiện để bắt đầu viết pipeline đầu tiên.

Distributed systems là phần cần học dần. Replication, partitioning, consistency và fault tolerance sẽ dễ hiểu hơn khi bạn đã gặp giới hạn của một database hoặc một máy xử lý.

## Một thứ tự gợi ý

Nếu cần một danh sách ngắn, hãy đi theo thứ tự này:

1. SQL.
2. Python và Git.
3. Database.
4. Một pipeline nhỏ chạy end-to-end.
5. Data modeling và data quality.
6. Orchestration và cloud cơ bản.
7. Batch processing, streaming và distributed systems khi bài toán yêu cầu.

## Học đến đâu thì chuyển sang bước tiếp theo?

Bạn có thể dùng chính project của mình để trả lời. Với SQL, thử nối đơn hàng với item rồi kiểm tra tổng tiền: bạn có nhận ra khi nào JOIN làm doanh thu tăng lên không? Nếu hai đơn cùng giá, query của bạn có còn tính đủ cả hai không?

Với Python, thử đọc một API có nhiều trang. Đọc được trang đầu chưa đủ; chương trình cần đi hết `next_page`, và nếu một trang lỗi thì log phải cho mình biết lỗi ở đâu. Khi lưu vào database, thử chạy lại cùng dữ liệu. Bốn đơn vẫn phải là bốn đơn. Thử làm bước ghi thất bại nữa, để thấy rollback giữ dữ liệu cũ như thế nào.

Đến lúc làm được những việc đó và giải thích được kết quả, bạn đã có thể học tiếp. Không cần đợi đến khi nhớ hết cú pháp hay biết mọi công cụ.

Lộ trình Nền tảng Data Engineer riêng vẫn đang được biên soạn. Trong lúc đó, bạn có thể bắt đầu bằng project dưới đây.

## Project: report đơn hàng theo ngày và khu vực

Nếu chưa biết chọn dữ liệu nào, mình dùng tiếp bài toán đơn hàng. Lần này có bốn đơn giả lập riêng cho project, đủ nhỏ để bạn tính bằng tay. Bạn chỉ cần sao chép các khối bên dưới thành file tương ứng, chưa cần kết nối dịch vụ bên ngoài.

Report cần cho biết mỗi ngày, mỗi khu vực có bao nhiêu đơn và doanh thu bao nhiêu. Trong project này, mình chỉ tính doanh thu cho đơn đã giao (`delivered`) và có thanh toán thành công (`paid`). Tiền là số nguyên VND, chưa xét phí hay hoàn tiền. Ngày của đơn lấy từ `created_at`, đổi sang giờ Singapore trước khi lấy ngày.

Mỗi row trong `orders` là một đơn, trong `restaurants` là một nhà hàng, còn trong `payments` là một lần thanh toán. Chỗ cuối đáng để ý: một đơn có thể thanh toán thất bại rồi thử lại.

`restaurants.csv`:

```csv
restaurant_id,restaurant_name,area
RES-18,Cơm Nhà,Tampines
RES-19,Bếp Nhỏ,Bedok
```

Phần đơn hàng được chia thành hai file JSON, giống như API trả dữ liệu theo từng trang. Bạn có thể viết hàm `fetch_page(page)` để đọc file tương ứng trước; sau này thay phần đọc file bằng lời gọi HTTP. Trường `next_page` cho biết còn trang nào cần lấy. Khi nó là `null` thì mới hết dữ liệu.

`orders-page-1.json`:

```json
{
  "data": [
    {"order_id":"LAB-01","restaurant_id":"RES-18","status":"delivered","total_amount":120000,"created_at":"2026-09-06T12:02:10+08:00"},
    {"order_id":"LAB-02","restaurant_id":"RES-18","status":"delivered","total_amount":120000,"created_at":"2026-09-06T13:00:00+08:00"}
  ],
  "next_page": 2
}
```

`orders-page-2.json`:

```json
{
  "data": [
    {"order_id":"LAB-03","restaurant_id":"RES-19","status":"cancelled","total_amount":50000,"created_at":"2026-09-06T14:00:00+08:00"},
    {"order_id":"LAB-04","restaurant_id":"RES-19","status":"delivered","total_amount":80000,"created_at":"2026-09-06T16:05:00Z"}
  ],
  "next_page": null
}
```

`payments.csv`:

```csv
payment_id,order_id,status
PAY-01,LAB-01,failed
PAY-02,LAB-01,paid
PAY-03,LAB-02,paid
PAY-04,LAB-04,paid
```

### Từ file nguồn đến report

Trước hết, thử đọc đủ hai trang JSON và hai file CSV. Bạn sẽ có bốn đơn, hai nhà hàng và bốn lần thanh toán. Giữ lại file gốc trong thư mục raw của lần chạy, đồng thời ghi log trang nào đã đọc và nhận được bao nhiêu row. Nếu số lượng chưa khớp, mình có chỗ để quay lại tìm.

Sau đó đưa data vào PostgreSQL, dùng `order_id`, `restaurant_id` và `payment_id` làm khoá chính cho từng bảng. Tải vào bảng chuẩn bị để kiểm tra trước: mã có bị thiếu hoặc trùng không, số tiền có âm không, timestamp có đọc được không? Trạng thái cần thuộc những giá trị đã dùng trong dữ liệu mẫu, và mỗi payment phải tìm được order tương ứng. Khi nguồn đã đủ và các kiểm tra đều qua, mới dùng dữ liệu đó để tạo report.

Khi ghép bảng, thử nhìn riêng `LAB-01`. Đơn này có hai lần thanh toán nhưng chỉ được xuất hiện một lần trong đầu ra. Bạn có thể dùng `EXISTS` như ở bài về AI, hoặc tổng hợp payment về một row mỗi đơn trước khi nối. Cũng cần giữ cả những đơn chưa có thanh toán trong tổng số đơn; LEFT JOIN có ích ở chỗ này.

Cuối cùng, nhóm theo ngày tạo và khu vực. `total_orders` đếm cả đơn huỷ, còn `paid_delivered_orders` chỉ đếm đơn đã giao và thanh toán thành công. Report sẽ ra như sau:

| order_date | area | total_orders | paid_delivered_orders | revenue (VND) |
| --- | --- | ---: | ---: | ---: |
| 2026-09-06 | Tampines | 2 | 2 | 240,000 |
| 2026-09-06 | Bedok | 1 | 0 | 0 |
| 2026-09-07 | Bedok | 1 | 1 | 80,000 |

Hai đơn Tampines cùng giá vẫn là hai đơn riêng. Đơn huỷ ở Bedok góp vào số đơn nhưng không góp doanh thu. `LAB-04` được tạo lúc 00:05 ngày 7 theo giờ Singapore. Tổng doanh thu là `320,000` VND.

### Khi report đã chạy được

Bây giờ thử chạy lại với cùng các file. Trong bảng vẫn phải có bốn đơn và report vẫn ra cùng số tiền. Bạn có thể dùng upsert, tức thêm mới hoặc cập nhật theo khoá, hay thay toàn bộ các bảng nhỏ trong một transaction. Điều cần kiểm tra là lần chạy sau không nối thêm bốn đơn nữa.

Tiếp theo, cho `fetch_page(2)` báo lỗi một lần trước khi trả data. Chương trình có thể thử lại, tối đa ba lần tổng cộng. Nhìn log, bạn cần biết nó đang lấy trang 2, vì sao lỗi và đã thử bao nhiêu lần. Khi lấy được trang đó, report phải trở về đúng kết quả phía trên.

Nếu cả ba lần đều thất bại thì sao? Lúc này chỉ có trang 1, nên chưa thể thay report cũ. Hãy giữ bản thành công trước đó và kết thúc lần chạy với thông báo lỗi. Nếu đây là lần đầu chạy, chưa có report nào để công bố.

Bạn cũng có thể thử bỏ `PAY-03` khỏi lần chạy đầu rồi thêm lại ở lần sau, như một thanh toán đến muộn. Doanh thu Tampines ngày 6 sẽ đi từ 120,000 lên 240,000 VND, trong khi tổng số đơn vẫn là bốn. Muốn sửa đúng con số này, pipeline phải tính lại ngày cũ từ dữ liệu hiện có, chứ không chỉ nhìn ngày hôm nay.

Đến đây, thử nhờ một người khác chạy project theo README của bạn. Họ cần biết cách chạy, mỗi row đại diện cho gì và doanh thu được tính thế nào. Giữ cả log của lần thành công, lần chạy lại và lần lỗi để giải thích vì sao bạn tin kết quả đó.

Từ những tình huống vừa gặp, bài [Một Data Pipeline hoạt động ra sao?]({{< relref "/wiki/data-engineering/data-pipeline.md" >}}) sẽ dễ theo dõi hơn. Đó cũng là bài đầu của [nhóm nhập môn Data Engineering]({{< relref "/wiki/data-engineering/_index.md" >}}#mới-tìm-hiểu-data-engineering).

