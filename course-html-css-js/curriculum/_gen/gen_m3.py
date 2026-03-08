#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo Module 3 – CSS Layout & Responsive – 30 bài tập đầy đủ tiếng Việt"""
import os, pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-03-css-layout")

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
  <div class="page-header module-3">
    <div class="breadcrumb">
      <a href="../../index.html">Trang Chủ</a> &rsaquo;
      <a href="../index.html">Module 3</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 3 – CSS Layout &amp; Responsive</p>
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
    const highlighted = await codeToHtml(raw, {{ lang: 'css', theme: 'github-dark' }});
    document.getElementById('code-highlight').innerHTML = highlighted;
    const pre = document.getElementById('code-highlight').querySelector('pre');
    if (pre) pre.style.cssText = 'border-radius:10px;padding:20px;font-size:0.87rem;overflow-x:auto;margin:0;line-height:1.7';
  </script>
</body>
</html>"""

exercises = [
  (1,"Display: block inline inline-block none",
   "Thực hành các giá trị của thuộc tính display – nền tảng của CSS layout.",
   "display là thuộc tính CSS quan trọng nhất cho layout. "
   "Hiểu sự khác biệt giữa block, inline, inline-block, none là bước đầu tiên của layout.",
   ["Tạo menu ngang bằng cách đặt li thành inline-block",
    "So sánh p (block) với span (inline) bằng cách đặt width và height",
    "Dùng display:none để ẩn phần tử (không chiếm không gian)",
    "Dùng visibility:hidden (vẫn chiếm không gian, chỉ ẩn nhìn thôi)"],
   ["<code>block</code>: chiếm hết chiều rộng, xuống dòng sau",
    "<code>inline</code>: chỉ rộng bằng nội dung, không xuống dòng, KHÔNG set được width/height",
    "<code>inline-block</code>: như inline (không xuống dòng) nhưng CÓ set được width/height",
    "<code>display:none</code>: ẩn hoàn toàn – không chiếm không gian",
    "<code>visibility:hidden</code>: ẩn nhìn thấy – VẪN chiếm không gian"],
   """/* Block */
div, p, h1, section { display: block; }
/* Chiếm 100% width của parent, xuống dòng */

/* Inline */
span, a, strong, em { display: inline; }
/* width/height không có tác dụng với inline */

/* Inline-block: ĐỈNH của sư tử! */
.nav-item {
  display: inline-block;
  width: 120px;
  height: 44px;
  line-height: 44px;
  text-align: center;
  background: #3182ce;
  color: white;
}

/* Ẩn phần tử */
.hidden { display: none; }    /* không chiếm chỗ */
.invisible { visibility: hidden; } /* chiếm chỗ, chỉ ẩn */"""),

  (2,"Float: căn trái phải",
   "Dùng float để sắp xếp phần tử nổi sang trái hoặc phải.",
   "Float ra đời để làm cho text chảy quanh ảnh (như báo in). "
   "Sau đó được dùng để tạo layout cột. Ngày nay Flexbox/Grid đã thay thế float cho layout.",
   ["Tạo bài viết có ảnh float: left với text chảy bên phải",
    "Tạo ảnh float: right với caption bên dưới",
    "Dùng float để tạo 2 cột đơn giản"],
   ["<code>float: left</code>: phần tử nổi sang trái, nội dung khác chảy bên phải",
    "<code>float: right</code>: phần tử nổi sang phải",
    "Phần tử float bị 'thoát khỏi' luồng thông thường",
    "Parent không tính chiều cao float children – cần clearfix",
    "Width phần tử float nên tính bằng phần trăm để linh hoạt"],
   """/* Ảnh float trái, text chảy bên */
.article img {
  float: left;
  width: 200px;
  margin: 0 16px 8px 0;
  border-radius: 8px;
}

/* 2 cột đơn giản */
.col-left  { float: left;  width: 60%; padding-right: 20px; }
.col-right { float: right; width: 40%; }

/* Ảnh float phải */
.pull-right {
  float: right;
  max-width: 300px;
  margin: 0 0 16px 20px;
}"""),

  (3,"Clearfix – Xử lý container bị sụp",
   "Áp dụng clearfix để ngăn container bị sụp khi chứa float elements.",
   "Vấn đề lớn nhất của float: container không 'bọc' được các child float – "
   "height = 0. Clearfix là giải pháp CSS để sửa lỗi này.",
   ["Tạo container chứa 3 float div – quan sát container bị sụp",
    "Áp dụng clearfix bằng class .clearfix",
    "So sánh cách dùng overflow:hidden và clearfix",
    "Sau đó dùng thẻ div dưới cùng style='clear:both'"],
   ["Vấn đề: parent chứa float children có height = 0",
    "Cách 1: <code>overflow: hidden</code> trên parent (đơn giản nhất)",
    "Cách 2: thêm div <code>style='clear:both'</code> cuối parent",
    "Cách 3 (tốt nhất): clearfix hack dùng <code>::after</code>",
    "<code>clear: both</code>: đặt phần tử xuống dưới cả float left và right"],
   """.clearfix::after {
  content: '';
  display: table;
  clear: both;
}
/* Hoặc ngắn gọn hơn */
.clearfix::after {
  content: '';
  display: block;
  clear: both;
}

/* Cách dùng */
<div class="clearfix">
  <div style="float:left; width:50%">Cột trái</div>
  <div style="float:right; width:50%">Cột phải</div>
  <!-- Không cần div clear nữa! -->
</div>

/* Cách overflow hidden */
.container { overflow: hidden; } /* Cũng tự clear được */"""),

  (4,"Position: static relative absolute",
   "Hiểu 3 giá trị position cơ bản và cách chúng ảnh hưởng layout.",
   "Thuộc tính position điều khiển cách phần tử được định vị. "
   "Hiểu rõ relative và absolute là chìa khóa để đặt phần tử đúng vị trí mong muốn.",
   ["Tạo badge 'Mới' đặt tuyệt đối góc trên phải của card",
    "Thực hành relative: dịch phần tử 10px mà không ảnh hưởng flow",
    "Overlay text trên ảnh dùng absolute positioning",
    "Tạo tooltip xuất hiện bên cạnh khi hover"],
   ["<code>static</code>: mặc định – theo luồng thông thường",
    "<code>relative</code>: dịch chuyển tương đối điểm ban đầu, VẪN giữ không gian",
    "<code>absolute</code>: đặt tuyệt đối theo ancestor có position!=static",
    "Ancestor của absolute: parent gần nhất có position: relative/absolute/fixed/sticky",
    "<code>top, right, bottom, left</code>: khoảng cách từ cạnh tương ứng của parent"],
   """/* Relative – dịch không ảnh hưởng flow */
.shifted {
  position: relative;
  top: 10px;    /* xuống 10px */
  left: 20px;   /* phải 20px */
}

