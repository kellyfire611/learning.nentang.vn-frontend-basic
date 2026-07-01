# Hướng dẫn prompt AI và cách giải bài Mini POS bán hàng trừ kho

Bài thực hành: **Mini POS bán hàng và trừ kho bằng HTML, CSS, JavaScript, json-server, Vitest và Playwright**.

Mục tiêu của bài này không phải chỉ là copy code từ AI, mà là:
- Biết mô tả yêu cầu rõ ràng.
- Biết yêu cầu AI tách code theo file.
- Biết sinh unit test cho logic nghiệp vụ.
- Biết sinh Playwright test cho giao diện.
- Biết chạy test và dùng lỗi terminal để yêu cầu AI sửa.

---

## 1. Cấu trúc prompt chuẩn

Một prompt tốt nên có đủ các phần:

```text
[1] Vai trò của AI
[2] Bối cảnh bài học
[3] Mục tiêu cần làm
[4] Công nghệ bắt buộc
[5] Yêu cầu nghiệp vụ
[6] Cấu trúc file mong muốn
[7] Ràng buộc kỹ thuật
[8] Yêu cầu kiểm thử
[9] Định dạng đầu ra
[10] Tiêu chí hoàn thành
```

Không nên hỏi:

```text
Làm giúp em app bán hàng có test.
```

Nên hỏi theo mẫu có cấu trúc.

---

# PHẦN A. BỘ PROMPT CHO HỌC VIÊN

## Prompt 1: Phân tích yêu cầu trước khi sinh code

Mục tiêu: yêu cầu AI phân tích bài toán, chưa viết code ngay.

```text
Bạn là lập trình viên frontend kiêm QA Automation Engineer.

Tôi là sinh viên đang học môn Kiểm thử tự động với AI và CI/CD. Tôi cần làm bài thực hành Mini POS bán hàng và trừ kho.

Công nghệ bắt buộc:
- HTML, CSS, JavaScript thuần
- json-server để giả lập database API
- Vitest để unit test logic nghiệp vụ
- Playwright để test giao diện người dùng
- Không dùng React, Vue, Angular

Yêu cầu nghiệp vụ:
1. Hiển thị danh sách sản phẩm từ json-server.
2. Mỗi sản phẩm có id, code, name, price, stock.
3. Người dùng nhập số lượng mua.
4. Không cho mua số lượng <= 0.
5. Không cho mua vượt quá tồn kho.
6. Bấm “Thêm vào giỏ hàng” thì sản phẩm được đưa vào giỏ.
7. Giỏ hàng hiển thị tên sản phẩm, số lượng, đơn giá, thành tiền.
8. Tổng tiền đơn hàng được tính tự động.
9. Bấm “Thanh toán” thì hệ thống cập nhật tồn kho trên json-server.
10. Sau khi thanh toán thành công, giỏ hàng rỗng.
11. Nếu giỏ hàng rỗng mà bấm thanh toán thì báo lỗi.
12. Giao diện cần có data-testid để viết Playwright test.

Chưa cần viết code. Hãy giúp tôi:
1. Phân tích yêu cầu nghiệp vụ.
2. Đề xuất cấu trúc thư mục.
3. Đề xuất danh sách test case.
4. Chỉ rõ test case nào dùng unit test, test case nào dùng Playwright UI test.
5. Đề xuất dữ liệu mẫu cho db.json.
```

Kết quả mong đợi:
- Có danh sách chức năng.
- Có cấu trúc thư mục.
- Có danh sách test case.
- Có phân loại unit test và Playwright test.

---

## Prompt 2: Sinh cấu trúc project và file cấu hình

Mục tiêu: tạo trước các file nền tảng.

```text
Dựa trên phân tích ở trên, hãy sinh các file cấu hình ban đầu cho project Mini POS.

Yêu cầu tạo các file:
1. package.json
2. db.json
3. db.seed.json
4. playwright.config.js
5. scripts/reset-db.mjs
6. README.md

Yêu cầu package.json có các script:
- api: chạy json-server ở port 3000
- dev: chạy web bằng Vite ở port 5173
- reset-db: reset db.json từ db.seed.json
- test: chạy Vitest
- test:e2e: chạy Playwright
- test:e2e:ui: chạy Playwright UI mode
- install:browsers: cài browser cho Playwright

Dữ liệu db.json có 5 sản phẩm:
1. Trà sữa, giá 25000, tồn 10
2. Bánh mì, giá 15000, tồn 5
3. Cà phê, giá 20000, tồn 8
4. Nước suối, giá 10000, tồn 20
5. Mì ly, giá 12000, tồn 12

Yêu cầu:
- Trả lời theo từng file.
- Mỗi file nằm trong một code block riêng.
- Không viết file chưa được yêu cầu.
- Code đơn giản, phù hợp sinh viên mới học.
```

