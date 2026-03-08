# gen_php1.py – Module 1: PHP Cơ Bản (25 bài)
# Run from: course-php/_gen/
import pathlib, textwrap

ROOT = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-php")
MOD  = ROOT / "module-01-php-co-ban"
MOD.mkdir(parents=True, exist_ok=True)

EXERCISES = [
  # (n, title, short_desc, req_list, know_list, code_sample)
  (1,
   "Cú Pháp PHP Cơ Bản – echo, print",
   "Viết chương trình PHP đầu tiên sử dụng echo và print để xuất nội dung.",
   [
     "Tạo file <code>index.php</code> với cấu trúc chuẩn <code>&lt;?php ... ?&gt;</code>",
     "Dùng <code>echo</code> để in một câu chào mừng bằng tiếng Việt",
     "Dùng <code>print</code> để in một câu khác",
     "In ra các thẻ HTML (<code>h1</code>, <code>p</code>) bằng echo",
     "Dùng echo để in nhiều giá trị cách nhau bởi dấu phẩy",
   ],
   [
     "<code>echo</code>: xuất một hoặc nhiều chuỗi, không trả về giá trị",
     "<code>print</code>: xuất một chuỗi, trả về 1 (có thể dùng trong biểu thức)",
     "PHP code nằm trong cặp thẻ <code>&lt;?php ... ?&gt;</code> hoặc <code>&lt;?= ... ?&gt;</code>",
     "Dấu chấm phẩy <code>;</code> kết thúc mỗi câu lệnh",
     "<code>echo 'a', 'b';</code> in 'ab' — nhưng <code>print</code> chỉ nhận 1 tham số",
   ],
   """\
<?php
// 1. echo cơ bản
echo "Xin chào! Đây là trang PHP đầu tiên của tôi.";
echo "<br>";

// 2. echo nhiều giá trị (dùng dấu phẩy)
echo "Tên: ", "Nguyễn Văn A", " – Tuổi: ", 22;
echo "<br>";

// 3. print (trả về 1)
$ket_qua = print("PHP rất thú vị!<br>");
echo "Giá trị trả về của print: " . $ket_qua . "<br>";

// 4. In thẻ HTML bằng echo
echo "<h2>Danh sách môn học</h2>";
echo "<ul>";
echo "  <li>HTML / CSS</li>";
echo "  <li>JavaScript</li>";
echo "  <li>PHP</li>";
echo "</ul>";

// 5. Cú pháp echo ngắn (short tag)
?>
<h3>Thông tin:</h3>
<p>Phiên bản PHP: <?= PHP_VERSION ?></p>
<p>Hệ điều hành: <?= PHP_OS ?></p>"""
  ),
  (2,
   "Biến và Kiểu Dữ Liệu Trong PHP",
   "Khai báo và sử dụng biến PHP với các kiểu dữ liệu: string, int, float, bool, null.",
   [
     "Khai báo biến tên, tuổi, chiều cao, là sinh viên (bool)",
     "In kiểu dữ liệu của mỗi biến bằng <code>gettype()</code>",
     "Dùng <code>var_dump()</code> để xem chi tiết biến",
     "Chuyển đổi kiểu dữ liệu (type casting): int → float → string",
     "Dùng <code>isset()</code>, <code>empty()</code>, <code>is_null()</code>",
   ],
   [
     "Biến PHP bắt đầu bằng <code>$</code>: <code>$ten</code>, <code>$tuoi</code>",
     "8 kiểu dữ liệu: int, float, string, bool, array, object, NULL, resource",
     "<code>var_dump($x)</code> — hiện type + value (rất hữu ích để debug)",
     "<code>gettype($x)</code> — trả về chuỗi tên kiểu (\"integer\", \"string\"...)",
     "PHP là ngôn ngữ loosely typed — biến tự thay đổi kiểu dữ liệu",
   ],
   """\
<?php
// ── Khai báo biến ──────────────────
$ten      = "Nguyễn Thị Bình";    // string
$tuoi     = 21;                    // integer
$diem_tb  = 8.75;                  // float
$la_sv    = true;                  // boolean
$que_quan = null;                  // NULL

// ── In kiểu dữ liệu ────────────────
echo gettype($ten)     . "<br>";   // string
echo gettype($tuoi)    . "<br>";   // integer
echo gettype($diem_tb) . "<br>";   // double
echo gettype($la_sv)   . "<br>";   // boolean

// ── var_dump chi tiết ──────────────
var_dump($ten);       // string(18) "Nguyễn Thị Bình"
var_dump($tuoi);      // int(21)
var_dump($diem_tb);   // float(8.75)
var_dump($la_sv);     // bool(true)
var_dump($que_quan);  // NULL

// ── Type casting (ép kiểu) ─────────
$so_nguyen = (int) 3.9;       // → 3 (cắt phần thập phân)
$so_thuc   = (float) "4.5px"; // → 4.5 (lấy đến ký tự phi số đầu tiên)
$chuoi     = (string) 100;    // → "100"
$bool      = (bool) 0;        // → false (0, "", "0", [] là false)
echo $so_nguyen . " | " . $so_thuc . " | " . $chuoi . "<br>";

// ── Kiểm tra biến ─────────────────
$bien_chua_dat;
echo isset($ten)         ? "ten: đã set<br>"    : "ten: chưa set<br>";
echo isset($bien_chua_dat) ? "đã set<br>"       : "chưa set<br>";
echo empty($que_quan)    ? "que_quan: rỗng<br>" : "có giá trị<br>";"""
  ),
  (3,
   "Toán Tử Trong PHP",
   "Sử dụng các toán tử số học, so sánh, logic và chuỗi trong PHP.",
   [
     "Tính toán với 5 phép tính cơ bản và modulo (<code>%</code>), lũy thừa (<code>**</code>)",
     "So sánh bằng <code>==</code> (giá trị) và <code>===</code> (giá trị + kiểu dữ liệu)",
     "Dùng toán tử logic: AND <code>&&</code>, OR <code>||</code>, NOT <code>!</code>",
     "Nối chuỗi bằng <code>.</code>, gán nối chuỗi bằng <code>.=</code>",
     "Toán tử ba ngôi (ternary) và null coalescing <code>??</code>",
   ],
   [
     "<code>==</code>: so sánh giá trị (1 == \"1\" là true); <code>===</code>: strict (1 === \"1\" là false)",
     "<code>%</code> lấy phần dư; <code>**</code> lũy thừa (2**10 = 1024)",
     "<code>.</code> nối chuỗi: \"Hello \" . \"World\" → \"Hello World\"",
     "<code>$a ?? $b</code>: trả về <code>$a</code> nếu không null, ngược lại trả <code>$b</code>",
     "<code>$a <=> $b</code>: spaceship operator — trả về -1, 0, hoặc 1",
   ],
   """\
<?php
// ── Số học ─────────────────────────
$a = 17; $b = 5;
echo "$a + $b = " . ($a + $b) . "<br>";   // 22
echo "$a - $b = " . ($a - $b) . "<br>";   // 12
echo "$a * $b = " . ($a * $b) . "<br>";   // 85
echo "$a / $b = " . ($a / $b) . "<br>";   // 3.4
echo "$a % $b = " . ($a % $b) . "<br>";   // 2  (phần dư)
echo "2 ** 10 = " . (2 ** 10)  . "<br>";  // 1024

// ── So sánh ────────────────────────
var_dump(1 == "1");   // true  (kiểu khác nhưng giá trị bằng)
var_dump(1 === "1");  // false (kiểu khác nhau)
var_dump(1 !== "1");  // true
var_dump(10 <=> 20);  // -1 (10 nhỏ hơn 20)

// ── Logic ──────────────────────────
$diem = 7.5; $diem_danh_gia = "B";
if ($diem >= 5 && $diem < 8) {
    echo "Khá – đạt yêu cầu<br>";
}
if ($diem < 5 || $diem_danh_gia === "F") {
    echo "Không đạt<br>";
} else {
    echo "Đạt<br>";
}

// ── Nối chuỗi ─────────────────────
$ho = "Trần"; $ten = "Văn C";
$ho_ten  = $ho . " " . $ten;    // nối bằng .
$ho_ten .= " (Sinh viên)";       // gán nối .=
echo $ho_ten . "<br>";

// ── Ternary & Null Coalescing ──────
$tuoi = 20;
echo ($tuoi >= 18 ? "Đủ tuổi" : "Chưa đủ tuổi") . "<br>";

$ten_nhap = null;
$hien_thi = $ten_nhap ?? "Khách";   // null coalescing
echo "Xin chào, $hien_thi!<br>";"""
  ),
  (4,
   "Xử Lý Chuỗi (String Functions)",
   "Dùng các hàm xử lý chuỗi phổ biến của PHP để thao tác với văn bản.",
   [
     "Đếm độ dài chuỗi, chuyển HOA/thường",
     "Cắt khoảng trắng, tìm kiếm trong chuỗi",
     "Thay thế chuỗi con, cắt chuỗi",
     "Định dạng chuỗi với <code>sprintf</code>",
     "Tách chuỗi thành mảng và ngược lại",
   ],
   [
     "<code>strlen($s)</code>: độ dài chuỗi; <code>mb_strlen($s)</code>: đếm đúng Unicode/tiếng Việt",
     "<code>strtolower()</code> / <code>strtoupper()</code> — chuyển hoa/thường",
     "<code>trim()</code> cắt đầu cuối; <code>ltrim()</code> / <code>rtrim()</code> cắt trái/phải",
     "<code>str_replace($tim, $thay, $str)</code> — thay thế chuỗi con",
     "<code>explode($sep, $str)</code> → array; <code>implode($sep, $arr)</code> → string",
   ],
   """\
<?php
$chuoi = "  Chào mừng bạn đến với PHP!  ";

// ── Độ dài và khoảng trắng ────────
echo strlen($chuoi) . "<br>";       // đếm byte (sai với UTF-8)
echo mb_strlen($chuoi) . "<br>";    // đếm ký tự đúng (UTF-8)
$sach = trim($chuoi);               // cắt đầu cuối
echo strlen($sach) . "<br>";

// ── Hoa / Thường ──────────────────
$ten = "nguyen van A";
echo strtoupper($ten) . "<br>";   // NGUYEN VAN A
echo strtolower($ten) . "<br>";   // nguyen van a
echo ucfirst($ten)    . "<br>";   // Nguyen van A
echo ucwords($ten)    . "<br>";   // Nguyen Van A

// ── Tìm kiếm ─────────────────────
$str = "PHP là ngôn ngữ phổ biến";
echo strpos($str, "ngôn ngữ") . "<br>";   // vị trí (byte)
echo (str_contains($str, "PHP") ? "Có PHP<br>" : "Không có<br>");  // PHP 8+
echo substr_count($str, "n") . "<br>";    // đếm lần xuất hiện của "n"

// ── Thay thế ─────────────────────
$html = "<h1>Tiêu đề</h1><p>Nội dung</p>";
echo strip_tags($html) . "<br>";             // bỏ thẻ HTML
echo str_replace("PHP", "Python", $str) . "<br>";

// ── Cắt chuỗi ────────────────────
echo substr($str, 0, 10) . "...<br>";   // 10 ký tự đầu

// ── sprintf (định dạng) ───────────
$gia = 1250000;
$ten_sp = "Áo thun";
echo sprintf("Sản phẩm: %s – Giá: %s đồng<br>", $ten_sp, number_format($gia, 0, ',', '.'));

// ── explode / implode ─────────────
$emails = "a@x.com,b@x.com,c@x.com";
$arr    = explode(",", $emails);     // tách thành array
echo count($arr) . " email<br>";
$lai  = implode(" | ", $arr);       // ghép lại
echo $lai . "<br>";"""
  ),
  (5,
   "Mảng (Array) Cơ Bản",
   "Tạo và thao tác với mảng chỉ số (indexed) và mảng kết hợp (associative).",
   [
     "Tạo mảng chỉ số <code>[]</code>, thêm phần tử, in mảng bằng <code>print_r</code>",
     "Tạo mảng kết hợp (key => value)",
     "Duyệt mảng bằng <code>foreach</code>",
     "Sắp xếp mảng: <code>sort()</code>, <code>rsort()</code>, <code>asort()</code>",
     "Tìm kiếm phần tử: <code>in_array()</code>, <code>array_search()</code>",
   ],
   [
     "Mảng chỉ số: <code>$arr = [1, 2, 3]</code> — key tự động 0, 1, 2...",
     "Mảng kết hợp: <code>$arr = ['ten' => 'An', 'tuoi' => 20]</code>",
     "<code>count($arr)</code> — số phần tử; <code>array_push($arr, $val)</code> — thêm cuối",
     "<code>sort()</code> sắp xếp tăng dần (reset key); <code>asort()</code> giữ key gốc",
     "<code>in_array($val, $arr)</code> — kiểm tra tồn tại; <code>array_search()</code> trả key",
   ],
   """\
<?php
// ── Mảng chỉ số ───────────────────
$mon_hoc = ["Toán", "Văn", "Anh", "Lý", "Hóa"];
echo "Số môn: " . count($mon_hoc) . "<br>";
echo $mon_hoc[0] . "<br>";   // Toán
array_push($mon_hoc, "Sinh"); // thêm cuối
$mon_hoc[] = "Sử";            // cách 2 thêm cuối
echo implode(", ", $mon_hoc) . "<br>";

// ── Mảng kết hợp ──────────────────
$sinh_vien = [
    "ho_ten" => "Lê Thị Mai",
    "tuoi"   => 20,
    "diem"   => 8.5,
    "lop"    => "CNTT-K22",
];
echo $sinh_vien["ho_ten"] . " – Lớp " . $sinh_vien["lop"] . "<br>";
$sinh_vien["dia_chi"] = "Hà Nội";   // thêm key mới
print_r($sinh_vien);

// ── foreach ───────────────────────
echo "<ul>";
foreach ($sinh_vien as $key => $val) {
    echo "<li><strong>$key</strong>: $val</li>";
}
echo "</ul>";

// ── Sắp xếp ──────────────────────
$diem_sv = [7.5, 9.0, 6.5, 8.0, 5.5];
sort($diem_sv);                           // tăng dần
echo implode(", ", $diem_sv) . "<br>";

rsort($diem_sv);                          // giảm dần
echo implode(", ", $diem_sv) . "<br>";

// ── Tìm kiếm ─────────────────────
if (in_array(9.0, $diem_sv)) {
    echo "Có điểm 9.0 trong mảng<br>";
}
$vi_tri = array_search(8.0, $diem_sv);
echo "Điểm 8.0 ở vị trí: $vi_tri<br>";"""
  ),
  (6,
   "Câu Lệnh Điều Kiện if / else / elseif",
   "Sử dụng cấu trúc điều kiện để thực hiện logic phân nhánh trong PHP.",
   [
     "Viết hàm xếp loại học lực dựa vào điểm trung bình",
     "Dùng <code>if / elseif / else</code> để phân loại tháng theo mùa",
     "Dùng toán tử điều kiện lồng nhau",
     "Dùng <code>match</code> (PHP 8) thay thế if/else",
     "Viết chương trình kiểm tra năm nhuận",
   ],
   [
     "<code>if ($dk) { } elseif ($dk2) { } else { }</code>",
     "Điều kiện trúng khi biểu thức truthy (khác 0, khác \"\", khác null, khác [])",
     "<code>match($x)</code> so sánh strict (===) và ngắn gọn hơn switch",
     "Toán tử <code>?:</code> (Elvis): <code>$a ?: $b</code> trả về $a nếu truthy, ngược lại $b",
     "Năm nhuận: chia hết 400, hoặc chia hết 4 nhưng không chia hết 100",
   ],
   """\
<?php
// ── Xếp loại học lực ──────────────
function xep_loai(float $diem): string {
    if ($diem >= 9.0) return "Xuất sắc";
    elseif ($diem >= 8.0) return "Giỏi";
    elseif ($diem >= 7.0) return "Khá";
    elseif ($diem >= 5.0) return "Trung bình";
    else return "Yếu";
}
$danh_sach_diem = [9.5, 8.2, 6.8, 5.1, 4.0];
foreach ($danh_sach_diem as $d) {
    echo "$d → " . xep_loai($d) . "<br>";
}

// ── Mùa theo tháng (match PHP 8) ──
$thang = (int) date('n');   // tháng hiện tại
$mua = match(true) {
    in_array($thang, [12, 1, 2]) => "Mùa Đông ❄️",
    in_array($thang, [3, 4, 5])  => "Mùa Xuân 🌸",
    in_array($thang, [6, 7, 8])  => "Mùa Hè ☀️",
    default                      => "Mùa Thu 🍂",
};
echo "Tháng $thang: $mua<br>";

// ── Năm nhuận ─────────────────────
function la_nam_nhuan(int $nam): bool {
    return ($nam % 400 === 0) || ($nam % 4 === 0 && $nam % 100 !== 0);
}
foreach ([2000, 1900, 2024, 2023] as $nam) {
    $ket = la_nam_nhuan($nam) ? "Nhuận ✅" : "Thường ❌";
    echo "$nam: $ket<br>";
}"""
  ),
  (7,
   "Switch / Case và Match",
   "Sử dụng switch/case để phân nhánh nhiều trường hợp, so sánh với match của PHP 8.",
   [
     "Viết switch phân loại theo ngày trong tuần",
     "Dùng <code>break</code> và fall-through (không có break)",
     "Dùng <code>default</code> khi không khớp case nào",
     "Viết lại bằng <code>match</code> (PHP 8) để so sánh",
     "Switch với nhiều case có cùng xử lý",
   ],
   [
     "<code>switch($x)</code> so sánh lỏng (==) không strict như match",
     "Thiếu <code>break</code> → fall-through: tiếp tục chạy case tiếp theo",
     "<code>match($x)</code>: strict (===), phải xử lý mọi case, trả về giá trị",
     "match ném <code>UnhandledMatchError</code> nếu không có default phù hợp",
   ],
   """\
<?php
// ── Switch theo ngày ──────────────
$thu = date('N');   // 1=Thứ Hai ... 7=Chủ Nhật

switch ($thu) {
    case 1: echo "Thứ Hai – Đầu tuần, hăng say!<br>"; break;
    case 2: echo "Thứ Ba<br>"; break;
    case 3: echo "Thứ Tư – Giữa tuần<br>"; break;
    case 4: echo "Thứ Năm<br>"; break;
    case 5: echo "Thứ Sáu – Sắp cuối tuần 🎉<br>"; break;
    case 6:
    case 7: echo "Cuối tuần – Nghỉ ngơi! 😴<br>"; break;
    default: echo "Không xác định<br>";
}

// ── Fall-through cố ý ─────────────
$quy = 2;
echo "Quý $quy gồm các tháng: ";
switch ($quy) {
    case 1: echo "1 "; // fall-through
    case 2: echo "2 ";
    case 3: echo "3 "; break;
    case 2: echo "4 "; break;  // PHP chỉ khớp case đầu tiên
}
echo "<br>";

// ── match (PHP 8) ─────────────────
$ma_loi = 404;
$thong_bao = match($ma_loi) {
    200      => "OK – Thành công",
    301, 302 => "Chuyển hướng",
    400      => "Yêu cầu sai",
    401      => "Chưa xác thực",
    403      => "Bị cấm",
    404      => "Không tìm thấy",
    500      => "Lỗi máy chủ",
    default  => "Mã lỗi không xác định",
};
echo "HTTP $ma_loi: $thong_bao<br>";"""
  ),
  (8,
   "Vòng Lặp for và while",
   "Sử dụng vòng lặp for và while để thực hiện lặp có kiểm soát số lần.",
   [
     "Vòng lặp <code>for</code> in bảng cửu chương số 7",
     "Vòng lặp <code>while</code> tính tổng 1+2+...+100",
     "Vòng lặp <code>do...while</code> ít nhất chạy 1 lần",
     "Dùng <code>break</code> và <code>continue</code>",
     "Vòng lặp lồng nhau tạo tam giác sao",
   ],
   [
     "<code>for ($i=0; $i<10; $i++)</code> — chạy khi điều kiện đúng",
     "<code>while ($dk) { ... }</code> — kiểm tra trước khi chạy",
     "<code>do { ... } while ($dk);</code> — chạy ít nhất 1 lần rồi mới kiểm tra",
     "<code>break</code>: thoát vòng lặp; <code>break 2</code>: thoát 2 lớp lồng nhau",
     "<code>continue</code>: bỏ qua lần lặp hiện tại",
   ],
   """\
<?php
// ── Bảng cửu chương 7 ─────────────
echo "<h3>Bảng cửu chương 7</h3>";
for ($i = 1; $i <= 10; $i++) {
    echo "7 × $i = " . (7 * $i) . "<br>";
}

// ── Tổng 1 đến 100 (while) ────────
$tong = 0; $i = 1;
while ($i <= 100) {
    $tong += $i;
    $i++;
}
echo "<br>Tổng 1→100 = $tong<br>";   // 5050

// ── do...while ────────────────────
$n = 1;
do {
    echo "do-while lần: $n<br>";
    $n++;
} while ($n <= 3);

// ── break và continue ─────────────
echo "<br>Số lẻ từ 1-20: ";
for ($i = 1; $i <= 20; $i++) {
    if ($i % 2 === 0) continue;   // bỏ qua số chẵn
    echo "$i ";
    if ($i >= 15) break;           // dừng ở 15
}
echo "<br>";

// ── Tam giác sao ─────────────────
echo "<pre>";
for ($dong = 1; $dong <= 6; $dong++) {
    for ($sao = 1; $sao <= $dong; $sao++) {
        echo "* ";
    }
    echo "\n";
}
echo "</pre>";"""
  ),
  (9,
   "Vòng Lặp foreach với Mảng",
   "Duyệt mảng chỉ số và mảng kết hợp bằng foreach, thực hành với mảng đa chiều.",
   [
     "Dùng <code>foreach</code> duyệt mảng in danh sách sinh viên",
     "Dùng <code>foreach ($arr as $key => $val)</code> với mảng kết hợp",
     "Xây dựng mảng 2 chiều (danh sách nhiều sinh viên) và duyệt",
     "In bảng HTML từ mảng 2 chiều",
     "Tính trung bình điểm và tìm học sinh giỏi nhất",
   ],
   [
     "<code>foreach ($arr as $val)</code> — không cần biến key",
     "<code>foreach ($arr as $k => $v)</code> — lấy cả key và value",
     "Không thay đổi được mảng gốc nếu không dùng tham chiếu <code>&$val</code>",
     "Mảng 2 chiều: mảng của các mảng <code>[['ten'=>'A','diem'=>8], ...]</code>",
   ],
   """\
<?php
// ── Mảng 1 chiều ──────────────────
$thu_do = ["Hà Nội", "Paris", "London", "Tokyo", "Seoul"];
echo "<ol>";
foreach ($thu_do as $key => $ten) {
    echo "<li>[$key] $ten</li>";
}
echo "</ol>";

// ── Mảng kết hợp ──────────────────
$sv = ["ho_ten" => "Trần Văn B", "msv" => "SV001", "diem_tb" => 8.2, "lop" => "CNTT3"];
echo "<table border='1' style='border-collapse:collapse;padding:8px'>";
foreach ($sv as $field => $value) {
    echo "<tr><th style='padding:6px 12px'>$field</th><td style='padding:6px 12px'>$value</td></tr>";
}
echo "</table><br>";

// ── Mảng 2 chiều ──────────────────
$ds_sv = [
    ["ho_ten" => "Nguyễn A", "diem_tb" => 8.5, "lop" => "K22A"],
    ["ho_ten" => "Trần B",   "diem_tb" => 7.2, "lop" => "K22B"],
    ["ho_ten" => "Lê C",     "diem_tb" => 9.1, "lop" => "K22A"],
    ["ho_ten" => "Phạm D",   "diem_tb" => 6.5, "lop" => "K22C"],
];

// In bảng HTML
echo "<table border='1' style='border-collapse:collapse;width:100%'>";
echo "<tr style='background:#667eea;color:white'><th>STT</th><th>Họ tên</th><th>Lớp</th><th>Điểm TB</th><th>Xếp loại</th></tr>";
foreach ($ds_sv as $i => $sv) {
    $xl = $sv["diem_tb"] >= 8 ? "Giỏi" : ($sv["diem_tb"] >= 6.5 ? "Khá" : "TB");
    echo "<tr><td>" . ($i+1) . "</td><td>{$sv['ho_ten']}</td><td>{$sv['lop']}</td><td>{$sv['diem_tb']}</td><td>$xl</td></tr>";
}
echo "</table><br>";

// Tìm điểm cao nhất
$diem_max = max(array_column($ds_sv, "diem_tb"));
$gv_nhat = array_filter($ds_sv, fn($sv) => $sv["diem_tb"] === $diem_max);
echo "Học sinh giỏi nhất: " . array_values($gv_nhat)[0]["ho_ten"] . " ($diem_max điểm)<br>";"""
  ),
  (10,
   "Hàm (Function) Cơ Bản",
   "Định nghĩa và gọi hàm trong PHP, truyền tham số, trả về giá trị.",
   [
     "Viết hàm tính diện tích hình chữ nhật, tam giác, hình tròn",
     "Hàm có tham số mặc định (default parameter)",
     "Hàm trả về nhiều giá trị qua mảng",
     "Hàm đệ quy (recursive) – tính giai thừa, Fibonacci",
     "Phạm vi biến (variable scope): local vs global",
   ],
   [
     "<code>function ten($tham_so) { return $ket_qua; }</code>",
     "Tham số mặc định: <code>function chao($ten = 'Bạn')</code>",
     "PHP truyền tham số theo giá trị; dùng <code>&$ref</code> để truyền tham chiếu",
     "Biến trong hàm là local; dùng <code>global $bien</code> để truy cập var ngoài",
     "Đệ quy: hàm gọi lại chính nó – cần điều kiện dừng (base case)",
   ],
   """\
<?php
// ── Hàm tính diện tích ────────────
function dien_tich_chu_nhat(float $dai, float $rong): float {
    return $dai * $rong;
}
function dien_tich_tam_giac(float $day, float $cao): float {
    return 0.5 * $day * $cao;
}
function dien_tich_hinh_tron(float $ban_kinh): float {
    return M_PI * $ban_kinh ** 2;
}
echo "Chữ nhật 5×3: "   . dien_tich_chu_nhat(5, 3) . "<br>";
echo "Tam giác 6,4: "   . dien_tich_tam_giac(6, 4) . "<br>";
echo "Hình tròn r=7: "  . round(dien_tich_hinh_tron(7), 2) . "<br>";

// ── Tham số mặc định ─────────────
function xin_chao(string $ten = "Bạn", string $loi = "Xin chào"): string {
    return "$loi, $ten!";
}
echo xin_chao() . "<br>";                  // Xin chào, Bạn!
echo xin_chao("An") . "<br>";             // Xin chào, An!
echo xin_chao("Mai", "Chào buổi sáng") . "<br>";

// ── Trả về nhiều giá trị ──────────
function thong_ke(array $arr): array {
    return [
        'min'  => min($arr),
        'max'  => max($arr),
        'tb'   => array_sum($arr) / count($arr),
        'tong' => array_sum($arr),
    ];
}
$diem = [7, 8.5, 6, 9, 7.5];
$tk = thong_ke($diem);
echo "Min: {$tk['min']} | Max: {$tk['max']} | TB: {$tk['tb']}<br>";

// ── Đệ quy: giai thừa ─────────────
function giai_thua(int $n): int {
    if ($n <= 1) return 1;           // base case
    return $n * giai_thua($n - 1);  // recursive
}
echo "5! = " . giai_thua(5) . "<br>";   // 120
echo "10! = " . giai_thua(10) . "<br>"; // 3628800

// ── Fibonacci ────────────────────
function fib(int $n): int {
    if ($n <= 1) return $n;
    return fib($n-1) + fib($n-2);
}
echo "Fibonacci 10 số đầu: ";
for ($i = 0; $i < 10; $i++) echo fib($i) . " ";
echo "<br>";"""
  ),
  (11,
   "Hàm Arrow, Closure và Callback",
   "Sử dụng hàm ẩn danh (anonymous), closure và arrow function trong PHP.",
   [
     "Gán hàm ẩn danh vào biến và gọi",
     "Dùng closure với <code>use</code> để bắt biến ngoài",
     "Arrow function <code>fn(...) =></code> (PHP 7.4+)",
     "Truyền hàm vào hàm khác (callback): <code>array_map</code>, <code>array_filter</code>, <code>usort</code>",
     "Hàm <code>array_reduce</code> với callback",
   ],
   [
     "Anonymous function: <code>$f = function($x) { return $x*2; };</code>",
     "<code>use ($bien)</code>: đưa biến ngoài vào closure; <code>use (&$bien)</code>: tham chiếu",
     "Arrow: <code>$f = fn($x) => $x * 2;</code> tự động capture biến ngoài",
     "<code>array_map($cb, $arr)</code>: áp callback lên từng phần tử, trả array mới",
     "<code>array_filter($arr, $cb)</code>: lọc phần tử thỏa điều kiện",
   ],
   """\
<?php
// ── Hàm ẩn danh ───────────────────
$boi_doi = function(int $x): int {
    return $x * 2;
};
echo $boi_doi(7) . "<br>";   // 14

// ── Closure với use ───────────────
$he_so = 3;
$nhan_he_so = function(int $x) use ($he_so): int {
    return $x * $he_so;
};
echo $nhan_he_so(5) . "<br>";   // 15

// ── Arrow function (PHP 7.4+) ──────
$binh_phuong = fn($x) => $x ** 2;
echo $binh_phuong(9) . "<br>";  // 81

// ── array_map ─────────────────────
$diem  = [5.0, 7.5, 8.0, 6.0];
$nhan3 = array_map(fn($d) => round($d * 1.1, 1), $diem);
echo implode(", ", $nhan3) . "<br>";

// ── array_filter ──────────────────
$diem_gioi = array_filter($diem, fn($d) => $d >= 7.5);
echo "Điểm giỏi: " . implode(", ", $diem_gioi) . "<br>";

// ── usort (sắp xếp tùy chỉnh) ─────
$sv = [
    ["ten" => "An",  "diem" => 8.0],
    ["ten" => "Bình","diem" => 9.2],
    ["ten" => "Cúc", "diem" => 7.5],
];
usort($sv, fn($a, $b) => $b["diem"] <=> $a["diem"]);  // giảm dần
foreach ($sv as $s) echo "{$s['ten']}: {$s['diem']}<br>";

// ── array_reduce ──────────────────
$tong = array_reduce($diem, fn($carry, $item) => $carry + $item, 0);
echo "Tổng: $tong | TB: " . ($tong / count($diem)) . "<br>";"""
  ),
  (12,
   "Include, Require và Tổ Chức File",
   "Chia nhỏ code PHP thành các file riêng biệt để dễ quản lý và tái sử dụng.",
   [
     "Tạo <code>header.php</code>, <code>footer.php</code>, <code>config.php</code>",
     "Dùng <code>include</code> và <code>require</code> để chèn file",
     "Dùng <code>include_once</code> / <code>require_once</code> để tránh include trùng",
     "Tạo file hàm dùng chung (<code>functions.php</code>)",
     "Cấu trúc dự án PHP chuẩn",
   ],
   [
     "<code>include</code>: cảnh báo (warning) nếu file không tồn tại, tiếp tục chạy",
     "<code>require</code>: lỗi nghiêm trọng (fatal error) nếu file không tồn tại, dừng",
     "<code>include_once</code> / <code>require_once</code>: chỉ include 1 lần, tránh redeclaration",
     "Đường dẫn tuyệt đối với <code>__DIR__</code>: <code>__DIR__ . '/config.php'</code>",
   ],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: config.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// <?php
// define('DB_HOST', 'localhost');
// define('DB_NAME', 'mydb');
// define('APP_NAME', 'Nền Tảng PHP');
// define('APP_URL', 'http://localhost');

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: functions.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// <?php
// function format_tien(int $so): string {
//     return number_format($so, 0, ',', '.') . ' đ';
// }
// function xuat_thong_bao(string $msg, string $loai = 'info'): void {
//     echo "<div class='alert alert-$loai'>$msg</div>";
// }

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: header.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// <?php
// require_once __DIR__ . '/config.php';
// ?>
// <!DOCTYPE html>
// <html lang="vi">
// <head>
//   <meta charset="UTF-8">
//   <title><?= APP_NAME ?></title>
// </head>
// <body>

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: index.php (trang chính)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/functions.php';

include __DIR__ . '/header.php';   // không fatal nếu thiếu

echo "<h1>" . APP_NAME . "</h1>";
echo "<p>Giá sản phẩm: " . format_tien(1_250_000) . "</p>";

require_once __DIR__ . '/footer.php';

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Cấu trúc thư mục chuẩn:
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// my-project/
// ├── index.php
// ├── config.php
// ├── functions.php
// ├── includes/
// │   ├── header.php
// │   └── footer.php
// ├── pages/
// │   ├── about.php
// │   └── contact.php
// └── assets/
//     ├── css/
//     └── js/"""
  ),
  (13,
   "Xử Lý Form HTML – Method GET",
   "Thu thập dữ liệu người dùng qua form HTML sử dụng phương thức GET.",
   [
     "Tạo form HTML với <code>method=\"GET\"</code>",
     "Đọc dữ liệu từ <code>$_GET</code> trong PHP",
     "Kiểm tra form đã submit chưa bằng <code>isset($_GET['submit'])</code>",
     "Hiển thị lại dữ liệu đã nhập trên cùng trang (sticky form)",
     "Hiểu URL query string khi dùng GET",
   ],
   [
     "<code>$_GET</code>: superglobal array chứa dữ liệu gửi qua URL (query string)",
     "GET: dữ liệu hiện trên URL → thích hợp tìm kiếm, lọc – KHÔNG dùng cho mật khẩu",
     "<code>htmlspecialchars($val)</code>: xuất giá trị an toàn, tránh XSS",
     "<code>isset($arr['key'])</code>: kiểm tra key tồn tại trong array",
     "Giới hạn GET: URL tối đa ~2000 ký tự",
   ],
   """\
<?php
// Khởi tạo biến tìm kiếm
$tu_khoa = "";
$ket_qua = [];

if (isset($_GET['tim_kiem'])) {
    // Lấy và làm sạch dữ liệu
    $tu_khoa = trim(htmlspecialchars($_GET['tu_khoa'] ?? ""));
    
    // Dữ liệu mẫu (thực tế lấy từ DB)
    $san_pham = [
        ["ten" => "Áo thun nam", "gia" => 150_000],
        ["ten" => "Quần jeans",  "gia" => 450_000],
        ["ten" => "Áo khoác",   "gia" => 800_000],
        ["ten" => "Giày thể thao","gia"=> 950_000],
        ["ten" => "Mũ lưỡi trai","gia"=> 120_000],
    ];
    
    // Tìm kiếm đơn giản
    if ($tu_khoa !== "") {
        foreach ($san_pham as $sp) {
            if (stripos($sp["ten"], $tu_khoa) !== false) {
                $ket_qua[] = $sp;
            }
        }
    } else {
        $ket_qua = $san_pham;
    }
}
?>
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="UTF-8"><title>Tìm kiếm sản phẩm</title></head>
<body>
<h2>🔍 Tìm kiếm sản phẩm</h2>

<form method="GET" action="">
  <input type="text" name="tu_khoa" placeholder="Nhập tên sản phẩm..."
         value="<?= htmlspecialchars($tu_khoa) ?>" />
  <button type="submit" name="tim_kiem">Tìm</button>
</form>

<?php if (isset($_GET['tim_kiem'])): ?>
  <p>Tìm thấy <?= count($ket_qua) ?> kết quả cho "<?= $tu_khoa ?>"</p>
  <ul>
  <?php foreach ($ket_qua as $sp): ?>
    <li><?= $sp['ten'] ?> – <?= number_format($sp['gia'], 0, ',', '.') ?>đ</li>
  <?php endforeach; ?>
  </ul>
<?php endif; ?>
</body></html>"""
  ),
  (14,
   "Xử Lý Form HTML – Method POST",
   "Thu thập và xử lý dữ liệu form bằng POST, bảo mật cơ bản và validation.",
   [
     "Tạo form đăng ký tài khoản với POST",
     "Đọc dữ liệu từ <code>$_POST</code>",
     "Validate: kiểm tra bắt buộc, độ dài, email hợp lệ",
     "Hiển thị thông báo lỗi bên cạnh mỗi field",
     "Redirect sau submit thành công (PRG pattern)",
   ],
   [
     "<code>$_POST</code>: dữ liệu ẩn trong body của request — không hiện trên URL",
     "POST an toàn hơn GET cho mật khẩu, thông tin nhạy cảm",
     "<code>filter_var($email, FILTER_VALIDATE_EMAIL)</code> kiểm tra email hợp lệ",
     "<code>header('Location: success.php')</code> + <code>exit;</code> → redirect",
     "PRG (Post/Redirect/Get) tránh trùng lặp khi F5",
   ],
   """\
<?php
$loi = [];
$du_lieu = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // ── Lấy và làm sạch ──────────
    $ho_ten  = trim($_POST['ho_ten']  ?? '');
    $email   = trim($_POST['email']   ?? '');
    $mat_khau= trim($_POST['mat_khau']?? '');
    $xac_nhan= trim($_POST['xac_nhan']?? '');
    
    // ── Validate ──────────────────
    if (empty($ho_ten))
        $loi['ho_ten'] = "Họ tên không được bỏ trống";
    elseif (mb_strlen($ho_ten) < 3)
        $loi['ho_ten'] = "Họ tên ít nhất 3 ký tự";
    
    if (empty($email))
        $loi['email'] = "Email không được bỏ trống";
    elseif (!filter_var($email, FILTER_VALIDATE_EMAIL))
        $loi['email'] = "Email không hợp lệ";
    
    if (empty($mat_khau))
        $loi['mat_khau'] = "Mật khẩu không được bỏ trống";
    elseif (strlen($mat_khau) < 8)
        $loi['mat_khau'] = "Mật khẩu ít nhất 8 ký tự";
    
    if ($xac_nhan !== $mat_khau)
        $loi['xac_nhan'] = "Mật khẩu xác nhận không khớp";
    
    // ── Xử lý nếu không lỗi ───────
    if (empty($loi)) {
        $mat_khau_hash = password_hash($mat_khau, PASSWORD_DEFAULT);
        // Lưu vào DB... (xem bài PHP & MySQL)
        echo "<p style='color:green'>✅ Đăng ký thành công! Email: $email</p>";
        // header('Location: login.php'); exit;
    }
    $du_lieu = compact('ho_ten', 'email');
}

function loi(array &$loi, string $key): string {
    return isset($loi[$key]) ? "<span style='color:red'>{$loi[$key]}</span>" : "";
}
?>
<form method="POST">
  <label>Họ tên: <input type="text" name="ho_ten" value="<?= htmlspecialchars($du_lieu['ho_ten'] ?? '') ?>"></label>
  <?= loi($loi, 'ho_ten') ?><br>
  
  <label>Email: <input type="email" name="email" value="<?= htmlspecialchars($du_lieu['email'] ?? '') ?>"></label>
  <?= loi($loi, 'email') ?><br>
  
  <label>Mật khẩu: <input type="password" name="mat_khau"></label>
  <?= loi($loi, 'mat_khau') ?><br>
  
  <label>Xác nhận: <input type="password" name="xac_nhan"></label>
  <?= loi($loi, 'xac_nhan') ?><br>
  
  <button type="submit">Đăng ký</button>
</form>"""
  ),
  (15,
   "Session – Lưu Trạng Thái Người Dùng",
   "Sử dụng session PHP để lưu thông tin người dùng giữa các trang.",
   [
     "Khởi động session với <code>session_start()</code>",
     "Lưu, đọc, xóa dữ liệu trong <code>$_SESSION</code>",
     "Xây dựng hệ thống đăng nhập đơn giản (không cần DB)",
     "Kiểm tra xem người dùng đã đăng nhập chưa",
     "Hủy session (đăng xuất) bằng <code>session_destroy()</code>",
   ],
   [
     "<code>session_start()</code>: phải gọi trước khi output bất kỳ thứ gì",
     "<code>$_SESSION['key'] = $val</code>: lưu; <code>unset($_SESSION['key'])</code>: xóa key",
     "<code>session_destroy()</code>: hủy toàn bộ session data",
     "Session ID lưu trong cookie <code>PHPSESSID</code> phía client",
     "Session data lưu trên server (mặc định là file trong /tmp)",
   ],
   """\
<?php
session_start();

// ── Đăng nhập ────────────────────
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['dang_nhap'])) {
    $email = trim($_POST['email'] ?? '');
    $matkhau = $_POST['mat_khau'] ?? '';
    
    // Tài khoản cứng (thực tế kiểm tra DB)
    $tai_khoan = [
        'admin@demo.vn' => ['mat_khau' => 'admin123', 'ten' => 'Quản trị viên', 'vai_tro' => 'admin'],
        'user@demo.vn'  => ['mat_khau' => 'user1234', 'ten' => 'Người dùng',   'vai_tro' => 'user'],
    ];
    
    if (isset($tai_khoan[$email]) && $tai_khoan[$email]['mat_khau'] === $matkhau) {
        $_SESSION['da_dang_nhap'] = true;
        $_SESSION['email']        = $email;
        $_SESSION['ten']          = $tai_khoan[$email]['ten'];
        $_SESSION['vai_tro']      = $tai_khoan[$email]['vai_tro'];
        $_SESSION['dang_nhap_luc']= date('Y-m-d H:i:s');
    } else {
        $thong_bao_loi = "Email hoặc mật khẩu không đúng!";
    }
}

// ── Đăng xuất ────────────────────
if (isset($_GET['dang_xuat'])) {
    session_unset();
    session_destroy();
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
}
?>
<?php if ($_SESSION['da_dang_nhap'] ?? false): ?>
  <h2>Xin chào, <?= htmlspecialchars($_SESSION['ten']) ?>! 👋</h2>
  <p>Email: <?= $_SESSION['email'] ?></p>
  <p>Vai trò: <?= $_SESSION['vai_tro'] ?></p>
  <p>Đăng nhập lúc: <?= $_SESSION['dang_nhap_luc'] ?></p>
  <p>Session ID: <?= session_id() ?></p>
  <a href="?dang_xuat=1">🚪 Đăng xuất</a>
<?php else: ?>
  <?php if (isset($thong_bao_loi)): ?>
    <p style="color:red"><?= $thong_bao_loi ?></p>
  <?php endif; ?>
  <form method="POST">
    <input type="email" name="email" placeholder="admin@demo.vn" required><br>
    <input type="password" name="mat_khau" placeholder="Mật khẩu" required><br>
    <button type="submit" name="dang_nhap">Đăng nhập</button>
  </form>
<?php endif; ?>"""
  ),
  (16,
   "Cookie – Lưu Dữ Liệu Phía Client",
   "Sử dụng cookie để lưu và đọc thông tin nhỏ ở phía trình duyệt người dùng.",
   [
     "Tạo cookie với <code>setcookie()</code> có thời gian hết hạn",
     "Đọc cookie từ <code>$_COOKIE</code>",
     "Xóa cookie bằng cách đặt thời gian quá khứ",
     "Lưu tùy chọn giao diện (theme) của người dùng",
     "Cookie vs Session – khi nào dùng cái nào",
   ],
   [
     "<code>setcookie($name, $value, $expire, $path, $domain, $secure, $httponly)</code>",
     "Cookie phải gọi trước <code>echo</code> hoặc output HTML",
     "Cookie lưu ở client (trình duyệt) — người dùng có thể xem và sửa",
     "Thời gian: <code>time() + 86400</code> = 1 ngày; <code>time() + 30*86400</code> = 30 ngày",
     "Dùng <code>httponly=true</code> để JavaScript không đọc được cookie",
   ],
   """\
<?php
// ── Đặt cookie ───────────────────
if (isset($_POST['luu_theme'])) {
    $theme = in_array($_POST['theme'], ['light', 'dark', 'blue']) ? $_POST['theme'] : 'light';
    setcookie('theme', $theme, time() + 30 * 86400, '/', '', false, true);
    setcookie('user_name', htmlspecialchars($_POST['ten'] ?? 'Khách'), time() + 7 * 86400, '/');
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
}

// ── Đọc cookie ───────────────────
$theme     = $_COOKIE['theme']     ?? 'light';
$user_name = $_COOKIE['user_name'] ?? 'Khách';

// ── Xóa cookie ───────────────────
if (isset($_GET['xoa_cookie'])) {
    setcookie('theme', '', time() - 3600, '/');       // đặt thời gian quá khứ
    setcookie('user_name', '', time() - 3600, '/');
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
}

// ── Hiển thị theme hiện tại ───────
$bg_colors = ['light' => '#fff', 'dark' => '#1a1a2e', 'blue' => '#ebf8ff'];
$text_colors = ['light' => '#333', 'dark' => '#eee', 'blue' => '#2c5282'];
$bg   = $bg_colors[$theme]   ?? '#fff';
$text = $text_colors[$theme] ?? '#333';
?>
<!DOCTYPE html>
<html lang="vi">
<body style="background:<?= $bg ?>;color:<?= $text ?>;padding:24px">
  <h2>Xin chào, <?= htmlspecialchars($user_name) ?>! 🍪</h2>
  <p>Theme hiện tại: <strong><?= $theme ?></strong></p>
  
  <form method="POST">
    <label>Tên: <input type="text" name="ten" value="<?= htmlspecialchars($user_name) ?>"></label><br>
    <label>Chọn theme:
      <select name="theme">
        <option value="light" <?= $theme==='light'?'selected':'' ?>>Light</option>
        <option value="dark"  <?= $theme==='dark' ?'selected':'' ?>>Dark</option>
        <option value="blue"  <?= $theme==='blue' ?'selected':'' ?>>Blue</option>
      </select>
    </label><br>
    <button type="submit" name="luu_theme">Lưu tùy chọn (30 ngày)</button>
  </form>
  <br>
  <a href="?xoa_cookie=1">🗑️ Xóa tất cả cookie</a>
  <pre style="margin-top:16px;background:#f0f0f0;padding:12px;color:#333"><?php print_r($_COOKIE); ?></pre>
</body></html>"""
  ),
  (17,
   "Xử Lý Upload File",
   "Cho phép người dùng upload hình ảnh hoặc tài liệu lên server với PHP.",
   [
     "Tạo form upload với <code>enctype=\"multipart/form-data\"</code>",
     "Đọc thông tin file từ <code>$_FILES</code>",
     "Validate: kiểm tra loại file, kích thước tối đa",
     "Di chuyển file vào thư mục lưu trữ với <code>move_uploaded_file()</code>",
     "Upload nhiều file cùng lúc",
   ],
   [
     "<code>$_FILES['input_name']</code>: array gồm name, type, size, tmp_name, error",
     "<code>move_uploaded_file($tmp, $dest)</code>: di chuyển file tạm lên vị trí cuối",
     "Đặt tên file ngẫu nhiên để tránh ghi đè: <code>uniqid() . ext</code>",
     "Kiểm tra MIME type thực tế bằng <code>finfo_file()</code> thay vì tin $_FILES['type']",
     "php.ini: <code>upload_max_filesize</code> và <code>post_max_size</code>",
   ],
   """\
<?php
$thong_bao = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $thu_muc  = __DIR__ . '/uploads/';
    $cho_phep = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
    $kich_thuoc_max = 2 * 1024 * 1024;   // 2MB

    if (!is_dir($thu_muc)) mkdir($thu_muc, 0755, true);

    $files = $_FILES['hinh_anh'];
    
    // Chuẩn hóa thành mảng (hỗ trợ upload nhiều file)
    if (!is_array($files['name'])) {
        foreach ($files as $key => $val) $files[$key] = [$val];
    }

    $so_file = count($files['name']);
    for ($i = 0; $i < $so_file; $i++) {
        if ($files['error'][$i] !== UPLOAD_ERR_OK) {
            $thong_bao[] = "❌ File {$files['name'][$i]}: lỗi upload";
            continue;
        }
        // Kiểm tra kích thước
        if ($files['size'][$i] > $kich_thuoc_max) {
            $thong_bao[] = "❌ {$files['name'][$i]}: vượt quá 2MB";
            continue;
        }
        // Kiểm tra MIME type thực tế
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime  = $finfo->file($files['tmp_name'][$i]);
        if (!in_array($mime, $cho_phep)) {
            $thong_bao[] = "❌ {$files['name'][$i]}: chỉ chấp nhận ảnh JPG/PNG/GIF/WEBP";
            continue;
        }
        // Tạo tên file an toàn
        $ext        = pathinfo($files['name'][$i], PATHINFO_EXTENSION);
        $ten_moi    = uniqid('img_') . '.' . $ext;
        $duong_dan  = $thu_muc . $ten_moi;
        if (move_uploaded_file($files['tmp_name'][$i], $duong_dan)) {
            $thong_bao[] = "✅ Upload thành công: $ten_moi (" . round($files['size'][$i]/1024) . " KB)";
        }
    }
}
?>
<form method="POST" enctype="multipart/form-data">
  <label>Chọn ảnh (tối đa 2MB, JPG/PNG/GIF):</label><br>
  <input type="file" name="hinh_anh[]" multiple accept="image/*" /><br><br>
  <button type="submit">📤 Upload</button>
</form>
<?php foreach ($thong_bao as $tb): ?>
  <p><?= $tb ?></p>
<?php endforeach; ?>"""
  ),
  (18,
   "Làm Việc Với Ngày Tháng (Date/Time)",
   "Sử dụng các hàm date/time của PHP để xử lý và định dạng ngày tháng.",
   [
     "Lấy ngày giờ hiện tại và định dạng theo ý muốn",
     "Tính khoảng cách giữa 2 ngày",
     "Tạo đối tượng <code>DateTime</code> và <code>DateInterval</code>",
     "Tính tuổi từ ngày sinh",
     "Đếm ngược đến sự kiện (event countdown)",
   ],
   [
     "<code>date('Y-m-d H:i:s')</code>: định dạng theo pattern (Y=năm, m=tháng, d=ngày...)",
     "<code>time()</code>: Unix timestamp (giây từ 1/1/1970)",
     "<code>strtotime('2025-12-31')</code>: chuyển chuỗi ngày sang timestamp",
     "<code>new DateTime('2000-05-15')</code>: đối tượng DateTime linh hoạt hơn",
     "<code>$dt1->diff($dt2)</code>: trả về DateInterval với days, months, years...",
   ],
   """\
<?php
// ── Ngày giờ hiện tại ─────────────
echo date('d/m/Y H:i:s') . "<br>";            // 08/03/2026 14:30:00
echo date('l, d F Y') . "<br>";               // Sunday, 08 March 2026
echo "Thứ " . (date('N') + 1) . "<br>";       // Thứ trong tuần (2-8, +1 cho VN)

// ── TimeZone Việt Nam ─────────────
date_default_timezone_set('Asia/Ho_Chi_Minh');
echo date('H:i:s T') . "<br>";                // giờ Việt Nam

// ── Tính tuổi ────────────────────
$ngay_sinh = new DateTime('2000-05-15');
$hom_nay   = new DateTime();
$khoang_cach = $hom_nay->diff($ngay_sinh);
echo "Tuổi: {$khoang_cach->y} tuổi {$khoang_cach->m} tháng<br>";

// ── Thêm/bớt khoảng thời gian ─────
$tet_2025 = new DateTime('2025-01-29');
$tet_2025->modify('+7 days');           // sau Tết 7 ngày
echo "Hết Tết: " . $tet_2025->format('d/m/Y') . "<br>";

// ── Đếm ngược đến sự kiện ─────────
$su_kien = new DateTime('2026-06-01 00:00:00');
$con_lai  = (new DateTime())->diff($su_kien);
if ($su_kien > new DateTime()) {
    echo "Còn {$con_lai->days} ngày đến kỳ thi tốt nghiệp 🎓<br>";
} else {
    echo "Kỳ thi đã qua!<br>";
}

// ── So sánh ngày ─────────────────
$han_nop = strtotime('2026-03-31');
$hom_nay_ts = time();
$con_bao_nhieu = ($han_nop - $hom_nay_ts) / 86400;
echo "Hạn nộp bài còn: " . (int)$con_bao_nhieu . " ngày<br>";

// ── Định dạng timestamp ───────────
$ts = mktime(8, 30, 0, 12, 25, 2025);   // giờ tùy chỉnh
echo date('d/m/Y H:i', $ts) . "<br>";   // 25/12/2025 08:30"""
  ),
  (19,
   "Đọc/Ghi File (File I/O)",
   "Thao tác với hệ thống file: đọc, ghi, thêm nội dung và quản lý file/thư mục.",
   [
     "Ghi nội dung vào file với <code>file_put_contents()</code>",
     "Đọc file với <code>file_get_contents()</code> và <code>file()</code>",
     "Thêm nội dung vào cuối file (append)",
     "Kiểm tra file tồn tại, kích thước, loại file",
     "Tạo, xóa, liệt kê thư mục",
   ],
   [
     "<code>file_put_contents($path, $data)</code>: ghi (ghi đè); <code>FILE_APPEND</code>: thêm cuối",
     "<code>file_get_contents($path)</code>: đọc toàn bộ thành chuỗi",
     "<code>file($path)</code>: đọc thành mảng từng dòng",
     "<code>file_exists()</code>, <code>is_file()</code>, <code>is_dir()</code>, <code>filesize()</code>",
     "<code>mkdir($path, 0755, true)</code>: tạo thư mục (recursive); <code>rmdir()</code>: xóa rỗng",
   ],
   """\
<?php
$file_nhat_ky = __DIR__ . '/nhat_ky.txt';
$file_json    = __DIR__ . '/du_lieu.json';

// ── Ghi file ─────────────────────
$noi_dung = "=== Nhật ký ngày " . date('d/m/Y') . " ===\\n";
$noi_dung .= "Đã hoàn thành bài tập PHP File I/O\\n";
$noi_dung .= "Thời gian: " . date('H:i:s') . "\\n\\n";

file_put_contents($file_nhat_ky, $noi_dung);                    // ghi đè
file_put_contents($file_nhat_ky, "Dòng mới thêm\\n", FILE_APPEND); // thêm cuối

echo "✅ Đã ghi file<br>";

// ── Đọc file ─────────────────────
if (file_exists($file_nhat_ky)) {
    $noi_dung_doc = file_get_contents($file_nhat_ky);
    echo "<pre>" . htmlspecialchars($noi_dung_doc) . "</pre>";
    
    $cac_dong = file($file_nhat_ky, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    echo count($cac_dong) . " dòng<br>";
}

// ── JSON file ─────────────────────
$du_lieu = [
    ['id' => 1, 'ten' => 'Sản phẩm A', 'gia' => 150000],
    ['id' => 2, 'ten' => 'Sản phẩm B', 'gia' => 300000],
];
file_put_contents($file_json, json_encode($du_lieu, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));

$doc_json = json_decode(file_get_contents($file_json), true);
foreach ($doc_json as $sp) {
    echo "{$sp['ten']}: " . number_format($sp['gia'], 0, ',', '.') . "đ<br>";
}

// ── Thông tin file ────────────────
echo "<hr>";
echo "Kích thước: " . filesize($file_nhat_ky) . " bytes<br>";
echo "Lần sửa cuối: " . date('d/m/Y H:i', filemtime($file_nhat_ky)) . "<br>";

// ── Liệt kê file trong thư mục ───
$files = glob(__DIR__ . '/*.txt');
echo "File .txt: " . count($files) . "<br>";
foreach ($files as $f) echo basename($f) . "<br>";"""
  ),
  (20,
   "JSON Trong PHP",
   "Mã hóa và giải mã JSON để trao đổi dữ liệu giữa PHP và JavaScript hoặc API.",
   [
     "Chuyển mảng PHP sang JSON bằng <code>json_encode()</code>",
     "Chuyển JSON sang mảng/object bằng <code>json_decode()</code>",
     "Tạo REST API JSON đơn giản",
     "Đọc JSON từ API ngoài bằng <code>file_get_contents()</code>",
     "Xử lý JSON lồng nhau (nested)",
   ],
   [
     "<code>json_encode($arr, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT)</code>",
     "<code>json_decode($json, true)</code>: true → mảng; false → object stdClass",
     "<code>header('Content-Type: application/json')</code>: khai báo API trả về JSON",
     "<code>json_last_error()</code>: kiểm tra lỗi parse JSON",
     "Hằng số hữu ích: <code>JSON_UNESCAPED_UNICODE</code>, <code>JSON_PRETTY_PRINT</code>, <code>JSON_HEX_TAG</code>",
   ],
   """\
<?php
// ── json_encode ───────────────────
$san_pham = [
    ['id' => 1, 'ten' => 'Áo thun', 'gia' => 150_000, 'ton_kho' => true],
    ['id' => 2, 'ten' => 'Quần jean', 'gia' => 450_000, 'ton_kho' => false],
    ['id' => 3, 'ten' => 'Giày thể thao', 'gia' => 850_000, 'ton_kho' => true],
];

$json = json_encode($san_pham, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
echo "<pre>" . $json . "</pre>";

// ── json_decode ───────────────────
$json_raw = '[{"id":10,"ten":"iPhone 15","gia":22990000},{"id":11,"ten":"Samsung S24","gia":19990000}]';
$phones = json_decode($json_raw, true);   // true = assoc array
foreach ($phones as $p) {
    echo "{$p['ten']}: " . number_format($p['gia'], 0, ',', '.') . "đ<br>";
}

// ── API endpoint giả lập ──────────
if (isset($_GET['api']) && $_GET['api'] === 'products') {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'status'  => 'success',
        'total'   => count($san_pham),
        'data'    => $san_pham,
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

// ── JSON lồng nhau ─────────────────
$don_hang = [
    'ma_don'     => 'ORD-2026-001',
    'ngay'       => date('Y-m-d'),
    'khach_hang' => ['ten' => 'Nguyễn A', 'email' => 'a@demo.vn'],
    'san_pham'   => $san_pham,
    'tong_tien'  => array_sum(array_column($san_pham, 'gia')),
];
$json_don_hang = json_encode($don_hang, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
echo "<pre>" . htmlspecialchars($json_don_hang) . "</pre>";

// Truy cập nested
$obj = json_decode($json_don_hang);
echo "Email khách: " . $obj->khach_hang->email . "<br>";"""
  ),
  (21,
   "Xử Lý Lỗi và Exception",
   "Bắt và xử lý lỗi trong PHP bằng try/catch/finally và custom exception.",
   [
     "Dùng <code>try { } catch (Exception $e) { }</code>",
     "Tạo custom Exception class",
     "Dùng <code>finally</code>",
     "Chuyển lỗi PHP thành Exception qua <code>set_error_handler</code>",
     "Logging lỗi vào file",
   ],
   [
     "<code>throw new Exception('msg')</code>: ném ngoại lệ",
     "<code>$e->getMessage()</code>, <code>$e->getCode()</code>, <code>$e->getFile()</code>, <code>$e->getLine()</code>",
     "<code>finally { }</code>: luôn chạy dù có exception hay không (ví dụ: đóng DB)",
     "Custom exception: <code>class ValidationException extends Exception { }</code>",
     "<code>error_log($msg, 3, 'errors.log')</code>: ghi log lỗi",
   ],
   """\
<?php
// ── Custom Exception ──────────────
class ValidationException extends RuntimeException {
    private array $errors;
    public function __construct(array $errors, string $msg = "Validation thất bại") {
        parent::__construct($msg, 422);
        $this->errors = $errors;
    }
    public function getErrors(): array { return $this->errors; }
}

class NotFoundException extends RuntimeException {
    public function __construct(string $resource) {
        parent::__construct("Không tìm thấy: $resource", 404);
    }
}

// ── Hàm có thể throw exception ────
function lay_san_pham(int $id): array {
    $db = [1 => ['ten' => 'Áo thun', 'gia' => 150000], 2 => ['ten' => 'Quần jean', 'gia' => 450000]];
    if (!isset($db[$id])) throw new NotFoundException("Sản phẩm #$id");
    return $db[$id];
}

function tao_don_hang(array $data): array {
    $loi = [];
    if (empty($data['ten_khach'])) $loi[] = "Tên khách hàng bắt buộc";
    if (empty($data['email']) || !filter_var($data['email'], FILTER_VALIDATE_EMAIL))
        $loi[] = "Email không hợp lệ";
    if (($data['so_luong'] ?? 0) <= 0) $loi[] = "Số lượng phải > 0";
    if (!empty($loi)) throw new ValidationException($loi);
    return ['ma_don' => 'ORD-' . uniqid(), 'trang_thai' => 'created'];
}

// ── Bắt exception ─────────────────
try {
    $sp = lay_san_pham(99);   // không tồn tại
} catch (NotFoundException $e) {
    echo "Lỗi {$e->getCode()}: {$e->getMessage()}<br>";
} finally {
    echo "Luôn chạy (dọn dẹp tài nguyên)<br>";
}

try {
    $don = tao_don_hang(['ten_khach' => '', 'email' => 'sai', 'so_luong' => -1]);
} catch (ValidationException $e) {
    echo "<strong>{$e->getMessage()}</strong><ul>";
    foreach ($e->getErrors() as $err) echo "<li>$err</li>";
    echo "</ul>";
} catch (Exception $e) {
    echo "Lỗi khác: " . $e->getMessage();
    error_log($e->getMessage() . " tại " . $e->getFile() . ":" . $e->getLine());
}"""
  ),
  (22,
   "Hàm Mảng Nâng Cao",
   "Thành thạo các hàm xử lý mảng mạnh mẽ của PHP để xử lý dữ liệu hiệu quả.",
   [
     "<code>array_map</code>, <code>array_filter</code>, <code>array_reduce</code>",
     "<code>array_unique</code>, <code>array_flip</code>, <code>array_combine</code>",
     "<code>array_slice</code>, <code>array_splice</code>, <code>array_chunk</code>",
     "<code>array_column</code>, <code>usort</code>, <code>array_multisort</code>",
     "Spread operator và unpacking mảng",
   ],
   [
     "<code>array_column($arr, 'key')</code>: lấy một cột từ mảng 2 chiều",
     "<code>array_chunk($arr, $n)</code>: chia mảng thành các chunk n phần tử",
     "<code>array_unique($arr)</code>: xóa phần tử trùng lặp",
     "<code>array_flip($arr)</code>: đổi key ↔ value",
     "<code>array_combine($keys, $values)</code>: tạo mảng từ 2 mảng key và value",
   ],
   """\
<?php
$sinh_vien = [
    ['ten' => 'An',   'diem' => 8.5, 'lop' => 'A', 'tuoi' => 20],
    ['ten' => 'Bình', 'diem' => 7.0, 'lop' => 'B', 'tuoi' => 21],
    ['ten' => 'Cúc',  'diem' => 9.2, 'lop' => 'A', 'tuoi' => 19],
    ['ten' => 'Dũng', 'diem' => 5.5, 'lop' => 'C', 'tuoi' => 22],
    ['ten' => 'Ema',  'diem' => 8.0, 'lop' => 'B', 'tuoi' => 20],
];

// ── array_column ──────────────────
$ten_sv = array_column($sinh_vien, 'ten');    // ['An','Bình','Cúc','Dũng','Ema']
$diem   = array_column($sinh_vien, 'diem');   // [8.5,7.0,9.2,5.5,8.0]
echo "Trung bình: " . round(array_sum($diem)/count($diem), 2) . "<br>";

// ── array_filter ──────────────────
$sv_gioi = array_filter($sinh_vien, fn($sv) => $sv['diem'] >= 8.0);
echo "Sinh viên giỏi: " . implode(', ', array_column($sv_gioi, 'ten')) . "<br>";

// ── usort (sắp xếp tùy chỉnh) ─────
usort($sinh_vien, fn($a, $b) => $b['diem'] <=> $a['diem']);  // giảm dần theo điểm
echo "Top 1: {$sinh_vien[0]['ten']} ({$sinh_vien[0]['diem']})<br>";

// ── array_chunk (phân trang) ───────
$trang_size = 2;
$pages = array_chunk($sinh_vien, $trang_size);
echo "Số trang: " . count($pages) . "<br>";
echo "Trang 1: " . implode(', ', array_column($pages[0], 'ten')) . "<br>";

// ── array_combine ──────────────────
$ky_hieu  = ['A', 'B', 'C'];
$mon_hoc  = ['Toán', 'Văn', 'Anh'];
$lu_chon  = array_combine($ky_hieu, $mon_hoc);
echo $lu_chon['B'] . "<br>";   // Văn

// ── array_unique ──────────────────
$lop_list = array_column($sinh_vien, 'lop');
$lop_uniq = array_unique($lop_list);
sort($lop_uniq);
echo "Các lớp: " . implode(', ', $lop_uniq) . "<br>";

// ── array_map ─────────────────────
$nhan_10  = array_map(fn($sv) => [...$sv, 'diem_x10' => $sv['diem']*10], $sinh_vien);
echo "Điểm×10: " . implode(', ', array_column($nhan_10, 'diem_x10')) . "<br>";"""
  ),
  (23,
   "Regular Expressions (Regex)",
   "Sử dụng biểu thức chính quy (regex) trong PHP để tìm kiếm và xử lý chuỗi phức tạp.",
   [
     "Dùng <code>preg_match()</code> để kiểm tra pattern",
     "Dùng <code>preg_match_all()</code> tìm tất cả khớp",
     "Dùng <code>preg_replace()</code> để thay thế theo pattern",
     "Validate số điện thoại VN, mã bưu điện, CCCD",
     "Tách và phân tích chuỗi phức tạp",
   ],
   [
     "<code>preg_match('/pattern/', $str)</code>: trả về 1 nếu khớp, 0 nếu không",
     "<code>preg_match('/pattern/', $str, $matches)</code>: lưu kết quả vào $matches",
     "<code>preg_replace('/p/', 'replace', $str)</code>: thay thế theo regex",
     "Modifier: <code>i</code>=case-insensitive, <code>m</code>=multiline, <code>u</code>=UTF-8",
     "Groups <code>(...)</code> bắt giá trị; <code>(?:...)</code> non-capturing group",
   ],
   """\
<?php
// ── Validate email ────────────────
$emails = ['user@example.com', 'invalid-email', 'test.user+tag@sub.domain.vn', '@nodomain'];
foreach ($emails as $e) {
    $ok = preg_match('/^[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,}$/', $e);
    echo "$e: " . ($ok ? "✅ hợp lệ" : "❌ không hợp lệ") . "<br>";
}

// ── Số điện thoại Việt Nam ────────
$so_dt = ['0912345678', '0385 123 456', '+84987654321', '09123', '01234567890'];
$pattern_dt = '/^(\\+84|0)(3[2-9]|5[6-9]|7[0-9]|8[0-9]|9[0-9])\\d{7}$/';
foreach ($so_dt as $s) {
    $sach = preg_replace('/[\\s\\-.]/', '', $s);  // xóa khoảng trắng và dấu
    echo "$s → " . (preg_match($pattern_dt, $sach) ? "✅" : "❌") . "<br>";
}

// ── Trích xuất thông tin ──────────
$van_ban = "Liên hệ: 0901234567 hoặc 0987654321 hoặc email@test.vn";
preg_match_all('/(0[3-9]\\d{8})/', $van_ban, $so_dts);
echo "Số điện thoại tìm thấy: " . implode(', ', $so_dts[1]) . "<br>";

// ── Tách URL ──────────────────────
$url = 'https://shop.example.vn/san-pham/ao-thun?color=do&size=L#reviews';
$pattern_url = '/^(https?):\/\/([^\/]+)(\/[^?#]*)?(\?[^#]*)?(#.*)?$/';
if (preg_match($pattern_url, $url, $m)) {
    echo "Protocol: {$m[1]}<br>";
    echo "Domain: {$m[2]}<br>";
    echo "Path: {$m[3]}<br>";
    echo "Query: {$m[4]}<br>";
}

// ── preg_replace nâng cao ─────────
$text = "Giá: 1500000 đồng, giảm 200000 đồng";
$result = preg_replace_callback('/\\d+/', function($m) {
    return number_format($m[0], 0, ',', '.');
}, $text);
echo $result . "<br>";   // Giá: 1.500.000 đồng, giảm 200.000 đồng"""
  ),
  (24,
   "Namespace và Autoloading",
   "Tổ chức code PHP theo namespace và tự động nạp class với autoloading.",
   [
     "Khai báo namespace trong class",
     "Dùng <code>use</code> để import class từ namespace khác",
     "Tạo autoloader đơn giản với <code>spl_autoload_register</code>",
     "Hiểu chuẩn PSR-4 autoloading",
     "Tạo cấu trúc dự án với multiple namespace",
   ],
   [
     "<code>namespace App\\Models;</code>: khai báo ở đầu file (sau <?php)",
     "<code>use App\\Models\\User;</code>: import để dùng không cần ghi đầy đủ",
     "PSR-4: namespace ánh xạ 1-1 với cấu trúc thư mục",
     "<code>spl_autoload_register(fn($class) => require str_replace('\\\\','/',$class).'.php')</code>",
     "Composer autoload: khai báo trong <code>composer.json</code> → chạy <code>composer dump-autoload</code>",
   ],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: src/Models/User.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// namespace App\\Models;
// class User {
//     public function __construct(
//         public readonly string $name,
//         public readonly string $email,
//         public readonly int    $age
//     ) {}
//     public function isAdult(): bool { return $this->age >= 18; }
//     public function toArray(): array {
//         return ['name'=>$this->name,'email'=>$this->email,'age'=>$this->age];
//     }
// }

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: src/Services/UserService.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// namespace App\\Services;
// use App\\Models\\User;
// class UserService {
//     private array $users = [];
//     public function create(string $name, string $email, int $age): User {
//         $user = new User($name, $email, $age);
//         $this->users[] = $user;
//         return $user;
//     }
//     public function getAll(): array { return $this->users; }
//     public function getAdults(): array {
//         return array_filter($this->users, fn(User $u) => $u->isAdult());
//     }
// }

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File: index.php (entry point)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Autoloader đơn giản (PSR-4)
spl_autoload_register(function(string $class): void {
    $file = __DIR__ . '/src/' . str_replace(['App\\\\', '\\\\'], ['', '/'], $class) . '.php';
    if (file_exists($file)) require_once $file;
});

// Dùng class qua namespace
// use App\\Services\\UserService;
// $svc = new UserService();
// $svc->create('Nguyễn An', 'an@demo.vn', 22);
// $svc->create('Trần B', 'b@demo.vn', 16);
// foreach ($svc->getAdults() as $u) {
//     echo "{$u->name} ({$u->age} tuổi)<br>";
// }

// ── composer.json ─────────────────
// {
//   "autoload": {
//     "psr-4": { "App\\\\": "src/" }
//   }
// }
// Sau đó chạy: composer dump-autoload
// Và trong code: require 'vendor/autoload.php';

echo "Namespace giúp tránh đụng tên class và tổ chức code sạch hơn!";"""
  ),
  (25,
   "Type Declarations và PHP 8 Features",
   "Sử dụng khai báo kiểu (type hints) và các tính năng mới PHP 8 để viết code an toàn.",
   [
     "Khai báo kiểu tham số và giá trị trả về",
     "Union types (<code>int|string</code>), Nullable (<code>?int</code>), <code>mixed</code>",
     "Named arguments (PHP 8.0)",
     "Fibers (PHP 8.1)",
     "Readonly properties (PHP 8.1), Enums (PHP 8.1)",
   ],
   [
     "<code>function add(int $a, int $b): int</code> — khai báo kiểu đầy đủ",
     "<code>?string</code> = <code>string|null</code>; <code>void</code>: hàm không return",
     "Named args: <code>setcookie(name: 'theme', value: 'dark', httponly: true)</code>",
     "<code>enum Status { Active; Inactive; }</code> — type-safe constants",
     "<code>readonly</code>: thuộc tính chỉ gán 1 lần trong constructor",
   ],
   """\
<?php
declare(strict_types=1);  // bật strict mode – ép kiểu chính xác

// ── Union types & Nullable ─────────
function dinh_dang_id(int|string $id): string {
    return is_int($id) ? "ID-{$id}" : strtoupper($id);
}
echo dinh_dang_id(42)   . "<br>";   // ID-42
echo dinh_dang_id('abc') . "<br>";  // ABC

function tim_user(?int $id): ?array {
    if ($id === null) return null;
    $db = [1 => ['ten' => 'An'], 2 => ['ten' => 'Bình']];
    return $db[$id] ?? null;
}
$u = tim_user(1);
echo ($u ? $u['ten'] : 'Không tìm thấy') . "<br>";

// ── Enum (PHP 8.1) ────────────────
// enum TrangThai: string {
//     case Cho       = 'pending';
//     case DangXu    = 'processing';
//     case HoanThanh = 'completed';
//     case HuyBo     = 'cancelled';
//     public function nhan(): string {
//         return match($this) {
//             self::Cho       => '⏳ Chờ',
//             self::DangXu    => '🔄 Đang xử lý',
//             self::HoanThanh => '✅ Hoàn thành',
//             self::HuyBo     => '❌ Hủy',
//         };
//     }
// }
// $ts = TrangThai::HoanThanh;
// echo $ts->value . ": " . $ts->nhan() . "<br>";

// ── Readonly properties (PHP 8.1) ──
class DonHang {
    public function __construct(
        public readonly string $ma_don,
        public readonly string $ngay_tao,
        public float $tong_tien = 0.0,
    ) {}
}
$don = new DonHang(ma_don: 'ORD-001', ngay_tao: date('Y-m-d'));
$don->tong_tien = 500_000;    // OK – không readonly
// $don->ma_don = 'XXX';     // Error – là readonly
echo "Đơn {$don->ma_don} ngày {$don->ngay_tao}: " . number_format($don->tong_tien) . "đ<br>";

// ── Named arguments ────────────────
function tao_the_html(
    string $tag,
    string $noi_dung,
    string $class = '',
    string $id    = '',
): string {
    $attr  = $class ? " class=\"$class\"" : '';
    $attr .= $id    ? " id=\"$id\""       : '';
    return "<$tag$attr>$noi_dung</$tag>";
}
echo tao_the_html(tag: 'h2', noi_dung: 'Tiêu đề', class: 'title') . "<br>";
echo tao_the_html(noi_dung: 'Đoạn văn', tag: 'p', id: 'intro')    . "<br>";"""
  ),
]

SHIKI_SCRIPT = """\
  <script type="module">
    import { codeToHtml } from 'https://esm.sh/shiki@1';
    const raw = document.getElementById('code-raw').textContent;
    const highlighted = await codeToHtml(raw, { lang: 'php', theme: 'github-dark' });
    document.getElementById('code-highlight').innerHTML = highlighted;
    const pre = document.getElementById('code-highlight').querySelector('pre');
    if (pre) pre.style.cssText = 'border-radius:10px;padding:20px;font-size:0.87rem;overflow-x:auto;margin:0;line-height:1.7';
  </script>"""

def build(n, title, short, reqs, knows, code):
    reqs_li  = "\n".join(f"          <li>{r}</li>" for r in reqs)
    knows_li = "\n".join(f"          <li>{k}</li>" for k in knows)
    code_esc = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    url_slug = f"bai-{n:02d}"
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="keywords" content="PHP,Lập trình PHP,Web,NenTang,Bài tập PHP,PHP cơ bản">
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
  <div class="page-header module-php-1">
    <div class="breadcrumb">
      <a href="../../index.html">PHP Course</a> &rsaquo;
      <a href="../index.html">Module 1</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 1 – PHP Cơ Bản</p>
  </div>

  <div class="exercise-page">
    <div class="exercise-box">
      <div class="ex-head">
        <h1>📝 Yêu cầu bài tập</h1>
        <p>{short}</p>
      </div>
      <div class="ex-desc">
        <h3>Yêu cầu</h3>
        <ul>
{reqs_li}
        </ul>
        <h3>🧠 Kiến thức cần nhớ</h3>
        <ul>
{knows_li}
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
  <a href="../index.html" class="btn-back">&#8592; Quay lại Module 1</a>
{SHIKI_SCRIPT}
</body>
</html>"""

created = 0
for ex in EXERCISES:
    n, title, short, reqs, knows, code = ex
    folder = MOD / f"bai-{n:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    html = build(n, title, short, reqs, knows, code)
    (folder / "index.html").write_text(html, encoding="utf-8")
    print(f"  ✓ bai-{n:02d}: {title}")
    created += 1

print(f"\n✅ Module 1 PHP: {created} bài tạo thành công tại {MOD}")
