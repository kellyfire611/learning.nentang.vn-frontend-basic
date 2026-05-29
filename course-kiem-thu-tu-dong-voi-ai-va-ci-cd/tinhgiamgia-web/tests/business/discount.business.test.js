import { describe, expect, it } from "vitest";
import { calculatePayment } from "../../src/discountCalculatorStore.js";

describe("Các kịch bản nghiệp vụ tính tiền giảm giá", () => {
  it("Cho trước người dùng bỏ trống giá gốc, Khi bấm tính tiền, Thì hệ thống yêu cầu nhập giá gốc", () => {
    const result = calculatePayment("", "10");

    expect(result).toBe("Vui lòng nhập giá gốc!");
  });

  it("Cho trước người dùng có giá gốc nhưng bỏ trống giảm giá, Khi bấm tính tiền, Thì hệ thống yêu cầu nhập phần trăm giảm", () => {
    const result = calculatePayment("200000", "");

    expect(result).toBe("Vui lòng nhập phần trăm giảm giá!");
  });

  it("Cho trước người dùng nhập giảm giá ngoài khoảng 0-100, Khi bấm tính tiền, Thì hệ thống báo lỗi nghiệp vụ", () => {
    const result = calculatePayment("200000", "101");

    expect(result).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("Cho trước người dùng nhập dữ liệu hợp lệ, Khi bấm tính tiền, Thì hệ thống trả về số tiền cần thanh toán", () => {
    const result = calculatePayment("200000", "10");

    expect(result).toBe("Số tiền cần trả: 180000 VNĐ");
  });
});
