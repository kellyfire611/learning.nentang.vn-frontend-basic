function toNumber(value, defaultValue = 0) {
  const numberValue = Number(value);
  return Number.isFinite(numberValue) ? numberValue : defaultValue;
}

function roundMoney(value) {
  return Math.round(toNumber(value));
}

function normalizeInput(input = {}) {
  return {
    baseSalary: toNumber(input.baseSalary),
    salaryCoefficient: toNumber(input.salaryCoefficient),
    standardWorkingDays: toNumber(input.standardWorkingDays, 26) || 26,
    actualWorkingDays: toNumber(input.actualWorkingDays, 26),
    overtimeHours: toNumber(input.overtimeHours),
    allowance: toNumber(input.allowance),
    bonus: toNumber(input.bonus),
    deduction: toNumber(input.deduction),
    advance: toNumber(input.advance),
    dependentCount: toNumber(input.dependentCount)
  };
}

export function calculateWorkingDaySalary(input = {}) {
  const data = normalizeInput(input);
  const salary =
    (data.baseSalary * data.salaryCoefficient * data.actualWorkingDays) /
    data.standardWorkingDays;

  return roundMoney(salary);
}

export function calculateOvertimePay(input = {}) {
  const data = normalizeInput(input);
  const hourlyRate =
    (data.baseSalary * data.salaryCoefficient) /
    data.standardWorkingDays /
    8;
  const overtimePay = hourlyRate * data.overtimeHours * 1.5;

  return roundMoney(overtimePay);
}

export function calculateGrossIncome(input = {}) {
  const data = normalizeInput(input);
  const workingDaySalary =
    input.workingDaySalary ?? calculateWorkingDaySalary(data);
  const overtimePay = input.overtimePay ?? calculateOvertimePay(data);

  return roundMoney(
    workingDaySalary + data.allowance + overtimePay + data.bonus
  );
}

export function calculateInsuranceAmount(input = {}) {
  const data = normalizeInput(input);
  return roundMoney(data.baseSalary * data.salaryCoefficient * 0.105);
}

export function calculatePersonalTax(input = {}) {
  const data = normalizeInput(input);
  const grossIncome = input.grossIncome ?? calculateGrossIncome(data);
  const insuranceAmount =
    input.insuranceAmount ?? calculateInsuranceAmount(data);

  const taxableIncome =
    grossIncome - insuranceAmount - 11000000 - data.dependentCount * 4400000;

  if (taxableIncome <= 0) {
    return 0;
  }

  return roundMoney(taxableIncome * 0.05);
}

export function calculateNetSalary(input = {}) {
  const data = normalizeInput(input);
  const grossIncome = input.grossIncome ?? calculateGrossIncome(data);
  const insuranceAmount =
    input.insuranceAmount ?? calculateInsuranceAmount(data);
  const personalTax = input.personalTax ?? calculatePersonalTax({
    ...data,
    grossIncome,
    insuranceAmount
  });

  return roundMoney(
    grossIncome - insuranceAmount - personalTax - data.deduction - data.advance
  );
}

export function calculatePayrollItem(input = {}) {
  const data = normalizeInput(input);
  const workingDaySalary = calculateWorkingDaySalary(data);
  const overtimePay = calculateOvertimePay(data);
  const grossIncome = calculateGrossIncome({
    ...data,
    workingDaySalary,
    overtimePay
  });
  const insuranceAmount = calculateInsuranceAmount(data);
  const personalTax = calculatePersonalTax({
    ...data,
    grossIncome,
    insuranceAmount
  });
  const netSalary = calculateNetSalary({
    ...data,
    grossIncome,
    insuranceAmount,
    personalTax
  });

  return {
    ...input,
    standardWorkingDays: data.standardWorkingDays,
    actualWorkingDays: data.actualWorkingDays,
    overtimeHours: data.overtimeHours,
    allowance: data.allowance,
    bonus: data.bonus,
    deduction: data.deduction,
    advance: data.advance,
    dependentCount: data.dependentCount,
    workingDaySalary,
    overtimePay,
    grossIncome,
    insuranceAmount,
    personalTax,
    netSalary
  };
}
