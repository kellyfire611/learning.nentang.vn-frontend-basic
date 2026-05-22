# Nhiệm vụ học viên - TODO starter

## Mục tiêu
- Đọc được source trong một buổi mà không bị quá tải.
- Tự viết được test từ app rất đơn giản trước khi chuyển sang app khó hơn.
- Biết cách đưa bài làm vào CI/CD cơ bản.

## Việc cần làm
1. Đọc `docs/test-plan.md` và `docs/test-cases.md`.
2. Hoàn thiện unit test trong `tests/unit/todoStore.test.js`.
3. Hoàn thiện business test trong `tests/business/todoFlow.business.test.js`.
4. Hoàn thiện E2E test trong `tests/e2e/todo.spec.js`.
5. Tự tạo `.github/workflows/ci.yml` để chạy `npm test` và `npm run test:e2e`.

## Gợi ý cho học viên yếu
- Viết 1 test nhỏ rồi chạy ngay.
- Chỉ làm 1 chức năng mỗi lần: thêm việc, rồi toggle, rồi lọc.
- Nếu dùng AI, luôn kiểm tra lại expected value và selector.