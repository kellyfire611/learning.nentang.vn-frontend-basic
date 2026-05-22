# Step 1 - Cài đặt môi trường

## Mục tiêu
- Chuẩn bị đầy đủ phần mềm để học viên có thể chạy app và test local.
- Hiểu mỗi công cụ dùng để làm gì.

## Phần mềm cần cài
1. Visual Studio Code
2. Node.js bản LTS, nên dùng Node.js 18 trở lên
3. Git
4. Trình duyệt Google Chrome hoặc Microsoft Edge

## Extension nên cài trong VS Code
1. GitHub Copilot
2. ESLint nếu dự án sau này có lint
3. Playwright Test for VS Code
4. Live Server là tùy chọn, không bắt buộc vì bài này dùng `http-server`

## Vì sao cần các công cụ này
- VS Code để viết code, đọc test, chạy terminal.
- Node.js để cài package và chạy `vitest`, `playwright`, `http-server`.
- Git để theo dõi thay đổi và đẩy bài lên repository.
- Chrome hoặc Edge để tự thao tác và quan sát UI.

## Kiểm tra môi trường sau khi cài
Mở terminal và chạy:

```bash
node -v
npm -v
git --version
```

Nếu 3 lệnh trên đều ra version thì môi trường cơ bản đã ổn.

## Cấu trúc source cần có sau bước setup

```text
source-mau-login-don-gian/
  index.html
  package.json
  vitest.config.js
  playwright.config.js
  src/
  styles/
  tests/
  docs/
```

## Lệnh cài dependency
Di chuyển vào thư mục project và chạy:

```bash
npm install
```

## Học viên cần hiểu sau bước này
- Package nào dùng cho unit test: `vitest`
- Package nào dùng cho coverage: `@vitest/coverage-v8`
- Package nào dùng cho E2E: `@playwright/test`
- Package nào dùng để serve app HTML/CSS/JS: `http-server`

## Kết quả mong đợi
- Chạy được `npm install`
- Thấy có thư mục `node_modules`
- Không có lỗi thiếu Node.js hoặc npm