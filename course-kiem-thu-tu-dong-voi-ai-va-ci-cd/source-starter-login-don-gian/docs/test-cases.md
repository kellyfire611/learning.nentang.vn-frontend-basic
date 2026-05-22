# Test Cases - Login App Don Gian

| ID | Kich ban | Du lieu | Ky vong |
| --- | --- | --- | --- |
| TC-01 | Submit rong | email = `""`, password = `""` | Bao `Vui long nhap email.`; attempts tang 1 |
| TC-02 | Email sai dinh dang | email = `student.example.com` | Bao `Email khong hop le.` |
| TC-03 | Thieu mat khau | email dung, password rong | Bao `Vui long nhap mat khau.` |
| TC-04 | Sai mat khau | email dung, password sai | Bao `Email hoac mat khau khong dung.`; authenticated = false |
| TC-05 | Dang nhap thanh cong | email = `student@example.com`, password = `123456` | message thanh cong; authenticated = true; co thong tin user |
| TC-06 | Dang nhap co rememberMe | rememberMe = true | Trang thai rememberMe = true |
| TC-07 | Dang xuat | Sau khi login thanh cong, bam logout | authenticated = false; user = null; message `Da dang xuat.` |
| TC-08 | Luong sai roi dung | Thu sai 1 lan, sau do dung | attempts tang theo tung lan submit; lan 2 dang nhap thanh cong |
| TC-09 | E2E submit rong | Bam nut dang nhap khi form rong | UI hien thong bao loi va trang thai `Chua dang nhap` |
| TC-10 | E2E dang nhap va dang xuat | Nhap dung thong tin, bam Dang nhap, sau do Dang xuat | Panel phien dang nhap hien/an dung theo trang thai |