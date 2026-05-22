import { expect, test } from "@playwright/test";

test.describe("mini shop", () => {
  test("tim kiem san pham va them vao gio", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("search-input").fill("Playwright");
    await expect(page.getByTestId("product-card-1")).toBeVisible();
    await expect(page.getByTestId("product-card-2")).toHaveCount(0);

    await page.getByTestId("add-to-cart-1").click();

    await expect(page.getByTestId("cart-count")).toHaveText("1");
    await expect(page.getByTestId("cart-row-1")).toBeVisible();
    await expect(page.getByTestId("cart-total")).toHaveText("480.000 đ");
  });

  test("ap dung ma giam gia va cap nhat tong thanh toan", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("add-to-cart-1").click();
    await page.getByTestId("add-to-cart-4").click();

    await page.getByTestId("coupon-input").fill("save10");
    await page.getByTestId("apply-coupon").click();

    await expect(page.getByTestId("cart-discount")).toHaveText("83.000 đ");
    await expect(page.getByTestId("cart-total")).toHaveText("777.000 đ");
    await expect(page.getByTestId("status-message")).toContainText("Da ap dung giam 10%");
  });
});