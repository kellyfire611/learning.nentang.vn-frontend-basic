import { describe, expect, it, vi } from "vitest";
import {
  CUSTOMER_API_URL,
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerStatus,
  updateCustomer,
} from "../../src/customerApiStore.js";

function createMockResponse(data, ok = true) {
  return {
    ok,
    json: async () => data,
  };
}

describe("customerApiStore", () => {
  it("TC-API-001: fetchCustomers gọi đúng GET /customers", async () => {
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse([]));

    const result = await fetchCustomers(fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(CUSTOMER_API_URL);
    expect(result).toEqual([]);
  });

  it("TC-API-002: createCustomer gọi đúng POST và gửi JSON body", async () => {
    const payload = { fullName: "Nguyen Van An", phone: "0912345678" };
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse({ id: "10", ...payload }));

    const result = await createCustomer(payload, fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(CUSTOMER_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    expect(result.id).toBe("10");
  });

  it("TC-API-003: patchCustomerStatus gọi đúng PATCH /customers/:id", async () => {
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse({ id: "1", status: "contacted" }));

    await patchCustomerStatus("1", "contacted", fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(`${CUSTOMER_API_URL}/1`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: "contacted" }),
    });
  });

  it("TC-API-004: updateCustomer gọi đúng PUT /customers/:id", async () => {
    const payload = { fullName: "Tran Thi Binh", phone: "0987654321" };
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse({ id: "2", ...payload }));

    await updateCustomer("2", payload, fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(`${CUSTOMER_API_URL}/2`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  });

  it("TC-API-005: deleteCustomer gọi đúng DELETE /customers/:id", async () => {
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse({}));

    await deleteCustomer("3", fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(`${CUSTOMER_API_URL}/3`, {
      method: "DELETE",
    });
  });

  it("TC-API-006: API trả lỗi thì throw Error", async () => {
    const fetchFn = vi.fn().mockResolvedValue(createMockResponse({}, false));

    await expect(fetchCustomers(fetchFn)).rejects.toThrow("Không thể tải danh sách khách hàng!");
  });
});
