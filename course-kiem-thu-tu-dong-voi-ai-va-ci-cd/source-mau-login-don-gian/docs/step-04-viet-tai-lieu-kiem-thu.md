# Step 4 - Viết tài liệu kiểm thử trước khi code test

## Mục tiêu
- Học viên biết phải viết tài liệu gì trước khi bắt đầu test.
- Tránh tình trạng viết test theo cảm tính rồi bỏ sót case.

## Tài liệu tối thiểu cần có
1. `test-plan.md`
2. `test-cases.md`
3. `student-checklist.md`

## `test-plan.md` dùng để làm gì
- Ghi mục tiêu kiểm thử
- Xác định phạm vi và ngoài phạm vi
- Ghi môi trường chạy test
- Đặt tiêu chí pass/fail

## `test-cases.md` dùng để làm gì
- Liệt kê từng kịch bản cụ thể
- Ghi input, thao tác và expected output
- Giúp map từ yêu cầu sang test code

## `student-checklist.md` dùng để làm gì
- Học viên tự rà xem đã làm đủ bài chưa
- Giáo viên có thể dùng như checklist chấm nhanh

## Cách nghĩ test case cho bài login này
1. Happy path: đăng nhập đúng
2. Negative case: thiếu email, email sai định dạng, thiếu mật khẩu, sai tài khoản
3. State transition: login rồi logout
4. Multi-step flow: sai 1 lần rồi đúng 1 lần
5. UI flow: submit form, đọc thông báo, kiểm tra panel hiển thị hay ẩn

## Tài liệu cần viết trước khi sang bước test code
- 1 test plan ngắn nhưng rõ phạm vi
- 1 bảng test case có ID và kỳ vọng rõ ràng
- 1 checklist tự kiểm tra

## Kết quả mong đợi
- Học viên không còn hỏi "em nên test gì trước" vì đã có danh sách rõ ràng