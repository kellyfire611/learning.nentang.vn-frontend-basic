#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo Module 5 – JavaScript Nâng Cao – 30 bài tập đầy đủ tiếng Việt"""
import pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-05-javascript-nang-cao")

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
  <div class="page-header module-5">
    <div class="breadcrumb">
      <a href="../../index.html">Trang Chủ</a> &rsaquo;
      <a href="../index.html">Module 5</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 5 – JavaScript Nâng Cao</p>
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
    const highlighted = await codeToHtml(raw, {{ lang: 'javascript', theme: 'github-dark' }});
    document.getElementById('code-highlight').innerHTML = highlighted;
    const pre = document.getElementById('code-highlight').querySelector('pre');
    if (pre) pre.style.cssText = 'border-radius:10px;padding:20px;font-size:0.87rem;overflow-x:auto;margin:0;line-height:1.7';
  </script>
</body>
</html>"""

exercises = [
  (1,"Object và Object Methods",
   "Tạo và làm việc với Object – kiểu dữ liệu nền tảng của JavaScript.",
   "Object lưu trữ dữ liệu dạng key-value. Gần như mọi thứ trong JS đều là object. "
   "Hiểu rõ Object là nền tảng để học OOP và JSON.",
   ["Tạo object sản phẩm với nhiều thuộc tính",
    "Thêm, sửa, xóa thuộc tính object",
    "Duyệt object bằng for...in và Object.entries()",
    "Computed property names: tên thuộc tính động"],
   ["<code>const obj = { key: value }</code>: object literal",
    "Truy cập: <code>obj.key</code> hoặc <code>obj['key']</code>",
    "<code>delete obj.key</code>: xóa thuộc tính",
    "<code>for (const key in obj) { }</code>: duyệt keys",
    "<code>Object.keys/values/entries(obj)</code>: mảng key/value/pair",
    "Computed property: <code>{ [tenBien]: value }</code>",
    "Shorthand: <code>{ ten, tuoi }</code> thay <code>{ ten: ten, tuoi: tuoi }</code>"],
   """// Object literal
const sanPham = {
  id: 1,
  ten: 'Áo Polo',
  gia: 250000,
  sizes: ['S','M','L','XL'],
  conHang: true,
};

// Shorthand property (ES6)
const ten = 'Nguyễn An'; const tuoi = 25;
const user = { ten, tuoi }; // { ten: 'Nguyễn An', tuoi: 25 }

// Thêm/sửa/xóa
sanPham.mau = 'Trắng';          // thêm
sanPham.gia = 300000;           // sửa
delete sanPham.conHang;         // xóa

// Computed property names
const field = 'mau';
const obj = { [field]: 'Đen' }; // { mau: 'Đen' }

// Duyệt object
Object.entries(sanPham).forEach(([key, val]) => {
  console.log(`${key}: ${val}`);
});

// Object methods
const keys   = Object.keys(sanPham);   // ['id','ten','gia',...]
const values = Object.values(sanPham); // [1,'Áo Polo',250000,...]

// Spread: copy + override
const spMoi = { ...sanPham, gia: 350000, id: 2 };

// Object.assign
const merged = Object.assign({}, sanPham, { id: 3 });"""),

  (2,"Destructuring và Spread/Rest",
   "Dùng destructuring để giải nén object/array và spread/rest để xử lý dữ liệu linh hoạt.",
   "Destructuring và spread/rest là cú pháp ES6 giúp code ngắn gọn hơn. "
   "Cực kỳ phổ biến trong React, API handling và function parameters.",
   ["Destructuring object: lấy tên, giá từ object sản phẩm",
    "Destructuring với giá trị mặc định và đổi tên",
    "Rest parameters trong function",
    "Spread: merge 2 object, clone array"],
   ["<code>const { ten, gia } = sanPham</code>: object destructuring",
    "<code>const { ten: name, gia = 0 } = sp</code>: đổi tên + mặc định",
    "<code>const [a, b, ...rest] = arr</code>: array destructuring + rest",
    "<code>function f(...args) { }</code>: rest parameters – mảng tất cả tham số",
    "<code>{ ...obj1, ...obj2 }</code>: merge objects (sau ghi đè trước)",
    "<code>[...arr1, ...arr2]</code>: merge arrays"],
   """// Object destructuring
const { ten, gia, mau = 'Không có' } = sanPham;
console.log(ten, gia); // 'Áo Polo', 250000

// Đổi tên khi destructure
const { ten: tenSP, gia: giaSP } = sanPham;

// Nested destructuring
const { dia_chi: { thanh_pho, quan } } = user;

// Array destructuring
const colors = ['đỏ', 'xanh', 'vàng'];
const [mau1, mau2, ...phanCon] = colors;
console.log(mau1, phanCon); // 'đỏ', ['vàng']

// Swap với destructuring
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b); // 2, 1

// Rest parameters trong function
function tong(...so) {
  return so.reduce((acc, n) => acc + n, 0);
}
console.log(tong(1, 2, 3, 4, 5)); // 15

// Spread để merge
const defaults = { color: 'white', size: 'M', inStock: true };
const custom   = { color: 'black', size: 'L' };
const final    = { ...defaults, ...custom }; // custom ghi đè defaults
console.log(final); // { color:'black', size:'L', inStock:true }

// Destructuring trong function parameter
function hienThi({ ten, gia, mau = 'N/A' }) {
  console.log(`${ten} – ${gia}đ – ${mau}`);
}
hienThi(sanPham);"""),

  (3,"Callback Function",
   "Hiểu và sử dụng callback – hàm được truyền như tham số cho hàm khác.",
   "Callback là nền tảng của lập trình bất đồng bộ trong JavaScript. "
   "Các array methods như map, filter, sort đều dùng callback.",
   ["Viết hàm xử lý danh sách với callback lọc tùy chỉnh",
    "Callback Error-first (Node.js style)",
    "Vấn đề Callback Hell và cách nhận biết"],
   ["Callback là function truyền vào function khác làm tham số",
    "Các array methods (map/filter/sort/forEach) đều dùng callback",
    "Callback bất đồng bộ: setTimeout, fetch, event listener",
    "Error-first callback: <code>function(err, data) { }</code> – quy ước Node.js",
    "Callback Hell: callback lồng callback lồng callback → khó đọc, khó debug",
    "Giải pháp cho callback hell: Promise hoặc async/await"],
   """// Callback cơ bản
function xuLyDanhSach(arr, locFn, sxFn, hienFn) {
  const loc = arr.filter(locFn);
  const sx  = loc.sort(sxFn);
  sx.forEach(hienFn);
}
xuLyDanhSach(
  sanPhams,
  sp => sp.gia < 500,              // lọc: giá < 500
  (a,b) => a.ten.localeCompare(b.ten), // sắp xếp: tên A-Z
  sp => console.log(sp.ten),       // in tên
);

// Error-first callback (Node.js style)
function layDuLieu(url, callback) {
  setTimeout(() => {
    const success = Math.random() > 0.3;
    if (!success) {
      callback(new Error('Không thể kết nối'), null);
    } else {
      callback(null, { data: [1,2,3] });
    }
  }, 500);
}
layDuLieu('/api/users', (err, data) => {
  if (err) { console.error('Lỗi:', err.message); return; }
  console.log('Dữ liệu:', data);
});

