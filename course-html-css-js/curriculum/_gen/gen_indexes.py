#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo file index.html đúng chuẩn cho module 3, 4, 5"""
import pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum")

SEO_COMMON = """  <meta name="keywords" content="Nền tảng,HTML,CSS,JavaScript,Lập trình,Web,Kiến thức,Đồ án">
  <meta name="author" content="Dương Nguyễn Phú Cường">"""

def module_index(mod_num, mod_slug, title, subtitle, star, exercises_data, accent_hover, accent_num):
    """exercises_data = list of (num, h3, p, tags_list)"""
    cards = ""
    for num, h3, p, tags in exercises_data:
        tag_spans = "".join(f'<span class="tag">{t}</span>' for t in tags)
        is_project = "ex-project" if ("Dự án" in h3 or "🏆" in h3) else ""
        cards += f"""
      <a href="bai-{num:02d}/index.html" class="exercise-card card-m{mod_num} {is_project}">
        <span class="num">Bài {num:02d}</span>
        <h3>{h3}</h3>
        <p>{p}</p>
        <div class="tags">{tag_spans}</div>
      </a>"""

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
{SEO_COMMON}
  <meta name="description" content="{subtitle}">
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Module {mod_num} – {title} | NenTang.vn">
  <meta property="og:description" content="{subtitle}">
  <meta property="og:url" content="https://nentang.vn/">
  <meta property="og:site_name" content="Nền tảng Kiến thức">
  <title>Module {mod_num} – {title} | NenTang.vn</title>
  <link rel="stylesheet" href="../shared.css" />
  <style>
    .card-m{mod_num}:hover {{ border-color: {accent_hover} !important; }}
    .card-m{mod_num} .num {{ color: {accent_num}; }}
    .ex-project {{ background: linear-gradient(135deg, #fffbeb, #fff); border-left-color: #f6ad55 !important; }}
  </style>
</head>
<body>
  <div class="page-header module-{mod_num}">
    <div class="breadcrumb"><a href="../index.html">← Trang Chủ</a></div>
    <h1>Module {mod_num}: {title}</h1>
    <p>{star} — 30 bài tập — {subtitle}</p>
  </div>

  <div class="container">
    <p class="section-title">Danh sách bài tập</p>
    <p class="section-subtitle">Click vào từng bài để xem yêu cầu và làm bài</p>

    <div class="exercises-grid">
{cards}
    </div>
  </div>
</body>
</html>"""

# ── MODULE 3: CSS Layout & Responsive ──────────────────────────────────────
m3 = [
  (1,  "Display: block inline inline-block none",    "Hiểu sự khác biệt giữa các giá trị display.",        ["display","block","inline"]),
  (2,  "Float: căn trái phải",                        "Dàn layout 2 cột bằng float left/right.",            ["float","layout"]),
  (3,  "Clearfix – Xử lý container bị sụp",           "Dùng clearfix để container chứa được phần tử float.", ["clearfix","float"]),
  (4,  "Position: static relative absolute",          "Phân biệt 3 kiểu định vị cơ bản.",                  ["position","relative","absolute"]),
  (5,  "Position: fixed và sticky",                   "Tạo header dính và nút cuộn lên đầu trang.",          ["fixed","sticky"]),
  (6,  "z-index – Thứ tự lớp chồng",                 "Kiểm soát thứ tự hiển thị phần tử chồng nhau.",      ["z-index","position"]),
  (7,  "Overflow: hidden scroll auto",                "Xử lý nội dung tràn ra ngoài container.",             ["overflow","scroll"]),
  (8,  "Flexbox: Container properties",               "display:flex, flex-direction, flex-wrap.",            ["flexbox","container"]),
  (9,  "Flexbox: justify-content và align-items",     "Căn chỉnh phần tử theo trục chính và phụ.",          ["flexbox","justify","align"]),
  (10, "Flexbox: flex-grow shrink basis",             "Kiểm soát kích thước linh hoạt của flex item.",      ["flex-grow","flex-shrink"]),
  (11, "Flexbox: order và align-self",                "Thay đổi thứ tự và căn chỉnh từng item riêng.",      ["order","align-self"]),
  (12, "Flexbox: Tạo Page Layout đầy đủ",             "Header – Sidebar – Content – Footer bằng Flexbox.",  ["flexbox","layout"]),
  (13, "Flexbox: Dashboard Card Grid",                "Lưới thẻ thống kê kiểu dashboard.",                  ["flexbox","grid","dashboard"]),
  (14, "CSS Grid: Cột và hàng cơ bản",               "grid-template-columns, rows, gap.",                   ["css-grid","columns"]),
  (15, "CSS Grid: row-gap, column-span",              "Trải phần tử qua nhiều cột / hàng.",                 ["grid","span"]),
  (16, "CSS Grid: Named Areas",                       "Đặt tên vùng lưới bằng grid-template-areas.",        ["grid","named-areas"]),
  (17, "CSS Grid: auto-fill và auto-fit",             "Lưới tự động co giãn số cột theo viewport.",         ["grid","auto-fill"]),
  (18, "CSS Grid: Newspaper Layout",                  "Bố cục báo nhiều cột phức tạp.",                     ["grid","newspaper"]),
  (19, "Media Queries – Responsive cơ bản",           "Thay đổi giao diện theo kích thước màn hình.",       ["media-query","responsive"]),
  (20, "Mobile-First Design",                         "Thiết kế từ màn hình nhỏ rồi mở rộng dần.",          ["mobile-first","responsive"]),
  (21, "Responsive Navigation",                       "Menu dọc trên mobile, ngang trên desktop.",           ["navbar","responsive"]),
  (22, "Responsive Card Grid",                        "Lưới thẻ tự động từ 1 đến 3 cột.",                   ["grid","responsive","card"]),
  (23, "Responsive Typography",                       "Cỡ chữ linh hoạt với clamp() và viewport units.",    ["typography","clamp","vw"]),
  (24, "Multi-level Dropdown Menu",                   "Menu nhiều cấp thuần CSS.",                           ["dropdown","navbar","css"]),
  (25, "Holy Grail Layout",                           "Bố cục kinh điển: header, 3 cột, footer.",           ["flexbox","grid","layout"]),
  (26, "Responsive Image Gallery",                    "Thư viện ảnh dạng masonry responsive.",               ["gallery","grid","responsive"]),
  (27, "CSS Container Queries",                       "Style phụ thuộc kích thước container.",               ["container-query","responsive"]),
  (28, "CSS Subgrid",                                 "Căn chỉnh lưới lồng nhau bằng subgrid.",             ["subgrid","grid"]),
  (29, "CSS Scroll Snap",                             "Scroll mượt dừng đúng vị trí.",                      ["scroll-snap","ux"]),
  (30, "🏆 Dự án: Trang E-Commerce hoàn chỉnh",      "Tổng hợp toàn bộ kỹ năng CSS Layout.",              ["project","e-commerce","responsive"]),
]

# ── MODULE 4: JavaScript Cơ Bản ────────────────────────────────────────────
m4 = [
  (1,  "Nhúng JavaScript vào HTML",                   "Internal script, external file, inline attribute.",   ["script","html","js"]),
  (2,  "Biến và kiểu dữ liệu",                        "var, let, const, typeof – 5 kiểu dữ liệu cơ bản.",  ["variable","typeof","js"]),
  (3,  "Toán tử số học và chuỗi",                     "+, -, *, /, %, **, nối chuỗi template literal.",     ["operator","arithmetic","js"]),
  (4,  "Toán tử so sánh và logic",                    "==, ===, !=, >, <, &&, ||, !",                        ["comparison","logic","js"]),
  (5,  "Câu lệnh if-else",                            "if / else if / else – phân nhánh điều kiện.",        ["if-else","condition","js"]),
  (6,  "Switch-case",                                  "Điều kiện nhiều nhánh với switch.",                   ["switch","case","js"]),
  (7,  "Toán tử ba ngôi (Ternary)",                   "condition ? trueVal : falseVal.",                     ["ternary","operator","js"]),
  (8,  "Vòng lặp for",                                "for, for…of, for…in – duyệt mảng và object.",        ["for-loop","iteration","js"]),
  (9,  "Vòng lặp while và do-while",                  "Lặp khi điều kiện đúng, kiểm tra trước/sau.",        ["while","do-while","js"]),
  (10, "Hàm (Function) cơ bản",                       "Khai báo hàm, tham số, giá trị trả về.",             ["function","return","js"]),
  (11, "Arrow Function",                               "Cú pháp ngắn gọn với =>.",                           ["arrow-function","es6","js"]),
  (12, "Mảng (Array) cơ bản",                         "push, pop, shift, unshift, indexOf, includes.",       ["array","js"]),
  (13, "Array Methods: slice, splice, find",           "Cắt, chèn, tìm kiếm trong mảng.",                   ["slice","splice","find"]),
  (14, "Array Methods: map, filter, reduce",           "Lập trình hàm với mảng.",                            ["map","filter","reduce"]),
  (15, "String Methods",                               "toUpperCase, trim, split, replace, includes.",        ["string","method","js"]),
  (16, "Math Object",                                  "Math.round, floor, ceil, random, max, min, abs.",    ["math","random","js"]),
  (17, "Date Object",                                  "Lấy ngày giờ hiện tại, format thời gian.",           ["date","time","js"]),
  (18, "DOM – querySelector và querySelectorAll",      "Chọn phần tử HTML bằng CSS selector.",               ["dom","querySelector","js"]),
  (19, "DOM – innerHTML và style",                     "Thay đổi nội dung và CSS trực tiếp.",                ["dom","innerHTML","js"]),
  (20, "DOM – classList",                              "add, remove, toggle, contains để thao tác class.",   ["classList","dom","js"]),
  (21, "DOM – createElement và appendChild",           "Tạo và chèn phần tử HTML động.",                    ["createElement","dom","js"]),
  (22, "DOM – addEventListener",                       "Lắng nghe sự kiện click, input, submit.",            ["event","addEventListener","js"]),
  (23, "Sự kiện Mouse và Keyboard",                   "mouseover, mouseout, keydown, keyup.",                ["mouse","keyboard","event"]),
  (24, "Form Validation bằng JavaScript",              "Kiểm tra dữ liệu nhập trước khi gửi form.",          ["form","validation","js"]),
  (25, "setTimeout và setInterval",                    "Trì hoãn và lặp lại thực thi hàm.",                  ["setTimeout","setInterval","timer"]),
  (26, "Xử lý Array nâng cao",                        "sort, flat, Object.entries, Object.keys.",            ["sort","flat","object"]),
  (27, "Closure và Scope",                             "Hiểu phạm vi biến, closure counter.",                ["closure","scope","js"]),
  (28, "Error Handling – try-catch",                   "Bắt lỗi và xử lý ngoại lệ.",                        ["try-catch","error","js"]),
  (29, "Local Storage",                                "Lưu và đọc dữ liệu trong trình duyệt.",              ["localStorage","storage","js"]),
  (30, "🏆 Dự án: Máy Tính Bỏ Túi",                  "Tổng hợp toàn bộ kiến thức JavaScript cơ bản.",     ["project","calculator","js"]),
]

# ── MODULE 5: JavaScript Nâng Cao ──────────────────────────────────────────
m5 = [
  (1,  "Object và Object Methods",                    "Tạo object, this, getter/setter.",                    ["object","method","js"]),
  (2,  "Destructuring và Spread/Rest",                "Destructure array/object, spread (...), rest params.", ["destructuring","spread","es6"]),
  (3,  "Callback Function",                            "Truyền hàm làm tham số, callback hell.",              ["callback","function","js"]),
  (4,  "Promise",                                      "resolve, reject, .then(), .catch(), Promise.all.",    ["promise","async","js"]),
  (5,  "Async/Await",                                  "Viết code bất đồng bộ theo phong cách đồng bộ.",     ["async","await","es8"]),
  (6,  "Fetch API – GET Request",                      "Gọi API và hiển thị dữ liệu JSON.",                  ["fetch","api","get"]),
  (7,  "Fetch API – POST, PUT, DELETE",                "Gửi và cập nhật dữ liệu lên server.",                ["fetch","post","rest"]),
  (8,  "JSON parse và stringify",                      "Chuyển đổi giữa JSON string và JS object.",          ["json","parse","stringify"]),
  (9,  "Regular Expressions (Regex)",                  "Tìm kiếm và thay thế chuỗi với regex.",              ["regex","regexp","js"]),
  (10, "Class và OOP",                                 "Constructor, kế thừa (extends), super.",             ["class","oop","extends"]),
  (11, "Prototype và Prototype Chain",                 "Object.create, __proto__, chuỗi kế thừa.",           ["prototype","inheritance","js"]),
  (12, "Module ES6 (import/export)",                   "Chia code thành nhiều file, export/import.",         ["module","import","export"]),
  (13, "Event Bubbling và Event Delegation",           "Sự kiện nổi bọt, delegate qua container cha.",       ["bubbling","delegation","event"]),
  (14, "IntersectionObserver – Lazy Loading",          "Tải ảnh trễ khi vào viewport.",                      ["intersection","lazy","observer"]),
  (15, "Debounce và Throttle",                         "Giới hạn tần suất gọi hàm.",                         ["debounce","throttle","performance"]),
  (16, "Countdown Timer",                              "Đồng hồ đếm ngược thời gian thực.",                  ["timer","countdown","setInterval"]),
  (17, "Image Slider / Carousel",                      "Slider ảnh tự động và điều hướng tay.",              ["slider","carousel","ui"]),
  (18, "Todo App đầy đủ",                             "Thêm, xóa, đánh dấu xong, lưu localStorage.",       ["todo","localStorage","crud"]),
  (19, "Real-time Search Filter",                      "Lọc danh sách theo từ khóa khi gõ.",                  ["search","filter","realtime"]),
  (20, "Dark Mode Toggle",                             "Chuyển đổi giao diện sáng/tối, ghi nhớ lựa chọn.",  ["darkmode","toggle","ux"]),
  (21, "Custom Dropdown Component",                    "Dropdown tùy chỉnh hoàn toàn bằng JS.",              ["dropdown","component","ui"]),
  (22, "Canvas API – Vẽ đồ họa",                     "Vẽ hình, văn bản, hoạt ảnh trên canvas.",            ["canvas","draw","animation"]),
  (23, "Advanced Form Validation",                     "Validate real-time với regex và tin nhắn lỗi tùy chỉnh.", ["form","validation","regex"]),
  (24, "Web Workers",                                  "Xử lý tác vụ nặng trên thread riêng.",               ["web-worker","thread","performance"]),
  (25, "Service Worker – Caching cơ bản",              "Làm ứng dụng hoạt động offline (PWA).",              ["service-worker","pwa","cache"]),
  (26, "Custom Event và Event Emitter",                "Tạo và phát sự kiện tùy chỉnh.",                     ["custom-event","emitter","js"]),
  (27, "IndexedDB – Lưu dữ liệu lớn",                "Database phía client cho dữ liệu có cấu trúc.",      ["indexeddb","storage","db"]),
  (28, "WebSocket – Real-time Communication",          "Giao tiếp hai chiều thời gian thực.",                ["websocket","realtime","network"]),
  (29, "TypeScript Basics",                            "Kiểu tĩnh, interface, type alias, generics cơ bản.", ["typescript","types","interface"]),
  (30, "🏆 Dự án: Weather App",                       "Ứng dụng thời tiết dùng OpenWeatherMap API.",        ["project","weather","api"]),
]

# ── Write files ─────────────────────────────────────────────────────────────
configs = [
  (3, "module-03-css-layout",        "CSS Layout & Responsive",  "★★★☆☆ Trung bình",  "Dàn trang web chuyên nghiệp với Float, Flexbox, CSS Grid và Responsive", m3, "#38f9d7", "#0d9488"),
  (4, "module-04-javascript-co-ban", "JavaScript Cơ Bản",       "★★★☆☆ Trung bình",  "Lập trình JavaScript từ biến, điều kiện đến DOM và Local Storage",        m4, "#fa709a", "#e53e8c"),
  (5, "module-05-javascript-nang-cao","JavaScript Nâng Cao",     "★★★★☆ Khó",         "OOP, Async/Await, Fetch API, Canvas, PWA và các dự án thực tế",          m5, "#a18cd1", "#7c3aed"),
]

for mod_num, slug, title, star, subtitle, exercises_data, accent_hover, accent_num in configs:
    content = module_index(mod_num, slug, title, subtitle, star, exercises_data, accent_hover, accent_num)
    path = BASE / slug / "index.html"
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {slug}/index.html")

print("Xong!")
