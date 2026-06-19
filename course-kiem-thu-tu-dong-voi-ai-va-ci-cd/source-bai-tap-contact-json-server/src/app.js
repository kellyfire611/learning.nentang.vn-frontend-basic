import {
  CUSTOMER_FILTER,
  CUSTOMER_STATUS,
  CUSTOMER_STATUS_LABEL,
  countCustomersByStatus,
  createCustomerPayload,
  createCustomerUpdatePayload,
  filterCustomers,
  findCustomerById,
  getFirstValidationMessage,
  hasValidationErrors,
  removeCustomerFromList,
  searchCustomers,
  toggleCustomerFavoriteInList,
  updateCustomerInList,
  updateCustomerStatusInList,
  validateCustomerForm,
} from "./customerBusiness.js";
import {
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerFavorite,
  patchCustomerStatus,
  updateCustomer,
} from "./customerApiStore.js";

let customers = [];
let currentFilter = CUSTOMER_FILTER.ALL;
let currentSearchKeyword = "";
let editingCustomerId = null;

const customerForm = document.querySelector("#customer-form");
const formTitle = document.querySelector("#form-title");
const fullNameInput = document.querySelector("#customer-full-name-input");
const phoneInput = document.querySelector("#customer-phone-input");
const emailInput = document.querySelector("#customer-email-input");
const courseInput = document.querySelector("#customer-course-input");
const noteInput = document.querySelector("#customer-note-input");
const statusSelect = document.querySelector("#customer-status-select");
const favoriteCheckbox = document.querySelector("#customer-favorite-checkbox");
const submitButton = document.querySelector("#submit-customer-button");
const cancelEditButton = document.querySelector("#cancel-edit-button");
const formMessage = document.querySelector("#form-message");
const apiMessage = document.querySelector("#api-message");
const loadingMessage = document.querySelector("#loading-message");
const customerList = document.querySelector("#customer-list");
const emptyMessage = document.querySelector("#empty-message");
const searchInput = document.querySelector("#customer-search-input");
const filterButtons = document.querySelectorAll("[data-filter]");
const totalCount = document.querySelector("#summary-total");
const newCount = document.querySelector("#summary-new");
const contactedCount = document.querySelector("#summary-contacted");
const registeredCount = document.querySelector("#summary-registered");
const favoriteCount = document.querySelector("#summary-favorite");

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function showMessage(element, message, type = "") {
  element.textContent = message;
  element.className = `message ${type}`.trim();
}

function clearMessage(element) {
  showMessage(element, "");
}

function getFormData() {
  return {
    fullName: fullNameInput.value,
    phone: phoneInput.value,
    email: emailInput.value,
    course: courseInput.value,
    note: noteInput.value,
    status: statusSelect.value,
    isFavorite: favoriteCheckbox.checked,
  };
}

function resetForm() {
  customerForm.reset();
  editingCustomerId = null;
  formTitle.textContent = "Thêm khách hàng mới";
  submitButton.textContent = "Thêm khách hàng";
  statusSelect.value = CUSTOMER_STATUS.NEW;
  favoriteCheckbox.checked = false;
  statusSelect.disabled = true;
  favoriteCheckbox.disabled = true;
  cancelEditButton.hidden = true;
  clearMessage(formMessage);
}

function setEditMode(customer) {
  editingCustomerId = customer.id;
  formTitle.textContent = "Sửa thông tin khách hàng";
  submitButton.textContent = "Lưu thay đổi";
  cancelEditButton.hidden = false;
  statusSelect.disabled = false;
  favoriteCheckbox.disabled = false;

  fullNameInput.value = customer.fullName;
  phoneInput.value = customer.phone;
  emailInput.value = customer.email;
  courseInput.value = customer.course;
  noteInput.value = customer.note || "";
  statusSelect.value = customer.status || CUSTOMER_STATUS.NEW;
  favoriteCheckbox.checked = customer.isFavorite === true;
  fullNameInput.focus();
}

function updateSummary() {
  const summary = countCustomersByStatus(customers);
  totalCount.textContent = summary.total;
  newCount.textContent = summary.new;
  contactedCount.textContent = summary.contacted;
  registeredCount.textContent = summary.registered;
  favoriteCount.textContent = summary.favorite;
}

function getVisibleCustomers() {
  const searchedCustomers = searchCustomers(customers, currentSearchKeyword);
  return filterCustomers(searchedCustomers, currentFilter);
}

function renderFilterButtons() {
  filterButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.filter === currentFilter);
  });
}

function renderCustomers() {
  updateSummary();
  renderFilterButtons();

  const visibleCustomers = getVisibleCustomers();
  customerList.innerHTML = "";
  emptyMessage.hidden = visibleCustomers.length > 0;

  visibleCustomers.forEach((customer) => {
    const item = document.createElement("article");
    item.className = "customer-card";
    item.dataset.customerId = customer.id;
    item.innerHTML = `
      <div class="customer-main">
        <div>
          <h3>${escapeHtml(customer.fullName)}</h3>
          <p class="customer-course">${escapeHtml(customer.course)}</p>
        </div>
        <span class="status-badge status-${escapeHtml(customer.status)}">${CUSTOMER_STATUS_LABEL[customer.status] || "Không rõ"}</span>
      </div>
      <div class="customer-info">
        <span>Điện thoại: <strong>${escapeHtml(customer.phone)}</strong></span>
        <span>Email: <strong>${escapeHtml(customer.email || "Chưa có")}</strong></span>
        <span>Yêu thích: <strong>${customer.isFavorite ? "Có" : "Không"}</strong></span>
      </div>
      <p class="customer-note">${escapeHtml(customer.note || "Không có ghi chú")}</p>
      <div class="card-actions">
        <button type="button" data-action="favorite">${customer.isFavorite ? "Bỏ yêu thích" : "Yêu thích"}</button>
        <button type="button" data-action="contacted">Đã tư vấn</button>
        <button type="button" data-action="registered">Đã đăng ký</button>
        <button type="button" data-action="edit">Sửa</button>
        <button type="button" data-action="delete" class="danger">Xóa</button>
      </div>
    `;
    customerList.appendChild(item);
  });
}

