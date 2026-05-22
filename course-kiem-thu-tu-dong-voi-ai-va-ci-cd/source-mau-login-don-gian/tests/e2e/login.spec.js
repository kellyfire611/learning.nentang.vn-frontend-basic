import { expect, test } from "@playwright/test";

test.describe("login app đơn giản", () => {
  test("hiển thị lỗi khi thiếu dữ liệu", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("login-submit").click();

    await expect(page.getByTestId("message")).toHaveText("Vui lòng nhập email.");
    await expect(page.getByTestId("attempts-count")).toHaveText("1");
    await expect(page.getByTestId("auth-status")).toHaveText("Chưa đăng nhập");
  });

  test("đăng nhập thành công rồi đăng xuất", async ({ page }) => {
    await page.goto("/");

    await page.getByLabel("Email").fill("student@example.com");
    await page.getByLabel("Mật khẩu").fill("123456");
    await page.getByLabel("Ghi nhớ đăng nhập").check();
    await page.getByTestId("login-submit").click();

    await expect(page.getByTestId("message")).toHaveText("Đăng nhập thành công.");
    await expect(page.getByTestId("auth-status")).toHaveText("Đã đăng nhập");
    await expect(page.getByTestId("session-panel")).toBeVisible();
    await expect(page.getByTestId("attempts-count")).toHaveText("1");
    await expect(page.getByTestId("session-panel")).toContainText("Học viên");

    await page.getByTestId("logout-button").click();

    await expect(page.getByTestId("message")).toHaveText("Đã đăng xuất.");
    await expect(page.getByTestId("auth-status")).toHaveText("Chưa đăng nhập");
    await expect(page.getByTestId("session-panel")).toBeHidden();
  });
});