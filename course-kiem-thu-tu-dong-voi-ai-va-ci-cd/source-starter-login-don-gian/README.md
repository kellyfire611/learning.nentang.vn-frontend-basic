# Source starter login đơn giản

Thư mục này dành cho học viên tự luyện test trước khi xem đáp án.

## Bản này có sẵn gì?
- Giao diện đăng nhập và source app chạy được.
- Tài liệu `docs/test-plan.md`, `docs/test-cases.md`, `docs/student-tasks.md`.
- File test mới ở mức khung (`todo` hoặc `skip`) để học viên tự viết.
- Chưa có workflow CI hoàn chỉnh để học viên tự cấu hình.

## Cách học
1. Chạy app và bấm thử các tình huống login đúng/sai.
2. Đọc toàn bộ tài liệu trong `docs/`.
3. Viết unit test trước, rồi business test, cuối cùng E2E test.
4. Sau cùng so sánh với `../source-mau-login-don-gian/`.

## Cách chạy

```bash
npm install
npm run serve
npm test
npm run test:e2e
```

## Lưu ý
- Bản starter dùng cổng `3109` để không đụng bản đáp án dùng cổng `3108`.
- `npm test` sẽ hiện `todo`, còn `npm run test:e2e` sẽ hiện `skipped` cho tới khi học viên tự hoàn thiện.