#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo lại Module 1 bài 13-30 với đầy đủ nội dung tiếng Việt"""
import os, pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-01-html-co-ban")

def tpl(n, title, short, desc, req_items, know_items, code):
    reqs = "\n          ".join(f"<li>{r}</li>" for r in req_items)
    knows = "\n          ".join(f"<li>{k}</li>" for k in know_items)
    code_esc = code.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="keywords" content="Nền tảng,HTML,CSS,JavaScript,Lập trình,Web,Kiến thức,Đồ án">
  <meta name="author" content="Dương Nguyễn Phú Cường">
  <meta name="description" content="{short}">
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Bài {n:02d} – {title} | NenTang.vn">
  <meta property="og:description" content="{short}">
  <meta property="og:url" content="https://nentang.vn/">
  <meta property="og:site_name" content="Nền tảng Kiến thức">
  <title>Bài {n:02d} – {title} | NenTang.vn</title>
  <link rel="stylesheet" href="../../shared.css" />
</head>
<body>
  <div class="page-header module-1">
    <div class="breadcrumb">
      <a href="../../index.html">Trang Chủ</a> &rsaquo;
      <a href="../index.html">Module 1</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 1 – HTML Cơ Bản</p>
  </div>

  <div class="exercise-page">
    <div class="exercise-box">
      <div class="ex-head">
        <h1>📝 Yêu cầu bài tập</h1>
        <p>{short}</p>
      </div>
      <div class="ex-desc">
        <h3>Mô tả</h3>
        <p>{desc}</p>
        <h3>Yêu cầu</h3>
        <ul>
          {reqs}
        </ul>
        <h3>🧠 Kiến thức cần nhớ</h3>
        <ul>
          {knows}
        </ul>
      </div>
      <div class="ex-work">
        <h3>💻 Code mẫu</h3>
        <div id="code-highlight">
          <pre id="code-raw" style="display:none">{code_esc}</pre>
        </div>
      </div>
    </div>
  </div>
  <a href="../index.html" class="btn-back" style="margin-top:20px;">&#8592; Quay lại</a>
  <script type="module">
    import {{ codeToHtml }} from 'https://esm.sh/shiki@1';
    const raw = document.getElementById('code-raw').textContent;
    const highlighted = await codeToHtml(raw, {{ lang: 'html', theme: 'github-dark' }});
    document.getElementById('code-highlight').innerHTML = highlighted;
    const pre = document.getElementById('code-highlight').querySelector('pre');
    if (pre) pre.style.cssText = 'border-radius:10px;padding:20px;font-size:0.87rem;overflow-x:auto;margin:0;line-height:1.7';
  </script>
</body>
</html>"""

exercises = [
  (13, "Bảng HTML cơ bản (table)",
   "Tạo bảng thời khóa biểu bằng thẻ table, tr, th, td.",
   "Bảng HTML là cách hiển thị dữ liệu dạng hàng và cột. "
   "Bảng rất hữu ích để trình bày thời khóa biểu, bảng điểm, danh sách sản phẩm.",
   ["Tạo bảng thời khóa biểu 1 tuần (6 cột: Tiết 1-5, 5 hàng Thứ 2-6)",
    "Hàng đầu dùng thẻ <code>&lt;th&gt;</code> làm tiêu đề",
    "Thêm thuộc tính <code>border='1'</code> để nhìn rõ ô",
    "Dùng CSS đơn giản tô màu hàng tiêu đề"],
   ["<code>&lt;table&gt;</code>: tạo bảng; <code>&lt;tr&gt;</code>: tạo hàng (table row)",
    "<code>&lt;th&gt;</code>: ô tiêu đề (in đậm, canh giữa mặc định)",
    "<code>&lt;td&gt;</code>: ô dữ liệu thông thường",
    "<code>border-collapse: collapse</code> trong CSS để gộp viền ô"],
   """<table border="1" style="border-collapse:collapse; width:100%">
  <tr style="background:#3182ce; color:white">
    <th>Tiết</th>
    <th>Thứ Hai</th>
    <th>Thứ Ba</th>
    <th>Thứ Tư</th>
    <th>Thứ Năm</th>
    <th>Thứ Sáu</th>
  </tr>
  <tr>
    <td>1</td><td>Toán</td><td>Văn</td><td>Lý</td><td>Hóa</td><td>Sinh</td>
  </tr>
  <tr>
    <td>2</td><td>Anh</td><td>Sử</td><td>Địa</td><td>Toán</td><td>Văn</td>
  </tr>
