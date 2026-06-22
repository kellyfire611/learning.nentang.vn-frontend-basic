# Bài tập quản lý khách hàng quan tâm khóa học

Ứng dụng web đơn giản dùng để quản lý danh sách khách hàng/học viên quan tâm khóa học.

Công nghệ sử dụng:

- HTML
- CSS
- JavaScript thuần
- JSON Server
- Vitest
- Playwright

## 1. Cài đặt

```bash
npm install
```

Cài trình duyệt cho Playwright:

```bash
npx playwright install
```

## 2. Chạy JSON Server

Mở terminal thứ nhất:

```bash
npm run server
```

JSON Server chạy tại:

```txt
http://localhost:3001/customers
```

## 3. Chạy ứng dụng

Mở terminal thứ hai:

```bash
npm run dev
```

Sau đó mở trình duyệt theo URL Vite hiển thị, thường là:

```txt
http://localhost:5173
```

## 4. Chạy test

### Unit test + Business test

```bash
npm run test
```

### Unit test business

```bash
npm run test:unit
```

### Business test Given - When - Then

```bash
npm run test:business
```

### Integration test với JSON Server thật

```bash
npm run test:integration
```

Test integration sẽ tự tạo database tạm và tự khởi động JSON Server ở port `3101`.

### E2E test với Playwright

```bash
npm run test:e2e
```

E2E test sẽ tự chạy:

- JSON Server ở port `3001`
- Vite ở port `5173`

## 5. Cấu trúc thư mục

```txt
bai-tap-contact-json-server/
├── index.html
├── db.json
├── package.json
├── playwright.config.js
├── scripts/
│   └── reset-e2e-db.js
├── src/
│   ├── customerApiStore.js
│   ├── customerBusiness.js
│   ├── app.js
│   └── style.css
├── tests/
│   ├── unit/
│   │   ├── customerBusiness.test.js
│   │   └── customerApiStore.test.js
│   ├── business/
│   │   └── customer-flow.test.js
│   ├── integration/
│   │   └── customer-api.integration.test.js
│   └── e2e/
│       └── customer.e2e.spec.js
├── docs/
│   ├── de-bai.md
│   ├── test-plan.md
│   ├── test-cases.md
│   └── checklist.md
└── README.md
```

## 6. Chức năng đã hoàn thành

- [x] Hiển thị danh sách khách hàng
- [x] Thêm khách hàng mới
- [x] Validate form
- [x] Cập nhật trạng thái đã tư vấn
- [x] Cập nhật trạng thái đã đăng ký
- [x] Sửa thông tin khách hàng
- [x] Xóa khách hàng
- [x] Lọc theo trạng thái/yêu thích
- [x] Tìm kiếm theo họ tên/số điện thoại/email/khóa học
- [x] Loading state
- [x] Empty state
- [x] Error state
- [x] Unit test business
- [x] Unit test API bằng mock fetch
- [x] Business test Given - When - Then
- [x] Integration test với JSON Server thật
- [x] E2E test bằng Playwright

## 7. Ghi chú cho học viên

App được tách thành 3 phần chính:

- `customerBusiness.js`: xử lý nghiệp vụ, validate, lọc, tìm kiếm, cập nhật danh sách.
- `customerApiStore.js`: xử lý gọi API bằng `fetch`.
- `app.js`: xử lý giao diện, render HTML và bắt sự kiện người dùng.

Không nên viết toàn bộ logic vào `index.html`.
