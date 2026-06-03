import { describe, expect, it } from "vitest";
import {
  validateKwh,
  calculateElectricityBill,
  formatCurrencyVnd,
  calculateElectricityPayment,
} from "../../src/electricityCalculatorStore.js";

describe("Unit test - Bai tap tinh tien dien co ban", () => {
  it("TC-UNIT-01: validateKwh tra loi khi bo trong", () => {
    expect(validateKwh("")).toBe("Vui long nhap so kWh dien!");
  });

  it("TC-UNIT-02: validateKwh tra loi khi khong phai so", () => {
    expect(validateKwh("abc")).toBe("So kWh dien phai la so hop le!");
  });

  it("TC-UNIT-03: validateKwh tra loi khi so am", () => {
    expect(validateKwh("-5")).toBe("So kWh dien khong duoc am!");
  });

  it("TC-UNIT-04: validateKwh hop le khi nhap 0", () => {
    expect(validateKwh("0")).toBe("");
  });

  it("TC-UNIT-05: validateKwh hop le khi nhap so duong", () => {
    expect(validateKwh("80")).toBe("");
  });

  it("TC-UNIT-06: calculateElectricityBill tinh dung khi 0 kWh", () => {
    expect(calculateElectricityBill(0)).toBe(0);
  });

  it("TC-UNIT-07: calculateElectricityBill tinh dung khi 30 kWh", () => {
    expect(calculateElectricityBill(30)).toBe(54000);
  });

  it("TC-UNIT-08: calculateElectricityBill tinh dung tai bien 50 kWh", () => {
    expect(calculateElectricityBill(50)).toBe(90000);
  });

  it("TC-UNIT-09: calculateElectricityBill tinh dung khi 80 kWh", () => {
    expect(calculateElectricityBill(80)).toBe(150000);
  });

  it("TC-UNIT-10: calculateElectricityBill tinh dung tai bien 100 kWh", () => {
    expect(calculateElectricityBill(100)).toBe(190000);
  });

  it("TC-UNIT-11: calculateElectricityBill tinh dung khi 120 kWh", () => {
    expect(calculateElectricityBill(120)).toBe(240000);
  });

  it("TC-UNIT-12: formatCurrencyVnd tra dung chuoi tien VND", () => {
    expect(formatCurrencyVnd(54000)).toBe("54000 VND");
  });

  it("TC-UNIT-13: calculateElectricityPayment tra loi khi bo trong", () => {
    expect(calculateElectricityPayment("")).toBe("Vui long nhap so kWh dien!");
  });

  it("TC-UNIT-14: calculateElectricityPayment tra dung chuoi ket qua khi hop le", () => {
    expect(calculateElectricityPayment("30")).toBe("So tien dien can tra: 54000 VND");
  });
});
