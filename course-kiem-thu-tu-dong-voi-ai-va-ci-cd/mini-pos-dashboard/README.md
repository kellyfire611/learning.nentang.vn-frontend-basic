# Mini POS Dashboard

Project thực hành cho môn **Kiểm thử tự động với AI và CI/CD**.

Ứng dụng mô phỏng một hệ thống bán hàng nhỏ gồm:

- Hiển thị danh sách sản phẩm.
- Thêm sản phẩm vào giỏ hàng.
- Kiểm tra số lượng mua hợp lệ.
- Không cho mua vượt tồn kho.
- Thanh toán và tự động trừ tồn kho.
- Lưu lịch sử đơn hàng vào `orders`.
- Dashboard báo cáo doanh thu.
- Biểu đồ thống kê bằng Chart.js.
- Unit test bằng Vitest.
- UI test bằng Playwright.

---

## 1. Công nghệ sử dụng

```txt
HTML
CSS
JavaScript thuần
json-server
Chart.js
Vitest
Playwright
Vite
```

---

## 2. Cấu trúc thư mục

```txt
mini-pos-dashboard/
├── index.html
├── dashboard.html
├── package.json
├── db.json
├── db.seed.json
├── playwright.config.js
├── scripts/
│   └── reset-db.mjs
├── src/
│   ├── main.js
│   ├── dashboard.js
│   ├── styles.css
│   ├── services/
│   │   ├── cartService.js
│   │   ├── productApi.js
│   │   ├── orderApi.js
│   │   └── reportService.js
│   └── utils/
│       └── formatMoney.js
├── tests/
│   ├── unit/
│   │   ├── cartService.test.js
│   │   └── reportService.test.js
│   └── e2e/
│       ├── mini-pos.spec.js
│       └── dashboard.spec.js
└── README.md
```

---

## 3. Cài đặt project

Chạy lệnh:

```bash
npm install
```

Cài trình duyệt cho Playwright:

```bash
npx playwright install
```

---

## 4. Chạy API json-server

Mở terminal thứ nhất:

```bash
npm run api
```

API chạy tại:

```txt
http://127.0.0.1:3000
```

Các endpoint chính:

```txt
GET    /products
PATCH  /products/:id
GET    /orders
POST   /orders
```

---

## 5. Chạy web app

Mở terminal thứ hai:

```bash
npm run dev
```

Web chạy tại:

```txt
http://127.0.0.1:5173
```

Các trang chính:

```txt
http://127.0.0.1:5173/index.html
http://127.0.0.1:5173/dashboard.html
```

---

## 6. Reset database

Khi cần đưa dữ liệu về ban đầu:

```bash
npm run reset-db
```

Lệnh này copy dữ liệu từ `db.seed.json` sang `db.json`.

---

## 7. Chạy unit test

```bash
npm test
```

Unit test đang kiểm tra:

- Tính tổng tiền giỏ hàng.
- Kiểm tra số lượng mua.
- Thêm sản phẩm vào giỏ.
- Tạo object đơn hàng.
- Tính tổng doanh thu.
- Đếm tổng đơn hàng.
- Tính tổng số lượng sản phẩm đã bán.
- Tìm sản phẩm bán chạy.
- Lọc sản phẩm sắp hết hàng.
- Gom doanh thu theo ngày.
- Gom số lượng bán theo sản phẩm.

---

## 8. Chạy Playwright test

```bash
npm run test:e2e
```

Playwright sẽ tự khởi động:

- json-server tại `http://127.0.0.1:3000`
- Vite tại `http://127.0.0.1:5173`

UI test đang kiểm tra:

- Hiển thị danh sách sản phẩm.
- Thêm sản phẩm vào giỏ.
- Không cho nhập số lượng sai.
- Không cho mua vượt tồn kho.
- Thanh toán thành công.
- Tồn kho giảm sau khi thanh toán.
- Dashboard hiển thị số liệu tổng quan.
- Dashboard có biểu đồ.
- Bán hàng xong thì dashboard cập nhật số liệu.

---

## 9. Gợi ý quy trình làm bài với AI

Sinh viên nên làm theo từng bước:

```txt
Bước 1: Chạy lại app Mini POS cũ.
Bước 2: Thêm orders vào db.json.
Bước 3: Tạo orderApi.js.
Bước 4: Cập nhật thanh toán để lưu đơn hàng.
Bước 5: Tạo reportService.js.
Bước 6: Viết unit test cho reportService.
Bước 7: Tạo dashboard.html.
Bước 8: Tạo dashboard.js.
Bước 9: Tích hợp Chart.js.
Bước 10: Viết Playwright test cho dashboard.
Bước 11: Chạy lại toàn bộ test.
```

---

## 10. Ghi chú

- Cần chạy `npm install` trước khi chạy project.
- Khi test E2E, Playwright sẽ tự bật server theo cấu hình trong `playwright.config.js`.
- Nếu đang mở sẵn Vite hoặc json-server, Playwright sẽ tái sử dụng server hiện có.
- Nếu dữ liệu bị thay đổi nhiều, hãy chạy `npm run reset-db`.
- Chart.js được nạp qua CDN trong `dashboard.html`, nên máy cần có Internet để biểu đồ render đầy đủ trên trình duyệt.
