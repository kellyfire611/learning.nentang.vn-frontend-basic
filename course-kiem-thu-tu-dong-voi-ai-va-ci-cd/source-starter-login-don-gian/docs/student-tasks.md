# Nhiệm vụ học viên - Login starter

## Mục tiêu
- Tự viết đầy đủ test cho một tính năng login đơn giản.
- Biết tách test theo 3 lớp: unit, business, e2e.
- Biết kiểm tra lại khi AI gợi ý test code.

## Việc cần làm
1. Đọc `docs/test-plan.md` và `docs/test-cases.md`.
2. Hoàn thiện unit test trong `tests/unit/loginStore.test.js`.
3. Hoàn thiện business test trong `tests/business/loginFlow.business.test.js`.
4. Hoàn thiện E2E test trong `tests/e2e/login.spec.js`.
5. Chạy `npm test` và sửa tới khi pass.
6. Chạy `npm run test:e2e` và sửa tới khi pass.
7. Tự tạo `.github/workflows/ci.yml` để chạy 2 lệnh test trên.

## Checklist hoàn thành
- [ ] Có test cho validate email, password và login success/fail.
- [ ] Có test cho luồng sai mật khẩu rồi đăng nhập đúng.
- [ ] Có test cho logout.
- [ ] E2E dùng đúng selector `data-testid`.
- [ ] Tất cả test pass trên máy local.

## Gợi ý cho học viên mới
- Làm theo thứ tự: unit -> business -> e2e.
- Mỗi lần chỉ viết 1 test nhỏ rồi chạy ngay.
- Không copy đáp án ngay, chỉ xem `source-mau-login-don-gian` khi đã tự làm xong.