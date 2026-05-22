# Step 8 - Hoàn thiện bài và tự kiểm tra

## Mục tiêu
- Biết thế nào là hoàn thành bài đúng yêu cầu.
- Biết tự rà trước khi nộp hoặc trước khi đưa AI sinh thêm test.

## Những file cuối cùng nên có
- `index.html`
- `src/loginStore.js`
- `src/main.js`
- `tests/unit/loginStore.test.js`
- `tests/business/loginFlow.business.test.js`
- `tests/e2e/login.spec.js`
- `docs/test-plan.md`
- `docs/test-cases.md`
- `docs/student-checklist.md`

## Quy trình tự kiểm tra
1. Chạy `npm test`
2. Chạy `npm run test:e2e`
3. Mở app bằng local server và tự bấm thử ít nhất 3 case
4. So lại `test-cases.md` xem có case nào chưa chuyển thành test code
5. Kiểm tra message tiếng Việt có đồng nhất giữa code và test

## Coverage nên hiểu thế nào trong bài này
- Coverage cao là tốt nhưng không phải mục tiêu duy nhất.
- Quan trọng hơn là test đúng luồng quan trọng.
- `main.js` có thể coverage thấp nếu bạn chưa viết test cho DOM ở mức unit.

## Gợi ý mở rộng nếu học viên làm xong sớm
1. Thêm case khóa tài khoản sau 3 lần sai
2. Thêm validate mật khẩu tối thiểu 6 ký tự
3. Thêm E2E test cho case sai mật khẩu rồi thử lại
4. Tự viết GitHub Actions chạy `npm test` và `npm run test:e2e`

## Kết quả mong đợi
- Học viên hiểu trọn một vòng đời nhỏ của kiểm thử tự động
- Từ một form login đơn giản, học viên đã đi qua setup, tài liệu, unit, business và e2e