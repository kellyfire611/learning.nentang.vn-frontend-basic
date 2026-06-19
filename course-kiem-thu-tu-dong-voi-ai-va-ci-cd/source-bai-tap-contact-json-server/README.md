# Bài tập tự làm: Quản lý danh bạ khách hàng với JSON Server

Bài tập này dành cho học viên sau khi đã học bài Todo CRUD với JSON Server. Mục tiêu là tự xây dựng một ứng dụng CRUD tương tự nhưng đổi sang nghiệp vụ quản lý khách hàng, để học viên phải tự phân tích yêu cầu, tự viết validate, tự gọi API và tự viết test.

## 1. Kết quả cần đạt

Ứng dụng cần có các chức năng:

- Hiển thị danh sách khách hàng từ JSON Server.
- Thêm khách hàng mới.
- Sửa thông tin khách hàng.
- Xóa khách hàng.
- Đánh dấu đã tư vấn.
- Đánh dấu đã đăng ký.
- Đánh dấu khách hàng yêu thích.
- Lọc theo trạng thái.
- Tìm kiếm theo tên, số điện thoại, email hoặc khóa học.
- Viết Unit test, Business test, Integration test và E2E test.

## 2. Cấu trúc project

```txt
source-bai-tap-contact-json-server/
├── index.html
├── db.json
├── package.json
├── playwright.config.js
├── src/
│   ├── customerApiStore.js
│   ├── customerBusiness.js
│   ├── app.js
│   └── style.css
├── tests/
│   ├── unit/
│   ├── business/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── de-bai.md
│   ├── test-plan.md
│   ├── test-cases.md
│   └── checklist.md
└── README.md
```

## 3. Cài đặt

```bash
cd course-kiem-thu-tu-dong-voi-ai-va-ci-cd/source-bai-tap-contact-json-server
npm install
npx playwright install
```

## 4. Chạy web và API

```bash
npm run dev
```

Mở web tại:

```txt
http://localhost:3000
```

API chạy tại:

```txt
http://localhost:3001/customers
```

## 5. Chạy test

Chạy Unit test:

```bash
npm run test:unit
```

Chạy Business test:

```bash
npm run test:business
```

Chạy cả Unit test và Business test:

```bash
npm run test:all
```

Chạy Integration test, cần JSON Server đang chạy:

```bash
npm run dev:api
```

Ở terminal khác:

```bash
npm run test:integration
```

Chạy E2E test:

```bash
npm run test:e2e
```

Chạy toàn bộ test có API thật:

```bash
npm run test:all-with-api
```

## 6. Tài liệu học viên cần đọc

- `docs/de-bai.md`: đề bài chi tiết.
- `docs/test-plan.md`: kế hoạch kiểm thử.
- `docs/test-cases.md`: danh sách test case.
- `docs/checklist.md`: checklist hoàn thành.

## 7. Gợi ý cách làm

Nên làm theo thứ tự:

1. Đọc đề bài và dữ liệu mẫu trong `db.json`.
2. Chạy JSON Server và thử mở endpoint `/customers`.
3. Viết các hàm business trước.
4. Viết Unit test business.
5. Viết API store và test mock `fetch`.
6. Nối UI với API.
7. Viết Integration test.
8. Viết E2E test.
9. Hoàn thiện README và checklist.
