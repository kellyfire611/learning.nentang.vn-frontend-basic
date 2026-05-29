import { describe, expect, it } from "vitest";
import {
  validatePrice,
  validateDiscountPercent,
  calculateFinalPrice,
  formatCurrencyVnd,
  calculatePayment,
} from "../../src/discountCalculatorStore.js";

describe("Unit test - Bài tập tính tiền giảm giá", () => {
  it("Mã TC-UNIT-01: validatePrice trả lỗi khi bỏ trống giá gốc", () => {
    expect(validatePrice("")).toBe("Vui lòng nhập giá gốc!");
  });

  it("Mã TC-UNIT-02: validatePrice trả lỗi khi giá gốc bằng 0", () => {
    expect(validatePrice("0")).toBe("Giá gốc phải là số lớn hơn 0!");
  });

  it("Mã TC-UNIT-03: validatePrice trả lỗi khi giá gốc âm", () => {
    expect(validatePrice("-1000")).toBe("Giá gốc phải là số lớn hơn 0!");
  });

  it("Mã TC-UNIT-04: validatePrice trả lỗi khi giá gốc không phải số", () => {
    expect(validatePrice("abc")).toBe("Giá gốc phải là số lớn hơn 0!");
  });

  it("Mã TC-UNIT-05: validatePrice hợp lệ với giá gốc dương", () => {
    expect(validatePrice("250000")).toBe("");
  });

  it("Mã TC-UNIT-06: validateDiscountPercent trả lỗi khi bỏ trống", () => {
    expect(validateDiscountPercent("")).toBe("Vui lòng nhập phần trăm giảm giá!");
  });

  it("Mã TC-UNIT-07: validateDiscountPercent trả lỗi khi < 0", () => {
    expect(validateDiscountPercent("-1")).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("Mã TC-UNIT-08: validateDiscountPercent trả lỗi khi > 100", () => {
    expect(validateDiscountPercent("101")).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("Mã TC-UNIT-09: validateDiscountPercent trả lỗi khi không phải số", () => {
    expect(validateDiscountPercent("abc")).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("Mã TC-UNIT-10: validateDiscountPercent hợp lệ tại biên 0 và 100", () => {
    expect(validateDiscountPercent("0")).toBe("");
    expect(validateDiscountPercent("100")).toBe("");
  });

  it("Mã TC-UNIT-11: calculateFinalPrice tính đúng giá sau giảm", () => {
    expect(calculateFinalPrice(200000, 10)).toBe(180000);
  });

  it("Mã TC-UNIT-12: calculateFinalPrice đúng tại biên 0% và 100%", () => {
    expect(calculateFinalPrice(200000, 0)).toBe(200000);
    expect(calculateFinalPrice(200000, 100)).toBe(0);
  });

  it("Mã TC-UNIT-13: formatCurrencyVnd làm tròn trước khi gắn đơn vị", () => {
    expect(formatCurrencyVnd(180000.6)).toBe("180001 VNĐ");
  });

  it("Mã TC-UNIT-14: calculatePayment trả đúng chuỗi kết quả với dữ liệu hợp lệ", () => {
    expect(calculatePayment("200000", "10")).toBe("Số tiền cần trả: 180000 VNĐ");
  });
});
