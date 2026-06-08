# Test Plan - Todo CRUD với JSON Server

## Unit test API

| Mã test | Loại test | Chức năng | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC-API-UNIT-01 | Unit API | `fetchTodos` gọi đúng URL | Mock fetch thành công | Gọi `http://localhost:3001/todos` |
| TC-API-UNIT-02 | Unit API | `fetchTodos` dùng GET mặc định | Mock fetch thành công | Không truyền options method |
| TC-API-UNIT-03 | Unit API | `fetchTodos` trả danh sách | Response ok, JSON là mảng Todo | Nhận đúng mảng Todo |
| TC-API-UNIT-04 | Unit API | `fetchTodos` xử lý lỗi | Response `ok: false` | Throw `Khong the tai danh sach cong viec!` |
| TC-API-UNIT-05 | Unit API | `createTodo` gọi đúng URL | Todo mới | Gọi đúng endpoint `/todos` |
| TC-API-UNIT-06 | Unit API | `createTodo` dùng POST | Todo mới | Method là `POST` |
| TC-API-UNIT-07 | Unit API | `createTodo` gửi Content-Type | Todo mới | Header là `application/json` |
| TC-API-UNIT-08 | Unit API | `createTodo` gửi body | Todo mới | Body là `JSON.stringify(todo)` |
| TC-API-UNIT-09 | Unit API | `createTodo` xử lý lỗi | Response `ok: false` | Throw `Khong the them cong viec!` |
| TC-API-UNIT-10 | Unit API | `updateTodo` dùng PUT | Todo đầy đủ | Method là `PUT` |
| TC-API-UNIT-11 | Unit API | `updateTodoStatus` dùng PATCH | `completed: true` | Method là `PATCH` |
| TC-API-UNIT-12 | Unit API | `updateTodoStatus` chỉ gửi completed | `completed: true` | Body chỉ có `{ completed: true }` |
| TC-API-UNIT-13 | Unit API | `deleteTodo` dùng DELETE | Id Todo | Method là `DELETE` |
| TC-API-UNIT-14 | Unit API | `deleteTodo` gọi đúng URL có id | Id `99` | URL là `/todos/99` |

## Unit test nghiệp vụ

| Mã test | Loại test | Chức năng | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC-BUSINESS-UNIT-01 | Unit nghiệp vụ | Validate rỗng | `"   "` | Báo lỗi bắt buộc nhập |
| TC-BUSINESS-UNIT-02 | Unit nghiệp vụ | Validate dưới 3 ký tự | `"ab"` | Báo lỗi ít nhất 3 ký tự |
| TC-BUSINESS-UNIT-03 | Unit nghiệp vụ | Validate trên 100 ký tự | Chuỗi 101 ký tự | Báo lỗi vượt quá 100 ký tự |
| TC-BUSINESS-UNIT-04 | Unit nghiệp vụ | Validate hợp lệ | `"Hoc API"` | Trả chuỗi rỗng |
| TC-BUSINESS-UNIT-05 | Unit nghiệp vụ | Trim title | `"  Hoc JavaScript  "` | Title là `"Hoc JavaScript"` |
| TC-BUSINESS-UNIT-06 | Unit nghiệp vụ | Mặc định chưa hoàn thành | `"Hoc JavaScript"` | `completed` bằng `false` |
| TC-BUSINESS-UNIT-07 | Unit nghiệp vụ | Lọc tất cả | Danh sách Todo | Trả toàn bộ danh sách |
| TC-BUSINESS-UNIT-08 | Unit nghiệp vụ | Lọc active | Danh sách Todo | Chỉ Todo chưa hoàn thành |
| TC-BUSINESS-UNIT-09 | Unit nghiệp vụ | Lọc completed | Danh sách Todo | Chỉ Todo đã hoàn thành |
| TC-BUSINESS-UNIT-10 | Unit nghiệp vụ | Tìm Todo theo id | Id dạng số hoặc chuỗi | Tìm đúng Todo |
| TC-BUSINESS-UNIT-11 | Unit nghiệp vụ | Cập nhật Todo trong danh sách | Todo đã cập nhật | Thay đúng Todo |
| TC-BUSINESS-UNIT-12 | Unit nghiệp vụ | Không mutate mảng cũ | Mảng ban đầu | Mảng cũ không đổi |
| TC-BUSINESS-UNIT-13 | Unit nghiệp vụ | Xóa Todo khỏi danh sách | Id cần xóa | Trả mảng mới không còn Todo đó |

## Business test

| Mã test | Loại test | Chức năng | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC-BIZ-01 | Business | Tạo payload hợp lệ | Tên Todo hợp lệ | Todo có `completed: false` |
| TC-BIZ-02 | Business | Không cho thêm tên rỗng | Tên rỗng | Trả thông báo lỗi |
| TC-BIZ-03 | Business | Lọc việc chưa hoàn thành | Danh sách có cả completed true/false | Chỉ trả Todo `completed: false` |
| TC-BIZ-04 | Business | Đánh dấu hoàn thành | Todo `completed: false` | Todo được cập nhật thành true |
| TC-BIZ-05 | Business | Xóa Todo | Danh sách có Todo cần xóa | Todo đó không còn trong danh sách |
| TC-BIZ-06 | Business | Thêm Todo qua API mock thành công | Mock API trả Todo có id | Nhận Todo mới có id |
| TC-BIZ-07 | Business | Thêm Todo qua API mock thất bại | Mock API lỗi | Trả thông báo lỗi phù hợp |

## Integration test

| Mã test | Loại test | Chức năng | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC-INT-01 | Integration | GET `/todos` status | JSON Server đang chạy | Status 200 |
| TC-INT-02 | Integration | GET `/todos` dữ liệu | JSON Server đang chạy | Response là array |
| TC-INT-03 | Integration | Schema Todo | Todo tạo riêng cho test | Có `id`, `title`, `completed` |
| TC-INT-04 | Integration | POST tạo Todo | Todo test mới | Tạo thành công |
| TC-INT-05 | Integration | POST trả id | Todo test mới | Todo mới có id |
| TC-INT-06 | Integration | PATCH trạng thái | Todo test mới | `completed` được cập nhật |
| TC-INT-07 | Integration | PUT title | Todo test mới | `title` được cập nhật |
| TC-INT-08 | Integration | DELETE Todo | Todo test mới | GET lại Todo trả 404 |

## E2E test

| Mã test | Loại test | Chức năng | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC-E2E-01 | E2E | Mở trang và tải danh sách | Truy cập `/` | Hiển thị danh sách Todo |
| TC-E2E-02 | E2E | Thêm Todo | Nhập title hợp lệ | Todo mới xuất hiện |
| TC-E2E-03 | E2E | Không thêm Todo rỗng | Submit input rỗng | Hiển thị lỗi |
| TC-E2E-04 | E2E | Đánh dấu hoàn thành | Todo test chưa hoàn thành | Chữ bị gạch ngang |
| TC-E2E-05 | E2E | Lọc chưa hoàn thành | Có Todo active và completed | Chỉ thấy Todo active |
| TC-E2E-06 | E2E | Lọc đã hoàn thành | Có Todo active và completed | Chỉ thấy Todo completed |
| TC-E2E-07 | E2E | Sửa tên Todo | Todo test | Tên mới hiển thị |
| TC-E2E-08 | E2E | Xóa Todo | Todo test | Todo biến mất khỏi danh sách |
