import { expect, test } from "@playwright/test";

const API_URL = "http://localhost:3001/todos";
const TEST_PREFIX = "E2E Todo";

async function createTodoByApi(request, title, completed = false) {
  const response = await request.post(API_URL, {
    data: {
      title,
      completed,
    },
  });
  return response.json();
}

async function cleanupE2eTodos(request) {
  const response = await request.get(API_URL);
  const todos = await response.json();
  const e2eTodos = todos.filter((todo) => todo.title.startsWith(TEST_PREFIX));

  for (const todo of e2eTodos) {
    await request.delete(`${API_URL}/${todo.id}`);
  }
}

test.afterEach(async ({ request }) => {
  await cleanupE2eTodos(request);
});

test("TC-E2E-01: Mở trang và tải được danh sách Todo", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator("h1")).toContainText("Quản lý công việc Todo");
  await expect(page.locator("#api-message")).toContainText("Tải dữ liệu thành công!");
  await expect(page.locator('[data-testid="todo-item"]').first()).toBeVisible();
});

test("TC-E2E-02: Thêm Todo mới thành công", async ({ page }) => {
  await page.goto("/");

  await page.locator("#todo-title-input").fill(`${TEST_PREFIX} thêm mới`);
  await page.locator("#add-todo-button").click();

  await expect(page.locator("#form-message")).toContainText("Thêm công việc thành công!");
  await expect(page.locator("#todo-list")).toContainText(`${TEST_PREFIX} thêm mới`);
});

test("TC-E2E-03: Không cho thêm Todo rỗng", async ({ page }) => {
  await page.goto("/");

  await page.locator("#add-todo-button").click();

  await expect(page.locator("#form-message")).toContainText("Vui long nhap ten cong viec!");
});

test("TC-E2E-04: Đánh dấu Todo hoàn thành", async ({ page, request }) => {
  const todo = await createTodoByApi(request, `${TEST_PREFIX} hoàn thành`, false);
  await page.goto("/");

  const item = page.locator(`[data-id="${todo.id}"]`);
  await item.locator('[data-testid="todo-checkbox"]').check();

  await expect(item.locator(".todo-title")).toHaveCSS("text-decoration-line", "line-through");
});

test("TC-E2E-05: Lọc Todo chưa hoàn thành", async ({ page, request }) => {
  await createTodoByApi(request, `${TEST_PREFIX} active`, false);
  await createTodoByApi(request, `${TEST_PREFIX} done`, true);
  await page.goto("/");

  await page.locator("#filter-active").click();

  await expect(page.locator("#todo-list")).toContainText(`${TEST_PREFIX} active`);
  await expect(page.locator("#todo-list")).not.toContainText(`${TEST_PREFIX} done`);
});

test("TC-E2E-06: Lọc Todo đã hoàn thành", async ({ page, request }) => {
  await createTodoByApi(request, `${TEST_PREFIX} active`, false);
  await createTodoByApi(request, `${TEST_PREFIX} done`, true);
  await page.goto("/");

  await page.locator("#filter-completed").click();

  await expect(page.locator("#todo-list")).toContainText(`${TEST_PREFIX} done`);
  await expect(page.locator("#todo-list")).not.toContainText(`${TEST_PREFIX} active`);
});

test("TC-E2E-07: Sửa tên Todo", async ({ page, request }) => {
  const todo = await createTodoByApi(request, `${TEST_PREFIX} cần sửa`, false);
  await page.goto("/");

  page.on("dialog", async (dialog) => {
    await dialog.accept(`${TEST_PREFIX} đã sửa`);
  });

  await page.locator(`[data-id="${todo.id}"]`).locator('[data-testid="edit-todo-button"]').click();

  await expect(page.locator("#api-message")).toContainText("Cập nhật công việc thành công!");
  await expect(page.locator("#todo-list")).toContainText(`${TEST_PREFIX} đã sửa`);
});

test("TC-E2E-08: Xóa Todo", async ({ page, request }) => {
  const todo = await createTodoByApi(request, `${TEST_PREFIX} cần xóa`, false);
  await page.goto("/");

  page.on("dialog", async (dialog) => {
    await dialog.accept();
  });

  await page.locator(`[data-id="${todo.id}"]`).locator('[data-testid="delete-todo-button"]').click();

  await expect(page.locator("#api-message")).toContainText("Xóa công việc thành công!");
  await expect(page.locator("#todo-list")).not.toContainText(`${TEST_PREFIX} cần xóa`);
});
