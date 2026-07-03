import { beforeEach, describe, expect, it, vi } from 'vitest';

const mockDb = vi.hoisted(() => ({
  employees: [],
  payrolls: []
}));

vi.mock('../../src/js/api.js', () => ({
  getData: vi.fn(async (resource) => mockDb[resource]),
  getDataById: vi.fn(async (resource, id) => {
    const item = mockDb[resource].find((record) => record.id === id);
    if (!item) throw new Error('Không tìm thấy dữ liệu.');
    return item;
  }),
  createData: vi.fn(async (resource, data) => {
    mockDb[resource].push(data);
    return data;
  }),
  updateData: vi.fn(async (resource, id, data) => {
    const index = mockDb[resource].findIndex((record) => record.id === id);
    if (index === -1) throw new Error('Không tìm thấy dữ liệu.');
    mockDb[resource][index] = data;
    return data;
  }),
  patchData: vi.fn(async (resource, id, data) => {
    const index = mockDb[resource].findIndex((record) => record.id === id);
    if (index === -1) throw new Error('Không tìm thấy dữ liệu.');
    mockDb[resource][index] = { ...mockDb[resource][index], ...data };
    return mockDb[resource][index];
  })
}));

import {
  createPayroll,
  recalculatePayrollItem,
  updatePayroll,
  lockPayroll,
  calculateTotalNetSalary
} from '../../src/js/payrollService.js';

function seedEmployees() {
  mockDb.employees = [
    {
      id: 'emp-001',
      employeeCode: 'NV001',
      fullName: 'Nguyễn Văn An',
      department: 'Đào tạo',
      position: 'Giảng viên',
      baseSalary: 2530000,
      salaryCoefficient: 3,
      allowance: 500000,
      dependentCount: 1,
      status: 'active'
    },
    {
      id: 'emp-002',
      employeeCode: 'NV002',
      fullName: 'Trần Thị Bình',
      department: 'Tư vấn',
      position: 'Nhân viên tư vấn',
      baseSalary: 2530000,
      salaryCoefficient: 2.34,
      allowance: 300000,
      dependentCount: 0,
      status: 'active'
    },
    {
      id: 'emp-003',
      employeeCode: 'NV003',
      fullName: 'Lê Văn Cường',
      department: 'Kỹ thuật',
      position: 'Nhân viên kỹ thuật',
      baseSalary: 2530000,
      salaryCoefficient: 2.67,
      allowance: 400000,
      dependentCount: 2,
      status: 'inactive'
    }
  ];
}

describe('payroll business rules', () => {
  beforeEach(() => {
    seedEmployees();
    mockDb.payrolls = [];
  });

  it('BT01: tạo bảng lương từ danh sách nhân viên active', async () => {
    const payroll = await createPayroll(7, 2026);

    expect(payroll.items).toHaveLength(2);
    expect(payroll.items.map((item) => item.employeeId)).toEqual([
      'emp-001',
      'emp-002'
    ]);
  });

  it('BT02: nhân viên inactive không có trong bảng lương mới', async () => {
    const payroll = await createPayroll(7, 2026);

    expect(payroll.items.some((item) => item.employeeId === 'emp-003')).toBe(false);
  });

  it('BT03: không cho tạo trùng bảng lương cùng tháng/năm', async () => {
    await createPayroll(7, 2026);

    await expect(createPayroll(7, 2026)).rejects.toThrow(
      'Bảng lương tháng này đã tồn tại'
    );
  });

  it('BT04: khi tạo bảng lương, thông tin nhân viên được snapshot', async () => {
    const payroll = await createPayroll(7, 2026);
    const item = payroll.items.find((record) => record.employeeId === 'emp-001');

    expect(item).toMatchObject({
      employeeCode: 'NV001',
      fullName: 'Nguyễn Văn An',
      department: 'Đào tạo',
      position: 'Giảng viên',
      baseSalary: 2530000,
      salaryCoefficient: 3
    });

    mockDb.employees[0].salaryCoefficient = 9;
    expect(item.salaryCoefficient).toBe(3);
  });

  it('BT05: cập nhật ngày công làm thay đổi netSalary', async () => {
    const payroll = await createPayroll(7, 2026);
    const item = payroll.items[0];

    const updatedItem = recalculatePayrollItem({
      ...item,
      actualWorkingDays: 20
    });

    expect(updatedItem.netSalary).not.toBe(item.netSalary);
    expect(updatedItem.netSalary).toBeLessThan(item.netSalary);
  });

  it('BT06: cập nhật thưởng làm tăng grossIncome', async () => {
    const payroll = await createPayroll(7, 2026);
    const item = payroll.items[0];

    const updatedItem = recalculatePayrollItem({
      ...item,
      bonus: 1000000
    });

    expect(updatedItem.grossIncome).toBeGreaterThan(item.grossIncome);
  });

  it('BT07: cập nhật khấu trừ làm giảm netSalary', async () => {
    const payroll = await createPayroll(7, 2026);
    const item = payroll.items[0];

    const updatedItem = recalculatePayrollItem({
      ...item,
      deduction: 500000
    });

    expect(updatedItem.netSalary).toBeLessThan(item.netSalary);
  });

  it('BT08: tổng quỹ lương bằng tổng netSalary của tất cả nhân viên', async () => {
    const payroll = await createPayroll(7, 2026);
    const expectedTotal = payroll.items.reduce(
      (total, item) => total + item.netSalary,
      0
    );

    expect(calculateTotalNetSalary(payroll)).toBe(expectedTotal);
  });

  it('BT09: khóa bảng lương chuyển status thành locked', async () => {
    const payroll = await createPayroll(7, 2026);
    const lockedPayroll = await lockPayroll(payroll.id);

    expect(lockedPayroll.status).toBe('locked');
  });

  it('BT10: không cho sửa bảng lương đã locked', async () => {
    const payroll = await createPayroll(7, 2026);
    const lockedPayroll = await lockPayroll(payroll.id);

    await expect(updatePayroll(lockedPayroll)).rejects.toThrow(
      'Bảng lương đã khóa'
    );
  });
});
