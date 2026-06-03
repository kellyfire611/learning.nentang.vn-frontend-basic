import { describe, expect, it, vi } from "vitest";
import {
  fetchCustomers,
  validateCustomers,
  formatCustomerList,
} from "../../src/customerApiStore.js";

const mockCustomers = [
  { id: 1, name: "Leanne Graham", email: "Sincere@april.biz" },
  { id: 2, name: "Ervin Howell", email: "Shanna@melissa.tv" },
];

describe("Unit test - Customer API", () => {
  it("TC-API-UNIT-01: fetchCustomers goi dung URL API", async () => {
    const fetchFn = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => mockCustomers,
    });

    await fetchCustomers(fetchFn);

    expect(fetchFn).toHaveBeenCalledWith("https://jsonplaceholder.typicode.com/users");
  });

  it("TC-API-UNIT-02: fetchCustomers tra ve danh sach customers khi response ok", async () => {
    const fetchFn = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => mockCustomers,
    });

    await expect(fetchCustomers(fetchFn)).resolves.toEqual(mockCustomers);
  });

  it("TC-API-UNIT-03: fetchCustomers throw loi khi response khong ok", async () => {
    const fetchFn = vi.fn().mockResolvedValue({ ok: false });

    await expect(fetchCustomers(fetchFn)).rejects.toThrow(
      "Khong the tai danh sach khach hang!"
    );
  });

  it("TC-API-UNIT-04: validateCustomers tra false neu du lieu khong phai array", () => {
    expect(validateCustomers(null)).toBe(false);
  });

  it("TC-API-UNIT-05: validateCustomers tra false neu array rong", () => {
    expect(validateCustomers([])).toBe(false);
  });

  it("TC-API-UNIT-06: validateCustomers tra true neu du lieu hop le", () => {
    expect(validateCustomers(mockCustomers)).toBe(true);
  });

  it("TC-API-UNIT-07: formatCustomerList format dung danh sach customers", () => {
    expect(formatCustomerList(mockCustomers)).toEqual([
      "1. Leanne Graham - Sincere@april.biz",
      "2. Ervin Howell - Shanna@melissa.tv",
    ]);
  });
});
