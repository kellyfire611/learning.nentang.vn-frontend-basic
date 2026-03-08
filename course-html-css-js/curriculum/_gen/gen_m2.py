#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo Module 2 – CSS Cơ Bản – 30 bài tập đầy đủ tiếng Việt"""
import os, pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-02-css-co-ban")

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
  <div class="page-header module-2">
    <div class="breadcrumb">
      <a href="../../index.html">Trang Chủ</a> &rsaquo;
      <a href="../index.html">Module 2</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 2 – CSS Cơ Bản</p>
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
  (1, "3 cách nhúng CSS vào HTML",
   "Thực hành nhúng CSS bằng inline, internal (style tag) và external (file .css).",
   "CSS có thể được áp dụng theo 3 cách: inline trực tiếp trên thẻ, internal trong thẻ &lt;style&gt; "
   "ở head, hoặc external link đến file .css. External được dùng phổ biến nhất vì tách biệt HTML và CSS.",
   ["Tạo 3 đoạn văn bản: mỗi đoạn dùng 1 cách CSS khác nhau",
    "Inline: tô màu đỏ trực tiếp trong thẻ &lt;p&gt;",
    "Internal: &lt;style&gt; trong &lt;head&gt; tô màu xanh",
    "External: link file style.css tô màu tím"],
   ["<code>style='color:red'</code>: inline – ưu tiên cao nhất nhưng khó bảo trì",
    "<code>&lt;style&gt;...&lt;/style&gt;</code>: internal – trong &lt;head&gt;",
    "<code>&lt;link rel='stylesheet' href='style.css'&gt;</code>: external – cách tốt nhất",
    "Thứ tự ưu tiên: Inline &gt; Internal/External (cái nào sau thắng)"],
   """<!-- 1. Inline CSS -->
<p style="color:red; font-size:18px">Tôi dùng Inline CSS</p>

<!-- 2. Internal CSS -->
<style>
  .internal { color: blue; font-weight: bold; }
</style>
<p class="internal">Tôi dùng Internal CSS</p>

<!-- 3. External CSS (tạo file style.css riêng) -->
<link rel="stylesheet" href="style.css">
<p class="external">Tôi dùng External CSS</p>
<!-- Trong style.css: .external { color: purple; } -->"""),

  (2, "CSS Selectors: tag, class, id",
   "Thực hành chọn phần tử HTML bằng selector tag, class và id.",
   "Selector là cách CSS 'chọn' phần tử cần tạo kiểu. "
   "Ba loại cơ bản: tag (tên thẻ), class (.ten-class) và id (#ten-id).",
   ["Tạo đoạn HTML với 5 thẻ p, h2, div",
    "Dùng tag selector tô màu tất cả thẻ p",
    "Dùng class selector tạo 3 màu nền khác nhau",
    "Dùng id selector style cho phần tử duy nhất",
    "Kết hợp nhiều selector với dấu phẩy"],
   ["<code>p { }</code>: chọn tất cả thẻ &lt;p&gt;",
    "<code>.ten-class { }</code>: chọn tất cả phần tử có class đó",
    "<code>#ten-id { }</code>: chọn phần tử có id đó (duy nhất)",
    "<code>h1, h2, h3 { }</code>: chọn nhiều loại cùng lúc",
    "ID có độ ưu tiên cao hơn class, class cao hơn tag"],
   """/* Tag selector */
p { color: #2d3748; line-height: 1.6; }
h2 { color: #2b6cb0; }

/* Class selector */
.highlight { background-color: #fef3cd; padding: 8px; border-radius: 4px; }
.success { color: #276749; background: #c6f6d5; padding: 8px; }
.danger { color: #9b2c2c; background: #fed7d7; padding: 8px; }

/* ID selector */
#tieu-de-chinh { font-size: 2rem; text-transform: uppercase; letter-spacing: 2px; }

/* Nhóm selector */
h1, h2, h3 { font-family: Georgia, serif; }"""),

  (3, "Advanced Selectors: con cháu, anh em",
   "Dùng CSS selectors kết hợp để chọn phần tử theo quan hệ trong DOM.",
   "Ngoài 3 selector cơ bản, CSS có nhiều selector kết hợp để chọn phần tử "
   "dựa trên vị trí và quan hệ với nhau trong cây DOM.",
   ["Dùng <code>div p</code> chọn p là con cháu của div",
    "Dùng <code>div &gt; p</code> chọn p là con TRỰC TIẾP của div",
    "Dùng <code>h2 + p</code> chọn p ngay sau h2 (adjacent sibling)",
    "Dùng <code>h2 ~ p</code> chọn tất cả p sau h2 (general sibling)",
    "Dùng attribute selector <code>a[href^='https']</code>"],
   ["<code>A B</code>: B là con cháu của A (bất kỳ cấp nào)",
    "<code>A &gt; B</code>: B là con TRỰC TIẾP của A",
    "<code>A + B</code>: B ngay kề sau A (cùng cấp)",
    "<code>A ~ B</code>: B ở sau A (cùng cấp, không nhất thiết liền kề)",
    "<code>[attr='value']</code>: chọn phần tử có thuộc tính xác định"],
   """/* Con cháu (descendant) */
.menu a { color: white; text-decoration: none; }

/* Con trực tiếp (child) */
.menu > li { display: inline-block; padding: 10px; }

/* Adjacent sibling */
h2 + p { font-size: 1.1rem; color: #4a5568; }

/* General sibling */
h2 ~ p { margin-left: 20px; }

/* Attribute selectors */
a[href^="https"] { color: green; } /* bắt đầu bằng https */
a[href$=".pdf"] { color: red; }    /* kết thúc bằng .pdf */
input[type="email"] { border: 2px solid blue; }
input[type="password"] { border: 2px solid orange; }"""),

  (4, "Màu sắc: HEX, RGB, HSL",
   "Sử dụng 3 cách biểu diễn màu trong CSS: HEX, RGB và HSL.",
   "CSS hỗ trợ nhiều cách khai báo màu. HEX phổ biến nhất, RGB cho phép "
   "điều chỉnh opacity (rgba), HSL trực quan hơn khi cần điều chỉnh sắc.",
   ["Tạo 5 ô màu: mỗi ô dùng 1 cú pháp màu khác nhau (tên, HEX, RGB, RGBA, HSL)",
    "Dùng RGBA tạo overlay trong suốt 50%",
    "Dùng HSL điều chỉnh sắc tối/sáng của cùng 1 màu (lightness 20%, 40%, 60%, 80%)"],
   ["Tên màu: <code>red, blue, tomato, cornflowerblue</code>... (140+ tên)",
    "HEX: <code>#RRGGBB</code> hoặc rút gọn <code>#RGB</code> (VD: #fff = #ffffff)",
    "RGB: <code>rgb(255, 0, 0)</code> – mỗi kênh 0-255",
    "RGBA: <code>rgba(0, 0, 0, 0.5)</code> – a: alpha 0 (trong) đến 1 (đục)",
    "HSL: <code>hsl(hue, saturation%, lightness%)</code> – dễ điều chỉnh tông màu"],
   """/* Tên màu */
.box1 { background: tomato; }

/* HEX – phổ biến nhất */
.box2 { background: #3182ce; }
.box3 { background: #fff; border: 1px solid #000; }

/* RGB */
.box4 { background: rgb(72, 187, 120); }

/* RGBA – có độ trong suốt */
.overlay { background: rgba(0, 0, 0, 0.5); }

/* HSL – dễ điều chỉnh */
.light { background: hsl(210, 80%, 80%); }
.normal { background: hsl(210, 80%, 55%); }
.dark { background: hsl(210, 80%, 30%); }

/* CSS hiện đại – oklch (Chrome 111+) */
.modern { background: oklch(0.6 0.2 240); }"""),

  (5, "Font chữ và Google Fonts",
   "Cài đặt font chữ tùy chỉnh bằng Google Fonts và font-family stack.",
   "Font mặc định của trình duyệt khá đơn giản. Google Fonts cung cấp hàng trăm "
   "font chữ đẹp miễn phí, nhúng dễ dàng qua link hoặc @import.",
   ["Nhúng 2 Google Font: Roboto (thân văn bản) và Playfair Display (tiêu đề)",
    "Đặt font fallback đúng cách: Roboto, sans-serif",
    "Áp dụng font khác nhau cho h1, h2 và p",
    "Thêm font chữ cho code bằng 'Fira Code', monospace"],
   ["<code>@import url('https://fonts.googleapis.com/css2?family=...')</code>",
    "Hoặc dùng &lt;link&gt; trong &lt;head&gt; – nhanh hơn @import",
    "<code>font-family: 'Tên Font', fallback, generic</code>",
    "Generic families: serif, sans-serif, monospace, cursive, fantasy",
    "Luôn khai báo fallback để tránh font mặc định xấu khi font không tải được"],
   """<!-- Trong HTML head -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto:wght@300;400;700&family=Fira+Code&display=swap" rel="stylesheet">

/* Trong CSS */
body {
  font-family: 'Roboto', Arial, sans-serif;
  font-weight: 400;
}

h1, h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-weight: 700;
}

code, pre {
  font-family: 'Fira Code', 'Courier New', monospace;
}"""),

  (6, "font-weight, font-style, text-transform",
   "Thực hành các thuộc tính định dạng văn bản cơ bản trong CSS.",
   "CSS cung cấp nhiều thuộc tính để định dạng chữ: độ đậm, nghiêng, "
   "chuyển đổi chữ hoa/thường, và trang trí gạch chân.",
   ["Tạo các đoạn văn với font-weight từ 100 đến 900",
    "Thực hành font-style: normal, italic, oblique",
    "Dùng text-transform: uppercase, lowercase, capitalize",
    "Dùng text-decoration: underline, overline, line-through, none"],
   ["<code>font-weight</code>: 100 (mỏng) đến 900 (đậm), hoặc bold/normal",
    "<code>font-style: italic</code>: nghiêng theo thiết kế font",
    "<code>font-style: oblique</code>: nghiêng bằng cách chuyển đổi cơ học",
    "<code>text-transform: uppercase</code>: IN HOA tất cả",
    "<code>text-decoration: underline dotted red</code>: gạch chân tùy chỉnh"],
   """/* font-weight */
.w100 { font-weight: 100; } /* Thin */
.w400 { font-weight: 400; } /* Normal */
.w700 { font-weight: 700; } /* Bold */
.w900 { font-weight: 900; } /* Black */

/* font-style */
.italic { font-style: italic; }
.oblique { font-style: oblique 15deg; }

/* text-transform */
.upper { text-transform: uppercase; }   /* VĂN BẢN */
.lower { text-transform: lowercase; }   /* văn bản */
.cap { text-transform: capitalize; }    /* Văn Bản */

/* text-decoration */
.underline { text-decoration: underline wavy red; }
.through { text-decoration: line-through; }
.no-underline a { text-decoration: none; } /* Bỏ gạch chân link */"""),

  (7, "text-align, line-height, letter-spacing",
   "Điều chỉnh căn lề, khoảng cách dòng và khoảng cách chữ cái.",
   "Những thuộc tính này ảnh hưởng trực tiếp đến khả năng đọc (readability) của văn bản. "
   "line-height tốt (1.5-1.8) và letter-spacing phù hợp giúp văn bản dễ đọc hơn nhiều.",
   ["Tạo 4 đoạn văn với 4 cách căn lề: left, center, right, justify",
    "So sánh line-height: 1.0, 1.5, 2.0 trên cùng đoạn văn",
    "Thêm letter-spacing cho tiêu đề: 0.1em đến 0.3em",
    "Dùng word-spacing điều chỉnh khoảng cách giữa các từ"],
   ["<code>text-align: left|center|right|justify</code>",
    "<code>line-height: 1.6</code>: không đơn vị – tốt nhất cho responsive",
    "<code>letter-spacing: 0.1em</code>: dùng em thay px để theo tỷ lệ font",
    "<code>word-spacing: 0.2em</code>: khoảng cách giữa từ",
    "Tiêu đề chữ hoa (uppercase) nên có letter-spacing rộng hơn"],
   """h1 {
  text-align: center;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.justify { text-align: justify; } /* Căn đều 2 bên */
.right { text-align: right; }

/* Khoảng cách dòng */
.tight { line-height: 1.2; }     /* Chật – tránh cho văn bản dài */
.normal { line-height: 1.6; }    /* Tốt cho body text */
.loose { line-height: 2.0; }     /* Thoáng – dùng cho trích dẫn */

/* Khoảng cách chữ */
.tracking-wide { letter-spacing: 0.2em; }
.tracking-tight { letter-spacing: -0.02em; } /* Chữ to, thu lại tí */

/* Khoảng cách từ */
.word-space { word-spacing: 0.3em; }"""),

  (8, "Box Model: margin padding border",
   "Hiểu và thực hành mô hình hộp CSS (Box Model) đầy đủ.",
   "Mọi phần tử HTML là một hộp chữ nhật gồm 4 lớp từ trong ra ngoài: "
   "content → padding → border → margin. Hiểu box model là THIẾT YẾU để làm layout.",
   ["Tạo div hiển thị rõ 4 phần: content (màu xanh), padding (màu vàng), border (đỏ), margin (xám)",
    "Thực hành shorthand: margin/padding với 1, 2, 3, 4 giá trị",
    "Dùng DevTools (F12) để kiểm tra box model"],
   ["<code>content</code>: nội dung thực tế (text, ảnh)",
    "<code>padding</code>: khoảng cách bên TRONG (giữa content và border)",
    "<code>border</code>: viền bao quanh padding",
    "<code>margin</code>: khoảng cách bên NGOÀI (giữa phần tử này và phần tử khác)",
    "Shorthand: <code>margin: top right bottom left</code> (clockwise)",
    "<code>margin: 10px 20px</code> = top&bottom:10px, left&right:20px"],
   """/* Box Model đầy đủ */
.box {
  width: 200px;
  height: 100px;         /* content */
  padding: 20px;         /* khoảng trong */
  border: 5px solid #e53e3e; /* viền */
  margin: 30px auto;     /* khoảng ngoài, căn giữa */
  background: #bee3f8;
}

/* Shorthand padding */
.p1 { padding: 20px; }             /* 4 phía = 20px */
.p2 { padding: 10px 20px; }        /* top-bottom: 10, left-right: 20 */
.p3 { padding: 10px 20px 15px; }   /* top: 10, lr: 20, bottom: 15 */
.p4 { padding: 10px 15px 20px 25px; } /* top right bottom left */

/* Margin auto để căn giữa block element */
.container { max-width: 800px; margin: 0 auto; }"""),

  (9, "box-sizing: border-box",
   "Hiểu sự khác biệt giữa content-box và border-box và tại sao nên dùng border-box.",
   "Mặc định CSS dùng content-box: width chỉ tính nội dung, padding và border được cộng thêm. "
   "border-box: width = tổng cả padding + border + content – trực quan hơn nhiều.",
   ["Tạo 2 div width:300px – một content-box, một border-box",
    "Thêm padding:20px và border:5px cho cả hai",
    "So sánh chiều rộng thực tế của 2 div",
    "Áp dụng box-sizing: border-box toàn trang bằng * selector"],
   ["<code>box-sizing: content-box</code>: mặc định – width + padding + border",
    "<code>box-sizing: border-box</code>: width đã BAO GỒM padding và border",
    "Best practice: <code>*, *::before, *::after { box-sizing: border-box; }</code>",
    "Với border-box: width: 300px + padding: 20px → content = 260px",
    "Với content-box: width: 300px + padding: 20px → tổng = 340px"],
   """/* Reset tốt nhất – áp dụng cho toàn dự án */
*, *::before, *::after {
  box-sizing: border-box;
}

/* So sánh content-box vs border-box */
.content-box {
  box-sizing: content-box; /* mặc định */
  width: 300px;
  padding: 20px;
  border: 5px solid red;
  /* Chiều rộng thực: 300 + 40 + 10 = 350px */
}

.border-box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 5px solid blue;
  /* Chiều rộng thực: 300px (không đổi!) */
  /* content = 300 - 40 - 10 = 250px */
}"""),

  (10, "Background: màu và hình ảnh",
   "Tạo các nền đẹp bằng màu sắc, hình ảnh và gradient trong CSS.",
   "Thuộc tính background trong CSS cực kỳ linh hoạt: có thể đặt màu, ảnh, "
   "lặp lại, định vị, điều chỉnh kích thước ảnh nền.",
   ["Đặt background-color bằng HEX, RGB và tên màu",
    "Đặt background-image từ URL picsum.photos",
    "Thực hành background-repeat: no-repeat, repeat-x, repeat-y",
    "Thực hành background-size: cover, contain, 50% 50%",
    "Thực hành background-position: center, top right"],
   ["<code>background-color: #hex</code>: màu nền",
    "<code>background-image: url('ảnh.jpg')</code>: ảnh nền",
    "<code>background-size: cover</code>: phủ đầy, giữ tỷ lệ (cắt nếu cần)",
    "<code>background-size: contain</code>: hiện toàn bộ ảnh (có thể trống)",
    "<code>background-position: center</code>: căn giữa ảnh nền",
    "Shorthand: <code>background: url() no-repeat center/cover</code>"],
   """/* Màu nền đơn giản */
.box1 { background-color: #3182ce; }

/* Ảnh nền cơ bản */
.box2 {
  background-image: url('https://picsum.photos/800/400');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 300px;
}

/* Nhiều lớp background (multiple backgrounds) */
.multi {
  background:
    url('overlay.png') no-repeat center,
    url('background.jpg') no-repeat center / cover;
}

/* Shorthand đầy đủ */
.hero {
  background: url('hero.jpg') no-repeat center center / cover;
  min-height: 80vh;
  color: white;
}"""),

  (11, "CSS Gradient: linear và radial",
   "Tạo nền gradient đẹp bằng linear-gradient và radial-gradient.",
   "Gradient là hiệu ứng chuyển màu mượt mà giữa 2 hoặc nhiều màu. "
   "CSS gradient không cần ảnh, giúp trang nhanh hơn và sắc nét hơn.",
   ["Tạo gradient ngang trái-phải: xanh → tím",
    "Tạo gradient chéo 45 độ: cam → hồng",
    "Tạo radial-gradient hình tròn từ trong ra ngoài",
    "Tạo gradient nhiều màu (rainbow effect)",
    "Tạo gradient với điểm dừng màu cụ thể (color stops)"],
   ["<code>linear-gradient(hướng, màu1, màu2)</code>",
    "Hướng: <code>to right, to bottom, 45deg, 135deg</code>",
    "<code>radial-gradient(shape, màu1, màu2)</code>",
    "Màu stop: <code>linear-gradient(red 0%, yellow 50%, green 100%)</code>",
    "Gradient là giá trị của <code>background-image</code> (không phải background-color)"],
   """/* Linear gradient cơ bản */
.g1 { background: linear-gradient(to right, #667eea, #764ba2); }
.g2 { background: linear-gradient(135deg, #f093fb, #f5576c); }
.g3 { background: linear-gradient(to bottom, #4facfe, #00f2fe); }

/* Radial gradient */
.r1 { background: radial-gradient(circle, #a8edea, #fed6e3); }
.r2 { background: radial-gradient(ellipse at top, #e0c3fc, #8ec5fc); }

/* Rainbow với nhiều màu */
.rainbow {
  background: linear-gradient(to right,
    red, orange, yellow, green, blue, indigo, violet
  );
}

/* Gradient với color stops cụ thể */
.sunset {
  background: linear-gradient(
    to bottom,
    #0f2027 0%,
    #203a43 40%,
    #2c5364 100%
  );
}"""),

  (12, "Border và border-radius",
   "Tạo viền đa dạng và bo góc các phần tử bằng CSS.",
   "Border và border-radius là hai thuộc tính cơ bản để tạo kiểu dáng cho box. "
   "Kết hợp đúng tạo ra button, card, avatar bo góc đẹp mắt.",
   ["Tạo border với đủ style: solid, dashed, dotted, double, groove",
    "Đặt màu viền khác nhau cho 4 cạnh",
    "Dùng border-radius: 8px tạo góc bo tròn đều",
    "Dùng border-radius: 50% tạo hình tròn từ div vuông",
    "Tạo avatar tròn từ ảnh bằng border-radius: 50%"],
   ["<code>border: 2px solid #color</code>: shorthand width style color",
    "Styles: solid, dashed, dotted, double, groove, ridge, inset, outset",
    "<code>border-radius: 8px</code>: bo 4 góc đều nhau",
    "<code>border-radius: 50%</code>: hình tròn hoàn hảo (cần width=height)",
    "<code>border-radius: 10px 20px 30px 40px</code>: bo từng góc khác nhau",
    "<code>border-top: 4px solid blue</code>: chỉ viền 1 cạnh"],
   """/* Các kiểu border */
.solid { border: 2px solid #3182ce; }
.dashed { border: 2px dashed #e53e3e; }
.dotted { border: 4px dotted #38a169; }
.double { border: 6px double #805ad5; }

/* Viền từng cạnh */
.accentbox {
  border-top: 4px solid #3182ce;
  border-left: 4px solid #3182ce;
  border-bottom: 1px solid #e2e8f0;
  border-right: 1px solid #e2e8f0;
}

/* Border radius */
.rounded { border-radius: 8px; }
.pill { border-radius: 9999px; }   /* dạng viên thuốc */
.circle { border-radius: 50%; }    /* hình tròn */

/* Avatar tròn */
.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 3px solid white;
  box-shadow: 0 0 0 2px #3182ce;
  object-fit: cover;
}"""),

  (13, "box-shadow và text-shadow",
   "Tạo bóng đổ cho box và văn bản bằng CSS shadow.",
   "Shadow (bóng đổ) tạo chiều sâu và nổi bật cho các phần tử, "
   "giúp UI trông chuyên nghiệp hơn. Có thể tạo nhiều lớp bóng.",
   ["Tạo card với box-shadow nhẹ nhàng",
    "Tạo button với bóng đổ thay đổi khi hover (hiệu ứng nổi)",
    "Tạo text-shadow cho tiêu đề hero",
    "Tạo inner shadow (inset) cho input filed"],
   ["<code>box-shadow: x y blur spread color</code>",
    "x: dịch ngang (dương: phải, âm: trái)",
    "y: dịch dọc (dương: xuống, âm: lên)",
    "blur: độ nhòe (0 = sắc nét)",
    "spread: độ lan rộng (âm: thu nhỏ)",
    "<code>inset</code>: bóng phía trong",
    "<code>text-shadow: x y blur color</code>: không có spread"],
   """/* Card shadow cơ bản */
.card {
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}

/* Hover nổi lên */
.button {
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s, transform 0.3s;
}
.button:hover {
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
  transform: translateY(-2px);
}

/* Nhiều lớp shadow */
.multi-shadow {
  box-shadow:
    0 1px 2px rgba(0,0,0,0.1),
    0 4px 8px rgba(0,0,0,0.1),
    0 16px 32px rgba(0,0,0,0.08);
}

/* Inset shadow (như input đang focus) */
.input-inset { box-shadow: inset 0 2px 4px rgba(0,0,0,0.15); }

/* Text shadow */
.hero-title { text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
.neon { text-shadow: 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #0ff; color: white; background: #000; }"""),

  (14, "opacity và RGBA",
   "Kiểm soát độ trong suốt của phần tử và màu sắc bằng opacity và RGBA.",
   "opacity áp dụng độ trong suốt cho TOÀN BỘ phần tử (kể cả nội dung). "
   "rgba() chỉ áp dụng cho màu đó, không ảnh hưởng nội dung bên trong.",
   ["Tạo ảnh nền với overlay bán trong suốt dùng rgba",
    "So sánh opacity: 0.5 trên parent vs rgba trên background-color",
    "Tạo hiệu ứng glass morphism: background rgba + backdrop-filter blur",
    "Tạo tooltip trong suốt xuất hiện khi hover"],
   ["<code>opacity: 0</code> (trong suốt) đến <code>opacity: 1</code> (đục hoàn toàn)",
    "<code>rgba(r, g, b, alpha)</code>: alpha 0-1 chỉ cho màu đó",
    "opacity ảnh hưởng toàn bộ gồm cả text, border, con cháu",
    "rgba chỉ ảnh hưởng màu background/border của phần tử đó",
    "<code>backdrop-filter: blur(10px)</code>: làm mờ nền phía sau (glass effect)"],
   """/* opacity – ảnh hưởng toàn phần tử */
.dim { opacity: 0.5; } /* Cả text lẫn nền đều bị mờ */

/* rgba – chỉ mờ màu nền */
.overlay {
  background: rgba(0, 0, 0, 0.6); /* nền đen 60% trong suốt */
  color: white; /* text vẫn rõ */
}

/* Glass morphism effect */
.glass {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 16px;
  padding: 24px;
}

/* Fade khi hover */
.fade { opacity: 1; transition: opacity 0.3s; }
.fade:hover { opacity: 0.7; }"""),

  (15, "Pseudo-class: hover focus active",
   "Dùng pseudo-class để tạo kiểu cho các trạng thái tương tác của phần tử.",
   "Pseudo-class chọn phần tử dựa trên TRẠNG THÁI của nó, không phải cấu trúc DOM. "
   "Dùng nhiều để tạo hiệu ứng tương tác như hover, focus, active.",
   ["Tạo menu với link đổi màu khi hover",
    "Tạo input đổi border khi focus",
    "Tạo button có hiệu ứng nhấn (active)",
    "Dùng :nth-child(even) tô màu dòng chẵn trong bảng",
    "Dùng :first-child và :last-child"],
   ["<code>:hover</code>: khi con trỏ chuột đang di đến",
    "<code>:focus</code>: khi phần tử được chọn (tab hoặc click input)",
    "<code>:active</code>: khoảnh khắc đang nhấn chuột",
    "<code>:visited</code>: link đã được truy cập",
    "<code>:nth-child(2n)</code>: chẵn | <code>:nth-child(2n+1)</code>: lẻ",
    "<code>:first-child</code>, <code>:last-child</code>, <code>:only-child</code>"],
   """/* Link states */
a { color: #3182ce; text-decoration: none; }
a:hover { color: #2c5282; text-decoration: underline; }
a:visited { color: #805ad5; }
a:active { color: #e53e3e; }

/* Input focus */
input {
  border: 2px solid #e2e8f0;
  outline: none;
  transition: border-color 0.2s;
}
input:focus { border-color: #3182ce; box-shadow: 0 0 0 3px rgba(49,130,206,0.3); }

/* Button active */
.btn:active { transform: scale(0.96); }

/* Zebra striping */
tr:nth-child(even) { background: #f7fafc; }
tr:nth-child(odd) { background: white; }
tr:hover { background: #ebf8ff; }

/* first/last child */
li:first-child { border-top: none; }
li:last-child { border-bottom: none; }"""),

  (16, "Pseudo-element: before after",
   "Dùng ::before và ::after để thêm nội dung trang trí vào phần tử.",
   "Pseudo-element tạo ra phần tử 'ảo' trước hoặc sau nội dung phần tử. "
   "Rất hữu ích để thêm icon, trang trí, hoặc hiệu ứng mà không cần HTML thêm.",
   ["Dùng ::before thêm icon 📍 trước mỗi item list",
    "Dùng ::after tạo dấu gạch chân animate cho link",
    "Tạo badge 'Mới' góc trên phải của card dùng ::before",
    "Dùng ::before tạo dấu ngoặc kép trích dẫn đẹp"],
   ["<code>::before</code> và <code>::after</code> tạo nội dung ảo",
    "PHẢI CÓ thuộc tính <code>content: ''</code> (có thể rỗng)",
    "Mặc định là inline, thường đặt thành <code>display:block</code> hoặc absolute",
    "Không xuất hiện trong DOM, không select được bằng JavaScript",
    "Rất hay dùng để trang trí icon, badge, underline effect, dấu chấm, dấu phẩy"],
   """/* List icon với ::before */
ul.custom li::before {
  content: "✅ ";
}

/* Gạch chân animate cho link */
.fancy-link {
  position: relative;
  text-decoration: none;
}
.fancy-link::after {
  content: '';
  position: absolute;
  bottom: -2px; left: 0;
  width: 0; height: 2px;
  background: currentColor;
  transition: width 0.3s;
}
.fancy-link:hover::after { width: 100%; }

/* Badge 'Mới' */
.card-new { position: relative; }
.card-new::before {
  content: 'Mới';
  position: absolute;
  top: -8px; right: -8px;
  background: #e53e3e;
  color: white;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 99px;
}

/* Dấu ngoặc kép trích dẫn */
blockquote::before { content: open-quote; font-size: 3em; color: #cbd5e0; }
blockquote::after { content: close-quote; }"""),

  (17, "CSS Specificity – Độ ưu tiên",
   "Hiểu quy tắc tính điểm độ ưu tiên CSS để debug style hiệu quả.",
   "Khi nhiều rule CSS cùng áp dụng cho một phần tử, trình duyệt dùng specificity "
   "(điểm ưu tiên) để quyết định rule nào thắng. Hiểu điều này giúp debug CSS dễ hơn.",
   ["Tạo ví dụ để thấy ID (100pts) thắng class (10pts) thắng tag (1pt)",
    "Thực hành kết hợp selector: .nav li a vs ul li a",
    "Hiểu khi nào dùng !important và tại sao nên tránh",
    "Dùng DevTools xem computed style và crossed-out declarations"],
   ["Điểm specificity: ID=100, Class/Pseudo-class/Attr=10, Tag/Pseudo-element=1",
    "<code>p</code> = 1 | <code>.class</code> = 10 | <code>#id</code> = 100",
    "<code>div.box p</code> = 1+10+1 = 12 | <code>#header .nav a</code> = 100+10+1 = 111",
    "<code>!important</code>: ghi đè tất cả (dùng khi thực sự cần thiết)",
    "Inline style = 1000 điểm, mạnh hơn tất cả selector"],
   """/* Specificity thấp đến cao */
p { color: gray; }               /* 1 pt  */
.text { color: blue; }           /* 10 pts */
p.text { color: green; }         /* 11 pts */
#main p { color: red; }          /* 101 pts */
#main p.text { color: purple; }  /* 111 pts */

/* Inline style (1000pts) – ghi đè tất cả rule CSS */
/* <p style="color:orange"> = thắng tất cả trên */

/* !important – mạnh nhất (tránh lạm dụng) */
.forced { color: pink !important; } /* thắng cả inline style */

/* Kỹ thuật tăng specificity không dùng !important */
.nav.nav li a { color: white; } /* .nav.nav = 20pts */
/* Thay vào đó hãy dùng selector rõ ràng hơn */"""),

  (18, "CSS Variables – Custom Properties",
   "Tạo và sử dụng biến CSS để quản lý màu sắc và giá trị nhất quán.",
   "CSS Custom Properties (biến CSS) cho phép định nghĩa giá trị 1 lần và dùng ở nhiều nơi. "
   "Dễ thay đổi toàn bộ theme chỉ bằng cách sửa 1 chỗ. Rất mạnh khi kết hợp với JavaScript.",
   ["Định nghĩa color palette trong :root (primary, secondary, accent, background, text)",
    "Tạo spacing system: --space-s, --space-m, --space-l",
    "Áp dụng variables cho button, card, navbar",
    "Dùng JavaScript thay đổi biến CSS để toggle dark mode"],
   ["Khai báo: <code>--ten-bien: gia-tri;</code> trong selector",
    "<code>:root { }</code>: scope toàn trang – dùng cho global variables",
    "Sử dụng: <code>var(--ten-bien)</code> hoặc <code>var(--ten-bien, fallback)</code>",
    "Variables kế thừa theo cascade, có thể override trong component",
    "JavaScript: <code>element.style.setProperty('--bien', 'gia-tri')</code>"],
   """:root {
  /* Color palette */
  --color-primary: #3182ce;
  --color-secondary: #805ad5;
  --color-accent: #ed8936;
  --color-bg: #f7fafc;
  --color-text: #2d3748;
  --color-text-light: #718096;

  /* Spacing */
  --space-xs: 4px;
  --space-s: 8px;
  --space-m: 16px;
  --space-l: 32px;
  --space-xl: 64px;

  /* Border */
  --radius: 8px;
  --radius-full: 9999px;
}

/* Dùng trong component */
.btn-primary {
  background: var(--color-primary);
  padding: var(--space-s) var(--space-m);
  border-radius: var(--radius);
}"""),

  (19, "Tạo Button đẹp với CSS",
   "Thiết kế các kiểu button chuyên nghiệp bằng CSS thuần.",
   "Button (nút bấm) là thành phần UI quan trọng nhất. Thiết kế button đẹp "
   "đòi hỏi kết hợp nhiều thuộc tính CSS và xử lý tốt các trạng thái.",
   ["Tạo 5 kiểu button: Primary, Secondary, Danger, Ghost, Icon button",
    "Thêm hover effect: đổi màu, nổi lên (translateY)",
    "Thêm active effect: nhấn xuống",
    "Tạo loading button với spinner CSS animation",
    "Tạo button group (dính liền nhau)"],
   ["Padding nên dùng em hoặc px: <code>padding: 0.6em 1.2em</code>",
    "<code>cursor: pointer</code>: thay đổi trỏ chuột khi hover",
    "<code>transition: all 0.2s</code>: animation mượt khi hover/active",
    "<code>transform: translateY(-2px)</code>: hiệu ứng nổi lên",
    "<code>disabled</code> state: <code>opacity:0.6; cursor:not-allowed</code>"],
   """.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border: 2px solid transparent;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn:active { transform: scale(0.96); }

.btn-primary { background: #3182ce; color: white; }
.btn-primary:hover { background: #2c5282; box-shadow: 0 4px 12px rgba(49,130,206,0.4); transform: translateY(-2px); }

.btn-ghost { background: transparent; border-color: #3182ce; color: #3182ce; }
.btn-ghost:hover { background: #ebf8ff; }

.btn-danger { background: #e53e3e; color: white; }
.btn-danger:hover { background: #c53030; }

.btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }"""),

  (20, "Tạo Navbar điều hướng",
   "Xây dựng thanh điều hướng ngang (navbar) cơ bản bằng HTML và CSS.",
   "Navbar là thành phần xuất hiện trên hầu hết trang web. "
   "Navbar cơ bản cần: logo bên trái, menu link bên phải, đổi màu khi hover.",
   ["Tạo navbar cố định trên đầu trang (fixed top)",
    "Logo bên trái, menu link bên phải",
    "Active class cho trang hiện tại",
    "Hover effect cho menu item",
    "Navbar đổi nền khi cuộn trang (dùng JavaScript đơn giản)"],
   ["Dùng <code>display: flex</code> để sắp xếp logo và menu",
    "<code>position: fixed; top: 0; width: 100%</code>: cố định trên đầu",
    "<code>z-index: 100</code>: đảm bảo navbar luôn trên các phần tử khác",
    "Thêm padding-top cho body bằng chiều cao navbar",
    "Class 'active' làm nổi bật menu item hiện tại"],
   """<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 32px;
  height: 64px;
  background: #1a202c;
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
}
.navbar-logo { color: white; font-size: 1.4rem; font-weight: bold; text-decoration: none; }
.navbar-links { display: flex; gap: 0; list-style: none; margin: 0; padding: 0; }
.navbar-links a {
  color: #a0aec0;
  text-decoration: none;
  padding: 0 16px;
  height: 64px;
  display: flex;
  align-items: center;
  transition: color 0.2s, background 0.2s;
}
.navbar-links a:hover { color: white; background: rgba(255,255,255,0.1); }
.navbar-links a.active { color: white; border-bottom: 3px solid #63b3ed; }
</style>

<nav class="navbar">
  <a href="#" class="navbar-logo">🌐 NềnTảng</a>
  <ul class="navbar-links">
    <li><a href="#" class="active">Trang chủ</a></li>
    <li><a href="#">Khóa học</a></li>
    <li><a href="#">Bài tập</a></li>
    <li><a href="#">Liên hệ</a></li>
  </ul>
</nav>"""),

  (21, "Tạo Card UI",
   "Thiết kế card sản phẩm/bài viết đẹp bằng CSS.",
   "Card là component UI phổ biến để hiển thị sản phẩm, bài viết, hồ sơ người dùng. "
   "Card cần: ảnh, tiêu đề, mô tả ngắn, action button, hover effect.",
   ["Tạo card sản phẩm: ảnh, tên, giá, nút mua",
    "Thêm badge 'Sale' góc trên trái bằng position absolute",
    "Hover effect: ảnh zoom nhẹ, card nổi lên",
    "Tạo grid 3 sản phẩm dùng CSS thông thường (chưa dùng flex/grid)"],
   ["<code>overflow: hidden</code> trên card để ảnh hover không tràn ra ngoài",
    "<code>object-fit: cover</code> cho ảnh không bị méo",
    "<code>position: absolute</code> trên badge, <code>relative</code> trên card",
    "<code>transition: transform, box-shadow</code> cho hover mượt",
    "<code>display: inline-block</code> để các card nằm cạnh nhau"],
   """.card {
  display: inline-block;
  width: 280px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.12);
  transition: transform 0.3s, box-shadow 0.3s;
  position: relative;
  vertical-align: top;
  margin: 12px;
}
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.2);
}
.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: transform 0.4s;
}
.card:hover img { transform: scale(1.05); }
.card-body { padding: 16px; }
.card-title { font-size: 1.1rem; font-weight: bold; margin: 0 0 8px; }
.card-price { color: #e53e3e; font-size: 1.3rem; font-weight: bold; }
.badge-sale {
  position: absolute;
  top: 12px; left: 12px;
  background: #e53e3e;
  color: white;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 13px;
}"""),

  (22, "CSS Form Styling – Thiết kế Form đẹp",
   "Tạo form đăng ký đẹp, chuyên nghiệp bằng CSS.",
   "Form mặc định của trình duyệt trông rất đơn giản. Với CSS ta có thể "
   "tạo form trông chuyên nghiệp với focus state, validation styling và layout đẹp.",
   ["Style input, select, textarea: border, padding, border-radius",
    "Focus state: border đổi màu + glow shadow",
    "Valid/invalid state bằng CSS :valid :invalid",
    "Tạo floating label (nhãn nổi lên khi input có giá trị)",
    "Style nút submit với hover và active"],
   ["<code>outline: none</code>: bỏ outline mặc định, thay bằng border-color",
    "<code>input:focus { border-color: blue; box-shadow: 0 0 0 3px rgba(...) }</code>",
    "<code>input:valid { border-color: green }</code>",
    "Floating label cần position relative/absolute và transition",
    "Dùng <code>appearance: none</code> để reset style select mặc định"],
   """/* Reset */
input, select, textarea {
  font-family: inherit;
  font-size: inherit;
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

/* Focus state */
input:focus, select:focus, textarea:focus {
  border-color: #3182ce;
  box-shadow: 0 0 0 3px rgba(49, 130, 206, 0.25);
}

/* Validation styling */
input:valid:not(:placeholder-shown) { border-color: #48bb78; }
input:invalid:not(:placeholder-shown) { border-color: #fc8181; }

/* Custom select */
select {
  appearance: none;
  background: url("data:image/svg+xml,...") no-repeat right 12px center;
  padding-right: 40px;
}

/* Submit button */
.form-submit {
  background: #3182ce;
  color: white;
  padding: 14px 32px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  width: 100%;
  transition: background 0.2s, transform 0.1s;
}
.form-submit:hover { background: #2c5282; }
.form-submit:active { transform: scale(0.98); }"""),

  (23, "CSS Transition – Hiệu ứng chuyển tiếp",
   "Tạo hiệu ứng chuyển tiếp mượt mà khi thuộc tính CSS thay đổi.",
   "Transition cho phép CSS thay đổi giá trị từ từ trong khoảng thời gian xác định "
   "thay vì thay đổi đột ngột. Dùng rất phổ biến với hover, focus, active.",
   ["Tạo button với transition màu nền khi hover (0.3s ease)",
    "Tạo menu link với transition transform (slide in từ trái)",
    "Tạo image gallery với transition opacity (fade in/out)",
    "Tạo accordion với transition height (mở rộng/thu nhỏ)"],
   ["<code>transition: property duration timing-function delay</code>",
    "Properties phổ biến: color, background, opacity, transform, box-shadow",
    "<code>transition: all 0.3s</code>: tất cả properties (hơi chậm, cẩn thận)",
    "Timing functions: ease (mặc định), linear, ease-in, ease-out, ease-in-out, cubic-bezier()",
    "Chỉ dùng transition cho các properties có thể 'tween' được (không dùng với display)"],
   """/* Transition cơ bản */
.btn {
  background: #3182ce;
  transition: background-color 0.3s ease,
              transform 0.2s ease,
              box-shadow 0.3s ease;
}
.btn:hover {
  background: #2c5282;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

/* Fade in/out ảnh */
.img-wrap img { opacity: 1; transition: opacity 0.4s; }
.img-wrap:hover img { opacity: 0.7; }

/* Slide menu item */
.menu-item {
  transform: translateX(0);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.menu-item:hover { transform: translateX(8px); }

/* Transition với cubic-bezier tùy chỉnh */
.elastic {
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.elastic:hover { transform: scale(1.1); } /* Nảy nhẹ */"""),

  (24, "CSS Animation với @keyframes",
   "Tạo animation CSS phức tạp bằng @keyframes và animation property.",
   "Trong khi transition chỉ đi từ A sang B khi có sự kiện, animation (@keyframes) "
   "có thể tự chạy nhiều bước, lặp lại, đảo chiều mà không cần JavaScript.",
   ["Tạo animation spinning circle (loading spinner)",
    "Tạo animation pulse (nhịp tim) cho thông báo",
    "Tạo animation floating (lơ lửng lên xuống)",
    "Tạo animation typing (gõ chữ dần dần)",
    "Tạo animation slide-in từ dưới lên khi vào trang"],
   ["<code>@keyframes ten { from { } to { } }</code>: 2 bước",
    "<code>@keyframes ten { 0% {} 50% {} 100% {} }</code>: nhiều bước",
    "<code>animation: ten duration timing iteration direction fill-mode</code>",
    "<code>animation-iteration-count: infinite</code>: lặp mãi",
    "<code>animation-direction: alternate</code>: đi rồi về",
    "<code>animation-fill-mode: forwards</code>: giữ trạng thái cuối cùng"],
   """/* Spinner */
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
.spinner {
  width: 40px; height: 40px;
  border: 4px solid #e2e8f0;
  border-top-color: #3182ce;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Pulse */
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.7; }
}
.badge-live {
  background: #e53e3e;
  animation: pulse 1.5s ease-in-out infinite;
}

/* Float */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}
.floating { animation: float 3s ease-in-out infinite; }

/* Slide in */
@keyframes slideInUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-in { animation: slideInUp 0.6s ease forwards; }"""),

  (25, "CSS Transform 2D",
   "Biến đổi phần tử bằng translate, rotate, scale, skew.",
   "CSS transform cho phép dịch chuyển, xoay, phóng to/thu nhỏ và nghiêng phần tử "
   "mà không ảnh hưởng layout các phần tử khác. Cao hiệu năng vì dùng GPU.",
   ["Dùng translate() dịch chuyển div mà không ảnh hưởng layout",
    "Dùng rotate() tạo thẻ bài nghiêng",
    "Dùng scale() tạo effect zoom khi hover",
    "Dùng skewX() tạo banner nghiêng",
    "Kết hợp nhiều transform trong 1 rule"],
   ["<code>translate(x, y)</code>: dịch chuyển – không ảnh hưởng flow",
    "<code>rotate(45deg)</code>: xoay theo chiều kim đồng hồ",
    "<code>scale(1.2)</code>: phóng to 120% từ tâm",
    "<code>scale(1, -1)</code>: lật ngược chiều dọc",
    "<code>skewX(15deg)</code>: nghiêng theo trục X",
    "<code>transform-origin</code>: điểm gốc biến đổi (mặc định: center)"],
   """/* Translate – dịch chuyển */
.moved { transform: translate(50px, 20px); }
.center-trick {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%); /* Căn giữa tuyệt đối */
}

/* Rotate */
.rotated { transform: rotate(45deg); }
.card-tilt:hover { transform: rotate(-3deg) scale(1.02); }

/* Scale */
.zoom:hover { transform: scale(1.1); transition: transform 0.3s; }

/* Skew – banner nghiêng */
.skewed {
  transform: skewX(-15deg);
  background: #3182ce;
  padding: 8px 24px;
  color: white;
}
.skewed span { display: inline-block; transform: skewX(15deg); } /* chỉnh lại text */

/* Kết hợp transform */
.combo:hover {
  transform: translateY(-5px) rotate(3deg) scale(1.05);
  transition: transform 0.3s;
}"""),

  (26, "CSS Filter – Bộ lọc hình ảnh",
   "Áp dụng hiệu ứng bộ lọc CSS lên ảnh và phần tử: blur, grayscale, brightness...",
   "CSS filter cho phép áp dụng hiệu ứng đồ họa mà không cần Photoshop. "
   "Rất hữu ích để làm ảnh đen trắng khi hover, tạo overlay effect.",
   ["Áp dụng grayscale(100%) rồi hover về màu gốc",
    "Dùng blur() làm mờ ảnh nền không mờ nội dung",
    "Dùng brightness() tối ảnh để text đọc được",
    "Dùng hue-rotate() tạo hiệu ứng đổi màu liên tục",
    "Kết hợp nhiều filter trong 1 rule"],
   ["<code>filter: grayscale(100%)</code>: đen trắng",
    "<code>filter: blur(4px)</code>: làm mờ",
    "<code>filter: brightness(0.5)</code>: tối đi (0=đen, 1=bình thường, 2=sáng)",
    "<code>filter: contrast(150%)</code>: tăng tương phản",
    "<code>filter: sepia(80%)</code>: tông nâu cổ điển",
    "<code>filter: hue-rotate(180deg)</code>: xoay màu sắc",
    "<code>backdrop-filter</code>: áp dụng cho phía sau phần tử"],
   """/* Grayscale hover effect */
.photo {
  filter: grayscale(100%);
  transition: filter 0.4s;
}
.photo:hover { filter: grayscale(0%); }

/* Làm tối ảnh để đọc text */
.hero-img {
  filter: brightness(0.6);
}

/* Kết hợp nhiều filter */
.vintage {
  filter: sepia(60%) contrast(110%) brightness(90%);
}

/* Blur background không blur content */
.blurred-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background: inherit;
  filter: blur(20px);
  z-index: -1;
}

/* Hue rotate animation */
@keyframes hue-anim {
  0% { filter: hue-rotate(0deg); }
  100% { filter: hue-rotate(360deg); }
}
.rainbow-img { animation: hue-anim 3s linear infinite; }"""),

  (27, "Tạo khung frame cho hình ảnh",
   "Tạo các kiểu khung ảnh sáng tạo bằng CSS thuần.\n",
   "CSS có thể tạo khung ảnh đẹp mà không cần ảnh nền hay thư viện. "
   "Kết hợp border, outline, box-shadow và ::before/::after để sáng tạo.",
   ["Tạo khung ảnh polaroid (viền trắng dày dưới)",
    "Tạo khung đa lớp dùng outline",
    "Tạo khung góc (corner brackets) dùng ::before::after",
    "Tạo khung ảnh với bóng đổ đẹp",
    "Tạo khung ảnh 3D dùng perspective"],
   ["<code>outline: 4px solid white</code> + <code>outline-offset: -12px</code>: khung trong",
    "<code>box-shadow</code> nhiều lớp tạo hiệu ứng khung đa lớp",
    "Polaroid: padding dày phía dưới, box-shadow nhẹ",
    "<code>::before</code> và <code>::after</code> tạo góc trang trí",
    "Perspective 3D: <code>transform: rotate3d()</code> cho hiệu ứng nghiêng"],
   """/* Polaroid frame */
.polaroid {
  display: inline-block;
  padding: 12px 12px 40px;
  background: white;
  box-shadow: 0 4px 16px rgba(0,0,0,0.2);
  transform: rotate(-3deg);
  transition: transform 0.3s;
}
.polaroid:hover { transform: rotate(0deg) scale(1.02); }

/* Khung vàng đa lớp */
.gold-frame {
  border: 4px solid #b7791f;
  outline: 2px solid #f6e05e;
  outline-offset: -8px;
  box-shadow: 0 0 0 8px #b7791f, 0 8px 24px rgba(0,0,0,0.4);
}

/* Corner brackets */
.corner-frame { position: relative; }
.corner-frame::before, .corner-frame::after {
  content: '';
  position: absolute;
  width: 24px; height: 24px;
  border: 3px solid #3182ce;
}
.corner-frame::before { top: -3px; left: -3px; border-right:none; border-bottom:none; }
.corner-frame::after  { bottom:-3px; right:-3px; border-left:none; border-top:none; }"""),

  (28, "Tổng hợp: Trang Landing Page đơn giản",
   "Tạo trang landing page mini tổng hợp kiến thức CSS cơ bản đã học.",
   "Landing page là trang đích khi người dùng click quảng cáo hay tìm kiếm. "
   "Cần có: Hero section, Features section, CTA button, Footer.",
   ["Hero section: nền gradient, tiêu đề lớn, mô tả, 2 nút CTA",
    "Features section: 3 icon cards",
    "CTA section: nền đậm, lời kêu gọi, nút đăng ký",
    "Footer: đơn giản với copyright",
    "Dùng đầy đủ: gradient, shadow, border-radius, transition, fonts"],
   ["Landing page cần: Hero(trên đầu), Value props, CTA(kêu gọi hành động), Social proof",
    "CTA button phải nổi bật: màu tương phản, to, dễ nhấn",
    "Giữ màu sắc nhất quán theo palette đã định",
    "Above the fold: nội dung quan trọng nhất phải thấy ngay khi vào",
    "White space (khoảng trắng) là bạn của thiết kế đẹp"],
   """/* Hero */
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 120px 32px;
}
.hero h1 { font-size: 3rem; margin-bottom: 16px; }
.hero p { font-size: 1.2rem; opacity: 0.9; margin-bottom: 32px; }
.btn-hero {
  display: inline-block;
  padding: 16px 40px;
  background: white;
  color: #764ba2;
  border-radius: 999px;
  font-weight: bold;
  text-decoration: none;
  font-size: 1.1rem;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}
.btn-hero:hover { transform: translateY(-3px); box-shadow: 0 16px 40px rgba(0,0,0,0.3); }

/* Features */
.features {
  display: flex;
  justify-content: center;
  gap: 32px;
  padding: 80px 32px;
  flex-wrap: wrap;
}
.feature-card {
  text-align: center;
  width: 260px;
  padding: 32px 24px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}
.feature-card:hover { transform: translateY(-6px); }
.feature-icon { font-size: 2.5rem; margin-bottom: 16px; }"""),

  (29, "CSS Nâng cao: Biến đổi 3D",
   "Tạo hiệu ứng 3D bằng perspective và transform 3D.",
   "CSS 3D transform cho phép tạo hiệu ứng không gian ba chiều ngay trong trình duyệt. "
   "Cần khai báo perspective trên parent để 3D có tác dụng.",
   ["Tạo card lật (flip card) khi hover – mặt trước/mặt sau",
    "Tạo cube 3D xoay bằng animation",
    "Tạo nút 3D với hiệu ứng nhấn xuống",
    "Tạo gallery dạng xoay vòng (carousel 3D đơn giản)"],
   ["<code>perspective: 1000px</code>: đặt trên PARENT, tạo không gian 3D",
    "<code>transform-style: preserve-3d</code>: giữ child 3D trong không gian 3D",
    "<code>rotateX(deg)</code>: xoay theo trục X (lật lên xuống)",
    "<code>rotateY(deg)</code>: xoay theo trục Y (lật trái phải)",
    "<code>backface-visibility: hidden</code>: ẩn mặt sau khi bị lật",
    "<code>translate3d(x,y,z)</code>: dịch chuyển theo 3 trục"],
   """/* Flip Card */
.flip-wrapper {
  perspective: 1000px;
  width: 300px;
  height: 200px;
}
.flip-card {
  width: 100%; height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.6s;
}
.flip-wrapper:hover .flip-card {
  transform: rotateY(180deg);
}
.flip-front, .flip-back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.flip-front { background: linear-gradient(135deg, #667eea, #764ba2); color: white; }
.flip-back  { background: linear-gradient(135deg, #f093fb, #f5576c); color: white; transform: rotateY(180deg); }"""),

  (30, "🏆 Dự án: Trang sản phẩm hoàn chỉnh",
   "Xây dựng trang giới thiệu sản phẩm đẹp, chuyên nghiệp bằng HTML + CSS thuần.",
   "Dự án cuối module tổng hợp TOÀN BỘ kiến thức CSS đã học. "
   "Tạo trang chi tiết sản phẩm (Product Detail) như trang thương mại điện tử thực tế.",
   ["Header: navbar với logo và giỏ hàng icon",
    "Product section: ảnh bên trái, thông tin bên phải (dùng inline-block hoặc float)",
    "Thông tin: tên, giá (gạch ngang giá gốc), rating sao, mô tả, nút thêm giỏ",
    "Tab section: Mô tả / Thông số / Đánh giá",
    "Sản phẩm liên quan: 4 card ngang",
    "Footer: 4 cột thông tin"],
   ["Phân chia layout bằng inline-block hoặc float (chuẩn bị cho flex ở module 3)",
    "Hình ảnh bên trái: width 45%, float left hoặc inline-block",
    "Tab UI: radio input hack hoặc JavaScript đơn giản",
    "Responsive tối thiểu: ảnh 100% khi màn hình nhỏ",
    "Sử dụng CSS variables cho consistent colors"],
   """/* Product page layout */
:root {
  --primary: #3182ce;
  --danger: #e53e3e;
}

.product-wrapper { display: flex; gap: 48px; padding: 48px; max-width: 1100px; margin: auto; }
.product-images { flex: 1; }
.product-images img { width: 100%; border-radius: 12px; }
.product-info { flex: 1; }
.product-name { font-size: 1.8rem; font-weight: bold; }
.price-old { text-decoration: line-through; color: #a0aec0; }
.price-new { font-size: 2rem; color: var(--danger); font-weight: bold; }
.discount-badge {
  background: var(--danger);
  color: white;
  padding: 2px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
}
.stars { color: #f6ad55; font-size: 1.2rem; }
.btn-add-cart {
  background: var(--primary);
  color: white;
  width: 100%;
  padding: 16px;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
}
.btn-add-cart:hover { background: #2c5282; }
.btn-add-cart:active { transform: scale(0.98); }"""),
]

count = 0
for num, title, short, desc, reqs, knows, code in exercises:
    folder = BASE / f"bai-{num:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    content = tpl(num, title, short, desc, reqs, knows, code)
    (folder / "index.html").write_text(content, encoding="utf-8")
    count += 1
    print(f"  ✓ bai-{num:02d}: {title}")

print(f"\nModule 2 – CSS Cơ Bản: Đã tạo {count} file")
