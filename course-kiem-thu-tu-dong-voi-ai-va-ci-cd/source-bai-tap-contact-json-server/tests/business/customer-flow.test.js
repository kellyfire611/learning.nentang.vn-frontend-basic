import { describe, expect, it } from "vitest";
import {
  CUSTOMER_STATUS,
  createCustomerPayload,
  filterCustomers,
  getFirstValidationMessage,
  hasValidationErrors,
  searchCustomers,
  validateCustomerForm,
} from "../../src/customerBusiness.js";

describe("customer business flow", () => {
  it("Given customers, When filter registered, Then only registered customers remain", () => {
    const customers = [
      { id: "1", fullName: "Khach Moi", status: "new" },
      { id: "2", fullName: "Da Tu Van", status: "contacted" },
      { id: "3", fullName: "Da Dang Ky", status: "registered" },
    ];

    const result = filterCustomers(customers, CUSTOMER_STATUS.REGISTERED);

    expect(result).toEqual([{ id: "3", fullName: "Da Dang Ky", status: "registered" }]);
  });

  it("Given invalid phone, When validate form, Then returns phone error", () => {
    const formData = {
      fullName: "Nguyen Van An",
      phone: "09abc",
      email: "an@example.com",
      course: "Playwright",
      note: "",
    };

    const errors = validateCustomerForm(formData);

    expect(hasValidationErrors(errors)).toBe(true);
    expect(getFirstValidationMessage(errors)).toBe("Số điện thoại chỉ được chứa chữ số!");
  });

  it("Given valid form, When create payload, Then trim data and use new status", () => {
    const payload = createCustomerPayload({
      fullName: "  Nguyen Van An  ",
      phone: " 0912345678 ",
      email: " an@example.com ",
      course: " Playwright ",
      note: " Goi sau 18h ",
    });

    expect(payload.fullName).toBe("Nguyen Van An");
    expect(payload.status).toBe(CUSTOMER_STATUS.NEW);
    expect(payload.isFavorite).toBe(false);
  });

  it("Given customers, When search by course, Then returns matched customer", () => {
    const customers = [
      { fullName: "Nguyen Van An", phone: "0912345678", email: "an@example.com", course: "Vitest" },
      { fullName: "Tran Thi Binh", phone: "0987654321", email: "binh@example.com", course: "Playwright" },
    ];

    const result = searchCustomers(customers, "playwright");

    expect(result).toHaveLength(1);
    expect(result[0].fullName).toBe("Tran Thi Binh");
  });
});
