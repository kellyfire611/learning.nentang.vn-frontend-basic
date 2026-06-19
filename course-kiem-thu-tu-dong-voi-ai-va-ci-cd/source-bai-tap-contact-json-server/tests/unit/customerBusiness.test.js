import { describe, expect, it } from "vitest";
import {
  CUSTOMER_FILTER,
  CUSTOMER_STATUS,
  createCustomerPayload,
  filterCustomers,
  removeCustomerFromList,
  searchCustomers,
  updateCustomerStatusInList,
  validateCustomerForm,
} from "../../src/customerBusiness.js";

const validForm = {
  fullName: "Nguyen Van An",
  phone: "0912345678",
  email: "an@example.com",
  course: "Kiem thu tu dong",
  note: "Quan tam lop toi",
};

const customers = [
  { id: "1", fullName: "Nguyen Van An", phone: "0912345678", email: "an@example.com", course: "Vitest", status: "new", isFavorite: true },
  { id: "2", fullName: "Tran Thi Binh", phone: "0987654321", email: "binh@example.com", course: "Playwright", status: "contacted", isFavorite: false },
  { id: "3", fullName: "Le Quoc Cuong", phone: "0901122334", email: "cuong@example.com", course: "CI/CD", status: "registered", isFavorite: false },
];

describe("customerBusiness", () => {
  it("TC-BUS-001: họ tên rỗng thì báo lỗi", () => {
    const errors = validateCustomerForm({ ...validForm, fullName: "   " });

    expect(errors.fullName).toBe("Vui lòng nhập họ tên khách hàng!");
  });

  it("TC-BUS-002: họ tên dưới 3 ký tự thì báo lỗi", () => {
    const errors = validateCustomerForm({ ...validForm, fullName: "An" });

    expect(errors.fullName).toBe("Họ tên phải có ít nhất 3 ký tự!");
  });

  it("TC-BUS-003: số điện thoại chứa chữ thì báo lỗi", () => {
    const errors = validateCustomerForm({ ...validForm, phone: "0912abc" });

    expect(errors.phone).toBe("Số điện thoại chỉ được chứa chữ số!");
  });

  it("TC-BUS-004: email không có @ thì báo lỗi", () => {
    const errors = validateCustomerForm({ ...validForm, email: "invalid-email" });

    expect(errors.email).toBe("Email phải có ký tự @!");
  });

  it("TC-BUS-005: tạo payload khách hàng mới đúng mặc định", () => {
    const payload = createCustomerPayload({ ...validForm, fullName: "  Nguyen Van An  ", phone: " 0912345678 " });

    expect(payload).toEqual({
      fullName: "Nguyen Van An",
      phone: "0912345678",
      email: "an@example.com",
      course: "Kiem thu tu dong",
      status: CUSTOMER_STATUS.NEW,
      isFavorite: false,
      note: "Quan tam lop toi",
    });
  });

  it("TC-BUS-006: lọc khách hàng theo trạng thái contacted", () => {
    const result = filterCustomers(customers, CUSTOMER_FILTER.CONTACTED);

    expect(result).toHaveLength(1);
    expect(result[0].fullName).toBe("Tran Thi Binh");
  });

  it("TC-BUS-007: tìm kiếm theo số điện thoại", () => {
    const result = searchCustomers(customers, "0901122334");

    expect(result).toHaveLength(1);
    expect(result[0].fullName).toBe("Le Quoc Cuong");
  });

  it("TC-BUS-008: cập nhật trạng thái khách hàng trong danh sách", () => {
    const result = updateCustomerStatusInList(customers, "1", CUSTOMER_STATUS.REGISTERED);

    expect(result[0].status).toBe(CUSTOMER_STATUS.REGISTERED);
    expect(customers[0].status).toBe(CUSTOMER_STATUS.NEW);
  });

  it("TC-BUS-009: xóa khách hàng khỏi danh sách", () => {
    const result = removeCustomerFromList(customers, "2");

    expect(result).toHaveLength(2);
    expect(result.some((customer) => customer.id === "2")).toBe(false);
  });
});
