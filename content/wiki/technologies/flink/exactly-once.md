---
title: "Exactly-once trong Flink: state đúng, sink có đúng không?"
description: "Phân biệt replay record với ảnh hưởng một lần và kiểm tra connector."
draft: false
contentType: "concept"
weight: 11
level: "beginner"
topics: ["flink"]
prerequisites: []
related: []
---

Sau restart, log cho thấy một record được xử lý hai lần. Điều đó không tự chứng minh exactly-once state đã hỏng: Flink có thể replay record nhưng phục hồi state về trước lần xử lý đầu, để ảnh hưởng cuối chỉ xuất hiện một lần trong state.

## Tính lại từ checkpoint

Checkpoint lưu A=40000 và vị trí đọc tiếp E2. E2/A/35000 đã chạy, rồi job chết. Restore đưa state về 40000 và replay E2, kết quả là 75000. Nếu giữ state 75000 rồi cộng lại E2 thì mới thành 110000 và sai.

Ví dụ là phép tính tay. Nó giả định source replay được, snapshot hoàn tất và phép xử lý phù hợp cơ chế phục hồi. Nguồn không replay được hoặc side effect bên ngoài có thể phá bảo đảm đầu cuối.

## Sink cần phối hợp

Nếu lần xử lý E2 đầu đã `INSERT` vào database và lần replay lại INSERT, state đúng vẫn có thể đi cùng output trùng. Connector hỗ trợ giao dịch có thể phối hợp commit với checkpoint; sink idempotent có thể dùng khóa xác định và ghi lại cùng giá trị.

Một phép tăng tiền ở database không tự idempotent. Muốn áp dụng mỗi sự kiện một lần, có thể cần ledger event ID và cập nhật số dư trong cùng transaction. Kiểm tra chính xác guarantee của connector/version, isolation của người đọc và cấu hình checkpoint.

## Duplicate nghiệp vụ là vấn đề khác

Nếu Kafka chứa E2 hai lần ở hai vị trí khác nhau, exactly-once engine không tự deduplicate E2. Engine có thể xử lý mỗi record nguồn một cách nhất quán và vẫn cộng hai lần. Cần chính sách event identity, state deduplicate và thời hạn giữ theo nghiệp vụ.

“Exactly-once” cũng không hứa rằng kết quả không bao giờ sửa: dữ liệu muộn hợp lệ có thể cập nhật cửa sổ. Sink phải hiểu upsert/changelog thay vì coi mọi emit là một dòng append độc lập.

## Kiểm tra đúng ranh giới

Fault test cần lỗi trước/sau sink commit và checkpoint completion, rồi so output theo key, số dòng và metric với oracle. Job restart thành công hoặc checkpoint có dấu xanh chưa đủ. Theo dõi retention nguồn để không mất khả năng replay trước khi restore.

Bài này đối chiếu Flink 1.20.3 và không tuyên bố đã fault-test một connector thật.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — stateful-stream-processing](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/stateful-stream-processing/) là nguồn đối chiếu cơ chế trong bài.
