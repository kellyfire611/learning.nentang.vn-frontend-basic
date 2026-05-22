# Step 5 - Viết unit test

## Mục tiêu
- Kiểm tra các hàm nhỏ và từng nhánh logic của store.
- Làm quen với `describe`, `test`, `expect` trong Vitest.

## File cần viết
- `tests/unit/loginStore.test.js`

## Những gì nên test ở lớp unit
1. `normalizeText`
2. `normalizeEmail`
3. `isValidEmail`
4. `login` khi thành công
5. `login` khi thiếu email
6. `login` khi email sai định dạng
7. `login` khi thiếu mật khẩu
8. `login` khi sai tài khoản
9. `logout`

## Ví dụ code unit test

```js
import { describe, expect, test } from "vitest";
import { createLoginStore, isValidEmail, normalizeEmail, normalizeText } from "../../src/loginStore.js";

describe("loginStore unit", () => {
  test("normalizeEmail chuyển về chữ thường và bỏ khoảng trắng", () => {
    expect(normalizeEmail("  Student@Example.com  ")).toBe("student@example.com");
  });

  test("báo lỗi khi thiếu email", () => {
    const store = createLoginStore();
    const state = store.login("", "123456");

    expect(state.attempts).toBe(1);
    expect(state.authenticated).toBe(false);
    expect(state.message).toBe("Vui lòng nhập email.");
  });
});
```

## Thứ tự nên viết
1. Viết test cho hàm nhỏ trước
2. Viết test cho happy path
3. Viết test cho từng nhánh lỗi
4. Viết test cho logout

## Lệnh chạy ở bước này

```bash
npm test
```

## Khi test fail thì nhìn gì trước
1. Message expected có khớp hẳn chuỗi thực tế không
2. `attempts` có tăng đúng số lần không
3. `authenticated`, `rememberMe`, `user` có đúng state không

## Kết quả mong đợi
- Unit test cover toàn bộ validate quan trọng
- Học viên hiểu được vì sao phải test hàm nhỏ trước E2E