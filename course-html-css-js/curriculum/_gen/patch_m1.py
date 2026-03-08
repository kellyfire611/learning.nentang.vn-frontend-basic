#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_m1.py – Ba nhiệm vụ:
  1. Thêm SEO meta tags vào bai-01 đến bai-12 (thiếu SEO)
  2. Escape các thẻ HTML bị lọt vào text mô tả (bai-14, 20, 23, 25, 27, 28)
  3. Tạo thêm bài tập Đồ Án (bai-31 đến bai-35) – bài tổng hợp nâng cao
"""
import re, pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-01-html-co-ban")

# ─────────────────────────────────────────────────────────────────────────────
# PHẦN 1: Metadata cho bai-01 đến bai-12 (để thêm SEO)
# ─────────────────────────────────────────────────────────────────────────────
SEO_DATA = {
    "01": ("Cấu trúc cơ bản trang HTML",  "Tạo file HTML đầu tiên với cấu trúc chuẩn DOCTYPE, html, head, body."),
    "02": ("Thẻ tiêu đề h1 đến h6",        "Sử dụng 6 cấp độ tiêu đề để tạo mục lục cho một bài viết."),
    "03": ("Thẻ đoạn văn và ngắt dòng",    "Tạo trang văn bản có nhiều đoạn văn và ngắt dòng hợp lý."),
    "04": ("Định dạng văn bản",             "Dùng các thẻ bold, italic, underline, mark, strong, em để định dạng văn bản."),
    "05": ("Danh sách không có thứ tự ul",  "Tạo menu nhà hàng với danh sách không thứ tự ul và li."),
    "06": ("Danh sách có thứ tự ol",        "Tạo danh sách các bước hướng dẫn nấu ăn với ol và li."),
    "07": ("Danh sách lồng nhau",           "Tạo mục lục bài học có nhiều cấp độ lồng nhau với ul và ol."),
    "08": ("Danh sách định nghĩa dl",       "Tạo trang từ điển mini với dl, dt, dd trong HTML."),
    "09": ("Chèn hình ảnh img",             "Hiển thị hình ảnh đúng cách với các thuộc tính src, alt, width, height."),
    "10": ("Liên kết cơ bản thẻ a",         "Tạo trang tổng hợp liên kết có ích bằng thẻ a href."),
    "11": ("Liên kết mở tab mới",           "Tạo trang danh sách tài nguyên học tập, mở tab mới khi click."),
    "12": ("Liên kết neo Anchor Link",       "Tạo trang dài với mục lục điều hướng bằng anchor link."),
}

SEO_BLOCK = """  <meta name="keywords" content="Nền tảng,HTML,CSS,JavaScript,Lập trình,Web,Kiến thức,Đồ án">
  <meta name="author" content="Dương Nguyễn Phú Cường">
  <meta name="description" content="{desc}">
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Bài {num} – {title} | NenTang.vn">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://nentang.vn/">
  <meta property="og:site_name" content="Nền tảng Kiến thức">"""

VIEWPORT_PAT = re.compile(r'(<meta name="viewport"[^>]*/?>)', re.IGNORECASE)
TITLE_PAT    = re.compile(r'<title>([^<]+)</title>', re.IGNORECASE)

def patch_seo(num_str):
    f = BASE / f"bai-{num_str}" / "index.html"
    if not f.exists():
        print(f"SKIP (not found): bai-{num_str}")
        return
    src = f.read_text(encoding="utf-8")
    if 'og:title' in src:
        print(f"  ✓ bai-{num_str}: SEO đã có")
        return
    title, desc = SEO_DATA[num_str]
    block = SEO_BLOCK.format(num=num_str, title=title, desc=desc)
    # Also fix <title> to include NenTang.vn suffix if missing
    def fix_title(m):
        t = m.group(1).strip()
        if "NenTang.vn" not in t:
            t = t.rstrip() + " | NenTang.vn"
        return f"<title>{t}</title>"
    src = TITLE_PAT.sub(fix_title, src)
    # Insert SEO block after viewport meta
    new_src = VIEWPORT_PAT.sub(r'\1\n' + block, src)
    if new_src == src:
        print(f"  ⚠ bai-{num_str}: không tìm thấy viewport meta để chèn SEO")
    else:
        f.write_text(new_src, encoding="utf-8")
        print(f"  ✓ bai-{num_str}: đã thêm SEO")

print("\n[1] Thêm SEO cho bai-01 đến bai-12...")
for n in [f"{i:02d}" for i in range(1, 13)]:
    patch_seo(n)

# ─────────────────────────────────────────────────────────────────────────────
# PHẦN 2: Escape thẻ HTML bị lọt trong text mô tả
# ─────────────────────────────────────────────────────────────────────────────
ESCAPE_MAP = {
    # bai-14
    "14": [
        ("Các thẻ <thead>, <tbody>, <tfoot>", "Các thẻ &lt;thead&gt;, &lt;tbody&gt;, &lt;tfoot&gt;"),
    ],
    # bai-16
    "16": [
        ("Một số ký tự như <, >, &, ©, ™", "Một số ký tự như &lt;, &gt;, &amp;, ©, ™"),
    ],
    # bai-20
    "20": [
        ("Thẻ <select> tạo danh sách dropdown", "Thẻ &lt;select&gt; tạo danh sách dropdown"),
        ("Thẻ <textarea> cho phép",              "Thẻ &lt;textarea&gt; cho phép"),
    ],
    # bai-23
    "23": [
        ("Thẻ <figure> bọc nội dung",  "Thẻ &lt;figure&gt; bọc nội dung"),
        ("<figcaption> thêm chú thích","&lt;figcaption&gt; thêm chú thích"),
    ],
    # bai-25
    "25": [
        ("Meta tags nằm trong <head>", "Meta tags nằm trong &lt;head&gt;"),
    ],
    # bai-27
    "27": [
        ("HTML5 cung cấp thẻ <audio>", "HTML5 cung cấp thẻ &lt;audio&gt;"),
    ],
    # bai-28
    "28": [
        ("Thẻ <video> trong HTML5", "Thẻ &lt;video&gt; trong HTML5"),
    ],
}

print("\n[2] Escape thẻ HTML trong text mô tả...")
for num_str, fixes in ESCAPE_MAP.items():
    f = BASE / f"bai-{num_str}" / "index.html"
    if not f.exists():
        print(f"  ⚠ bai-{num_str}: không tìm thấy file")
        continue
    src = f.read_text(encoding="utf-8")
    changed = False
    for old, new in fixes:
        if old in src:
            src = src.replace(old, new)
            changed = True
    if changed:
        f.write_text(src, encoding="utf-8")
        print(f"  ✓ bai-{num_str}: đã fix escape")
    else:
        print(f"  ✓ bai-{num_str}: không cần fix (đã ok)")

print("\nHoàn thành SEO + escape fix!")
