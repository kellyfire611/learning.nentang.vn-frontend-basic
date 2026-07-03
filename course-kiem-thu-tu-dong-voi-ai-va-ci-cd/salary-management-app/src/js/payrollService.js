import { getData, getDataById, createData, updateData, patchData } from './api.js';
import { calculatePayrollItem } from './salaryCalculator.js';

function normalizeMonthYear(month, year) {
  return {
    month: Number(month),
    year: Number(year)
  };
}

function buildPayrollId(month, year) {
  return `payroll-${year}-${String(month).padStart(2, '0')}`;
}

export async function getPayrolls() {
  return getData('payrolls');
}

export async function getPayrollByMonthYear(month, year) {
  const normalized = normalizeMonthYear(month, year);
  const payrolls = await getPayrolls();

  return payrolls.find(
    (payroll) =>
      Number(payroll.month) === normalized.month &&
      Number(payroll.year) === normalized.year
  );
}

export async function createPayroll(month, year) {
  const normalized = normalizeMonthYear(month, year);

  if (!normalized.month || normalized.month < 1 || normalized.month > 12) {
    throw new Error('Tháng lập lương không hợp lệ.');
  }

  if (!normalized.year || normalized.year < 2000) {
    throw new Error('Năm lập lương không hợp lệ.');
  }

  const existingPayroll = await getPayrollByMonthYear(
    normalized.month,
    normalized.year
  );

  if (existingPayroll) {
    throw new Error('Bảng lương tháng này đã tồn tại.');
  }

  const employees = await getData('employees');
  const activeEmployees = employees.filter((employee) => employee.status === 'active');

  if (activeEmployees.length === 0) {
    throw new Error('Không có nhân viên đang làm việc để lập bảng lương.');
  }

  const payroll = {
    id: buildPayrollId(normalized.month, normalized.year),
    month: normalized.month,
    year: normalized.year,
    status: 'draft',
    items: activeEmployees.map((employee) =>
      calculatePayrollItem({
        employeeId: employee.id,
        employeeCode: employee.employeeCode,
        fullName: employee.fullName,
        department: employee.department,
        position: employee.position,
        baseSalary: employee.baseSalary,
        salaryCoefficient: employee.salaryCoefficient,
        allowance: employee.allowance,
        dependentCount: employee.dependentCount,
        standardWorkingDays: 26,
        actualWorkingDays: 26,
        overtimeHours: 0,
        bonus: 0,
        deduction: 0,
        advance: 0
      })
    ),
    createdAt: new Date().toISOString()
  };

  return createData('payrolls', payroll);
}

export function recalculatePayrollItem(item) {
  return calculatePayrollItem(item);
}

export async function updatePayroll(payroll) {
  if (payroll.status === 'locked') {
    throw new Error('Bảng lương đã khóa, không thể chỉnh sửa.');
  }

  const recalculatedPayroll = {
    ...payroll,
    items: payroll.items.map((item) => recalculatePayrollItem(item))
  };

  return updateData('payrolls', payroll.id, recalculatedPayroll);
}

export async function lockPayroll(id) {
  const payroll = await getDataById('payrolls', id);

  if (payroll.status === 'locked') {
    return payroll;
  }

  return patchData('payrolls', id, { status: 'locked' });
}

export function calculateTotalNetSalary(payroll) {
  if (!payroll || !Array.isArray(payroll.items)) {
    return 0;
  }

  return payroll.items.reduce((total, item) => total + Number(item.netSalary || 0), 0);
}
