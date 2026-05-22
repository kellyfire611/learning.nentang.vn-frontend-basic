import { describe, expect, it } from "vitest";
import { createTodoStore } from "../../src/todoStore.js";

describe("todo flow business", () => {
  it("đếm đúng số việc đang làm và đã xong", () => {
    const store = createTodoStore();

    store.addTodo("Hoc unit test");
    store.addTodo("Hoc E2E test");
    store.toggleTodo(2);

    expect(store.getSummary()).toEqual({
      total: 2,
      active: 1,
      done: 1,
      filter: "all"
    });
  });

  it("lọc đúng danh sách active", () => {
    const store = createTodoStore();

    store.addTodo("Viet test plan");
    store.addTodo("Viet unit test");
    store.toggleTodo(2);
    store.setFilter("active");

    expect(store.getState().visibleTodos).toEqual([
      expect.objectContaining({ id: 1, title: "Viet test plan", completed: false })
    ]);
  });

  it("lọc đúng danh sách done", () => {
    const store = createTodoStore();

    store.addTodo("Doc testcase");
    store.addTodo("Chay CI");
    store.toggleTodo(1);
    store.setFilter("done");

    expect(store.getState().visibleTodos).toEqual([
      expect.objectContaining({ id: 1, completed: true })
    ]);
  });

  it("clearCompleted chỉ xóa việc đã xong", () => {
    const store = createTodoStore();

    store.addTodo("Hoc HTML");
    store.addTodo("Hoc CSS");
    store.toggleTodo(1);
    store.clearCompleted();

    expect(store.getState()).toMatchObject({
      todos: [expect.objectContaining({ id: 2, title: "Hoc CSS", completed: false })],
      summary: expect.objectContaining({ total: 1, active: 1, done: 0 })
    });
  });

  it("removeTodo xóa đúng công việc", () => {
    const store = createTodoStore();

    store.addTodo("Bai 1");
    store.addTodo("Bai 2");
    store.removeTodo(1);

    expect(store.getState().todos).toEqual([
      expect.objectContaining({ id: 2, title: "Bai 2" })
    ]);
  });
});