Kết quả mong đợi:
- Có file package.json.
- Có db.json và db.seed.json.
- Có cấu hình Playwright.
- Có script reset database.

---

## Prompt 3: Sinh giao diện HTML và CSS

Mục tiêu: tạo UI có đủ phần tử để test.

```text
Hãy sinh giao diện cho project Mini POS bằng HTML và CSS thuần.

Tạo 2 file:
1. index.html
2. src/styles.css

Yêu cầu giao diện index.html:
- Có tiêu đề “Mini POS bán hàng và trừ kho”.
- Có bảng danh sách sản phẩm.
- Có khu vực giỏ hàng.
- Có tổng tiền.
- Có nút Thanh toán.
- Có khu vực hiển thị thông báo lỗi/thành công.
- Import CSS từ /src/styles.css.
- Import JavaScript module từ /src/main.js.

Các phần tử quan trọng phải có data-testid:
- product-list
- cart-items
- cart-total
- checkout-button
- message
- reload-button

Lưu ý:
- Danh sách sản phẩm sẽ được render bằng JavaScript sau.
- Chỉ viết HTML khung và CSS.
- Giao diện rõ ràng, dễ nhìn, không cần quá phức tạp.
- Trả lời theo từng file, mỗi file một code block.
```

Kết quả mong đợi:
- Có giao diện khung.
- Có đủ data-testid chính.
- Chưa cần chạy được nghiệp vụ.

---

## Prompt 4: Sinh logic nghiệp vụ và API service

Mục tiêu: tách logic ra khỏi UI để unit test được.

```text
Hãy sinh các file JavaScript xử lý nghiệp vụ và gọi API cho project Mini POS.

Tạo các file:
1. src/services/cartService.js
2. src/services/productApi.js
3. src/utils/formatMoney.js

Yêu cầu file cartService.js:
- Không dùng DOM.
- Không gọi API.
- Chỉ chứa logic thuần để có thể unit test.

Cần có các hàm:
1. validateQuantity(quantity, stock)
   - Nếu quantity không phải số nguyên: không hợp lệ
   - Nếu quantity <= 0: không hợp lệ
   - Nếu quantity > stock: không hợp lệ
   - Ngược lại hợp lệ

2. calculateLineTotal(price, quantity)
   - Trả về price * quantity

3. calculateCartTotal(cartItems)
   - Tính tổng tiền của giỏ hàng

4. updateStockAfterCheckout(products, cartItems)
   - Trả về danh sách sản phẩm mới sau khi trừ kho

5. addItemToCart(cartItems, product, quantity)
   - Nếu sản phẩm chưa có trong giỏ thì thêm mới
   - Nếu đã có thì cộng dồn số lượng

Yêu cầu file productApi.js:
- Gọi API json-server tại http://127.0.0.1:3000/products
- Có hàm getProducts()
- Có hàm updateProductStock(productId, newStock)

Yêu cầu file formatMoney.js:
- Có hàm formatMoney(value)
- Định dạng tiền Việt Nam VND

Trả lời theo từng file, mỗi file một code block.
```

Kết quả mong đợi:
- Có service nghiệp vụ thuần.
- Có API service.
- Có hàm định dạng tiền.
- Có thể viết unit test cho cartService.js.

---

## Prompt 5: Sinh file main.js kết nối UI với nghiệp vụ

Mục tiêu: tạo phần chạy chính của app.

```text
Hãy sinh file src/main.js cho project Mini POS.

Yêu cầu:
- Import các hàm từ cartService.js.
- Import getProducts và updateProductStock từ productApi.js.
- Import formatMoney từ formatMoney.js.
- Khi mở trang, gọi API lấy danh sách sản phẩm.
- Render danh sách sản phẩm ra bảng.
- Mỗi dòng sản phẩm có:
  - data-testid="product-row-{id}"
  - data-testid="product-stock-{id}"
  - data-testid="product-quantity-{id}"
  - data-testid="add-to-cart-{id}"
- Khi bấm thêm vào giỏ:
  - Lấy số lượng từ input.
  - Validate số lượng.
  - Nếu sai thì hiển thị lỗi.
  - Nếu đúng thì thêm vào giỏ hàng.
- Render giỏ hàng vào data-testid="cart-items".
- Render tổng tiền vào data-testid="cart-total".
- Khi bấm thanh toán:
  - Nếu giỏ hàng rỗng thì báo lỗi “Giỏ hàng đang rỗng”.
  - Nếu có sản phẩm thì cập nhật tồn kho lên json-server.
  - Sau khi thanh toán thành công, tải lại sản phẩm.
  - Xóa giỏ hàng.
  - Hiển thị thông báo “Thanh toán thành công”.

Ràng buộc:
- Code dễ hiểu, có comment ngắn bằng tiếng Việt.
- Không viết lại các file khác.
- Chỉ sinh file src/main.js.
```

