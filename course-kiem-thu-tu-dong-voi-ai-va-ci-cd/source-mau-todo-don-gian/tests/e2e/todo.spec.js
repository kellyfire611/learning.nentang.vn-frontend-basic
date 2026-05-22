import { expect, test } from "@playwright/test";

test.describe("todo app don gian", () => {
  test("thêm công việc mới và cập nhật số đếm", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("todo-input").fill("Hoc unit test");
    await page.getByTestId("add-button").click();

    await expect(page.getByTestId("todo-item-1")).toBeVisible();
    await expect(page.getByTestId("total-count")).toHaveText("1 việc");
    await expect(page.getByTestId("active-count")).toHaveText("1 đang làm");
  });

  test("đánh dấu xong, lọc done và xóa việc đã xong", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("todo-input").fill("Hoc Playwright");
    await page.getByTestId("add-button").click();
    await page.getByTestId("toggle-todo-1").check();

    await expect(page.getByTestId("done-count")).toHaveText("1 đã xong");
    await page.getByTestId("filter-done").click();
    await expect(page.getByTestId("todo-item-1")).toBeVisible();
    await expect(page.getByTestId("todo-status-1")).toHaveText("Đã xong");

    await page.getByTestId("clear-done").click();
    await expect(page.getByTestId("todo-item-1")).toHaveCount(0);
    await expect(page.getByTestId("total-count")).toHaveText("0 việc");
  });
});