/* Parent là context cho absolute */
.card { position: relative; }

/* Absolute – đặt tuyệt đối trong parent .card */
.badge {
  position: absolute;
  top: 12px;
  right: 12px;
  background: #e53e3e;
  color: white;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
}

/* Overlay text lên ảnh */
.img-container { position: relative; }
.img-overlay {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  background: rgba(0,0,0,0.6);
  color: white;
  padding: 12px;
}"""),

  (5,"Position: fixed và sticky",
   "Tạo navbar cố định và header dính bằng position fixed và sticky.",
   "fixed: phần tử cố định theo viewport (màn hình), không cuộn theo trang. "
   "sticky: như relative bình thường nhưng 'dính' khi cuộn đến vị trí xác định.",
   ["Tạo navbar fixed cố định trên đầu trang khi cuộn",
    "Tạo nút 'Về đầu trang' fixed góc dưới phải",
    "Tạo header bảng sticky: cố định khi cuộn bảng dài",
    "Tạo sidebar sticky đi theo khi cuộn trang"],
   ["<code>position: fixed</code>: cố định theo viewport, không cuộn theo trang",
    "<code>position: sticky</code>: dính khi đến ngưỡng top/bottom xác định",
    "fixed thoát khỏi flow hoàn toàn – phải thêm padding-top body bằng chiều cao navbar",
    "sticky KHÔNG thoát flow – vẫn chiếm không gian ban đầu",
    "sticky cần parent có đủ height để 'dính' trong"],
   """/* Navbar fixed */
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 60px;
  background: #1a202c;
  z-index: 100;
  /* NHỚ thêm padding-top cho body */
}
body { padding-top: 60px; }

/* Nút back-to-top */
.back-top {
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 48px; height: 48px;
  background: #3182ce;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 99;
}

/* Sticky header bảng */
.table-sticky th {
  position: sticky;
  top: 0;
  background: #2d3748;
  color: white;
  z-index: 10;
}

/* Sticky sidebar */
.sidebar {
  position: sticky;
  top: 80px; /* 80px từ top viewport */
  align-self: flex-start;
}"""),

  (6,"z-index – Thứ tự lớp chồng",
   "Kiểm soát thứ tự lớp chồng của các phần tử bằng z-index.",
   "Khi các phần tử có position != static chồng lên nhau, z-index quyết định "
   "phần tử nào hiện lên trên. Giá trị lớn hơn = trên trước.",
   ["Tạo 3 div chồng lên nhau, điều chỉnh z-index từ 1-3",
    "Tạo modal popup hiển thị trên overlay",
    "Tạo dropdown menu xuất hiện trên nội dung trang",
    "Xử lý vấn đề stacking context"],
   ["<code>z-index</code> chỉ hoạt động với phần tử có <code>position != static</code>",
    "Giá trị lớn hơn = hiện trên trước",
    "Có thể là số âm (xuống dưới cùng)",
    "Stacking context mới: khi có position+z-index, transform, opacity<1, isolation:isolate",
    "Tránh dùng z-index quá cao (9999999) – lập kế hoạch z-index system"],
   """/* Z-index system có tổ chức */
:root {
  --z-below:   -1;
  --z-base:     0;
  --z-raised:  10;
  --z-dropdown: 100;
  --z-sticky:  200;
  --z-fixed:   300;
  --z-overlay: 400;
  --z-modal:   500;
  --z-toast:   600;
}

/* Modal overlay */
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: var(--z-overlay);
}
.modal {
  position: fixed;
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  background: white;
  border-radius: 12px;
  padding: 32px;
  z-index: var(--z-modal);
  min-width: 320px;
}

/* Dropdown menu */
.dropdown { position: relative; }
.dropdown-menu {
  position: absolute;
  top: 100%; left: 0;
  background: white;
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  z-index: var(--z-dropdown);
  border-radius: 8px;
}"""),

  (7,"Overflow: hidden scroll auto",
   "Kiểm soát nội dung tràn ra ngoài container bằng overflow.",
   "Khi nội dung vượt quá kích thước container, overflow quyết định "
   "hiển thị hay ẩn phần bị tràn, hoặc thêm thanh cuộn.",
   ["Tạo div cố định height, nội dung nhiều – so sánh overflow: visible/hidden/scroll/auto",
    "Tạo custom scrollbar CSS cho overflow:scroll",
    "Dùng overflow:hidden + border-radius để ảnh không vượt khỏi góc bo tròn",
    "Tạo text truncate (cắt bớt bằng dấu ...) với overflow và text-overflow"],
   ["<code>overflow: visible</code>: mặc định – nội dung tràn ra ngoài",
    "<code>overflow: hidden</code>: cắt bỏ phần tràn",
    "<code>overflow: scroll</code>: luôn hiện thanh cuộn",
    "<code>overflow: auto</code>: chỉ hiện thanh cuộn khi cần (thường dùng nhất)",
    "<code>text-overflow: ellipsis</code>: hiện dấu ... khi cắt text (cần overflow:hidden + white-space:nowrap)"],
   """/* Text truncate 1 dòng */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 200px;
}

/* Text truncate nhiều dòng (2 dòng) */
.clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Scrollable box */
.scroll-box {
  height: 200px;
  overflow-y: auto;
  padding: 16px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}

