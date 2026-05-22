# Test Plan - Login App Đơn Giản

## Mục tiêu
- Đảm bảo validate dữ liệu đầu vào hoạt động đúng.
- Đảm bảo luồng đăng nhập và đăng xuất cập nhật state chính xác.
- Đảm bảo giao diện hiển thị đúng thông báo và trạng thái phiên đăng nhập.

## Phạm vi
- Unit test cho `normalizeText`, `normalizeEmail`, `isValidEmail`.
- Unit test cho `login`, `logout`, `getState`.
- Business test cho các luồng nhiều bước.
- E2E test cho thao tác trên form login.

## Ngoài phạm vi
- Không gọi API backend thật.
- Không kiểm thử bảo mật nâng cao.
- Không kiểm thử persistence thật ra localStorage hay database.

## Môi trường
- Node.js 18+
- npm
- Playwright
- `http-server`
- Cổng chạy local: `3108`

## Tiêu chí pass
- `npm test` pass toàn bộ.
- `npm run test:e2e` pass toàn bộ.
- Happy path và các negative case chính đều có test.