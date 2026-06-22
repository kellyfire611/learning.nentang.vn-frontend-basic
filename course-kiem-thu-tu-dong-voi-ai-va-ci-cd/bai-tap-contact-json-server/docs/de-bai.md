# Đề bài: Quản lý khách hàng quan tâm khóa học

Một trung tâm đào tạo nhỏ muốn quản lý danh sách khách hàng/học viên quan tâm khóa học. Mỗi khách hàng có thông tin: họ tên, số điện thoại, email, khóa học quan tâm, trạng thái tư vấn, đánh dấu yêu thích và ghi chú.

Học viên xây dựng ứng dụng web bằng HTML, CSS, JavaScript thuần, sử dụng JSON Server làm REST API local.

## Resource chính

```txt
/customers
```

## Cấu trúc dữ liệu

```json
{
  "id": "1",
  "fullName": "Nguyễn Văn An",
  "phone": "0912345678",
  "email": "an@example.com",
  "course": "Lập trình Web",
  "status": "new",
  "isFavorite": false,
  "note": "Muốn học buổi tối"
}
```

## Trạng thái khách hàng

```json
[
  "new",
  "contacted",
  "registered"
]
```

Ý nghĩa:

- `new`: khách hàng mới
- `contacted`: đã tư vấn
- `registered`: đã đăng ký

## Chức năng bắt buộc

1. Hiển thị danh sách khách hàng bằng `GET /customers`.
2. Thêm khách hàng mới bằng `POST /customers`.
3. Cập nhật trạng thái đã tư vấn bằng `PATCH /customers/:id`.
4. Cập nhật trạng thái đã đăng ký bằng `PATCH /customers/:id`.
5. Sửa đầy đủ thông tin khách hàng bằng `PUT /customers/:id`.
6. Xóa khách hàng bằng `DELETE /customers/:id`.
7. Lọc danh sách theo: tất cả, khách mới, đã tư vấn, đã đăng ký, yêu thích.
8. Tìm kiếm theo: họ tên, số điện thoại, email, khóa học.

## Luật nghiệp vụ

Tách các hàm nghiệp vụ vào file:

```txt
src/customerBusiness.js
```

Các rule bắt buộc:

- Họ tên không được rỗng, tối thiểu 3 ký tự.
- Số điện thoại không được rỗng, chỉ chứa số, độ dài từ 9 đến 11 ký tự.
- Email có thể rỗng, nếu có nhập thì phải có ký tự `@`.
- Khóa học không được rỗng.
- Khi tạo khách hàng mới, cần trim dữ liệu và mặc định `status = new`, `isFavorite = false`.

## Test bắt buộc

- Unit test business.
- Unit test API bằng mock fetch.
- Business test theo Given - When - Then.
- Integration test với JSON Server thật.
- E2E test bằng Playwright.