/* Custom scrollbar */
.scroll-box::-webkit-scrollbar { width: 6px; }
.scroll-box::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 3px; }
.scroll-box::-webkit-scrollbar-thumb { background: #3182ce; border-radius: 3px; }

/* Overflow hidden giúp ảnh tôn trọng border-radius */
.card { border-radius: 12px; overflow: hidden; }"""),

  (8,"Flexbox: Container properties",
   "Học các thuộc tính cơ bản của Flex Container để sắp xếp layout.",
   "Flexbox (Flexible Box) là hệ thống layout 1 chiều rất mạnh. "
   "Đặt display:flex trên container để các children trở thành flex items.",
   ["Tạo container flex, thêm 5 box con, quan sát flex-direction",
    "Thực hành justify-content: flex-start, center, flex-end, space-between, space-around, space-evenly",
    "Thực hành align-items: flex-start, center, flex-end, stretch, baseline",
    "Thực hành flex-wrap: nowrap, wrap, wrap-reverse"],
   ["<code>display: flex</code>: bật flexbox cho container",
    "<code>flex-direction: row|column|row-reverse|column-reverse</code>",
    "<code>justify-content</code>: căn trên TRỤC CHÍNH (main axis)",
    "<code>align-items</code>: căn trên TRỤC PHỤ (cross axis) – 1 dòng",
    "<code>flex-wrap: wrap</code>: cho phép xuống dòng khi hết chỗ",
    "<code>gap: 16px</code>: khoảng cách giữa các items (thay margin)"],
   """/* Flex container cơ bản */
.flex-container {
  display: flex;
  flex-direction: row;       /* row (default) | column */
  justify-content: center;   /* căn trục chính */
  align-items: center;       /* căn trục phụ */
  flex-wrap: wrap;           /* xuống dòng khi hết chỗ */
  gap: 16px;                 /* khoảng cách đều */
}

/* justify-content các giá trị */
.jc-start   { justify-content: flex-start; }
.jc-center  { justify-content: center; }
.jc-end     { justify-content: flex-end; }
.jc-between { justify-content: space-between; } /* phổ biến nhất */
.jc-around  { justify-content: space-around; }
.jc-evenly  { justify-content: space-evenly; }

/* Căn giữa hoàn hảo: flex + justify+align center */
.perfect-center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}"""),

  (9,"Flexbox: justify-content và align-items",
   "Thực hành căn chỉnh flex items theo cả hai trục bằng justify-content và align-items.",
   "Đây là 2 thuộc tính quan trọng nhất của Flexbox. Hiểu rõ trục chính (main axis) "
   "và trục phụ (cross axis) theo flex-direction là chìa khóa.",
   ["Tạo navbar: logo trái, links phải bằng justify-content: space-between",
    "Căn giữa nội dung hero section theo cả 2 chiều",
    "Tạo grid icon 3x3 dùng flex-wrap + justify-content",
    "Tạo footer 3 cột đều nhau"],
   ["Trục chính (main axis): theo chiều flex-direction",
    "Trục phụ (cross axis): vuông góc với main axis",
    "<code>justify-content</code>: căn trên main axis",
    "<code>align-items</code>: căn trên cross axis (tất cả items)",
    "<code>align-content</code>: căn nhiều dòng trên cross axis (khi wrap)",
    "flex-direction:row → main=ngang, cross=dọc; column → ngược lại"],
   """/* Navbar: logo trái, menu phải */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 32px;
  height: 64px;
}

/* Hero căn giữa tuyệt đối */
.hero {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  text-align: center;
}

/* Grid icon 3x3 */
.icon-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
.icon-item { width: calc(33.333% - 20px); }

/* Footer 3 cột */
.footer {
  display: flex;
  justify-content: space-between;
  gap: 32px;
}
.footer-col { flex: 1; }"""),

  (10,"Flexbox: flex-grow shrink basis",
   "Kiểm soát cách flex items co giãn với flex-grow, flex-shrink, flex-basis.",
   "Ba thuộc tính này điều khiển cách items phân chia không gian còn lại trong container. "
   "Shorthand flex: [grow] [shrink] [basis].",
   ["Tạo sidebar 250px cố định + content co giãn dùng flex-grow",
    "Tạo 3 cột tỷ lệ 1:2:1 dùng flex-grow",
    "Thực hành flex-shrink để ngăn items bị thu nhỏ",
    "Dùng flex: 1 shorthand cho các cột đều nhau"],
   ["<code>flex-grow: n</code>: tỷ lệ nhận không gian dư (0 = không nhận)",
    "<code>flex-shrink: n</code>: tỷ lệ co lại khi thiếu không gian (1 = co bình thường)",
    "<code>flex-basis: px|%|auto</code>: kích thước ban đầu trước khi grow/shrink",
    "<code>flex: 1</code> = <code>flex: 1 1 0</code>: co giãn đều nhau",
    "<code>flex: none</code> = <code>flex: 0 0 auto</code>: không co giãn"],
   """/* Sidebar + Main layout */
.layout {
  display: flex;
  gap: 24px;
}
.sidebar {
  flex: 0 0 250px; /* không grow, không shrink, luôn 250px */
  /* hoặc: flex-shrink:0; width:250px */
}
.main-content {
  flex: 1; /* nhận hết không gian còn lại */
}

/* 3 cột tỷ lệ 1:2:1 */
.col-1 { flex: 1; }  /* 1 phần */
.col-2 { flex: 2; }  /* 2 phần */
.col-3 { flex: 1; }  /* 1 phần */

/* Ngăn co lại */
.no-shrink { flex-shrink: 0; }

/* Điền đầy phần còn lại */
.fill { flex: 1; }

/* Min-width để không bị nhỏ quá */
.card-item {
  flex: 1 1 200px; /* grow, shrink, min-width 200px */
  max-width: 300px;
}"""),

  (11,"Flexbox: order và align-self",
   "Thay đổi thứ tự hiển thị và căn chỉnh riêng từng flex item.",
   "order thay đổi thứ tự hiển thị mà không cần thay đổi HTML. "
   "align-self ghi đè align-items cho một item cụ thể.",
   ["Tạo layout có Sidebar sau Main trong HTML nhưng hiển thị trước",
    "Tạo card grid: card đặc biệt kéo dài hết chiều cao cột dùng align-self: stretch",
    "Tạo navigation với item 'Đăng nhập' căn phải"],
   ["<code>order: n</code>: thứ tự hiển thị – mặc định 0, số lớn hơn hiển thị sau",
    "<code>order: -1</code>: hiển thị đầu tiên",
    "<code>align-self</code>: ghi đè align-items cho 1 item cụ thể",
    "Giá trị align-self: auto, flex-start, flex-end, center, stretch, baseline",
    "order chỉ thay đổi thứ tự HIỂN THỊ, không thay đổi DOM thực tế"],
   """/* Order */
.nav-item-login { order: 100; } /* luôn ở cuối */
.nav-brand { order: -1; }       /* luôn ở đầu */

/* Sidebar đặt sau main trong HTML nhưng hiển thị trước */
.sidebar { order: -1; }  /* hiện trước main */
.main { order: 0; }

/* align-self */
.flex-container {
  display: flex;
  align-items: flex-start; /* mặc định cho tất cả */
  height: 200px;
}
.item-stretch { align-self: stretch; }  /* kéo dài hết chiều cao */
.item-center  { align-self: center; }   /* chỉ item này căn giữa */
.item-end     { align-self: flex-end; } /* chỉ item này xuống dưới */

/* Nav với login button bên phải */
.nav-links { display: flex; align-items: center; gap: 0; }
.nav-login  { margin-left: auto; } /* đẩy sang phải */"""),

  (12,"Flexbox: Tạo Page Layout đầy đủ",
   "Xây dựng layout trang web hoàn chỉnh Header-Sidebar-Main-Footer bằng Flexbox.",
   "Bài tập thực hành tổng hợp Flexbox để tạo layout trang web thực tế "
   "với header, nav, sidebar, main content và footer.",
   ["Header full width với logo và nav",
    "Body section: sidebar 260px bên trái + main co giãn",
    "Footer full width",
    "Các phần tử trong header và footer đều dùng flexbox để căn chỉnh"],
   ["Flexbox lồng nhau (nested flexbox): container flex chứa flex container",
    "Outer layout: column direction (header, body, footer xếp dọc)",
    "Body: row direction (sidebar + main xếp ngang)",
    "<code>min-height: 100vh</code>: trang đủ cao để đẩy footer xuống dưới",
    "Sidebar: <code>flex: 0 0 260px</code> để không co giãn"],
   """body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 32px;
  height: 64px;
  background: #1a202c;
  color: white;
}

