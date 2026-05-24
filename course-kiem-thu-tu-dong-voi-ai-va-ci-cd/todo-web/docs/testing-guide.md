# Hướng Dẫn Kiểm Thử

## 1. Mục tiêu kiểm thử
- Unit test: kiểm tra từng quy tắc trong hàm đăng nhập.
- Business test: kiểm tra theo kịch bản nghiệp vụ người dùng.
- E2E test: mô phỏng thao tác thật trên giao diện, xác nhận nội dung và class trạng thái của vùng thông báo.

## 2. Cấu trúc test
- `tests/unit/loginStore.unit.test.js`: kiểm thử đơn vị cho hàm `login`.
- `tests/business/loginStore.business.test.js`: kiểm thử nghiệp vụ theo ngữ cảnh Given/When/Then.
- `tests/e2e/login.e2e.spec.js`: kiểm thử giao diện thật bằng Playwright.

## 3. Cách viết test mới
1. Xác định rõ dữ liệu đầu vào và kết quả mong đợi.
2. Đặt tên test mô tả đúng hành vi cần kiểm tra.
3. Với Unit và Business test:
- Import hàm cần test.
- Gọi hàm với dữ liệu cụ thể.
- Dùng `expect(...).toBe(...)` để so sánh thông báo trả về.
4. Với E2E test:
- Điều hướng đến trang bằng `page.goto("/")`.
- Điền dữ liệu vào form bằng `page.fill(...)`.
- Bấm nút đăng nhập bằng `page.click("#login-button")`.
- Kiểm tra vùng thông báo `#login-message`:
- Nội dung hiển thị đúng.
- Class trạng thái đúng (`is-success` hoặc `is-error`).

## 4. Lệnh chạy test
- Chạy unit test: `npm run test:unit`
- Chạy business test: `npm run test:business`
- Chạy e2e test: `npm run test:e2e`
- Chạy toàn bộ test: `npm run test:all`
- Chạy test kèm coverage: `npm run test:coverage`

## 5. Tiêu chí đạt
- Tất cả test đều pass.
- Không phát sinh lỗi JavaScript khi submit form đăng nhập.
- Luồng hiển thị thông báo trên giao diện hoạt động đúng: đúng nội dung, đúng class trạng thái.

## 6. Lưu ý khi thay đổi chức năng
- Nếu thay đổi logic đăng nhập, cập nhật đồng thời Unit, Business và E2E test.
- Nếu thay đổi cách hiển thị thông báo, cập nhật selector và assertion trong E2E test trước.
