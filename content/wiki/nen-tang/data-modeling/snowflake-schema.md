---
title: "Mô hình bông tuyết"
description: "Snowflake schema: khi dimension được tách thêm"
draft: false
contentType: "concept"
weight: 4
level: "beginner"
topics: ["data-modeling"]
prerequisites: ["/wiki/nen-tang/data-modeling/overview"]
related: []
---

Trong star schema, dimension sản phẩm có cả tên món và tên nhóm món. Nếu tách nhóm món sang một bảng riêng, fact phải đi qua sản phẩm rồi tới nhóm. Dimension phân nhánh thêm, tạo cấu trúc gọi là snowflake schema.

Đây là tên một kiểu mô hình dữ liệu, không có nghĩa phải dùng sản phẩm Snowflake hay dịch vụ cloud.

## So sánh bằng hai bảng nhỏ

Trong mô hình tách, `dim_product` có sản phẩm 10 → nhóm 1, sản phẩm 20 → nhóm 2. `dim_category` có nhóm 1 → Cà phê, nhóm 2 → Cà phê sữa. Fact lưu tiền dòng hàng như bài star schema.

Truy vấn sau tự tạo dữ liệu bằng CTE, chạy được trong SQLite 3.25 trở lên:

```sql
WITH dim_category(category_key, category_name) AS (
  VALUES (1,'Cà phê'),(2,'Cà phê sữa')
), dim_product(product_key, category_key) AS (
  VALUES (10,1),(20,2)
), fact_sales(line_key, product_key, net_amount_vnd) AS (
  VALUES (1,10,40000),(2,20,35000)
)
SELECT c.category_name, SUM(f.net_amount_vnd) AS revenue_vnd
FROM fact_sales AS f
JOIN dim_product AS p ON f.product_key = p.product_key
JOIN dim_category AS c ON p.category_key = c.category_key
GROUP BY c.category_name
ORDER BY c.category_name;
```

Kết quả vẫn là **Cà phê, 40000** và **Cà phê sữa, 35000**. So với star, thêm một JOIN để lấy tên nhóm.

## Đổi lại được gì?

Bảng nhóm có thể quản lý thuộc tính dùng chung ở một nơi và giảm lặp trong dimension. Nhưng người viết báo cáo phải hiểu nhiều bảng hơn; mô hình quyền, lịch sử và kiểm tra khóa cũng có thêm quan hệ.

Không thể kết luận snowflake luôn chậm hơn chỉ từ số JOIN. Hiệu năng phụ thuộc engine, kích thước và kế hoạch. Cũng không nên chọn nó chỉ vì thấy các chuỗi tên nhóm lặp lại: lặp có chủ đích trong dimension có thể giúp mô hình dễ sử dụng.

## Lịch sử không biến mất khi tách bảng

Nếu sản phẩm chuyển nhóm vào giữa tháng, thay `category_key` trên dòng sản phẩm sẽ làm báo cáo cũ được nhìn theo nhóm mới. Nếu yêu cầu giữ phân loại lúc bán, cần phiên bản và thời gian hiệu lực phù hợp. Cả star và snowflake đều phải giải quyết câu hỏi nghiệp vụ này.

Bài tập: xóa nhóm 2 khỏi CTE dimension nhóm. INNER JOIN sẽ làm mất dòng doanh thu Latte. Với bảng thật, dùng khóa ngoại hoặc kiểm tra chất lượng để phát hiện, thay vì để báo cáo âm thầm hụt 35000 đồng.

Tham khảo: [Microsoft: star schema guidance, snowflake dimensions](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema). Đọc trước [star schema]({{< relref "/wiki/nen-tang/data-modeling/star-schema.md" >}}).