.body-section {
  display: flex;
  flex: 1;
}

.sidebar {
  flex: 0 0 260px;
  background: #f7fafc;
  padding: 24px;
  border-right: 1px solid #e2e8f0;
}

.main-content {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}

footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 32px;
  background: #2d3748;
  color: #a0aec0;
}"""),

  (13,"Flexbox: Dashboard Card Grid",
   "Tạo dashboard với grid card responsive bằng Flexbox.",
   "Dashboard thường có nhiều card thống kê dạng grid. "
   "Dùng flex-wrap + flex-basis để tạo grid tự động xuống dòng.",
   ["Tạo 4 stat card hàng đầu (icon, số lớn, label)",
    "Tạo grid card sản phẩm tự xuống dòng",
    "Card cuối cùng trong hàng dùng flex-grow để điền đầy"],
   ["<code>flex: 1 1 200px</code>: grow được, shrink được, min-width 200px",
    "Kết hợp với <code>max-width</code> để card không quá rộng",
    "<code>flex-wrap: wrap</code> bắt buộc để xuống dòng",
    "gap thay thế margin hack (margin: -8px / padding: 8px)",
    "CSS Grid thường tốt hơn cho 2D grid, Flexbox tốt cho 1D"],
   """.stats-row {
  display: flex;
  gap: 20px;
  margin-bottom: 24px;
}
.stat-card {
  flex: 1;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  gap: 16px;
}
.stat-icon { font-size: 2rem; }
.stat-value { font-size: 2rem; font-weight: bold; }
.stat-label { color: #718096; font-size: 0.9rem; }

/* Product grid */
.product-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.product-card {
  flex: 1 1 200px;
  max-width: 280px;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.product-card img { width: 100%; height: 160px; object-fit: cover; }"""),

  (14,"CSS Grid: Cột và hàng cơ bản",
   "Học cú pháp cơ bản của CSS Grid để tạo layout 2 chiều.",
   "CSS Grid là hệ thống layout 2 chiều (rows + columns) mạnh nhất trong CSS hiện đại. "
   "Dùng Grid cho layout tổng thể, Flexbox cho căn chỉnh bên trong component.",
   ["Tạo grid 3 cột đều nhau dùng repeat(3, 1fr)",
    "Tạo grid 2x3 (2 cột, 3 hàng) với kích thước cố định",
    "Dùng grid-template-areas để xem preview layout",
    "Thực hành fr unit (fractional unit)"],
   ["<code>display: grid</code>: bật CSS Grid",
    "<code>grid-template-columns: 1fr 2fr 1fr</code>: 3 cột tỷ lệ 1:2:1",
    "<code>repeat(3, 1fr)</code> = <code>1fr 1fr 1fr</code>",
    "<code>fr</code>: fractional unit – phần còn lại sau khi trừ fixed/auto",
    "<code>gap: row-gap col-gap</code>: khoảng cách",
    "<code>grid-template-rows</code>: định nghĩa chiều cao hàng"],
   """/* Grid cơ bản */
.grid-3col {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  /* hoặc: repeat(3, 1fr) */
  gap: 20px;
}

/* Grid hỗn hợp */
.grid-mixed {
  display: grid;
  grid-template-columns: 250px 1fr 200px; /* sidebar, main, aside */
  grid-template-rows: 60px 1fr 60px;      /* header, body, footer */
  gap: 16px;
  min-height: 100vh;
}

/* auto-fill vs auto-fit */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

/* fr unit */
.three-col {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr; /* tỷ lệ 1:2:1 */
}"""),

  (15,"CSS Grid: row-gap, column-span",
   "Cho grid item chiếm nhiều cột/hàng bằng grid-column và grid-row span.",
   "grid-column và grid-row cho phép một item chiếm nhiều ô trong grid, "
   "tạo layout phức tạp như magazine, dashboard.",
   ["Tạo grid 3 cột, item đầu tiên chiếm hết hàng (span 3)",
    "Tạo item chiếm 2 cột và 2 hàng đồng thời",
    "Tạo grid 4 cột: item hero chiếm 3 cột đầu, sidebar 1 cột (span đến cuối)"],
   ["<code>grid-column: 1 / 3</code>: từ line 1 đến line 3 (chiếm 2 cột)",
    "<code>grid-column: span 2</code>: chiếm 2 cột tính từ vị trí hiện tại",
    "<code>grid-column: 1 / -1</code>: từ đầu đến cuối (chiếm toàn hàng)",
    "<code>grid-row: span 2</code>: chiếm 2 hàng",
    "Grid lines: bắt đầu từ 1, dùng -1 cho dòng cuối cùng"],
   """/* Grid với span */
.photo-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 200px;
  gap: 12px;
}

/* Item chiếm toàn hàng */
.hero-item {
  grid-column: 1 / -1; /* từ đầu đến cuối */
}

/* Item chiếm 2 cột */
.wide-item { grid-column: span 2; }

/* Item chiếm 2 hàng */
.tall-item { grid-row: span 2; }

/* Item chiếm 2x2 */
.featured {
  grid-column: span 2;
  grid-row: span 2;
}

/* Đặt vị trí cụ thể */
.sidebar {
  grid-column: 3 / 4;  /* cột 3 */
  grid-row: 1 / 4;     /* hàng 1 đến 3 */
}"""),

  (16,"CSS Grid: Named Areas",
   "Định nghĩa vùng tên (named areas) trong CSS Grid để layout trực quan.",
   "grid-template-areas cho phép bạn 'vẽ' layout bằng tên vùng trong CSS, "
   "giúp code đọc rất dễ và dễ điều chỉnh layout.",
   ["Tạo layout cổ điển: header, sidebar, main, footer bằng named areas",
    "Chuyển layout sang mobile bằng media query (sidebar xuống dưới main)",
    "Tạo layout tạp chí 2 cột dùng named areas"],
   ["<code>grid-template-areas: 'header header' 'sidebar main' 'footer footer'</code>",
    "Tên vùng phải liên tục, hình chữ nhật",
    "Dùng <code>.</code> cho ô không có tên",
    "Đặt vào item: <code>grid-area: header</code>",
    "Thay đổi layout responsive chỉ bằng thay đổi grid-template-areas"],
   """/* Layout với named areas */
.page {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: 64px 1fr 60px;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
  gap: 0;
}

.page-header  { grid-area: header;  background: #1a202c; }
.page-sidebar { grid-area: sidebar; background: #f7fafc; }
.page-main    { grid-area: main;    padding: 24px; }
.page-footer  { grid-area: footer;  background: #2d3748; }

/* Responsive: mobile */
@media (max-width: 768px) {
  .page {
    grid-template-columns: 1fr;
    grid-template-rows: 56px auto 1fr 60px;
    grid-template-areas:
      "header"
      "sidebar"
      "main"
      "footer";
  }
}"""),

  (17,"CSS Grid: auto-fill và auto-fit",
   "Tạo grid tự động điều chỉnh số cột theo kích thước màn hình.",
   "Kết hợp repeat(auto-fill/auto-fit), minmax() tạo grid responsive "
   "mà không cần media query – grid tự tính số cột phù hợp.",
   ["Tạo photo gallery tự động điều chỉnh 1-4 cột theo màn hình",
    "So sánh auto-fill và auto-fit với số lượng ít item",
    "Tạo product grid min-width 200px, tự wrap xuống dòng"],
   ["<code>repeat(auto-fill, minmax(200px, 1fr))</code>: tự điền cột, tối thiểu 200px",
    "<code>auto-fill</code>: giữ ô trống khi ít item hơn cột",
    "<code>auto-fit</code>: kéo giãn items để điền đầy hàng",
    "<code>minmax(min, max)</code>: kích thước item trong khoảng min-max",
    "Responsive grid không cần media query với kỹ thuật này"],
   """/* Gallery tự responsive */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

/* Product grid: min 180px, max 1fr */
.products {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
}

/* Masonry-like layout */
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 200px;
  gap: 12px;
}
.masonry .tall { grid-row: span 2; }
.masonry .wide { grid-column: span 2; }"""),

  (18,"CSS Grid: Newspaper Layout",
   "Tạo layout tạp chí nhiều cột phức tạp bằng CSS Grid.",
   "Báo chí/tạp chí cần layout phức tạp với bài viết lớn nhỏ xen kẽ. "
   "CSS Grid giải quyết hoàn hảo với span và named areas.",
   ["Tạo grid 4 cột, 3 hàng tạp chí",
    "Bài viết đặc biệt chiếm 2 cột 2 hàng",
    "Ảnh nền full cover cho mỗi ô tạp chí",
    "Text caption overlay bên dưới mỗi ảnh"],
   ["Tạp chí cần nhiều loại item: hero (lớn), feature, normal, small",
    "Mỗi item = grid cell có ảnh nền và text overlay",
    "Kết hợp grid-column span + grid-row span cho item lớn",
    "Object-fit: cover cho ảnh trong ô grid",
    "position: absolute cho text overlay"],
   """/* Newspaper grid */
.newspaper {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 250px;
  gap: 4px;
  max-width: 1200px;
  margin: auto;
}

.article {
  position: relative;
  overflow: hidden;
  border-radius: 4px;
}
.article img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s;
}
.article:hover img { transform: scale(1.05); }

.article-caption {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,0.8));
  color: white;
  padding: 16px;
}
.article-caption h3 { margin: 0; }