</table>"""),

  (14, "Bảng nâng cao với thead tbody tfoot",
   "Tạo bảng điểm học sinh có phân chia đầu–thân–chân rõ ràng.",
   "Các thẻ <thead>, <tbody>, <tfoot> giúp tổ chức bảng hợp lý, hỗ trợ "
   "accessibility, CSS dễ tùy chỉnh, và khi in ấn đầu/chân bảng tự lặp lại.",
   ["Tạo bảng điểm 5 môn học, 5 học sinh",
    "Dùng <code>&lt;thead&gt;</code> chứa hàng tiêu đề",
    "Dùng <code>&lt;tbody&gt;</code> chứa dữ liệu học sinh",
    "Dùng <code>&lt;tfoot&gt;</code> hiển thị điểm trung bình lớp"],
   ["<code>&lt;thead&gt;</code>: đầu bảng – thường chứa <th>",
    "<code>&lt;tbody&gt;</code>: thân bảng – dữ liệu chính",
    "<code>&lt;tfoot&gt;</code>: chân bảng – tổng kết, chú thích",
    "CSS selector <code>thead tr</code>, <code>tbody tr:nth-child(even)</code> để tô màu xen kẽ"],
   """<table border="1" style="border-collapse:collapse; width:100%">
  <thead>
    <tr style="background:#2d3748; color:white">
      <th>Họ tên</th><th>Toán</th><th>Văn</th><th>Anh</th><th>TB</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Nguyễn Văn An</td><td>9</td><td>8</td><td>9.5</td><td><b>8.8</b></td></tr>
    <tr><td>Trần Thị Mai</td><td>7</td><td>8.5</td><td>8</td><td><b>7.8</b></td></tr>
  </tbody>
  <tfoot>
    <tr style="background:#ebf8ff">
      <td colspan="4"><b>Điểm TB toàn lớp</b></td>
      <td><b>8.3</b></td>
    </tr>
  </tfoot>
</table>"""),

  (15, "Colspan và Rowspan trong bảng",
   "Dùng colspan và rowspan để gộp ô trong bảng HTML.",
   "colspan gộp nhiều cột thành một ô, rowspan gộp nhiều hàng thành một ô. "
   "Tính năng quan trọng để tạo bảng phức tạp như lịch, biểu mẫu.",
   ["Tạo bảng thời khóa biểu có tiết học kéo dài 2 tiết (rowspan=\"2\")",
    "Gộp ô tiêu đề 'Buổi Sáng' qua 3 cột dùng colspan=\"3\"",
    "Thêm ô 'Nghỉ' kéo dài 2 hàng và 2 cột"],
   ["<code>colspan=\"n\"</code>: ô chiếm n cột liên tiếp",
    "<code>rowspan=\"n\"</code>: ô chiếm n hàng liên tiếp",
    "Phải xóa bớt các ô &lt;td&gt; bị gộp, tránh bảng bị lệch",
    "Kết hợp colspan + rowspan cẩn thận, đếm đúng số ô"],
   """<table border="1" style="border-collapse:collapse; width:100%; text-align:center">
  <tr>
    <th rowspan="2">Tiết</th>
    <th colspan="3">Buổi Sáng</th>
    <th colspan="2">Buổi Chiều</th>
  </tr>
  <tr>
    <th>Thứ 2</th><th>Thứ 3</th><th>Thứ 4</th>
    <th>Thứ 5</th><th>Thứ 6</th>
  </tr>
  <tr>
    <td>1</td><td>Toán</td>
    <td rowspan="2" style="background:#fed7d7">Nghỉ</td>
    <td>Lý</td><td>Hóa</td><td>Sinh</td>
  </tr>
  <tr>
    <td>2</td><td>Văn</td>
    <td>Địa</td><td>Toán</td><td>Anh</td>
  </tr>
</table>"""),

  (16, "Ký tự đặc biệt HTML Entities",
   "Hiển thị đúng các ký tự đặc biệt trong HTML bằng HTML entities.",
   "Một số ký tự như <, >, &, ©, ™ cần dùng entities để tránh trình duyệt "
   "hiểu nhầm là mã HTML. Entities bắt đầu bằng & và kết thúc bằng ;",
   ["Tạo bảng liệt kê 10 entities phổ biến: &amp;, &lt;, &gt;, &copy;, &#169;, &nbsp;, &hearts;",
    "Tạo đoạn văn có chứa ký hiệu toán học: ≤, ≥, ±, ×, ÷",
    "Hiển thị đoạn code HTML bằng entities thay vì thẻ thực"],
   ["<code>&amp;lt;</code> → &lt; | <code>&amp;gt;</code> → &gt; | <code>&amp;amp;</code> → &amp;",
    "<code>&amp;copy;</code> → © | <code>&amp;reg;</code> → ® | <code>&amp;trade;</code> → ™",
    "<code>&amp;nbsp;</code>: khoảng trắng không ngắt dòng (non-breaking space)",
    "Có thể dùng mã số: <code>&amp;#169;</code> = © | <code>&amp;#9829;</code> = ♥"],
   """<!-- Ký tự đặc biệt thường dùng -->
