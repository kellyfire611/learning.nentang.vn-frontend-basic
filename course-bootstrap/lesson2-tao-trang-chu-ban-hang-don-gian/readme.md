# Lesson 2 - Bootstrap
Tạo bố cục sử dụng Bootstrap

## Step 1: Tạo cấu trúc thư mục dự án
- Mục tiêu của việc tạo cấu trúc dự án giúp cho Việc quản lý các tập tin (các file code HTML, CSS, JS; các file Media, Hình ảnh, Âm thanh, Video) được gọn gàng, dễ dàng phát triển, thuận lợi trong làm việc nhóm.
- Có nhiều cách tạo cấu trúc thư mục dự án, sau đây là gợi ý về cách tổ chức Source code.
- Tạo cấu trúc thư mục dự án theo đề nghị như sau:
```
lesson1-tao-bo-cuc-su-dung-bootstrap/        <- Thư mục gốc của dự án
+---assets/                                  <- Thư mục chứa các file Css, Js, Image, Video, ...
|   \---img/                                 <- Thư mục chứa các ảnh dùng cho Trang web  
|   \---video/                               <- Thư mục chứa các file video dùng cho Trang web
|   \---css/                                 <- Thư mục chứa các file CSS do chúng ta tự viết
|   \---js/                                  <- Thư mục chứa các file JS do chúng ta tự viết
\---vendor/                                  <- Thư mục chứa các thư viện (library) do các nhà cung cấp (vendor) / bên thứ 3 (3rd party)
    +---bootstrap/                           <- Thư viện Bootstrap
    |   +---css/
    |   \---js/
    \---jquery/                              <- Thư viện JQuery
\---index.html                               <- File sẽ được chạy đầu tiên khi truy cập vào Trang web, thường đặt tên là index (hay còn gọi là Trang chủ)
```

## Step 2: Tích hợp thư viện Bootstrap vào Trang web
### Liên kết CSS của Bootstrap
- Cần liên kết file CSS của Bootstrap `bootstrap.min.css` trong phần thẻ `<head>...</head>` của Trang web.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Bootstrap lesson 2</title>

    <!-- Liên kết CSS Bootstrap -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" type="text/css" rel="stylesheet" />

    <!-- Liên kết CSS do chúng ta tự viết (custom CSS) -->
    <link href="assets/css/app.css" type="text/css" rel="stylesheet" />

</head>
...

```

### Liên kết JS của Bootstrap
- Cú pháp Javascript của Boostrap được viết phụ thuộc vào JQUERY, do đó: chúng ta cần liên kết thư viện JQuery trước, sau đó sẽ liên kết thư viện Bootstrap
- Các file Javascript nên được nhúng (include) vào trước khi đóng thẻ `</body>` để tăng hiệu suất khi load trang web.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    ...
</head>
<body>
    ...

    <!-- Liên kết Jquery -->
    <script src="vendor/jquery/jquery.min.js"></script>

    <!-- Liên kết Bootstrap -->
    <script src="vendor/bootstrap/js/bootstrap.js"></script>

    <!-- Liên kết JS do chúng ta tự viết (custom JS) -->
    <script src="assets/js/app.js"></script>
</body>
```