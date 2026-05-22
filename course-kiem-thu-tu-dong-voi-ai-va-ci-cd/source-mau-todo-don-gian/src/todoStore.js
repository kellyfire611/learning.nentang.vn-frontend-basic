export function normalizeText(text) {
  return String(text || "").trim().replace(/\s+/g, " ");
}

export function createTodoStore() {
  const state = {
    todos: [],
    filter: "all",
    nextId: 1
  };

  function addTodo(text) {
    const title = normalizeText(text);
    if (!title) {
      throw new Error("Nội dung công việc không được để trống.");
    }

    state.todos.push({
      id: state.nextId,
      title,
      completed: false
    });
    state.nextId += 1;

    return getState();
  }

  function toggleTodo(id) {
    const todo = state.todos.find((item) => item.id === id);
    if (!todo) {
      throw new Error("Không tìm thấy công việc.");
    }

    todo.completed = !todo.completed;
    return getState();
  }

  function removeTodo(id) {
    state.todos = state.todos.filter((item) => item.id !== id);
    return getState();
  }

  function clearCompleted() {
    state.todos = state.todos.filter((item) => !item.completed);
    return getState();
  }

  function setFilter(filter) {
    if (!["all", "active", "done"].includes(filter)) {
      throw new Error("Bộ lọc không hợp lệ.");
    }

    state.filter = filter;
    return getState();
  }

  function getVisibleTodos() {
    if (state.filter === "active") {
      return state.todos.filter((item) => !item.completed);
    }

    if (state.filter === "done") {
      return state.todos.filter((item) => item.completed);
    }

    return state.todos;
  }

  function getSummary() {
    const total = state.todos.length;
    const done = state.todos.filter((item) => item.completed).length;
    const active = total - done;

    return {
      total,
      active,
      done,
      filter: state.filter
    };
  }

  function getState() {
    return {
      todos: state.todos.map((item) => ({ ...item })),
      visibleTodos: getVisibleTodos().map((item) => ({ ...item })),
      summary: getSummary()
    };
  }

  return {
    addTodo,
    toggleTodo,
    removeTodo,
    clearCompleted,
    setFilter,
    getVisibleTodos,
    getSummary,
    getState
  };
}