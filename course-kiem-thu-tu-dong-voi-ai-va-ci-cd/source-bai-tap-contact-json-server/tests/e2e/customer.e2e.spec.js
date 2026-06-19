import { expect, test } from "@playwright/test";

const API_URL = "http://localhost:3001/customers";

async function createCustomerByApi(overrides = {}) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      fullName: `E2E Customer ${Date.now()}`,
      phone: "0912345678",
      email: "e2e@example.com",
      course: "Playwright E2E Testing",
      status: "new",
      isFavorite: false,
      note: "Du lieu E2E",
      ...overrides,
    }),
  });

  return response.json();
}

async function deleteCustomerByApi(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" }).catch(() => null);
}

test("TC-E2E-001: page loads customer list", async ({ page }) => {
  await page.goto("/");

  await expect(page.getByRole("heading", { name: "Quản lý danh bạ khách hàng" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Danh sách khách hàng" })).toBeVisible();
});

test("TC-E2E-002: create new customer", async ({ page }) => {
  const fullName = `Khach E2E ${Date.now()}`;

  await page.goto("/");
  await page.locator("#customer-full-name-input").fill(fullName);
  await page.locator("#customer-phone-input").fill("0912345678");
  await page.locator("#customer-email-input").fill("khach.e2e@example.com");
  await page.locator("#customer-course-input").fill("Vitest co ban");
  await page.locator("#customer-note-input").fill("Them tu E2E test");
  await page.locator("#submit-customer-button").click();

  await expect(page.getByText(fullName)).toBeVisible();

  const customers = await (await fetch(`${API_URL}?fullName=${encodeURIComponent(fullName)}`)).json();
  await Promise.all(customers.map((customer) => deleteCustomerByApi(customer.id)));
});

test("TC-E2E-003: show validation error when full name is missing", async ({ page }) => {
  await page.goto("/");
  await page.locator("#customer-phone-input").fill("0912345678");
  await page.locator("#customer-course-input").fill("Vitest co ban");
  await page.locator("#submit-customer-button").click();

  await expect(page.getByText("Vui lòng nhập họ tên khách hàng!")).toBeVisible();
});

test("TC-E2E-004: mark customer as contacted", async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: `Tu Van E2E ${Date.now()}` });

  await page.goto("/");
  const card = page.locator(".customer-card", { hasText: customer.fullName });
  await card.getByRole("button", { name: "Đã tư vấn" }).click();

  await expect(card.getByText("Đã tư vấn").first()).toBeVisible();
  await deleteCustomerByApi(customer.id);
});

test("TC-E2E-005: filter registered customers", async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: `Dang Ky E2E ${Date.now()}`, status: "registered" });

  await page.goto("/");
  await page.getByRole("button", { name: "Đã đăng ký" }).first().click();

  await expect(page.getByText(customer.fullName)).toBeVisible();
  await deleteCustomerByApi(customer.id);
});

test("TC-E2E-006: search by phone", async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: `Search E2E ${Date.now()}`, phone: "0909999888" });

  await page.goto("/");
  await page.locator("#customer-search-input").fill("0909999888");

  await expect(page.getByText(customer.fullName)).toBeVisible();
  await deleteCustomerByApi(customer.id);
});

test("TC-E2E-007: delete customer from list", async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: `Delete E2E ${Date.now()}` });

  page.on("dialog", (dialog) => dialog.accept());
  await page.goto("/");
  const card = page.locator(".customer-card", { hasText: customer.fullName });
  await card.getByRole("button", { name: "Xóa" }).click();

  await expect(page.getByText(customer.fullName)).not.toBeVisible();
});
