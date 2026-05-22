import { describe, test } from "vitest";

describe("todo flow business", () => {
  test.todo("đếm đúng số việc đang làm và đã xong");
  test.todo("lọc đúng danh sách active và done");
  test.todo("xóa đúng việc đã xong với clearCompleted");
  test.todo("xóa đúng 1 công việc khi bấm nút xóa");
});