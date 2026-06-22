import {
  CUSTOMER_STATUS,
  CUSTOMER_STATUS_LABEL,
  createCustomerPayload,
  createUpdateCustomerPayload,
  filterCustomers,
  getVisibleCustomers,
  removeCustomerFromList,
  searchCustomers,
  updateCustomerInList,
  updateCustomerStatusInList,
  validateCustomerForm,
} from './customerBusiness.js';

import {
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerStatus,
  updateCustomer,
} from './customerApiStore.js';

const elements = {
  loading: document.querySelector('[data-testid="loading"]'),
  message: document.querySelector('[data-testid="message"]'),
  customerList: document.querySelector('[data-testid="customerList"]'),
  customerCount: document.querySelector('[data-testid="customerCount"]'),
  form: document.querySelector('[data-testid="customerForm"]'),
  formTitle: document.querySelector('[data-testid="formTitle"]'),
  submitButton: document.querySelector('[data-testid="submitButton"]'),
  cancelEditButton: document.querySelector('[data-testid="cancelEditButton"]'),
  searchInput: document.querySelector('[data-testid="searchInput"]'),
  filterButtons: document.querySelectorAll('[data-filter]'),
  fullNameInput: document.querySelector('[data-testid="fullNameInput"]'),
  phoneInput: document.querySelector('[data-testid="phoneInput"]'),
  emailInput: document.querySelector('[data-testid="emailInput"]'),
  courseInput: document.querySelector('[data-testid="courseInput"]'),
  noteInput: document.querySelector('[data-testid="noteInput"]'),
  statusInput: document.querySelector('[data-testid="statusInput"]'),
  isFavoriteInput: document.querySelector('[data-testid="isFavoriteInput"]'),
  newCount: document.querySelector('[data-testid="newCount"]'),
  contactedCount: document.querySelector('[data-testid="contactedCount"]'),
  registeredCount: document.querySelector('[data-testid="registeredCount"]'),
};

let customers = [];
let currentFilter = 'all';
let currentKeyword = '';
let editingCustomerId = null;

function setLoading(isLoading) {
  elements.loading.hidden = !isLoading;
}

function showMessage(message, type = 'info') {
  elements.message.textContent = message;
  elements.message.dataset.type = type;
  elements.message.hidden = !message;
}

function clearFieldErrors() {
  document.querySelectorAll('[data-error-for]').forEach((element) => {
    element.textContent = '';
  });
}

function showFieldErrors(errors) {
  clearFieldErrors();

  Object.entries(errors).forEach(([fieldName, message]) => {
    const element = document.querySelector(`[data-error-for="${fieldName}"]`);
    if (element) element.textContent = message;
  });
}

function getFormData() {
  return {
    fullName: elements.fullNameInput.value,
    phone: elements.phoneInput.value,
    email: elements.emailInput.value,
    course: elements.courseInput.value,
    note: elements.noteInput.value,
    status: elements.statusInput.value,
    isFavorite: elements.isFavoriteInput.checked,
  };
}

function resetForm() {
  editingCustomerId = null;
  elements.form.reset();
  elements.statusInput.value = CUSTOMER_STATUS.NEW;
  elements.isFavoriteInput.checked = false;
  elements.formTitle.textContent = 'Thêm khách hàng mới';
  elements.submitButton.textContent = 'Thêm khách hàng';
  elements.cancelEditButton.hidden = true;
  clearFieldErrors();
}

function fillForm(customer) {
  editingCustomerId = String(customer.id);
  elements.fullNameInput.value = customer.fullName ?? '';
  elements.phoneInput.value = customer.phone ?? '';
  elements.emailInput.value = customer.email ?? '';
  elements.courseInput.value = customer.course ?? '';
  elements.noteInput.value = customer.note ?? '';
  elements.statusInput.value = customer.status ?? CUSTOMER_STATUS.NEW;
  elements.isFavoriteInput.checked = Boolean(customer.isFavorite);
  elements.formTitle.textContent = `Sửa khách hàng: ${customer.fullName}`;
  elements.submitButton.textContent = 'Lưu thay đổi';
  elements.cancelEditButton.hidden = false;
  clearFieldErrors();
  elements.fullNameInput.focus();
}

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function statusClass(status) {
  if (status === CUSTOMER_STATUS.CONTACTED) return 'badge badge-contacted';
  if (status === CUSTOMER_STATUS.REGISTERED) return 'badge badge-registered';
  return 'badge badge-new';
}

function renderSummary() {
  elements.newCount.textContent = customers.filter((customer) => customer.status === CUSTOMER_STATUS.NEW).length;
  elements.contactedCount.textContent = customers.filter((customer) => customer.status === CUSTOMER_STATUS.CONTACTED).length;
  elements.registeredCount.textContent = customers.filter((customer) => customer.status === CUSTOMER_STATUS.REGISTERED).length;
}

