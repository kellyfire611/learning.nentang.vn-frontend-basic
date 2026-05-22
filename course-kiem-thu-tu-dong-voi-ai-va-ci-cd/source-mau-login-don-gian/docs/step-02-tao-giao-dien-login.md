# Step 2 - Tạo giao diện login

## Mục tiêu
- Dựng được một form login đơn giản nhưng đủ để test.
- Tạo sẵn các điểm bám (`id`, `data-testid`) để code JS và test dễ truy cập.

## Những gì cần có trên giao diện
1. Ô nhập email
2. Ô nhập mật khẩu
3. Checkbox ghi nhớ đăng nhập
4. Nút đăng nhập
5. Vùng hiển thị thông báo
6. Vùng hiển thị số lượt thử và trạng thái đăng nhập
7. Panel phiên đăng nhập với nút đăng xuất

## File cần tạo hoặc hoàn thiện
- `index.html`
- `styles/main.css`

## HTML cốt lõi cần có

```html
<form id="login-form" class="login-form" novalidate>
  <label>
    Email
    <input id="email-input" type="email" autocomplete="username" placeholder="student@example.com" />
  </label>

  <label>
    Mật khẩu
    <input id="password-input" type="password" autocomplete="current-password" placeholder="123456" />
  </label>

  <label class="checkbox-row">
    <input id="remember-input" type="checkbox" />
    Ghi nhớ đăng nhập
  </label>

  <button id="login-button" type="submit" data-testid="login-submit">Đăng nhập</button>
</form>

<p id="message" class="message" data-testid="message"></p>

<dd data-testid="attempts-count">0</dd>
<dd data-testid="auth-status">Chưa đăng nhập</dd>

<section id="session-card" hidden data-testid="session-panel">
  <button id="logout-button" type="button" data-testid="logout-button">Đăng xuất</button>
</section>
```

## Vì sao phải có `data-testid`
- E2E test cần selector ổn định, không phụ thuộc CSS hay text quá nhiều.
- Khi sửa giao diện, test ít bị gãy hơn.

## Những lỗi học viên hay gặp ở bước này
1. Quên `type="submit"` cho nút đăng nhập
2. Quên `hidden` ở panel phiên đăng nhập
3. Quên `data-testid` nên E2E test khó viết
4. Dùng class để test thay vì selector ổn định

## Tự kiểm tra sau bước này
1. Mở `index.html` qua local server
2. Kiểm tra đủ các ô nhập và nút
3. Kiểm tra panel đăng nhập đang ẩn lúc ban đầu

## Kết quả mong đợi
- Giao diện hiển thị được đầy đủ form login
- Chưa cần xử lý logic, chỉ cần phần nhìn và các điểm bám test đã đúng