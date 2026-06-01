# Kế hoạch kiểm thử - Bài tập "Tính tiền điện cơ bản"

## 1. Mục tiêu
Xác nhận chức năng tính tiền điện hoạt động đúng theo quy tắc:
- 0 - 50 kWh: 1.800 VNĐ/kWh
- 51 - 100 kWh: 2.000 VNĐ/kWh
- Trên 100 kWh: 2.500 VNĐ/kWh

## 2. Phạm vi kiểm thử
- Hàm xử lý dữ liệu trong src/electricityCalculatorStore.js
- Luồng nghiệp vụ tính tiền điện
- Tương tác người dùng trên giao diện index.html

## 3. Cấp độ kiểm thử
- Unit test
- Business test
- End-to-End (E2E) test

## 4. Danh sách test case

### 4.1 Unit test
- TC-UNIT-01: validateKwh trả lỗi khi bỏ trống
- TC-UNIT-02: validateKwh trả lỗi khi không phải số
- TC-UNIT-03: validateKwh trả lỗi khi số âm
- TC-UNIT-04: validateKwh hợp lệ khi nhập 0
- TC-UNIT-05: validateKwh hợp lệ khi nhập số dương
- TC-UNIT-06: calculateElectricityBill tính đúng khi 0 kWh
- TC-UNIT-07: calculateElectricityBill tính đúng khi 30 kWh
- TC-UNIT-08: calculateElectricityBill tính đúng tại biên 50 kWh
- TC-UNIT-09: calculateElectricityBill tính đúng khi 80 kWh
- TC-UNIT-10: calculateElectricityBill tính đúng tại biên 100 kWh
- TC-UNIT-11: calculateElectricityBill tính đúng khi 120 kWh
- TC-UNIT-12: formatCurrencyVnd trả đúng chuỗi tiền VNĐ
- TC-UNIT-13: calculateElectricityPayment trả lỗi khi bỏ trống
- TC-UNIT-14: calculateElectricityPayment trả đúng chuỗi kết quả khi hợp lệ

### 4.2 Business test
- TC-BIZ-01: Cho trước bỏ trống số kWh, Khi tính tiền điện, Thì yêu cầu nhập số kWh
- TC-BIZ-02: Cho trước số kWh không phải số, Khi tính tiền điện, Thì báo dữ liệu không hợp lệ
- TC-BIZ-03: Cho trước số kWh âm, Khi tính tiền điện, Thì báo số kWh không được âm
- TC-BIZ-04: Cho trước 0 kWh, Khi tính tiền điện, Thì tiền điện bằng 0
- TC-BIZ-05: Cho trước 30 kWh, Khi tính tiền điện, Thì tính theo bậc 1
- TC-BIZ-06: Cho trước 50 kWh, Khi tính tiền điện, Thì tính đúng tại biên bậc 1
- TC-BIZ-07: Cho trước 80 kWh, Khi tính tiền điện, Thì tính đúng bậc 1 và bậc 2
- TC-BIZ-08: Cho trước 100 kWh, Khi tính tiền điện, Thì tính đúng tại biên bậc 2
- TC-BIZ-09: Cho trước 120 kWh, Khi tính tiền điện, Thì tính đúng cả 3 bậc

### 4.3 E2E test
- TC-E2E-01: UI hiển thị lỗi khi bỏ trống số kWh
- TC-E2E-02: UI hiển thị lỗi khi nhập số kWh âm
- TC-E2E-03: UI tính đúng tiền điện khi nhập 30 kWh
- TC-E2E-04: UI tính đúng tiền điện tại biên 50 kWh
- TC-E2E-05: UI tính đúng tiền điện khi nhập 80 kWh
- TC-E2E-06: UI tính đúng tiền điện khi nhập 120 kWh

## 5. Môi trường kiểm thử
- Node.js 18+
- Vitest cho unit/business test
- Playwright + Chromium cho E2E test

## 6. Tiêu chí đạt
- Toàn bộ test case TC-* chạy pass.
- Không có lỗi JavaScript runtime khi submit form.
- Nội dung và trạng thái hiển thị (is-error/is-success) đúng theo kết quả xử lý.
