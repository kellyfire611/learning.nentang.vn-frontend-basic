import { test, expect } from "@playwright/test";

test.describe("E2E test - Bài tập tính tiền điện cơ bản", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("TC-E2E-01: UI hiển thị lỗi khi bỏ trống số kWh", async ({ page }) => {
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Vui lòng nhập số kWh điện!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("TC-E2E-02: UI hiển thị lỗi khi nhập số kWh âm", async ({ page }) => {
    await page.fill("#kwh-input", "-5");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số kWh điện không được âm!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("TC-E2E-03: UI tính đúng tiền điện khi nhập 30 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "30");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền điện cần trả: 54000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-04: UI tính đúng tiền điện tại biên 50 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "50");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền điện cần trả: 90000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-05: UI tính đúng tiền điện khi nhập 80 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "80");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền điện cần trả: 150000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-06: UI tính đúng tiền điện khi nhập 120 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "120");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Số tiền điện cần trả: 240000 VNĐ");
    await expect(message).toHaveClass(/is-success/);
  });
});
