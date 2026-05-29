import { describe, expect, it } from "vitest";
import { calculatePayment } from "../../src/discountCalculatorStore.js";

describe("Business test - Kịch bản nghiệp vụ tính tiền giảm giá", () => {
  it("Mã TC-BIZ-01: Cho trước bỏ trống giá gốc, Khi tính tiền, Thì yêu cầu nhập giá gốc", () => {
    expect(calculatePayment("", "10")).toBe("Vui lòng nhập giá gốc!");
  });

  it("Mã TC-BIZ-02: Cho trước giá gốc âm, Khi tính tiền, Thì báo giá gốc không hợp lệ", () => {
    expect(calculatePayment("-50000", "10")).toBe("Giá gốc phải là số lớn hơn 0!");
  });

  it("Mã TC-BIZ-03: Cho trước bỏ trống phần trăm giảm, Khi tính tiền, Thì yêu cầu nhập phần trăm giảm", () => {
    expect(calculatePayment("200000", "")).toBe("Vui lòng nhập phần trăm giảm giá!");
  });

  it("Mã TC-BIZ-04: Cho trước phần trăm giảm vượt quá 100, Khi tính tiền, Thì báo lỗi nghiệp vụ", () => {
    expect(calculatePayment("200000", "101")).toBe("Phần trăm giảm giá phải từ 0 đến 100!");
  });

  it("Mã TC-BIZ-05: Cho trước giảm giá 0 phần trăm, Khi tính tiền, Thì số tiền cần trả bằng giá gốc", () => {
    expect(calculatePayment("200000", "0")).toBe("Số tiền cần trả: 200000 VNĐ");
  });

  it("Mã TC-BIZ-06: Cho trước giảm giá 100 phần trăm, Khi tính tiền, Thì số tiền cần trả bằng 0", () => {
    expect(calculatePayment("200000", "100")).toBe("Số tiền cần trả: 0 VNĐ");
  });

  it("Mã TC-BIZ-07: Cho trước dữ liệu hợp lệ thông thường, Khi tính tiền, Thì trả đúng số tiền cuối", () => {
    expect(calculatePayment("200000", "10")).toBe("Số tiền cần trả: 180000 VNĐ");
  });

  it("Mã TC-BIZ-08: Cho trước dữ liệu thập phân, Khi tính tiền, Thì kết quả được làm tròn đúng", () => {
    expect(calculatePayment("99999.9", "10")).toBe("Số tiền cần trả: 90000 VNĐ");
  });
});
