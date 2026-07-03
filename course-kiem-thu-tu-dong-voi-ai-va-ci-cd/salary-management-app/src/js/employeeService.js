import { getData, createData, updateData, patchData } from './api.js';

function normalizeText(value) {
  return String(value ?? '').trim();
}

function normalizeEmployee(employee) {
  return {
    ...employee,
    employeeCode: normalizeText(employee.employeeCode),
    fullName: normalizeText(employee.fullName),
    department: normalizeText(employee.department),
    position: normalizeText(employee.position),
    baseSalary: Number(employee.baseSalary),
    salaryCoefficient: Number(employee.salaryCoefficient),
    allowance: Number(employee.allowance ?? 0),
    dependentCount: Number(employee.dependentCount ?? 0),
    status: employee.status || 'active'
  };
}

export async function getEmployees() {
  const employees = await getData('employees');
  return [...employees].sort((a, b) => a.employeeCode.localeCompare(b.employeeCode));
}

export async function searchEmployees(keyword = '', status = 'all') {
  const employees = await getEmployees();
  const normalizedKeyword = keyword.trim().toLowerCase();

  return employees.filter((employee) => {
    const matchKeyword =
      !normalizedKeyword ||
      employee.employeeCode.toLowerCase().includes(normalizedKeyword) ||
      employee.fullName.toLowerCase().includes(normalizedKeyword) ||
      employee.department.toLowerCase().includes(normalizedKeyword);

    const matchStatus = status === 'all' || employee.status === status;

    return matchKeyword && matchStatus;
  });
}

export function validateEmployee(employee, existingEmployees = [], editingId = '') {
  const data = normalizeEmployee(employee);
  const errors = [];

  if (!data.employeeCode) {
    errors.push('Mã nhân viên không được để trống.');
  }

  if (!data.fullName) {
    errors.push('Họ tên không được để trống.');
  }

  const duplicated = existingEmployees.some((item) => {
    const sameCode =
      item.employeeCode.toLowerCase() === data.employeeCode.toLowerCase();
    const differentEmployee = item.id !== editingId;
    return sameCode && differentEmployee;
  });

  if (duplicated) {
    errors.push('Mã nhân viên đã tồn tại.');
  }

  if (!Number.isFinite(data.baseSalary) || data.baseSalary <= 0) {
    errors.push('Lương cơ bản phải lớn hơn 0.');
  }

  if (!Number.isFinite(data.salaryCoefficient) || data.salaryCoefficient <= 0) {
    errors.push('Hệ số lương phải lớn hơn 0.');
  }

  if (!Number.isFinite(data.allowance) || data.allowance < 0) {
    errors.push('Phụ cấp không được âm.');
  }

  if (!Number.isInteger(data.dependentCount) || data.dependentCount < 0) {
    errors.push('Số người phụ thuộc không được âm.');
  }

  return errors;
}

export async function createEmployee(employee) {
  const data = normalizeEmployee(employee);
  const newEmployee = {
    id: `emp-${Date.now()}`,
    ...data,
    status: data.status || 'active',
    createdAt: new Date().toISOString()
  };

  return createData('employees', newEmployee);
}

export async function updateEmployee(id, employee) {
  const data = normalizeEmployee(employee);
  return updateData('employees', id, {
    id,
    ...data,
    createdAt: employee.createdAt || new Date().toISOString()
  });
}

export async function deactivateEmployee(id) {
  // Không xóa cứng để vẫn giữ được lịch sử bảng lương cũ.
  return patchData('employees', id, { status: 'inactive' });
}