Kết quả mong đợi:
- Web chạy được.
- Có danh sách sản phẩm.
- Thêm giỏ hàng được.
- Thanh toán trừ kho được.

---

## Prompt 6: Sinh unit test bằng Vitest

Mục tiêu: test các hàm nghiệp vụ.

```text
Hãy viết unit test bằng Vitest cho file src/services/cartService.js.

Tạo file:
tests/unit/cartService.test.js

Cần test các hàm:

1. validateQuantity(quantity, stock)
Test case:
- số lượng hợp lệ
- số lượng bằng 0
- số lượng âm
- số lượng vượt tồn kho

2. calculateLineTotal(price, quantity)
Test case:
- tính đúng thành tiền một dòng

3. calculateCartTotal(cartItems)
Test case:
- tính đúng tổng tiền nhiều sản phẩm
- giỏ hàng rỗng thì tổng tiền bằng 0

4. updateStockAfterCheckout(products, cartItems)
Test case:
- mua thành công thì tồn kho giảm đúng
- sản phẩm không mua thì tồn kho giữ nguyên

Yêu cầu:
- Dùng describe, test, expect.
- Import đúng đường dẫn từ ../../src/services/cartService.js.
- Trả lời bằng nội dung đầy đủ của file test.
```

Kết quả mong đợi:
- Chạy `npm run test` pass.
- Sinh viên hiểu unit test là test hàm, không mở trình duyệt.

---

## Prompt 7: Sinh Playwright UI test

Mục tiêu: test thao tác người dùng trên trình duyệt.

```text
Hãy viết Playwright UI test cho project Mini POS.

Tạo file:
tests/e2e/pos.spec.js

Yêu cầu:
- Dùng @playwright/test.
- Dùng getByTestId.
- Có beforeEach để reset db.json từ db.seed.json và mở trang.
- Không dùng selector CSS phức tạp nếu không cần.

Cần test các luồng:

1. Hiển thị danh sách sản phẩm
- Kiểm tra có Trà sữa
- Kiểm tra có Bánh mì
- Kiểm tra tồn kho Trà sữa là 10

2. Thêm sản phẩm vào giỏ hàng
- Nhập số lượng Trà sữa = 2
- Bấm thêm vào giỏ
- Kiểm tra giỏ hàng có Trà sữa
- Kiểm tra tổng tiền là 50.000

3. Không cho nhập số lượng bằng 0
- Nhập 0
- Bấm thêm vào giỏ
- Kiểm tra báo lỗi “Số lượng phải lớn hơn 0”

4. Không cho mua vượt tồn kho
- Nhập 99
- Bấm thêm vào giỏ
- Kiểm tra báo lỗi “Số lượng vượt quá tồn kho”
- Kiểm tra tồn kho không đổi

5. Thanh toán thành công thì tồn kho giảm
- Tồn kho Trà sữa ban đầu là 10
- Mua 3
- Thanh toán
- Kiểm tra thông báo “Thanh toán thành công”
- Kiểm tra tồn kho còn 7

6. Thanh toán xong thì giỏ hàng rỗng

7. Giỏ hàng rỗng thì không cho thanh toán

Sau khi viết test, hãy nhắc tôi chạy:
npm run test:e2e
```

Kết quả mong đợi:
- Chạy `npm run test:e2e` pass.
- Sinh viên hiểu Playwright test là test qua giao diện.

---

## Prompt 8: Prompt sửa lỗi khi test fail

Mục tiêu: học viên biết dùng AI để sửa lỗi dựa trên bằng chứng.

```text
Tôi đang làm project Mini POS bán hàng và trừ kho.

Khi chạy lệnh:

[ghi lệnh đã chạy, ví dụ npm run test:e2e]

Tôi gặp lỗi sau:

[dán toàn bộ lỗi terminal tại đây]

Đây là file test liên quan:

[dán file test tại đây]

Đây là file code liên quan:

[dán file code tại đây]

Yêu cầu:
1. Giải thích lỗi này nghĩa là gì.
2. Chỉ ra nguyên nhân có thể xảy ra.
3. Đề xuất cách sửa tối thiểu.
4. Không viết lại toàn bộ project nếu không cần.
5. Sau khi sửa, cho biết tôi cần chạy lại lệnh nào để kiểm tra.
```

