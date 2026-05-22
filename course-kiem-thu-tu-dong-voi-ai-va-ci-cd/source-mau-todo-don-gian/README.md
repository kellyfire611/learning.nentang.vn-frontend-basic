# Source mẫu TODO đơn giản

Thư mục này là bản source mẫu nhẹ hơn để học viên mới bắt đầu học testing có thể đọc được nhanh.

## App này có gì?
- 1 input để thêm công việc
- 1 danh sách TODO
- 3 bộ lọc: tất cả, chưa xong, đã xong
- 1 nút xóa tất cả việc đã xong

## Vì sao app này dễ học?
- Không có công thức tính tiền, coupon hay nghiệp vụ phức tạp.
- Store chỉ có một file `src/todoStore.js`.
- E2E test rất ngắn, để học viên đọc từng bước.

## Cách chạy

```bash
npm install
npm test
npm run test:e2e
```

## Các file quan trọng
- `src/todoStore.js`: logic chính để viết unit test và business test.
- `src/main.js`: gắn store vào HTML.
- `tests/unit/`: test hàm cơ bản.
- `tests/business/`: test luồng xử lý chính.
- `tests/e2e/`: test thao tác người dùng trên trình duyệt.