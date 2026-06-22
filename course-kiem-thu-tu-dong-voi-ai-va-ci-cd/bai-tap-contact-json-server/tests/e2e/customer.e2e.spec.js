import { expect, test } from '@playwright/test';

const apiBaseUrl = 'http://localhost:3001';

function uniquePhone() {
  return `09${String(Date.now()).slice(-8)}`;
}

async function createCustomerByApi(overrides = {}) {
  const customer = {
    fullName: `E2E User ${Date.now()}`,
    phone: uniquePhone(),
    email: 'e2e@example.com',
    course: 'Playwright cơ bản',
    status: 'new',
    isFavorite: false,
    note: 'Tạo bởi E2E test',
    ...overrides,
  };

  const response = await fetch(`${apiBaseUrl}/customers`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(customer),
  });

  return response.json();
}

async function cleanupById(id) {
  if (!id) return;
  try {
    await fetch(`${apiBaseUrl}/customers/${id}`, { method: 'DELETE' });
  } catch {
    // Bỏ qua nếu dữ liệu đã bị xóa.
  }
}

async function cleanupByPhone(phone) {
  if (!phone) return;
  const response = await fetch(`${apiBaseUrl}/customers?phone=${encodeURIComponent(phone)}`);
  const customers = await response.json();

  await Promise.all(customers.map((customer) => cleanupById(customer.id)));
}

test('TC-E2E-001: Trang tải được danh sách khách hàng', async ({ page }) => {
  await page.goto('/');

  await expect(page.getByTestId('customerRow').first()).toBeVisible();
  await expect(page.getByText('Nguyễn Văn An')).toBeVisible();
});

test('TC-E2E-002: Thêm khách hàng mới thành công', async ({ page }) => {
  const phone = uniquePhone();

  await page.goto('/');
  await page.getByTestId('fullNameInput').fill('Khách Test E2E');
  await page.getByTestId('phoneInput').fill(phone);
  await page.getByTestId('emailInput').fill('khach.e2e@example.com');
  await page.getByTestId('courseInput').fill('Lập trình Web');
  await page.getByTestId('noteInput').fill('Đăng ký từ E2E test');
  await page.getByTestId('submitButton').click();

  await expect(page.getByText('Đã thêm khách hàng mới.')).toBeVisible();
  await expect(page.getByText('Khách Test E2E')).toBeVisible();

  await cleanupByPhone(phone);
});

test('TC-E2E-003: Thêm khách hàng thiếu họ tên thì báo lỗi', async ({ page }) => {
  await page.goto('/');
  await page.getByTestId('phoneInput').fill('0911111111');
  await page.getByTestId('courseInput').fill('JavaScript cơ bản');
  await page.getByTestId('submitButton').click();

  await expect(page.getByText('Họ tên không được rỗng')).toBeVisible();
  await expect(page.getByText('Vui lòng kiểm tra lại thông tin nhập.')).toBeVisible();
});

test('TC-E2E-004: Đánh dấu khách hàng đã tư vấn', async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: 'E2E Đánh dấu tư vấn' });

  try {
    await page.goto('/');
    await page.getByTestId(`markContacted-${customer.id}`).click();

    await expect(page.getByText('Đã cập nhật trạng thái: Đã tư vấn.')).toBeVisible();
    const row = page.locator(`[data-testid="customerRow"][data-id="${customer.id}"]`);
    await expect(row.getByTestId('customerStatus')).toHaveText('Đã tư vấn');
  } finally {
    await cleanupById(customer.id);
  }
});

test('TC-E2E-005: Lọc danh sách khách đã đăng ký', async ({ page }) => {
  const customer = await createCustomerByApi({
    fullName: 'E2E Registered User',
    status: 'registered',
  });

  try {
    await page.goto('/');
    await page.getByTestId('filterRegistered').click();

    await expect(page.getByText('E2E Registered User')).toBeVisible();

    const statuses = await page.getByTestId('customerStatus').allTextContents();
    expect(statuses.length).toBeGreaterThan(0);
    expect(statuses.every((status) => status === 'Đã đăng ký')).toBe(true);
  } finally {
    await cleanupById(customer.id);
  }
});

test('TC-E2E-006: Tìm kiếm theo số điện thoại', async ({ page }) => {
  const phone = uniquePhone();
  const customer = await createCustomerByApi({
    fullName: 'E2E Search Phone',
    phone,
  });

  try {
    await page.goto('/');
    await page.getByTestId('searchInput').fill(phone);

    await expect(page.getByText('E2E Search Phone')).toBeVisible();
    const rows = await page.getByTestId('customerRow').count();
    expect(rows).toBe(1);
  } finally {
    await cleanupById(customer.id);
  }
});

test('TC-E2E-007: Xóa khách hàng khỏi danh sách', async ({ page }) => {
  const customer = await createCustomerByApi({ fullName: 'E2E Delete User' });

  page.on('dialog', async (dialog) => {
    expect(dialog.type()).toBe('confirm');
    await dialog.accept();
  });

  await page.goto('/');
  await page.getByTestId(`deleteCustomer-${customer.id}`).click();

  await expect(page.getByText('Đã xóa khách hàng.')).toBeVisible();
  await expect(page.getByText('E2E Delete User')).toBeHidden();

  await cleanupById(customer.id);
});
