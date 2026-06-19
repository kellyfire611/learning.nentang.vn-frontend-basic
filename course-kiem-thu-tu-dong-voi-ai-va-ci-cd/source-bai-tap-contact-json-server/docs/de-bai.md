# Bài tập tự làm: Quản lý danh bạ khách hàng với JSON Server

## 1. Bối cảnh

Một trung tâm đào tạo muốn quản lý danh sách khách hàng/học viên quan tâm khóa học. Mỗi khách hàng có họ tên, số điện thoại, email, khóa học quan tâm, trạng thái tư vấn, đánh dấu yêu thích và ghi chú.

Học viên cần xây dựng ứng dụng bằng HTML, CSS và JavaScript thuần. Dữ liệu được lưu thông qua REST API local bằng JSON Server.

## 2. Resource API

Resource chính:

```txt
/customers
```

Mỗi khách hàng có cấu trúc:

```json
{
  "id": "1",
  "fullName": "Nguyen Van An",
  "phone": "0912345678",
  "email": "an@example.com",
  "course": "Kiem thu tu dong voi AI va CI/CD",
  "status": "new",
  "isFavorite": true,
  "note": "Quan tam lop cuoi tuan"
}
```

Trạng thái hợp lệ:

| Giá trị | Ý nghĩa |
|---|---|
| `new` | Khách hàng mới |
| `contacted` | Đã tư vấn |
| `registered` | Đã đăng ký |

## 3. Chức năng bắt buộc

1. Hiển thị danh sách khách hàng từ `GET /customers`.
2. Thêm khách hàng mới bằng `POST /customers`.
3. Cập nhật trạng thái đã tư vấn bằng `PATCH /customers/:id`.
4. Cập nhật trạng thái đã đăng ký bằng `PATCH /customers/:id`.
5. Sửa đầy đủ thông tin khách hàng bằng `PUT /customers/:id`.
6. Xóa khách hàng bằng `DELETE /customers/:id`.
7. Lọc danh sách theo tất cả, khách mới, đã tư vấn, đã đăng ký, yêu thích.
8. Tìm kiếm theo họ tên, số điện thoại, email hoặc khóa học.

## 4. Luật nghiệp vụ

- Họ tên không được rỗng và phải có ít nhất 3 ký tự.
- Số điện thoại không được rỗng, chỉ chứa chữ số, độ dài từ 9 đến 11 ký tự.
- Email có thể rỗng, nhưng nếu nhập thì phải có ký tự `@`.
- Khóa học quan tâm không được rỗng.
- Khi thêm mới, `status` mặc định là `new` và `isFavorite` mặc định là `false`.

## 5. Yêu cầu tách code

- `src/customerBusiness.js`: xử lý validate, tạo payload, lọc, tìm kiếm, cập nhật danh sách.
- `src/customerApiStore.js`: xử lý gọi REST API.
- `src/app.js`: xử lý DOM, event, state và nối UI với API.

## 6. Yêu cầu kiểm thử

Học viên cần viết đủ:

- Unit test cho business function.
- Unit test cho API store bằng mock `fetch`.
- Business test theo Given - When - Then.
- Integration test gọi JSON Server thật.
- E2E test thao tác trên trình duyệt bằng Playwright.
