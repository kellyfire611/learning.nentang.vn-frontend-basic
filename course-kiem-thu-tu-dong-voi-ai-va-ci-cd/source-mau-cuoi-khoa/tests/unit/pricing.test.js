import { describe, expect, it } from "vitest";
import {
  calculateShipping,
  calculateSummary,
  formatCurrency,
  getCouponDiscount,
  normalizeCoupon,
  validateQuantity
} from "../../src/cart/pricing.js";

describe("pricing helpers", () => {
  it("formatCurrency hien thi dung dinh dang tien te", () => {
    expect(formatCurrency(123456)).toBe("123.456 đ");
  });

  it("normalize coupon ve chu hoa va bo khoang trang", () => {
    expect(normalizeCoupon("  save10 ")).toBe("SAVE10");
  });

  it("validateQuantity chap nhan so hop le", () => {
    expect(validateQuantity(3)).toBe(3);
  });

  it("validateQuantity throw voi so luong ngoai khoang", () => {
    expect(() => validateQuantity(0)).toThrow(/1-10/);
    expect(() => validateQuantity(11)).toThrow(/1-10/);
  });

  it("SAVE10 chi hop le tu 500000", () => {
    expect(getCouponDiscount(400000, 1, "SAVE10")).toEqual({
      appliedCoupon: "",
      discount: 0,
      note: "Ma SAVE10 chi ap dung tu 500.000 đ."
    });
    expect(getCouponDiscount(500000, 1, "SAVE10").discount).toBe(50000);
  });

  it("FREESHIP ghi de phi ship", () => {
    expect(calculateShipping(200000, "FREESHIP")).toBe(0);
    expect(getCouponDiscount(200000, 1, "FREESHIP")).toEqual({
      appliedCoupon: "FREESHIP",
      discount: 0,
      note: "Da ap dung mien phi van chuyen."
    });
  });

  it("COMBO15 khong hop le neu thieu dieu kien", () => {
    expect(getCouponDiscount(1000000, 2, "COMBO15")).toEqual({
      appliedCoupon: "",
      discount: 0,
      note: "COMBO15 can it nhat 3 san pham va tam tinh tu 1.000.000 đ."
    });
  });

  it("ma coupon sai se bi tu choi", () => {
    expect(getCouponDiscount(900000, 2, "ABC123")).toEqual({
      appliedCoupon: "",
      discount: 0,
      note: "Ma giam gia khong hop le."
    });
  });

  it("calculateSummary tra tong tien dung voi gio hang rong", () => {
    expect(calculateSummary([])).toMatchObject({
      itemCount: 0,
      subtotal: 0,
      discount: 0,
      shipping: 0,
      total: 0
    });
  });
});