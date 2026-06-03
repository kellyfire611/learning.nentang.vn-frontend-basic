import { test, expect } from "@playwright/test";

test.describe("E2E test - Bai tap tinh tien dien co ban", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("TC-E2E-01: UI hien thi loi khi bo trong so kWh", async ({ page }) => {
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("Vui long nhap so kWh dien!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("TC-E2E-02: UI hien thi loi khi nhap so kWh am", async ({ page }) => {
    await page.fill("#kwh-input", "-5");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("So kWh dien khong duoc am!");
    await expect(message).toHaveClass(/is-error/);
  });

  test("TC-E2E-03: UI tinh dung tien dien khi nhap 30 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "30");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("So tien dien can tra: 54000 VND");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-04: UI tinh dung tien dien tai bien 50 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "50");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("So tien dien can tra: 90000 VND");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-05: UI tinh dung tien dien khi nhap 80 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "80");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("So tien dien can tra: 150000 VND");
    await expect(message).toHaveClass(/is-success/);
  });

  test("TC-E2E-06: UI tinh dung tien dien khi nhap 120 kWh", async ({ page }) => {
    await page.fill("#kwh-input", "120");
    await page.click("#calculate-button");

    const message = page.locator("#calculation-message");
    await expect(message).toHaveText("So tien dien can tra: 240000 VND");
    await expect(message).toHaveClass(/is-success/);
  });
});
