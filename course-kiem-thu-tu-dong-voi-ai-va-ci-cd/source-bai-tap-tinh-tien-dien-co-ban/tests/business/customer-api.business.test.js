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

describe("Business test - Customer API", () => {
  it("TC-API-BIZ-01: Cho truoc API tra ve danh sach khach hang, Khi tai du lieu, Thi he thong nhan duoc danh sach hop le", async () => {
    const fetchFn = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => mockCustomers,
    });

    const customers = await fetchCustomers(fetchFn);

    expect(validateCustomers(customers)).toBe(true);
  });

  it("TC-API-BIZ-02: Cho truoc API bi loi, Khi tai du lieu, Thi he thong tra ve loi phu hop", async () => {
    const fetchFn = vi.fn().mockResolvedValue({ ok: false });

    await expect(fetchCustomers(fetchFn)).rejects.toThrow(
      "Khong the tai danh sach khach hang!"
    );
  });

  it('TC-API-BIZ-03: Cho truoc danh sach khach hang, Khi format du lieu, Thi hien thi dung dang "id. name - email"', () => {
    expect(formatCustomerList(mockCustomers)).toEqual([
      "1. Leanne Graham - Sincere@april.biz",
      "2. Ervin Howell - Shanna@melissa.tv",
    ]);
  });
});
