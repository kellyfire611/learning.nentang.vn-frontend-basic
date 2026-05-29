import { test, expect } from "@playwright/test";

test.describe("Kiểm thử E2E cho bài tính tiền giảm giá", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("hiển thị lỗi khi bỏ trống giá gốc", async ({ page }) => {
    await page.fill("#discount-input", "10");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");

    await expect(message).toHaveText("Vui lòng nhập giá gốc!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("hiển thị lỗi khi nhập giảm giá vượt quá 100", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "101");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");

    await expect(message).toHaveText("Phần trăm giảm giá phải từ 0 đến 100!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("tính đúng tiền cần trả khi dữ liệu hợp lệ", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "10");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");

    await expect(message).toHaveText("Số tiền cần trả: 180000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });
});
