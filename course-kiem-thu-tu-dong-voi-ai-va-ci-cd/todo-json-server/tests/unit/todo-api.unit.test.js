import { describe, expect, it, vi } from "vitest";
import {
  TODO_API_URL,
  createTodo,
  deleteTodo,
  fetchTodos,
  updateTodo,
  updateTodoStatus,
} from "../../src/todoApiStore.js";

const mockTodos = [
  {
    id: "1",
    title: "Hoc HTML",
    completed: true,
  },
  {
    id: "2",
    title: "Hoc JavaScript",
    completed: false,
  },
];

function createSuccessFetch(data) {
  return vi.fn().mockResolvedValue({
    ok: true,
    json: async () => data,
  });
}

function createErrorFetch() {
  return vi.fn().mockResolvedValue({
    ok: false,
    json: async () => ({}),
  });
}

describe("Unit test API Todo", () => {
  it("TC-API-UNIT-01: fetchTodos gọi đúng URL", async () => {
    const fetchFn = createSuccessFetch(mockTodos);

    await fetchTodos(fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(TODO_API_URL);
  });

  it("TC-API-UNIT-02: fetchTodos sử dụng method GET mặc định", async () => {
    const fetchFn = createSuccessFetch(mockTodos);

    await fetchTodos(fetchFn);

    expect(fetchFn.mock.calls[0][1]).toBeUndefined();
  });

  it("TC-API-UNIT-03: fetchTodos trả về danh sách khi response ok", async () => {
    const fetchFn = createSuccessFetch(mockTodos);

    const result = await fetchTodos(fetchFn);

    expect(result).toEqual(mockTodos);
  });

  it("TC-API-UNIT-04: fetchTodos throw lỗi khi response không ok", async () => {
    const fetchFn = createErrorFetch();

    await expect(fetchTodos(fetchFn)).rejects.toThrow("Khong the tai danh sach cong viec!");
  });

  it("TC-API-UNIT-05: createTodo gọi đúng URL", async () => {
    const todo = { title: "Hoc API", completed: false };
    const fetchFn = createSuccessFetch({ id: "3", ...todo });

    await createTodo(todo, fetchFn);

    expect(fetchFn.mock.calls[0][0]).toBe(TODO_API_URL);
  });

  it("TC-API-UNIT-06: createTodo sử dụng method POST", async () => {
    const todo = { title: "Hoc API", completed: false };
    const fetchFn = createSuccessFetch({ id: "3", ...todo });

    await createTodo(todo, fetchFn);

    expect(fetchFn.mock.calls[0][1].method).toBe("POST");
  });

  it("TC-API-UNIT-07: createTodo gửi đúng Content-Type", async () => {
    const todo = { title: "Hoc API", completed: false };
    const fetchFn = createSuccessFetch({ id: "3", ...todo });

    await createTodo(todo, fetchFn);

    expect(fetchFn.mock.calls[0][1].headers).toEqual({
      "Content-Type": "application/json",
    });
  });

  it("TC-API-UNIT-08: createTodo gửi đúng body", async () => {
    const todo = { title: "Hoc API", completed: false };
    const fetchFn = createSuccessFetch({ id: "3", ...todo });

    await createTodo(todo, fetchFn);

    expect(fetchFn).toHaveBeenCalledWith(TODO_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(todo),
    });
  });

  it("TC-API-UNIT-09: createTodo throw lỗi khi API lỗi", async () => {
    const fetchFn = createErrorFetch();

    await expect(createTodo({ title: "Loi", completed: false }, fetchFn)).rejects.toThrow(
      "Khong the them cong viec!",
    );
  });

  it("TC-API-UNIT-10: updateTodo sử dụng method PUT", async () => {
    const todo = { id: "1", title: "Cap nhat", completed: true };
    const fetchFn = createSuccessFetch(todo);

    await updateTodo("1", todo, fetchFn);

    expect(fetchFn.mock.calls[0][1].method).toBe("PUT");
  });

  it("TC-API-UNIT-11: updateTodoStatus sử dụng method PATCH", async () => {
    const fetchFn = createSuccessFetch({ id: "1", title: "Hoc HTML", completed: false });

    await updateTodoStatus("1", false, fetchFn);

    expect(fetchFn.mock.calls[0][1].method).toBe("PATCH");
  });

  it("TC-API-UNIT-12: updateTodoStatus chỉ gửi completed", async () => {
    const fetchFn = createSuccessFetch({ id: "1", title: "Hoc HTML", completed: true });

    await updateTodoStatus("1", true, fetchFn);

    expect(fetchFn.mock.calls[0][1].body).toBe(JSON.stringify({ completed: true }));
  });

  it("TC-API-UNIT-13: deleteTodo sử dụng method DELETE", async () => {
    const fetchFn = createSuccessFetch({});

    await deleteTodo("1", fetchFn);

    expect(fetchFn.mock.calls[0][1].method).toBe("DELETE");
  });

  it("TC-API-UNIT-14: deleteTodo gọi đúng URL có id", async () => {
    const fetchFn = createSuccessFetch({});

    await deleteTodo("99", fetchFn);

    expect(fetchFn.mock.calls[0][0]).toBe(`${TODO_API_URL}/99`);
  });
});
