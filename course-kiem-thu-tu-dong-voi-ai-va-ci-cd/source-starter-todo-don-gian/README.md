# Source starter TODO đơn giản

Thư mục này dành cho học viên mới bắt đầu tự làm bài trước khi xem đáp án.

## Bản này có sẵn gì?
- Giao diện TODO app và toàn bộ source chạy được.
- Tài liệu `test-plan` và `test-cases` viết sẵn bằng tiếng Việt có dấu.
- Các file test chỉ để khung `todo` hoặc `skip` để học viên tự hoàn thiện.
- Chưa có workflow CI hoàn chỉnh để học viên tự tạo.

## Cách học
1. Chạy app và tự bấm thử các chức năng.
2. Đọc `docs/student-tasks.md`.
3. Viết test từng bước từ unit đến E2E.
4. Sau cùng so sánh với `../source-mau-todo-don-gian/`.

## Cách chạy

```bash
npm install
npm run serve
npm test
npm run test:e2e
```

## Lưu ý
- Bản starter dùng cổng `3107` để không đụng bản đáp án dùng cổng `3106`.
- `npm test` sẽ hiện `todo`, còn `npm run test:e2e` sẽ hiện `skipped` cho tới khi học viên tự viết test.