async function loadCustomers() {
  loadingMessage.textContent = "Đang tải danh sách khách hàng...";
  clearMessage(apiMessage);

  try {
    customers = await fetchCustomers();
    renderCustomers();
    showMessage(apiMessage, "Tải danh sách khách hàng thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, error.message || "Không thể tải danh sách khách hàng!", "error");
  } finally {
    loadingMessage.textContent = "";
  }
}

async function handleCreateCustomer() {
  const formData = getFormData();
  const errors = validateCustomerForm(formData);

  if (hasValidationErrors(errors)) {
    showMessage(formMessage, getFirstValidationMessage(errors), "error");
    return;
  }

  const createdCustomer = await createCustomer(createCustomerPayload(formData));
  customers = [...customers, createdCustomer];
  resetForm();
  renderCustomers();
  showMessage(apiMessage, "Thêm khách hàng thành công!", "success");
}

async function handleUpdateCustomer() {
  const formData = getFormData();
  const errors = validateCustomerForm(formData);

  if (hasValidationErrors(errors)) {
    showMessage(formMessage, getFirstValidationMessage(errors), "error");
    return;
  }

  const updatedCustomer = await updateCustomer(editingCustomerId, createCustomerUpdatePayload(formData));
  customers = updateCustomerInList(customers, updatedCustomer);
  resetForm();
  renderCustomers();
  showMessage(apiMessage, "Cập nhật khách hàng thành công!", "success");
}

async function handleSubmitCustomer(event) {
  event.preventDefault();
  clearMessage(formMessage);
  clearMessage(apiMessage);

  try {
    if (editingCustomerId) {
      await handleUpdateCustomer();
    } else {
      await handleCreateCustomer();
    }
  } catch (error) {
    showMessage(apiMessage, error.message || "Không thể lưu khách hàng!", "error");
  }
}

async function handleCustomerAction(event) {
  const button = event.target.closest("button[data-action]");
  const card = event.target.closest(".customer-card");

  if (!button || !card) {
    return;
  }

  const customerId = card.dataset.customerId;
  const customer = findCustomerById(customers, customerId);

  if (!customer) {
    return;
  }

  const action = button.dataset.action;
  clearMessage(apiMessage);

  try {
    if (action === "favorite") {
      const updatedCustomer = await patchCustomerFavorite(customerId, !customer.isFavorite);
      customers = toggleCustomerFavoriteInList(customers, customerId, updatedCustomer.isFavorite);
      renderCustomers();
      showMessage(apiMessage, "Cập nhật yêu thích thành công!", "success");
      return;
    }

    if (action === "contacted") {
      const updatedCustomer = await patchCustomerStatus(customerId, CUSTOMER_STATUS.CONTACTED);
      customers = updateCustomerStatusInList(customers, customerId, updatedCustomer.status);
      renderCustomers();
      showMessage(apiMessage, "Đã chuyển sang trạng thái đã tư vấn!", "success");
      return;
    }

    if (action === "registered") {
      const updatedCustomer = await patchCustomerStatus(customerId, CUSTOMER_STATUS.REGISTERED);
      customers = updateCustomerStatusInList(customers, customerId, updatedCustomer.status);
      renderCustomers();
      showMessage(apiMessage, "Đã chuyển sang trạng thái đã đăng ký!", "success");
      return;
    }

    if (action === "edit") {
      setEditMode(customer);
      showMessage(formMessage, "Đang sửa thông tin khách hàng.", "success");
      return;
    }

    if (action === "delete") {
      const confirmed = window.confirm(`Bạn có chắc muốn xóa ${customer.fullName}?`);

      if (!confirmed) {
        return;
      }

      await deleteCustomer(customerId);
      customers = removeCustomerFromList(customers, customerId);
      renderCustomers();
      showMessage(apiMessage, "Xóa khách hàng thành công!", "success");
    }
  } catch (error) {
    showMessage(apiMessage, error.message || "Thao tác thất bại!", "error");
  }
}

function handleFilterClick(event) {
  const button = event.target.closest("[data-filter]");

  if (!button) {
    return;
  }

  currentFilter = button.dataset.filter;
  renderCustomers();
}

function handleSearchInput(event) {
  currentSearchKeyword = event.target.value;
  renderCustomers();
}

customerForm.addEventListener("submit", handleSubmitCustomer);
cancelEditButton.addEventListener("click", resetForm);
customerList.addEventListener("click", handleCustomerAction);
searchInput.addEventListener("input", handleSearchInput);
filterButtons.forEach((button) => button.addEventListener("click", handleFilterClick));

resetForm();
loadCustomers();
