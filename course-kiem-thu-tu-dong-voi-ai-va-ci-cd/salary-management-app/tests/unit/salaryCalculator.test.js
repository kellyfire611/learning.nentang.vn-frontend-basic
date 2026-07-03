import { describe, it, expect } from 'vitest';
import {
  calculateWorkingDaySalary,
  calculateOvertimePay,
  calculateGrossIncome,
  calculateInsuranceAmount,
  calculatePersonalTax,
  calculateNetSalary,
  calculatePayrollItem
} from '../../src/js/salaryCalculator.js';

describe('salaryCalculator', () => {
  it('UT01: tính lương đủ 26 ngày công', () => {
    const result = calculateWorkingDaySalary({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      standardWorkingDays: 26,
      actualWorkingDays: 26
    });

    expect(result).toBe(7590000);
  });

  it('UT02: tính lương 13/26 ngày công', () => {
    const result = calculateWorkingDaySalary({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      standardWorkingDays: 26,
      actualWorkingDays: 13
    });

    expect(result).toBe(3795000);
  });

  it('UT03: tăng ca 0 giờ thì overtimePay bằng 0', () => {
    const result = calculateOvertimePay({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      standardWorkingDays: 26,
      overtimeHours: 0
    });

    expect(result).toBe(0);
  });

  it('UT04: tăng ca 8 giờ tính đúng công thức', () => {
    const result = calculateOvertimePay({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      standardWorkingDays: 26,
      overtimeHours: 8
    });

    expect(result).toBe(437885);
  });

  it('UT05: gross income gồm lương ngày công, phụ cấp, tăng ca và thưởng', () => {
    const result = calculateGrossIncome({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      standardWorkingDays: 26,
      actualWorkingDays: 26,
      allowance: 500000,
      overtimeHours: 8,
      bonus: 1000000
    });

    expect(result).toBe(9527885);
  });

  it('UT06: bảo hiểm bằng baseSalary * coefficient * 10.5%', () => {
    const result = calculateInsuranceAmount({
      baseSalary: 2530000,
      salaryCoefficient: 3
    });

    expect(result).toBe(796950);
  });

  it('UT07: thu nhập chưa tới mức chịu thuế thì personalTax bằng 0', () => {
    const result = calculatePersonalTax({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      grossIncome: 8000000,
      insuranceAmount: 737100,
      dependentCount: 1
    });

    expect(result).toBe(0);
  });

  it('UT08: thu nhập vượt mức chịu thuế thì personalTax bằng taxableIncome * 5%', () => {
    const result = calculatePersonalTax({
      baseSalary: 2530000,
      salaryCoefficient: 3,
      grossIncome: 20000000,
      insuranceAmount: 737100,
      dependentCount: 0
    });

    expect(result).toBe(413145);
  });

  it('UT09: net salary bằng gross - insurance - tax - deduction - advance', () => {
    const result = calculateNetSalary({
      grossIncome: 10000000,
      insuranceAmount: 737100,
      personalTax: 0,
      deduction: 200000,
      advance: 500000
    });

    expect(result).toBe(8562900);
  });

  it('UT10: calculatePayrollItem trả về đầy đủ các trường tính lương', () => {
    const item = calculatePayrollItem({
      employeeId: 'emp-001',
      employeeCode: 'NV001',
      fullName: 'Nguyễn Văn An',
      baseSalary: 2530000,
      salaryCoefficient: 3,
      allowance: 500000,
      dependentCount: 1,
      standardWorkingDays: 26,
      actualWorkingDays: 26,
      overtimeHours: 8,
      bonus: 1000000,
      deduction: 200000,
      advance: 500000
    });

    expect(item).toMatchObject({
      workingDaySalary: 7590000,
      overtimePay: 437885,
      grossIncome: 9527885,
      insuranceAmount: 796950,
      personalTax: 0,
      netSalary: 8030935
    });
  });
});