function renderCustomers() {
  const filteredCustomers = filterCustomers(customers, currentFilter);
  const visibleCustomers = searchCustomers(filteredCustomers, currentKeyword);

  elements.customerCount.textContent = visibleCustomers.length;
  renderSummary();

  if (visibleCustomers.length === 0) {
    elements.customerList.innerHTML = `
      <tr>
        <td colspan="8" class="empty-state" data-testid="emptyState">
          Không có khách hàng phù hợp.
        </td>
      </tr>
    `;
    return;
  }

  elements.customerList.innerHTML = visibleCustomers
    .map((customer) => {
      const id = escapeHtml(customer.id);
      const status = customer.status ?? CUSTOMER_STATUS.NEW;

      return `
        <tr data-testid="customerRow" data-id="${id}">
          <td>
            <strong data-testid="customerName">${escapeHtml(customer.fullName)}</strong>
            ${customer.isFavorite ? '<span class="favorite" title="Yêu thích">★</span>' : ''}
          </td>
          <td>${escapeHtml(customer.phone)}</td>
          <td>${escapeHtml(customer.email || '—')}</td>
          <td>${escapeHtml(customer.course)}</td>
          <td><span class="${statusClass(status)}" data-testid="customerStatus">${CUSTOMER_STATUS_LABEL[status] ?? status}</span></td>
          <td>${escapeHtml(customer.note || '—')}</td>
          <td class="action-cell">
            <button class="button button-small" data-action="contacted" data-id="${id}" data-testid="markContacted-${id}">Đã tư vấn</button>
            <button class="button button-small button-success" data-action="registered" data-id="${id}" data-testid="markRegistered-${id}">Đã đăng ký</button>
            <button class="button button-small button-secondary" data-action="edit" data-id="${id}" data-testid="editCustomer-${id}">Sửa</button>
            <button class="button button-small button-danger" data-action="delete" data-id="${id}" data-testid="deleteCustomer-${id}">Xóa</button>
          </td>
        </tr>
      `;
    })
    .join('');
}

async function loadCustomers() {
  setLoading(true);
  showMessage('');

  try {
    customers = await fetchCustomers();
    renderCustomers();
  } catch (error) {
    showMessage('Không thể tải danh sách khách hàng. Vui lòng thử lại sau.', 'error');
    elements.customerList.innerHTML = `
      <tr>
        <td colspan="8" class="empty-state">API lỗi: ${escapeHtml(error.message)}</td>
      </tr>
    `;
  } finally {
    setLoading(false);
  }
}

async function handleSubmit(event) {
  event.preventDefault();
  showMessage('');

  const formData = getFormData();
  const validation = validateCustomerForm(formData);

  if (!validation.isValid) {
    showFieldErrors(validation.errors);
    showMessage('Vui lòng kiểm tra lại thông tin nhập.', 'error');
    return;
  }

  clearFieldErrors();

  try {
    setLoading(true);

    if (editingCustomerId) {
      const payload = createUpdateCustomerPayload(formData, editingCustomerId);
      const updatedCustomer = await updateCustomer(editingCustomerId, payload);
      customers = updateCustomerInList(customers, updatedCustomer);
      showMessage('Đã cập nhật thông tin khách hàng.', 'success');
    } else {
      const payload = createCustomerPayload(formData);
      const createdCustomer = await createCustomer(payload);
      customers = [createdCustomer, ...customers];
      showMessage('Đã thêm khách hàng mới.', 'success');
    }

    resetForm();
    renderCustomers();
  } catch (error) {
    showMessage(`Không thể lưu khách hàng: ${error.message}`, 'error');
  } finally {
    setLoading(false);
  }
}

async function handleCustomerAction(event) {
  const button = event.target.closest('button[data-action]');
  if (!button) return;

  const { action, id } = button.dataset;
  const customer = customers.find((item) => String(item.id) === String(id));
  if (!customer) return;

  try {
    if (action === 'contacted') {
      await patchCustomerStatus(id, CUSTOMER_STATUS.CONTACTED);
      customers = updateCustomerStatusInList(customers, id, CUSTOMER_STATUS.CONTACTED);
      showMessage('Đã cập nhật trạng thái: Đã tư vấn.', 'success');
    }

    if (action === 'registered') {
      await patchCustomerStatus(id, CUSTOMER_STATUS.REGISTERED);
      customers = updateCustomerStatusInList(customers, id, CUSTOMER_STATUS.REGISTERED);
      showMessage('Đã cập nhật trạng thái: Đã đăng ký.', 'success');
    }

    if (action === 'edit') {
      fillForm(customer);
      return;
    }

    if (action === 'delete') {
      const accepted = confirm(`Bạn có chắc chắn muốn xóa khách hàng "${customer.fullName}" không?`);
      if (!accepted) return;

      await deleteCustomer(id);
      customers = removeCustomerFromList(customers, id);
      showMessage('Đã xóa khách hàng.', 'success');
    }

    renderCustomers();
  } catch (error) {
    showMessage(`Thao tác thất bại: ${error.message}`, 'error');
  }
}

function handleFilterClick(event) {
  const button = event.target.closest('[data-filter]');
  if (!button) return;

  currentFilter = button.dataset.filter;

  elements.filterButtons.forEach((item) => {
    item.classList.toggle('active', item.dataset.filter === currentFilter);
  });

  renderCustomers();
}

function handleSearchInput(event) {
  currentKeyword = event.target.value;
  renderCustomers();
}

function initApp() {
  elements.form.addEventListener('submit', handleSubmit);
  elements.cancelEditButton.addEventListener('click', resetForm);
  elements.customerList.addEventListener('click', handleCustomerAction);
  elements.searchInput.addEventListener('input', handleSearchInput);
  document.querySelector('[data-testid="filterGroup"]').addEventListener('click', handleFilterClick);

  resetForm();
  loadCustomers();
}

initApp();

export {
  getVisibleCustomers,
};
