---
title: "Mô hình ngôi sao"
description: "Star schema: làm báo cáo từ fact và các chiều"
draft: false
contentType: "concept"
weight: 3
level: "beginner"
topics: ["data-modeling"]
prerequisites: ["/wiki/nen-tang/data-modeling/overview"]
related: []
---

Báo cáo cần doanh thu theo món, cửa hàng và ngày. Một cấu trúc dễ đọc là đặt fact bán hàng ở giữa, nối trực tiếp tới các dimension sản phẩm, cửa hàng và ngày. Nhìn sơ đồ giống ngôi sao, nên gọi là star schema.

Bài này dùng dữ liệu giả lập riêng, không cần café fixture. Bạn có thể chạy truy vấn dưới đây trong SQLite 3.25 trở lên; CTE tạo toàn bộ dữ liệu ngay trong câu lệnh.

## Thử một nhánh của ngôi sao

```sql
WITH dim_product(product_key, product_name, category) AS (
  VALUES (10,'Cà phê đen','Cà phê'),(20,'Latte','Cà phê sữa')
), fact_sales(line_key, product_key, net_amount_vnd) AS (
  VALUES (1,10,40000),(2,20,35000)
)
SELECT d.category, SUM(f.net_amount_vnd) AS revenue_vnd
FROM fact_sales AS f
JOIN dim_product AS d ON f.product_key = d.product_key
GROUP BY d.category
ORDER BY d.category;
```

Kết quả: **Cà phê, 40000** và **Cà phê sữa, 35000**. Mỗi dòng fact là một dòng hàng; mỗi khóa dimension chỉ khớp một dòng. Trong mô hình đầy đủ, fact còn có `store_key`, `date_key` để nối tới các dimension tương ứng.

## Vì sao để thuộc tính ở dimension?

Tên và nhóm món được quản lý ở một nơi, truy vấn dùng tên dễ hiểu, và các báo cáo có thể dùng chung cách phân loại. Nếu nhiều fact cùng dùng dimension ngày hoặc sản phẩm, phải thống nhất ý nghĩa và khóa; giống tên cột chưa đủ để coi chúng dùng chung được.

Dimension thường để các thuộc tính phân cấp như cửa hàng, thành phố, vùng trong cùng bảng. Điều này giảm số JOIN và dễ sử dụng, nhưng lặp lại một số giá trị. Star schema ưu tiên thuận tiện cho phân tích; không phải mục tiêu loại bỏ mọi sự lặp như trong một số thiết kế OLTP.

## Những chỗ dễ sai

Thêm mã đơn vào fact dòng hàng không làm grain thành một đơn. Nối fact bán hàng trực tiếp với fact thanh toán có thể tạo quan hệ nhiều–nhiều. Nên tổng hợp về cùng mức hoặc phân tích riêng trước khi kết hợp.

Khi thuộc tính sản phẩm thay đổi, star schema vẫn cần chính sách lịch sử. [SCD]({{< relref "/wiki/nen-tang/data-modeling/slowly-changing-dimension.md" >}}) giải thích vì sao cùng mã sản phẩm có thể có nhiều khóa phiên bản.

Star schema hữu ích khi người dùng thường lọc, nhóm và tổng hợp theo các chiều rõ ràng. Nó không thay thế mọi mô hình lưu trữ nguồn hay thiết kế sự kiện.

Tham khảo: [Kimball star schema](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/). So sánh với [snowflake schema]({{< relref "/wiki/nen-tang/data-modeling/snowflake-schema.md" >}}).
