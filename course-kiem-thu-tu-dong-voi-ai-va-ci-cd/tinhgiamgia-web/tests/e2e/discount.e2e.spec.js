import { test, expect } from "@playwright/test";

test.describe("E2E test - Bài tập tính tiền giảm giá", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("Mã TC-E2E-01: UI hiển thị lỗi khi bỏ trống giá gốc", async ({ page }) => {
    await page.fill("#discount-input", "10");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Vui lòng nhập giá gốc!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("Mã TC-E2E-02: UI hiển thị lỗi khi bỏ trống phần trăm giảm", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Vui lòng nhập phần trăm giảm giá!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("Mã TC-E2E-03: UI hiển thị lỗi khi nhập giảm giá vượt quá 100", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "101");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Phần trăm giảm giá phải từ 0 đến 100!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("Mã TC-E2E-04: UI tính đúng tiền khi dữ liệu hợp lệ", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "10");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền cần trả: 180000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });

  test("Mã TC-E2E-05: UI xử lý đúng biên giảm giá 0 phần trăm", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "0");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền cần trả: 200000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });

  test("Mã TC-E2E-06: UI xử lý đúng biên giảm giá 100 phần trăm", async ({ page }) => {
    await page.fill("#price-input", "200000");
    await page.fill("#discount-input", "100");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền cần trả: 0 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });
});