/* Featured article */
.featured { grid-column: span 2; grid-row: span 2; }

/* Wide article */
.wide { grid-column: span 2; }"""),

  (19,"Media Queries – Responsive cơ bản",
   "Viết media query để website hiển thị khác nhau trên các kích thước màn hình.",
   "Media query cho phép áp dụng CSS khác nhau dựa trên đặc điểm thiết bị "
   "như chiều rộng màn hình. Đây là nền tảng của Responsive Web Design.",
   ["Tạo div đổi màu nền theo màn hình: mobile xanh, tablet vàng, desktop đỏ",
    "Ẩn sidebar trên mobile (max-width: 768px)",
    "Thay đổi font-size theo breakpoint",
    "Tạo navigation ẩn/hiện khác nhau trên mobile/desktop"],
   ["<code>@media (max-width: 768px) { }</code>: áp dụng khi <=768px",
    "<code>@media (min-width: 768px) { }</code>: áp dụng khi >=768px",
    "Breakpoints phổ biến: 480px (mobile), 768px (tablet), 1024px (desktop), 1280px (wide)",
    "Mobile-first: viết CSS cho mobile trước, dùng min-width để thêm cho màn lớn hơn",
    "Desktop-first: viết cho desktop trước, dùng max-width để điều chỉnh nhỏ hơn"],
   """/* Điều chỉnh layout theo breakpoint */
/* Mobile: 1 cột, font nhỏ hơn */
@media (max-width: 480px) {
  .grid { grid-template-columns: 1fr; }
  body { font-size: 14px; }
  .hide-mobile { display: none; }
}

/* Tablet */
@media (min-width: 481px) and (max-width: 1024px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 1025px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body { background: #1a202c; color: #e2e8f0; }
}

/* Giảm animation cho người dùng nhạy cảm */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}"""),

  (20,"Mobile-First Design",
   "Thực hành phương pháp mobile-first: thiết kế từ mobile rồi nâng cấp lên desktop.",
   "Mobile-first là phương pháp viết CSS cho mobile trước, sau đó dùng min-width "
   "media query để thêm style cho màn hình lớn hơn. Hiệu quả và tốt hơn desktop-first.",
   ["Viết CSS cho mobile (1 cột) làm mặc định",
    "Thêm @media (min-width: 768px) cho tablet (2 cột)",
    "Thêm @media (min-width: 1024px) cho desktop (3 cột)",
    "Compare: CSS mobile-first vs desktop-first cho cùng kết quả"],
   ["Mobile-first tiết kiệm dữ liệu: CSS nhỏ tải trước cho mobile",
    "Buộc designer suy nghĩ về nội dung quan trọng nhất",
    "Google ưu tiên mobile-friendly trong SEO",
    "min-width query: 'từ kích thước này TRỞ LÊN'",
    "Không cần override CSS mobile trong query – chỉ thêm mới"],
   """/* === MOBILE FIRST === */

/* Mặc định: mobile (< 768px) */
.container {
  width: 100%;
  padding: 0 16px;
}
.grid {
  display: grid;
  grid-template-columns: 1fr; /* 1 cột */
  gap: 16px;
}
.sidebar { display: none; } /* Ẩn sidebar trên mobile */
h1 { font-size: 1.5rem; }

/* Tablet (>= 768px) */
@media (min-width: 768px) {
  .container { max-width: 720px; margin: 0 auto; }
  .grid { grid-template-columns: repeat(2, 1fr); }
  h1 { font-size: 2rem; }
}

/* Desktop (>= 1024px) */
@media (min-width: 1024px) {
  .container { max-width: 1100px; }
  .layout { display: grid; grid-template-columns: 260px 1fr; }
  .sidebar { display: block; } /* Hiện sidebar */
  .grid { grid-template-columns: repeat(3, 1fr); }
  h1 { font-size: 2.5rem; }
}

