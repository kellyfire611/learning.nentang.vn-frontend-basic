# Mini POS bán hàng và trừ kho

Bài mẫu dùng cho học phần kiểm thử tự động với AI và CI/CD.

## Công nghệ

- HTML, CSS, JavaScript thuần
- json-server: giả lập API database
- Vitest: unit test logic nghiệp vụ
- Playwright: UI/E2E test

## Cài đặt

```bash
npm install
npx playwright install
```

## Chạy API json-server

```bash
npm run api
```

API chạy tại:

```text
http://127.0.0.1:3000/products
```

## Chạy giao diện web

Mở terminal khác:

```bash
npm run dev
```

Web chạy tại:

```text
http://127.0.0.1:5173
```

## Reset dữ liệu

```bash
npm run reset-db
```

## Chạy unit test

```bash
npm run test
```

## Chạy Playwright E2E test

```bash
npm run test:e2e
```

Lệnh này tự khởi động json-server và Vite nếu chưa chạy.

## Nghiệp vụ chính

1. Hiển thị danh sách sản phẩm.
2. Nhập số lượng mua.
3. Không cho mua số lượng <= 0.
4. Không cho mua vượt quá tồn kho.
5. Thêm sản phẩm vào giỏ hàng.
6. Tính tổng tiền.
7. Thanh toán thành công thì cập nhật tồn kho trong `db.json`.
8. Thanh toán xong thì giỏ hàng rỗng.

## Gợi ý mở rộng cho sinh viên

- Thêm nút xóa sản phẩm khỏi giỏ hàng.
- Thêm mã giảm giá SALE10.
- Thêm lọc/tìm kiếm sản phẩm.
- Thêm kiểm tra sản phẩm hết hàng.
- Thêm CI bằng GitHub Actions.
