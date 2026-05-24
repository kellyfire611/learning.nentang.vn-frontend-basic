import { describe, expect, it } from "vitest";
import { login } from "../../src/loginStore.js";

describe("Các kịch bản nghiệp vụ đăng nhập", () => {
  it("Cho trước người dùng bỏ trống email, Khi bấm đăng nhập, Thì hệ thống yêu cầu nhập email", () => {
    const result = login("", "any-password");

    expect(result).toBe("Vui lòng nhập email!");
  });

  it("Cho trước người dùng đã nhập email nhưng bỏ trống mật khẩu, Khi bấm đăng nhập, Thì hệ thống yêu cầu nhập mật khẩu", () => {
    const result = login("admin@gmail.com", "");

    expect(result).toBe("Vui lòng nhập mật khẩu!");
  });

  it("Cho trước người dùng nhập đúng tài khoản admin, Khi bấm đăng nhập, Thì đăng nhập thành công", () => {
    const result = login("admin@gmail.com", "123456");

    expect(result).toBe("Đăng nhập thành công!");
  });

  it("Cho trước người dùng nhập sai thông tin, Khi bấm đăng nhập, Thì đăng nhập thất bại", () => {
    const result = login("admin@gmail.com", "wrong-password");

    expect(result).toBe("Đăng nhập thất bại!");
  });
});