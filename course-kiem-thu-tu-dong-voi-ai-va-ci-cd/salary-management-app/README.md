# Salary Management App

Bài mẫu xây dựng ứng dụng **quản lý nhân viên và lập bảng lương** bằng HTML, CSS, JavaScript thuần, JSON Server, Vitest và Playwright.

Ứng dụng gồm 2 trang:

- `employees.html`: quản lý danh sách nhân viên.
- `payroll.html`: lập bảng lương theo tháng.

---

## 1. Công nghệ sử dụng

- HTML
- CSS
- JavaScript ES Module
- Vite
- JSON Server
- Vitest
- Playwright

---

## 2. Cấu trúc thư mục

```txt
salary-management-app/
├── db.json
├── package.json
├── index.html
├── employees.html
├── payroll.html
├── playwright.config.js
├── src/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── api.js
│       ├── salaryCalculator.js
│       ├── employeeService.js
│       ├── payrollService.js
│       ├── employeesPage.js
│       └── payrollPage.js
├── tests/
│   ├── unit/
│   │   └── salaryCalculator.test.js
│   ├── business/
│   │   └── payrollBusiness.test.js
│   └── e2e/
│       ├── employees.spec.js
│       └── payroll.spec.js
└── README.md
```

---

## 3. Chức năng chính

### Trang quản lý nhân viên

- Xem danh sách nhân viên.
- Thêm nhân viên.
- Sửa nhân viên.
- Ngừng hoạt động nhân viên.
- Tìm kiếm theo mã, tên, phòng ban.
- Lọc theo trạng thái `active` hoặc `inactive`.

### Trang lập bảng lương

- Chọn tháng/năm.
- Tạo bảng lương.
- Không cho tạo trùng bảng lương cùng tháng/năm.
- Chỉ đưa nhân viên `active` vào bảng lương mới.
- Snapshot thông tin nhân viên vào bảng lương.
- Nhập ngày công, tăng ca, thưởng, khấu trừ, tạm ứng.
- Tự động tính lại lương.
- Lưu bảng lương.
- Khóa bảng lương.
- Bảng lương đã khóa không cho chỉnh sửa.

---

## 4. Công thức tính lương

```txt
workingDaySalary = baseSalary * salaryCoefficient * actualWorkingDays / standardWorkingDays

hourlyRate = baseSalary * salaryCoefficient / standardWorkingDays / 8

overtimePay = hourlyRate * overtimeHours * 1.5

grossIncome = workingDaySalary + allowance + overtimePay + bonus

insuranceAmount = baseSalary * salaryCoefficient * 0.105

taxableIncome = grossIncome - insuranceAmount - 11000000 - dependentCount * 4400000

Nếu taxableIncome <= 0:
personalTax = 0

Nếu taxableIncome > 0:
personalTax = taxableIncome * 0.05

netSalary = grossIncome - insuranceAmount - personalTax - deduction - advance
```

Tất cả giá trị tiền tệ được làm tròn bằng `Math.round()`.

---

## 5. Cài đặt project

```bash
npm install
```

Cài trình duyệt cho Playwright:

```bash
npx playwright install
```

---

## 6. Chạy JSON Server

Mở terminal 1:

```bash
npm run server
```

JSON Server chạy tại:

```txt
http://localhost:3000
```

Các endpoint chính:

```txt
http://localhost:3000/employees
http://localhost:3000/payrolls
```

---

## 7. Chạy giao diện web

Mở terminal 2:

```bash
npm run dev
```

Ứng dụng chạy tại:

```txt
http://localhost:5173
```

Các trang:

```txt
http://localhost:5173/index.html
http://localhost:5173/employees.html
http://localhost:5173/payroll.html
```

---

## 8. Chạy Unit Test

```bash
npm run test:unit
```

Unit Test kiểm tra các hàm tính lương trong file:

```txt
src/js/salaryCalculator.js
```

---

## 9. Chạy Business Test

```bash
npm run test:business
```

Business Test kiểm tra nghiệp vụ lập bảng lương ở mức service, ví dụ:

- Chỉ lấy nhân viên `active`.
- Không tạo trùng bảng lương.
- Snapshot dữ liệu nhân viên.
- Không cho sửa bảng lương đã khóa.

---

## 10. Chạy toàn bộ Vitest

```bash
npm run test
```

---

## 11. Chạy Playwright UI Test

Có 2 cách.

### Cách 1: Tự chạy server trước

Terminal 1:

```bash
npm run server
```

Terminal 2:

```bash
npm run dev
```

Terminal 3:

```bash
npm run test:e2e
```

### Cách 2: Để Playwright tự chạy server

```bash
npm run test:e2e
```

File `playwright.config.js` đã cấu hình tự chạy:

- JSON Server tại `http://localhost:3000`
- Vite tại `http://localhost:5173`

---

## 12. Danh sách test case

### Unit Test

- UT01: Tính lương đủ 26 ngày công.
- UT02: Tính lương 13/26 ngày công.
- UT03: Tăng ca 0 giờ.
- UT04: Tăng ca 8 giờ.
- UT05: Tính gross income.
- UT06: Tính bảo hiểm.
- UT07: Thu nhập chưa tới mức chịu thuế.
- UT08: Thu nhập vượt mức chịu thuế.
- UT09: Tính net salary.
- UT10: Tính đầy đủ payroll item.

### Business Test

- BT01: Tạo bảng lương từ nhân viên active.
- BT02: Nhân viên inactive không có trong bảng lương mới.
- BT03: Không tạo trùng bảng lương.
- BT04: Snapshot dữ liệu nhân viên.
- BT05: Cập nhật ngày công làm đổi lương thực nhận.
- BT06: Thưởng làm tăng gross income.
- BT07: Khấu trừ làm giảm net salary.
- BT08: Tổng quỹ lương bằng tổng net salary.
- BT09: Khóa bảng lương.
- BT10: Không sửa bảng lương đã locked.

### Playwright UI Test

- E2E01: Mở trang nhân viên.
- E2E02: Thêm nhân viên mới.
- E2E03: Không cho thêm khi thiếu họ tên.
- E2E04: Tìm kiếm nhân viên.
- E2E05: Cập nhật hệ số lương.
- E2E06: Ngừng hoạt động nhân viên.
- E2E07: Mở trang bảng lương.
- E2E08: Tạo bảng lương.
- E2E09: Không tạo trùng bảng lương.
- E2E10: Nhập ngày công làm đổi lương.
- E2E11: Nhập thưởng làm tăng lương.
- E2E12: Nhập tạm ứng làm giảm lương.
- E2E13: Khóa bảng lương.
- E2E14: Bảng lương locked không cho chỉnh sửa.

---

## 13. Ghi chú dữ liệu

File `db.json` có 2 collection:

```json
{
  "employees": [],
  "payrolls": []
}
```

Khi chạy ứng dụng, dữ liệu thêm mới sẽ được lưu trực tiếp vào `db.json`.

Khi muốn reset dữ liệu, có thể xóa các bảng lương trong `payrolls` hoặc copy lại file `db.json` ban đầu.
