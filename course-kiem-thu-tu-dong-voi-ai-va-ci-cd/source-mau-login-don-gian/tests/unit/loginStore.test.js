import { describe, expect, test } from "vitest";
import { createLoginStore, isValidEmail, normalizeEmail, normalizeText } from "../../src/loginStore.js";

describe("loginStore unit", () => {
  test("normalizeText loại bỏ khoảng trắng dư thừa", () => {
    expect(normalizeText("  hello   world  ")).toBe("hello   world");
  });

  test("normalizeEmail chuyển về chữ thường và bỏ khoảng trắng", () => {
    expect(normalizeEmail("  Student@Example.com  ")).toBe("student@example.com");
  });

  test.each([
    ["student@example.com", true],
    ["student.example.com", false],
    ["student@", false],
    ["", false]
  ])("isValidEmail(%s) trả về %s", (value, expected) => {
    expect(isValidEmail(value)).toBe(expected);
  });

  test("đăng nhập thành công với thông tin mẫu", () => {
    const store = createLoginStore();

    const state = store.login("student@example.com", "123456", true);

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(true);
    expect(state.rememberMe).toBe(true);
    expect(state.message).toBe("Đăng nhập thành công.");
    expect(state.user).toEqual({ email: "student@example.com", name: "Học viên" });
  });

  test("báo lỗi khi thiếu email", () => {
    const store = createLoginStore();

    const state = store.login("", "123456");

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(false);
    expect(state.message).toBe("Vui lòng nhập email.");
    expect(state.user).toBeNull();
  });

  test("báo lỗi khi email không đúng định dạng", () => {
    const store = createLoginStore();

    const state = store.login("student.example.com", "123456");

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(false);
    expect(state.message).toBe("Email không hợp lệ.");
  });

  test("báo lỗi khi mật khẩu rỗng", () => {
    const store = createLoginStore();

    const state = store.login("student@example.com", "");

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(false);
    expect(state.message).toBe("Vui lòng nhập mật khẩu.");
  });

  test("báo lỗi khi sai tài khoản", () => {
    const store = createLoginStore();

    const state = store.login("student@example.com", "sai-mat-khau");

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(false);
    expect(state.message).toBe("Email hoặc mật khẩu không đúng.");
  });

  test("đăng xuất xóa phiên đăng nhập", () => {
    const store = createLoginStore();

    store.login("student@example.com", "123456", true);
    const state = store.logout();

    expect(state.authenticated).toBe(false);
    expect(state.rememberMe).toBe(false);
    expect(state.user).toBeNull();
    expect(state.message).toBe("Đã đăng xuất.");
  });
});