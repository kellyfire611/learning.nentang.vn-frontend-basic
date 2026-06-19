# Test Cases - Contact JSON Server

## 1. Unit test business

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-BUS-001 | Họ tên rỗng | Báo lỗi họ tên bắt buộc |
| TC-BUS-002 | Họ tên dưới 3 ký tự | Báo lỗi độ dài họ tên |
| TC-BUS-003 | Số điện thoại chứa chữ | Báo lỗi số điện thoại chỉ chứa số |
| TC-BUS-004 | Email không có `@` | Báo lỗi email |
| TC-BUS-005 | Tạo payload hợp lệ | Trim dữ liệu, status là `new`, isFavorite là `false` |
| TC-BUS-006 | Lọc status `contacted` | Chỉ còn khách đã tư vấn |
| TC-BUS-007 | Tìm theo số điện thoại | Trả về khách hàng phù hợp |

## 2. Unit test API

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-API-001 | `fetchCustomers` | Gọi đúng `GET /customers` |
| TC-API-002 | `createCustomer` | Gọi đúng POST và gửi JSON body |
| TC-API-003 | `patchCustomerStatus` | Gọi đúng PATCH `/customers/:id` |
| TC-API-004 | `updateCustomer` | Gọi đúng PUT `/customers/:id` |
| TC-API-005 | `deleteCustomer` | Gọi đúng DELETE `/customers/:id` |
| TC-API-006 | API trả lỗi | Hàm throw Error |

## 3. Integration test

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-INT-001 | GET `/customers` | Trả về mảng |
| TC-INT-002 | POST `/customers` | Tạo được khách hàng mới |
| TC-INT-003 | PATCH `/customers/:id` | Cập nhật được trạng thái |
| TC-INT-004 | PUT `/customers/:id` | Cập nhật được toàn bộ thông tin |
| TC-INT-005 | DELETE `/customers/:id` | Xóa được dữ liệu |

## 4. E2E test

| Mã | Tình huống | Kết quả mong đợi |
|---|---|---|
| TC-E2E-001 | Mở trang | Thấy tiêu đề và danh sách khách hàng |
| TC-E2E-002 | Thêm khách hàng hợp lệ | Khách hàng xuất hiện trên danh sách |
| TC-E2E-003 | Thêm thiếu họ tên | Hiển thị lỗi validate |
| TC-E2E-004 | Đánh dấu đã tư vấn | Trạng thái đổi thành đã tư vấn |
| TC-E2E-005 | Lọc đã đăng ký | Thấy khách hàng đã đăng ký |
| TC-E2E-006 | Tìm theo số điện thoại | Thấy khách hàng phù hợp |
| TC-E2E-007 | Xóa khách hàng | Khách hàng biến mất khỏi danh sách |
