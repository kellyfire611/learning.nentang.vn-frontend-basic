# Đề bài
## Lưu dữ liệu dưới LocalStorage

Ở bài Assignment 01, khi bạn mở lại ứng dụng thì toàn bộ thông tin thú cưng trước sẽ không còn nữa. Vậy nên ở bài Assignment 02 bạn sẽ thực hành lưu các dữ liệu thú cưng đó lại. Điều này giúp cho khi mở lại ứng dụng thì bạn vẫn còn thông tin thú cưng đã nhập trước đó.

Để hoàn thanh được yêu cầu này, bạn sẽ cần sử dụng một API trong trình duyệt, gọi là `LocalStorage` - đây là một API giúp bạn lưu trữ các dữ liệu (ở dạng String hoặc Number) theo cấu trúc Key-Value xuống dưới bộ nhớ của trình duyệt, dữ liệu này sẽ không bị xóa kể cả bạn có tải lại trang. Bạn sẽ viết vào một file `storage.js` hai hàm:

- `saveToStorage`: Hàm nhận hai tham số là Key và Value, sau đó sẽ thực hiện việc lưu xuống LocalStorage.
- `getFromStorage`: Hàm nhận vào tham số là Key, sau đó sẽ lấy dữ liệu từ LocalStorage theo Key tương ứng.

Sau đó, bạn sẽ cần cập nhật lại các đoạn code ở bài Assignment:

- Khi mở ứng dụng, sẽ cần lấy lại dữ liệu đã lưu ở LocalStorage và hiển thị các thư cưng đã nhập.
- Khi nhập một thú cưng mới, cần lưu lại dữ liệu vào LocalStorage.
- Khi xóa thú cưng, cần xóa thú cưng tương ứng ở LocalStorage.