<p>&lt;p&gt; là thẻ đoạn văn trong HTML</p>
<p>5 &lt; 10 và 20 &gt; 15</p>
<p>Công thức: a&sup2; + b&sup2; = c&sup2;</p>
<p>Bản quyền &copy; 2024 Công ty ABC</p>
<p>Giá: 500&nbsp;000&nbsp;đ (dùng &amp;nbsp; tránh ngắt số)</p>
<p>Ký hiệu: &hearts; &clubs; &diams; &spades;</p>
<p>Toán học: 2&times;3&divide;6&plusmn;1 &le; 2 &ge; 0</p>"""),

  (17, "Thẻ pre và code",
   "Hiển thị đoạn code máy tính đúng định dạng bằng thẻ pre và code.",
   "Thẻ <pre> giữ nguyên khoảng trắng và xuống dòng. "
   "Thẻ <code> dùng font monospace để hiển thị code inline. "
   "Kết hợp cả hai để tạo block code có định dạng đẹp.",
   ["Dùng <code>&lt;pre&gt;&lt;code&gt;</code> để hiển thị đoạn HTML code",
    "Dùng <code>&lt;code&gt;</code> inline trong đoạn văn",
    "Dùng <code>&lt;kbd&gt;</code> cho tổ hợp phím như Ctrl+C",
    "Dùng <code>&lt;samp&gt;</code> cho output máy tính"],
   ["<code>&lt;pre&gt;</code>: preformatted – giữ nguyên space và newline",
    "<code>&lt;code&gt;</code>: inline code – font monospace",
    "<code>&lt;kbd&gt;</code>: keyboard input (tổ hợp phím)",
    "<code>&lt;samp&gt;</code>: sample output (kết quả chương trình)",
    "Kết hợp pre + code cho code block nhiều dòng"],
   """<p>Dùng thẻ <code>&lt;p&gt;</code> để tạo đoạn văn.</p>

<p>Nhấn <kbd>Ctrl</kbd> + <kbd>C</kbd> để sao chép.</p>

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="vi"&gt;
&lt;head&gt;
  &lt;title&gt;Trang đầu tiên&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Xin chào!&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>

<p>Kết quả: <samp>Hello, World!</samp></p>"""),

  (18, "Form đăng nhập cơ bản",
   "Tạo form đăng nhập với email và mật khẩu.",
   "Form HTML cho phép người dùng nhập và gửi dữ liệu. "
   "Form đăng nhập là form phổ biến nhất, bao gồm trường email/tên đăng nhập và mật khẩu.",
   ["Tạo form với action và method",
    "Thẻ <code>&lt;label&gt;</code> liên kết với from input (dùng for và id)",
    "Input type='email' và type='password'",
    "Nút Submit với giá trị 'Đăng nhập'",
    "Thêm placeholder và required cho các trường"],
   ["<code>&lt;form action='' method='post'&gt;</code>: tạo form",
    "<code>&lt;label for='id'&gt;</code>: nhãn liên kết với input cùng id",
    "<code>type='email'</code>: tự validate định dạng email",
    "<code>type='password'</code>: ẩn ký tự nhập",
    "<code>required</code>: bắt buộc nhập trước khi submit"],
   """<form action="#" method="post" style="max-width:400px; margin:auto; padding:24px; background:#f7fafc; border-radius:12px">
  <h2 style="text-align:center; color:#2d3748">Đăng nhập</h2>

  <div style="margin-bottom:16px">
    <label for="email" style="display:block; font-weight:bold; margin-bottom:6px">Email</label>
    <input type="email" id="email" name="email"
           placeholder="ten@email.com" required
           style="width:100%; padding:10px; border:1px solid #cbd5e0; border-radius:6px; font-size:15px">
  </div>

  <div style="margin-bottom:20px">
    <label for="pass" style="display:block; font-weight:bold; margin-bottom:6px">Mật khẩu</label>
    <input type="password" id="pass" name="password"
           placeholder="Nhập mật khẩu" required
           style="width:100%; padding:10px; border:1px solid #cbd5e0; border-radius:6px; font-size:15px">
  </div>

  <button type="submit"
          style="width:100%; padding:12px; background:#3182ce; color:white; border:none; border-radius:8px; font-size:16px; cursor:pointer">
    Đăng nhập
  </button>
