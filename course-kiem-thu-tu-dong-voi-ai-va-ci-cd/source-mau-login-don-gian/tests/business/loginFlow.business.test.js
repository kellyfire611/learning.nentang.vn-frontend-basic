import { describe, expect, test } from "vitest";
import { createLoginStore } from "../../src/loginStore.js";

describe("login flow business", () => {
  test("đi qua một lần sai rồi đăng nhập đúng", () => {
    const store = createLoginStore();

    const firstTry = store.login("student@example.com", "sai-mat-khau");
    const secondTry = store.login("student@example.com", "123456");

    expect(firstTry.message).toBe("Email hoặc mật khẩu không đúng.");
    expect(firstTry.attempts).toBe(1);
    expect(secondTry.authenticated).toBe(true);
    expect(secondTry.attempts).toBe(2);
    expect(secondTry.user?.name).toBe("Học viên");
  });

  test("có thể đọc nhanh toàn bộ trạng thái sau đăng nhập", () => {
    const store = createLoginStore();

    const state = store.login("student@example.com", "123456", true);

    expect(state).toMatchObject({
      authenticated: true,
      rememberMe: true,
      message: "Đăng nhập thành công."
    });
    expect(state.user).toEqual({
      email: "student@example.com",
      name: "Học viên"
    });
  });

  test("logout đưa app về trạng thái ban đầu", () => {
    const store = createLoginStore();

    store.login("student@example.com", "123456");
    const state = store.logout();

    expect(state).toMatchObject({
      authenticated: false,
      rememberMe: false,
      message: "Đã đăng xuất."
    });
    expect(state.user).toBeNull();
  });
});