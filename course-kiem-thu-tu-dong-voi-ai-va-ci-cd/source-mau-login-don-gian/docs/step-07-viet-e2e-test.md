# Step 7 - Viết E2E test

## Mục tiêu
- Kiểm tra toàn bộ luồng thật trên trình duyệt.
- Xác nhận HTML, JS và state đang nối với nhau đúng.

## File cần viết
- `tests/e2e/login.spec.js`

## Những case nên có
1. Submit form rỗng và thấy lỗi
2. Đăng nhập đúng rồi đăng xuất

## Selector nên ưu tiên
1. `getByTestId()` cho vùng trạng thái quan trọng
2. `getByLabel()` cho input form

## Ví dụ E2E test

```js
test("đăng nhập thành công rồi đăng xuất", async ({ page }) => {
  await page.goto("/");

  await page.getByLabel("Email").fill("student@example.com");
  await page.getByLabel("Mật khẩu").fill("123456");
  await page.getByLabel("Ghi nhớ đăng nhập").check();
  await page.getByTestId("login-submit").click();

  await expect(page.getByTestId("message")).toHaveText("Đăng nhập thành công.");
  await expect(page.getByTestId("session-panel")).toBeVisible();

  await page.getByTestId("logout-button").click();

  await expect(page.getByTestId("message")).toHaveText("Đã đăng xuất.");
});
```

## Lệnh chạy

```bash
npm run test:e2e
```

## Khi test fail thì nhìn gì trước
1. `data-testid` có đúng với HTML không
2. Text expected có đúng dấu và đúng khoảng trắng không
3. App có đang chạy đúng cổng không
4. `playwright.config.js` có đúng `baseURL` và `webServer.port` không

## Điều học viên cần rút ra
- E2E test chậm hơn unit test nhưng xác nhận được trải nghiệm thật.
- Không nên dồn toàn bộ việc test vào E2E.

## Kết quả mong đợi
- Học viên có thể tự thao tác và viết lại được ít nhất 2 test E2E cơ bản