# Kế Hoạch Kiểm Thử - Chức Năng Đăng Nhập

## 1. Phạm vi
Kiểm thử chức năng đăng nhập trong giao diện và logic xử lý tương ứng.

## 2. Cấp độ kiểm thử
- Unit test
- Business test (kịch bản nghiệp vụ)
- End-to-End test (giao diện thật)

## 3. Danh sách test case chính

| Mã test | Loại test | Dữ liệu vào | Kết quả mong đợi |
|---|---|---|---|
| TC-UNIT-01 | Unit | Email rỗng, mật khẩu hợp lệ | Trả về `Vui lòng nhập email!` |
| TC-UNIT-02 | Unit | Email hợp lệ, mật khẩu rỗng | Trả về `Vui lòng nhập mật khẩu!` |
| TC-UNIT-03 | Unit | `admin@gmail.com` / `123456` | Trả về `Đăng nhập thành công!` |
| TC-UNIT-04 | Unit | Sai email hoặc sai mật khẩu | Trả về `Đăng nhập thất bại!` |
| TC-BIZ-01 | Business | Người dùng bỏ trống email | Hệ thống yêu cầu nhập email |
| TC-BIZ-02 | Business | Người dùng bỏ trống mật khẩu | Hệ thống yêu cầu nhập mật khẩu |
| TC-BIZ-03 | Business | Người dùng nhập đúng thông tin | Hệ thống báo đăng nhập thành công |
| TC-BIZ-04 | Business | Người dùng nhập sai thông tin | Hệ thống báo đăng nhập thất bại |
| TC-E2E-01 | E2E | Thao tác UI, bỏ trống email | `#login-message` hiển thị đúng nội dung và có class `is-error` |
| TC-E2E-02 | E2E | Thao tác UI, bỏ trống mật khẩu | `#login-message` hiển thị đúng nội dung và có class `is-error` |
| TC-E2E-03 | E2E | Thao tác UI, nhập đúng thông tin | `#login-message` hiển thị đúng nội dung và có class `is-success` |
| TC-E2E-04 | E2E | Thao tác UI, nhập sai thông tin | `#login-message` hiển thị đúng nội dung và có class `is-error` |

## 4. Môi trường kiểm thử
- Node.js phiên bản 18 trở lên
- Trình duyệt Chromium do Playwright cung cấp

## 5. Tiêu chí đạt
- 100% test case trong danh sách chạy thành công.
- Không phát sinh lỗi JavaScript trong quá trình submit form.
- Trạng thái giao diện phản ánh đúng kết quả đăng nhập thông qua class của vùng thông báo.
