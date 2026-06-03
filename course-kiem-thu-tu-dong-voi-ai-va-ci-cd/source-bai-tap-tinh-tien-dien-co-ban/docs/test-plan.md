# Ke hoach kiem thu - Bai tap "Tinh tien dien co ban + Public API"

## 1. Muc tieu
Xac nhan 2 chuc nang hoat dong dung:
- Tinh tien dien theo quy tac:
  - 0 - 50 kWh: 1.800 VND/kWh
  - 51 - 100 kWh: 2.000 VND/kWh
  - Tren 100 kWh: 2.500 VND/kWh
- Tai danh sach khach hang mau tu Public API va hien thi len giao dien

## 2. Pham vi kiem thu
- Ham xu ly du lieu trong `src/electricityCalculatorStore.js`
- Ham xu ly API trong `src/customerApiStore.js`
- Luong nghiep vu tinh tien dien
- Luong nghiep vu tai danh sach khach hang tu Public API
- Tuong tac nguoi dung tren giao dien `index.html`

## 3. Cap do kiem thu
- Unit test
- Business test
- End-to-End (E2E) test

## 4. Danh sach test case

### 4.1 Unit test
- TC-UNIT-01: validateKwh tra loi khi bo trong
- TC-UNIT-02: validateKwh tra loi khi khong phai so
- TC-UNIT-03: validateKwh tra loi khi so am
- TC-UNIT-04: validateKwh hop le khi nhap 0
- TC-UNIT-05: validateKwh hop le khi nhap so duong
- TC-UNIT-06: calculateElectricityBill tinh dung khi 0 kWh
- TC-UNIT-07: calculateElectricityBill tinh dung khi 30 kWh
- TC-UNIT-08: calculateElectricityBill tinh dung tai bien 50 kWh
- TC-UNIT-09: calculateElectricityBill tinh dung khi 80 kWh
- TC-UNIT-10: calculateElectricityBill tinh dung tai bien 100 kWh
- TC-UNIT-11: calculateElectricityBill tinh dung khi 120 kWh
- TC-UNIT-12: formatCurrencyVnd tra dung chuoi tien VND
- TC-UNIT-13: calculateElectricityPayment tra loi khi bo trong
- TC-UNIT-14: calculateElectricityPayment tra dung chuoi ket qua khi hop le
- TC-API-UNIT-01: fetchCustomers goi dung URL API
- TC-API-UNIT-02: fetchCustomers tra ve danh sach customers khi response ok
- TC-API-UNIT-03: fetchCustomers throw loi khi response khong ok
- TC-API-UNIT-04: validateCustomers tra false neu du lieu khong phai array
- TC-API-UNIT-05: validateCustomers tra false neu array rong
- TC-API-UNIT-06: validateCustomers tra true neu du lieu hop le
- TC-API-UNIT-07: formatCustomerList format dung danh sach customers

### 4.2 Business test
- TC-BIZ-01: Cho truoc bo trong so kWh, Khi tinh tien dien, Thi yeu cau nhap so kWh
- TC-BIZ-02: Cho truoc so kWh khong phai so, Khi tinh tien dien, Thi bao du lieu khong hop le
- TC-BIZ-03: Cho truoc so kWh am, Khi tinh tien dien, Thi bao so kWh khong duoc am
- TC-BIZ-04: Cho truoc 0 kWh, Khi tinh tien dien, Thi tien dien bang 0
- TC-BIZ-05: Cho truoc 30 kWh, Khi tinh tien dien, Thi tinh theo bac 1
- TC-BIZ-06: Cho truoc 50 kWh, Khi tinh tien dien, Thi tinh dung tai bien bac 1
- TC-BIZ-07: Cho truoc 80 kWh, Khi tinh tien dien, Thi tinh dung bac 1 va bac 2
- TC-BIZ-08: Cho truoc 100 kWh, Khi tinh tien dien, Thi tinh dung tai bien bac 2
- TC-BIZ-09: Cho truoc 120 kWh, Khi tinh tien dien, Thi tinh dung ca 3 bac
- TC-API-BIZ-01: Cho truoc API tra ve danh sach khach hang, Khi tai du lieu, Thi he thong nhan duoc danh sach hop le
- TC-API-BIZ-02: Cho truoc API bi loi, Khi tai du lieu, Thi he thong tra ve loi phu hop
- TC-API-BIZ-03: Cho truoc danh sach khach hang, Khi format du lieu, Thi hien thi dung dang "id. name - email"

### 4.3 E2E test
- TC-E2E-01: UI hien thi loi khi bo trong so kWh
- TC-E2E-02: UI hien thi loi khi nhap so kWh am
- TC-E2E-03: UI tinh dung tien dien khi nhap 30 kWh
- TC-E2E-04: UI tinh dung tien dien tai bien 50 kWh
- TC-E2E-05: UI tinh dung tien dien khi nhap 80 kWh
- TC-E2E-06: UI tinh dung tien dien khi nhap 120 kWh
- TC-API-E2E-01: Bam nut tai khach hang thi hien thi danh sach khach hang
- TC-API-E2E-02: Khi API loi thi UI hien thi thong bao loi

## 5. Moi truong kiem thu
- Node.js 18+
- Vitest cho unit/business test
- Playwright + Chromium cho E2E test

## 6. Tieu chi dat
- Toan bo test case `TC-*` chay pass.
- Khong co loi JavaScript runtime khi submit form hoac bam nut tai customer.
- Noi dung va trang thai hien thi (`is-error`/`is-success`) dung theo ket qua xu ly.
- Phan Public API khong lam hong phan tinh tien dien.
