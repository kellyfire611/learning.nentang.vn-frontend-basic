# Student Tasks - Starter Project

## Muc tieu
- Tu doc source va hieu luong nghiep vu cua mini shop.
- Tu viet test plan, unit test, business test, E2E test va workflow CI.
- Sau cung doi chieu voi `../source-mau-cuoi-khoa/` de tu review.

## Viec can lam
1. Doc `docs/test-cases.md` va bo sung neu thay con thieu boundary case.
2. Viet unit test cho `src/cart/pricing.js`.
3. Viet business test cho `src/cart/cart.js`.
4. Viet E2E test cho luong tim kiem, them gio hang, ap coupon.
5. Tao `.github/workflows/ci.yml` de chay `npm test` va `npm run test:e2e`.
6. Dung AI ho tro sinh test, nhung phai review lai bang `docs/ai-review-checklist.md`.

## Tieu chi hoan thanh goi y
- Unit/business test cover du happy path, negative path, boundary case.
- E2E test dung `data-testid`, khong dung selector mong manh.
- Khong co test phu thuoc thu tu thuc thi.
- CI chay xanh tren GitHub Actions.