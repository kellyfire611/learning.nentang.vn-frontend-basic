import {
  getEmployees,
  searchEmployees,
  validateEmployee,
  createEmployee,
  updateEmployee,
  deactivateEmployee
} from './employeeService.js';

let employees = [];

const currencyFormatter = new Intl.NumberFormat('vi-VN', {
  style: 'currency',
  currency: 'VND'
});

const form = document.querySelector('#employee-form');
const employeeIdInput = document.querySelector('#employee-id-input');
const employeeCodeInput = document.querySelector('#employee-code-input');
const employeeNameInput = document.querySelector('#employee-name-input');
const employeeDepartmentInput = document.querySelector('#employee-department-input');
const employeePositionInput = document.querySelector('#employee-position-input');
const baseSalaryInput = document.querySelector('#base-salary-input');
const salaryCoefficientInput = document.querySelector('#salary-coefficient-input');
const allowanceInput = document.querySelector('#allowance-input');
const dependentCountInput = document.querySelector('#dependent-count-input');
const employeeStatusSelect = document.querySelector('#employee-status-select');
const resetButton = document.querySelector('#reset-employee-button');
const searchInput = document.querySelector('#search-employee-input');
const filterStatusSelect = document.querySelector('#filter-status-select');
const tableBody = document.querySelector('#employee-table-body');
const messageBox = document.querySelector('#employee-message');

function formatCurrency(value) {
  return currencyFormatter.format(Number(value || 0));
}

function getStatusLabel(status) {
  return status === 'active' ? 'Đang làm việc' : 'Nghỉ việc';
}

function showMessage(message, type = 'success') {
  messageBox.textContent = message;
  messageBox.className = `message ${type}`;
}

function clearMessage() {
  messageBox.textContent = '';
  messageBox.className = 'message';
}

function getEmployeeFromForm() {
  return {
    id: employeeIdInput.value,
    employeeCode: employeeCodeInput.value,
    fullName: employeeNameInput.value,
    department: employeeDepartmentInput.value,
    position: employeePositionInput.value,
    baseSalary: Number(baseSalaryInput.value),
    salaryCoefficient: Number(salaryCoefficientInput.value),
    allowance: Number(allowanceInput.value),
    dependentCount: Number(dependentCountInput.value),
    status: employeeStatusSelect.value
  };
}

function resetForm(options = {}) {
  const { clearFeedback = true } = options;
  form.reset();
  employeeIdInput.value = '';
  baseSalaryInput.value = '2530000';
  salaryCoefficientInput.value = '2.34';
  allowanceInput.value = '0';
  dependentCountInput.value = '0';
  employeeStatusSelect.value = 'active';
  employeeCodeInput.disabled = false;

  if (clearFeedback) {
    clearMessage();
  }
}

function fillForm(employee) {
  employeeIdInput.value = employee.id;
  employeeCodeInput.value = employee.employeeCode;
  employeeNameInput.value = employee.fullName;
  employeeDepartmentInput.value = employee.department;
  employeePositionInput.value = employee.position;
  baseSalaryInput.value = employee.baseSalary;
  salaryCoefficientInput.value = employee.salaryCoefficient;
  allowanceInput.value = employee.allowance;
  dependentCountInput.value = employee.dependentCount;
  employeeStatusSelect.value = employee.status;
}

function renderEmployees(employeeList) {
  if (employeeList.length === 0) {
    tableBody.innerHTML = `
      <tr>
        <td colspan="9" class="empty-cell">Không có nhân viên phù hợp.</td>
      </tr>
    `;
    return;
  }

  tableBody.innerHTML = employeeList
    .map(
      (employee) => `
        <tr data-employee-id="${employee.id}">
          <td>${employee.employeeCode}</td>
          <td>${employee.fullName}</td>
          <td>${employee.department}</td>
          <td>${employee.position}</td>
          <td class="money">${formatCurrency(employee.baseSalary)}</td>
          <td>${employee.salaryCoefficient}</td>
          <td class="money">${formatCurrency(employee.allowance)}</td>
          <td>
            <span class="badge ${employee.status}">${getStatusLabel(employee.status)}</span>
          </td>
          <td>
            <div class="row-actions">
              <button id="edit-employee-${employee.id}" class="secondary" type="button" data-action="edit" data-id="${employee.id}">Sửa</button>
              <button id="deactivate-employee-${employee.id}" class="danger" type="button" data-action="deactivate" data-id="${employee.id}" ${employee.status === 'inactive' ? 'disabled' : ''}>Ngừng</button>
            </div>
          </td>
        </tr>
      `
    )
    .join('');
}

async function loadEmployees() {
  employees = await getEmployees();
  renderEmployees(employees);
}

async function applySearchAndFilter() {
  const keyword = searchInput.value;
  const status = filterStatusSelect.value;
  const result = await searchEmployees(keyword, status);
  renderEmployees(result);
}

async function handleSubmit(event) {
  event.preventDefault();
  clearMessage();

  try {
    const formData = getEmployeeFromForm();
    const editingId = employeeIdInput.value;
    const errors = validateEmployee(formData, employees, editingId);

    if (errors.length > 0) {
      showMessage(errors.join(' '), 'error');
      return;
    }

    if (editingId) {
      const currentEmployee = employees.find((item) => item.id === editingId);
      await updateEmployee(editingId, {
        ...currentEmployee,
        ...formData
      });
      showMessage('Cập nhật nhân viên thành công.');
    } else {
      await createEmployee(formData);
      showMessage('Thêm nhân viên thành công.');
    }

    resetForm({ clearFeedback: false });
    await loadEmployees();
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

async function handleTableClick(event) {
  const button = event.target.closest('button[data-action]');
  if (!button) return;

  const id = button.dataset.id;
  const action = button.dataset.action;
  const employee = employees.find((item) => item.id === id);

  if (!employee) return;

  if (action === 'edit') {
    fillForm(employee);
    showMessage(`Đang sửa nhân viên ${employee.fullName}.`, 'success');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return;
  }

  if (action === 'deactivate') {
    const confirmed = confirm(`Bạn có chắc muốn ngừng hoạt động ${employee.fullName}?`);
    if (!confirmed) return;

    try {
      await deactivateEmployee(id);
      showMessage('Đã chuyển nhân viên sang trạng thái nghỉ việc.');
      await loadEmployees();
    } catch (error) {
      showMessage(error.message, 'error');
    }
  }
}

form.addEventListener('submit', handleSubmit);
resetButton.addEventListener('click', resetForm);
searchInput.addEventListener('input', applySearchAndFilter);
filterStatusSelect.addEventListener('change', applySearchAndFilter);
tableBody.addEventListener('click', handleTableClick);

loadEmployees().catch((error) => {
  showMessage(`Không tải được danh sách nhân viên: ${error.message}`, 'error');
});
