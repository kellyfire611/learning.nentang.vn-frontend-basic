export const DEMO_ACCOUNT = {
  email: "student@example.com",
  password: "123456",
  name: "Học viên"
};

export function normalizeText(value) {
  return String(value ?? "").trim();
}

export function normalizeEmail(value) {
  return normalizeText(value).toLowerCase();
}

export function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function createLoginStore({ account = DEMO_ACCOUNT } = {}) {
  const state = {
    attempts: 0,
    authenticated: false,
    rememberMe: false,
    message: "",
    user: null
  };

  function getState() {
    return {
      attempts: state.attempts,
      authenticated: state.authenticated,
      rememberMe: state.rememberMe,
      message: state.message,
      user: state.user ? { ...state.user } : null
    };
  }

  function setFailure(message) {
    state.authenticated = false;
    state.rememberMe = false;
    state.user = null;
    state.message = message;
    return getState();
  }

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

  function logout() {
    state.authenticated = false;
    state.rememberMe = false;
    state.user = null;
    state.message = "Đã đăng xuất.";

    return getState();
  }

  return {
    login,
    logout,
    getState
  };
}