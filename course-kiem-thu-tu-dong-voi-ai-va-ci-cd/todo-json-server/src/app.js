import {
  createTodo,
  deleteTodo,
  fetchTodos,
  updateTodo,
  updateTodoStatus,
} from "./todoApiStore.js";
import {
  createTodoPayload,
  filterTodos,
  findTodoById,
  removeTodoFromList,
  updateTodoInList,
  validateTodoTitle,
} from "./todoBusiness.js";

const todoForm = document.querySelector("#todo-form");
const todoTitleInput = document.querySelector("#todo-title-input");
const formMessage = document.querySelector("#form-message");
const loadingMessage = document.querySelector("#loading-message");
const apiMessage = document.querySelector("#api-message");
const todoList = document.querySelector("#todo-list");
const filterAllButton = document.querySelector("#filter-all");
const filterActiveButton = document.querySelector("#filter-active");
const filterCompletedButton = document.querySelector("#filter-completed");

let todos = [];
let currentFilter = "all";

function showMessage(element, message, type) {
  element.textContent = message;
  element.className = `message ${type}`;
}

function clearMessage(element) {
  element.textContent = "";
  element.className = "message";
}

async function loadTodos() {
  loadingMessage.textContent = "Đang tải danh sách công việc...";
  clearMessage(apiMessage);

  try {
    todos = await fetchTodos();
    renderTodos();
    showMessage(apiMessage, "Tải dữ liệu thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, "Không thể tải danh sách công việc!", "error");
  } finally {
    loadingMessage.textContent = "";
  }
}

function renderTodos() {
  const visibleTodos = filterTodos(todos, currentFilter);
  todoList.textContent = "";

  if (visibleTodos.length === 0) {
    const emptyItem = document.createElement("li");
    emptyItem.className = "empty-item";
    emptyItem.textContent = "Khong co cong viec nao.";
    todoList.appendChild(emptyItem);
    return;
  }

  visibleTodos.forEach((todo) => {
    todoList.appendChild(renderTodoItem(todo));
  });
}

function renderTodoItem(todo) {
  const item = document.createElement("li");
  item.className = todo.completed ? "todo-item completed" : "todo-item";
  item.dataset.testid = "todo-item";
  item.dataset.id = todo.id;

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = todo.completed;
  checkbox.dataset.testid = "todo-checkbox";
  checkbox.addEventListener("change", () => handleToggleTodo(todo.id, checkbox.checked));

  const title = document.createElement("span");
  title.className = "todo-title";
  title.textContent = todo.title;

  const editButton = document.createElement("button");
  editButton.type = "button";
  editButton.className = "edit-button";
  editButton.dataset.testid = "edit-todo-button";
  editButton.textContent = "Sửa";
  editButton.addEventListener("click", () => handleEditTodo(todo.id));

  const deleteButton = document.createElement("button");
  deleteButton.type = "button";
  deleteButton.className = "delete-button";
  deleteButton.dataset.testid = "delete-todo-button";
  deleteButton.textContent = "Xóa";
  deleteButton.addEventListener("click", () => handleDeleteTodo(todo.id));

  item.append(checkbox, title, editButton, deleteButton);
  return item;
}

async function handleCreateTodo(event) {
  event.preventDefault();
  clearMessage(formMessage);

  const title = todoTitleInput.value;
  const errorMessage = validateTodoTitle(title);

  if (errorMessage) {
    showMessage(formMessage, errorMessage, "error");
    return;
  }

  try {
    const newTodo = await createTodo(createTodoPayload(title));
    todos = [...todos, newTodo];
    todoTitleInput.value = "";
    renderTodos();
    showMessage(formMessage, "Thêm công việc thành công!", "success");
  } catch (error) {
    showMessage(formMessage, error.message, "error");
  }
}

async function handleToggleTodo(id, completed) {
  try {
    const updatedTodo = await updateTodoStatus(id, completed);
    todos = updateTodoInList(todos, updatedTodo);
    renderTodos();
    showMessage(apiMessage, "Cập nhật công việc thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, error.message, "error");
    renderTodos();
  }
}

async function handleEditTodo(id) {
  const currentTodo = findTodoById(todos, id);

  if (!currentTodo) {
    return;
  }

  const newTitle = prompt("Nhap ten cong viec moi:", currentTodo.title);

  if (newTitle === null) {
    return;
  }

  const errorMessage = validateTodoTitle(newTitle);

  if (errorMessage) {
    showMessage(apiMessage, errorMessage, "error");
    return;
  }

  try {
    const updatedTodo = await updateTodo(id, {
      ...currentTodo,
      title: newTitle.trim(),
    });
    todos = updateTodoInList(todos, updatedTodo);
    renderTodos();
    showMessage(apiMessage, "Cập nhật công việc thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, error.message, "error");
  }
}

async function handleDeleteTodo(id) {
  const accepted = confirm("Ban co chac muon xoa cong viec nay?");

  if (!accepted) {
    return;
  }

  try {
    await deleteTodo(id);
    todos = removeTodoFromList(todos, id);
    renderTodos();
    showMessage(apiMessage, "Xóa công việc thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, error.message, "error");
  }
}

function setFilter(filter) {
  currentFilter = filter;
  filterAllButton.classList.toggle("active", filter === "all");
  filterActiveButton.classList.toggle("active", filter === "active");
  filterCompletedButton.classList.toggle("active", filter === "completed");
  renderTodos();
}

todoForm.addEventListener("submit", handleCreateTodo);
filterAllButton.addEventListener("click", () => setFilter("all"));
filterActiveButton.addEventListener("click", () => setFilter("active"));
filterCompletedButton.addEventListener("click", () => setFilter("completed"));

loadTodos();
