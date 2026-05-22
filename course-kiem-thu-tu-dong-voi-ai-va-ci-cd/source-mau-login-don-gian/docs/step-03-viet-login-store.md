# Step 3 - Viết login store và tách logic ra khỏi giao diện

## Mục tiêu
- Tách logic nghiệp vụ login ra khỏi DOM để test dễ hơn.
- Biến phần khó kiểm thử nhất thành các hàm thuần hoặc gần thuần.

## File chính
- `src/loginStore.js`

## Ý tưởng thiết kế
- `normalizeText`: chuẩn hóa chuỗi đầu vào
- `normalizeEmail`: bỏ khoảng trắng, chuyển thường
- `isValidEmail`: kiểm tra định dạng email
- `createLoginStore`: quản lý state của tính năng login
- `login`: xử lý validate và đăng nhập
- `logout`: xóa trạng thái phiên đăng nhập
- `getState`: trả về ảnh chụp state để test

## State tối thiểu nên có

```js
const state = {
  attempts: 0,
  authenticated: false,
  rememberMe: false,
  message: "",
  user: null
};
```

## Dữ liệu account mẫu

```js
export const DEMO_ACCOUNT = {
  email: "student@example.com",
  password: "123456",
  name: "Học viên"
};
```

## Luật nghiệp vụ cần code
1. Submit lần nào thì `attempts` tăng lần đó
2. Email rỗng thì báo `Vui lòng nhập email.`
3. Email sai định dạng thì báo `Email không hợp lệ.`
4. Mật khẩu rỗng thì báo `Vui lòng nhập mật khẩu.`
5. Sai email hoặc mật khẩu thì báo `Email hoặc mật khẩu không đúng.`
6. Đăng nhập đúng thì set `authenticated = true`
7. Đăng xuất thì trả về trạng thái chưa đăng nhập

## Khung code quan trọng

```js
function login(emailInput, passwordInput, rememberMe = false) {
  state.attempts += 1;

  const email = normalizeEmail(emailInput);
  const password = normalizeText(passwordInput);

  if (!email) {
    return setFailure("Vui lòng nhập email.");
  }

  if (!isValidEmail(email)) {
    return setFailure("Email không hợp lệ.");
  }

  if (!password) {
    return setFailure("Vui lòng nhập mật khẩu.");
  }

  if (email !== account.email || password !== account.password) {
    return setFailure("Email hoặc mật khẩu không đúng.");
  }

  state.authenticated = true;
  state.rememberMe = Boolean(rememberMe);
  state.user = {
    email: account.email,
    name: account.name
  };
  state.message = "Đăng nhập thành công.";

  return getState();
}
```

## Vì sao bước này quan trọng
- Nếu nhét hết logic vào `main.js`, unit test sẽ khó viết hơn nhiều.
- Khi store đứng riêng, học viên có thể test validate mà không cần mở trình duyệt.

## Tự kiểm tra sau bước này
1. Đọc code và kiểm tra mỗi nhánh lỗi đều có message riêng
2. Kiểm tra `getState()` không trả trực tiếp object gốc của `user`
3. Kiểm tra `logout()` có xóa user và reset `rememberMe`

## Kết quả mong đợi
- Có một file store đủ rõ ràng để viết unit test ngay ở bước sau