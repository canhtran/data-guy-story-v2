---
title: "Bảng Fact và Dimension"
description: "Fact và dimension: số đo đi cùng bối cảnh"
draft: false
contentType: "concept"
weight: 2
level: "beginner"
topics: ["data-modeling"]
prerequisites: ["/wiki/nen-tang/data-modeling/overview"]
related: []
---

Trong báo cáo bán hàng, “75000 đồng” là số đo. “Bán món gì, tại cửa hàng nào, ngày nào” là bối cảnh để hiểu số đo đó. Mô hình chiều thường tách hai phần này thành fact và dimension.

**Fact table** ghi sự kiện hoặc trạng thái ở một grain đã xác định. **Dimension** chứa thuộc tính dùng để lọc, nhóm và diễn giải. Đây không đơn giản là “fact toàn số, dimension toàn chữ”: dimension vẫn có khóa số, fact có thể có mã đơn và đôi khi không có đo lường số.

## Một bộ dữ liệu nhỏ

| line_key | product_key | quantity | net_amount_vnd |
| --- | --- | --- | --- |
| 1 | 10 | 2 | 40000 |
| 2 | 20 | 1 | 35000 |

Fact có một dòng mỗi dòng hàng. Dimension sản phẩm có khóa 10 là Cà phê đen, nhóm Cà phê; khóa 20 là Latte, nhóm Cà phê sữa. Nối fact với dimension theo khóa duy nhất giúp báo cáo cộng tiền theo nhóm món mà không lặp dòng.

Tổng tiền là **75000**, tổng số ly **3**. Giá một ly không phải đo lường có thể cộng như tiền dòng hàng: 20000 + 35000 không phải “giá tổng” có ý nghĩa. Giá trung bình theo số ly trong ca này là 75000 / 3 = **25000 đồng**, không phải trung bình đơn giản hai mức giá.

## Đo lường có thể cộng theo chiều nào?

Tiền dòng hàng thường cộng được theo ngày, món và cửa hàng nếu quy tắc tiền tệ giống nhau. Tồn kho cuối ngày có thể cộng giữa các cửa hàng, nhưng cộng nhiều ngày sẽ đếm lại cùng hàng tồn. Tỷ lệ chuyển đổi cần cộng tử số và mẫu số rồi tính lại, không cộng các tỷ lệ.

Fact còn có thể lưu snapshot mỗi kỳ hoặc theo dõi các mốc của một quy trình. Hãy chọn theo câu hỏi; đừng dồn giao dịch và tồn kho ngày vào một bảng rồi để người dùng tự đoán grain.

## Khóa và dòng chưa biết

Khóa nguồn nhận diện sản phẩm; khóa thay thế trong warehouse có thể nhận diện một phiên bản thuộc tính. Khi sản phẩm chưa tới dimension nhưng fact đã tới, cần quy tắc dòng “chưa biết” hoặc chờ xử lý. Đừng âm thầm bỏ fact khỏi báo cáo bằng INNER JOIN.

Bài tập: sản phẩm 10 xuất hiện hai lần trong dimension với cùng khóa. JOIN sẽ tạo bao nhiêu dòng cho fact đầu? Hai. Vì thế kiểm tra tính duy nhất của khóa dimension là kiểm tra trực tiếp độ đúng của báo cáo.

Đọc tiếp [star schema]({{< relref "/wiki/nen-tang/data-modeling/star-schema.md" >}}) và [SCD]({{< relref "/wiki/nen-tang/data-modeling/slowly-changing-dimension.md" >}}). Tham khảo: [Kimball fact tables](https://www.kimballgroup.com/2008/11/fact-tables/).
