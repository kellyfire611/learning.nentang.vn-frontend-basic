import { afterEach, describe, expect, it } from "vitest";
import {
  CUSTOMER_API_URL,
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerStatus,
  updateCustomer,
} from "../../src/customerApiStore.js";

const createdIds = [];

function createTestCustomer(overrides = {}) {
  return {
    fullName: `Integration Test ${Date.now()}`,
    phone: "0912345678",
    email: "integration@example.com",
    course: "JSON Server Testing",
    status: "new",
    isFavorite: false,
    note: "Du lieu tu integration test",
    ...overrides,
  };
}

afterEach(async () => {
  while (createdIds.length > 0) {
    const id = createdIds.pop();
    await fetch(`${CUSTOMER_API_URL}/${id}`, { method: "DELETE" }).catch(() => null);
  }
});

describe("customer API integration", () => {
  it("TC-INT-001: GET /customers returns an array", async () => {
    const customers = await fetchCustomers();

    expect(Array.isArray(customers)).toBe(true);
  });

  it("TC-INT-002: POST /customers creates a customer", async () => {
    const createdCustomer = await createCustomer(createTestCustomer());
    createdIds.push(createdCustomer.id);

    expect(createdCustomer.id).toBeDefined();
    expect(createdCustomer.fullName).toContain("Integration Test");
  });

  it("TC-INT-003: PATCH /customers/:id updates status", async () => {
    const createdCustomer = await createCustomer(createTestCustomer());
    createdIds.push(createdCustomer.id);

    const updatedCustomer = await patchCustomerStatus(createdCustomer.id, "contacted");

    expect(updatedCustomer.status).toBe("contacted");
  });

  it("TC-INT-004: PUT /customers/:id updates full customer", async () => {
    const createdCustomer = await createCustomer(createTestCustomer());
    createdIds.push(createdCustomer.id);

    const updatedCustomer = await updateCustomer(createdCustomer.id, {
      fullName: "Integration Updated",
      phone: "0987654321",
      email: "updated@example.com",
      course: "Vitest",
      status: "registered",
      isFavorite: true,
      note: "Da cap nhat",
    });

    expect(updatedCustomer.fullName).toBe("Integration Updated");
    expect(updatedCustomer.isFavorite).toBe(true);
  });

  it("TC-INT-005: DELETE /customers/:id removes customer", async () => {
    const createdCustomer = await createCustomer(createTestCustomer());

    await deleteCustomer(createdCustomer.id);

    const response = await fetch(`${CUSTOMER_API_URL}/${createdCustomer.id}`);
    expect(response.status).toBe(404);
  });
});
