import { test, expect } from '@playwright/test';

const API_BASE_URL = 'http://localhost:3000';
const DEFAULT_TEST_MONTH = '12';

function buildTestPeriod(testInfo) {
  const uniqueYear = 3000 + (Date.now() % 100000) + testInfo.workerIndex * 1000;

  return {
    month: DEFAULT_TEST_MONTH,
    year: String(uniqueYear)
  };
}

function parseCurrency(text) {
  return Number(String(text).replace(/[^0-9-]/g, ''));
}

async function deleteTestPayroll(request, period) {
  const response = await request.get(`${API_BASE_URL}/payrolls`);
  const payrolls = await response.json();
  const testPayrolls = payrolls.filter(
    (payroll) =>
      Number(payroll.month) === Number(period.month) &&
      Number(payroll.year) === Number(period.year)
  );

  for (const payroll of testPayrolls) {
    await request.delete(`${API_BASE_URL}/payrolls/${payroll.id}`);
  }
}

async function getTestPayroll(request, period) {
  const response = await request.get(`${API_BASE_URL}/payrolls`);
  const payrolls = await response.json();

  return payrolls.find(
    (payroll) =>
      Number(payroll.month) === Number(period.month) &&
      Number(payroll.year) === Number(period.year)
  );
}

async function createPayrollFromUi(page, request, period) {
  await deleteTestPayroll(request, period);
  await page.goto('/payroll.html');
  await page.locator('#payroll-month-select').selectOption(period.month);
  await page.locator('#payroll-year-input').fill(period.year);
  await page.locator('#create-payroll-button').click();
  await expect(page.locator('#payroll-status')).toContainText('draft');
}

async function firstEmployeeId(page) {
  const firstRow = page.locator('#payroll-table-body tr').first();
  return firstRow.getAttribute('data-employee-id');
}

test.describe('payroll.html', () => {
  test('E2E07: mở trang payroll.html và kiểm tra tiêu đề', async ({ page }) => {
    await page.goto('/payroll.html');

    await expect(page.getByRole('heading', { name: 'Lập bảng lương' })).toBeVisible();
  });

  test('E2E08: tạo bảng lương cho tháng mới', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const payroll = await getTestPayroll(request, period);
    const rowCount = await page.locator('#payroll-table-body tr').count();

    expect(payroll).toBeTruthy();
    expect(rowCount).toBe(payroll.items.length);
    await expect(page.locator('#total-net-salary')).not.toContainText('0 ₫');
  });

  test('E2E09: không cho tạo bảng lương trùng tháng/năm', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    await page.locator('#create-payroll-button').click();

    await expect(page.locator('#payroll-message')).toContainText('Bảng lương tháng này đã tồn tại');
  });

  test('E2E10: nhập ngày công và hệ thống tính lại lương', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const employeeId = await firstEmployeeId(page);
    const netSalaryCell = page.getByTestId(`net-salary-${employeeId}`);
    const before = parseCurrency(await netSalaryCell.textContent());

    await page.getByTestId(`actual-working-days-${employeeId}`).fill('20');
    await page.getByTestId(`actual-working-days-${employeeId}`).blur();

    const after = parseCurrency(await netSalaryCell.textContent());
    expect(after).not.toBe(before);
    expect(after).toBeLessThan(before);
  });

  test('E2E11: nhập thưởng và lương thực nhận tăng', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const employeeId = await firstEmployeeId(page);
    const netSalaryCell = page.getByTestId(`net-salary-${employeeId}`);
    const before = parseCurrency(await netSalaryCell.textContent());

    await page.getByTestId(`bonus-${employeeId}`).fill('1000000');
    await page.getByTestId(`bonus-${employeeId}`).blur();

    const after = parseCurrency(await netSalaryCell.textContent());
    expect(after).toBeGreaterThan(before);
  });

  test('E2E12: nhập tạm ứng và lương thực nhận giảm', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const employeeId = await firstEmployeeId(page);
    const netSalaryCell = page.getByTestId(`net-salary-${employeeId}`);
    const before = parseCurrency(await netSalaryCell.textContent());

    await page.getByTestId(`advance-${employeeId}`).fill('500000');
    await page.getByTestId(`advance-${employeeId}`).blur();

    const after = parseCurrency(await netSalaryCell.textContent());
    expect(after).toBeLessThan(before);
  });

  test('E2E13: khóa bảng lương thành công', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const employeeId = await firstEmployeeId(page);

    page.on('dialog', async (dialog) => {
      await dialog.accept();
    });

    await page.locator('#lock-payroll-button').click();

    await expect(page.locator('#payroll-status')).toContainText('locked');
    await expect(page.getByTestId(`actual-working-days-${employeeId}`)).toBeDisabled();
    await expect(page.getByTestId(`bonus-${employeeId}`)).toBeDisabled();
  });

  test('E2E14: bảng lương đã khóa không cho chỉnh sửa', async ({ page, request }, testInfo) => {
    const period = buildTestPeriod(testInfo);
    await createPayrollFromUi(page, request, period);
    const employeeId = await firstEmployeeId(page);

    page.on('dialog', async (dialog) => {
      await dialog.accept();
    });

    await page.locator('#lock-payroll-button').click();

    await expect(page.getByTestId(`actual-working-days-${employeeId}`)).toBeDisabled();
    await expect(page.getByTestId(`overtime-hours-${employeeId}`)).toBeDisabled();
    await expect(page.getByTestId(`deduction-${employeeId}`)).toBeDisabled();
    await expect(page.getByTestId(`advance-${employeeId}`)).toBeDisabled();
  });
});
