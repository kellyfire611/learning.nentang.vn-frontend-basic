# Kế hoạch kiểm thử - Bài tập "Tính tiền giảm giá"

## 1. Mục tiêu
Xác nhận chức năng tính tiền sau giảm giá hoạt động đúng theo nghiệp vụ:
- Nhập giá gốc hợp lệ (> 0)
- Nhập phần trăm giảm giá hợp lệ (0 đến 100)
- Tính đúng số tiền cần trả
- Hiển thị thông báo đúng trên giao diện

## 2. Phạm vi kiểm thử
- Hàm xử lý dữ liệu trong `src/discountCalculatorStore.js`
- Luồng nghiệp vụ tính tiền sau giảm giá
- Tương tác người dùng trên giao diện `index.html`

## 3. Cấp độ kiểm thử
- Unit test
- Business test
- End-to-End (E2E) test

## 4. Danh sách test case

| Mã TC | Cấp độ | Phân loại | Mục tiêu | Dữ liệu vào | Kết quả mong đợi |
|---|---|---|---|---|---|
| Mã TC-UNIT-01 | Unit | Negative case | Bắt lỗi bỏ trống giá gốc | `price = ""` | `Vui lòng nhập giá gốc!` |
| Mã TC-UNIT-02 | Unit | Boundary case | Bắt lỗi giá gốc = 0 | `price = "0"` | `Giá gốc phải là số lớn hơn 0!` |
| Mã TC-UNIT-03 | Unit | Negative case | Bắt lỗi giá gốc âm | `price = "-1000"` | `Giá gốc phải là số lớn hơn 0!` |
| Mã TC-UNIT-04 | Unit | Negative case | Bắt lỗi giá gốc không phải số | `price = "abc"` | `Giá gốc phải là số lớn hơn 0!` |
| Mã TC-UNIT-05 | Unit | Happy path | Chấp nhận giá gốc hợp lệ | `price = "250000"` | Không có lỗi (`""`) |
| Mã TC-UNIT-06 | Unit | Negative case | Bắt lỗi bỏ trống % giảm | `discount = ""` | `Vui lòng nhập phần trăm giảm giá!` |
| Mã TC-UNIT-07 | Unit | Boundary case | Bắt lỗi % giảm < 0 | `discount = "-1"` | `Phần trăm giảm giá phải từ 0 đến 100!` |
| Mã TC-UNIT-08 | Unit | Boundary case | Bắt lỗi % giảm > 100 | `discount = "101"` | `Phần trăm giảm giá phải từ 0 đến 100!` |
| Mã TC-UNIT-09 | Unit | Negative case | Bắt lỗi % giảm không phải số | `discount = "abc"` | `Phần trăm giảm giá phải từ 0 đến 100!` |
| Mã TC-UNIT-10 | Unit | Boundary case | Chấp nhận % giảm tại biên | `discount = "0"`, `"100"` | Không có lỗi (`""`) |
| Mã TC-UNIT-11 | Unit | Happy path | Tính đúng tiền cuối sau giảm | `price = 200000`, `discount = 10` | `180000` |
| Mã TC-UNIT-12 | Unit | Boundary case | Tính đúng tại biên 0% và 100% | `200000, 0`; `200000, 100` | `200000`; `0` |
| Mã TC-UNIT-13 | Unit | Boundary case | Làm tròn tiền đúng khi format | `amount = 180000.6` | `180001 VNĐ` |
| Mã TC-UNIT-14 | Unit | Happy path | Trả kết quả hoàn chỉnh khi dữ liệu hợp lệ | `price = "200000"`, `discount = "10"` | `Số tiền cần trả: 180000 VNĐ` |
| Mã TC-BIZ-01 | Business | Negative case | Người dùng quên nhập giá gốc | `"", "10"` | Thông báo yêu cầu nhập giá gốc |
| Mã TC-BIZ-02 | Business | Negative case | Người dùng nhập giá gốc âm | `"-50000", "10"` | Thông báo giá gốc không hợp lệ |
| Mã TC-BIZ-03 | Business | Negative case | Người dùng quên nhập % giảm | `"200000", ""` | Thông báo yêu cầu nhập % giảm |
| Mã TC-BIZ-04 | Business | Boundary case | Người dùng nhập % giảm > 100 | `"200000", "101"` | Thông báo % giảm không hợp lệ |
| Mã TC-BIZ-05 | Business | Boundary case | Người dùng nhập % giảm = 0 | `"200000", "0"` | Số tiền cần trả bằng giá gốc |
| Mã TC-BIZ-06 | Business | Boundary case | Người dùng nhập % giảm = 100 | `"200000", "100"` | Số tiền cần trả bằng 0 |
| Mã TC-BIZ-07 | Business | Happy path | Người dùng nhập hợp lệ thông thường | `"200000", "10"` | `Số tiền cần trả: 180000 VNĐ` |
| Mã TC-BIZ-08 | Business | Happy path | Người dùng nhập số thập phân hợp lệ | `"99999.9", "10"` | Kết quả làm tròn hợp lệ |
| Mã TC-E2E-01 | E2E | Negative case | UI báo lỗi khi trống giá gốc | Bỏ trống giá gốc, nhập giảm giá | `#calculation-message` hiển thị lỗi + `is-error` |
| Mã TC-E2E-02 | E2E | Negative case | UI báo lỗi khi trống % giảm | Nhập giá gốc, bỏ trống giảm giá | `#calculation-message` hiển thị lỗi + `is-error` |
| Mã TC-E2E-03 | E2E | Boundary case | UI báo lỗi khi % giảm > 100 | `200000`, `101` | Hiển thị lỗi + `is-error` |
| Mã TC-E2E-04 | E2E | Happy path | UI tính đúng với dữ liệu hợp lệ | `200000`, `10` | Hiển thị `Số tiền cần trả: 180000 VNĐ` + `is-success` |
| Mã TC-E2E-05 | E2E | Boundary case | UI xử lý biên giảm 0% | `200000`, `0` | Hiển thị `Số tiền cần trả: 200000 VNĐ` + `is-success` |
| Mã TC-E2E-06 | E2E | Boundary case | UI xử lý biên giảm 100% | `200000`, `100` | Hiển thị `Số tiền cần trả: 0 VNĐ` + `is-success` |

## 5. Môi trường kiểm thử
- Node.js 18+
- Vitest cho unit/business
- Playwright + Chromium cho E2E

## 6. Tiêu chí đạt
- Toàn bộ test case `Mã TC-*` chạy pass.
- Không có lỗi JavaScript runtime khi submit form.
- Nội dung và trạng thái hiển thị (`is-error`/`is-success`) đúng với kết quả xử lý.
