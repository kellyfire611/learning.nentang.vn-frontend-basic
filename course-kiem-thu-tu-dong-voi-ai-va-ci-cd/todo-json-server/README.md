# Todo CRUD với JSON Server

Bài thực hành này hướng dẫn xây dựng ứng dụng Todo bằng HTML, CSS và JavaScript thuần. Ứng dụng gọi REST API local bằng JSON Server và có đủ Unit test, Business test, Integration test, E2E test.

## 1. Mục tiêu bài học

Sau khi hoàn thành, học viên hiểu được:

- `GET /todos`: lấy danh sách công việc.
- `POST /todos`: thêm công việc mới.
- `PATCH /todos/:id`: cập nhật một phần dữ liệu, ví dụ trạng thái hoàn thành.
- `PUT /todos/:id`: cập nhật toàn bộ công việc.
- `DELETE /todos/:id`: xóa công việc.
- Cách dùng `fetch` để gửi và nhận JSON.
- Cách tách code API, code nghiệp vụ và code giao diện.
- Cách viết Unit test, Business test, Integration test và E2E test.

## 2. Cấu trúc project

```txt
todo-json-server/
├── index.html
├── db.json
├── package.json
├── playwright.config.js
├── src/
│   ├── todoApiStore.js
│   ├── todoBusiness.js
│   ├── app.js
│   └── style.css
├── tests/
│   ├── unit/
│   ├── business/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── test-plan.md
│   └── testing-guide.md
└── README.md
```

## 3. Cài đặt

Mở terminal tại thư mục bài tập:

```bash
cd course-kiem-thu-tu-dong-voi-ai-va-ci-cd/todo-json-server
npm install
npx playwright install
```

## 4. Chạy cả web và API

```bash
npm run dev
```

Sau đó mở:

```txt
http://localhost:3000
```

API Todo chạy tại:

```txt
http://localhost:3001/todos
```

## 5. Chạy riêng từng phần

Chạy riêng JSON Server:

```bash
npm run dev:api
```

Chạy riêng web:

```bash
npm run dev:web
```

## 6. Hướng dẫn thực hiện từng bước

### Bước 1: Tạo dữ liệu API local

Tạo file `db.json`:

```json
{
  "todos": [
    {
      "id": "1",
      "title": "Học HTML cơ bản",
      "completed": true
    },
    {
      "id": "2",
      "title": "Học JavaScript cơ bản",
      "completed": false
    }
  ]
}
```

JSON Server đọc file này và tạo REST API tự động tại `/todos`.

### Bước 2: Tạo lớp gọi API

File `src/todoApiStore.js` chỉ xử lý việc gọi server:

```js
export const TODO_API_URL = "http://localhost:3001/todos";

export async function fetchTodos(fetchFn = fetch) {
  const response = await fetchFn(TODO_API_URL);

  if (!response.ok) {
    throw new Error("Khong the tai danh sach cong viec!");
  }

  return response.json();
}
```

Khi cần thêm Todo:

```js
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

  return response.json();
}
```

### Bước 3: Tạo lớp nghiệp vụ

File `src/todoBusiness.js` không gọi API và không đụng DOM. File này chỉ xử lý dữ liệu:

```js
export function validateTodoTitle(title) {
  const trimmedTitle = title.trim();

  if (trimmedTitle.length === 0) {
    return "Vui long nhap ten cong viec!";
  }

  if (trimmedTitle.length < 3) {
    return "Ten cong viec phai co it nhat 3 ky tu!";
  }

  return "";
}
```

Tạo payload trước khi gửi API:

```js
export function createTodoPayload(title) {
  return {
    title: title.trim(),
    completed: false,
  };
}
```

### Bước 4: Tạo giao diện HTML

Trong `index.html`, cần có các id ổn định để JavaScript và E2E test sử dụng:

```html
<form id="todo-form">
  <input id="todo-title-input" type="text" />
  <button id="add-todo-button" type="submit">Thêm công việc</button>
  <p id="form-message"></p>
</form>

<button id="filter-all">Tất cả</button>
<button id="filter-active">Chưa hoàn thành</button>
<button id="filter-completed">Đã hoàn thành</button>

<p id="loading-message"></p>
<p id="api-message"></p>
<ul id="todo-list"></ul>
```

### Bước 5: Nối giao diện với API

Trong `src/app.js`, khi trang mở, gọi `loadTodos()`:

```js
async function loadTodos() {
  loadingMessage.textContent = "Đang tải danh sách công việc...";

  try {
    todos = await fetchTodos();
    renderTodos();
    showMessage(apiMessage, "Tải dữ liệu thành công!", "success");
  } catch (error) {
    showMessage(apiMessage, "Không thể tải danh sách công việc!", "error");
  } finally {
    loadingMessage.textContent = "";
  }
}
```

Khi submit form, validate trước rồi mới gọi API:

```js
async function handleCreateTodo(event) {
  event.preventDefault();

  const errorMessage = validateTodoTitle(todoTitleInput.value);

  if (errorMessage) {
    showMessage(formMessage, errorMessage, "error");
    return;
  }

  const newTodo = await createTodo(createTodoPayload(todoTitleInput.value));
  todos = [...todos, newTodo];
  renderTodos();
}
```

### Bước 6: Viết test

Thứ tự học viên nên làm:

1. Viết Unit test cho `todoBusiness.js` vì không cần server.
2. Viết Unit test cho `todoApiStore.js` bằng mock `fetch`.
3. Viết Business test theo tình huống Cho trước - Khi - Thì.
4. Viết Integration test gọi JSON Server thật.
5. Viết E2E test thao tác trực tiếp trên giao diện.

## 7. Chạy test

Chạy Unit test:

```bash
npm run test:unit
```

Chạy Business test:

```bash
npm run test:business
```

Chạy cả Unit test và Business test:

```bash
npm run test:all
```

Chạy Integration test, cần JSON Server đang chạy:

```bash
npm run dev:api
```

Ở terminal khác:

```bash
npm run test:integration
```

Chạy E2E test:

```bash
npm run test:e2e
```

Chạy toàn bộ test có API thật:

```bash
npm run test:all-with-api
```

## 8. Tiêu chí hoàn thành

Project hoàn thành khi:

- Hiển thị được danh sách Todo từ JSON Server.
- Thêm, sửa, xóa Todo được.
- Đánh dấu hoàn thành được.
- Lọc được Todo theo tất cả, chưa hoàn thành, đã hoàn thành.
- Có xử lý lỗi API.
- Có Unit test, Business test, Integration test và E2E test.
- Có README, test plan và testing guide.
- Toàn bộ test chạy được.
