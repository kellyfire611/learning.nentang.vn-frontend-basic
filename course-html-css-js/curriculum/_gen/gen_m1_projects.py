#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_m1_projects.py – Thêm 5 bài Đồ Án tổng hợp cho Module 1 (bai-31 đến bai-35)
Mỗi bài có mô tả đầy đủ + code skeleton mẫu để học viên làm theo.
"""
import pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-01-html-co-ban")

def tpl(n, title, short, desc, req_items, know_items, code):
    reqs  = "\n          ".join(f"<li>{r}</li>" for r in req_items)
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
    <p>Module 1 – HTML Cơ Bản &nbsp;|&nbsp; 🏆 Bài Đồ Án Tổng Hợp</p>
  </div>

  <div class="exercise-page">
    <div class="exercise-box">
      <div class="ex-head">
        <h1>🏆 Đồ Án: {title}</h1>
        <p>{short}</p>
      </div>
      <div class="ex-desc">
        <h3>Mô tả dự án</h3>
        <p>{desc}</p>
        <h3>📋 Yêu cầu chi tiết</h3>
        <ul>
          {reqs}
        </ul>
        <h3>🧠 Kiến thức tổng hợp áp dụng</h3>
        <ul>
          {knows}
        </ul>
      </div>
      <div class="ex-work">
        <h3>💻 Code Skeleton – Khung sườn ban đầu để bắt đầu</h3>
        <p style="color:#718096;font-size:0.88rem;margin-bottom:12px;">
          📌 Đây là khung HTML cơ bản. Bạn cần tự điền nội dung, thêm CSS inline hoặc thẻ &lt;style&gt; để hoàn thiện theo yêu cầu.
        </p>
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

projects = [

  # ── BÀI 31: TRANG BLOG CÁ NHÂN ────────────────────────────────────────────
  (31,
   "Đồ Án: Trang Blog Cá Nhân",
   "Xây dựng trang blog cá nhân hoàn chỉnh với danh sách bài viết, sidebar và phân trang.",
   """Trang blog là dự án thực tế giúp bạn tổng hợp toàn bộ kiến thức HTML: 
   cấu trúc semantic, danh sách, liên kết, hình ảnh, bảng và form. 
   Blog cần có layout 2 cột (nội dung chính + sidebar), các thẻ bài viết, 
   và form đăng ký nhận tin tức.""",
   [
     "Tạo header với logo, tên blog và nav điều hướng (Trang Chủ, Về tôi, Liên Hệ)",
     "Tạo layout 2 cột dùng thẻ &lt;main&gt; và &lt;aside&gt; (tỷ lệ 70/30)",
     "Trong main: liệt kê 3 bài viết, mỗi bài có ảnh thumbnail, tiêu đề h2, tóm tắt, ngày đăng, link <em>Đọc thêm</em>",
     "Trong aside: widget danh mục, widget bài viết mới nhất (dùng ul/li), widget tag cloud",
     "Thêm phân trang (1, 2, 3 ... Tiếp theo) ở dưới danh sách bài viết",
     "Tạo footer với bản quyền, liên kết mạng xã hội (dùng ký tự entity ✉ ✦)",
     "Thêm form đăng ký nhận bản tin (email input + button Subscribe)",
     "Áp dụng thẻ semantic: header, nav, main, article, section, aside, footer",
   ],
   [
     "Thẻ semantic: &lt;header&gt;, &lt;nav&gt;, &lt;main&gt;, &lt;article&gt;, &lt;section&gt;, &lt;aside&gt;, &lt;footer&gt;",
     "Cấu trúc &lt;article&gt;: có &lt;header&gt;, &lt;figure&gt;, &lt;p&gt;, &lt;footer&gt; bên trong",
     "Liên kết: &lt;a href&gt; điều hướng, target='_blank' mở tab mới",
     "&lt;time datetime='2025-01-15'&gt; cho ngày tháng semantic",
     "HTML entities: &amp;copy; cho ©, &amp;mdash; cho —",
     "Form: &lt;form&gt;, &lt;input type='email'&gt;, &lt;button&gt;",
   ],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog Của Tôi</title>
  <style>
    /* TODO: Thêm CSS của bạn vào đây */
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }

    /* Header */
    header { background: #2c3e50; color: white; padding: 16px 0; }
    nav a { color: white; margin: 0 12px; text-decoration: none; }

    /* Layout 2 cột */
    .layout { display: flex; gap: 32px; margin: 32px 0; }
    main   { flex: 7; }   /* 70% */
    aside  { flex: 3; }   /* 30% */

    /* TODO: Bạn tự thêm style cho article card, aside widget, footer... */
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="container">
      <h1>📝 Blog Lập Trình</h1>
      <nav>
        <a href="#">Trang Chủ</a>
        <a href="#">Về Tôi</a>
        <a href="#">Liên Hệ</a>
      </nav>
    </div>
  </header>

  <!-- BODY LAYOUT -->
  <div class="container layout">

    <!-- NỘI DUNG CHÍNH -->
    <main>
      <!-- TODO: Thêm 3 article bài viết vào đây -->
      <article>
        <header>
          <h2><a href="#">Tiêu đề bài viết 1</a></h2>
          <time datetime="2025-03-01">01/03/2025</time>
        </header>
        <figure>
          <img src="https://picsum.photos/600/200" alt="Ảnh minh họa" width="100%">
          <figcaption>Chú thích ảnh</figcaption>
        </figure>
        <p>Tóm tắt nội dung bài viết... Lorem ipsum dolor sit amet.</p>
        <a href="#">Đọc thêm &rarr;</a>
      </article>

      <!-- TODO: Thêm bài viết 2 và 3 tương tự -->

      <!-- Phân trang -->
      <nav aria-label="Phân trang">
        <a href="#">&laquo; Trước</a>
        <a href="#" aria-current="page">1</a>
        <a href="#">2</a>
        <a href="#">3</a>
        <a href="#">Tiếp &raquo;</a>
      </nav>
    </main>

    <!-- SIDEBAR -->
    <aside>
      <!-- Widget Danh Mục -->
      <section>
        <h3>Danh Mục</h3>
        <ul>
          <li><a href="#">HTML (12)</a></li>
          <li><a href="#">CSS (8)</a></li>
          <li><a href="#">JavaScript (15)</a></li>
        </ul>
      </section>

      <!-- Widget Tags -->
      <section>
        <h3>Tags</h3>
        <!-- TODO: Thêm các tag -->
      </section>

      <!-- Form đăng ký bản tin -->
      <section>
        <h3>&#128231; Nhận Bản Tin</h3>
        <form>
          <input type="email" placeholder="Email của bạn" required>
          <button type="submit">Đăng Ký</button>
        </form>
      </section>
    </aside>

  </div><!-- /.layout -->

  <!-- FOOTER -->
  <footer>
    <div class="container">
      <p>&copy; 2025 Blog Của Tôi. All rights reserved.</p>
      <!-- TODO: Thêm liên kết mạng xã hội -->
    </div>
  </footer>

</body>
</html>"""),

  # ── BÀI 32: TRANG CV / HỒ SƠ XIN VIỆC ────────────────────────────────────
  (32,
   "Đồ Án: Trang CV / Hồ Sơ Xin Việc",
   "Tạo trang CV trực tuyến chuyên nghiệp với đầy đủ thông tin cá nhân, kỹ năng và kinh nghiệm.",
   """CV trực tuyến (Web Resume) là trang web giới thiệu bản thân chuyên nghiệp. 
   Khác với bài Portfolio trước, CV tập trung vào cấu trúc dữ liệu: bảng thông tin, 
   danh sách kỹ năng, timeline kinh nghiệm dùng dl/dt/dd, và form liên hệ tuyển dụng.""",
   [
     "Tạo section thông tin cá nhân: ảnh đại diện (img), tên, chức danh, liên hệ (email, phone, LinkedIn)",
     "Section kỹ năng: dùng 2 danh sách (ul) – Hard Skills và Soft Skills",
     "Section kinh nghiệm làm việc: dùng &lt;dl&gt;/&lt;dt&gt;/&lt;dd&gt; hoặc &lt;article&gt; cho từng công việc",
     "Section học vấn: tên trường, chuyên ngành, năm tốt nghiệp",
     "Section dự án cá nhân: bảng (table) liệt kê tên dự án, công nghệ, link demo",
     "Section chứng chỉ: ordered list với năm và tên chứng chỉ",
     "Form liên hệ tuyển dụng: họ tên, email, vị trí ứng tuyển (select), tin nhắn (textarea), submit",
     "Dùng đúng thẻ semantic cho toàn bộ trang",
   ],
   [
     "&lt;address&gt; cho thông tin liên hệ (phone, email, address)",
     "&lt;dl&gt;/&lt;dt&gt;/&lt;dd&gt; rất phù hợp để diễn đạt cặp khóa-giá trị",
     "&lt;time datetime&gt; cho thời gian làm việc, tốt nghiệp",
     "&lt;table&gt; với thead/tbody/tfoot và colspan để tạo bảng dự án",
     "&lt;abbr title&gt; để viết tắt tên công nghệ (HTML, CSS, JS...)",
     "&lt;blockquote cite&gt; cho câu nhận xét / testimonial",
   ],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CV - Nguyễn Văn A | Lập Trình Viên Web</title>
  <style>
    body { font-family: 'Segoe UI', sans-serif; margin: 0; color: #333; }
    .page { max-width: 900px; margin: 30px auto; background: white; padding: 40px; box-shadow: 0 0 20px rgba(0,0,0,.1); }
    h2 { border-bottom: 2px solid #3498db; padding-bottom: 8px; color: #2c3e50; }
    /* TODO: Bổ sung thêm CSS */
  </style>
</head>
<body>
<div class="page">

  <!-- THÔNG TIN CÁ NHÂN -->
  <header style="display:flex; gap:24px; align-items:center; margin-bottom:32px;">
    <img src="https://i.pravatar.cc/120" alt="Ảnh đại diện" width="120" height="120"
         style="border-radius:50%; border:3px solid #3498db;">
    <div>
      <h1 style="margin:0">Nguyễn Văn A</h1>
      <p style="color:#3498db; font-size:1.1rem; margin:4px 0">Lập Trình Viên Web Front-End</p>
      <address>
        &#128231; <a href="mailto:a@email.com">a@email.com</a> &nbsp;|&nbsp;
        &#128222; 0912 345 678 &nbsp;|&nbsp;
        &#127968; Hà Nội, Việt Nam
      </address>
    </div>
  </header>

  <!-- KỸ NĂNG -->
  <section>
    <h2>🛠️ Kỹ Năng</h2>
    <div style="display:flex; gap:40px;">
      <div>
        <h3>Hard Skills</h3>
        <ul>
          <li>HTML5 / CSS3</li>
          <li>JavaScript (ES6+)</li>
          <!-- TODO: thêm kỹ năng -->
        </ul>
      </div>
      <div>
        <h3>Soft Skills</h3>
        <ul>
          <li>Làm việc nhóm</li>
          <!-- TODO: thêm kỹ năng -->
        </ul>
      </div>
    </div>
  </section>

  <!-- KINH NGHIỆM -->
  <section>
    <h2>💼 Kinh Nghiệm Làm Việc</h2>
    <dl>
      <dt><strong>Front-End Developer</strong> – Công ty ABC
        <time datetime="2023-06"> (06/2023</time> – Hiện tại)</dt>
      <dd>
        <ul>
          <li>Phát triển giao diện web bằng React và Next.js</li>
          <!-- TODO: thêm mô tả chi tiết -->
        </ul>
      </dd>
      <!-- TODO: Thêm kinh nghiệm trước đó -->
    </dl>
  </section>

  <!-- HỌC VẤN -->
  <section>
    <h2>🎓 Học Vấn</h2>
    <!-- TODO: Thêm thông tin học vấn dùng dl hoặc article -->
  </section>

  <!-- DỰ ÁN -->
  <section>
    <h2>🚀 Dự Án Cá Nhân</h2>
    <table border="1" style="width:100%; border-collapse:collapse;">
      <thead>
        <tr style="background:#3498db; color:white;">
          <th>Tên Dự Án</th><th>Công Nghệ</th><th>Link Demo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Portfolio Website</td>
          <td><abbr title="HyperText Markup Language">HTML</abbr>, CSS, JS</td>
          <td><a href="#" target="_blank">Xem demo</a></td>
        </tr>
        <!-- TODO: Thêm các dự án khác -->
      </tbody>
    </table>
  </section>

  <!-- FORM LIÊN HỆ TUYỂN DỤNG -->
  <section>
    <h2>📩 Liên Hệ Tuyển Dụng</h2>
    <form>
      <label>Họ và tên: <input type="text" required placeholder="Tên nhà tuyển dụng"></label><br><br>
      <label>Email: <input type="email" required placeholder="email@company.com"></label><br><br>
      <label>Vị trí ứng tuyển:
        <select name="position">
          <option value="">-- Chọn vị trí --</option>
          <option>Front-End Developer</option>
          <option>Full-Stack Developer</option>
          <option>UI/UX Designer</option>
        </select>
      </label><br><br>
      <label>Tin nhắn:<br>
        <textarea rows="4" cols="60" placeholder="Nội dung liên hệ..."></textarea>
      </label><br><br>
      <button type="submit">Gửi Liên Hệ</button>
    </form>
  </section>

</div>
</body>
</html>"""),

  # ── BÀI 33: TRANG MENU NHÀ HÀNG ───────────────────────────────────────────
  (33,
   "Đồ Án: Trang Menu Nhà Hàng",
   "Xây dựng trang thực đơn nhà hàng có phân loại món ăn, giá cả và form đặt bàn.",
   """Trang menu nhà hàng kết hợp nhiều loại nội dung phong phú: hình ảnh món ăn, 
   bảng thực đơn với giá, danh sách phân loại, và form đặt bàn trực tuyến. 
   Đây là loại trang thực tế rất phổ biến trong các dự án web thực tế.""",
   [
     "Header với tên nhà hàng, logo (emoji hoặc img), và nav (Thực Đơn, Về Chúng Tôi, Đặt Bàn)",
     "Section thực đơn dùng bảng: cột Món Ăn, Mô Tả, Giá. Dùng &lt;caption&gt; đặt tiêu đề bảng",
     "Phân loại bảng bằng &lt;thead&gt;/&lt;tbody&gt;, dùng colspan cho hàng nhóm (Khai Vị, Món Chính, Tráng Miệng)",
     "Mỗi món ăn có hình ảnh nhỏ (img trong td), tên, mô tả, và giá định dạng (120.000đ)",
     "Section giới thiệu nhà hàng dùng blockquote cho câu review của khách hàng",
     "Form đặt bàn: input họ tên, email, số điện thoại, ngày (date input), giờ (time input), số khách (number), yêu cầu thêm (textarea)",
     "Dùng fieldset và legend để nhóm các trường của form",
     "Footer với địa chỉ, giờ mở cửa dùng thẻ &lt;address&gt; và &lt;time&gt;",
   ],
   [
     "&lt;table&gt; phức tạp: caption, thead, tbody, tfoot, colspan để nhóm hàng",
     "&lt;blockquote cite='URL'&gt; cho review/trích dẫn",
     "&lt;fieldset&gt; và &lt;legend&gt; để nhóm form controls",
     "Input type='date', type='time', type='number', type='tel' trong HTML5",
     "&lt;figure&gt;/&lt;figcaption&gt; bọc hình ảnh trong table cell",
     "Currency formatting: dùng &amp;nbsp; cho dấu phân cách hàng nghìn nếu cần",
   ],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>&#127829; Nhà Hàng Bếp Việt – Thực Đơn</title>
  <style>
    body { font-family: Georgia, serif; margin: 0; background: #fdf6ec; }
    header { background: #8b1a1a; color: #ffd700; text-align: center; padding: 20px; }
    nav a { color: #ffd700; margin: 0 16px; text-decoration: none; font-weight: bold; }
    .container { max-width: 960px; margin: 0 auto; padding: 20px; }
    table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 8px rgba(0,0,0,.1); }
    th, td { border: 1px solid #ddd; padding: 10px 14px; }
    caption { font-size: 1.3rem; font-weight: bold; padding: 12px; background: #8b1a1a; color: white; }
    .group-row { background: #f4e4c1; font-weight: bold; font-style: italic; }
    .price { color: #c0392b; font-weight: bold; white-space: nowrap; }
    /* TODO: Thêm CSS cho form, blockquote, footer */
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <h1>&#127829; Bếp Việt</h1>
    <p>Ẩm thực truyền thống – Hương vị quê hương</p>
    <nav>
      <a href="#menu">Thực Đơn</a>
      <a href="#about">Về Chúng Tôi</a>
      <a href="#booking">Đặt Bàn</a>
    </nav>
  </header>

  <div class="container">

    <!-- THỰC ĐƠN -->
    <section id="menu">
      <table>
        <caption>&#127829; THỰC ĐƠN BẾP VIỆT 2025</caption>
        <thead>
          <tr>
            <th>Hình</th>
            <th>Tên Món</th>
            <th>Mô Tả</th>
            <th>Giá</th>
          </tr>
        </thead>
        <tbody>
          <!-- Nhóm Khai Vị -->
          <tr class="group-row">
            <td colspan="4">🥗 Khai Vị</td>
          </tr>
          <tr>
            <td><img src="https://picsum.photos/60/60?random=1" alt="Gỏi cuốn"></td>
            <td>Gỏi Cuốn Tôm Thịt</td>
            <td>Gỏi cuốn tươi kèm tương hoisin</td>
            <td class="price">45.000đ</td>
          </tr>
          <!-- TODO: Thêm khai vị khác -->

          <!-- Nhóm Món Chính -->
          <tr class="group-row">
            <td colspan="4">🍜 Món Chính</td>
          </tr>
          <tr>
            <td><img src="https://picsum.photos/60/60?random=2" alt="Phở bò"></td>
            <td>Phở Bò Tái Nạm</td>
            <td>Phở bò hầm xương 8 tiếng, rau sống đầy đủ</td>
            <td class="price">75.000đ</td>
          </tr>
          <!-- TODO: Thêm món chính khác -->

          <!-- Nhóm Tráng Miệng -->
          <tr class="group-row">
            <td colspan="4">🍮 Tráng Miệng</td>
          </tr>
          <!-- TODO: Thêm tráng miệng -->
        </tbody>
        <tfoot>
          <tr>
            <td colspan="4" style="text-align:center; font-style:italic;">
              Giá đã bao gồm VAT. Phụ thu 5% ngoài giờ hành chính.
            </td>
          </tr>
        </tfoot>
      </table>
    </section>

    <!-- REVIEW KHÁCH HÀNG -->
    <section id="about">
      <h2>💬 Khách Hàng Nói Gì?</h2>
      <blockquote cite="https://google.com/maps">
        <p>"Phở ở đây tuyệt vời! Nước dùng đậm đà, thịt mềm. Sẽ quay lại lần nữa."</p>
        <footer>— Nguyễn Văn A, <cite>Google Maps</cite></footer>
      </blockquote>
      <!-- TODO: Thêm review khác -->
    </section>

    <!-- FORM ĐẶT BÀN -->
    <section id="booking">
      <h2>📅 Đặt Bàn Trực Tuyến</h2>
      <form action="#" method="post">
        <fieldset>
          <legend>Thông Tin Khách Hàng</legend>
          <label>Họ và tên: <input type="text" name="name" required placeholder="Nguyễn Văn A"></label><br><br>
          <label>Email: <input type="email" name="email" required></label><br><br>
          <label>Điện thoại: <input type="tel" name="phone" placeholder="09xx xxx xxx"></label>
        </fieldset>
        <br>
        <fieldset>
          <legend>Thông Tin Đặt Bàn</legend>
          <label>Ngày: <input type="date" name="date" required min="2025-01-01"></label><br><br>
          <label>Giờ: <input type="time" name="time" required min="11:00" max="22:00"></label><br><br>
          <label>Số khách: <input type="number" name="guests" min="1" max="20" value="2"></label><br><br>
          <label>Yêu cầu thêm:<br>
            <textarea name="notes" rows="3" cols="40" placeholder="Bàn cạnh cửa sổ, sinh nhật..."></textarea>
          </label>
        </fieldset>
        <br>
        <button type="submit">&#128204; Đặt Bàn Ngay</button>
      </form>
    </section>

  </div>

  <!-- FOOTER -->
  <footer style="background:#8b1a1a; color:#ffd700; text-align:center; padding:20px; margin-top:40px;">
    <address>
      &#127968; 123 Đường Lê Lợi, Quận 1, TP.HCM<br>
      &#128222; 028 3456 7890 &nbsp;|&nbsp;
      &#128197; Mở cửa: <time>10:00</time> – <time>22:00</time> mỗi ngày
    </address>
    <p>&copy; 2025 Nhà Hàng Bếp Việt</p>
  </footer>

</body>
</html>"""),

  # ── BÀI 34: TRANG KHÓA HỌC TRỰC TUYẾN ────────────────────────────────────
  (34,
   "Đồ Án: Trang Khóa Học Trực Tuyến",
   "Xây dựng trang giới thiệu một khóa học lập trình với chương trình học, giảng viên và form đăng ký.",
   """Trang landing page khóa học trực tuyến là dạng trang web rất phổ biến trong 
   thực tế. Nó kết hợp nhiều dạng nội dung: danh sách bài học, bảng so sánh gói học, 
   phần câu hỏi thường gặp (FAQ) dùng dl, và form đăng ký học viên đầy đủ validators.""",
   [
     "Hero section: tiêu đề h1 hấp dẫn, mô tả ngắn, ảnh banner, 2 nút CTA (Đăng Ký Ngay / Xem Demo)",
     "Section 'Bạn sẽ học được gì': ul với ít nhất 8 mục lợi ích (dùng emoji ✅ trước mỗi mục)",
     "Section chương trình học: ol có thứ tự với các module, mỗi module có ul lồng liệt kê bài học",
     "Section giảng viên: ảnh + tên + tiêu đề + mô tả + danh sách thành tích",
     "Bảng so sánh 3 gói: Miễn Phí / Cơ Bản / Pro – dùng table với colspan, đánh dấu gói khuyến nghị",
     "FAQ section: dùng &lt;details&gt;/&lt;summary&gt; cho 5 câu hỏi thường gặp",
     "Form đăng ký học: input text, email, phone, select khóa học, radio chọn hình thức học, checkbox điều khoản",
     "Dùng &lt;progress&gt; hoặc &lt;meter&gt; để hiển thị mức độ lấp đầy khóa học",
   ],
   [
     "&lt;details&gt;/&lt;summary&gt;: phần tử HTML5 gốc tạo accordion không cần JS",
     "&lt;progress value='75' max='100'&gt;: thanh tiến trình native",
     "&lt;meter min='0' max='100' value='75'&gt;: đo lường trong phạm vi",
     "Table phức tạp: rowspan để gộp các ô trong cột đặc điểm giống nhau",
     "Radio group: các input cùng name='type' là một nhóm chọn 1",
     "Checkbox với required để bắt buộc đồng ý điều khoản",
     "&lt;kbd&gt; cho phím tắt bàn phím trong mô tả tính năng",
   ],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Khóa Học HTML &amp; CSS – Nền Tảng.vn</title>
  <style>
    body { font-family: 'Segoe UI', sans-serif; margin: 0; color: #333; }
    .container { max-width: 1000px; margin: 0 auto; padding: 20px; }
    .hero { background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 60px 20px; text-align: center; }
    .hero h1 { font-size: 2.2rem; margin-bottom: 16px; }
    .btn { display: inline-block; padding: 12px 28px; border-radius: 6px; text-decoration: none; font-weight: bold; margin: 8px; }
    .btn-primary { background: #f6ad55; color: #333; }
    .btn-outline { border: 2px solid white; color: white; }
    /* Giá gói */
    .pricing { display: flex; gap: 20px; margin: 20px 0; }
    .plan { background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 24px; flex: 1; text-align: center; }
    .plan.recommended { border-color: #667eea; position: relative; }
    /* FAQ */
    details { border: 1px solid #e2e8f0; border-radius: 8px; margin: 8px 0; }
    summary { padding: 12px 16px; cursor: pointer; font-weight: bold; }
    details p { padding: 0 16px 12px; }
    /* TODO: Thêm CSS của bạn */
  </style>
</head>
<body>

  <!-- HERO -->
  <section class="hero">
    <p style="font-size:1rem;opacity:.8;">&#127891; Khóa Học Trực Tuyến</p>
    <h1>Học HTML &amp; CSS Từ A đến Z<br>Làm Chủ Web Trong 30 Ngày</h1>
    <p>Hơn <strong>5.000 học viên</strong> đã tốt nghiệp &nbsp;|&nbsp;
       <meter min="0" max="100" value="82" title="82% chỗ đã đăng ký">82%</meter>
       <strong>82%</strong> chỗ đã đăng ký</p>
    <a href="#register" class="btn btn-primary">&#128640; Đăng Ký Ngay</a>
    <a href="#" class="btn btn-outline">&#9654; Xem Demo</a>
  </section>

  <div class="container">

    <!-- BẠN SẼ HỌC ĐƯỢC GÌ -->
    <section>
      <h2>✅ Bạn Sẽ Học Được Gì?</h2>
      <ul>
        <li>✅ Cấu trúc HTML5 semantic chuẩn</li>
        <li>✅ CSS3 đầy đủ: Box Model, Flexbox, Grid</li>
        <li>✅ Responsive Design – Trang web chạy mọi thiết bị</li>
        <li>✅ SEO cơ bản và tối ưu hiệu suất</li>
        <!-- TODO: Thêm ít nhất 4 mục nữa -->
      </ul>
    </section>

    <!-- CHƯƠNG TRÌNH HỌC -->
    <section>
      <h2>📚 Chương Trình Học</h2>
      <ol>
        <li>
          <strong>Module 1: HTML Cơ Bản</strong> (10 bài)
          <ul>
            <li>Bài 1: Cấu trúc trang HTML</li>
            <li>Bài 2: Thẻ tiêu đề và đoạn văn</li>
            <!-- TODO: Thêm bài học -->
          </ul>
        </li>
        <li>
          <strong>Module 2: CSS Styling</strong> (12 bài)
          <ul>
            <li>Bài 1: Inline, Internal, External CSS</li>
            <!-- TODO: Thêm bài học -->
          </ul>
        </li>
        <!-- TODO: Thêm module khác -->
      </ol>
    </section>

    <!-- BẢNG GIÁ -->
    <section>
      <h2>💰 Bảng Giá Khóa Học</h2>
      <div class="pricing">
        <div class="plan">
          <h3>Miễn Phí</h3>
          <p style="font-size:2rem;font-weight:bold;">0đ</p>
          <ul style="text-align:left;">
            <li>10 bài học đầu tiên</li>
            <li>Tài liệu PDF</li>
            <li style="color:#ccc;">❌ Chứng chỉ</li>
          </ul>
          <a href="#" class="btn btn-outline" style="border-color:#667eea;color:#667eea;">Bắt Đầu Miễn Phí</a>
        </div>
        <div class="plan recommended">
          <p style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);
             background:#667eea;color:white;padding:2px 12px;border-radius:20px;font-size:.8rem;">
             ⭐ Khuyến Nghị
          </p>
          <h3>Cơ Bản</h3>
          <p style="font-size:2rem;font-weight:bold;color:#667eea;">499.000đ</p>
          <ul style="text-align:left;">
            <li>Toàn bộ 60 bài học</li>
            <li>Tài liệu + Source Code</li>
            <li>✅ Chứng chỉ hoàn thành</li>
            <li>Hỗ trợ 3 tháng</li>
          </ul>
          <a href="#register" class="btn btn-primary">Đăng Ký Ngay</a>
        </div>
        <div class="plan">
          <h3>Pro</h3>
          <p style="font-size:2rem;font-weight:bold;">999.000đ</p>
          <ul style="text-align:left;">
            <li>Tất cả Cơ Bản</li>
            <li>✅ 1-1 Mentoring</li>
            <li>✅ Review Code</li>
            <li>Hỗ trợ 1 năm</li>
          </ul>
          <a href="#register" class="btn btn-outline" style="border-color:#333;color:#333;">Chọn Pro</a>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section>
      <h2>❓ Câu Hỏi Thường Gặp</h2>
      <details>
        <summary>Khóa học phù hợp với ai?</summary>
        <p>Phù hợp với người mới bắt đầu hoàn toàn, không cần kiến thức lập trình trước đó.</p>
      </details>
      <details>
        <summary>Học trực tuyến, tôi có thể học lúc nào?</summary>
        <p>Học mọi lúc mọi nơi, không có lịch cố định. Video lưu trữ vĩnh viễn.</p>
      </details>
      <!-- TODO: Thêm 3 câu hỏi nữa -->
    </section>

    <!-- FORM ĐĂNG KÝ -->
    <section id="register">
      <h2>📝 Đăng Ký Học Ngay</h2>
      <form action="#" method="post">
        <label>Họ và tên: <input type="text" name="name" required></label><br><br>
        <label>Email: <input type="email" name="email" required></label><br><br>
        <label>Số điện thoại: <input type="tel" name="phone"></label><br><br>
        <label>Khóa học:
          <select name="course" required>
            <option value="">-- Chọn gói học --</option>
            <option value="free">Miễn Phí</option>
            <option value="basic">Cơ Bản – 499.000đ</option>
            <option value="pro">Pro – 999.000đ</option>
          </select>
        </label><br><br>
        <p>Hình thức học:</p>
        <label><input type="radio" name="type" value="online" checked> Trực tuyến (Online)</label><br>
        <label><input type="radio" name="type" value="offline"> Tại trung tâm (Offline)</label><br><br>
        <label>
          <input type="checkbox" name="agree" required>
          Tôi đồng ý với <a href="#">Điều Khoản Sử Dụng</a>
        </label><br><br>
        <button type="submit">&#128640; Đăng Ký Ngay</button>
      </form>
    </section>

  </div>

  <footer style="background:#2d3748;color:#a0aec0;text-align:center;padding:20px;margin-top:40px;">
    <p>&copy; 2025 NenTang.vn &mdash; Nền Tảng Kiến Thức Lập Trình</p>
  </footer>

</body>
</html>"""),

  # ── BÀI 35: TỔNG HỢP – TRANG WEB BÁN SẢN PHẨM ───────────────────────────
  (35,
   "Đồ Án Tổng Hợp: Trang Web Bán Sản Phẩm",
   "Dự án cuối cùng: tạo hoàn chỉnh một trang bán hàng online từ header đến footer dùng thuần HTML.",
   """Đây là bài tập tổng hợp NÂNG CAO nhất của Module 1 – kết hợp TẤT CẢ kiến thức HTML đã học 
   để xây dựng một trang bán sản phẩm thực tế hoàn chỉnh. Trang sẽ bao gồm: header với 
   navigation và giỏ hàng, banner quảng cáo, lưới sản phẩm, bảng so sánh chi tiết, 
   phần đánh giá, và form thanh toán đầy đủ.""",
   [
     "Header sticky: logo, nav (Trang Chủ, Sản Phẩm, Khuyến Mãi), thanh tìm kiếm (input+button), icon giỏ hàng với badge số lượng",
     "Banner quảng cáo: img toàn chiều rộng với chú thích nổi bật dùng figure/figcaption",
     "Breadcrumb điều hướng: Trang Chủ › Điện Tử › Điện Thoại (dùng nav với aria-label='breadcrumb')",
     "Lưới sản phẩm: ít nhất 6 sản phẩm, mỗi sản phẩm có ảnh, badge (Mới / Sale), tên, giá cũ, giá mới, rating (★★★★☆), nút Thêm vào Giỏ",
     "Bảng so sánh chi tiết 3 sản phẩm: dùng table có thead/tbody, rowspan, đánh dấu cột nổi bật",
     "Section đánh giá: 3 review với tên người dùng, rating sao, ngày đăng, nội dung (dùng blockquote + cite)",
     "Form thanh toán đầy đủ với fieldset: thông tin giao hàng, chọn phương thức thanh toán (radio), nhập mã giảm giá",
     "Footer 4 cột: Về Chúng Tôi, Sản Phẩm (ul links), Hỗ Trợ (ul links), Liên Hệ (address + mạng xã hội)",
   ],
   [
     "Tổng hợp: header/nav/main/section/article/aside/footer + breadcrumb nav",
     "table nâng cao: caption, thead, tbody, tfoot, colspan, rowspan",
     "Form phức tạp: fieldset/legend, mixed input types, radio payment methods",
     "Hình ảnh: img với srcset cho responsive images, figure/figcaption",
     "Semantic markup cho e-commerce: aria-label, aria-current, data-* attributes",
     "&lt;del&gt; cho giá cũ gạch ngang, &lt;ins&gt; cho giá mới highlight",
     "Rating sao: dùng ký tự entity &#9733;&#9733;&#9733;&#9733;&#9734; (★★★★☆)",
   ],
   """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ShopTech – Mua Sắm Điện Tử Online</title>
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #f8f9fa; color: #333; }
    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

    /* HEADER */
    header { background: #1a202c; color: white; position: sticky; top: 0; z-index: 100; }
    .header-inner { display: flex; align-items: center; gap: 20px; padding: 12px 0; }
    .logo { font-size: 1.4rem; font-weight: bold; color: #f6ad55; text-decoration: none; }
    nav a { color: #e2e8f0; text-decoration: none; margin: 0 10px; }
    .search-bar { flex: 1; display: flex; }
    .search-bar input { flex: 1; padding: 8px 12px; border: none; border-radius: 4px 0 0 4px; }
    .search-bar button { padding: 8px 16px; background: #f6ad55; border: none; border-radius: 0 4px 4px 0; cursor: pointer; }
    .cart-icon { position: relative; color: white; text-decoration: none; font-size: 1.3rem; }
    .cart-badge { position: absolute; top: -8px; right: -8px; background: #e53e3e; color: white;
                  border-radius: 50%; width: 18px; height: 18px; font-size: .7rem; display: flex;
                  align-items: center; justify-content: center; }

    /* PRODUCT GRID */
    .product-grid { display: flex; flex-wrap: wrap; gap: 20px; }
    .product-card { background: white; border-radius: 10px; overflow: hidden; width: calc(33.33% - 14px);
                    box-shadow: 0 2px 8px rgba(0,0,0,.08); }
    .product-card img { width: 100%; height: 180px; object-fit: cover; }
    .card-body { padding: 14px; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: .75rem; margin-bottom: 8px; }
    .badge-new  { background: #48bb78; color: white; }
    .badge-sale { background: #e53e3e; color: white; }
    .price del  { color: #a0aec0; }
    .price ins  { color: #e53e3e; font-weight: bold; font-size: 1.1rem; text-decoration: none; }
    .rating     { color: #f6ad55; }
    .btn-cart   { background: #3182ce; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; width: 100%; margin-top: 10px; }

    /* COMPARISON TABLE */
    .compare-table { width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; }
    .compare-table th, .compare-table td { border: 1px solid #e2e8f0; padding: 12px; text-align: center; }
    .compare-table thead tr { background: #2d3748; color: white; }
    .compare-table .highlight { background: #ebf8ff; font-weight: bold; }

    /* REVIEWS */
    blockquote { border-left: 4px solid #3182ce; margin: 16px 0; padding: 12px 20px; background: white; border-radius: 0 8px 8px 0; }

    /* FOOTER */
    footer { background: #1a202c; color: #a0aec0; padding: 40px 0 20px; margin-top: 60px; }
    .footer-grid { display: flex; gap: 40px; }
    .footer-col { flex: 1; }
    .footer-col h4 { color: white; margin-bottom: 12px; }
    .footer-col ul { list-style: none; padding: 0; }
    .footer-col ul li { margin-bottom: 6px; }
    .footer-col a { color: #a0aec0; text-decoration: none; }

    /* TODO: Responsive, form, và các style khác */
  </style>
</head>
<body>

  <!-- ═══ HEADER ═══ -->
  <header>
    <div class="container header-inner">
      <a href="#" class="logo">&#9889; ShopTech</a>
      <nav>
        <a href="#">Trang Chủ</a>
        <a href="#products">Sản Phẩm</a>
        <a href="#">Khuyến Mãi</a>
      </nav>
      <div class="search-bar">
        <input type="search" placeholder="Tìm kiếm sản phẩm...">
        <button>&#128269;</button>
      </div>
      <a href="#" class="cart-icon">
        &#128722;
        <span class="cart-badge">3</span>
      </a>
    </div>
  </header>

  <div class="container">

    <!-- BANNER -->
    <figure style="margin: 24px 0;">
      <img src="https://picsum.photos/1200/300?random=99" alt="Sale tháng 3" style="width:100%;border-radius:12px;">
      <figcaption style="text-align:center;color:#718096;margin-top:8px;">
        &#127881; Sale tháng 3 – Giảm đến 50% tất cả sản phẩm điện tử
      </figcaption>
    </figure>

    <!-- BREADCRUMB -->
    <nav aria-label="Điều hướng breadcrumb" style="margin-bottom:24px;">
      <a href="#">Trang Chủ</a> ›
      <a href="#">Điện Tử</a> ›
      <span aria-current="page">Điện Thoại</span>
    </nav>

    <!-- LƯỚI SẢN PHẨM -->
    <section id="products">
      <h2>&#128241; Điện Thoại Nổi Bật</h2>
      <div class="product-grid">

        <!-- Sản phẩm 1 -->
        <article class="product-card">
          <img src="https://picsum.photos/300/180?random=1" alt="iPhone 15 Pro">
          <div class="card-body">
            <span class="badge badge-new">Mới</span>
            <h3 style="margin:0 0 8px;">iPhone 15 Pro</h3>
            <div class="price">
              <del>29.990.000đ</del>
              <ins>27.490.000đ</ins>
            </div>
            <div class="rating">&#9733;&#9733;&#9733;&#9733;&#9734; (128)</div>
            <button class="btn-cart">&#43; Thêm vào Giỏ</button>
          </div>
        </article>

        <!-- Sản phẩm 2 -->
        <article class="product-card">
          <img src="https://picsum.photos/300/180?random=2" alt="Samsung S24">
          <div class="card-body">
            <span class="badge badge-sale">-20%</span>
            <h3 style="margin:0 0 8px;">Samsung Galaxy S24</h3>
            <div class="price">
              <del>24.990.000đ</del>
              <ins>19.990.000đ</ins>
            </div>
            <div class="rating">&#9733;&#9733;&#9733;&#9733;&#9733; (256)</div>
            <button class="btn-cart">&#43; Thêm vào Giỏ</button>
          </div>
        </article>

        <!-- TODO: Thêm 4 sản phẩm nữa theo cấu trúc tương tự -->

      </div>
    </section>

    <!-- BẢNG SO SÁNH -->
    <section style="margin-top:40px;">
      <h2>&#128202; So Sánh Chi Tiết</h2>
      <table class="compare-table">
        <caption style="padding:12px;font-weight:bold;font-size:1.1rem;">So sánh 3 dòng điện thoại cao cấp</caption>
        <thead>
          <tr>
            <th>Thông Số</th>
            <th>iPhone 15 Pro</th>
            <th class="highlight">Samsung S24 ⭐</th>
            <th>Pixel 8 Pro</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Giá</strong></td>
            <td>27.490.000đ</td>
            <td class="highlight">19.990.000đ</td>
            <td>22.990.000đ</td>
          </tr>
          <tr>
            <td><strong>RAM</strong></td>
            <td>8 GB</td>
            <td class="highlight">12 GB</td>
            <td>12 GB</td>
          </tr>
          <tr>
            <td><strong>Camera</strong></td>
            <td>48MP + 12MP + 12MP</td>
            <td class="highlight">50MP + 10MP + 12MP</td>
            <td>50MP + 48MP + 48MP</td>
          </tr>
          <tr>
            <td><strong>Pin</strong></td>
            <td>3.274 mAh</td>
            <td class="highlight">4.000 mAh</td>
            <td>5.050 mAh</td>
          </tr>
          <!-- TODO: Thêm các thông số khác -->
        </tbody>
        <tfoot>
          <tr>
            <td colspan="4" style="font-style:italic;text-align:center;color:#718096;">
              Thông số có thể thay đổi theo phiên bản. Cập nhật: 03/2025.
            </td>
          </tr>
        </tfoot>
      </table>
    </section>

    <!-- ĐÁNH GIÁ KHÁCH HÀNG -->
    <section style="margin-top:40px;">
      <h2>&#9733; Đánh Giá Từ Khách Hàng</h2>
      <blockquote>
        <p><span style="color:#f6ad55;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
           "Mua Samsung S24 ở đây, giao hàng nhanh, máy zin 100%, rất hài lòng!"</p>
        <footer>— <cite>Nguyễn Minh Tuấn</cite>,
          <time datetime="2025-02-15">15/02/2025</time>
        </footer>
      </blockquote>
      <!-- TODO: Thêm 2 review nữa -->
    </section>

    <!-- FORM THANH TOÁN -->
    <section style="margin-top:40px;">
      <h2>&#128179; Thanh Toán</h2>
      <form action="#" method="post">

        <fieldset>
          <legend>Thông Tin Giao Hàng</legend>
          <label>Họ và tên: <input type="text" required placeholder="Nguyễn Văn A"></label><br><br>
          <label>Email: <input type="email" required></label><br><br>
          <label>Điện thoại: <input type="tel" required></label><br><br>
          <label>Địa chỉ giao hàng:<br>
            <textarea rows="3" style="width:100%;max-width:500px;" placeholder="Số nhà, đường, phường/xã, quận/huyện, tỉnh/thành"></textarea>
          </label>
        </fieldset>

        <br>
        <fieldset>
          <legend>Phương Thức Thanh Toán</legend>
          <label><input type="radio" name="payment" value="cod" checked> &#128230; Thanh toán khi nhận hàng (COD)</label><br>
          <label><input type="radio" name="payment" value="bank"> &#127968; Chuyển khoản ngân hàng</label><br>
          <label><input type="radio" name="payment" value="momo"> &#128136; Ví MoMo</label>
        </fieldset>

        <br>
        <fieldset>
          <legend>Mã Giảm Giá</legend>
          <input type="text" name="coupon" placeholder="Nhập mã giảm giá...">
          <button type="button">Áp Dụng</button>
        </fieldset>

        <br>
        <label>
          <input type="checkbox" name="agree" required>
          Tôi đồng ý với <a href="#">Điều Khoản</a> và <a href="#">Chính Sách Bảo Mật</a>
        </label>
        <br><br>
        <button type="submit" style="background:#e53e3e;color:white;padding:12px 32px;border:none;border-radius:8px;font-size:1rem;cursor:pointer;">
          &#128230; Đặt Hàng Ngay
        </button>

      </form>
    </section>

  </div><!-- /.container -->

  <!-- ═══ FOOTER ═══ -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>&#9889; ShopTech</h4>
          <p>Chuyên cung cấp thiết bị điện tử chính hãng, bảo hành toàn quốc.</p>
        </div>
        <div class="footer-col">
          <h4>Sản Phẩm</h4>
          <ul>
            <li><a href="#">Điện Thoại</a></li>
            <li><a href="#">Laptop</a></li>
            <li><a href="#">Phụ Kiện</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Hỗ Trợ</h4>
          <ul>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Chính Sách Đổi Trả</a></li>
            <li><a href="#">Bảo Hành</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Liên Hệ</h4>
          <address>
            &#128231; <a href="mailto:shop@shoptech.vn" style="color:#a0aec0;">shop@shoptech.vn</a><br>
            &#128222; 1800 1234 (Miễn phí)<br>
            &#127968; 456 Nguyễn Huệ, Q.1, TP.HCM
          </address>
        </div>
      </div>
      <hr style="border-color:#4a5568;margin:24px 0;">
      <p style="text-align:center;">&copy; 2025 ShopTech Vietnam. All rights reserved.</p>
    </div>
  </footer>

</body>
</html>"""),
]

print("Tạo các bài đồ án Module 1 (bai-31 đến bai-35)...")
for num, title, short, desc, reqs, knows, code in projects:
    folder = BASE / f"bai-{num:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    content = tpl(num, title, short, desc, reqs, knows, code)
    (folder / "index.html").write_text(content, encoding="utf-8")
    print(f"  ✓ bai-{num:02d}: {title}")

print(f"\nHoàn thành! Đã tạo {len(projects)} bài đồ án.")
