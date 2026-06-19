# Test Plan - Contact JSON Server

## 1. Phạm vi kiểm thử

Kiểm thử ứng dụng quản lý danh bạ khách hàng gồm các chức năng: tải danh sách, thêm, sửa, xóa, cập nhật trạng thái, lọc, tìm kiếm và xử lý lỗi.

## 2. Các loại test

| Loại test | Mục tiêu | Công cụ |
|---|---|---|
| Unit test | Kiểm tra hàm nhỏ, độc lập | Vitest |
| Business test | Kiểm tra tình huống nghiệp vụ | Vitest |
| Integration test | Gọi JSON Server thật | Vitest + fetch |
| E2E test | Thao tác như người dùng thật | Playwright |

## 3. Môi trường

```bash
npm install
npx playwright install
```

Chạy web và API:

```bash
npm run dev
```

Web chạy tại:

```txt
http://localhost:3000
```

API chạy tại:

```txt
http://localhost:3001/customers
```

## 4. Lệnh chạy test

```bash
npm run test:unit
npm run test:business
npm run test:integration
npm run test:e2e
npm run test:all-with-api
```

## 5. Rủi ro cần lưu ý

- Integration test và E2E test có thể làm thay đổi `db.json`.
- Test cần tự tạo dữ liệu riêng và cleanup sau khi chạy.
- Không nên phụ thuộc vào thứ tự dữ liệu có sẵn trong file `db.json`.