// Callback Hell – TRÁNH!
getData(id, (err, user) => {
  if (err) return;
  getPosts(user.id, (err, posts) => {
    if (err) return;
    getComments(posts[0].id, (err, comments) => {
      // Khó đọc, khó debug...
    });
  });
});
// → Dùng Promise hoặc async/await thay thế"""),

  (4,"Promise",
   "Dùng Promise để xử lý bất đồng bộ một cách rõ ràng hơn callback.",
   "Promise đại diện cho một giá trị sẽ có trong tương lai (hoặc lỗi). "
   "Giải quyết vấn đề callback hell bằng chuỗi .then().",
   ["Tạo Promise mô phỏng gọi API (setTimeout)",
    "Xử lý nhiều Promise song song với Promise.all()",
    "Chuỗi Promise: .then().then().catch()"],
   ["Promise có 3 trạng thái: pending, fulfilled, rejected",
    "<code>new Promise((resolve, reject) => { })</code>",
    "<code>resolve(data)</code>: thành công, <code>reject(err)</code>: thất bại",
    "<code>.then(data => { })</code>: xử lý thành công",
    "<code>.catch(err => { })</code>: xử lý lỗi",
    "<code>.finally(() => { })</code>: luôn chạy",
    "<code>Promise.all([p1,p2,p3])</code>: chờ TẤT CẢ thành công",
    "<code>Promise.race([p1,p2])</code>: lấy kết quả nào về trước"],
   """// Tạo Promise
function layUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id <= 0) reject(new Error('ID không hợp lệ'));
      else resolve({ id, ten: 'Nguyễn An', email: 'an@example.com' });
    }, 800);
  });
}

// Dùng Promise
layUser(1)
  .then(user => {
    console.log('User:', user.ten);
    return layBaiViet(user.id); // trả về Promise tiếp theo
  })
  .then(posts => console.log('Posts:', posts))
  .catch(err => console.error('Lỗi:', err.message))
  .finally(() => console.log('Hoàn tất'));

// Promise.all – chạy song song, chờ tất cả
Promise.all([layUser(1), layUser(2), layUser(3)])
  .then(([u1, u2, u3]) => {
    console.log(u1, u2, u3);
  })
  .catch(err => console.error('Một trong số bị lỗi:', err));

// Promise.allSettled – chờ tất cả, kể cả lỗi
Promise.allSettled([layUser(1), layUser(-1)])
  .then(results => {
    results.forEach(r => {
      if (r.status === 'fulfilled') console.log('OK:', r.value);
      else console.log('Lỗi:', r.reason.message);
    });
  });

// Promise.race – lấy kết quả đầu tiên
const timeout = new Promise((_, reject) => setTimeout(() => reject(new Error('Timeout')), 3000));
Promise.race([layUser(1), timeout]).then(console.log).catch(console.error);"""),

  (5,"Async/Await",
   "Viết code bất đồng bộ đọc như đồng bộ với async/await.",
   "async/await là cú pháp ES2017 xây dựng trên Promise. "
   "Giúp code bất đồng bộ dễ đọc như code tuần tự thông thường.",
   ["Viết lại đoạn Promise .then() thành async/await",
    "Dùng try-catch với async/await để xử lý lỗi",
    "Chạy song song với Promise.all trong async function"],
   ["<code>async function f() { }</code>: hàm trả về Promise",
    "<code>await promise</code>: chờ Promise resolve, chỉ dùng trong async function",
    "Lỗi: dùng try-catch (thay vì .catch())",
    "Chạy song song: <code>const [a,b] = await Promise.all([p1,p2])</code>",
    "KHÔNG dùng await trong vòng lặp forEach – dùng for-of hoặc Promise.all",
    "Top-level await (ES2022): dùng await ngoài function trong ES Module"],
   """// async/await cơ bản
async function layThongTinUser(id) {
  try {
    const user  = await layUser(id);      // chờ Promise
    const posts = await layBaiViet(user.id);
    return { user, posts };
  } catch (err) {
    console.error('Lỗi:', err.message);
    throw err; // re-throw để caller biết
  }
}

// Gọi async function
layThongTinUser(1).then(({ user, posts }) => {
  console.log(user.ten, posts.length);
});

// Hoặc dùng IIFE async
(async () => {
  const data = await layThongTinUser(1);
  console.log(data);
})();

// Song song đúng cách
async function layNhieuUser() {
  // SAI: chạy tuần tự – chậm
  // const u1 = await layUser(1);
  // const u2 = await layUser(2);

  // ĐÚNG: chạy song song – nhanh
  const [u1, u2] = await Promise.all([layUser(1), layUser(2)]);
  return [u1, u2];
}

// Async trong vòng lặp
async function xuLyNhieu(ids) {
  // ĐÚNG – for-of với await
  for (const id of ids) {
    const user = await layUser(id);
    console.log(user.ten);
  }
  // Hoặc song song:
  const users = await Promise.all(ids.map(id => layUser(id)));
}"""),

  (6,"Fetch API – GET Request",
   "Gọi API lấy dữ liệu từ server bằng Fetch API.",
   "Fetch API là cách hiện đại để gọi HTTP request trong JavaScript. "
   "Thay thế cho XMLHttpRequest cũ. Trả về Promise.",
   ["Fetch dữ liệu từ JSONPlaceholder API",
    "Hiển thị danh sách posts lên DOM",
    "Xử lý lỗi mạng và lỗi HTTP",
    "Loading state: hiện spinner khi đang tải"],
   ["<code>fetch(url)</code>: trả về Promise&lt;Response&gt;",
    "<code>response.ok</code>: true nếu status 200-299",
    "<code>await response.json()</code>: parse JSON body",
    "Luôn kiểm tra response.ok trước khi parse",
    "AbortController: hủy request đang chạy",
    "Dùng URL free: <code>https://jsonplaceholder.typicode.com/posts</code>"],
   """// Fetch cơ bản
async function layPosts() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=10');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const posts = await response.json();
    return posts;
  } catch (err) {
    if (err.name === 'AbortError') console.log('Request bị hủy');
    else console.error('Lỗi fetch:', err);
    return [];
  }
}

// Hiển thị lên DOM
async function hienThiPosts() {
  const list = document.getElementById('post-list');
  list.innerHTML = '<p class="loading">Đang tải...</p>';
  const posts = await layPosts();
  if (!posts.length) { list.innerHTML = '<p>Không có dữ liệu</p>'; return; }
  list.innerHTML = posts.map(p => `
    <article class="post-card">
      <h3>${p.title}</h3>
      <p>${p.body.slice(0, 100)}...</p>
    </article>
  `).join('');
}

// AbortController: hủy nếu quá 5 giây
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);

fetch('/api/slow', { signal: controller.signal })
  .then(r => r.json())
  .catch(err => {
    if (err.name === 'AbortError') alert('Tải quá lâu, đã hủy!');
  });"""),

  (7,"Fetch API – POST, PUT, DELETE",
   "Gửi dữ liệu lên server bằng POST, cập nhật bằng PUT, xóa bằng DELETE.",
   "CRUD là 4 thao tác cơ bản: Create (POST), Read (GET), Update (PUT), Delete (DELETE). "
   "Mỗi thao tác dùng HTTP method khác nhau.",
   ["POST: tạo mới bài viết với title và body",
    "PUT: cập nhật thông tin bài viết theo id",
    "DELETE: xóa bài viết theo id",
    "Hiển thị thông báo sau mỗi thao tác"],
   ["POST body phải là JSON.stringify(data)",
    "Headers: Content-Type: application/json",
    "PUT thay thế toàn bộ resource, PATCH chỉ thay đổi một phần",
    "DELETE thường không có body",
    "Response status: 201 Created, 200 OK, 204 No Content",
    "Tạo helper function để tái sử dụng fetch logic"],
   """// Helper: xử lý fetch chung
async function apiCall(url, method = 'GET', data = null) {
  const options = {
    method,
    headers: { 'Content-Type': 'application/json' },
  };
  if (data) options.body = JSON.stringify(data);
  const response = await fetch(url, options);
  if (!response.ok) throw new Error(`${method} ${url}: ${response.status}`);
  if (response.status === 204) return null; // No Content
  return response.json();
}

const BASE_URL = 'https://jsonplaceholder.typicode.com';

// CREATE – POST
async function taoPost(title, body) {
  const post = await apiCall(`${BASE_URL}/posts`, 'POST', { title, body, userId: 1 });
  console.log('Tạo thành công:', post.id);
  return post;
}

// UPDATE – PUT
async function capNhatPost(id, data) {
  const updated = await apiCall(`${BASE_URL}/posts/${id}`, 'PUT', data);
  console.log('Cập nhật thành công:', updated);
  return updated;
}

// DELETE
async function xoaPost(id) {
  await apiCall(`${BASE_URL}/posts/${id}`, 'DELETE');
  console.log('Đã xóa post', id);
}

// Chạy thử
(async () => {
  const p = await taoPost('Tiêu đề test', 'Nội dung test');
  await capNhatPost(p.id, { ...p, title: 'Tiêu đề đã sửa' });
  await xoaPost(p.id);
})();"""),

  (8,"JSON parse và stringify",
   "Chuyển đổi giữa JavaScript object và chuỗi JSON.",
   "JSON (JavaScript Object Notation) là định dạng trao đổi dữ liệu phổ biến nhất. "
   "JSON.parse() và JSON.stringify() là 2 hàm quan trọng khi làm việc với API.",
   ["Chuyển object thành JSON string",
    "Parse JSON string thành object",
    "JSON.stringify với tham số replacer và spaces",
    "Xử lý lỗi khi parse JSON không hợp lệ"],
   ["<code>JSON.stringify(obj)</code>: object → string",
    "<code>JSON.parse(str)</code>: string → object",
    "<code>JSON.stringify(obj, null, 2)</code>: format đẹp, indent 2 spaces",
    "JSON không hỗ trợ: undefined, function, Date (thành string), Symbol",
    "Deep clone: <code>JSON.parse(JSON.stringify(obj))</code> (không dùng cho hàm/Date phức tạp)",
    "structuredClone() (ES2022): deep clone tốt hơn"],
   """// stringify – object sang JSON
const user = {
  ten: 'Nguyễn An',
  tuoi: 25,
  hobbies: ['code', 'gym'],
  address: { thanh_pho: 'HCM' },
};

const jsonStr = JSON.stringify(user);
// '{"ten":"Nguyễn An","tuoi":25,...}'

const jsonDep = JSON.stringify(user, null, 2);
// Có indent dễ đọc – dùng để debug

// parse – JSON sang object
const obj = JSON.parse(jsonStr);
console.log(obj.ten); // 'Nguyễn An'

// Lỗi JSON
try {
  JSON.parse('{ sai cú pháp }');
} catch (e) {
  console.error('JSON lỗi!', e.message);
}

// Replacer: chọn fields cần serialize
const partial = JSON.stringify(user, ['ten', 'tuoi']);
// Chỉ có ten và tuoi

// Reviver: transform khi parse
const json2 = '{"ngaySinh":"2000-01-15"}';
const parsed = JSON.parse(json2, (key, value) => {
  if (key === 'ngaySinh') return new Date(value);
  return value;
});
console.log(parsed.ngaySinh instanceof Date); // true

// Deep clone (an toàn cho các object cơ bản)
const clone = JSON.parse(JSON.stringify(user));
clone.ten = 'Khác'; // Không ảnh hưởng user gốc"""),

  (9,"Regular Expressions (Regex)",
   "Dùng Regular Expression để tìm kiếm và validate chuỗi nâng cao.",
   "Regex là ngôn ngữ con để xử lý chuỗi theo pattern. "
   "Cực kỳ mạnh cho validation, search-replace, extract data.",
   ["Validate email, số điện thoại VN, ngày sinh",
    "Tìm và thay thế tất cả từ bằng regex",
    "Extract số từ chuỗi hỗn hợp"],
   ["Tạo regex: <code>/pattern/flags</code> hoặc <code>new RegExp('pattern', 'flags')</code>",
    "Flags: g (global-tìm tất cả), i (case-insensitive), m (multiline)",
    "<code>regex.test(str)</code>: true/false",
    "<code>str.match(regex)</code>: mảng kết quả",
    "<code>str.replace(regex, rep)</code>: thay thế",
    "Các metachar: . * + ? ^ $ [] {} () | \\"],
   r"""// Validate email
const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
console.log(emailReg.test('user@example.com'));  // true
console.log(emailReg.test('khong-hop-le'));      // false

// Số điện thoại Việt Nam: 0[35789]xxxxxxxx
const sdtReg = /^(0|\+84)[35789]\d{8}$/;
console.log(sdtReg.test('0901234567'));  // true
console.log(sdtReg.test('01209999999')); // false

// Extract tất cả số trong chuỗi
const text = 'Mua 3 áo giá 150k và 2 quần giá 200k';
const so_match = text.match(/\d+/g);
console.log(so_match); // ['3', '150', '2', '200']

// Replace với regex global
const dirty = 'Hello   World   JavaScript';
const clean = dirty.replace(/\s+/g, ' ').trim();
console.log(clean); // 'Hello World JavaScript'

// Capture groups
const dateStr = '2024-12-31';
const [, nam, thang, ngay] = dateStr.match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(nam, thang, ngay); // '2024' '12' '31'

// Named groups (ES2018)
const { groups: { year, month } } = '2024-12'.match(/(?<year>\d{4})-(?<month>\d{2})/);
console.log(year, month); // '2024' '12'"""),

  (10,"Class và OOP",
   "Viết code hướng đối tượng với class trong JavaScript.",
   "ES6 class giúp tổ chức code theo mô hình OOP (Object-Oriented Programming). "
   "Class là cú pháp sugar trên prototype-based system của JS.",
   ["Tạo class SanPham với constructor và methods",
    "Kế thừa: SanPhamKhuyenMai extends SanPham",
    "Private field (#) và static method",
    "Getter/setter"],
   ["<code>class Animal { constructor() {} method() {} }</code>",
    "<code>extends</code>: kế thừa",
    "<code>super()</code>: gọi constructor cha",
    "Private field: <code>#privateField</code> (chỉ truy cập trong class)",
    "<code>static</code>: method/property thuộc class, không phải instance",
    "Getter/setter: <code>get prop() { }</code> / <code>set prop(val) { }</code>"],
   """class SanPham {
  #id;  // Private field
  static count = 0;

  constructor(ten, gia) {
    SanPham.count++;
    this.#id   = SanPham.count;
    this.ten   = ten;
    this._gia  = gia;
    this.tags  = [];
  }

  // Getter
  get gia() { return this._gia; }
  // Setter với validation
  set gia(val) {
    if (val < 0) throw new Error('Giá không thể âm');
    this._gia = val;
  }

  get id() { return this.#id; }

  themTag(...tags) { this.tags.push(...tags); return this; } // chaining
  thongTin() { return `[${this.#id}] ${this.ten}: ${this._gia.toLocaleString()}đ`; }
  toString() { return this.thongTin(); }

  static timTheoTen(ds, ten) { return ds.find(sp => sp.ten === ten); }
}

// Kế thừa
class SanPhamKM extends SanPham {
  constructor(ten, gia, giam) {
    super(ten, gia); // BẮT BUỘC gọi super()
    this.giam = giam;
  }
  get giaKM() { return this.gia * (1 - this.giam / 100); }
  thongTin() { return `${super.thongTin()} (giảm ${this.giam}% → ${this.giaKM.toLocaleString()}đ)`; }
}

const ao = new SanPhamKM('Áo Polo', 250000, 20);
console.log(ao.thongTin()); // [1] Áo Polo: 250,000đ (giảm 20% → 200,000đ)
console.log(SanPham.count); // số sản phẩm đã tạo"""),

  (11,"Prototype và Prototype Chain",
   "Hiểu cơ chế prototype – nền tảng thực sự của OOP trong JavaScript.",
   "JavaScript là prototype-based language. Class chỉ là sugar syntax. "
   "Hiểu prototype giúp debug và optimize code hiệu quả hơn.",
   ["Thêm method vào Array.prototype và String.prototype",
    "Kiểm tra prototype chain với instanceof",
    "Object.create() để tạo object với prototype tùy chỉnh"],
   ["Mỗi object có thuộc tính __proto__ trỏ đến prototype của constructor",
    "Khi gọi method: JS tìm trong object → prototype → prototype của prototype... → null",
    "<code>Object.getPrototypeOf(obj)</code>: lấy prototype",
    "<code>obj instanceof Class</code>: kiểm tra prototype chain",
    "Thêm vào prototype: <code>Array.prototype.myMethod = fn</code>",
    "KHÔNG nên sửa prototype của built-in (Array, String...) trong production"],
   """// Prototype chain
function Animal(name) { this.name = name; }
Animal.prototype.speak = function() { return `${this.name} kêu!`; };

function Dog(name, breed) {
  Animal.call(this, name); // gọi constructor cha
  this.breed = breed;
}
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
Dog.prototype.fetch = function() { return `${this.name} đi lấy bóng!`; };

const rex = new Dog('Rex', 'Husky');
console.log(rex.speak());  // Rex kêu!   (kế thừa từ Animal)
console.log(rex.fetch());  // Rex đi lấy bóng!
console.log(rex instanceof Dog);    // true
console.log(rex instanceof Animal); // true

// Prototype chain: rex → Dog.prototype → Animal.prototype → Object.prototype → null
console.log(Object.getPrototypeOf(rex) === Dog.prototype); // true

// Thêm method vào Array (chỉ demo, không làm trong production)
if (!Array.prototype.sum) {
  Array.prototype.sum = function() { return this.reduce((a,b) => a+b, 0); };
}
console.log([1,2,3,4,5].sum()); // 15

// Object.create
const animal = { speak() { return 'Kêu!'; } };
const dog = Object.create(animal);
dog.fetch = function() { return 'Lấy bóng!'; };
console.log(dog.speak()); // Kêu! (kế thừa từ animal)"""),

  (12,"Module ES6 (import/export)",
   "Tổ chức code thành các module với import và export.",
   "Modules giúp tách code thành file nhỏ, tái sử dụng. "
   "ES6 Module là chuẩn JavaScript hiện đại, hỗ trợ trên browser và Node.js.",
   ["Xuất hàm và class từ module",
    "Import cụ thể, import all, import default",
    "Re-export từ module khác",
    "Dùng type='module' trong thẻ script"],
   ["<code>export function f() { }</code>: named export",
    "<code>export default class X { }</code>: default export (1 file 1 default)",
    "<code>import { f } from './module.js'</code>: import named",
    "<code>import X from './module.js'</code>: import default",
    "<code>import * as utils from './utils.js'</code>: import tất cả",
    "HTML: <code>&lt;script type='module' src='app.js'&gt;</code>",
    "Module luôn ở strict mode, defer tự động, scope riêng"],
   """// === utils.js ===
export const PI = 3.14159;

export function tinhChuVi(r) { return 2 * PI * r; }
export function tinhDienTich(r) { return PI * r * r; }

// === api.js ===
const BASE = 'https://api.example.com';
export async function layDuLieu(path) {
  const res = await fetch(BASE + path);
  return res.json();
}
export default { layDuLieu }; // default export

// === models/User.js ===
export class User {
  constructor(data) { Object.assign(this, data); }
  get initials() { return this.ten.split(' ').map(w=>w[0]).join(''); }
}

// === app.js (main) ===
import { PI, tinhChuVi, tinhDienTich } from './utils.js';
import api from './api.js';           // default import
import { User } from './models/User.js';
import * as Calc from './utils.js';   // namespace import

console.log(tinhChuVi(5));     // 31.41...
console.log(Calc.tinhDienTich(3)); // 28.27...

// Dynamic import – load khi cần
const btn = document.getElementById('load');
btn.addEventListener('click', async () => {
  const { Chart } = await import('./chart.js'); // lazy load
  new Chart('#canvas', data);
});"""),

  (13,"Event Bubbling và Event Delegation",
   "Hiểu cơ chế event bubbling để dùng event delegation hiệu quả.",
   "Sự kiện trong DOM 'nổi bong bóng' từ phần tử con lên parent. "
   "Event delegation tận dụng điều này để gắn 1 listener thay vì nhiều listeners.",
   ["Demo event bubbling: click con, parent cũng nhận sự kiện",
    "stopPropagation: ngăn bubbling",
    "Event delegation cho danh sách động"],
   ["Bubbling: click p → p fires → div fires → body fires → document fires",
    "<code>event.stopPropagation()</code>: dừng bubble lên",
    "<code>event.target</code>: phần tử gây sự kiện (con)",
    "<code>event.currentTarget</code>: phần tử đang lắng nghe (parent)",
    "Delegation: gắn listener ở parent, xử lý con bằng e.target",
    "Capturing: sự kiện đi từ trên xuống (ít dùng, dùng {capture:true})"],
   """// Bubbling demo
document.querySelector('.outer').addEventListener('click', () => console.log('Outer'));
document.querySelector('.middle').addEventListener('click', () => console.log('Middle'));
document.querySelector('.inner').addEventListener('click', (e) => {
  e.stopPropagation(); // Ngăn bubble lên outer và middle
  console.log('Inner');
});
// Click Inner → chỉ in 'Inner' (nếu có stopPropagation)
// Click Inner → in 'Inner', 'Middle', 'Outer' (nếu không có)

// Event Delegation – cực kỳ hữu dụng
const ul = document.getElementById('todo-list');
ul.addEventListener('click', (e) => {
  // Kiểm tra phần tử được click là gì
  if (e.target.matches('.btn-done')) {
    e.target.closest('li').classList.toggle('done');
  }
  if (e.target.matches('.btn-delete')) {
    e.target.closest('li').remove();
  }
  if (e.target.matches('.btn-edit')) {
    const li = e.target.closest('li');
    const span = li.querySelector('.text');
    const newText = prompt('Sửa:', span.textContent);
    if (newText) span.textContent = newText;
  }
});
// Tất cả nằm trong 1 listener – kể cả li được thêm sau!"""),

  (14,"IntersectionObserver – Lazy Loading",
   "Dùng IntersectionObserver để lazy load ảnh và trigger animation khi scroll.",
   "IntersectionObserver theo dõi khi phần tử vào/ra khỏi viewport. "
   "Dùng để lazy load ảnh, trigger animation, infinite scroll.",
   ["Lazy load ảnh: chỉ tải khi sắp vào viewport",
    "Fade-in animation khi element scroll vào view",
    "Infinite scroll: tải thêm data khi scroll xuống dưới"],
   ["<code>new IntersectionObserver(callback, options)</code>",
    "<code>observer.observe(el)</code>: bắt đầu theo dõi",
    "<code>observer.unobserve(el)</code>: dừng theo dõi phần tử đó",
    "<code>entry.isIntersecting</code>: true khi vào viewport",
    "<code>entry.intersectionRatio</code>: tỷ lệ phần tử trong viewport (0-1)",
    "threshold: 0 (bất kỳ pixel nào), 0.5 (50%), 1 (toàn bộ)"],
   """// Lazy load ảnh
const imageObserver = new IntersectionObserver((entries, obs) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const img = entry.target;
    img.src = img.dataset.src;  // data-src → src thực
    img.classList.add('loaded');
    obs.unobserve(img);         // Dừng theo dõi sau khi load
  });
}, { rootMargin: '200px' }); // Tải trước khi vào view 200px

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});

// Scroll animation
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  animObserver.observe(el);
});

// Infinite scroll: sentinel element ở cuối
const sentinel = document.getElementById('sentinel');
const scrollObserver = new IntersectionObserver(async (entries) => {
  if (entries[0].isIntersecting) {
    const morePosts = await fetchMorePosts(currentPage++);
    appendPosts(morePosts);
  }
});
scrollObserver.observe(sentinel);"""),

  (15,"Debounce và Throttle",
   "Tối ưu hiệu năng với debounce và throttle cho sự kiện tần suất cao.",
   "Scroll, resize, input gây ra hàng trăm sự kiện mỗi giây. "
   "Debounce và throttle giới hạn tần suất gọi hàm để tránh lag.",
   ["Debounce input search: chỉ tìm kiếm sau 300ms dừng gõ",
    "Throttle scroll handler: chỉ cập nhật mỗi 100ms",
    "So sánh hành vi debounce vs throttle"],
   ["Debounce: chờ N ms sau lần gọi CUỐI, rồi thực thi (1 lần)",
    "Throttle: thực thi tối đa 1 lần mỗi N ms",
    "Debounce dùng cho: search input, window resize",
    "Throttle dùng cho: scroll, mouse move, game loop",
    "lodash có sẵn _.debounce và _.throttle"],
   """// Debounce implementation
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// Throttle implementation
function throttle(fn, limit) {
  let lastRun = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastRun >= limit) {
      lastRun = now;
      fn.apply(this, args);
    }
  };
}

// Debounce search input
const timKiem = debounce((query) => {
  console.log('Tìm kiếm:', query);
  fetch(`/api/search?q=${query}`).then(r => r.json()).then(render);
}, 300);

document.getElementById('search').addEventListener('input', (e) => {
  timKiem(e.target.value);
});

// Throttle scroll
const xuLyScroll = throttle(() => {
  const scrollY = window.scrollY;
  // Hiện/ẩn header, back-to-top button...
  document.getElementById('header').classList.toggle('sticky', scrollY > 100);
}, 100);

window.addEventListener('scroll', xuLyScroll);

// requestAnimationFrame throttle (tốt hơn cho animation)
let rafId;
window.addEventListener('scroll', () => {
  cancelAnimationFrame(rafId);
  rafId = requestAnimationFrame(() => {
    // Code cập nhật UI
  });
});"""),

  (16,"Countdown Timer",
   "Tạo countdown timer đếm ngược đến sự kiện đặc biệt.",
   "Countdown timer là bài tập thực hành tổng hợp: Date, setInterval, DOM manipulation. "
   "Hiển thị ngày, giờ, phút, giây đếm ngược.",
   ["Countdown đến ngày lễ hoặc sự kiện quan trọng",
    "Hiển thị: ngày, giờ, phút, giây dưới dạng card",
    "Khi hết giờ: hiển thị 'Đã đến rồi!' và confetti",
    "Tự động dừng setInterval khi hết giờ"],
   ["<code>target.getTime() - Date.now()</code>: milliseconds còn lại",
    "Chia để lấy ngày: <code>Math.floor(diff / 86400000)</code>",
    "Giờ còn lại: <code>Math.floor((diff % 86400000) / 3600000)</code>",
    "String.padStart(2, '0'): thêm số 0 phía trước",
    "clearInterval khi diff <= 0 để dừng timer"],
   """// Countdown Timer
const TARGET = new Date('2025-01-01T00:00:00');

function tinhConLai() {
  const now = new Date();
  const diff = TARGET - now;
  if (diff <= 0) return null;
  return {
    ngay:   Math.floor(diff / (1000 * 60 * 60 * 24)),
    gio:    Math.floor((diff / (1000 * 60 * 60)) % 24),
    phut:   Math.floor((diff / (1000 * 60)) % 60),
    giay:   Math.floor((diff / 1000) % 60),
  };
}

function capNhat() {
  const t = tinhConLai();
  if (!t) {
    clearInterval(timer);
    document.getElementById('countdown').innerHTML =
      '<h2 class="celebrate">🎉 Chúc mừng Năm Mới! 🎉</h2>';
    return;
  }
  const fmt = n => String(n).padStart(2, '0');
  document.getElementById('days').textContent   = fmt(t.ngay);
  document.getElementById('hours').textContent  = fmt(t.gio);
  document.getElementById('minutes').textContent = fmt(t.phut);
  document.getElementById('seconds').textContent = fmt(t.giay);
}

capNhat();
const timer = setInterval(capNhat, 1000);

/* HTML:
<div id="countdown">
  <div class="time-block"><span id="days">00</span><label>Ngày</label></div>
  <div class="time-block"><span id="hours">00</span><label>Giờ</label></div>
  <div class="time-block"><span id="minutes">00</span><label>Phút</label></div>
  <div class="time-block"><span id="seconds">00</span><label>Giây</label></div>
</div> */"""),

  (17,"Image Slider / Carousel",
   "Tạo image slider tự động và có điều khiển bằng JavaScript.",
   "Slider là component phổ biến trong web. Bài này thực hành: DOM, "
   "setInterval, event listener, CSS transition.",
   ["Tạo slider với 5 ảnh",
    "Nút prev/next để chuyển ảnh",
    "Dot indicators ở dưới",
    "Tự động chuyển mỗi 4 giây, dừng khi hover",
    "Transition mượt mà"],
   ["Slider state: currentIndex, total slides, isPlaying",
    "CSS transform: translateX() để dịch chuyển slides",
    "Modulo (%) để vòng lại index: <code>(n + total) % total</code>",
    "mouseenter/mouseleave để pause/resume auto-play",
    "Touch events: touchstart/touchend để swipe trên mobile"],
   """class Slider {
  constructor(container) {
    this.container  = container;
    this.slides     = container.querySelectorAll('.slide');
    this.dots       = container.querySelectorAll('.dot');
    this.total      = this.slides.length;
    this.current    = 0;
    this.autoTimer  = null;
    this.init();
  }
  init() {
    container.querySelector('.prev').addEventListener('click', () => this.prev());
    container.querySelector('.next').addEventListener('click', () => this.next());
    this.dots.forEach((dot, i) => dot.addEventListener('click', () => this.goTo(i)));
    container.addEventListener('mouseenter', () => this.pause());
    container.addEventListener('mouseleave', () => this.play());
    this.goTo(0);
    this.play();
  }
  goTo(n) {
    this.slides[this.current].classList.remove('active');
    this.dots[this.current]?.classList.remove('active');
    this.current = ((n % this.total) + this.total) % this.total;
    this.slides[this.current].classList.add('active');
    this.dots[this.current]?.classList.add('active');
  }
  next() { this.goTo(this.current + 1); }
  prev() { this.goTo(this.current - 1); }
  play() { this.autoTimer = setInterval(() => this.next(), 4000); }
  pause() { clearInterval(this.autoTimer); }
}

new Slider(document.getElementById('mySlider'));"""),

  (18,"Todo App đầy đủ",
   "Xây dựng ứng dụng Todo hoàn chỉnh với thêm, sửa, xóa, lọc và lưu localStorage.",
   "Todo App là project thực hành kinh điển tổng hợp: DOM, events, "
   "array manipulation, localStorage. Implement đủ 4 thao tác CRUD.",
   ["Thêm todo mới khi nhấn Enter hoặc nút +",
    "Đánh dấu hoàn thành khi click checkbox",
    "Xóa todo, sửa todo inline",
    "Lọc: All / Active / Completed",
    "Lưu vào localStorage, load khi mở lại",
    "Đếm số việc chưa xong"],
   ["State trung tâm: mảng todos",
    "Mỗi action: cập nhật state → re-render → lưu localStorage",
    "Filter chỉ ảnh hưởng hiển thị, không ảnh hưởng data",
    "Edit inline: click label → input, blur → lưu",
    "ID: dùng Date.now() để tạo unique id đơn giản"],
   """// State
let todos = JSON.parse(localStorage.getItem('todos') || '[]');
let filter = 'all'; // 'all' | 'active' | 'done'

// Actions
const addTodo = (text) => {
  if (!text.trim()) return;
  todos.push({ id: Date.now(), text: text.trim(), done: false });
  save(); render();
};
const toggleTodo = (id) => {
  todos = todos.map(t => t.id === id ? {...t, done: !t.done} : t);
  save(); render();
};
const deleteTodo  = (id) => { todos = todos.filter(t => t.id !== id); save(); render(); };
const editTodo    = (id, text) => {
  if (!text.trim()) { deleteTodo(id); return; }
  todos = todos.map(t => t.id === id ? {...t, text: text.trim()} : t);
  save(); render();
};
const clearDone = () => { todos = todos.filter(t => !t.done); save(); render(); };
const save = () => localStorage.setItem('todos', JSON.stringify(todos));

// Render
function render() {
  const filtered = todos.filter(t =>
    filter === 'all' ? true : filter === 'active' ? !t.done : t.done
  );
  const list = document.getElementById('todo-list');
  list.innerHTML = filtered.length ? filtered.map(t => `
    <li class="${t.done ? 'done' : ''}" data-id="${t.id}">
      <input type="checkbox" ${t.done?'checked':''} class="cb" />
      <span class="text" contenteditable="true">${t.text}</span>
      <button class="del">✕</button>
    </li>`).join('') : '<li class="empty">Không có việc nào</li>';
  document.getElementById('count').textContent = todos.filter(t=>!t.done).length;
}

// Events
document.getElementById('new-input').addEventListener('keydown', e => {
  if (e.key === 'Enter') { addTodo(e.target.value); e.target.value = ''; }
});
document.getElementById('todo-list').addEventListener('click', e => {
  const id = +e.target.closest('li')?.dataset.id;
  if (!id) return;
  if (e.target.matches('.cb')) toggleTodo(id);
  if (e.target.matches('.del')) deleteTodo(id);
});
document.getElementById('todo-list').addEventListener('blur', e => {
  if (e.target.matches('.text')) editTodo(+e.target.closest('li').dataset.id, e.target.textContent);
}, true);

render();"""),

  (19,"Real-time Search Filter",
   "Tạo tính năng tìm kiếm/lọc danh sách theo thời gian thực khi gõ.",
   "Real-time search là tính năng UX quan trọng: lọc ngay khi người dùng gõ, "
   "highlight từ khóa, không cần nút tìm kiếm.",
   ["Lọc danh sách sinh viên theo tên khi gõ",
    "Highlight từ khóa trong kết quả (đánh dấu vàng)",
    "Thông báo 'Không tìm thấy' khi không có kết quả",
    "Debounce 200ms để không chạy quá nhiều lần"],
   ["Lọc dữ liệu: <code>arr.filter(item => item.ten.toLowerCase().includes(query))</code>",
    "Highlight: thay thế từ khóa bằng <code>&lt;mark&gt;từ&lt;/mark&gt;</code>",
    "Cẩn thận XSS khi dùng innerHTML với input người dùng",
    "Escape HTML trước khi dùng innerHTML",
    "Regex cho highlight chính xác và case-insensitive"],
   """const danhSach = [
  { id:1, ten:'Nguyễn Văn An', lop:'12A1', email:'an@school.vn' },
  { id:2, ten:'Trần Thị Bình', lop:'12B2', email:'binh@school.vn' },
  // ...
];

function escapeHtml(str) {
  return str.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
}

function highlight(text, query) {
  if (!query) return escapeHtml(text);
  const escaped = escapeHtml(text);
  const re = new RegExp(`(${escapeHtml(query)})`, 'gi');
  return escaped.replace(re, '<mark>$1</mark>');
}

const timKiem = debounce((query) => {
  const q = query.trim().toLowerCase();
  const filtered = q
    ? danhSach.filter(hs =>
        hs.ten.toLowerCase().includes(q) ||
        hs.lop.toLowerCase().includes(q) ||
        hs.email.toLowerCase().includes(q)
      )
    : danhSach;
  const tbody = document.querySelector('#table tbody');
  if (!filtered.length) {
    tbody.innerHTML = '<tr><td colspan="4">Không tìm thấy kết quả</td></tr>';
    return;
  }
  tbody.innerHTML = filtered.map(hs => `<tr>
    <td>${highlight(hs.ten, query)}</td>
    <td>${highlight(hs.lop, query)}</td>
    <td>${highlight(hs.email, query)}</td>
  </tr>`).join('');
  document.getElementById('count').textContent = `${filtered.length}/${danhSach.length}`;
}, 200);

document.getElementById('search').addEventListener('input', e => timKiem(e.target.value));"""),

  (20,"Dark Mode Toggle",
   "Cài đặt dark mode với CSS variables và localStorage.",
   "Dark mode là tính năng UX ngày càng quan trọng. "
   "Dùng CSS variables để đổi theme và localStorage để nhớ lựa chọn.",
   ["Toggle dark/light mode bằng nút",
    "CSS variables cho màu sắc theme",
    "Nhớ lựa chọn qua localStorage",
    "Tôn trọng system preference: prefers-color-scheme",
    "Transition mượt khi đổi theme"],
   ["CSS variables: <code>--bg-color: #fff</code>, ghi đè trong [data-theme='dark']",
    "JavaScript: thêm/xóa attribute <code>data-theme='dark'</code> trên html hoặc body",
    "System preference: <code>window.matchMedia('(prefers-color-scheme: dark)')</code>",
    "Lưu localStorage: nhớ khi load lại trang",
    "Transition: <code>transition: background 0.3s, color 0.3s</code>"],
   """:root {
  --bg: #ffffff; --text: #1a202c; --card: #f7fafc;
  --primary: #3182ce; --border: #e2e8f0;
}
[data-theme='dark'] {
  --bg: #1a202c; --text: #f7fafc; --card: #2d3748;
  --primary: #63b3ed; --border: #4a5568;
}
body { background: var(--bg); color: var(--text); transition: background 0.3s, color 0.3s; }

/* JavaScript */
const html = document.documentElement;
const btn  = document.getElementById('theme-toggle');

// Ưu tiên: 1. localStorage, 2. system preference, 3. light
function getInitialTheme() {
  const saved = localStorage.getItem('theme');
  if (saved) return saved;
  const sys = window.matchMedia('(prefers-color-scheme: dark)');
  return sys.matches ? 'dark' : 'light';
}

function applyTheme(theme) {
  html.dataset.theme = theme;
  btn.textContent = theme === 'dark' ? '☀️ Sáng' : '🌙 Tối';
  localStorage.setItem('theme', theme);
}

btn.addEventListener('click', () => {
  applyTheme(html.dataset.theme === 'dark' ? 'light' : 'dark');
});

// Lắng nghe system preference thay đổi
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  if (!localStorage.getItem('theme')) applyTheme(e.matches ? 'dark' : 'light');
});

applyTheme(getInitialTheme());"""),

  (21,"Custom Dropdown Component",
   "Xây dựng custom dropdown select tùy chỉnh giao diện hoàn toàn bằng JS.",
   "Select mặc định của trình duyệt rất khó style. Custom dropdown cho phép "
   "thiết kế tự do, có search, multi-select, grouped options.",
   ["Tạo custom dropdown thay thế select tag",
    "Có ô search để lọc option",
    "Đóng khi click ngoài",
    "Keyboard navigation: mũi tên lên/xuống, Enter để chọn, Escape để đóng"],
   ["Custom dropdown state: isOpen, selectedValue, searchQuery",
    "Click ngoài: document.addEventListener('click') + closest() để phát hiện",
    "Keyboard: ArrowUp/Down để navigate, Enter để chọn",
    "Accessibility: role='listbox', aria-selected, aria-expanded",
    "Portal: append dropdown vào body để tránh bị overflow:hidden cắt"],
   """class CustomSelect {
  constructor(container, options) {
    this.options  = options;
    this.selected = null;
    this.isOpen   = false;
    this.query    = '';
    this.container = container;
    this.render();
    this.bindEvents();
  }

  get filtered() {
    return this.options.filter(o =>
      o.label.toLowerCase().includes(this.query.toLowerCase())
    );
  }

  render() {
    this.container.innerHTML = `
      <div class="cs-trigger" tabindex="0" aria-expanded="${this.isOpen}">
        <span>${this.selected?.label ?? 'Chọn...'}</span>
        <span class="arrow">${this.isOpen ? '▲' : '▼'}</span>
      </div>
      ${this.isOpen ? `
      <div class="cs-dropdown">
        <input class="cs-search" placeholder="Tìm kiếm..." value="${this.query}" />
        <ul class="cs-list">
          ${this.filtered.map(o => `
            <li class="cs-item ${o.value===this.selected?.value?'selected':''}" data-value="${o.value}">
              ${o.label}
            </li>`).join('')}
          ${!this.filtered.length ? '<li class="cs-empty">Không tìm thấy</li>' : ''}
        </ul>
      </div>` : ''}
    `;
  }

  bindEvents() {
    this.container.addEventListener('click', (e) => {
      if (e.target.closest('.cs-trigger')) { this.isOpen = !this.isOpen; this.render(); this.bindEvents(); }
      const item = e.target.closest('.cs-item');
      if (item) { this.selected = this.options.find(o => o.value == item.dataset.value); this.isOpen = false; this.render(); this.bindEvents(); this.container.dispatchEvent(new CustomEvent('change', {detail: this.selected})); }
    });
    const searchEl = this.container.querySelector('.cs-search');
    if (searchEl) { searchEl.focus(); searchEl.addEventListener('input', e => { this.query = e.target.value; this.render(); this.bindEvents(); }); }
    document.addEventListener('click', (e) => { if (!this.container.contains(e.target)) { this.isOpen = false; this.render(); } }, { once: true });
  }
}"""),

  (22,"Canvas API – Vẽ đồ họa",
   "Vẽ hình ảnh và đồ họa bằng HTML5 Canvas API.",
   "Canvas API cho phép vẽ 2D trực tiếp lên trình duyệt bằng JavaScript. "
   "Dùng cho game, chart, editor ảnh, animation.",
   ["Vẽ hình học: rect, circle, line, triangle",
    "Vẽ text với kiểu chữ và màu",
    "Vẽ animation đơn giản: bounce ball",
    "Dùng canvas làm signature pad"],
   ["<code>canvas.getContext('2d')</code>: lấy 2D context",
    "Hình chữ nhật: <code>fillRect(x,y,w,h)</code>",
    "Tròn: <code>arc(cx,cy,r,0,Math.PI*2)</code>",
    "<code>beginPath()</code> trước mỗi hình mới",
    "<code>fillStyle</code> / <code>strokeStyle</code>: màu fill/stroke",
    "<code>requestAnimationFrame(fn)</code>: animation 60fps",
    "<code>clearRect(0,0,w,h)</code>: xóa canvas trước khi vẽ frame mới"],
   """const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = 600; canvas.height = 400;

// Vẽ các hình cơ bản
ctx.fillStyle = '#3182ce';
ctx.fillRect(20, 20, 120, 80); // x, y, width, height

ctx.strokeStyle = '#e53e3e';
ctx.lineWidth = 3;
ctx.strokeRect(160, 20, 120, 80);

// Vòng tròn
ctx.beginPath();
ctx.arc(360, 60, 40, 0, Math.PI * 2);
ctx.fillStyle = '#48bb78';
ctx.fill();

// Text
ctx.fillStyle = '#1a202c';
ctx.font = 'bold 24px Segoe UI';
ctx.textAlign = 'center';
ctx.fillText('Canvas API', canvas.width/2, 160);

// Animation: bounce ball
const ball = { x: 60, y: 60, r: 20, vx: 3, vy: 2, color: '#f6ad55' };
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Di chuyển và nảy
  ball.x += ball.vx; ball.y += ball.vy;
  if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) ball.vx *= -1;
  if (ball.y + ball.r > canvas.height || ball.y - ball.r < 0) ball.vy *= -1;
  // Vẽ bóng
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI*2);
  ctx.fillStyle = ball.color;
  ctx.fill();
  requestAnimationFrame(animate);
}
animate();"""),

  (23,"Advanced Form Validation",
   "Xây dựng hệ thống validation form phức tạp có thể tái sử dụng.",
   "Form validation production-level cần: validate rules có thể cấu hình, "
   "message t rực quan, async validation (check username tồn tại), sanitize input.",
   ["Validator class có thể cấu hình rules",
    "Async validation: check email chưa đăng ký (giả lập API)",
    "Real-time feedback khi gõ",
    "Submit chỉ khi tất cả hợp lệ"],
   ["Tách rules validation khỏi UI",
    "Async validator: debounce + fetch để tránh quá nhiều request",
    "Sanitize: trim, lowercase email, remove script tags",
    "UX tốt: chỉ validate sau blur lần đầu, sau đó validate mỗi keystroke"],
   """class Validator {
  constructor(form) {
    this.form = form;
    this.rules = {};
    this.touched = new Set();
    this.form.addEventListener('submit', e => this.handleSubmit(e));
  }

  field(name, ...rules) {
    this.rules[name] = rules;
    const input = this.form.elements[name];
    input.addEventListener('blur', () => { this.touched.add(name); this.validate(name); });
    input.addEventListener('input', () => { if (this.touched.has(name)) this.validate(name); });
    return this;
  }

  async validate(name) {
    const input = this.form.elements[name];
    const val   = input.value.trim();
    let err = null;
    for (const rule of this.rules[name]) {
      const result = await rule(val);
      if (result !== true) { err = result; break; }
    }
    this.showResult(name, err);
    return !err;
  }

  showResult(name, err) {
    const input = this.form.elements[name];
    const wrap  = input.closest('.field');
    input.classList.toggle('error', !!err);
    input.classList.toggle('valid', !err);
    let msg = wrap.querySelector('.msg');
    if (!msg) { msg = document.createElement('p'); msg.className = 'msg'; wrap.appendChild(msg); }
    msg.textContent = err || '';
  }

  async handleSubmit(e) {
    e.preventDefault();
    Object.keys(this.rules).forEach(n => this.touched.add(n));
    const results = await Promise.all(Object.keys(this.rules).map(n => this.validate(n)));
    if (results.every(Boolean)) this.form.dispatchEvent(new Event('valid-submit'));
  }
}

// Rules tái sử dụng
const required = (v) => v ? true : 'Bắt buộc điền';
const minLen = n => v => v.length >= n || `Tối thiểu ${n} ký tự`;
const email = v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || 'Email không hợp lệ';
const checkEmail = async v => { await new Promise(r => setTimeout(r, 500)); return v.includes('test') ? 'Email đã tồn tại' : true; };

const v = new Validator(document.getElementById('reg'));
v.field('ten', required, minLen(2))
 .field('email', required, email, checkEmail)
 .field('password', required, minLen(8));"""),

  (24,"Web Workers",
   "Chạy tác vụ nặng tính toán trong background thread với Web Workers.",
   "JavaScript là single-threaded – tác vụ nặng làm UI đơ. Web Worker cho phép "
   "chạy code trong thread riêng mà không block giao diện người dùng.",
   ["Tính số Fibonacci lớn trong Worker (không block UI)",
    "Giao tiếp qua postMessage",
    "So sánh: chạy trong main thread vs Worker"],
   ["Worker chạy trong thread riêng, không truy cập DOM",
    "<code>worker.postMessage(data)</code>: gửi dữ liệu sang worker",
    "<code>worker.onmessage = e => { e.data }</code>: nhận từ worker",
    "Trong worker: <code>self.onmessage / self.postMessage</code>",
    "Terminate: <code>worker.terminate()</code>",
    "SharedArrayBuffer + Atomics: dùng bộ nhớ chung giữa threads (nâng cao)"],
   """// worker.js – file riêng
self.onmessage = function(e) {
  const { type, data } = e.data;
  if (type === 'fibonacci') {
    const result = fibonacci(data.n);
    self.postMessage({ type: 'result', result });
  }
  if (type === 'sort') {
    const sorted = data.arr.sort((a.b) => a - b);
    self.postMessage({ type: 'sorted', sorted });
  }
};

function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n-1) + fibonacci(n-2);
}

// main.js
const worker = new Worker('worker.js');

worker.onmessage = (e) => {
  const { type, result } = e.data;
  if (type === 'result') {
    document.getElementById('output').textContent = `Fibonacci: ${result}`;
    document.getElementById('loading').hidden = true;
  }
};

worker.onerror = (err) => {
  console.error('Worker error:', err);
};

document.getElementById('calc').addEventListener('click', () => {
  const n = +document.getElementById('n').value;
  document.getElementById('loading').hidden = false;
  worker.postMessage({ type: 'fibonacci', data: { n } });
});

// Inline worker (không cần file riêng)
const blob = new Blob([`self.onmessage=e=>{self.postMessage(e.data*2)}`], {type:'text/javascript'});
const inlineWorker = new Worker(URL.createObjectURL(blob));"""),

  (25,"Service Worker – Caching cơ bản",
   "Cài đặt Service Worker để cache tài nguyên cho Progressive Web App.",
   "Service Worker là script chạy trong background, độc lập với trang. "
   "Dùng để cache, push notification, background sync – nền tảng của PWA.",
   ["Đăng ký Service Worker",
    "Cache tài nguyên tĩnh khi install",
    "Serve từ cache khi offline",
    "Cache-first strategy"],
   ["SW có lifecycle: install → activate → fetch",
    "Cache API: <code>caches.open(name).then(cache => cache.addAll([...]))</code>",
    "Intercept fetch: <code>self.addEventListener('fetch', e => { })</code>",
    "Cache-first: trả cache ngay, nếu không có thì fetch mạng",
    "Network-first: fetch mạng trước, dùng cache nếu offline",
    "HTTPS bắt buộc cho production SW (localhost OK cho dev)"],
   """// service-worker.js
const CACHE = 'my-app-v1';
const ASSETS = ['/', '/index.html', '/css/style.css', '/js/app.js', '/img/logo.png'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting(); // Activate ngay, không chờ tab cũ đóng
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  clients.claim();
});

// Cache-first strategy
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(response => {
        if (!response.ok) return response;
        const copy = response.clone();
        caches.open(CACHE).then(cache => cache.put(e.request, copy));
        return response;
      });
    })
  );
});

// main.js: Đăng ký SW
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js')
      .then(reg => console.log('SW đã đăng ký:', reg.scope))
      .catch(err => console.error('Lỗi SW:', err));
  });
}"""),

  (26,"Custom Event và Event Emitter",
   "Tạo hệ thống sự kiện tùy chỉnh để giao tiếp giữa các component.",
   "Custom Events và Event Emitter pattern cho phép các phần của ứng dụng "
   "giao tiếp loose-coupled, không cần tham chiếu trực tiếp.",
   ["Tạo và dispatch Custom Event",
    "Tạo EventEmitter class đơn giản",
    "Dùng EventEmitter để kết nối các component"],
   ["<code>new CustomEvent('name', { detail: data })</code>",
    "<code>el.dispatchEvent(event)</code>: kích hoạt event",
    "<code>el.addEventListener('name', e => e.detail)</code>",
    "Event Emitter: pub/sub pattern – subscribe và publish",
    "Giúp decouple: component A không cần biết về B để giao tiếp"],
   """// Custom Event
function addToCart(product) {
  document.dispatchEvent(new CustomEvent('cart:add', {
    detail: { product, quantity: 1 },
    bubbles: true,
  }));
}
document.addEventListener('cart:add', (e) => {
  const { product, quantity } = e.detail;
  updateCartUI(product, quantity);
});

// EventEmitter class (pub/sub pattern)
class EventEmitter {
  constructor() { this._listeners = {}; }
  on(event, fn) {
    if (!this._listeners[event]) this._listeners[event] = [];
    this._listeners[event].push(fn);
    return () => this.off(event, fn); // unsubscribe function
  }
  off(event, fn) {
    this._listeners[event] = (this._listeners[event] || []).filter(f => f !== fn);
  }
  emit(event, data) {
    (this._listeners[event] || []).forEach(fn => fn(data));
  }
  once(event, fn) {
    const wrap = (data) => { fn(data); this.off(event, wrap); };
    this.on(event, wrap);
  }
}

// Sử dụng
const bus = new EventEmitter();

// Component Giỏ hàng lắng nghe
bus.on('add-to-cart', ({product, qty}) => {
  console.log(`Thêm ${product.ten} x${qty}`);
});

// Component Sản phẩm phát sự kiện
bus.emit('add-to-cart', { product: { ten: 'Áo', gia: 150 }, qty: 2 });"""),

  (27,"IndexedDB – Lưu dữ liệu lớn",
   "Lưu trữ dữ liệu có cấu trúc lớn trên trình duyệt bằng IndexedDB.",
   "localStorage chỉ lưu được ~5MB string. IndexedDB là database thực sự "
   "trong trình duyệt: lưu đối tượng, index, query, transaction.",
   ["Tạo/mở database IndexedDB",
    "Thêm, đọc, cập nhật, xóa bản ghi",
    "Query với index"],
   ["<code>indexedDB.open(name, version)</code>: mở/tạo DB",
    "onupgradeneeded: tạo object store và index",
    "Transaction: <code>db.transaction(store, 'readwrite')</code>",
    "Object store: như table trong SQL",
    "Index: truy vấn theo field khác ngoài key",
    "IDB API dùng callback/event – thường wrap bằng Promise"],
   """// Wrapper Promise cho IndexedDB
function openDB(name, version, onUpgrade) {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(name, version);
    req.onupgradeneeded = e => onUpgrade(e.target.result);
    req.onsuccess = e => resolve(e.target.result);
    req.onerror   = e => reject(e.target.error);
  });
}
function idbAction(db, store, mode, action) {
  return new Promise((resolve, reject) => {
    const tx  = db.transaction(store, mode);
    const os  = tx.objectStore(store);
    const req = action(os);
    req.onsuccess = e => resolve(e.target.result);
    req.onerror   = e => reject(e.target.error);
  });
}

async function main() {
  const db = await openDB('my-app', 1, (db) => {
    if (!db.objectStoreNames.contains('products')) {
      const store = db.createObjectStore('products', { keyPath: 'id', autoIncrement: true });
      store.createIndex('name', 'name', { unique: false });
      store.createIndex('price', 'price');
    }
  });

  // Thêm
  await idbAction(db, 'products', 'readwrite', os => os.add({ name:'Áo', price:150 }));

  // Đọc tất cả
  const all = await idbAction(db, 'products', 'readonly', os => os.getAll());
  console.log(all);

  // Xóa
  await idbAction(db, 'products', 'readwrite', os => os.delete(1));
}
main();"""),

  (28,"WebSocket – Real-time Communication",
   "Kết nối WebSocket để giao tiếp hai chiều theo thời gian thực.",
   "WebSocket cung cấp kết nối hai chiều liên tục giữa client và server. "
   "Dùng cho: chat, collaborative editing, live notifications, game.",
   ["Kết nối đến WebSocket server (echo.websocket.org)",
    "Gửi và nhận tin nhắn",
    "Xử lý reconnect khi mất kết nối",
    "Chat UI đơn giản"],
   ["<code>new WebSocket('wss://echo.websocket.org')</code>",
    "Events: onopen, onmessage, onerror, onclose",
    "<code>ws.send(JSON.stringify(data))</code>: gửi message",
    "ws.readyState: 0=CONNECTING, 1=OPEN, 2=CLOSING, 3=CLOSED",
    "Reconnect: setTimeout khi onclose, exponential backoff",
    "Thực tế cần server WebSocket (Node.js ws, Socket.io...)"],
   """class WSClient {
  constructor(url) {
    this.url     = url;
    this.ws      = null;
    this.retries = 0;
    this.listeners = {};
    this.connect();
  }

  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen    = () => { console.log('Đã kết nối'); this.retries = 0; this.emit('open'); };
    this.ws.onmessage = (e) => {
      try { this.emit('message', JSON.parse(e.data)); }
      catch { this.emit('message', e.data); }
    };
    this.ws.onerror   = (e) => { console.error('WS Error:', e); };
    this.ws.onclose   = () => {
      console.log('Ngắt kết nối'); this.emit('close');
      // Tự reconnect với exponential backoff
      const delay = Math.min(1000 * 2**this.retries, 30000);
      this.retries++;
      setTimeout(() => this.connect(), delay);
    };
  }
  send(data) {
    if (this.ws.readyState === WebSocket.OPEN) this.ws.send(JSON.stringify(data));
    else console.warn('WS chưa mở');
  }
  on(event, fn) { this.listeners[event] = fn; }
  emit(event, data) { this.listeners[event]?.(data); }
  close() { this.ws.close(); }
}

// Chat UI
const ws = new WSClient('wss://echo.websocket.org');
ws.on('open', () => { document.getElementById('status').textContent = '🟢 Đã kết nối'; });
ws.on('close', () => { document.getElementById('status').textContent = '🔴 Ngắt kết nối'; });
ws.on('message', (msg) => { appendMessage(msg.user ?? 'Server', msg.text ?? msg, false); });

function guiTinNhan() {
  const input = document.getElementById('msg-input');
  const text  = input.value.trim();
  if (!text) return;
  ws.send({ user: 'Tôi', text, time: Date.now() });
  appendMessage('Tôi', text, true);
  input.value = '';
}"""),

  (29,"TypeScript Basics",
   "Bắt đầu với TypeScript – JavaScript có kiểu dữ liệu mạnh mẽ.",
   "TypeScript là superset của JavaScript thêm static typing. "
   "Giúp bắt lỗi sớm, IDE support tốt hơn, code dễ refactor.",
   ["Khai báo kiểu cho biến và hàm",
    "Interface và Type alias",
    "Generic types cơ bản",
    "Compile TypeScript sang JavaScript"],
   ["TypeScript cần compile: <code>tsc file.ts</code> → <code>file.js</code>",
    "<code>const name: string = 'An'</code>: kiểu tường minh",
    "Type inference: TS tự suy kiểu khi có giá trị ban đầu",
    "Interface: định nghĩa hình dạng object",
    "Union type: <code>string | number</code>",
    "Generic: <code>function f&lt;T&gt;(arg: T): T</code>"],
   """// TypeScript syntax
// Cài đặt: npm install -g typescript
// Compile: tsc app.ts

// Kiểu cơ bản
let ten: string = 'Nguyễn An';
let tuoi: number = 25;
let actife: boolean = true;
let items: string[] = ['a','b','c'];
let tuple: [string, number] = ['An', 25];

// Union và Optional
let id: string | number = 123;
function greet(name: string, prefix?: string): string {
  return `${prefix ?? 'Xin chào'}, ${name}!`;
}

// Interface
interface SanPham {
  id: number;
  ten: string;
  gia: number;
  mau?: string;       // optional
  readonly ma: string; // không thể thay đổi
}

// Type alias
type Status = 'active' | 'inactive' | 'pending';
type ID = string | number;

// Generic
function firstItem<T>(arr: T[]): T | undefined {
  return arr[0];
}
const first = firstItem([1, 2, 3]); // T suy ra là number

// Class với TypeScript
class User {
  constructor(
    public readonly id: number,
    private name: string,
    protected email: string,
  ) {}
  getName(): string { return this.name; }
}

// Utility types
type Partial_SP = Partial<SanPham>;  // tất cả optional
type Pick_SP    = Pick<SanPham, 'id' | 'ten'>;
type Readonly_SP = Readonly<SanPham>;"""),

  (30,"🏆 Dự án: Weather App",
   "Xây dựng ứng dụng thời tiết lấy dữ liệu từ API thực tế.",
   "Dự án cuối tổng hợp tất cả kiến thức Module 5: Fetch API, async/await, "
   "DOM manipulation, localStorage, error handling. Lấy dữ liệu thời tiết thực.",
   ["Ô nhập tên thành phố, nút tìm kiếm",
    "Fetch dữ liệu từ OpenWeatherMap API (cần API key miễn phí)",
    "Hiển thị: nhiệt độ, mô tả, độ ẩm, tốc độ gió, icon thời tiết",
    "Lưu lịch sử 5 thành phố gần nhất vào localStorage",
    "Xử lý lỗi: tên thành phố sai, offline, API key hết hạn",
    "Loading state và skeleton screen",
    "Đổi đơn vị: Celsius ↔ Fahrenheit"],
   ["OpenWeatherMap API: đăng ký miễn phí tại openweathermap.org",
    "URL: <code>https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=vi</code>",
    "Icon: <code>https://openweathermap.org/img/wn/{icon}@2x.png</code>",
    "Cache kết quả trong sessionStorage để tránh gọi API nhiều lần",
    "Geolocation API để lấy thời tiết vị trí hiện tại"],
   """const API_KEY = 'YOUR_API_KEY'; // Đăng ký tại openweathermap.org
const BASE = 'https://api.openweathermap.org/data/2.5';

// Cache ngắn hạn (10 phút)
const cache = new Map();
const CACHE_TTL = 10 * 60 * 1000;

async function layThoiTiet(city) {
  const cacheKey = city.toLowerCase();
  const cached = cache.get(cacheKey);
  if (cached && Date.now() - cached.time < CACHE_TTL) return cached.data;

  const url = `${BASE}/weather?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric&lang=vi`;
  const res = await fetch(url);
  if (!res.ok) {
    if (res.status === 404) throw new Error(`Không tìm thấy thành phố "${city}"`);
    throw new Error(`Lỗi API: ${res.status}`);
  }
  const data = await res.json();
  cache.set(cacheKey, { data, time: Date.now() });
  return data;
}

function hienThiThoiTiet(d) {
  let nhietDo = d.main.temp;
  document.getElementById('city').textContent = `${d.name}, ${d.sys.country}`;
  document.getElementById('temp').textContent = `${Math.round(nhietDo)}°C`;
  document.getElementById('desc').textContent = d.weather[0].description;
  document.getElementById('humidity').textContent = `${d.main.humidity}%`;
  document.getElementById('wind').textContent = `${d.wind.speed} m/s`;
  document.getElementById('icon').src = `https://openweathermap.org/img/wn/${d.weather[0].icon}@2x.png`;
}

async function timKiem(city) {
  try {
    hienLoading(true);
    const data = await layThoiTiet(city);
    hienThiThoiTiet(data);
    luuLichSu(city);
  } catch (err) {
    hienLoi(err.message);
  } finally {
    hienLoading(false);
  }
}

// Lịch sử
function luuLichSu(city) {
  let lich = JSON.parse(localStorage.getItem('weather-history') || '[]');
  lich = [city, ...lich.filter(c => c.toLowerCase() !== city.toLowerCase())].slice(0, 5);
  localStorage.setItem('weather-history', JSON.stringify(lich));
  renderLichSu(lich);
}

// Geolocation
navigator.geolocation?.getCurrentPosition(async pos => {
  const { latitude: lat, longitude: lon } = pos.coords;
  const res = await fetch(`${BASE}/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=vi`);
  const data = await res.json();
  hienThiThoiTiet(data);
});"""),
]

count = 0
for num, title, short, desc, reqs, knows, code in exercises:
    folder = BASE / f"bai-{num:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    content = tpl(num, title, short, desc, reqs, knows, code)
    (folder / "index.html").write_text(content, encoding="utf-8")
    count += 1
    print(f"  ✓ bai-{num:02d}: {title}")

print(f"\nModule 5 – JavaScript Nâng Cao: Đã tạo {count} file")
