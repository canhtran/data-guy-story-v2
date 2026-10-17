---
title: "Dimension thay đổi chậm (SCD)"
description: "SCD: giữ lịch sử hay sửa lại thuộc tính?"
draft: false
contentType: "concept"
weight: 5
level: "beginner"
topics: ["data-modeling"]
prerequisites: ["/wiki/nen-tang/data-modeling/overview"]
related: []
---

Cửa hàng S1 chuyển từ vùng Bắc sang vùng Trung từ ngày 01/09. Báo cáo doanh thu tháng 8 nên thuộc vùng nào? Nếu câu trả lời là “vùng lúc bán”, mình phải giữ phiên bản cũ thay vì ghi đè mọi thứ.

Slowly Changing Dimension — SCD — là nhóm cách xử lý thuộc tính dimension thay đổi. “Slowly” không đảm bảo dữ liệu thay đổi ít; quyết định chính là cần nhìn lịch sử theo cách nào.

## Type 1 và Type 2

**Type 1** ghi đè giá trị. Nó phù hợp khi sửa lỗi tên hoặc người dùng muốn mọi báo cáo nhìn theo phân loại hiện tại. **Type 2** thêm một dòng phiên bản với khóa thay thế mới, phù hợp khi muốn giữ thuộc tính có hiệu lực lúc sự kiện xảy ra.

Ví dụ Type 2, thời điểm theo giờ Việt Nam và khoảng hiệu lực **[từ, đến)**:

| store_key | store_id | region | valid_from | valid_to |
| --- | --- | --- | --- | --- |
| 11 | S1 | Bắc | 2026-01-01 | 2026-09-01 |
| 12 | S1 | Trung | 2026-09-01 | NULL |

`store_id` nhận diện cửa hàng trong nguồn; `store_key` nhận diện phiên bản trong warehouse. Bản ghi bán ngày 31/08 dùng khóa 11; bán ngày 01/09 dùng khóa 12.

## Thử nối theo thời gian

Truy vấn độc lập dưới đây chạy trong SQLite 3.25 trở lên. Ngày dùng định dạng ISO thống nhất, không trộn múi giờ:

```sql
WITH dim_store(store_key, store_id, region, valid_from, valid_to) AS (
  VALUES (11,'S1','Bắc','2026-01-01','2026-09-01'),
         (12,'S1','Trung','2026-09-01',NULL)
), sales(sale_id, store_id, business_date, amount_vnd) AS (
  VALUES (1,'S1','2026-08-31',40000),
         (2,'S1','2026-09-01',35000)
)
SELECT s.sale_id, d.store_key, d.region
FROM sales AS s
JOIN dim_store AS d ON s.store_id = d.store_id
  AND s.business_date >= d.valid_from
  AND (d.valid_to IS NULL OR s.business_date < d.valid_to)
ORDER BY s.sale_id;
```

Kết quả: **1, 11, Bắc** và **2, 12, Trung**. Dùng `< valid_to` giúp sự kiện đúng ranh giới ngày 01/09 chỉ khớp phiên bản mới. Khi nạp fact thật, thường xác định khóa phiên bản rồi lưu khóa đó vào fact.

## Các ca phải kiểm tra

Hai khoảng hiệu lực chồng nhau sẽ làm một sự kiện khớp hai phiên bản. Khoảng bị hở có thể làm sự kiện không khớp dòng nào. Dữ liệu đến muộn cần tìm theo thời gian sự kiện, không mặc định lấy phiên bản đang hiện hành.

Nếu nhận một sửa đổi lịch sử, phải quyết định cập nhật lại phiên bản và fact nào. Nạp lại cùng thay đổi không được tạo thêm phiên bản trùng. Type 2 cũng không tự giữ “ngày hệ thống biết thông tin”: nếu cần cả lịch sử hiệu lực nghiệp vụ lẫn lịch sử nhận biết, mô hình cần bổ sung một trục thời gian nữa.

Đừng chọn một loại SCD cho toàn bộ dimension theo thói quen. Tên sửa lỗi có thể Type 1, vùng kinh doanh có thể Type 2, tùy câu hỏi báo cáo.

Tham khảo: [Kimball: Type 1](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-1/) và [SCD Type 2](https://www.kimballgroup.com/2008/09/slowly-changing-dimensions-part-2/).
