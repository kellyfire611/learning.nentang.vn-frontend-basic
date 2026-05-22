# Source starter cuoi khoa - AI Testing va CI/CD

Thu muc nay danh cho hoc vien tu lam bai truoc khi xem dap an.

## Ban nay co san gi?
- `index.html` + `styles/` + `src/`: app mini shop da co san source de tap trung vao bai toan testing.
- `docs/test-plan.md` va `docs/test-cases.md`: tai lieu dau vao de hoc vien viet test.
- `docs/student-tasks.md`: checklist viec can lam.
- `tests/`: chi co khung `todo`, hoc vien tu hoan thien.
- Chua co workflow CI hoan chinh, hoc vien tu tao them.

## Cach hoc de dat hieu qua
1. Chay app local va tu nghich luong nghiep vu.
2. Doc `docs/test-cases.md` va bo sung them case neu can.
3. Viet test vao cac file trong `tests/`.
4. Tu tao `.github/workflows/ci.yml`.
5. Sau khi xong, doi chieu voi `../source-mau-cuoi-khoa/`.

## Cach chay local

```bash
npm install
npm run serve
npm test
npm run test:e2e
```

## Luu y
- App dung cong `3105` de tranh dung voi server khac.
- `npm test` va `npm run test:e2e` se chi hien `todo` cho den khi hoc vien tu viet test that.