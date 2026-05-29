import { describe, expect, it } from "vitest";
import {
  validatePrice,
  validateDiscountPercent,
  calculateFinalPrice,
  formatCurrencyVnd,
} from "../../src/discountCalculatorStore.js";

describe("Kiểm thử unit cho bài tính tiền giảm giá", () => {
  it("validatePrice trả lỗi khi bỏ trống giá gốc", () => {
    const result = validatePrice("");

    expect(result).toBe("Vui lòng nhập giá gốc!");
  });

  it("validatePrice trả lỗi khi giá gốc không hợp lệ", () => {
    const result = validatePrice("-1000");

    expect(result).toBe("Giá gốc phải là số lớn hơn 0!");
  });

  it("validatePrice hợp lệ khi là số lớn hơn 0", () => {
    const result = validatePrice("250000");

    expect(result).toBe("");
  });

  it("validateDiscountPercent trả lỗi khi bỏ trống phần trăm giảm", () => {
    const result = validateDiscountPercent("");

    expect(result).toBe("Vui lòng nhập phần trăm giảm giá!");
  });

  it("validateDiscountPercent trả lỗi khi phần trăm ngoài 0-100", () => {
    const result = validateDiscountPercent("120");

    expect(result).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("validateDiscountPercent hợp lệ khi trong khoảng 0-100", () => {
    const result = validateDiscountPercent("15");

    expect(result).toBe("");
  });

  it("calculateFinalPrice tính đúng số tiền cuối", () => {
    const result = calculateFinalPrice(200000, 10);

    expect(result).toBe(180000);
  });

  it("formatCurrencyVnd format đúng chuỗi tiền tệ đơn giản", () => {
    const result = formatCurrencyVnd(180000);

    expect(result).toBe("180000 VNĐ");
  });
});
