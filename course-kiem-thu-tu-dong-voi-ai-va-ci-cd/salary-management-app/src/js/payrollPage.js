import {
  getPayrollByMonthYear,
  createPayroll,
  recalculatePayrollItem,
  updatePayroll,
  lockPayroll,
  calculateTotalNetSalary
} from './payrollService.js';

let currentPayroll = null;

const currencyFormatter = new Intl.NumberFormat('vi-VN', {
  style: 'currency',
  currency: 'VND'
});

const monthSelect = document.querySelector('#payroll-month-select');
const yearInput = document.querySelector('#payroll-year-input');
const createPayrollButton = document.querySelector('#create-payroll-button');
const loadPayrollButton = document.querySelector('#load-payroll-button');
const payrollStatus = document.querySelector('#payroll-status');
const tableBody = document.querySelector('#payroll-table-body');
const totalNetSalary = document.querySelector('#total-net-salary');
const savePayrollButton = document.querySelector('#save-payroll-button');
const lockPayrollButton = document.querySelector('#lock-payroll-button');
const messageBox = document.querySelector('#payroll-message');

function formatCurrency(value) {
  return currencyFormatter.format(Number(value || 0));
}

function showMessage(message, type = 'success') {
  messageBox.textContent = message;
  messageBox.className = `message ${type}`;
}

function clearMessage() {
  messageBox.textContent = '';
  messageBox.className = 'message';
}

function getSelectedMonthYear() {
  return {
    month: Number(monthSelect.value),
    year: Number(yearInput.value)
  };
}

function getStatusLabel(status) {
  if (status === 'draft') return 'draft';
  if (status === 'locked') return 'locked';
  return 'Chưa tải';
}

function updateSummary() {
  const status = currentPayroll?.status || 'muted';
  payrollStatus.textContent = getStatusLabel(currentPayroll?.status);
  payrollStatus.className = `badge ${status}`;
  totalNetSalary.textContent = formatCurrency(calculateTotalNetSalary(currentPayroll));

  const hasPayroll = Boolean(currentPayroll);
  const isLocked = currentPayroll?.status === 'locked';
  savePayrollButton.disabled = !hasPayroll || isLocked;
  lockPayrollButton.disabled = !hasPayroll || isLocked;
}

function renderEmpty(message = 'Chưa có bảng lương được tải.') {
  tableBody.innerHTML = `
    <tr>
      <td colspan="16" class="empty-cell">${message}</td>
    </tr>
  `;
  updateSummary();
}

function renderPayroll() {
  if (!currentPayroll) {
    renderEmpty();
    return;
  }

  const isLocked = currentPayroll.status === 'locked';

  tableBody.innerHTML = currentPayroll.items
    .map(
      (item) => `
        <tr data-employee-id="${item.employeeId}">
          <td>${item.employeeCode}</td>
          <td>${item.fullName}</td>
          <td>${item.department}</td>
          <td>${item.position}</td>
          <td class="money">${formatCurrency(item.baseSalary)}</td>
          <td>${item.salaryCoefficient}</td>
          <td>
            <input class="payroll-input" type="number" min="0" max="31" data-field="actualWorkingDays" data-employee-id="${item.employeeId}" data-testid="actual-working-days-${item.employeeId}" value="${item.actualWorkingDays}" ${isLocked ? 'disabled' : ''} />
          </td>
          <td>
            <input class="payroll-input" type="number" min="0" data-field="overtimeHours" data-employee-id="${item.employeeId}" data-testid="overtime-hours-${item.employeeId}" value="${item.overtimeHours}" ${isLocked ? 'disabled' : ''} />
          </td>
          <td class="money">${formatCurrency(item.allowance)}</td>
          <td>
            <input class="payroll-input" type="number" min="0" step="1000" data-field="bonus" data-employee-id="${item.employeeId}" data-testid="bonus-${item.employeeId}" value="${item.bonus}" ${isLocked ? 'disabled' : ''} />
          </td>
          <td>
            <input class="payroll-input" type="number" min="0" step="1000" data-field="deduction" data-employee-id="${item.employeeId}" data-testid="deduction-${item.employeeId}" value="${item.deduction}" ${isLocked ? 'disabled' : ''} />
          </td>
          <td>
            <input class="payroll-input" type="number" min="0" step="1000" data-field="advance" data-employee-id="${item.employeeId}" data-testid="advance-${item.employeeId}" value="${item.advance}" ${isLocked ? 'disabled' : ''} />
          </td>
          <td class="money">${formatCurrency(item.grossIncome)}</td>
          <td class="money">${formatCurrency(item.insuranceAmount)}</td>
          <td class="money">${formatCurrency(item.personalTax)}</td>
          <td class="money" data-testid="net-salary-${item.employeeId}">${formatCurrency(item.netSalary)}</td>
        </tr>
      `
    )
    .join('');

  updateSummary();
}

function setDefaultMonthYear() {
  const now = new Date();
  monthSelect.value = String(now.getMonth() + 1);
  yearInput.value = String(now.getFullYear());
}

async function handleCreatePayroll() {
  clearMessage();
  const { month, year } = getSelectedMonthYear();

  try {
    currentPayroll = await createPayroll(month, year);
    renderPayroll();
    showMessage('Tạo bảng lương thành công.');
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

async function handleLoadPayroll() {
  clearMessage();
  const { month, year } = getSelectedMonthYear();

  try {
    currentPayroll = await getPayrollByMonthYear(month, year);
    if (!currentPayroll) {
      renderEmpty('Chưa có bảng lương cho tháng/năm đã chọn.');
      showMessage('Chưa có bảng lương cho tháng/năm đã chọn.', 'error');
      return;
    }

    renderPayroll();
    showMessage('Tải bảng lương thành công.');
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

function handlePayrollInput(event) {
  const input = event.target.closest('input[data-field]');
  if (!input || !currentPayroll || currentPayroll.status === 'locked') return;

  const employeeId = input.dataset.employeeId;
  const field = input.dataset.field;
  const itemIndex = currentPayroll.items.findIndex(
    (item) => item.employeeId === employeeId
  );

  if (itemIndex === -1) return;

  const currentItem = currentPayroll.items[itemIndex];
  const updatedItem = recalculatePayrollItem({
    ...currentItem,
    [field]: Number(input.value)
  });

  currentPayroll = {
    ...currentPayroll,
    items: currentPayroll.items.map((item, index) =>
      index === itemIndex ? updatedItem : item
    )
  };

  renderPayroll();
}

async function handleSavePayroll() {
  clearMessage();

  if (!currentPayroll) {
    showMessage('Chưa có bảng lương để lưu.', 'error');
    return;
  }

  try {
    currentPayroll = await updatePayroll(currentPayroll);
    renderPayroll();
    showMessage('Lưu bảng lương thành công.');
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

async function handleLockPayroll() {
  clearMessage();

  if (!currentPayroll) {
    showMessage('Chưa có bảng lương để khóa.', 'error');
    return;
  }

  const confirmed = confirm('Bạn có chắc muốn khóa bảng lương này? Sau khi khóa sẽ không thể chỉnh sửa.');
  if (!confirmed) return;

  try {
    currentPayroll = await lockPayroll(currentPayroll.id);
    renderPayroll();
    showMessage('Khóa bảng lương thành công.');
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

createPayrollButton.addEventListener('click', handleCreatePayroll);
loadPayrollButton.addEventListener('click', handleLoadPayroll);
tableBody.addEventListener('change', handlePayrollInput);
savePayrollButton.addEventListener('click', handleSavePayroll);
lockPayrollButton.addEventListener('click', handleLockPayroll);

setDefaultMonthYear();
renderEmpty();
