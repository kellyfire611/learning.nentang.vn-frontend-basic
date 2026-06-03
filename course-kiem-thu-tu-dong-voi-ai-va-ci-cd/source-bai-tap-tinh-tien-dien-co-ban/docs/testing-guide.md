# Huong dan kiem thu - Bai tinh tien dien co ban + Public API

## 1. Muc tieu kiem thu
- Unit test: kiem tra tung ham validate, tinh tien, format tien.
- Unit test: kiem tra tung ham goi API, validate JSON va format danh sach customer.
- Business test: kiem tra cac kich ban nghiep vu theo dau vao nguoi dung.
- E2E test: mo phong thao tac nhap lieu, bam nut va mock API tren giao dien that.

## 2. Cau truc test
- `tests/unit/electricity.unit.test.js`: kiem thu don vi cho tung ham tinh tien dien.
- `tests/unit/customer-api.unit.test.js`: kiem thu don vi cho `fetchCustomers`, `validateCustomers`, `formatCustomerList`.
- `tests/business/electricity.business.test.js`: kiem thu nghiep vu ham `calculateElectricityPayment`.
- `tests/business/customer-api.business.test.js`: kiem thu flow nghiep vu tai customer.
- `tests/e2e/electricity.e2e.spec.js`: kiem thu giao dien tinh tien dien bang Playwright.
- `tests/e2e/customer-api.e2e.spec.js`: kiem thu UI API va mock route.

## 3. Cach viet test moi
1. Xac dinh dau vao cu the va ket qua mong doi ro rang.
2. Dat ten test theo ma TC de de doi chieu voi test-plan.
3. Voi Unit va Business test:
   - Import ham tu file `src/*.js`.
   - Goi ham voi du lieu test.
   - Dung `expect(...).toBe(...)` hoac `toEqual(...)` de so sanh ket qua.
4. Voi E2E test:
   - Dieu huong toi trang bang `page.goto("/")`.
   - Dung dung selector: `#kwh-input`, `#calculate-button`, `#calculation-message`.
   - Voi phan API dung `#load-customers-button`, `#customer-api-message`, `#customer-list`.
   - Kiem tra noi dung va class trang thai `is-error` hoac `is-success`.

## 4. Thuc hanh goi Public API
- Public API la API cong khai, cho phep goi thu ma khong can tai khoan hoac API key.
- `fetch` la API co san trong trinh duyet de gui HTTP request va nhan response JSON.
- Unit test nen mock API de test nhanh, on dinh va khong phu thuoc internet.
- E2E test nen mock API bang Playwright `route` de kiem tra UI on dinh, tranh flakey test.
- Chi nen goi API that khi test tich hop hoac co moi truong rieng de xac nhan ket noi that.

## 5. Lenh chay test
- Chay unit test: `npm run test:unit`
- Chay business test: `npm run test:business`
- Chay e2e test: `npm run test:e2e`
- Chay toan bo test: `npm run test`
- Chay test kem coverage: `npm run test:coverage`

## 6. Tieu chi dat
- Tat ca test pass.
- Khong co loi JavaScript khi submit form hoac tai customer.
- Giao dien hien thi dung thong bao theo tung tinh huong.

## 7. Luu y khi thay doi chuc nang
- Neu thay doi nghiep vu tinh tien dien, cap nhat dong thoi Unit, Business va E2E test.
- Neu thay doi format customer hoac message API, cap nhat dong thoi cac test `customer-api`.
- Neu thay doi selector UI, cap nhat test E2E tuong ung truoc khi chay lai pipeline.
