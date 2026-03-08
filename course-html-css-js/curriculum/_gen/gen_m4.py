#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo Module 4 – JavaScript Cơ Bản – 30 bài tập đầy đủ tiếng Việt"""
import pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-04-javascript-co-ban")

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
  <div class="page-header module-4">
    <div class="breadcrumb">
      <a href="../../index.html">Trang Chủ</a> &rsaquo;
      <a href="../index.html">Module 4</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 4 – JavaScript Cơ Bản</p>
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
  (1,"Nhúng JavaScript vào HTML",
   "Học 3 cách nhúng JavaScript vào trang HTML: inline, internal và external.",
   "JavaScript có thể nhúng vào HTML theo 3 cách. Hiểu ưu nhược điểm của mỗi cách "
   "giúp bạn tổ chức code đúng từ đầu.",
   ["Thử cách 1: inline JS dùng onclick='alert()'",
    "Thử cách 2: thẻ script bên trong HTML (internal)",
    "Thử cách 3: tạo file script.js riêng, link vào HTML (external – khuyến nghị)",
    "Đặt thẻ script ở cuối body để trang tải ảnh/CSS trước"],
   ["<code>onclick='...'</code>: inline – khó quản lý, không nên dùng",
    "<code>&lt;script&gt;...&lt;/script&gt;</code>: internal – dùng được cho trang nhỏ",
    "<code>&lt;script src='app.js'&gt;</code>: external – tốt nhất, tách biệt logic và HTML",
    "Đặt script trước </body> để không block tải trang",
    "Hoặc dùng <code>defer</code>: <code>&lt;script src='app.js' defer&gt;</code>"],
   """<!-- Cách 1: Inline (không khuyến nghị) -->
<button onclick="alert('Xin chào!')">Nhấn tôi</button>

<!-- Cách 2: Internal script -->
<script>
  function greet() {
    alert('Xin chào từ internal script!');
  }
</script>

<!-- Cách 3: External (khuyến nghị nhất) -->
<!-- Tạo file script.js -->
<!-- Trong HTML: -->
<script src="script.js" defer></script>

/* script.js */
console.log('Trang đã tải xong!');
document.getElementById('btn').addEventListener('click', function() {
  alert('Xin chào từ external script!');
});

// defer: chờ HTML parse xong mới chạy script
// async: chạy song song, không đảm bảo thứ tự"""),

  (2,"Biến và kiểu dữ liệu",
   "Khai báo biến với var, let, const và làm việc với các kiểu dữ liệu cơ bản.",
   "JavaScript có 7 kiểu dữ liệu nguyên thủy. Biến là 'hộp chứa' dữ liệu. "
   "Chọn let/const thay vì var trong code hiện đại.",
   ["Khai báo biến với let và const, thử thay đổi giá trị",
    "In ra console: string, number, boolean, null, undefined",
    "Dùng typeof để kiểm tra kiểu dữ liệu",
    "Thực hành string template literal (backtick)"],
   ["<code>const</code>: hằng số – không thể gán lại (dùng mặc định)",
    "<code>let</code>: biến có thể thay đổi trong block",
    "<code>var</code>: cũ – có function scope, tránh dùng",
    "7 kiểu nguyên thủy: string, number, boolean, null, undefined, BigInt, Symbol",
    "<code>typeof value</code>: trả về kiểu dữ liệu dạng string",
    "Template literal: <code>`Xin chào ${name}`</code>"],
   """// Khai báo biến
const PI = 3.14159;          // hằng số – không đổi
let userName = 'Nguyễn An';  // biến string
let age = 25;                // number
let isStudent = true;        // boolean
let address = null;          // null: có chủ đích không có giá trị
let score;                   // undefined: chưa gán giá trị

// Kiểm tra kiểu
console.log(typeof userName);  // "string"
console.log(typeof age);       // "number"
console.log(typeof isStudent); // "boolean"
console.log(typeof null);      // "object" (quirk của JS!)
console.log(typeof score);     // "undefined"

// Template literal
const greeting = `Xin chào, ${userName}! Bạn ${age} tuổi.`;
console.log(greeting);

// Số đặc biệt
console.log(1 / 0);   // Infinity
console.log(0 / 0);   // NaN (Not a Number)
console.log(isNaN('abc')); // true"""),

  (3,"Toán tử số học và chuỗi",
   "Thực hành các toán tử số học và ghép chuỗi trong JavaScript.",
   "JavaScript hỗ trợ đầy đủ toán tử số học. Toán tử + đặc biệt: dùng cả cho "
   "ghép chuỗi và số học – cần chú ý type coercion.",
   ["Tính diện tích và chu vi hình chữ nhật",
    "Tính điểm trung bình 3 môn học",
    "Dùng toán tử % (chia dư) để kiểm tra số chẵn/lẻ",
    "Thực hành toán tử tăng/giảm ++, --",
    "Chuyển đổi kiểu: parseInt, parseFloat, Number()"],
   ["<code>+ - * / %</code>: cộng trừ nhân chia dư",
    "<code>**</code>: lũy thừa (ES7): <code>2**10</code> = 1024",
    "<code>++i</code>: tăng trước, <code>i++</code>: tăng sau",
    "<code>'5' + 3</code> = '53' (ghép chuỗi!), <code>'5' - 3</code> = 2 (ép số)",
    "<code>parseInt('42px')</code> = 42, <code>Number('42px')</code> = NaN",
    "Math.round/floor/ceil/abs/max/min/random – xem bài tiếp theo"],
   """// Toán tử số học
const a = 10, b = 3;
console.log(a + b);   // 13
console.log(a - b);   // 7
console.log(a * b);   // 30
console.log(a / b);   // 3.333...
console.log(a % b);   // 1 (chia dư)
console.log(a ** b);  // 1000 (10^3)

// Type coercion
console.log('5' + 3);   // '53' (string!)
console.log('5' - 3);   // 2 (number)
console.log(+'5');       // 5 (chuyển sang number)

// Tính diện tích
const chieu_rong = 5.5, chieu_cao = 3.2;
const dien_tich = chieu_rong * chieu_cao;
const chu_vi = 2 * (chieu_rong + chieu_cao);
console.log(`Diện tích: ${dien_tich} m²`);
console.log(`Chu vi: ${chu_vi} m`);

// Kiểm tra chẵn/lẻ
const so = 7;
console.log(so % 2 === 0 ? 'Chẵn' : 'Lẻ'); // Lẻ

// Chuyển đổi kiểu
console.log(parseInt('42px'));  // 42
console.log(parseFloat('3.14em')); // 3.14
console.log(Number('100'));     // 100
console.log(Number('abc'));     // NaN"""),

  (4,"Toán tử so sánh và logic",
   "Sử dụng toán tử so sánh và logic để kiểm tra điều kiện.",
   "Toán tử so sánh trả về true/false. Chú ý sự khác biệt giữa == (loose) "
   "và === (strict). Luôn dùng === trong code thực tế.",
   ["So sánh 2 số và in kết quả ra console",
    "Dùng === và == để so sánh '5' và 5 – quan sát sự khác biệt",
    "Kết hợp && và || để tạo điều kiện phức tạp",
    "Toán tử ! (phủ định) và !! (ép sang boolean)"],
   ["<code>==</code>: so sánh lỏng (có type coercion): <code>'5' == 5</code> → true",
    "<code>===</code>: so sánh nghiêm (cả giá trị lẫn kiểu): <code>'5' === 5</code> → false",
    "<code>&amp;&amp;</code>: AND – cả hai cùng true mới true",
    "<code>||</code>: OR – một trong hai true là true",
    "<code>!</code>: NOT – đảo ngược boolean",
    "Falsy values: false, 0, '', null, undefined, NaN"],
   """// Toán tử so sánh
console.log(5 > 3);    // true
console.log(5 < 3);    // false
console.log(5 >= 5);   // true
console.log(5 !== 3);  // true

// == vs ===
console.log('5' == 5);  // true (loose – NGUY HIỂM!)
console.log('5' === 5); // false (strict – AN TOÀN)
console.log(null == undefined);  // true
console.log(null === undefined); // false

// Toán tử logic
const tuoi = 20;
const coThe = tuoi >= 18 && tuoi <= 60; // &&: AND
console.log(coThe); // true

const nghi = tuoi < 18 || tuoi > 60;    // ||: OR
console.log(nghi);  // false

const chua_dang_ky = !true;             // !: NOT
console.log(chua_dang_ky); // false

// Short-circuit evaluation
const ten = null;
const hienThi = ten || 'Khách';  // Dùng || để fallback
console.log(hienThi); // 'Khách'

const user = { name: 'An' };
console.log(user?.name ?? 'Ẩn danh'); // Optional chaining"""),

  (5,"Câu lệnh if-else",
   "Dùng if-else để rẽ nhánh thực thi code theo điều kiện.",
   "if-else là cấu trúc điều khiển cơ bản nhất trong lập trình. "
   "JavaScript cũng có else if để kiểm tra nhiều điều kiện.",
   ["Viết chương trình kiểm tra điểm: A/B/C/D/F",
    "Kiểm tra số dương/âm/bằng 0",
    "Kiểm tra năm nhuận: chia hết 400 OR (chia hết 4 AND không chia hết 100)"],
   ["<code>if (điều_kiện) { } else if { } else { }</code>",
    "Điều kiện phải là biểu thức truthy/falsy",
    "Có thể lồng if bên trong if (nhưng tránh lồng quá sâu)",
    "Early return: kiểm tra điều kiện sai trước, return sớm → code sạch hơn",
    "Truthy: mọi giá trị trừ falsy values"],
   """// Xếp loại học lực
function xepLoai(diem) {
  if (diem >= 9) {
    return 'Xuất sắc';
  } else if (diem >= 8) {
    return 'Giỏi';
  } else if (diem >= 6.5) {
    return 'Khá';
  } else if (diem >= 5) {
    return 'Trung bình';
  } else {
    return 'Yếu';
  }
}
console.log(xepLoai(8.5)); // Giỏi

// Kiểm tra năm nhuận
function laNamNhuan(nam) {
  return (nam % 400 === 0) || (nam % 4 === 0 && nam % 100 !== 0);
}
console.log(laNamNhuan(2024)); // true
console.log(laNamNhuan(1900)); // false

// Early return pattern (code sạch)
function kiemTra(tuoi) {
  if (tuoi < 0) return 'Tuổi không hợp lệ';
  if (tuoi < 18) return 'Chưa đủ tuổi';
  return 'Đủ điều kiện';
}"""),

  (6,"Switch-case",
   "Dùng switch-case để xử lý nhiều trường hợp giá trị xác định.",
   "switch-case phù hợp khi kiểm tra một biến với nhiều giá trị cụ thể. "
   "Thường dùng cho menu, ngày trong tuần, mã lỗi...",
   ["Chương trình in tên ngày trong tuần (1-7)",
    "Menu máy tính: +, -, *, / dùng switch",
    "Phân loại mùa theo tháng"],
   ["<code>switch (biến) { case giá_trị: ... break; default: ... }</code>",
    "<code>break</code>: PHẢI có để thoát switch, không thì 'fall through'",
    "Fall through: nhiều case dùng chung code (kỹ thuật có chủ ý)",
    "<code>default</code>: chạy khi không có case nào khớp (như else)",
    "switch dùng === để so sánh"],
   """// Tên ngày theo số
function tenNgay(so) {
  switch (so) {
    case 1: return 'Thứ Hai';
    case 2: return 'Thứ Ba';
    case 3: return 'Thứ Tư';
    case 4: return 'Thứ Năm';
    case 5: return 'Thứ Sáu';
    case 6: return 'Thứ Bảy';
    case 7: return 'Chủ Nhật';
    default: return 'Không hợp lệ';
  }
}

// Fall through: nhiều case dùng chung code
function loaiNgay(so) {
  switch (so) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
      return 'Ngày làm việc';
    case 6:
    case 7:
      return 'Cuối tuần';
    default:
      return 'Không hợp lệ';
  }
}

// Máy tính đơn giản
function tinh(a, phep, b) {
  switch (phep) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/': return b !== 0 ? a / b : 'Lỗi: Chia cho 0';
    default:  return 'Phép tính không hợp lệ';
  }
}
console.log(tinh(10, '+', 5)); // 15"""),

  (7,"Toán tử ba ngôi (Ternary)",
   "Rút gọn if-else đơn giản bằng toán tử ba ngôi.",
   "Toán tử ba ngôi là cách viết if-else ngắn gọn trên 1 dòng. "
   "Phù hợp cho các điều kiện đơn giản trong biến hoặc JSX.",
   ["Rút gọn xếp loại đạt/không đạt bằng ternary",
    "Dùng ternary trong template literal",
    "Ternary lồng nhau (giới hạn 2 cấp)"],
   ["Cú pháp: <code>điều_kiện ? giá_trị_true : giá_trị_false</code>",
    "Dùng khi biểu thức ngắn, điều kiện rõ ràng",
    "Tránh lồng ternary quá nhiều – khó đọc",
    "Hay dùng trong: gán biến, template string, JSX (React)",
    "Khác với switch và if-else: ternary là BIỂU THỨC, trả về giá trị"],
   """// if-else thông thường
let ket;
if (diem >= 5) { ket = 'Đạt'; }
else           { ket = 'Rớt'; }

// Rút gọn bằng ternary
const ketQua = diem >= 5 ? 'Đạt' : 'Rớt';

// Trong template literal
console.log(`Điểm: ${diem} – ${diem >= 5 ? 'Đạt ✅' : 'Rớt ❌'}`);

// Ternary lồng (tối đa 2 cấp)
const xep = diem >= 8 ? 'Giỏi' : diem >= 6.5 ? 'Khá' : 'Trung bình';

// Nullish coalescing (??) – tương tự ternary cho null/undefined
const ten = null;
const hienThi = ten ?? 'Ẩn danh'; // 'Ẩn danh' (vì null)
// Khác ||: ?? chỉ fallback khi null/undefined, không fallback khi 0 hay ''

// Optional chaining (?.) kết hợp với ??
const user = null;
const name = user?.profile?.name ?? 'Chưa có tên';"""),

  (8,"Vòng lặp for",
   "Dùng vòng lặp for để lặp qua danh sách và thực hiện tác vụ nhiều lần.",
   "Vòng lặp cho phép thực thi code nhiều lần mà không cần viết lặp. "
   "for là vòng lặp phổ biến nhất khi biết trước số lần lặp.",
   ["In bảng cửu chương từ 1 đến 9",
    "Tính tổng từ 1 đến 100",
    "Tìm số nguyên tố từ 2 đến 50",
    "In tam giác sao bằng vòng lặp lồng nhau"],
   ["<code>for (let i=0; i&lt;10; i++) { }</code>: i từ 0 đến 9",
    "Biến đếm thường đặt tên i, j, k (quy ước)",
    "Vòng lặp lồng: 2 vòng for, tổng độ phức tạp O(n²)",
    "<code>break</code>: thoát vòng lặp ngay lập tức",
    "<code>continue</code>: bỏ qua lần lặp hiện tại, tiếp tục lần sau",
    "for-of: lặp qua iterable (array, string) – xem bài mảng"],
   """// Bảng cửu chương 3
for (let i = 1; i <= 10; i++) {
  console.log(`3 x ${i} = ${3 * i}`);
}

// Tổng 1 đến n
function tongDen(n) {
  let tong = 0;
  for (let i = 1; i <= n; i++) {
    tong += i;
  }
  return tong;
}
console.log(tongDen(100)); // 5050

// Số nguyên tố
function laNguyenTo(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

// Lọc số nguyên tố từ 2 đến 50
const ntp = [];
for (let i = 2; i <= 50; i++) {
  if (laNguyenTo(i)) ntp.push(i);
}
console.log('Số nguyên tố:', ntp.join(', '));

// break và continue
for (let i = 0; i < 10; i++) {
  if (i === 3) continue; // bỏ qua 3
  if (i === 7) break;    // dừng tại 7
  console.log(i); // 0, 1, 2, 4, 5, 6
}"""),

  (9,"Vòng lặp while và do-while",
   "Dùng while và do-while khi không biết trước số lần lặp.",
   "while và do-while dùng khi điều kiện dừng phụ thuộc runtime. "
   "Cẩn thận vòng lặp vô hạn: luôn đảm bảo điều kiện kết thúc.",
   ["Đoán số may mắn: lặp đến khi đoán đúng",
    "Đọc dữ liệu đến khi nhập 'quit'",
    "So sánh while và do-while: do-while luôn chạy ít nhất 1 lần"],
   ["<code>while (điều_kiện) { }</code>: kiểm tra TRƯỚC khi chạy",
    "<code>do { } while (điều_kiện)</code>: chạy TRƯỚC, kiểm tra SAU",
    "do-while đảm bảo body chạy ít nhất 1 lần",
    "PHẢI có lệnh cập nhật để điều kiện cuối cùng false – tránh vòng lặp vô hạn",
    "for phù hợp khi biết số lần, while phù hợp khi không biết"],
   """// while: đếm ngược
let dem = 5;
while (dem > 0) {
  console.log(`Đếm: ${dem}`);
  dem--;        // QUAN TRỌNG: cập nhật để thoát vòng lặp
}
console.log('Hết giờ!');

// do-while: luôn chạy ít nhất 1 lần
let nhap;
do {
  nhap = prompt('Nhập số từ 1-10 (hoặc nhập số đúng để thử):');
  nhap = parseInt(nhap);
} while (nhap < 1 || nhap > 10 || isNaN(nhap));
console.log('Bạn nhập:', nhap);

// Đoán số may mắn (giả lập)
const soMayMan = 7;
let guess = 0;
let luot = 0;
while (guess !== soMayMan) {
  guess = Math.floor(Math.random() * 10) + 1;
  luot++;
  console.log(`Lượt ${luot}: đoán ${guess}`);
}
console.log(`Đúng rồi! Cần ${luot} lượt`);"""),

  (10,"Hàm (Function) cơ bản",
   "Khai báo và gọi hàm với tham số và giá trị trả về.",
   "Hàm giúp đóng gói code để tái sử dụng. Là khối xây dựng cơ bản "
   "của mọi chương trình JavaScript. DRY: Don't Repeat Yourself.",
   ["Viết hàm tính diện tích tam giác với 2 tham số",
    "Hàm có giá trị mặc định (default parameter)",
    "Hàm trả về nhiều giá trị qua object",
    "Gọi hàm trước khi khai báo (hoisting)"],
   ["<code>function tenHam(tham_so) { return ket_qua; }</code>",
    "Hàm không có return trả về undefined",
    "Tham số mặc định: <code>function greet(name = 'Bạn') { }</code>",
    "Function declaration: hoisted (có thể gọi trước khai báo)",
    "Function expression và arrow function: KHÔNG hoisted",
    "Số tham số không bắt buộc khớp – thiếu → undefined, dư → bị bỏ qua"],
   """// Khai báo hàm (Function Declaration)
function tinhDienTich(day, caoDuong) {
  return (day * caoDuong) / 2;
}
console.log(tinhDienTich(6, 4)); // 12

// Tham số mặc định
function chao(ten = 'Bạn', loi = 'Xin chào') {
  return `${loi}, ${ten}!`;
}
console.log(chao());          // Xin chào, Bạn!
console.log(chao('Minh'));    // Xin chào, Minh!
console.log(chao('An', 'Hi')); // Hi, An!

// Trả về nhiều giá trị (qua object)
function thongKe(arr) {
  const tong = arr.reduce((a, b) => a + b, 0);
  return {
    tong,
    trungBinh: tong / arr.length,
    lon_nhat: Math.max(...arr),
    nho_nhat: Math.min(...arr),
  };
}
const kq = thongKe([5, 8, 6, 9, 7]);
console.log(kq); // { tong: 35, trungBinh: 7, ... }

// Hoisting: gọi trước khai báo OK với function declaration
console.log(tong(3, 4)); // 7
function tong(a, b) { return a + b; }"""),

  (11,"Arrow Function",
   "Viết hàm ngắn gọn với cú pháp arrow function (ES6).",
   "Arrow function là cú pháp viết hàm ngắn hơn trong ES6. "
   "Ngoài cú pháp ngắn, arrow function còn có hành vi 'this' khác với function thông thường.",
   ["Viết lại 3 hàm thông thường thành arrow function",
    "Arrow function một dòng: bỏ {} và return",
    "Arrow function với array methods: map, filter, reduce"],
   ["<code>const ham = (a, b) => a + b;</code>: 1 dòng, không cần return",
    "<code>const ham = a => a * 2;</code>: 1 tham số không cần ()",
    "<code>const ham = () => ({ key: value });</code>: trả về object cần bọc ()",
    "Arrow function KHÔNG có <code>this</code> riêng – dùng this của scope cha",
    "Arrow function KHÔNG thể dùng làm constructor (new)",
    "Phù hợp cho callback, array methods"],
   """// Function thường
function nhan(a, b) { return a * b; }

// Arrow function tương đương
const nhan2 = (a, b) => a * b;

// 1 tham số không cần ()
const binh_phuong = x => x ** 2;
console.log(binh_phuong(5)); // 25

// Không tham số cần ()
const chaoHoi = () => 'Xin chào!';

// Nhiều dòng dùng {}
const tinhVAT = (gia, phanTram = 10) => {
  const vat = gia * phanTram / 100;
  return gia + vat;
};

// Trả về object: bọc trong ()
const taoUser = (ten, tuoi) => ({ ten, tuoi, active: true });

// Cực kỳ hữu dụng với array methods
const so = [1, 2, 3, 4, 5];
const chan = so.filter(n => n % 2 === 0);      // [2, 4]
const binh = so.map(n => n ** 2);               // [1, 4, 9, 16, 25]
const tong = so.reduce((acc, n) => acc + n, 0); // 15
console.log(chan, binh, tong);"""),

  (12,"Mảng (Array) cơ bản",
   "Tạo và thao tác với mảng: thêm, xóa, truy cập và duyệt phần tử.",
   "Mảng là cấu trúc dữ liệu quan trọng nhất trong JS. Lưu trữ "
   "danh sách có thứ tự, có thể chứa bất kỳ kiểu dữ liệu nào.",
   ["Tạo mảng tên học sinh, in ra từng tên",
    "Thêm phần tử cuối (push), đầu (unshift)",
    "Xóa phần tử cuối (pop), đầu (shift)",
    "Truy cập phần tử: index, at(-1) cho phần tử cuối"],
   ["<code>const arr = [1, 2, 3];</code>: mảng literal",
    "Index bắt đầu từ 0, phần tử cuối: <code>arr[arr.length - 1]</code>",
    "<code>arr.push(x)</code>: thêm cuối, <code>arr.pop()</code>: xóa cuối",
    "<code>arr.unshift(x)</code>: thêm đầu, <code>arr.shift()</code>: xóa đầu",
    "<code>arr.at(-1)</code>: phần tử cuối (ES2022)",
    "<code>arr.includes(x)</code>: kiểm tra có phần tử x không",
    "<code>arr.indexOf(x)</code>: vị trí của x (-1 nếu không có)"],
   """// Tạo mảng
const hocSinh = ['An', 'Bình', 'Chi', 'Dũng'];
console.log(hocSinh.length); // 4
console.log(hocSinh[0]);     // 'An'
console.log(hocSinh.at(-1)); // 'Dũng' (phần tử cuối)

// Thêm/xóa
hocSinh.push('Em');      // ['An', ...,'Em']
hocSinh.unshift('Anh');  // ['Anh', 'An', ...]
const cuoi = hocSinh.pop();    // xóa 'Em', trả về 'Em'
const dau = hocSinh.shift();   // xóa 'Anh', trả về 'Anh'

// Duyệt mảng
for (const ten of hocSinh) {
  console.log(ten);
}

// Kiểm tra
console.log(hocSinh.includes('An'));    // true
console.log(hocSinh.indexOf('Chi'));    // 2 (index)
console.log(hocSinh.indexOf('Xyz'));    // -1 (không có)

// Trải mảng (spread)
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const ketHop = [...arr1, ...arr2]; // [1,2,3,4,5,6]

// Destructuring
const [dau2, thu2, ...phanCon] = hocSinh;
console.log(dau2, thu2, phanCon);"""),

  (13,"Array Methods: slice, splice, find",
   "Thao tác nâng cao với mảng: cắt, chèn/xóa, tìm kiếm phần tử.",
   "slice và splice giúp thao tác với phần của mảng. "
   "find và findIndex tìm phần tử theo điều kiện.",
   ["Cắt mảng sản phẩm lấy trang 2 (phần tử 3-6) bằng slice",
    "Xóa phần tử ở vị trí bất kỳ bằng splice",
    "Tìm sản phẩm có giá dưới 100 bằng find",
    "Tìm index của sản phẩm theo tên bằng findIndex"],
   ["<code>slice(start, end)</code>: cắt KHÔNG thay đổi mảng gốc, end không tính",
    "<code>splice(start, deleteCount, ...items)</code>: sửa mảng gốc, thêm/xóa",
    "<code>find(fn)</code>: trả về phần tử đầu tiên thỏa điều kiện (undefined nếu không)",
    "<code>findIndex(fn)</code>: trả về index (-1 nếu không tìm thấy)",
    "<code>some(fn)</code>: true nếu ít nhất 1 phần tử thỏa",
    "<code>every(fn)</code>: true nếu TẤT CẢ phần tử thỏa"],
   """const sanPham = [
  { id:1, ten:'Áo', gia:150 },
  { id:2, ten:'Quần', gia:80 },
  { id:3, ten:'Giày', gia:200 },
  { id:4, ten:'Mũ', gia:50 },
  { id:5, ten:'Túi', gia:120 },
];

// slice – cắt ra mảng mới (không đổi gốc)
const trang2 = sanPham.slice(2, 4); // index 2,3

// splice – sửa mảng gốc
const copy = [...sanPham];
copy.splice(1, 1); // xóa 1 phần tử tại index 1
copy.splice(1, 0, { id:6, ten:'Belt', gia:60 }); // chèn

// find – tìm phần tử đầu tiên
const reHon100 = sanPham.find(sp => sp.gia < 100);
console.log(reHon100); // { id:2, ten:'Quần', gia:80 }

// findIndex – tìm vị trí
const idxGiay = sanPham.findIndex(sp => sp.ten === 'Giày');
console.log(idxGiay); // 2

// some / every
const coSanPhamDat = sanPham.some(sp => sp.gia > 100);  // true
const tatCaDat    = sanPham.every(sp => sp.gia > 100); // false
console.log(coSanPhamDat, tatCaDat);"""),

  (14,"Array Methods: map, filter, reduce",
   "Xử lý mảng hàm bậc cao: biến đổi, lọc và tổng hợp dữ liệu.",
   "map, filter, reduce là bộ ba quyền năng của functional programming trong JS. "
   "Kết hợp chúng để xử lý dữ liệu mảng theo chuỗi.",
   ["Dùng map: chuyển mảng giá sang mảng giá sau VAT (10%)",
    "Dùng filter: lọc sản phẩm còn hàng",
    "Dùng reduce: tính tổng giá trị giỏ hàng",
    "Chuỗi method: filter → map → reduce"],
   ["<code>map(fn)</code>: biến đổi từng phần tử, trả về mảng MỚI cùng độ dài",
    "<code>filter(fn)</code>: lọc, trả về mảng MỚI chỉ gồm phần tử thỏa điều kiện",
    "<code>reduce(fn, initial)</code>: gộp toàn mảng về 1 giá trị",
    "Cả 3 đều KHÔNG thay đổi mảng gốc (immutable)",
    "Chaining: <code>arr.filter(...).map(...).reduce(...)</code>",
    "Callback nhận 3 tham số: (phần_tử, index, mảng_gốc)"],
   """const gio_hang = [
  { ten:'Áo T-shirt', gia:150, sl:2, con_hang:true },
  { ten:'Quần Jeans', gia:320, sl:1, con_hang:false },
  { ten:'Giày Nike', gia:850, sl:1, con_hang:true },
  { ten:'Mũ Cap', gia:95,  sl:3, con_hang:true },
];

// map: thêm trường thanh_tien
const voi_tien = gio_hang.map(sp => ({
  ...sp,
  thanh_tien: sp.gia * sp.sl
}));

// filter: chỉ lấy sản phẩm còn hàng
const con_hang = gio_hang.filter(sp => sp.con_hang);
console.log('Còn hàng:', con_hang.length); // 3

// reduce: tổng tiền
const tong_tien = gio_hang
  .filter(sp => sp.con_hang)
  .reduce((total, sp) => total + sp.gia * sp.sl, 0);

console.log(`Tổng tiền: ${tong_tien.toLocaleString('vi-VN')}đ`);
// 150*2 + 850*1 + 95*3 = 300 + 850 + 285 = 1435

// flat/flatMap
const nested = [[1,2],[3,4],[5,6]];
console.log(nested.flat()); // [1,2,3,4,5,6]"""),

  (15,"String Methods",
   "Thao tác chuỗi với các phương thức phổ biến của String.",
   "JavaScript có nhiều phương thức string hữu ích để xử lý, tìm kiếm, "
   "thay thế và định dạng văn bản.",
   ["Tạo hàm kiểm tra email hợp lệ (đơn giản) dùng includes, endsWith",
    "Chuẩn hóa tên: trim, capitalize từng từ",
    "Tách chuỗi CSV thành mảng dùng split"],
   ["<code>str.toUpperCase()</code> / <code>toLowerCase()</code>",
    "<code>str.trim()</code>: xóa khoảng trắng 2 đầu",
    "<code>str.includes(sub)</code>: kiểm tra có chuỗi con không",
    "<code>str.startsWith(s)</code> / <code>endsWith(s)</code>",
    "<code>str.replace(old, new)</code>: thay thế lần đầu tiên",
    "<code>str.replaceAll(old, new)</code>: thay thế tất cả",
    "<code>str.split(sep)</code>: tách chuỗi thành mảng",
    "<code>arr.join(sep)</code>: gộp mảng thành chuỗi",
    "<code>str.slice(start, end)</code>: cắt chuỗi con"],
   """// Xử lý tên
const tenDirty = '  nguyễn văn   an  ';
const tenSach = tenDirty.trim()
  .split(' ')
  .filter(w => w.length > 0)
  .map(w => w[0].toUpperCase() + w.slice(1).toLowerCase())
  .join(' ');
console.log(tenSach); // 'Nguyễn Văn An'

// Kiểm tra email đơn giản
function kiemTraEmail(email) {
  const e = email.trim().toLowerCase();
  return e.includes('@') && e.includes('.') && !e.startsWith('@') && !e.endsWith('.');
}

// Xử lý CSV
const csv = 'An,20,HCM;Bình,22,HN;Chi,19,ĐN';
const nguoi = csv.split(';').map(row => {
  const [ten, tuoi, thanh_pho] = row.split(',');
  return { ten, tuoi: +tuoi, thanh_pho };
});
console.log(nguoi);

// Pad và repeat
const so = 42;
console.log(String(so).padStart(5, '0')); // '00042'
console.log('=-'.repeat(10) + '=');       // trang trí

// replace với regex
const text = 'Xin chào chào chào!';
console.log(text.replaceAll('chào', 'hello')); // thay tất cả"""),

  (16,"Math Object",
   "Dùng Math object cho các tính toán toán học: làm tròn, random, lũy thừa.",
   "Math là object tích hợp của JavaScript với các phương thức và hằng số toán học. "
   "Math.random() đặc biệt hữu dụng để tạo dữ liệu ngẫu nhiên.",
   ["Tạo hàm lấy số ngẫu nhiên trong khoảng [min, max]",
    "Tạo màu hex ngẫu nhiên",
    "Làm tròn giá tiền đến hàng nghìn"],
   ["<code>Math.round(x)</code>: làm tròn thông thường",
    "<code>Math.floor(x)</code>: làm tròn xuống",
    "<code>Math.ceil(x)</code>: làm tròn lên",
    "<code>Math.random()</code>: số thực ngẫu nhiên [0, 1)",
    "<code>Math.floor(Math.random() * N)</code>: số nguyên [0, N-1]",
    "<code>Math.max(...arr)</code> / <code>Math.min(...arr)</code>: max/min mảng",
    "<code>Math.abs(x)</code>: giá trị tuyệt đối",
    "<code>Math.sqrt(x)</code>: căn bậc hai"],
   """// Random trong khoảng
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
console.log(random(1, 6)); // đổ xúc xắc 1-6

// Sinh màu hex ngẫu nhiên
function mauHexNgauNhien() {
  const hex = Math.floor(Math.random() * 0xFFFFFF).toString(16);
  return '#' + hex.padStart(6, '0');
}
console.log(mauHexNgauNhien()); // e.g. '#3a7f2c'

// Làm tròn giá
const gia = 45678.9;
console.log(Math.round(gia));   // 45679
console.log(Math.floor(gia));   // 45678
console.log(Math.ceil(gia));    // 45679

// Làm tròn đến hàng nghìn
const lam_tron_nghin = x => Math.round(x / 1000) * 1000;
console.log(lam_tron_nghin(45678)); // 46000

// Các hằng số và hàm khác
console.log(Math.PI);          // 3.14159...
console.log(Math.sqrt(144));   // 12
console.log(Math.abs(-42));    // 42
console.log(Math.pow(2, 10));  // 1024
console.log(Math.max(3,1,4,1,5,9,2,6)); // 9
console.log(Math.min(3,1,4,1,5,9,2,6)); // 1"""),

  (17,"Date Object",
   "Làm việc với ngày và giờ trong JavaScript bằng Date object.",
   "Date object cho phép lấy thời gian hiện tại, tính toán khoảng cách ngày, "
   "định dạng và hiển thị ngày tháng.",
   ["In ngày giờ hiện tại theo định dạng Việt Nam",
    "Tính số ngày còn lại đến Tết Dương Lịch",
    "Tính tuổi từ ngày sinh"],
   ["<code>new Date()</code>: thời gian hiện tại",
    "<code>new Date('2024-12-31')</code>: ngày cụ thể",
    "<code>date.getFullYear()</code>, <code>getMonth()</code> (0-11!), <code>getDate()</code>",
    "getMonth() bắt đầu từ 0 – cộng 1 để lấy tháng thực",
    "<code>Date.now()</code>: timestamp hiện tại (ms từ 1/1/1970)",
    "Tính khoảng thời gian: trừ hai Date, chia cho ms/ngày",
    "<code>toLocaleDateString('vi-VN')</code>: định dạng Việt Nam"],
   """// Ngày giờ hiện tại
const now = new Date();
console.log(now.getFullYear());  // 2024
console.log(now.getMonth() + 1); // tháng thực (cộng 1!)
console.log(now.getDate());      // ngày trong tháng
console.log(now.getHours(), now.getMinutes());

// Định dạng Việt Nam
const vn = now.toLocaleDateString('vi-VN', {
  weekday: 'long',
  day: '2-digit', month: '2-digit', year: 'numeric'
});
console.log(vn); // Thứ Hai, 15/01/2024

// Tính số ngày còn lại đến Tết
const tet = new Date(now.getFullYear() + 1, 0, 1); // 1/1 năm sau
const khoangCach = tet - now; // ms
const conLai = Math.ceil(khoangCach / (1000 * 60 * 60 * 24));
console.log(`Còn ${conLai} ngày đến năm mới`);

// Tính tuổi
function tinhTuoi(ngaySinh) {
  const sinh = new Date(ngaySinh);
  const hom_nay = new Date();
  let tuoi = hom_nay.getFullYear() - sinh.getFullYear();
  const chuaSinh = hom_nay < new Date(hom_nay.getFullYear(), sinh.getMonth(), sinh.getDate());
  if (chuaSinh) tuoi--;
  return tuoi;
}
console.log(tinhTuoi('2000-03-15')); // tuổi hiện tại"""),

  (18,"DOM – querySelector và querySelectorAll",
   "Chọn phần tử HTML từ JavaScript bằng querySelector.",
   "DOM (Document Object Model) là giao diện để JavaScript tương tác với HTML. "
   "querySelector dùng CSS selector để tìm phần tử – linh hoạt và mạnh mẽ.",
   ["Chọn phần tử bằng #id, .class, tag, [attribute]",
    "Chọn nhiều phần tử với querySelectorAll",
    "Dùng NodeList.forEach để xử lý nhiều phần tử"],
   ["<code>document.querySelector('.class')</code>: phần tử ĐẦU TIÊN khớp",
    "<code>document.querySelectorAll('li')</code>: NodeList TẤT CẢ phần tử khớp",
    "querySelector dùng CÚ PHÁP CSS: '#id', '.class', 'tag', '[attr]'",
    "<code>document.getElementById('id')</code>: nhanh hơn, ID cụ thể",
    "NodeList.forEach() để lặp – nhưng không có map/filter",
    "Chuyển sang Array: <code>Array.from(nodeList)</code>"],
   """// Chọn phần tử
const title = document.querySelector('h1');
const btn = document.querySelector('#btnDangNhap');
const cards = document.querySelector('.card');
const input = document.querySelector('input[type="email"]');

// Chọn nhiều phần tử
const allLi = document.querySelectorAll('ul li');
const allCards = document.querySelectorAll('.product-card');

// Duyệt NodeList
allCards.forEach((card, index) => {
  console.log(`Card ${index + 1}:`, card.textContent);
});

// Chuyển NodeList sang Array để dùng array methods
const cardArr = Array.from(allCards);
const tenCard = cardArr.map(c => c.querySelector('h3')?.textContent);

// querySelector trong phạm vi phần tử cụ thể
const form = document.querySelector('#formDangNhap');
const emailInput = form.querySelector('input[type="email"]');
// Chỉ tìm trong form, không tìm toàn trang

// Kiểm tra phần tử có tồn tại
if (btn) {
  btn.addEventListener('click', () => console.log('Clicked!'));
}"""),

  (19,"DOM – innerHTML và style",
   "Thay đổi nội dung và style phần tử HTML qua JavaScript.",
   "Sau khi chọn phần tử, chúng ta có thể thay đổi nội dung (innerHTML/textContent) "
   "và style (element.style) để tạo trang web động.",
   ["Tạo button đổi màu nền trang khi click",
    "Hiển thị/ẩn đoạn text khi toggle",
    "Cập nhật nội dung counter khi nhấn +/-"],
   ["<code>el.textContent = 'text'</code>: thay nội dung text (an toàn, không render HTML)",
    "<code>el.innerHTML = '&lt;b&gt;bold&lt;/b&gt;'</code>: render HTML (cẩn thận XSS)",
    "<code>el.style.color = 'red'</code>: đặt style inline",
    "Tên CSS trong JS: camelCase – <code>backgroundColor</code> thay vì <code>background-color</code>",
    "style.display = 'none'/'block': ẩn/hiện",
    "Nên dùng classList.toggle() thay vì thay đổi style trực tiếp"],
   """// textContent vs innerHTML
const tieuDe = document.querySelector('h1');
tieuDe.textContent = 'Tiêu đề mới';      // SAFE
tieuDe.innerHTML = '<em>Tiêu đề</em>';   // Render HTML

// Style trực tiếp
const box = document.querySelector('.box');
box.style.backgroundColor = '#3182ce';   // camelCase!
box.style.padding = '20px';
box.style.borderRadius = '8px';
box.style.display = 'none';   // ẩn
box.style.display = '';       // reset về CSS gốc

// Counter
let dem = 0;
const hienThi = document.getElementById('counter');
const btnTang = document.getElementById('btnTang');
const btnGiam = document.getElementById('btnGiam');

btnTang.addEventListener('click', () => {
  dem++;
  hienThi.textContent = dem;
  hienThi.style.color = dem > 0 ? 'green' : dem < 0 ? 'red' : 'inherit';
});
btnGiam.addEventListener('click', () => {
  dem--;
  hienThi.textContent = dem;
  hienThi.style.color = dem > 0 ? 'green' : dem < 0 ? 'red' : 'inherit';
});"""),

  (20,"DOM – classList",
   "Quản lý class CSS của phần tử bằng classList API.",
   "classList là cách tốt nhất để thay đổi style phần tử: "
   "thêm/xóa/toggle class thay vì sửa style inline trực tiếp. Tách biệt logic và presentation.",
   ["Toggle dark mode: thêm/xóa class 'dark' cho body",
    "Highlight tab active: xóa class active tất cả tab, thêm cho tab được click",
    "Validation: thêm class 'error' / 'success' cho input"],
   ["<code>el.classList.add('class')</code>: thêm class",
    "<code>el.classList.remove('class')</code>: xóa class",
    "<code>el.classList.toggle('class')</code>: thêm nếu chưa có, xóa nếu đã có",
    "<code>el.classList.contains('class')</code>: kiểm tra có class không",
    "<code>el.classList.replace('old','new')</code>: thay đổi class",
    "Nên dùng classList thay vì sửa el.className hay el.style trực tiếp"],
   """// Dark mode toggle
const btn = document.getElementById('btnDarkMode');
btn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  btn.textContent = document.body.classList.contains('dark') ? '☀️ Light' : '🌙 Dark';
});

// Tab active
const tabs = document.querySelectorAll('.tab-btn');
const contents = document.querySelectorAll('.tab-content');

tabs.forEach((tab, i) => {
  tab.addEventListener('click', () => {
    // Xóa active khỏi tất cả
    tabs.forEach(t => t.classList.remove('active'));
    contents.forEach(c => c.classList.remove('active'));
    // Thêm active cho tab được click
    tab.classList.add('active');
    contents[i].classList.add('active');
  });
});

// Input validation
const input = document.querySelector('#email');
input.addEventListener('input', () => {
  const valid = input.value.includes('@');
  input.classList.toggle('error',  !valid);
  input.classList.toggle('success', valid);
});"""),

  (21,"DOM – createElement và appendChild",
   "Tạo phần tử HTML mới và thêm vào DOM bằng JavaScript.",
   "createElement cho phép tạo phần tử HTML động. Kết hợp với appendChild "
   "để render danh sách, thẻ, comment từ dữ liệu.",
   ["Render danh sách sản phẩm từ mảng ra DOM",
    "Tạo nút 'Thêm vào giỏ' cho mỗi sản phẩm",
    "Thêm/xóa item todo trong danh sách"],
   ["<code>document.createElement('div')</code>: tạo phần tử mới (chưa vào DOM)",
    "<code>parent.appendChild(el)</code>: thêm vào cuối parent",
    "<code>parent.prepend(el)</code>: thêm vào đầu parent",
    "<code>el.remove()</code>: xóa phần tử khỏi DOM",
    "<code>parent.insertBefore(new, ref)</code>: chèn trước phần tử ref",
    "innerHTML = template string: nhanh hơn nhưng XSS risk",
    "insertAdjacentHTML: thêm HTML mà không replace nội dung"],
   """// Render danh sách từ data
const sanPhams = [
  { id:1, ten:'Áo Polo', gia:250, img:'ao.jpg' },
  { id:2, ten:'Quần Kaki', gia:320, img:'quan.jpg' },
];

const container = document.getElementById('product-list');

function renderSanPham(sp) {
  const card = document.createElement('div');
  card.className = 'product-card';
  card.innerHTML = `
    <img src="${sp.img}" alt="${sp.ten}" />
    <div class="card-body">
      <h3>${sp.ten}</h3>
      <p>${sp.gia.toLocaleString()}đ</p>
      <button data-id="${sp.id}" class="btn-add">Thêm giỏ</button>
    </div>
  `;
  // Sự kiện nút thêm giỏ
  card.querySelector('.btn-add').addEventListener('click', (e) => {
    themGio(sp.id);
  });
  return card;
}

sanPhams.forEach(sp => container.appendChild(renderSanPham(sp)));

// Todo list
function themTodo(text) {
  const li = document.createElement('li');
  li.innerHTML = `<span>${text}</span><button class="xoa">✕</button>`;
  li.querySelector('.xoa').addEventListener('click', () => li.remove());
  document.getElementById('todo-list').appendChild(li);
}"""),

  (22,"DOM – addEventListener",
   "Gắn sự kiện cho phần tử HTML bằng addEventListener.",
   "addEventListener là cách hiện đại để lắng nghe sự kiện: click, input, "
   "submit, mouseover, keydown... Cho phép một phần tử có nhiều handler.",
   ["Gắn sự kiện click cho button",
    "Lắng nghe sự kiện input để hiển thị ký tự đã nhập theo thời gian thực",
    "Sự kiện mouseover/mouseout để tooltip",
    "Xóa sự kiện bằng removeEventListener"],
   ["<code>el.addEventListener('click', handler)</code>",
    "Tên sự kiện: 'click', 'input', 'change', 'submit', 'keydown', 'mouseover'...",
    "Handler là function nhận tham số event object",
    "<code>event.target</code>: phần tử gây ra sự kiện",
    "<code>event.preventDefault()</code>: ngăn hành vi mặc định (submit form, click link...)",
    "<code>removeEventListener</code>: phải dùng ĐÚNG function reference để xóa"],
   """// Sự kiện click
const btn = document.getElementById('myBtn');
btn.addEventListener('click', (e) => {
  console.log('Đã click!', e.target);
  e.target.textContent = 'Đã nhấn ✓';
});

// Sự kiện input theo thời gian thực
const input = document.getElementById('search');
const preview = document.getElementById('preview');
input.addEventListener('input', (e) => {
  preview.textContent = e.target.value;
  preview.style.display = e.target.value ? 'block' : 'none';
});

// Sự kiện form submit
const form = document.getElementById('myForm');
form.addEventListener('submit', (e) => {
  e.preventDefault();           // Ngăn trang reload
  const data = new FormData(form);
  console.log(Object.fromEntries(data));
});

// Event delegation: gắn 1 sự kiện cho parent
document.getElementById('list').addEventListener('click', (e) => {
  if (e.target.matches('li')) {
    e.target.classList.toggle('done');
  }
});"""),

  (23,"Sự kiện Mouse và Keyboard",
   "Xử lý sự kiện chuột và bàn phím để tạo tương tác phong phú.",
   "JavaScript cung cấp nhiều sự kiện cho chuột (click, hover, drag) "
   "và bàn phím (keydown, keyup, keypress). Kết hợp để tạo UX tốt.",
   ["Vẽ theo chuột trên canvas (mousedown + mousemove)",
    "Phím tắt: nhấn Enter để submit, Escape để đóng modal",
    "Kéo thả đơn giản với mousedown/mousemove/mouseup"],
   ["Mouse events: click, dblclick, mousedown, mouseup, mousemove, mouseenter, mouseleave",
    "Keyboard events: keydown, keyup, keypress (deprecated)",
    "<code>event.key</code>: 'Enter', 'Escape', 'a', 'A', 'ArrowUp'...",
    "<code>event.code</code>: 'KeyA', 'ArrowUp' – không phụ thuộc ngôn ngữ",
    "<code>event.ctrlKey, shiftKey, altKey</code>: phím modifier",
    "<code>e.clientX, e.clientY</code>: tọa độ chuột trong viewport"],
   """// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
  if (e.key === 's' && e.ctrlKey) {
    e.preventDefault();
    saveData();
  }
  if (e.key === 'ArrowUp')   moveUp();
  if (e.key === 'ArrowDown') moveDown();
});

// Vẽ bằng chuột
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let isDrawing = false;

canvas.addEventListener('mousedown', () => { isDrawing = true; });
canvas.addEventListener('mouseup', () => { isDrawing = false; ctx.beginPath(); });
canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  const rect = canvas.getBoundingClientRect();
  ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
  ctx.stroke();
});

// Mouse enter/leave
const tooltip = document.getElementById('tooltip');
document.querySelectorAll('[data-tip]').forEach(el => {
  el.addEventListener('mouseenter', (e) => {
    tooltip.textContent = e.target.dataset.tip;
    tooltip.style.display = 'block';
  });
  el.addEventListener('mouseleave', () => {
    tooltip.style.display = 'none';
  });
});"""),

  (24,"Form Validation bằng JavaScript",
   "Validate form phía client trước khi gửi dữ liệu lên server.",
   "Validation phía client cho phản hồi ngay lập tức cho người dùng. "
   "Cần validate cả phía server, nhưng client validation cải thiện UX rất nhiều.",
   ["Validate form đăng ký: tên, email, mật khẩu, xác nhận mật khẩu",
    "Hiển thị lỗi ngay dưới mỗi ô input",
    "Highlight input lỗi màu đỏ, thành công màu xanh",
    "Chỉ cho submit khi tất cả hợp lệ"],
   ["Validate khi blur (rời ô input) và khi submit",
    "Tạo hàm validate riêng cho từng trường",
    "Thêm class 'error'/'valid' và text thông báo",
    "Regex cho email: <code>/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/</code>",
    "Mật khẩu: độ dài, có chữ hoa, số, ký tự đặc biệt"],
   """function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email.trim());
}
function validatePassword(pw) {
  return pw.length >= 8 && /[A-Z]/.test(pw) && /[0-9]/.test(pw);
}

function showError(input, msg) {
  const wrap = input.closest('.form-group') || input.parentElement;
  input.classList.add('error'); input.classList.remove('valid');
  let err = wrap.querySelector('.err-msg');
  if (!err) { err = document.createElement('p'); err.className = 'err-msg'; wrap.appendChild(err); }
  err.textContent = msg;
}
function showValid(input) {
  const wrap = input.closest('.form-group') || input.parentElement;
  input.classList.remove('error'); input.classList.add('valid');
  const err = wrap.querySelector('.err-msg');
  if (err) err.textContent = '';
}

document.getElementById('regForm').addEventListener('submit', (e) => {
  e.preventDefault();
  let ok = true;
  const email = document.getElementById('email');
  const pw = document.getElementById('password');
  const pw2 = document.getElementById('confirm');
  if (!validateEmail(email.value)) { showError(email, 'Email không hợp lệ'); ok = false; }
  else showValid(email);
  if (!validatePassword(pw.value)) { showError(pw, 'Mật khẩu ≥8 ký tự, có chữ hoa và số'); ok = false; }
  else showValid(pw);
  if (pw.value !== pw2.value) { showError(pw2, 'Mật khẩu không khớp'); ok = false; }
  else showValid(pw2);
  if (ok) alert('Đăng ký thành công!');
});"""),

  (25,"setTimeout và setInterval",
   "Thực thi code theo thời gian với setTimeout và setInterval.",
   "setTimeout chạy code sau một khoảng thời gian. setInterval chạy code lặp lại "
   "sau mỗi khoảng thời gian. Cả hai đều bất đồng bộ.",
   ["Tạo đồng hồ đếm giờ thực (HH:MM:SS) dùng setInterval",
    "Tạo countdown timer: 60 giây đếm ngược",
    "Toast notification tự ẩn sau 3 giây"],
   ["<code>setTimeout(fn, ms)</code>: chạy fn SAU ms mili giây (1 lần)",
    "<code>setInterval(fn, ms)</code>: chạy fn mỗi ms mili giây (lặp lại)",
    "<code>clearTimeout(id)</code> / <code>clearInterval(id)</code>: hủy timer",
    "Lưu return value của setTimeout/setInterval để có thể hủy",
    "setInterval không chính xác 100% – mỗi lần chạy có thể trễ chút",
    "Dùng Date.now() thay setInterval cho timer chính xác hơn"],
   """// Đồng hồ thực
function capNhatGio() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2,'0');
  const m = String(now.getMinutes()).padStart(2,'0');
  const s = String(now.getSeconds()).padStart(2,'0');
  document.getElementById('clock').textContent = `${h}:${m}:${s}`;
}
capNhatGio(); // Chạy ngay lần đầu
const clockInterval = setInterval(capNhatGio, 1000);

// Countdown Timer
let con_lai = 60;
const hien = document.getElementById('countdown');
const timer = setInterval(() => {
  hien.textContent = con_lai;
  if (con_lai <= 0) {
    clearInterval(timer);
    hien.textContent = 'Hết giờ!';
    return;
  }
  con_lai--;
}, 1000);

// Toast notification
function hienToast(msg, type = 'success') {
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = msg;
  document.body.appendChild(toast);
  // Thêm class show sau 10ms để trigger transition
  setTimeout(() => toast.classList.add('show'), 10);
  // Ẩn sau 3s
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}"""),

  (26,"Xử lý Array nâng cao: sort, flat, Object.entries",
   "Sắp xếp mảng, xử lý mảng lồng nhau và chuyển đổi giữa Object và Array.",
   "sort() sắp xếp mảng theo tiêu chí tùy chỉnh. flat() làm phẳng mảng lồng nhau. "
   "Object.entries/keys/values chuyển object thành array để xử lý.",
   ["Sắp xếp danh sách sản phẩm theo giá tăng/giảm",
    "Sắp xếp theo tên (locale-aware cho tiếng Việt)",
    "Nhóm sản phẩm theo category dùng reduce"],
   ["<code>arr.sort((a,b) => a-b)</code>: sắp xếp tăng dần (số)",
    "<code>arr.sort((a,b) => b-a)</code>: sắp xếp giảm dần",
    "<code>arr.sort((a,b) => a.ten.localeCompare(b.ten, 'vi'))</code>: so sánh chuỗi Việt",
    "<code>Object.entries(obj)</code>: mảng [key, value] pairs",
    "<code>Object.keys(obj)</code>: mảng các key",
    "<code>Object.values(obj)</code>: mảng các value",
    "sort() THAY ĐỔI mảng gốc – dùng [...arr].sort() nếu muốn giữ nguyên"],
   """const sp = [
  { ten:'Áo', gia:150, cat:'quần-áo' },
  { ten:'Bàn', gia:500, cat:'nội-thất' },
  { ten:'Quần', gia:80, cat:'quần-áo' },
  { ten:'Ghế', gia:300, cat:'nội-thất' },
];

// Sắp xếp giá tăng (không đổi gốc)
const tangGia = [...sp].sort((a,b) => a.gia - b.gia);
const giamGia = [...sp].sort((a,b) => b.gia - a.gia);

// Sắp xếp tên tiếng Việt
const theoTen = [...sp].sort((a,b) => a.ten.localeCompare(b.ten, 'vi'));

// Nhóm theo category (group by)
const theo_cat = sp.reduce((acc, item) => {
  if (!acc[item.cat]) acc[item.cat] = [];
  acc[item.cat].push(item);
  return acc;
}, {});
console.log(theo_cat);
// { 'quần-áo': [...], 'nội-thất': [...] }

// Xử lý dùng Object.entries
Object.entries(theo_cat).forEach(([cat, items]) => {
  console.log(`${cat}: ${items.length} sản phẩm`);
});"""),

  (27,"Closure và Scope",
   "Hiểu scope và closure để viết code không bị lỗi biến toàn cục.",
   "Scope xác định phạm vi biến có thể truy cập. Closure là hàm "
   "có thể nhớ scope bên ngoài sau khi scope đó đã kết thúc.",
   ["Tạo counter factory bằng closure: mỗi counter độc lập",
    "Meme kinh điển: vòng lặp setTimeout với var vs let",
    "Tạo private variable bằng closure"],
   ["Block scope: <code>let/const</code> chỉ trong {} hiện tại",
    "Function scope: <code>var</code> trong function",
    "Global scope: ngoài tất cả function",
    "Closure: hàm 'nhớ' biến từ scope cha dù scope cha đã kết thúc",
    "Vấn đề var + vòng lặp: dùng let hoặc IIFE để fix",
    "Module pattern dùng closure để tạo private state"],
   """// Closure: counter factory
function taoCounter(batDau = 0) {
  let dem = batDau;  // private – bên ngoài không truy cập được
  return {
    tang:  () => ++dem,
    giam:  () => --dem,
    reset: () => { dem = batDau; },
    lay:   () => dem,
  };
}
const c1 = taoCounter(0);
const c2 = taoCounter(10);
c1.tang(); c1.tang(); // c1 = 2
c2.giam();            // c2 = 9
console.log(c1.lay(), c2.lay()); // 2, 9 – ĐỘC LẬP !

// VAR vs LET trong vòng lặp
// Vấn đề với var:
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log('var:', i), 100);
}
// In ra: 3, 3, 3 (vì var chia sẻ cùng i)

// Fix bằng let:
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log('let:', j), 100);
}
// In ra: 0, 1, 2 (let có block scope riêng mỗi lần lặp)

// Module pattern
const BankAccount = (() => {
  let balance = 0;           // private
  return {
    deposit: (n) => { if(n>0) balance+=n; },
    withdraw: (n) => { if(n>0&&balance>=n) balance-=n; },
    getBalance: () => balance,
  };
})();"""),

  (28,"Error Handling – try-catch",
   "Xử lý lỗi trong JavaScript bằng try-catch-finally.",
   "Lỗi không được xử lý khiến chương trình dừng đột ngột. try-catch "
   "bẫy lỗi để xử lý gracefully. finally luôn chạy dù có lỗi hay không.",
   ["Bẫy lỗi khi parse JSON không hợp lệ",
    "Custom error class kế thừa Error",
    "Xử lý lỗi trong async/await"],
   ["<code>try { } catch(err) { } finally { }</code>",
    "<code>err.message</code>: thông báo lỗi",
    "<code>err.name</code>: loại lỗi (TypeError, RangeError...)",
    "<code>throw new Error('message')</code>: ném lỗi tự định nghĩa",
    "<code>finally</code>: luôn chạy – dùng để cleanup (đóng file, loading spinner tắt)",
    "Custom Error: <code>class MyError extends Error { }</code>"],
   """// try-catch cơ bản
try {
  const data = JSON.parse('{ sai json }');
} catch (err) {
  console.log('Lỗi JSON:', err.message);
  console.log('Loại lỗi:', err.name); // SyntaxError
}

// finally: luôn chạy – dùng để tắt loading
function fetchData(url) {
  showLoading(true);
  try {
    const data = getData(url);
    renderData(data);
  } catch (err) {
    showError(err.message);
  } finally {
    showLoading(false); // Luôn tắt loading
  }
}

// Custom Error
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}
function validateAge(age) {
  if (age < 0 || age > 150) throw new ValidationError('age', 'Tuổi không hợp lệ');
  return true;
}
try { validateAge(-5); }
catch (err) {
  if (err instanceof ValidationError) console.log(`Lỗi trường ${err.field}: ${err.message}`);
  else throw err; // Re-throw lỗi không handle được
}"""),

  (29,"Local Storage",
   "Lưu trữ dữ liệu trên trình duyệt bằng localStorage.",
   "localStorage cho phép lưu dữ liệu trên trình duyệt, tồn tại sau khi "
   "đóng tab. Dùng cho: theme, cài đặt, todo list, giỏ hàng...",
   ["Lưu và đọc theme (dark/light) trong localStorage",
    "Todo list lưu vào localStorage, reload không mất dữ liệu",
    "Giỏ hàng đơn giản lưu localStorage"],
   ["<code>localStorage.setItem('key', 'value')</code>: chỉ lưu string",
    "<code>localStorage.getItem('key')</code>: đọc ra",
    "<code>localStorage.removeItem('key')</code>: xóa 1 key",
    "<code>localStorage.clear()</code>: xóa tất cả",
    "Object/Array: <code>JSON.stringify()</code> trước khi lưu, <code>JSON.parse()</code> khi đọc",
    "localStorage: tồn tại mãi (5-10MB)",
    "sessionStorage: chỉ tồn tại trong tab hiện tại"],
   """// Lưu/đọc dữ liệu đơn giản
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme'); // 'dark'

// Áp dụng theme khi load
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.classList.add(savedTheme);

// Object/Array: cần JSON
const todos = [
  { id: 1, text: 'Học JavaScript', done: false },
  { id: 2, text: 'Làm bài tập', done: true },
];
localStorage.setItem('todos', JSON.stringify(todos));

// Đọc lại
const saved = JSON.parse(localStorage.getItem('todos') || '[]');

// Helper functions
const storage = {
  get: (key, def=null) => {
    try { return JSON.parse(localStorage.getItem(key)) ?? def; }
    catch { return def; }
  },
  set: (key, val) => localStorage.setItem(key, JSON.stringify(val)),
  del: (key) => localStorage.removeItem(key),
};
// Sử dụng:
storage.set('user', { name: 'An', age: 25 });
const user = storage.get('user', {});
console.log(user.name); // 'An'"""),

  (30,"🏆 Dự án: Máy Tính Bỏ Túi",
   "Xây dựng máy tính bỏ túi đầy đủ bằng HTML, CSS và JavaScript.",
   "Dự án cuối module tổng hợp: DOM manipulation, sự kiện, logic toán học, "
   "edge cases xử lý. Máy tính có giao diện giống iPhone Calculator.",
   ["Giao diện HTML/CSS giống máy tính thực tế",
    "Xử lý click phím số 0-9",
    "Xử lý phép tính: +, -, ×, ÷",
    "Xử lý dấu thập phân, phần trăm, đổi dấu +/-",
    "Nút AC xóa tất cả, C xóa 1 ký tự",
    "Hiển thị lịch sử phép tính",
    "Keyboard support: nhấn phím số và phép tính"],
   ["State management: lưu currentValue, previousValue, operator, waitingForSecond",
    "Edge cases: chia cho 0, số quá lớn, dấu phẩy chỉ 1 lần",
    "Sử dụng eval() không an toàn – tự viết logic tính",
    "parseFloat để xử lý số thập phân",
    "toFixed() để tránh floating point issue: 0.1+0.2"],
   """// State
const state = {
  current: '0',
  previous: '',
  operator: null,
  justEvaluated: false,
};

// UI elements
const hienThi = document.getElementById('display');
const lich_su = document.getElementById('history');

function capNhatManHinh() {
  hienThi.textContent = parseFloat(state.current).toLocaleString() || '0';
}

function nhapSo(so) {
  if (state.justEvaluated) { state.current = so; state.justEvaluated = false; return; }
  if (state.current === '0' && so !== '.') { state.current = so; return; }
  if (so === '.' && state.current.includes('.')) return;
  if (state.current.replace('.','').length >= 10) return;
  state.current += so;
}

function chonPhep(phep) {
  if (state.operator && !state.justEvaluated) bTinhKetQua();
  state.previous = state.current;
  state.operator = phep;
  state.justEvaluated = false;
  state.current = '0';
  lich_su.textContent = `${state.previous} ${phep}`;
}

function bTinhKetQua() {
  const a = parseFloat(state.previous), b = parseFloat(state.current);
  let kq;
  switch (state.operator) {
    case '+': kq = a + b; break;
    case '-': kq = a - b; break;
    case '×': kq = a * b; break;
    case '÷': kq = b !== 0 ? a / b : 'Lỗi'; break;
    default: return;
  }
  lich_su.textContent = `${a} ${state.operator} ${b} =`;
  state.current = kq === 'Lỗi' ? '0' : String(parseFloat(kq.toFixed(10)));
  state.operator = null; state.justEvaluated = true;
}

function xoaTat() { state.current = '0'; state.previous = ''; state.operator = null; lich_su.textContent = ''; }
function xoa1() { state.current = state.current.length > 1 ? state.current.slice(0,-1) : '0'; }
function doiDau() { state.current = String(-parseFloat(state.current)); }
function phanTram() { state.current = String(parseFloat(state.current) / 100); }

// Keyboard support
document.addEventListener('keydown', (e) => {
  if (e.key >= '0' && e.key <= '9') nhapSo(e.key);
  if (e.key === '.') nhapSo('.');
  if (e.key === '+') chonPhep('+');
  if (e.key === '-') chonPhep('-');
  if (e.key === '*') chonPhep('×');
  if (e.key === '/') { e.preventDefault(); chonPhep('÷'); }
  if (e.key === 'Enter' || e.key === '=') bTinhKetQua();
  if (e.key === 'Escape') xoaTat();
  if (e.key === 'Backspace') xoa1();
  capNhatManHinh();
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

print(f"\nModule 4 – JavaScript Cơ Bản: Đã tạo {count} file")
