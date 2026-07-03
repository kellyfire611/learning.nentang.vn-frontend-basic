import { test, expect } from '@playwright/test';

const API_BASE_URL = 'http://localhost:3000';
const TEST_EMPLOYEE_CODE = 'NV999';

async function deleteTestEmployees(request) {
  const response = await request.get(`${API_BASE_URL}/employees`);
  const employees = await response.json();
  const testEmployees = employees.filter(
    (employee) => employee.employeeCode === TEST_EMPLOYEE_CODE
  );

  for (const employee of testEmployees) {
    try {
      await request.delete(`${API_BASE_URL}/employees/${employee.id}`);
    } catch {
      // Ignore cleanup races when another worker already removed this record.
    }
  }
}

async function createTestEmployee(request) {
  await request.post(`${API_BASE_URL}/employees`, {
    data: {
      id: `emp-e2e-${Date.now()}`,
      employeeCode: TEST_EMPLOYEE_CODE,
      fullName: 'Test Nhân Viên',
      department: 'Kiểm thử',
      position: 'Nhân viên test',
      baseSalary: 2530000,
      salaryCoefficient: 2.5,
      allowance: 300000,
      dependentCount: 0,
      status: 'active',
      createdAt: new Date().toISOString()
    }
  });
}

test.describe('employees.html', () => {
  test.beforeEach(async ({ request }) => {
    await deleteTestEmployees(request);
  });

  test('E2E01: mở trang employees.html và kiểm tra tiêu đề', async ({ page }) => {
    await page.goto('/employees.html');

    await expect(page.getByRole('heading', { name: 'Quản lý nhân viên' })).toBeVisible();
  });

  test('E2E02: thêm nhân viên mới thành công', async ({ page }) => {
    await page.goto('/employees.html');

    await page.locator('#employee-code-input').fill(TEST_EMPLOYEE_CODE);
    await page.locator('#employee-name-input').fill('Test Nhân Viên');
    await page.locator('#employee-department-input').fill('Kiểm thử');
    await page.locator('#employee-position-input').fill('Nhân viên test');
    await page.locator('#base-salary-input').fill('2530000');
    await page.locator('#salary-coefficient-input').fill('2.5');
    await page.locator('#allowance-input').fill('300000');
    await page.locator('#dependent-count-input').fill('0');
    await page.locator('#save-employee-button').click();

    await expect(page.locator('#employee-message')).toContainText('Thêm nhân viên thành công');
    await expect(page.locator('#employee-table-body')).toContainText('Test Nhân Viên');
  });

  test('E2E03: không cho thêm nhân viên khi thiếu họ tên', async ({ page }) => {
    await page.goto('/employees.html');

    await page.locator('#employee-code-input').fill(TEST_EMPLOYEE_CODE);
    await page.locator('#employee-name-input').fill('');
    await page.locator('#base-salary-input').fill('2530000');
    await page.locator('#salary-coefficient-input').fill('2.5');
    await page.locator('#save-employee-button').click();

    await expect(page.locator('#employee-message')).toContainText('Họ tên không được để trống');
  });

  test('E2E04: tìm kiếm nhân viên theo tên', async ({ page, request }) => {
    await createTestEmployee(request);
    await page.goto('/employees.html');

    await page.locator('#search-employee-input').fill('Test Nhân Viên');

    await expect(page.locator('#employee-table-body')).toContainText('Test Nhân Viên');
    await expect(page.locator('#employee-table-body')).toContainText(TEST_EMPLOYEE_CODE);
  });

  test('E2E05: cập nhật hệ số lương', async ({ page, request }) => {
    await createTestEmployee(request);
    await page.goto('/employees.html');

    await page.locator('#search-employee-input').fill('Test Nhân Viên');
    await page.locator('#employee-table-body button[data-action="edit"]').first().click();
    await page.locator('#salary-coefficient-input').fill('3.1');
    await page.locator('#save-employee-button').click();

    await expect(page.locator('#employee-message')).toContainText('Cập nhật nhân viên thành công');
    await page.locator('#search-employee-input').fill('Test Nhân Viên');
    await expect(page.locator('#employee-table-body')).toContainText('3.1');
  });

  test('E2E06: ngừng hoạt động nhân viên', async ({ page, request }) => {
    await createTestEmployee(request);
    await page.goto('/employees.html');

    page.on('dialog', async (dialog) => {
      await dialog.accept();
    });

    await page.locator('#search-employee-input').fill('Test Nhân Viên');
    await page.locator('#employee-table-body button[data-action="deactivate"]').first().click();

    await expect(page.locator('#employee-message')).toContainText('Đã chuyển nhân viên sang trạng thái nghỉ việc');
    await page.locator('#filter-status-select').selectOption('inactive');
    await page.locator('#search-employee-input').fill('Test Nhân Viên');
    await expect(page.locator('#employee-table-body')).toContainText('Nghỉ việc');
  });
});
