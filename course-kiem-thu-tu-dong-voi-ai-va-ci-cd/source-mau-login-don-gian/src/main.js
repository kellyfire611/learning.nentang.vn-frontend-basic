import { createLoginStore } from "./loginStore.js";

const store = createLoginStore();

const elements = {
  form: document.querySelector("#login-form"),
  email: document.querySelector("#email-input"),
  password: document.querySelector("#password-input"),
  remember: document.querySelector("#remember-input"),
  message: document.querySelector("#message"),
  attempts: document.querySelector('[data-testid="attempts-count"]'),
  authStatus: document.querySelector('[data-testid="auth-status"]'),
  sessionCard: document.querySelector('[data-testid="session-panel"]'),
  welcomeTitle: document.querySelector("#welcome-title"),
  sessionSummary: document.querySelector("#session-summary"),
  logoutButton: document.querySelector("#logout-button")
};

function render() {
  const state = store.getState();

  elements.message.textContent = state.message;
  elements.attempts.textContent = String(state.attempts);
  elements.authStatus.textContent = state.authenticated ? "Đã đăng nhập" : "Chưa đăng nhập";
  elements.sessionCard.hidden = !state.authenticated;

  if (state.authenticated && state.user) {
    elements.welcomeTitle.textContent = `Xin chào, ${state.user.name}`;
    elements.sessionSummary.textContent = `Email: ${state.user.email} · Ghi nhớ: ${state.rememberMe ? "Có" : "Không"}`;
  } else {
    elements.welcomeTitle.textContent = "Xin chào";
    elements.sessionSummary.textContent = "";
  }
}

function handleLogin(event) {
  event.preventDefault();
  store.login(elements.email.value, elements.password.value, elements.remember.checked);
  render();
}

elements.form.addEventListener("submit", handleLogin);
elements.logoutButton.addEventListener("click", () => {
  store.logout();
  render();
});

render();