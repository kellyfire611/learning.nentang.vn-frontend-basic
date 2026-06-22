# Test Cases

## 1. Unit test business

| Mã test case | Nội dung | Kết quả mong đợi |
|---|---|---|
| TC-BUS-001 | Họ tên rỗng | Báo lỗi họ tên không được rỗng |
| TC-BUS-002 | Họ tên dưới 3 ký tự | Báo lỗi họ tên tối thiểu 3 ký tự |
| TC-BUS-003 | Số điện thoại chứa chữ | Báo lỗi số điện thoại chỉ được chứa số |
| TC-BUS-004 | Email không có @ | Báo lỗi email phải có ký tự @ |
| TC-BUS-005 | Tạo payload khách hàng mới | `status = new`, `isFavorite = false`, dữ liệu được trim |
| TC-BUS-006 | Lọc khách hàng contacted | Chỉ trả về khách hàng đã tư vấn |
| TC-BUS-007 | Tìm kiếm theo số điện thoại | Trả về khách hàng có số điện thoại phù hợp |
| TC-BUS-008 | Cập nhật trạng thái trong list | Trạng thái khách hàng thay đổi đúng |
| TC-BUS-009 | Xóa khách hàng khỏi list | Danh sách không còn khách hàng bị xóa |

## 2. Unit test API

| Mã test case | Nội dung | Kết quả mong đợi |
|---|---|---|
| TC-API-001 | Gọi `fetchCustomers` | Gọi đúng `GET /customers` |
| TC-API-002 | Gọi `createCustomer` | Gọi đúng `POST /customers` và gửi JSON body |
| TC-API-003 | Gọi `patchCustomerStatus` | Gọi đúng `PATCH /customers/:id` |
| TC-API-004 | Gọi `updateCustomer` | Gọi đúng `PUT /customers/:id` |
| TC-API-005 | Gọi `deleteCustomer` | Gọi đúng `DELETE /customers/:id` |
| TC-API-006 | API trả lỗi | Hàm phải throw Error |

## 3. Integration test

| Mã test case | Nội dung | Kết quả mong đợi |
|---|---|---|
| TC-INT-001 | GET /customers | Trả về mảng dữ liệu |
| TC-INT-002 | POST /customers | Thêm được khách hàng mới |
| TC-INT-003 | PATCH /customers/:id | Cập nhật được trạng thái |
| TC-INT-004 | PUT /customers/:id | Cập nhật đầy đủ thông tin |
| TC-INT-005 | DELETE /customers/:id | Xóa được dữ liệu |

## 4. E2E test

| Mã test case | Nội dung | Kết quả mong đợi |
|---|---|---|
| TC-E2E-001 | Trang tải danh sách | Có danh sách khách hàng hiển thị |
| TC-E2E-002 | Thêm khách hàng mới | Khách hàng mới xuất hiện trên danh sách |
| TC-E2E-003 | Thêm thiếu họ tên | Hiển thị lỗi validate |
| TC-E2E-004 | Đánh dấu đã tư vấn | Trạng thái chuyển thành đã tư vấn |
| TC-E2E-005 | Lọc đã đăng ký | Chỉ hiển thị khách đã đăng ký |
| TC-E2E-006 | Tìm theo số điện thoại | Hiển thị đúng khách hàng cần tìm |
| TC-E2E-007 | Xóa khách hàng | Khách hàng biến mất khỏi danh sách |