Kết quả mong đợi:
- AI không đoán mò.
- AI dựa vào lỗi terminal và code để sửa.
- Sinh viên học cách debug.

---

# PHẦN B. CÁCH GIẢI MẪU

## 1. Cấu trúc thư mục đúng

```text
mini-pos-playwright/
├─ index.html
├─ package.json
├─ db.json
├─ db.seed.json
├─ playwright.config.js
├─ PROMPTS.md
├─ README.md
├─ scripts/
│  └─ reset-db.mjs
├─ src/
│  ├─ main.js
│  ├─ styles.css
│  ├─ services/
│  │  ├─ cartService.js
│  │  └─ productApi.js
│  └─ utils/
│     └─ formatMoney.js
└─ tests/
   ├─ unit/
   │  └─ cartService.test.js
   └─ e2e/
      └─ pos.spec.js
```

## 2. Cài đặt project

```bash
npm install
npx playwright install
```

## 3. Chạy API json-server

Terminal 1:

```bash
npm run api
```

Kiểm tra API:

```text
http://127.0.0.1:3000/products
```

## 4. Chạy giao diện web

Terminal 2:

```bash
npm run dev
```

Mở:

```text
http://127.0.0.1:5173
```

## 5. Chạy unit test

```bash
npm run test
```

Kết quả mong đợi:

```text
tests/unit/cartService.test.js
✓ validateQuantity
✓ calculateLineTotal
✓ calculateCartTotal
✓ updateStockAfterCheckout
```

## 6. Chạy Playwright test

```bash
npm run test:e2e
```

Kết quả mong đợi:

```text
7 passed
```

## 7. Các chức năng phải kiểm tra bằng tay

Trước khi chạy test, sinh viên nên tự kiểm tra:

```text
1. Web hiển thị danh sách sản phẩm.
2. Nhập số lượng 2 cho Trà sữa.
3. Bấm Thêm vào giỏ.
4. Giỏ hàng có Trà sữa.
5. Tổng tiền là 50.000 ₫.
6. Nhập 99 thì báo lỗi vượt tồn kho.
7. Bấm Thanh toán thì tồn kho giảm.
8. Thanh toán xong thì giỏ hàng rỗng.
```

---

# PHẦN C. GỢI Ý CHẤM ĐIỂM

| Tiêu chí | Điểm |
|---|---:|
| Source code chạy được | 2 |
| json-server hoạt động đúng | 1 |
| Nghiệp vụ bán hàng trừ kho đúng | 2 |
| Unit test đầy đủ và pass | 1.5 |
| Playwright test đầy đủ và pass | 2 |
| Có PROMPTS.md ghi lại prompt và nhận xét | 1 |
| Biết giải thích lỗi/sửa lỗi | 0.5 |

---

# PHẦN D. YÊU CẦU NỘP BÀI

Sinh viên nộp:

```text
1. Source code project
2. Ảnh chụp web chạy được
3. Ảnh chụp npm run test pass
4. Ảnh chụp npm run test:e2e pass
5. File PROMPTS.md
6. Nhận xét ngắn:
   - AI làm đúng gì?
   - AI làm sai gì?
   - Em đã sửa gì?
```

---

# PHẦN E. LƯU Ý KHI DÙNG CHATGPT MIỄN PHÍ

Nếu dùng ChatGPT miễn phí, học viên nên:
- Không yêu cầu AI sinh toàn bộ project trong một lần.
- Chia thành từng prompt nhỏ theo từng file.
- Mỗi lần chỉ yêu cầu 1 đến 3 file.
- Dán lỗi terminal đầy đủ khi yêu cầu sửa lỗi.
- Không dán toàn bộ project nếu không cần.
- Ưu tiên dán file liên quan đến lỗi.

Cách làm tốt nhất với tài khoản miễn phí:

```text
Lần 1: Yêu cầu phân tích yêu cầu.
Lần 2: Yêu cầu sinh package.json, db.json, config.
Lần 3: Yêu cầu sinh HTML/CSS.
Lần 4: Yêu cầu sinh service.
Lần 5: Yêu cầu sinh main.js.
Lần 6: Yêu cầu sinh unit test.
Lần 7: Yêu cầu sinh Playwright test.
Lần 8: Dán lỗi nếu có và yêu cầu sửa.
```
