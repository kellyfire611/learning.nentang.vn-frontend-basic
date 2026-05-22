# Test Plan - Login App Don Gian

## Mục tiêu
- Đảm bảo validate dữ liệu đăng nhập đúng yêu cầu.
- Đảm bảo trạng thái phiên đăng nhập thay đổi đúng khi login/logout.
- Đảm bảo giao diện phản hồi đúng thông báo với thao tác người dùng.

## Phạm vi
- Unit test cho hàm `normalizeText`, `normalizeEmail`, `isValidEmail`.
- Unit test cho `login` và `logout` trong store.
- Business test cho luồng sai -> đúng, login với rememberMe, và logout.
- E2E test cho các thao tác trên form và kiểm tra UI state.

## Ngoài phạm vi
- Không kiểm thử API server thật.
- Không kiểm thử bảo mật nâng cao (rate limit, captcha, lock account).
- Không kiểm thử multi-user hoặc phân quyền.

## Tiêu chi pass
- Toan bo unit/business test pass.
- Toan bo e2e test pass.
- Khong con test `todo` hoac `skip` trong bai nop cuoi.

## Moi truong test
- Node.js 18+.
- Trinh duyet Chromium do Playwright quan ly.
- App chay local qua `http-server` tren cong `3109`.

## Thu tu thuc hien
1. Chay `npm install`.
2. Chay `npm test` de xu ly unit va business test.
3. Chay `npm run test:e2e` de xu ly e2e test.
4. Neu can, chay `npm run serve` de tu thao tac thu tren trinh duyet.