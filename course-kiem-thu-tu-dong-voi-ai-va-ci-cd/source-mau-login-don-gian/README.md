# Source mẫu đăng nhập đơn giản

Đây là bản mẫu rất nhỏ để học kiểm thử theo một luồng duy nhất: nhập email, nhập mật khẩu, đăng nhập và đăng xuất.

## App này có gì?
- 1 form đăng nhập với email, mật khẩu và checkbox ghi nhớ đăng nhập.
- 1 store logic thuần để viết unit test và business test.
- 1 vùng hiển thị trạng thái phiên đăng nhập để test E2E.

## Vì sao app này dễ học?
- Chỉ có một nghiệp vụ chính nên học viên không phải đọc nhiều logic cùng lúc.
- `src/loginStore.js` là nơi chứa toàn bộ luật kiểm tra dữ liệu.
- Test được chia thành 3 lớp: `unit`, `business`, `e2e`.

## Cách chạy

```bash
npm install
npm test
npm run test:e2e
```

## Học step-by-step
- Xem lộ trình tại `docs/README.md`.
- Đi theo từng bước từ cài đặt, tạo giao diện, tách logic, viết tài liệu, rồi mới sang unit test, business test và E2E test.
- Tài liệu mẫu hoàn chỉnh có sẵn trong `docs/test-plan.md`, `docs/test-cases.md` và `docs/student-checklist.md`.

## Các file quan trọng
- `src/loginStore.js`: logic login để viết test.
- `src/main.js`: gắn store vào giao diện.
- `tests/unit/`: test các hàm và luật validate.
- `tests/business/`: test luồng đăng nhập - đăng xuất.
- `tests/e2e/`: test thao tác người dùng trên trình duyệt.