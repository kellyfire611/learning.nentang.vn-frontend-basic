export const TODO_API_URL = "http://localhost:3001/todos";

function buildTodoUrl(id) {
  return `${TODO_API_URL}/${id}`;
}

async function parseJson(response) {
  return response.json();
}

export async function fetchTodos(fetchFn = fetch) {
  const response = await fetchFn(TODO_API_URL);

  if (!response.ok) {
    throw new Error("Khong the tai danh sach cong viec!");
  }

  return parseJson(response);
}

export async function fetchTodoById(id, fetchFn = fetch) {
  const response = await fetchFn(buildTodoUrl(id));

  if (!response.ok) {
    throw new Error("Khong the tai cong viec!");
  }

  return parseJson(response);
}

export async function createTodo(todo, fetchFn = fetch) {
  const response = await fetchFn(TODO_API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(todo),
  });

  if (!response.ok) {
    throw new Error("Khong the them cong viec!");
  }

  return parseJson(response);
}

export async function updateTodo(id, todo, fetchFn = fetch) {
  const response = await fetchFn(buildTodoUrl(id), {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(todo),
  });

  if (!response.ok) {
    throw new Error("Khong the cap nhat cong viec!");
  }

  return parseJson(response);
}

export async function updateTodoStatus(id, completed, fetchFn = fetch) {
  const response = await fetchFn(buildTodoUrl(id), {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ completed }),
  });

  if (!response.ok) {
    throw new Error("Khong the cap nhat trang thai cong viec!");
  }

  return parseJson(response);
}

export async function deleteTodo(id, fetchFn = fetch) {
  const response = await fetchFn(buildTodoUrl(id), {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Khong the xoa cong viec!");
  }

  return parseJson(response);
}

if (typeof window !== "undefined") {
  window.todoApiStore = {
    fetchTodos,
    fetchTodoById,
    createTodo,
    updateTodo,
    updateTodoStatus,
    deleteTodo,
  };
}