</form>"""),

  (19, "Radio Button và Checkbox",
   "Tạo form khảo sát dùng radio button và checkbox.",
   "Radio button cho phép chọn MỘT trong nhiều lựa chọn. "
   "Checkbox cho phép chọn NHIỀU lựa chọn cùng lúc. "
   "Cả hai đều cần attribute name để nhóm lại.",
   ["Tạo nhóm radio chọn giới tính (Nam/Nữ/Khác)",
    "Tạo nhóm radio chọn trình độ học vấn",
    "Tạo nhóm checkbox chọn sở thích (ít nhất 5 lựa chọn)",
    "Dùng <code>fieldset</code> và <code>legend</code> để nhóm trường"],
   ["Radio: cùng <code>name</code> → chỉ chọn được 1 lựa chọn",
    "Checkbox: cùng <code>name</code> → chọn được nhiều lựa chọn",
    "<code>value</code>: giá trị gửi lên server khi chọn",
    "<code>checked</code>: mặc định được chọn sẵn",
    "<code>&lt;fieldset&gt;</code> + <code>&lt;legend&gt;</code> nhóm các input liên quan"],
   """<form>
  <fieldset>
    <legend>Giới tính</legend>
    <label><input type="radio" name="gioitinh" value="nam"> Nam</label>
    <label><input type="radio" name="gioitinh" value="nu"> Nữ</label>
    <label><input type="radio" name="gioitinh" value="khac"> Khác</label>
  </fieldset>

  <fieldset style="margin-top:16px">
    <legend>Sở thích (chọn nhiều)</legend>
    <label><input type="checkbox" name="sothich" value="doc"> 📚 Đọc sách</label><br>
    <label><input type="checkbox" name="sothich" value="nhac" checked> 🎵 Nghe nhạc</label><br>
    <label><input type="checkbox" name="sothich" value="game"> 🎮 Chơi game</label><br>
    <label><input type="checkbox" name="sothich" value="du-lich"> ✈️ Du lịch</label><br>
    <label><input type="checkbox" name="sothich" value="nau-an"> 🍳 Nấu ăn</label>
  </fieldset>

  <button type="submit" style="margin-top:12px; padding:8px 20px">Gửi khảo sát</button>
</form>"""),

  (20, "Select Dropdown và Textarea",
   "Tạo form liên hệ với dropdown chọn chủ đề và textarea nhập nội dung.",
   "Thẻ <select> tạo danh sách dropdown để chọn một hoặc nhiều tùy chọn. "
   "Thẻ <textarea> cho phép nhập đoạn văn bản nhiều dòng.",
   ["Tạo dropdown chọn chủ đề liên hệ (Hỗ trợ/Khiếu nại/Góp ý/Khác)",
    "Thêm <code>&lt;optgroup&gt;</code> nhóm các tùy chọn",
    "Tạo textarea 5 hàng nhập nội dung tin nhắn",
    "Tạo select multiple chọn nhiều quốc gia yêu thích"],
   ["<code>&lt;select&gt;&lt;option&gt;</code>: dropdown chọn 1",
    "<code>&lt;select multiple&gt;</code>: giữ Ctrl/Cmd để chọn nhiều",
    "<code>&lt;optgroup label=''&gt;</code>: nhóm các option",
    "<code>&lt;textarea rows='' cols=''&gt;</code>: ô nhập nhiều dòng",
    "Textarea không phải self-closing, nội dung mặc định đặt giữa thẻ mở/đóng"],
   """<!-- Dropdown đơn -->
<label for="topic">Chủ đề:</label>
<select id="topic" name="topic">
  <optgroup label="Hỗ trợ">
    <option value="billing">Thanh toán</option>
    <option value="technical">Kỹ thuật</option>
  </optgroup>
  <optgroup label="Phản hồi">
    <option value="feedback">Góp ý</option>
    <option value="complaint">Khiếu nại</option>
  </optgroup>
</select>

<!-- Dropdown nhiều lựa chọn -->
<label for="country">Quốc gia yêu thích (Ctrl+click):</label>
<select id="country" name="country" multiple size="4">
  <option>Việt Nam</option>
  <option>Nhật Bản</option>
  <option>Hàn Quốc</option>
  <option>Pháp</option>
</select>

<!-- Textarea -->
<label for="msg">Nội dung:</label>
<textarea id="msg" name="message" rows="5" cols="40"
          placeholder="Nhập tin nhắn của bạn..."></textarea>"""),

  (21, "HTML5 Input Types mới",
   "Khám phá các kiểu input mới trong HTML5 như number, range, color, date.",
   "HTML5 bổ sung nhiều kiểu input hữu ích giúp trải nghiệm người dùng tốt hơn "
   "và giảm bớt nhu cầu dùng JavaScript cho validate cơ bản.",
   ["Tạo input type='date' chọn ngày sinh",
    "Tạo input type='time' chọn giờ hẹn",
    "Tạo type='range' (thanh kéo) điều chỉnh âm lượng 0-100",
    "Tạo type='color' chọn màu yêu thích",
    "Tạo type='number' nhập tuổi min=1 max=120"],
   ["<code>type='date'</code>: hiện date picker",
    "<code>type='time'</code>: hiện time picker",
    "<code>type='range' min max step</code>: thanh trượt",
    "<code>type='color'</code>: bảng chọn màu",
    "<code>type='number' min max step</code>: nhập số có nút +/-",
    "<code>type='search'</code>: ô tìm kiếm có nút X"],
   """<form style="max-width:400px">
  <p>
    <label>Ngày sinh: <input type="date" name="ngaysinh"></label>
  </p>
  <p>
    <label>Giờ hẹn: <input type="time" name="giohim" min="08:00" max="18:00"></label>
  </p>
  <p>
    <label>Âm lượng: <input type="range" min="0" max="100" value="50" oninput="this.nextElementSibling.value=this.value">
    <output>50</output></label>
  </p>
  <p>
    <label>Màu yêu thích: <input type="color" value="#3182ce"></label>
  </p>
  <p>
    <label>Tuổi: <input type="number" min="1" max="120" placeholder="Nhập tuổi"></label>
  </p>
  <p>
    <label>Tìm kiếm: <input type="search" placeholder="Tìm..."></label>
  </p>
