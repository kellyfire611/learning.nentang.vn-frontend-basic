const VALID_EMAIL = "admin@gmail.com";
const VALID_PASSWORD = "123456";

export function validateEmail(emailInput) {
  if (!emailInput) {
    return "Vui lòng nhập email!";
  }

  return "";
}

export function validatePassword(passwordInput) {
  if (!passwordInput) {
    return "Vui lòng nhập mật khẩu!";
  }

  return "";
}

export function checkAccount(emailInput, passwordInput) {
  return emailInput === VALID_EMAIL && passwordInput === VALID_PASSWORD;
}

export function login(emailInput, passwordInput) {
  // 1. Kiểm tra email
  const emailError = validateEmail(emailInput);
  if (emailError) {
    return emailError;
  }

  // 2. Kiểm tra mật khẩu
  const passwordError = validatePassword(passwordInput);
  if (passwordError) {
    return passwordError;
  }

  // 3. Kiểm tra logic/nghiệp vụ:
  // Tài khoản có đúng không?
  // Giả sử: admin@gmail.com và 123456 là đúng
  const isValidAccount = checkAccount(emailInput, passwordInput);
  if (isValidAccount) {
    return "Đăng nhập thành công!";
  } else {
    return "Đăng nhập thất bại!";
  }
}

// Giữ tương thích với trang HTML đang gọi login(...) từ window.
if (typeof window !== "undefined") {
  window.login = login;
}
