import { afterEach, beforeAll, describe, expect, it } from "vitest";
import { TODO_API_URL, createTodo, deleteTodo, fetchTodos, updateTodo, updateTodoStatus } from "../../src/todoApiStore.js";

const createdTodoIds = [];

async function checkApiIsRunning() {
  try {
    const response = await fetch(TODO_API_URL);
    if (!response.ok) {
      throw new Error();
    }
  } catch (error) {
    throw new Error("JSON Server chưa chạy. Hãy chạy npm run dev:api trước khi chạy integration test.");
  }
}

async function createTestTodo(title = "Integration test Todo") {
  const todo = await createTodo({
    title,
    completed: false,
  });
  createdTodoIds.push(todo.id);
  return todo;
}

describe("Integration test API thật với JSON Server", () => {
  beforeAll(async () => {
    await checkApiIsRunning();
  });

  afterEach(async () => {
    while (createdTodoIds.length > 0) {
      const id = createdTodoIds.pop();
      try {
        await deleteTodo(id);
      } catch (error) {
        // Todo có thể đã bị xóa trong test DELETE.
      }
    }
  });

  it("TC-INT-01 và TC-INT-02: GET /todos trả status 200 và array", async () => {
    const response = await fetch(TODO_API_URL);
    const todos = await response.json();

    expect(response.status).toBe(200);
    expect(Array.isArray(todos)).toBe(true);
  });

  it("TC-INT-03: Todo có id, title, completed", async () => {
    const todo = await createTestTodo("Integration schema Todo");
    const todos = await fetchTodos();
    const foundTodo = todos.find((item) => String(item.id) === String(todo.id));

    expect(foundTodo).toHaveProperty("id");
    expect(foundTodo).toHaveProperty("title");
    expect(foundTodo).toHaveProperty("completed");
  });

  it("TC-INT-04 và TC-INT-05: POST /todos tạo được Todo mới có id", async () => {
    const todo = await createTestTodo("Integration POST Todo");

    expect(todo.id).toBeDefined();
    expect(todo.title).toBe("Integration POST Todo");
  });

  it("TC-INT-06: PATCH /todos/:id cập nhật completed", async () => {
    const todo = await createTestTodo("Integration PATCH Todo");

    const updatedTodo = await updateTodoStatus(todo.id, true);

    expect(updatedTodo.completed).toBe(true);
  });

  it("TC-INT-07: PUT /todos/:id cập nhật title", async () => {
    const todo = await createTestTodo("Integration PUT Todo");

    const updatedTodo = await updateTodo(todo.id, {
      id: todo.id,
      title: "Integration PUT Todo Updated",
      completed: todo.completed,
    });

    expect(updatedTodo.title).toBe("Integration PUT Todo Updated");
  });

  it("TC-INT-08: DELETE /todos/:id xóa Todo", async () => {
    const todo = await createTestTodo("Integration DELETE Todo");

    await deleteTodo(todo.id);
    createdTodoIds.pop();

    const response = await fetch(`${TODO_API_URL}/${todo.id}`);
    expect(response.status).toBe(404);
  });
});
