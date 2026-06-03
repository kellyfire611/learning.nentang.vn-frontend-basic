import { describe, expect, it } from "vitest";
import { calculateElectricityPayment } from "../../src/electricityCalculatorStore.js";

describe("Business test - Kich ban nghiep vu tinh tien dien", () => {
  it("TC-BIZ-01: Cho truoc bo trong so kWh, Khi tinh tien dien, Thi yeu cau nhap so kWh", () => {
    expect(calculateElectricityPayment("")).toBe("Vui long nhap so kWh dien!");
  });

  it("TC-BIZ-02: Cho truoc so kWh khong phai so, Khi tinh tien dien, Thi bao du lieu khong hop le", () => {
    expect(calculateElectricityPayment("abc")).toBe("So kWh dien phai la so hop le!");
  });

  it("TC-BIZ-03: Cho truoc so kWh am, Khi tinh tien dien, Thi bao so kWh khong duoc am", () => {
    expect(calculateElectricityPayment("-5")).toBe("So kWh dien khong duoc am!");
  });

  it("TC-BIZ-04: Cho truoc 0 kWh, Khi tinh tien dien, Thi tien dien bang 0", () => {
    expect(calculateElectricityPayment("0")).toBe("So tien dien can tra: 0 VND");
  });

  it("TC-BIZ-05: Cho truoc 30 kWh, Khi tinh tien dien, Thi tinh theo bac 1", () => {
    expect(calculateElectricityPayment("30")).toBe("So tien dien can tra: 54000 VND");
  });

  it("TC-BIZ-06: Cho truoc 50 kWh, Khi tinh tien dien, Thi tinh dung tai bien bac 1", () => {
    expect(calculateElectricityPayment("50")).toBe("So tien dien can tra: 90000 VND");
  });

  it("TC-BIZ-07: Cho truoc 80 kWh, Khi tinh tien dien, Thi tinh dung bac 1 va bac 2", () => {
    expect(calculateElectricityPayment("80")).toBe("So tien dien can tra: 150000 VND");
  });

  it("TC-BIZ-08: Cho truoc 100 kWh, Khi tinh tien dien, Thi tinh dung tai bien bac 2", () => {
    expect(calculateElectricityPayment("100")).toBe("So tien dien can tra: 190000 VND");
  });

  it("TC-BIZ-09: Cho truoc 120 kWh, Khi tinh tien dien, Thi tinh dung ca 3 bac", () => {
    expect(calculateElectricityPayment("120")).toBe("So tien dien can tra: 240000 VND");
  });
});
