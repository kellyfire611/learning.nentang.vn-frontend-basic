import { describe, expect, it, vi } from "vitest";
import { createTodo } from "../../src/todoApiStore.js";
import {
  createTodoPayload,
  filterTodos,
  removeTodoFromList,
  updateTodoInList,
  validateTodoTitle,
} from "../../src/todoBusiness.js";

describe("Business test Todo theo tình huống Cho trước - Khi - Thì", () => {
  it("TC-BIZ-01: tạo payload từ tên công việc hợp lệ", () => {
    // Cho trước
    const title = "Hoc JSON Server";

    // Khi
    const payload = createTodoPayload(title);

    // Thì
    expect(payload).toEqual({
      title: "Hoc JSON Server",
      completed: false,
    });
  });

  it("TC-BIZ-02: không cho phép thêm khi tên công việc rỗng", () => {
    const title = "   ";

    const errorMessage = validateTodoTitle(title);

    expect(errorMessage).toBe("Vui long nhap ten cong viec!");
  });

  it("TC-BIZ-03: lọc công việc chưa hoàn thành", () => {
    const todos = [
      { id: "1", title: "Da xong", completed: true },
      { id: "2", title: "Chua xong", completed: false },
    ];

    const activeTodos = filterTodos(todos, "active");

    expect(activeTodos).toEqual([{ id: "2", title: "Chua xong", completed: false }]);
  });

  it("TC-BIZ-04: đánh dấu một Todo hoàn thành", () => {
    const todos = [{ id: "1", title: "Hoc API", completed: false }];
    const updatedTodo = { id: "1", title: "Hoc API", completed: true };

    const result = updateTodoInList(todos, updatedTodo);

    expect(result[0].completed).toBe(true);
  });

  it("TC-BIZ-05: xóa một Todo khỏi danh sách", () => {
    const todos = [
      { id: "1", title: "Giu lai", completed: false },
      { id: "2", title: "Can xoa", completed: false },
    ];

    const result = removeTodoFromList(todos, "2");

    expect(result).toEqual([{ id: "1", title: "Giu lai", completed: false }]);
  });

  it("TC-BIZ-06: API trả về thành công khi thêm Todo hợp lệ", async () => {
    const payload = createTodoPayload("Hoc Vitest");
    const fetchFn = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ id: "10", ...payload }),
    });

    const newTodo = await createTodo(payload, fetchFn);

    expect(newTodo.id).toBe("10");
    expect(newTodo.title).toBe("Hoc Vitest");
  });

  it("TC-BIZ-07: API bị lỗi khi thêm Todo", async () => {
    const payload = createTodoPayload("Hoc Playwright");
    const fetchFn = vi.fn().mockResolvedValue({
      ok: false,
      json: async () => ({}),
    });

    await expect(createTodo(payload, fetchFn)).rejects.toThrow("Khong the them cong viec!");
  });
});
