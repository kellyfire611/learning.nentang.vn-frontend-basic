# Hướng dẫn kiểm thử - Bài tính tiền điện cơ bản

## 1. Mục tiêu kiểm thử
- Unit test: kiểm tra từng hàm validate, tính tiền và format tiền.
- Business test: kiểm tra các kịch bản nghiệp vụ theo đầu vào người dùng.
- E2E test: mô phỏng thao tác nhập liệu và bấm nút trên giao diện thật.

## 2. Cấu trúc test
- tests/unit/electricity.unit.test.js: kiểm thử đơn vị cho từng hàm trong store.
- tests/business/electricity.business.test.js: kiểm thử nghiệp vụ hàm calculateElectricityPayment.
- tests/e2e/electricity.e2e.spec.js: kiểm thử giao diện bằng Playwright.

## 3. Cách viết test mới
1. Xác định đầu vào cụ thể và kết quả mong đợi rõ ràng.
2. Đặt tên test theo mã TC để dễ đối chiếu với test-plan.
3. Với Unit và Business test:
- Import hàm từ src/electricityCalculatorStore.js.
- Gọi hàm với dữ liệu test.
- Dùng expect(...).toBe(...) để so sánh kết quả.
4. Với E2E test:
- Điều hướng tới trang bằng page.goto("/").
- Dùng đúng selector: #kwh-input, #calculate-button, #calculation-message.
- Kiểm tra nội dung và class trạng thái is-error hoặc is-success.

## 4. Lệnh chạy test
- Chạy unit test: npm run test:unit
- Chạy business test: npm run test:business
- Chạy e2e test: npm run test:e2e
- Chạy toàn bộ test: npm run test
- Chạy test kèm coverage: npm run test:coverage

## 5. Tiêu chí đạt
- Tất cả test pass.
- Không có lỗi JavaScript khi submit form.
- Giao diện hiển thị đúng thông báo theo từng tình huống.

## 6. Lưu ý khi thay đổi chức năng
- Nếu thay đổi nghiệp vụ tính tiền điện, cập nhật đồng thời Unit, Business và E2E test.
- Nếu thay đổi selector UI, cập nhật test E2E tương ứng trước khi chạy lại pipeline.
