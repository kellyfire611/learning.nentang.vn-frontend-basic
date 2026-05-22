# Step 6 - Viết business test

## Mục tiêu
- Kiểm tra luồng nghiệp vụ gồm nhiều bước, không chỉ một hàm đơn lẻ.
- Giúp học viên phân biệt unit test với business test.

## File cần viết
- `tests/business/loginFlow.business.test.js`

## Khi nào dùng business test
- Khi muốn mô phỏng cả một flow người dùng nhưng vẫn chưa cần UI thật.
- Khi cần kiểm tra state chuyển qua nhiều bước liên tiếp.

## Các luồng nên có
1. Sai mật khẩu một lần rồi đăng nhập đúng
2. Đăng nhập thành công với `rememberMe = true`
3. Đăng xuất đưa app về trạng thái ban đầu

## Ví dụ business test

```js
test("đi qua một lần sai rồi đăng nhập đúng", () => {
  const store = createLoginStore();

  const firstTry = store.login("student@example.com", "sai-mat-khau");
  const secondTry = store.login("student@example.com", "123456");

  expect(firstTry.message).toBe("Email hoặc mật khẩu không đúng.");
  expect(firstTry.attempts).toBe(1);
  expect(secondTry.authenticated).toBe(true);
  expect(secondTry.attempts).toBe(2);
});
```

## Điều học viên cần hiểu
- Unit test thường test từng mảnh nhỏ.
- Business test test một chuỗi hành động mang ý nghĩa nghiệp vụ.
- Business test chưa cần click thật trên trình duyệt.

## Lỗi hay gặp
1. Gộp business test thành E2E quá sớm
2. Viết quá chi tiết như unit test, làm mất ý nghĩa flow
3. Không kiểm tra state sau từng bước

## Kết quả mong đợi
- Học viên nhìn ra được flow chính của bài login mà không cần mở UI