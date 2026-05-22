# Test Cases - Mini Shop

| ID | Kich ban | Du lieu | Ky vong |
| --- | --- | --- | --- |
| TC-01 | Tim kiem theo tu khoa | `Playwright` | Chi hien san pham co tu khoa phu hop |
| TC-02 | Them 1 san pham vao gio | San pham ID 1 | `cart-count = 1`, tong = `480.000 đ` |
| TC-03 | Them 2 san pham va ap `SAVE10` | ID 1 + ID 4 | Giam `83.000 đ`, tong `777.000 đ` |
| TC-04 | Ap `SAVE10` khi chua dat nguong | Chi co ID 3 | Khong giam gia, thong bao dieu kien chua dat |
| TC-05 | Ap `FREESHIP` | Bat ky don co san pham | Phi ship = `0 đ` |
| TC-06 | Ap `COMBO15` hop le | 3 san pham, subtotal >= 1.000.000 đ | Giam 15% |
| TC-07 | So luong = 0 | Sua quantity trong gio | He thong bao loi, khong cap nhat state |
| TC-08 | Xoa san pham khoi gio | Click nut xoa | Dung dong gio hang bien mat, tong cap nhat |
| TC-09 | Ma coupon sai | `ABC123` | Khong giam gia, hien thong bao ma khong hop le |
| TC-10 | Gio hang rong | Mo trang moi | Tam tinh, ship, tong deu = `0 đ` |

## Boundary cases can nhan manh cho hoc vien
- So luong = 1 va 10 hop le, 0 va 11 khong hop le.
- Nguong `SAVE10` tai dung moc `500.000 đ`.
- Nguong mien phi ship tai dung moc `800.000 đ` sau giam gia.
- `COMBO15` yeu cau dong thoi theo so mat hang va gia tri don.