# Test Cases - TODO App Đơn Giản

| ID | Kịch bản | Dữ liệu | Kỳ vọng |
| --- | --- | --- | --- |
| TC-01 | Thêm công việc mới | `Học unit test` | Danh sách có 1 item, active = 1 |
| TC-02 | Không cho thêm rỗng | `"   "` | Báo lỗi, không tạo item |
| TC-03 | Đánh dấu hoàn thành | Toggle item 1 | done = 1, active giảm |
| TC-04 | Lọc việc chưa xong | Filter `active` | Chỉ hiện item `completed = false` |
| TC-05 | Lọc việc đã xong | Filter `done` | Chỉ hiện item `completed = true` |
| TC-06 | Xóa việc đã xong | Click `Xóa việc đã xong` | Tất cả item completed bị xóa |
| TC-07 | Xóa 1 công việc | Click nút xóa trên item | Item biến mất khỏi danh sách |