/* Large Desktop (>= 1280px) */
@media (min-width: 1280px) {
  .container { max-width: 1200px; }
  .grid { grid-template-columns: repeat(4, 1fr); }
}"""),

  (21,"Responsive Navigation",
   "Tạo navbar responsive: menu ngang trên desktop, hamburger menu trên mobile.",
   "Navbar responsive là thử thách phổ biến: trên desktop hiện menu ngang, "
   "trên mobile menu ẩn và có nút hamburger để toggle.",
   ["Desktop: navbar ngang với links",
    "Mobile: links ẩn, hiện nút hamburger ☰",
    "Click hamburger: menu slide down dùng max-height transition",
    "Đóng menu khi click ngoài (dùng JavaScript)"],
   ["Mobile menu: <code>display:none</code> → khi toggle thêm class 'open' → <code>display:block</code>",
    "Transition height: dùng max-height thay vì height vì height:auto không transition được",
    "Hamburger: 3 div ngang, transform thành X khi mở",
    "Nên dùng aria-expanded và aria-label cho accessibility",
    "JavaScript: toggle class 'open' khi click hamburger"],
   """/* Navbar base */
.navbar { display: flex; justify-content: space-between; align-items: center; padding: 0 24px; height: 56px; background:#1a202c; }
.nav-logo { color:white; font-weight:bold; text-decoration:none; font-size:1.2rem; }
.nav-links { display:flex; list-style:none; gap:4px; margin:0; padding:0; }
.nav-links a { color:#a0aec0; text-decoration:none; padding:8px 12px; border-radius:6px; }
.nav-links a:hover { color:white; background:rgba(255,255,255,0.1); }
.hamburger { display:none; flex-direction:column; gap:5px; cursor:pointer; background:none; border:none; padding:8px; }
.hamburger span { display:block; width:22px; height:2px; background:white; transition:all 0.3s; }

/* Mobile */
@media (max-width:768px) {
  .hamburger { display:flex; }
  .nav-links { display:none; position:absolute; top:56px; left:0; right:0; flex-direction:column; background:#1a202c; padding:8px; }
  .nav-links.open { display:flex; }
}

/* Hamburger → X khi mở */
.hamburger.open span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: rotate(-45deg) translate(5px,-5px); }"""),

  (22,"Responsive Card Grid",
   "Tạo grid card sản phẩm tự động thay đổi số cột theo màn hình.",
   "Card grid là pattern phổ biến nhất trong web hiện đại. "
   "Dùng auto-fill/auto-fit + minmax để tạo grid responsive không cần media query.",
   ["Tạo grid 12 card sản phẩm tự responsive",
    "Mobile: 1 cột, Tablet: 2-3 cột, Desktop: 4 cột",
    "Card: ảnh, tên, giá, rating, nút thêm giỏ",
    "Hover effect: card nổi lên, ảnh zoom"],
   ["<code>repeat(auto-fill, minmax(240px, 1fr))</code>: tự tính số cột",
    "Card nên dùng <code>display:flex; flex-direction:column</code>",
    "<code>flex: 1</code> cho phần nội dung để card đều chiều cao",
    "Ảnh luôn cố định height + object-fit:cover",
    "Thêm <code>aspect-ratio: 4/3</code> cho ảnh giữ tỷ lệ"],
   """/* Grid responsive */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
  padding: 24px;
}

/* Card */
.product-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  transition: transform 0.3s, box-shadow 0.3s;
}
.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.15);
}
.product-card img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  transition: transform 0.4s;
}
.product-card:hover img { transform: scale(1.05); }

