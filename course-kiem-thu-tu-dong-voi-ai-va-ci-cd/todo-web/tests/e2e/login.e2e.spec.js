import { test, expect } from "@playwright/test";

test.describe("Kiểm thử đăng nhập E2E", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("hiển thị thông báo lỗi khi bỏ trống email", async ({ page }) => {
    await page.fill("#password-input", "123456");
    await page.click("#login-button");

    const loginMessage = page.locator("#login-message");

    await expect(loginMessage).toHaveText("Vui lòng nhập email!");
    await expect(loginMessage).toHaveClass(/is-error/);
  });

  test("hiển thị thông báo lỗi khi bỏ trống mật khẩu", async ({ page }) => {
    await page.fill("#email-input", "admin@gmail.com");
    await page.click("#login-button");

    const loginMessage = page.locator("#login-message");

    await expect(loginMessage).toHaveText("Vui lòng nhập mật khẩu!");
    await expect(loginMessage).toHaveClass(/is-error/);
  });

  test("đăng nhập thành công khi nhập đúng thông tin", async ({ page }) => {
    await page.fill("#email-input", "admin@gmail.com");
    await page.fill("#password-input", "123456");
    await page.click("#login-button");

    const loginMessage = page.locator("#login-message");

    await expect(loginMessage).toHaveText("Đăng nhập thành công!");
    await expect(loginMessage).toHaveClass(/is-success/);
  });

  test("đăng nhập thất bại khi nhập sai thông tin", async ({ page }) => {
    await page.fill("#email-input", "admin@gmail.com");
    await page.fill("#password-input", "wrong-password");
    await page.click("#login-button");

    const loginMessage = page.locator("#login-message");

    await expect(loginMessage).toHaveText("Đăng nhập thất bại!");
    await expect(loginMessage).toHaveClass(/is-error/);
  });
});