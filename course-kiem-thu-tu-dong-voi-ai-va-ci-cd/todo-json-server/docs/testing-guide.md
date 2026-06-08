# Testing Guide - Todo CRUD với JSON Server

Tài liệu này giải thích các loại test trong project Todo bằng ví dụ trực tiếp từ bài thực hành.

## Unit test là gì?

Unit test kiểm tra một hàm nhỏ, độc lập.

Ví dụ: hàm `validateTodoTitle(title)` chỉ nhận title và trả về thông báo lỗi hoặc chuỗi rỗng. Hàm này không gọi API, không đụng giao diện, nên rất dễ test.

```js
expect(validateTodoTitle("")).toBe("Vui long nhap ten cong viec!");
expect(validateTodoTitle("Hoc API")).toBe("");
```

## Business test là gì?

Business test kiểm tra một tình huống nghiệp vụ theo cách người dùng hoặc hệ thống thật sự cần.

Ví dụ:

```txt
Cho trước tên công việc hợp lệ
Khi tạo payload
Thì hệ thống tạo Todo có completed bằng false
```

Code test:

```js
const payload = createTodoPayload("Hoc JSON Server");

expect(payload).toEqual({
  title: "Hoc JSON Server",
  completed: false,
});
```

Business test thường đọc dễ hơn Unit test vì nó nói theo ngôn ngữ nghiệp vụ.

## Integration test là gì?

Integration test kiểm tra nhiều phần kết hợp với nhau.

Trong project này, Integration test gọi JSON Server thật tại:

```txt
http://localhost:3001/todos
```

Ví dụ test quy trình cập nhật:

1. POST tạo Todo mới.
2. Lấy `id` Todo vừa tạo.
3. PATCH Todo đó thành `completed: true`.
4. Kiểm tra kết quả trả về.
5. DELETE Todo test để dọn dữ liệu.

Integration test giúp biết hàm gọi API có làm việc đúng với server thật hay không.

## E2E test là gì?

E2E là End-to-End test. Loại test này mở trình duyệt thật và thao tác giống người dùng.

Ví dụ:

1. Mở trang `http://localhost:3000`.
2. Nhập tên Todo vào ô input.
3. Bấm nút Thêm công việc.
4. Kiểm tra Todo mới xuất hiện trong danh sách.

E2E test kiểm tra toàn bộ luồng: giao diện, JavaScript, API và dữ liệu.

## Mock fetch là gì?

Mock fetch là thay thế `fetch` thật bằng một hàm giả trong test.

Ví dụ:

```js
const fetchFn = vi.fn().mockResolvedValue({
  ok: true,
  json: async () => [{ id: "1", title: "Hoc API", completed: false }],
});

const todos = await fetchTodos(fetchFn);
```

Lúc này test không gọi `http://localhost:3001/todos`. Test chỉ kiểm tra hàm `fetchTodos` có xử lý đúng response hay không.

## Vì sao Unit test không gọi API thật?

Unit test cần nhanh, ổn định và chỉ kiểm tra một đơn vị nhỏ.

Nếu Unit test gọi API thật thì test có thể fail vì:

- JSON Server chưa chạy.
- Port bị trùng.
- Dữ liệu trong `db.json` đã thay đổi.
- Mạng hoặc môi trường máy bị lỗi.

Vì vậy Unit test dùng mock `fetch`.

## Vì sao Integration test gọi JSON Server thật?

Integration test cần kiểm tra hàm API có hoạt động đúng với server thật.

Ví dụ, test `POST /todos` giúp xác nhận:

- Gửi đúng URL.
- Gửi đúng method.
- Gửi đúng JSON body.
- Server thật tạo Todo mới và trả về `id`.

## Vì sao phải cleanup dữ liệu test?

Khi test tạo Todo mới, dữ liệu đó sẽ nằm trong `db.json`. Nếu không xóa, lần chạy test sau có thể bị ảnh hưởng.

Ví dụ test hôm nay tạo:

```txt
Integration POST Todo
```

Nếu không cleanup, ngày mai danh sách Todo đã có sẵn dữ liệu này. Test lọc, test đếm số lượng hoặc test xóa có thể bị sai.

Vì vậy Integration test và E2E test đều phải xóa dữ liệu test sau khi chạy xong.

## Nên chạy test theo thứ tự nào?

Nên chạy từ nhỏ đến lớn:

```bash
npm run test:unit
npm run test:business
npm run test:integration
npm run test:e2e
```

Nếu Unit test fail, hãy sửa hàm nhỏ trước. Nếu Unit test pass nhưng Integration test fail, hãy kiểm tra JSON Server, URL, method và body gửi lên API.
