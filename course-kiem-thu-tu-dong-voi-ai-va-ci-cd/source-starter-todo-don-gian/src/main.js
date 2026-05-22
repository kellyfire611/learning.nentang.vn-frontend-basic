import { createTodoStore } from "./todoStore.js";

const store = createTodoStore();

const elements = {
  input: document.querySelector("#todo-input"),
  addButton: document.querySelector("#add-button"),
  message: document.querySelector("#message"),
  totalCount: document.querySelector('[data-testid="total-count"]'),
  activeCount: document.querySelector('[data-testid="active-count"]'),
  doneCount: document.querySelector('[data-testid="done-count"]'),
  currentFilter: document.querySelector("#current-filter"),
  todoList: document.querySelector("#todo-list"),
  clearDone: document.querySelector("#clear-done"),
  filterButtons: Array.from(document.querySelectorAll("[data-filter]"))
};

function getFilterLabel(filter) {
  if (filter === "active") return "chưa xong";
  if (filter === "done") return "đã xong";
  return "tất cả";
}

function updateMessage(message) {
  elements.message.textContent = message;
}

function render() {
  const { visibleTodos, summary } = store.getState();

  elements.totalCount.textContent = `${summary.total} việc`;
  elements.activeCount.textContent = `${summary.active} đang làm`;
  elements.doneCount.textContent = `${summary.done} đã xong`;
  elements.currentFilter.textContent = `Đang xem: ${getFilterLabel(summary.filter)}`;

  elements.filterButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.filter === summary.filter);
  });

  if (!visibleTodos.length) {
    elements.todoList.innerHTML = '<div class="empty-state">Không có công việc nào trong bộ lọc hiện tại.</div>';
    return;
  }

  elements.todoList.innerHTML = visibleTodos.map((todo) => `
    <section class="todo-item" data-testid="todo-item-${todo.id}">
      <div class="todo-left">
        <input
          type="checkbox"
          data-testid="toggle-todo-${todo.id}"
          data-toggle-id="${todo.id}"
          ${todo.completed ? "checked" : ""}
        />
        <div>
          <strong class="todo-title ${todo.completed ? "done" : ""}">${todo.title}</strong>
          <div class="todo-badge ${todo.completed ? "done" : ""}" data-testid="todo-status-${todo.id}">
            ${todo.completed ? "Đã xong" : "Đang làm"}
          </div>
        </div>
      </div>
      <button class="remove-button" data-testid="remove-todo-${todo.id}" data-remove-id="${todo.id}" type="button">Xóa</button>
    </section>
  `).join("");

  elements.todoList.querySelectorAll("[data-toggle-id]").forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      store.toggleTodo(Number(checkbox.dataset.toggleId));
      updateMessage("Đã cập nhật trạng thái công việc.");
      render();
    });
  });

  elements.todoList.querySelectorAll("[data-remove-id]").forEach((button) => {
    button.addEventListener("click", () => {
      store.removeTodo(Number(button.dataset.removeId));
      updateMessage("Đã xóa công việc.");
      render();
    });
  });
}

function addTodoFromInput() {
  try {
    store.addTodo(elements.input.value);
    elements.input.value = "";
    updateMessage("Đã thêm công việc mới.");
    render();
    elements.input.focus();
  } catch (error) {
    updateMessage(error.message);
  }
}

elements.addButton.addEventListener("click", addTodoFromInput);

elements.input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    addTodoFromInput();
  }
});

elements.filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    store.setFilter(button.dataset.filter);
    updateMessage(`Đã chuyển bộ lọc sang ${getFilterLabel(button.dataset.filter)}.`);
    render();
  });
});

elements.clearDone.addEventListener("click", () => {
  store.clearCompleted();
  updateMessage("Đã xóa các việc đã xong.");
  render();
});

render();