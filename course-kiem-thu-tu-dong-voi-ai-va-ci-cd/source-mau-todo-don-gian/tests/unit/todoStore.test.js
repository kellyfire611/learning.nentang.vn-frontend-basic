import { describe, expect, it } from "vitest";
import { createTodoStore, normalizeText } from "../../src/todoStore.js";

describe("todoStore unit", () => {
  it("normalizeText bỏ khoảng trắng thừa", () => {
    expect(normalizeText("  hoc   vitest  ")).toBe("hoc vitest");
  });

  it("addTodo thêm công việc mới", () => {
    const store = createTodoStore();
    store.addTodo("Hoc Playwright");

    expect(store.getState()).toMatchObject({
      todos: [expect.objectContaining({ id: 1, title: "Hoc Playwright", completed: false })],
      summary: expect.objectContaining({ total: 1, active: 1, done: 0 })
    });
  });

  it("addTodo throw nếu rỗng", () => {
    const store = createTodoStore();
    expect(() => store.addTodo("   ")).toThrow(/để trống/i);
  });

  it("toggleTodo đổi trạng thái completed", () => {
    const store = createTodoStore();
    store.addTodo("Hoc test");
    store.toggleTodo(1);

    expect(store.getState().todos[0]).toMatchObject({ completed: true });
  });

  it("setFilter throw nếu filter sai", () => {
    const store = createTodoStore();
    expect(() => store.setFilter("abc")).toThrow(/hợp lệ/i);
  });
});