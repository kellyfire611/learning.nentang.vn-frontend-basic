import { describe, expect, it } from "vitest";
import { calculateElectricityPayment } from "../../src/electricityCalculatorStore.js";

describe("Business test - Kịch bản nghiệp vụ tính tiền điện", () => {
  it("TC-BIZ-01: Cho trước bỏ trống số kWh, Khi tính tiền điện, Thì yêu cầu nhập số kWh", () => {
    expect(calculateElectricityPayment("")).toBe("Vui lòng nhập số kWh điện!");
  });

  it("TC-BIZ-02: Cho trước số kWh không phải số, Khi tính tiền điện, Thì báo dữ liệu không hợp lệ", () => {
    expect(calculateElectricityPayment("abc")).toBe("Số kWh điện phải là số hợp lệ!");
  });

  it("TC-BIZ-03: Cho trước số kWh âm, Khi tính tiền điện, Thì báo số kWh không được âm", () => {
    expect(calculateElectricityPayment("-5")).toBe("Số kWh điện không được âm!");
  });

  it("TC-BIZ-04: Cho trước 0 kWh, Khi tính tiền điện, Thì tiền điện bằng 0", () => {
    expect(calculateElectricityPayment("0")).toBe("Số tiền điện cần trả: 0 VNĐ");
  });

  it("TC-BIZ-05: Cho trước 30 kWh, Khi tính tiền điện, Thì tính theo bậc 1", () => {
    expect(calculateElectricityPayment("30")).toBe("Số tiền điện cần trả: 54000 VNĐ");
  });

  it("TC-BIZ-06: Cho trước 50 kWh, Khi tính tiền điện, Thì tính đúng tại biên bậc 1", () => {
    expect(calculateElectricityPayment("50")).toBe("Số tiền điện cần trả: 90000 VNĐ");
  });

  it("TC-BIZ-07: Cho trước 80 kWh, Khi tính tiền điện, Thì tính đúng bậc 1 và bậc 2", () => {
    expect(calculateElectricityPayment("80")).toBe("Số tiền điện cần trả: 150000 VNĐ");
  });

  it("TC-BIZ-08: Cho trước 100 kWh, Khi tính tiền điện, Thì tính đúng tại biên bậc 2", () => {
    expect(calculateElectricityPayment("100")).toBe("Số tiền điện cần trả: 190000 VNĐ");
  });

  it("TC-BIZ-09: Cho trước 120 kWh, Khi tính tiền điện, Thì tính đúng cả 3 bậc", () => {
    expect(calculateElectricityPayment("120")).toBe("Số tiền điện cần trả: 240000 VNĐ");
  });
});
