export function validateTodoTitle(title) {
  const trimmedTitle = title.trim();

  if (trimmedTitle.length === 0) {
    return "Vui long nhap ten cong viec!";
  }

  if (trimmedTitle.length < 3) {
    return "Ten cong viec phai co it nhat 3 ky tu!";
  }

  if (trimmedTitle.length > 100) {
    return "Ten cong viec khong duoc vuot qua 100 ky tu!";
  }

  return "";
}

export function createTodoPayload(title) {
  return {
    title: title.trim(),
    completed: false,
  };
}

export function filterTodos(todos, filter) {
  if (filter === "active") {
    return todos.filter((todo) => todo.completed === false);
  }

  if (filter === "completed") {
    return todos.filter((todo) => todo.completed === true);
  }

  return todos;
}

export function findTodoById(todos, id) {
  return todos.find((todo) => String(todo.id) === String(id));
}

export function updateTodoInList(todos, updatedTodo) {
  return todos.map((todo) => {
    if (String(todo.id) === String(updatedTodo.id)) {
      return updatedTodo;
    }

    return todo;
  });
}

export function removeTodoFromList(todos, id) {
  return todos.filter((todo) => String(todo.id) !== String(id));
}