</form>"""),

  (22, "Validate form HTML5",
   "Dùng thuộc tính HTML5 để validate form tự động mà không cần JavaScript.",
   "HTML5 cung cấp các thuộc tính validate mạnh mẽ: required, pattern, min, max, "
   "minlength, maxlength. Trình duyệt sẽ hiển thị thông báo lỗi tự động.",
   ["Tạo form đăng ký với các trường: tên (minlength=2), email (required), "
    "SĐT (pattern), tuổi (min=18 max=100), mật khẩu (minlength=8)",
    "Thêm thuộc tính <code>novalidate</code> để tắt validate thử nghiệm",
    "Dùng CSS <code>:valid</code> và <code>:invalid</code> để tô màu trường"],
   ["<code>required</code>: bắt buộc nhập",
    "<code>minlength='n'</code> / <code>maxlength='n'</code>: giới hạn độ dài",
    "<code>pattern='regex'</code>: kiểm tra định dạng bằng regex",
    "<code>min</code> / <code>max</code>: giới hạn giá trị số/ngày",
    "CSS <code>input:valid { border-color: green }</code>"],
   """<style>
  input:valid { border: 2px solid #48bb78; }
  input:invalid { border: 2px solid #fc8181; }
  input:placeholder-shown { border: 2px solid #cbd5e0; }
</style>
<form style="max-width:400px">
  <p>
    <label>Họ tên (ít nhất 2 ký tự):
      <input type="text" minlength="2" required placeholder="Nguyễn Văn A">
    </label>
  </p>
  <p>
    <label>Email:
      <input type="email" required placeholder="ten@email.com">
    </label>
  </p>
  <p>
    <label>Số điện thoại (10 số):
      <input type="tel" pattern="[0-9]{10}" placeholder="0987654321">
    </label>
  </p>
  <p>
    <label>Tuổi (18-100):
      <input type="number" min="18" max="100">
    </label>
  </p>
  <button type="submit">Đăng ký</button>
</form>"""),

  (23, "Thẻ figure và figcaption",
   "Dùng figure và figcaption để thêm chú thích cho hình ảnh.",
   "Thẻ <figure> bọc nội dung độc lập (hình ảnh, code, biểu đồ). "
   "<figcaption> thêm chú thích mô tả. Giúp HTML semantic và SEO tốt hơn.",
   ["Tạo thư viện ảnh 4 ảnh mỗi ảnh có figcaption",
    "Dùng CSS tạo caption xuất hiện khi hover",
    "Bọc đoạn code bằng figure + figcaption 'Ví dụ code Python'",
    "Tạo hình ảnh có caption bên dưới căn giữa"],
   ["<code>&lt;figure&gt;</code>: bọc nội dung độc lập (ảnh, code, biểu đồ)",
    "<code>&lt;figcaption&gt;</code>: chú thích – đặt trước hoặc sau nội dung",
    "figure + figcaption tốt hơn img + p vì ngữ nghĩa rõ ràng",
    "Hỗ trợ accessibility: screen reader đọc caption liên quan đến hình",
    "Có thể chứa nhiều hình ảnh trong 1 figure"],
   """<figure style="text-align:center; max-width:400px; margin:auto">
  <img src="https://picsum.photos/400/250?random=1"
       alt="Phong cảnh thiên nhiên" style="width:100%; border-radius:8px">
  <figcaption style="margin-top:8px; color:#718096; font-style:italic">
    Hình 1: Phong cảnh thiên nhiên tuyệt đẹp
  </figcaption>
</figure>

<figure style="background:#1a202c; padding:16px; border-radius:8px; margin-top:20px">
  <pre><code style="color:#e2e8f0">print("Xin chào, Việt Nam!")</code></pre>
  <figcaption style="color:#a0aec0; margin-top:8px">
    Đoạn code Python in lời chào
  </figcaption>
</figure>"""),

  (24, "Thẻ Semantic HTML5",
   "Xây dựng trang web dùng các thẻ semantic HTML5 thay thế div thuần túy.",
   "HTML5 giới thiệu các thẻ có ý nghĩa ngữ nghĩa rõ ràng như header, nav, main, "
   "article, aside, section, footer. Giúp SEO, accessibility, code dễ đọc hơn.",
   ["Tạo layout trang web đầy đủ dùng các thẻ semantic",
    "header chứa logo và nav",
    "main chứa article (bài viết chính) và aside (thanh bên)",
    "footer chứa thông tin liên hệ"],
   ["<code>&lt;header&gt;</code>: phần đầu trang/bài viết",
    "<code>&lt;nav&gt;</code>: menu điều hướng",
    "<code>&lt;main&gt;</code>: nội dung chính (chỉ dùng 1 lần/trang)",
    "<code>&lt;article&gt;</code>: nội dung độc lập (bài báo, bài blog)",
    "<code>&lt;aside&gt;</code>: nội dung phụ (sidebar, quảng cáo)",
    "<code>&lt;section&gt;</code>: nhóm nội dung liên quan có heading",
    "<code>&lt;footer&gt;</code>: chân trang"],
   """<!DOCTYPE html>
<html lang="vi">
<body>
  <header>
    <h1>🌐 Logo Website</h1>
    <nav>
      <a href="#">Trang chủ</a> |
      <a href="#">Sản phẩm</a> |
      <a href="#">Liên hệ</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Bài viết: HTML Semantic</h2>
      <section>
        <h3>Giới thiệu</h3>
        <p>HTML semantic giúp máy đọc hiểu cấu trúc trang...</p>
      </section>
      <section>
        <h3>Ưu điểm</h3>
        <p>Tốt cho SEO, dễ đọc code, hỗ trợ accessibility...</p>
      </section>
    </article>
    <aside>
      <h3>Bài viết liên quan</h3>
      <ul>
        <li><a href="#">CSS Flexbox</a></li>
        <li><a href="#">JavaScript Cơ bản</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2024 Website của tôi. Liên hệ: info@example.com</p>
  </footer>
</body>
</html>"""),

  (25, "Meta tags và SEO cơ bản",
   "Thêm các meta tag quan trọng để SEO và hiển thị đúng trên mạng xã hội.",
   "Meta tags nằm trong <head> cung cấp thông tin về trang cho máy tìm kiếm "
   "và mạng xã hội. Các meta tag Open Graph giúp trang hiển thị đẹp khi chia sẻ.",
   ["Tạo trang HTML đầy đủ meta: charset, viewport, description, keywords, author",
    "Thêm Open Graph (og:title, og:description, og:image) cho Facebook",
    "Thêm Twitter Card meta tags",
    "Thêm canonical URL và robots meta tag"],
   ["<code>&lt;meta name='description'&gt;</code>: mô tả hiện trong Google (150-160 ký tự)",
    "<code>&lt;meta name='viewport'&gt;</code>: bắt buộc cho responsive",
    "<code>og:title, og:description, og:image</code>: hiển thị khi share Facebook",
    "<code>twitter:card</code>: hiển thị khi share Twitter/X",
    "Canonical URL tránh nội dung trùng lặp"],
   """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO cơ bản -->
  <title>Học HTML CSS JavaScript - Nền Tảng</title>
  <meta name="description" content="Khóa học HTML, CSS, JavaScript từ cơ bản đến nâng cao. 150+ bài tập thực hành.">
  <meta name="keywords" content="học HTML, học CSS, học JavaScript, lập trình web">
  <meta name="author" content="Nền Tảng">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://nentang.vn/course">

  <!-- Open Graph (Facebook, Zalo) -->
  <meta property="og:title" content="Học Web - Nền Tảng">
  <meta property="og:description" content="Học lập trình web từ đầu, có bài tập thực hành.">
  <meta property="og:image" content="https://nentang.vn/og-image.jpg">
  <meta property="og:url" content="https://nentang.vn/course">
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Học Web - Nền Tảng">
  <meta name="twitter:image" content="https://nentang.vn/og-image.jpg">
</head>"""),

  (26, "Nhúng nội dung với Iframe",
   "Dùng thẻ iframe để nhúng trang web khác, bản đồ, video YouTube vào trang.",
   "Iframe (Inline Frame) cho phép hiển thị một trang web khác bên trong trang hiện tại. "
   "Rất hay dùng để nhúng Google Maps, video YouTube, tài liệu PDF.",
   ["Nhúng video YouTube (dùng embed URL)",
    "Nhúng Google Maps vị trí Hà Nội",
    "Nhúng trang Wikipedia tiếng Việt",
    "Thêm sandbox attribute cho iframe không đáng tin"],
   ["<code>&lt;iframe src='' width='' height=''&gt;</code>: nhúng nội dung",
    "YouTube embed URL: <code>https://www.youtube.com/embed/VIDEO_ID</code>",
    "<code>allowfullscreen</code>: cho phép toàn màn hình",
    "<code>sandbox</code>: giới hạn quyền của iframe (bảo mật)",
    "<code>loading='lazy'</code>: chỉ tải khi gần đến viewport"],
   """<!-- Nhúng video YouTube -->
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  title="YouTube video"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media"
  allowfullscreen
  loading="lazy">
</iframe>

<!-- Nhúng Google Maps -->
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3723.8!2d105.85!3d21.028!..."
  width="600" height="400"
  style="border:0; border-radius:8px"
  allowfullscreen=""
  loading="lazy">
</iframe>"""),

  (27, "Thẻ Audio – Phát âm thanh",
   "Dùng thẻ audio để nhúng và phát file âm thanh trên trang web.",
   "HTML5 cung cấp thẻ <audio> giúp nhúng âm thanh trực tiếp vào trang mà không cần plugin. "
   "Hỗ trợ nhiều định dạng: MP3, OGG, WAV.",
   ["Tạo audio player với controls hiển thị",
    "Thêm nhiều source (MP3 + OGG) để tương thích trình duyệt",
    "Thêm các thuộc tính: autoplay, loop, muted, preload",
    "Tạo playlist mini với JavaScript điều khiển src"],
   ["<code>&lt;audio controls&gt;</code>: hiển thị thanh điều khiển mặc định",
    "<code>&lt;source src='' type='audio/mpeg'&gt;</code>: file MP3",
    "<code>autoplay</code>: tự phát (cần muted mới hoạt động trên Chrome)",
    "<code>loop</code>: phát lặp lại | <code>muted</code>: tắt tiếng ban đầu",
    "<code>preload='auto|metadata|none'</code>: kiểm soát tải trước"],
   """<!-- Audio player cơ bản -->
<audio controls style="width:100%; margin:10px 0">
  <source src="nhac.mp3" type="audio/mpeg">
  <source src="nhac.ogg" type="audio/ogg">
  Trình duyệt của bạn không hỗ trợ audio.
</audio>

<!-- Audio tự phát, tắt tiếng, lặp lại -->
<audio autoplay muted loop>
  <source src="nhac-nen.mp3" type="audio/mpeg">
</audio>

<!-- Playlist mini với JavaScript -->
<div>
  <audio id="player" controls src="bai1.mp3"></audio>
  <br>
  <button onclick="document.getElementById('player').src='bai1.mp3'">🎵 Bài 1</button>
  <button onclick="document.getElementById('player').src='bai2.mp3'">🎵 Bài 2</button>
  <button onclick="document.getElementById('player').src='bai3.mp3'">🎵 Bài 3</button>
</div>"""),

  (28, "Thẻ Video – Phát video",
   "Dùng thẻ video để nhúng và phát file video HTML5 trên trang web.",
   "Thẻ <video> trong HTML5 cho phép phát video trực tiếp. Hỗ trợ MP4, WebM, OGG. "
   "Có thể thêm poster (ảnh thumbnail), track phụ đề (subtitles).",
   ["Tạo video player đầy đủ với controls",
    "Thêm poster thumbnail hiển thị trước khi play",
    "Thêm track phụ đề WebVTT cho video",
    "Dùng CSS làm video full-width responsive"],
   ["<code>&lt;video controls width='' height=''&gt;</code>: player cơ bản",
    "<code>poster='thumb.jpg'</code>: ảnh hiển thị trước khi play",
    "<code>&lt;source&gt;</code>: cung cấp nhiều định dạng khác nhau",
    "<code>&lt;track kind='subtitles' src='sub.vtt'&gt;</code>: phụ đề",
    "CSS: <code>video { width:100%; height:auto }</code> để responsive"],
   """<!-- Video player cơ bản -->
<video controls width="640" height="360"
       poster="thumbnail.jpg"
       style="width:100%; border-radius:8px; background:#000">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="subtitles" src="phu-de.vtt" srclang="vi" label="Tiếng Việt">
  Trình duyệt không hỗ trợ video HTML5.
</video>

<!-- Responsive video wrapper -->
<style>
  .video-wrapper {
    position: relative;
    padding-bottom: 56.25%; /* tỉ lệ 16:9 */
    height: 0;
    overflow: hidden;
  }
  .video-wrapper video {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
  }
</style>
<div class="video-wrapper">
  <video controls src="video.mp4"></video>
</div>"""),

  (29, "Dự án: Trang giỏ hàng bằng Table",
   "Xây dựng trang giỏ hàng hoàn chỉnh bằng table HTML với tổng tiền.",
   "Dự án thực tế kết hợp kiến thức bảng HTML, form, entities và style cơ bản. "
   "Trang giỏ hàng thường gặp trong các trang thương mại điện tử.",
   ["Tạo bảng giỏ hàng với cột: STT, Sản phẩm, Đơn giá, Số lượng (input), Thành tiền, Xóa",
    "Hàng cuối hiển thị Tổng cộng dùng colspan",
    "Nút 'Đặt hàng' bên dưới bảng",
    "Dùng CSS tô màu xen kẽ các hàng (zebra striping)"],
   ["Kết hợp table + form (input number trong td)",
    "Dùng colspan để gộp ô tổng cộng cuối bảng",
    "CSS <code>tr:nth-child(even)</code> tô hàng chẵn",
    "Dùng ký tự ✕ hoặc entity &amp;times; cho nút xóa",
    "Dùng <code>text-align:right</code> cho cột số tiền"],
   """<style>
  table { border-collapse:collapse; width:100% }
  th,td { border:1px solid #e2e8f0; padding:12px; text-align:left }
  th { background:#2d3748; color:white }
  tr:nth-child(even) { background:#f7fafc }
  .price { text-align:right; font-weight:bold; color:#2f855a }
  input[type=number] { width:60px; padding:4px; border:1px solid #cbd5e0; border-radius:4px }
  .btn-order { margin-top:16px; padding:12px 30px; background:#e53e3e; color:white; border:none; border-radius:8px; font-size:16px; cursor:pointer }
</style>
<h2>🛒 Giỏ hàng của bạn</h2>
<table>
  <thead>
    <tr><th>STT</th><th>Sản phẩm</th><th>Đơn giá</th><th>Số lượng</th><th>Thành tiền</th><th>Xóa</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td><td>Áo thun trắng</td><td class="price">150.000đ</td>
      <td><input type="number" value="2" min="1"></td>
      <td class="price">300.000đ</td><td><button>&times;</button></td>
    </tr>
    <tr>
      <td>2</td><td>Quần jean xanh</td><td class="price">350.000đ</td>
      <td><input type="number" value="1" min="1"></td>
      <td class="price">350.000đ</td><td><button>&times;</button></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="4" style="text-align:right; font-weight:bold">Tổng cộng:</td>
      <td class="price" style="font-size:1.2em">650.000đ</td>
      <td></td>
    </tr>
  </tfoot>
</table>
<button class="btn-order">Đặt hàng ngay &rarr;</button>"""),

  (30, "🏆 Dự án: Trang Portfolio cá nhân",
   "Xây dựng trang giới thiệu bản thân hoàn chỉnh bằng HTML thuần.",
   "Dự án cuối module tổng hợp TẤT CẢ kiến thức HTML đã học. "
   "Trang portfolio là trang web cá nhân để giới thiệu kỹ năng và kinh nghiệm với nhà tuyển dụng.",
   ["Header: ảnh đại diện, tên, chức danh, mạng xã hội",
    "Section 'Về tôi': đoạn giới thiệu + danh sách kỹ năng",
    "Section 'Dự án': bảng liệt kê dự án đã làm",
    "Section 'Liên hệ': form liên hệ đầy đủ",
    "Footer: thông tin bản quyền",
    "Dùng ĐÚNG các thẻ semantic: header, nav, main, section, article, footer"],
   ["Portfolio cần: ảnh chuyên nghiệp, mô tả ngắn gọn, dự án nổi bật, contact",
    "Dùng semantic HTML đúng cách: header, main, section, footer",
    "Alt text cho ảnh quan trọng cho SEO và accessibility",
    "Meta description mô tả bản thân ngắn gọn 160 ký tự",
    "Form liên hệ với validate HTML5"],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Nguyễn Văn A – Lập trình viên Web</title>
  <meta name="description" content="Lập trình viên Web với 2 năm kinh nghiệm HTML, CSS, JavaScript">
</head>
<body>
  <header>
    <img src="avatar.jpg" alt="Ảnh của tôi" width="100">
    <h1>Nguyễn Văn A</h1>
    <p>🖥️ Lập trình viên Web Junior</p>
    <nav>
      <a href="#gioi-thieu">Về tôi</a> |
      <a href="#du-an">Dự án</a> |
      <a href="#lien-he">Liên hệ</a>
    </nav>
  </header>

  <main>
    <section id="gioi-thieu">
      <h2>👋 Về tôi</h2>
      <p>Xin chào! Tôi là Văn A, sinh viên năm 3 ngành CNTT.
         Đam mê lập trình web và luôn muốn học hỏi công nghệ mới.</p>
      <h3>Kỹ năng</h3>
      <ul>
        <li>HTML5 &amp; CSS3</li>
        <li>JavaScript (ES6+)</li>
        <li>Bootstrap 5</li>
      </ul>
    </section>

    <section id="du-an">
      <h2>🚀 Dự án đã làm</h2>
      <table border="1">
        <tr><th>Dự án</th><th>Công nghệ</th><th>Link</th></tr>
        <tr><td>Web giới thiệu cafe</td><td>HTML, CSS</td><td><a href="#">Xem</a></td></tr>
        <tr><td>Todo List</td><td>JavaScript</td><td><a href="#">Xem</a></td></tr>
      </table>
    </section>

    <section id="lien-he">
      <h2>📧 Liên hệ</h2>
      <form>
        <p><label>Tên: <input type="text" required></label></p>
        <p><label>Email: <input type="email" required></label></p>
        <p><label>Tin nhắn:<br><textarea rows="4" cols="40"></textarea></label></p>
        <button type="submit">Gửi tin nhắn</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2024 Nguyễn Văn A. Tất cả quyền được bảo lưu.</p>
  </footer>
</body>
</html>"""),
]

count = 0
for num, title, short, desc, reqs, knows, code in exercises:
    folder = BASE / f"bai-{num:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    content = tpl(num, title, short, desc, reqs, knows, code)
    (folder / "index.html").write_text(content, encoding="utf-8")
    count += 1
    print(f"  ✓ bai-{num:02d}: {title}")

print(f"\nModule 1 bai-13~30: Đã tạo {count} file")
