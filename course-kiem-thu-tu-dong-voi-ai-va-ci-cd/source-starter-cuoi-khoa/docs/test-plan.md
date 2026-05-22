# Test Plan - Mini Shop

## 1. Muc tieu
- Dam bao logic gio hang dung khi them, xoa, cap nhat so luong.
- Dam bao rule giam gia va phi van chuyen khong bi sai lech khi refactor.
- Dam bao luong nguoi dung chinh tren giao dien hoat dong tu dau den cuoi.

## 2. Pham vi test
- Unit test: helper pricing, validate quantity, coupon normalization.
- Business test: summary don hang, coupon SAVE10, COMBO15, FREESHIP.
- E2E test: tim kiem san pham, them vao gio, ap coupon, cap nhat tong tien.

## 3. Ngoai pham vi
- Thanh toan thuc te voi cong thanh toan.
- Dang nhap, dang ky, luu gio hang tren backend.

## 4. Moi truong
- Node.js 20+
- Trinh duyet Chromium do Playwright cai dat
- Local static server tai cong 3105

## 5. Tieu chi pass
- Toan bo Vitest pass.
- Toan bo Playwright pass.
- Coverage phan `src/cart` dat toi thieu 90%.

## 6. Rui ro can theo doi
- Rule coupon thay doi nhung test business chua cap nhat.
- Selector giao dien doi ten neu sua HTML ma bo qua `data-testid`.
- E2E de fail neu app phu thuoc network hoặc trang thai dung chung.