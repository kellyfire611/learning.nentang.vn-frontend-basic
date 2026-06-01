import { describe, expect, it } from "vitest";
import {
  validateKwh,
  calculateElectricityBill,
  formatCurrencyVnd,
  calculateElectricityPayment,
} from "../../src/electricityCalculatorStore.js";

describe("Unit test - Bài tập tính tiền điện cơ bản", () => {
  it("TC-UNIT-01: validateKwh trả lỗi khi bỏ trống", () => {
    expect(validateKwh("")).toBe("Vui lòng nhập số kWh điện!");
  });

  it("TC-UNIT-02: validateKwh trả lỗi khi không phải số", () => {
    expect(validateKwh("abc")).toBe("Số kWh điện phải là số hợp lệ!");
  });

  it("TC-UNIT-03: validateKwh trả lỗi khi số âm", () => {
    expect(validateKwh("-5")).toBe("Số kWh điện không được âm!");
  });

  it("TC-UNIT-04: validateKwh hợp lệ khi nhập 0", () => {
    expect(validateKwh("0")).toBe("");
  });

  it("TC-UNIT-05: validateKwh hợp lệ khi nhập số dương", () => {
    expect(validateKwh("80")).toBe("");
  });

  it("TC-UNIT-06: calculateElectricityBill tính đúng khi 0 kWh", () => {
    expect(calculateElectricityBill(0)).toBe(0);
  });

  it("TC-UNIT-07: calculateElectricityBill tính đúng khi 30 kWh", () => {
    expect(calculateElectricityBill(30)).toBe(54000);
  });

  it("TC-UNIT-08: calculateElectricityBill tính đúng tại biên 50 kWh", () => {
    expect(calculateElectricityBill(50)).toBe(90000);
  });

  it("TC-UNIT-09: calculateElectricityBill tính đúng khi 80 kWh", () => {
    expect(calculateElectricityBill(80)).toBe(150000);
  });

  it("TC-UNIT-10: calculateElectricityBill tính đúng tại biên 100 kWh", () => {
    expect(calculateElectricityBill(100)).toBe(190000);
  });

  it("TC-UNIT-11: calculateElectricityBill tính đúng khi 120 kWh", () => {
    expect(calculateElectricityBill(120)).toBe(240000);
  });

  it("TC-UNIT-12: formatCurrencyVnd trả đúng chuỗi tiền VNĐ", () => {
    expect(formatCurrencyVnd(54000)).toBe("54000 VNĐ");
  });

  it("TC-UNIT-13: calculateElectricityPayment trả lỗi khi bỏ trống", () => {
    expect(calculateElectricityPayment("")).toBe("Vui lòng nhập số kWh điện!");
  });

  it("TC-UNIT-14: calculateElectricityPayment trả đúng chuỗi kết quả khi hợp lệ", () => {
    expect(calculateElectricityPayment("30")).toBe("Số tiền điện cần trả: 54000 VNĐ");
  });
});
