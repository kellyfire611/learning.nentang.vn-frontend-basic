import { describe, expect, it } from "vitest";
import {
  validateEmail,
  validatePassword,
  checkAccount,
} from "../../src/loginStore.js";

describe("Kiểm thử từng hàm nhỏ của chức năng đăng nhập", () => {
  it("hàm validateEmail trả về lỗi khi email bị bỏ trống", () => {
    const result = validateEmail("");

    expect(result).toBe("Vui lòng nhập email!");
  });

  it("hàm validateEmail không trả về lỗi khi email có dữ liệu", () => {
    const result = validateEmail("admin@gmail.com");

    expect(result).toBe("");
  });

  it("hàm validatePassword trả về lỗi khi mật khẩu bị bỏ trống", () => {
    const result = validatePassword("");

    expect(result).toBe("Vui lòng nhập mật khẩu!");
  });

  it("hàm validatePassword không trả về lỗi khi mật khẩu có dữ liệu", () => {
    const result = validatePassword("123456");

    expect(result).toBe("");
  });

  it("hàm checkAccount trả về true khi tài khoản hợp lệ", () => {
    const result = checkAccount("admin@gmail.com", "123456");

    expect(result).toBe(true);
  });

  it("hàm checkAccount trả về false khi tài khoản không hợp lệ", () => {
    const result = checkAccount("user@gmail.com", "wrong-password");

    expect(result).toBe(false);
  });
});
