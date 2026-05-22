# Test Cases - Login App Đơn Giản

| ID | Kịch bản | Dữ liệu | Kỳ vọng |
| --- | --- | --- | --- |
| TC-01 | Submit rỗng | email = `""`, password = `""` | Báo `Vui lòng nhập email.`; attempts = 1 |
| TC-02 | Email sai định dạng | email = `student.example.com` | Báo `Email không hợp lệ.` |
| TC-03 | Thiếu mật khẩu | email đúng, password rỗng | Báo `Vui lòng nhập mật khẩu.` |
| TC-04 | Sai tài khoản | email đúng, password sai | Báo `Email hoặc mật khẩu không đúng.` |
| TC-05 | Đăng nhập thành công | `student@example.com` / `123456` | `authenticated = true`; hiện panel đăng nhập |
| TC-06 | Đăng nhập với rememberMe | rememberMe = true | `rememberMe = true` |
| TC-07 | Đăng xuất | click `Đăng xuất` sau khi login thành công | `authenticated = false`; panel bị ẩn |
| TC-08 | Sai một lần rồi đúng | lần 1 sai, lần 2 đúng | attempts tăng theo từng lần submit |
| TC-09 | E2E submit rỗng | click nút đăng nhập khi form rỗng | UI hiện lỗi và vẫn ở trạng thái chưa đăng nhập |
| TC-10 | E2E đăng nhập rồi đăng xuất | nhập đúng thông tin rồi logout | UI đổi trạng thái đúng ở cả 2 bước |