# Test Plan

## 1. Mục tiêu

Kiểm tra ứng dụng quản lý khách hàng hoạt động đúng về nghiệp vụ, API, giao diện và luồng người dùng thật.

## 2. Phạm vi test

### Unit test business

Kiểm thử các hàm trong `src/customerBusiness.js`:

- `validateCustomerForm`
- `createCustomerPayload`
- `filterCustomers`
- `searchCustomers`
- `updateCustomerStatusInList`
- `removeCustomerFromList`

### Unit test API

Kiểm thử các hàm trong `src/customerApiStore.js` bằng mock fetch:

- `fetchCustomers`
- `createCustomer`
- `updateCustomer`
- `patchCustomerStatus`
- `deleteCustomer`

### Business test

Kiểm thử theo dạng Given - When - Then.

### Integration test

Chạy JSON Server thật và kiểm thử các API:

- GET
- POST
- PATCH
- PUT
- DELETE

### E2E test

Dùng Playwright kiểm tra thao tác thật trên trình duyệt.

## 3. Tiêu chí đạt

- Chạy được app.
- Chạy được JSON Server.
- Tất cả unit test pass.
- Tất cả business test pass.
- Integration test tự cleanup dữ liệu.
- E2E test chạy được luồng chính của người dùng.
