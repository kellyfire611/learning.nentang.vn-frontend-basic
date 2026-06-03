import { describe, expect, it } from "vitest";

const API_URL = "https://jsonplaceholder.typicode.com/users";

describe("Integration test - Goi API that JSONPlaceholder", () => {
  it("TC-API-REAL-01: API users tra ve status thanh cong", async () => {
    const response = await fetch(API_URL);

    expect(response.ok).toBe(true);
    expect(response.status).toBe(200);
  });

  it("TC-API-REAL-02: API users tra ve danh sach user", async () => {
    const response = await fetch(API_URL);
    const users = await response.json();

    expect(Array.isArray(users)).toBe(true);
    expect(users.length).toBeGreaterThan(0);
  });

  it("TC-API-REAL-03: User dau tien co cac field can thiet", async () => {
    const response = await fetch(API_URL);
    const users = await response.json();

    expect(users[0]).toHaveProperty("id");
    expect(users[0]).toHaveProperty("name");
    expect(users[0]).toHaveProperty("email");
  });

  it("TC-API-REAL-04: User dau tien co email dung dang chuoi", async () => {
    const response = await fetch(API_URL);
    const users = await response.json();

    expect(typeof users[0].email).toBe("string");
    expect(users[0].email).toContain("@");
  });

  it("TC-API-REAL-05: API tra ve dung content-type JSON", async () => {
    const response = await fetch(API_URL);

    const contentType = response.headers.get("content-type");

    expect(contentType).toContain("application/json");
  });
});