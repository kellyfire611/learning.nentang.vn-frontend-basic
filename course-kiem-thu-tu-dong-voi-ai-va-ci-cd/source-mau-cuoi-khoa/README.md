# Source mau cuoi khoa - AI Testing va CI/CD

Thu muc nay la bo du an tham khao de hoc vien xem sau khi hoc xong toan bo khoa.

## Co gi ben trong?
- `index.html` + `styles/` + `src/`: mini shop tinh bang HTML CSS JS.
- `tests/unit/`: test helper va validation.
- `tests/business/`: test nghiep vu gio hang, coupon, phi ship.
- `tests/e2e/`: Playwright cho luong nguoi dung that.
- `docs/`: test plan, test case va checklist review ket qua AI.
- `.github/workflows/ci.yml`: pipeline CI mau.
- Playwright duoc cau hinh chay app mau tren cong `3105` de tranh dung voi server khac trong may hoc vien.

## Cach chay local

```bash
npm install
npm test
npm run test:e2e
```

## Script
- `npm run serve`: chay static server tai cong 3105.
- `npm test`: chay Vitest va coverage.
- `npm run test:e2e`: chay Playwright.
- `npm run test:all`: chay tat ca test.

## Goi y su dung trong lop
- Cho hoc vien doc `docs/test-cases.md` truoc khi mo source.
- An thu muc `tests/`, yeu cau hoc vien tu viet test truoc.
- Sau do so sanh voi source mau de thao luan vi sao case nao quan trong.