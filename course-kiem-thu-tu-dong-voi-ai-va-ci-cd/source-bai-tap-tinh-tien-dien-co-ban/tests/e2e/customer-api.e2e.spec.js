import { test, expect } from "@playwright/test";

test.describe("E2E test - Customer API", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("TC-API-E2E-01: Bam nut tai khach hang thi hien thi danh sach khach hang", async ({ page }) => {
    await page.route("https://jsonplaceholder.typicode.com/users", async (route) => {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify([
          { id: 1, name: "Leanne Graham", email: "Sincere@april.biz" },
          { id: 2, name: "Ervin Howell", email: "Shanna@melissa.tv" },
        ]),
      });
    });

    await page.click("#load-customers-button");

    await expect(page.locator("#customer-api-message")).toContainText(
      "Tai danh sach khach hang thanh cong!"
    );
    await expect(page.locator("#customer-api-message")).toHaveClass(/is-success/);
    await expect(page.locator("#customer-list")).toContainText(
      "1. Leanne Graham - Sincere@april.biz"
    );
  });

  test("TC-API-E2E-02: Khi API loi thi UI hien thi thong bao loi", async ({ page }) => {
    await page.route("https://jsonplaceholder.typicode.com/users", async (route) => {
      await route.fulfill({
        status: 500,
        contentType: "application/json",
        body: JSON.stringify({ message: "Server error" }),
      });
    });

    await page.click("#load-customers-button");

    await expect(page.locator("#customer-api-message")).toContainText(
      "Khong the tai danh sach khach hang!"
    );
    await expect(page.locator("#customer-api-message")).toHaveClass(/is-error/);
  });
});