.card-body {
  padding: 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.card-price { color: #e53e3e; font-size: 1.2rem; font-weight: bold; margin-top: auto; }
.btn-cart {
  margin-top: 12px;
  padding: 10px;
  background: #3182ce;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-cart:hover { background: #2c5282; }"""),

  (23,"Responsive Typography",
   "Cài đặt typography responsive với fluid font-size và viewport units.",
   "Typography responsive đảm bảo chữ đọc được trên mọi kích thước màn hình. "
   "Fluid typography dùng clamp() để font tự scale mượt mà.",
   ["Dùng clamp() tạo font-size tự scale: h1 từ 1.8rem (mobile) đến 3.5rem (desktop)",
    "Cài đặt font-size tương đối bằng rem và em",
    "Thiết lập line-height và max-width tối ưu đọc (65-75 ký tự)",
    "Tạo modular type scale (ratio 1.25)"],
   ["<code>clamp(min, preferred, max)</code>: giá trị tự scale trong khoảng",
    "<code>clamp(1.5rem, 4vw, 3rem)</code>: min 1.5rem, tốt nhất 4vw, max 3rem",
    "<code>vw</code>: viewport width – 1vw = 1% chiều rộng màn hình",
    "Modular scale: mỗi cấp nhân với ratio (1.25 = Minor Third)",
    "<code>max-width: 65ch</code>: giới hạn 65 ký tự – tối ưu đọc"],
   """/* Fluid typography với clamp */
h1 { font-size: clamp(1.8rem, 5vw, 3.5rem); }
h2 { font-size: clamp(1.4rem, 4vw, 2.5rem); }
h3 { font-size: clamp(1.1rem, 3vw, 1.75rem); }
p  { font-size: clamp(0.95rem, 2vw, 1.1rem); }

/* Type scale 1.25 ratio */
:root {
  --text-xs:   0.64rem;
  --text-sm:   0.8rem;
  --text-base: 1rem;
  --text-lg:   1.25rem;
  --text-xl:   1.563rem;
  --text-2xl:  1.953rem;
  --text-3xl:  2.441rem;
  --text-4xl:  3.052rem;
}

/* Reading optimized */
.article-body {
  font-size: var(--text-lg);
  line-height: 1.8;
  max-width: 65ch;
  margin: 0 auto;
}

/* Responsive đơn giản với media query */
@media (max-width: 480px) {
  h1 { font-size: 1.8rem; }
  h2 { font-size: 1.4rem; }
}"""),

  (24,"Multi-level Dropdown Menu",
   "Tạo menu điều hướng có dropdown nhiều cấp bằng CSS thuần.",
   "Dropdown menu cho phép tổ chức nhiều link trong ít không gian. "
   "CSS-only dropdown dùng :hover để hiển thị menu con.",
   ["Tạo navbar có dropdown 2 cấp",
    "Dropdown hiển thị khi hover menu item",
    "Dropdown cấp 2 hiển thị bên phải cấp 1",
    "Transition mượt mà khi mở/đóng dropdown",
    "Hỗ trợ keyboard: :focus-within thay :hover"],
   ["<code>.dropdown:hover .dropdown-menu</code>: hiển thị khi hover",
    "Dropdown ẩn: <code>opacity:0; visibility:hidden; pointer-events:none</code> (dùng thay display:none để transition được)",
    "<code>visibility:hidden</code> + opacity khác với <code>display:none</code>: transition được",
    "<code>:focus-within</code>: mở dropdown khi focus bất kỳ child (keyboard accessible)",
    "Dropdown cấp 2: <code>left: 100%; top: 0</code>"],
   """.nav { display: flex; list-style: none; background: #1a202c; padding: 0 16px; }
.nav > li { position: relative; }
.nav a { color: #a0aec0; text-decoration: none; display: block; padding: 18px 16px; }
.nav > li:hover > a { color: white; background: rgba(255,255,255,0.1); }

/* Dropdown */
.dropdown-menu {
  position: absolute;
  top: 100%; left: 0;
  background: white;
  min-width: 200px;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-8px);
  transition: all 0.2s;
  z-index: 100;
}
.dropdown-menu a { color: #2d3748; padding: 10px 16px; }
.dropdown-menu a:hover { background: #ebf8ff; color: #3182ce; }

li:hover > .dropdown-menu,
li:focus-within > .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/* Level 2 – hiện bên phải */
.dropdown-menu .dropdown-menu { top: 0; left: 100%; }"""),

  (25,"Holy Grail Layout",
   "Xây dựng Holy Grail Layout kinh điển bằng CSS Flexbox và Grid.",
   "Holy Grail Layout (layout chén thánh) là pattern kinh điển gồm: header, "
   "3 cột (left sidebar, main, right sidebar), footer. Từng rất khó làm, nay dễ với flexbox/grid.",
   ["Tạo full layout: header, left sidebar, main, right sidebar, footer",
    "Header và footer full width",
    "3 cột giữa: sidebar-L 200px, main co giãn, sidebar-R 200px",
    "Footer luôn ở cuối trang dù nội dung ít",
    "Responsive: 2 sidebar thu về 0 trên mobile"],
   ["Flexbox approach: outer=column, middle section=row",
    "Grid approach: grid-template-areas 3 cột",
    "<code>min-height: 100vh</code> và <code>flex:1</code> cho middle section để footer xuống đáy",
    "Trên mobile: ẩn cả 2 sidebar, main full width",
    "Grid cách dễ hơn cho Holy Grail vì named areas trực quan"],
   """/* Grid approach – dễ và trực quan */
.holy-grail {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header  header"
    "sidebar main    aside"
    "footer  footer  footer";
  min-height: 100vh;
}

.hg-header  { grid-area: header;  background: #1a202c; color:white; padding:16px; }
.hg-sidebar { grid-area: sidebar; background: #f7fafc; padding:16px; }
.hg-main    { grid-area: main;    padding:24px; }
.hg-aside   { grid-area: aside;   background: #f7fafc; padding:16px; }
.hg-footer  { grid-area: footer;  background: #2d3748; color:#a0aec0; padding:16px; }

/* Responsive mobile */
@media (max-width: 768px) {
  .holy-grail {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "aside"
      "footer";
  }
}"""),

  (26,"Responsive Image Gallery",
   "Tạo thư viện ảnh responsive với lightbox bằng CSS và JavaScript tối thiểu.",
   "Gallery ảnh là bài toán thực tế phổ biến. Cần: grid responsive, "
   "hover overlay, click để xem ảnh lớn (lightbox).",
   ["Tạo gallery 12 ảnh dùng CSS Grid auto-fill",
    "Hover: overlay tối với biểu tượng phóng to",
    "Click ảnh: lightbox hiện ảnh lớn hơn",
    "Nút đóng lightbox",
    "Phím Escape để đóng lightbox"],
   ["Grid auto-fill + minmax cho gallery responsive không cần media query",
    "Overlay: position absolute, opacity 0 → 1 khi hover",
    "Lightbox: position fixed, z-index cao, full screen overlay",
    "JavaScript: thêm event listener click cho mỗi ảnh",
    "Nên có alt text tốt cho ảnh (accessibility + SEO)"],
   """/* Gallery grid */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
  padding: 24px;
}

/* Gallery item */
.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  cursor: pointer;
  aspect-ratio: 1;  /* vuông */
}
.gallery-item img { width:100%; height:100%; object-fit:cover; transition:transform 0.4s; }
.gallery-item:hover img { transform: scale(1.1); }

/* Hover overlay */
.gallery-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
  color: white;
  font-size: 2rem;
}
.gallery-item:hover .gallery-overlay { opacity: 1; }

/* Lightbox */
.lightbox {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.9);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
}
.lightbox img { max-width:100%; max-height:90vh; border-radius:8px; }
.lightbox-close { position:absolute; top:16px; right:24px; color:white; font-size:2rem; cursor:pointer; }"""),

  (27,"CSS Container Queries",
   "Dùng Container Queries để tạo component responsive theo kích thước container, không phải viewport.",
   "Container Queries là tính năng CSS hiện đại cho phép component tự điều chỉnh "
   "theo kích thước CONTAINER chứa nó – linh hoạt hơn media queries.",
   ["Khai báo container với container-type",
    "Viết @container query thay đổi layout card theo chiều rộng container",
    "So sánh card trong container nhỏ và container lớn"],
   ["<code>container-type: inline-size</code>: khai báo phần tử là container",
    "<code>@container (min-width: 400px) { }</code>: style khi container >= 400px",
    "Component sẽ thay đổi theo CONTAINER, không phải viewport",
    "container-name: đặt tên container để query cụ thể",
    "Hỗ trợ Chrome 105+, Firefox 110+, Safari 16+"],
   """/* Container Queries */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Mặc định: layout dọc (container nhỏ) */
.card {
  display: flex;
  flex-direction: column;
}
.card img { width: 100%; aspect-ratio: 16/9; object-fit: cover; }

/* Khi container >= 400px: layout ngang */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
  .card img {
    width: 160px;
    height: auto;
    aspect-ratio: auto;
  }
}

/* Khi container >= 600px: card to hơn */
@container card (min-width: 600px) {
  .card { padding: 24px; gap: 24px; }
  .card-title { font-size: 1.5rem; }
}"""),

  (28,"CSS Subgrid",
   "Dùng CSS Subgrid để các nested element căn thẳng hàng với grid ngoài.",
   "Subgrid cho phép một grid item chia sẻ grid lines với parent grid. "
   "Giải quyết nhu cầu căn chỉnh phức tạp nhiều hàng.",
   ["Tạo card grid mà tiêu đề, ảnh, description, button đều thẳng hàng dù nội dung khác độ dài",
    "Dùng grid-template-rows: subgrid để card con căn theo grid cha"],
   ["<code>grid-row: span N</code> để item chiếm đủ hàng",
    "<code>display: grid; grid-template-rows: subgrid</code>: chia sẻ rows của parent",
    "Subgrid giải quyết vấn đề card không đều chiều cao khi nội dung khác nhau",
    "Hỗ trợ Chrome 117+, Firefox 71+, Safari 16+",
    "Trước subgrid: dùng display:contents hoặc JavaScript để đo chiều cao"],
   """/* Parent grid */
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;  /* rows tự động */
  gap: 16px;
  align-items: start;
}

/* Card dùng subgrid để căn hàng */
.card {
  grid-row: span 4;  /* ảnh, tiêu đề, mô tả, button */
  display: grid;
  grid-template-rows: subgrid; /* chia sẻ rows của .cards */
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Tự động căn thẳng hàng dù nội dung khác nhau */
.card img { grid-row: 1; }
.card h3  { grid-row: 2; padding: 0 16px; }
.card p   { grid-row: 3; padding: 0 16px; color: #718096; }
.card .btn { grid-row: 4; margin: 0 16px 16px; align-self: end; }"""),

  (29,"CSS Scroll Snap",
   "Tạo scroll snap để trang 'khóa' vào các phần khi cuộn.",
   "Scroll Snap tạo trải nghiệm cuộn mượt mà: khi cuộn, trang tự động 'nhảy' "
   "vào section tiếp theo. Rất hay dùng cho landing page, slide, gallery.",
   ["Tạo landing page full-screen sections cuộn xuống theo snap",
    "Tạo horizontal scroll gallery với snap",
    "Scroll snap menu thumbnail video"],
   ["<code>scroll-snap-type: y mandatory</code>: snap theo chiều dọc, bắt buộc khóa",
    "<code>scroll-snap-align: start|center|end</code>: đặt trên scroll children",
    "<code>scroll-behavior: smooth</code>: cuộn mượt khi click anchor link",
    "mandatory: luôn khóa vào snap point (dùng cho full-page)",
    "proximity: chỉ khóa khi gần snap point (ít cưỡng bức hơn)"],
   """/* Full-page scroll snap */
html { scroll-behavior: smooth; }

.pages-container {
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
}

.page-section {
  height: 100vh;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  justify-content: center;
}
.page-section:nth-child(1) { background: linear-gradient(135deg,#667eea,#764ba2); }
.page-section:nth-child(2) { background: linear-gradient(135deg,#f093fb,#f5576c); }
.page-section:nth-child(3) { background: linear-gradient(135deg,#4facfe,#00f2fe); }

/* Horizontal scroll gallery */
.h-gallery {
  display: flex;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  gap: 16px;
  padding: 16px;
}
.h-gallery img {
  flex-shrink: 0;
  width: 80vw;
  scroll-snap-align: center;
  border-radius: 12px;
  object-fit: cover;
}"""),

  (30,"🏆 Dự án: Trang E-Commerce hoàn chỉnh",
   "Xây dựng trang thương mại điện tử responsive hoàn chỉnh bằng HTML + CSS.",
   "Dự án cuối module tổng hợp TẤT CẢ kiến thức layout đã học. "
   "Tạo trang e-commerce gồm header, hero, product grid, filters, footer responsive.",
   ["Header: logo, search bar, navigation, giỏ hàng – dùng Flexbox",
    "Hero banner: gradient, text lớn, CTA button",
    "Filter bar: tags lọc danh mục",
    "Product grid: responsive 1-4 cột, mỗi card có ảnh/tên/giá/rating/nút thêm giỏ",
    "Footer: 4 cột, responsive về 2 cột trên tablet và 1 cột mobile",
    "Toàn trang responsive từ 320px đến 1440px"],
   ["Dùng named grid areas cho page layout tổng thể",
    "Product grid: auto-fill + minmax để tự responsive",
    "Header: flex layout với search bar co giãn",
    "Mobile menu: hamburger toggle",
    "sticky header khi cuộn trang"],
   """/* Layout tổng thể */
body { margin:0; font-family:'Segoe UI',sans-serif; }
.page { display:grid; grid-template-rows:auto auto 1fr auto; min-height:100vh; }

/* Header */
.header { position:sticky; top:0; z-index:100; background:white; box-shadow:0 1px 8px rgba(0,0,0,0.1);
  display:flex; align-items:center; gap:16px; padding:0 24px; height:64px; }
.header-logo { font-size:1.4rem; font-weight:800; color:#e53e3e; white-space:nowrap; }
.header-search { flex:1; display:flex; }
.header-search input { flex:1; padding:10px 16px; border:2px solid #e2e8f0; border-right:none; border-radius:8px 0 0 8px; outline:none; }
.header-search button { padding:10px 16px; background:#e53e3e; color:white; border:none; border-radius:0 8px 8px 0; cursor:pointer; }
.cart-btn { position:relative; background:none; border:none; font-size:1.4rem; cursor:pointer; }
.cart-count { position:absolute; top:-6px; right:-6px; background:#e53e3e; color:white; font-size:11px; width:18px; height:18px; border-radius:50%; display:flex; align-items:center; justify-content:center; }

/* Hero */
.hero { background:linear-gradient(135deg,#667eea,#764ba2); color:white; text-align:center; padding:64px 24px; }
.hero h1 { font-size:clamp(2rem,5vw,3.5rem); margin-bottom:16px; }
.hero-btn { display:inline-block; padding:14px 40px; background:white; color:#764ba2; font-weight:bold; border-radius:999px; text-decoration:none; transition:transform .3s,box-shadow .3s; }
.hero-btn:hover { transform:translateY(-3px); box-shadow:0 12px 32px rgba(0,0,0,0.2); }

/* Products */
.products-section { padding:40px 24px; max-width:1200px; margin:0 auto; width:100%; box-sizing:border-box; }
.product-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:20px; margin-top:24px; }
.p-card { background:white; border-radius:12px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08); transition:transform .3s,box-shadow .3s; display:flex; flex-direction:column; }
.p-card:hover { transform:translateY(-4px); box-shadow:0 12px 24px rgba(0,0,0,0.15); }
.p-card img { width:100%; aspect-ratio:1; object-fit:cover; }
.p-body { padding:12px; flex:1; display:flex; flex-direction:column; }
.p-name { font-weight:600; margin-bottom:4px; }
.p-price { color:#e53e3e; font-size:1.1rem; font-weight:bold; margin-top:auto; }
.p-btn { margin-top:8px; padding:8px; background:#3182ce; color:white; border:none; border-radius:6px; cursor:pointer; }

/* Footer */
.footer { background:#1a202c; color:#a0aec0; padding:48px 24px 24px; }
.footer-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:32px; margin-bottom:32px; }
.footer h4 { color:white; margin-bottom:12px; }
@media(max-width:768px) { .footer-grid { grid-template-columns:repeat(2,1fr); } }
@media(max-width:480px) { .footer-grid { grid-template-columns:1fr; } .header-nav { display:none; } }"""),
]

count = 0
for num, title, short, desc, reqs, knows, code in exercises:
    folder = BASE / f"bai-{num:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    content = tpl(num, title, short, desc, reqs, knows, code)
    (folder / "index.html").write_text(content, encoding="utf-8")
    count += 1
    print(f"  ✓ bai-{num:02d}: {title}")

print(f"\nModule 3 – CSS Layout: Đã tạo {count} file")
