# Bai thuc hanh tinh tien dien co ban + Public API

## Muc tieu bai hoc
- Biet cach tach logic nghiep vu sang file JavaScript rieng de test.
- Viet duoc Unit test, Business test va E2E test cho cung mot chuc nang.
- Biet cach goi Public API bang `fetch` va hien thi JSON len UI.
- Biet vi sao can mock API trong unit test va E2E test.
- Chay duoc toan bo test bang npm script co san.

## Cai dat
1. Mo terminal tai thu muc project.
2. Cai package:

```bash
npm install
```

## Chay web

```bash
npx http-server -p 3000
```

Sau do mo trinh duyet tai dia chi `http://127.0.0.1:3000`.

## Chay test unit

```bash
npm run test:unit
```

## Chay test business

```bash
npm run test:business
```

## Chay test e2e

```bash
npm run test:e2e
```

## Chay tat ca test

```bash
npm run test
```

## Tai lieu kiem thu
- Ke hoach kiem thu: [docs/test-plan.md](docs/test-plan.md)
- Huong dan kiem thu: [docs/testing-guide.md](docs/testing-guide.md)

## Phan thuc hanh Public API
- API demo: `https://jsonplaceholder.typicode.com/users`
- File xu ly API: `src/customerApiStore.js`
- Tren giao dien se co 2 phan:
  1. Tinh tien dien co ban
  2. Thuc hanh goi Public API
