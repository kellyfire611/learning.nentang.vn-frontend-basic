import { describe, expect, it } from "vitest";
import {
  createTodoPayload,
  filterTodos,
  findTodoById,
  removeTodoFromList,
  updateTodoInList,
  validateTodoTitle,
} from "../../src/todoBusiness.js";

const sampleTodos = [
  { id: "1", title: "Hoc HTML", completed: true },
  { id: "2", title: "Hoc JavaScript", completed: false },
  { id: "3", title: "Viet test", completed: false },
];

describe("Unit test nghiệp vụ Todo", () => {
  it("TC-BUSINESS-UNIT-01: validateTodoTitle báo lỗi khi bỏ trống", () => {
    expect(validateTodoTitle("   ")).toBe("Vui long nhap ten cong viec!");
  });

  it("TC-BUSINESS-UNIT-02: validateTodoTitle báo lỗi khi dưới 3 ký tự", () => {
    expect(validateTodoTitle("ab")).toBe("Ten cong viec phai co it nhat 3 ky tu!");
  });

  it("TC-BUSINESS-UNIT-03: validateTodoTitle báo lỗi khi trên 100 ký tự", () => {
    expect(validateTodoTitle("a".repeat(101))).toBe("Ten cong viec khong duoc vuot qua 100 ky tu!");
  });

  it("TC-BUSINESS-UNIT-04: validateTodoTitle hợp lệ", () => {
    expect(validateTodoTitle("Hoc API")).toBe("");
  });

  it("TC-BUSINESS-UNIT-05: createTodoPayload trim title", () => {
    expect(createTodoPayload("  Hoc JavaScript  ").title).toBe("Hoc JavaScript");
  });

  it("TC-BUSINESS-UNIT-06: createTodoPayload mặc định completed false", () => {
    expect(createTodoPayload("Hoc JavaScript").completed).toBe(false);
  });

  it("TC-BUSINESS-UNIT-07: filterTodos all trả toàn bộ", () => {
    expect(filterTodos(sampleTodos, "all")).toEqual(sampleTodos);
  });

  it("TC-BUSINESS-UNIT-08: filterTodos active trả việc chưa hoàn thành", () => {
    expect(filterTodos(sampleTodos, "active")).toEqual([
      { id: "2", title: "Hoc JavaScript", completed: false },
      { id: "3", title: "Viet test", completed: false },
    ]);
  });

  it("TC-BUSINESS-UNIT-09: filterTodos completed trả việc đã hoàn thành", () => {
    expect(filterTodos(sampleTodos, "completed")).toEqual([
      { id: "1", title: "Hoc HTML", completed: true },
    ]);
  });

  it("TC-BUSINESS-UNIT-10: findTodoById tìm đúng Todo", () => {
    expect(findTodoById(sampleTodos, 2)).toEqual({ id: "2", title: "Hoc JavaScript", completed: false });
  });

  it("TC-BUSINESS-UNIT-11: updateTodoInList cập nhật đúng Todo", () => {
    const updatedTodo = { id: "2", title: "Hoc API", completed: true };

    expect(updateTodoInList(sampleTodos, updatedTodo)[1]).toEqual(updatedTodo);
  });

  it("TC-BUSINESS-UNIT-12: updateTodoInList không thay đổi mảng cũ", () => {
    const updatedTodo = { id: "2", title: "Hoc API", completed: true };

    updateTodoInList(sampleTodos, updatedTodo);

    expect(sampleTodos[1]).toEqual({ id: "2", title: "Hoc JavaScript", completed: false });
  });

  it("TC-BUSINESS-UNIT-13: removeTodoFromList xóa đúng Todo", () => {
    expect(removeTodoFromList(sampleTodos, "2")).toEqual([
      { id: "1", title: "Hoc HTML", completed: true },
      { id: "3", title: "Viet test", completed: false },
    ]);
  });
});
