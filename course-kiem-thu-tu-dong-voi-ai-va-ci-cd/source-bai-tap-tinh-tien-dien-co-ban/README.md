# Bài thực hành tính tiền điện cơ bản

## Mục tiêu bài học
- Biết cách tách logic nghiệp vụ sang file JavaScript riêng để test.
- Viết được Unit test, Business test và E2E test cho cùng một chức năng.
- Chạy được toàn bộ test bằng npm script có sẵn.

## Cài đặt
1. Mở terminal tại thư mục project.
2. Cài package:

```bash
npm install
```

## Chạy web

```bash
npx http-server -p 3000
```

Sau đó mở trình duyệt tại địa chỉ `http://127.0.0.1:3000`.

## Chạy test unit

```bash
npm run test:unit
```

## Chạy test business

```bash
npm run test:business
```

## Chạy test e2e

```bash
npm run test:e2e
```

## Chạy tất cả test

```bash
npm run test
```

## Tài liệu kiểm thử
- Kế hoạch kiểm thử: [docs/test-plan.md](docs/test-plan.md)
- Hướng dẫn kiểm thử: [docs/testing-guide.md](docs/testing-guide.md)
