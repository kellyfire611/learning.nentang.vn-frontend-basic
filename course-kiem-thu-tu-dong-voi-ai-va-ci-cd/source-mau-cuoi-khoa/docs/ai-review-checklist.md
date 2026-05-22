# Checklist review ket qua AI sinh test

1. AI co bo sot happy path, negative path, boundary case nao khong?
2. Assertion co kiem tra dung yeu cau nghiep vu hay chi kiem tra text chung chung?
3. Test co phu thuoc implementation detail de gay vo test khi refactor khong?
4. Du lieu test co ro rang, co doc duoc y nghia nghiep vu khong?
5. Selector E2E co on dinh, uu tien `data-testid` hay khong?
6. Test co reset state giua cac case hay de lai phu thuoc an?
7. AI co viet nham expected value khong? Can tu tinh lai tong, ship, discount.

## Prompt mau

```text
Hay viet business test cho module gio hang JavaScript nay.
Yeu cau:
- Cover happy path, invalid coupon, boundary subtotal 500000, 800000, 1000000
- Moi test phai dat ten theo nghiep vu
- Khong mock neu khong can thiet
- Neu thay thieu test case, liet ke truoc khi viet code
```