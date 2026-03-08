# gen_php3.py – Module 3: PHP & MySQL Thực Chiến (15 bài)
import pathlib

ROOT = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-php")
MOD  = ROOT / "module-03-php-mysql"
MOD.mkdir(parents=True, exist_ok=True)

EXERCISES = [
  (1, "Thiết Kế Database và Kết Nối PDO",
   "Thiết kế schema database chuẩn và kết nối với PHP PDO.",
   ["Thiết kế ERD cho hệ thống bán hàng đơn giản",
    "Tạo database và tables với SQL",
    "Kết nối PDO an toàn với config riêng",
    "Định nghĩa constants DB trong file cấu hình",
    "Test kết nối và hiển thị version MySQL"],
   ["<code>CREATE DATABASE IF NOT EXISTS</code> rồi <code>USE dbname</code>",
    "ERD: Entity Relationship Diagram – vẽ sơ đồ bảng và quan hệ",
    "Tách config DB ra file riêng (<code>config/database.php</code>)",
    "<code>PDO::ATTR_EMULATE_PREPARES => false</code>: dùng native prepared statements",
    "Charset UTF8MB4: hỗ trợ tiếng Việt và emoji đầy đủ"],
   """\
<?php
// config/database.php
define('DB_HOST', 'localhost');
define('DB_NAME', 'shop_db');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_CHARSET', 'utf8mb4');

function get_pdo(): PDO {
    static $pdo = null;
    if ($pdo !== null) return $pdo;  // Singleton connection
    $dsn = sprintf('mysql:host=%s;dbname=%s;charset=%s', DB_HOST, DB_NAME, DB_CHARSET);
    $pdo = new PDO($dsn, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ]);
    return $pdo;
}

// ── Tạo schema ────────────────────
$sql_schema = "
CREATE DATABASE IF NOT EXISTS shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE shop_db;

CREATE TABLE IF NOT EXISTS danh_muc (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ten         VARCHAR(100) NOT NULL,
    slug        VARCHAR(100) UNIQUE,
    mo_ta       TEXT,
    thu_tu      INT DEFAULT 0,
    active      TINYINT(1) DEFAULT 1,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS san_pham (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    danh_muc_id INT,
    ten         VARCHAR(200) NOT NULL,
    slug        VARCHAR(200) UNIQUE,
    gia         DECIMAL(15,2) NOT NULL DEFAULT 0,
    gia_km      DECIMAL(15,2) DEFAULT NULL,
    anh         VARCHAR(255),
    mo_ta       TEXT,
    so_luong    INT DEFAULT 0,
    luot_xem    INT DEFAULT 0,
    active      TINYINT(1) DEFAULT 1,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (danh_muc_id) REFERENCES danh_muc(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS khach_hang (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten      VARCHAR(100) NOT NULL,
    email       VARCHAR(150) UNIQUE NOT NULL,
    dien_thoai  VARCHAR(20),
    dia_chi     TEXT,
    mat_khau    VARCHAR(255),
    role        ENUM('user','admin') DEFAULT 'user',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
";

// Chạy schema
try {
    $pdo = new PDO('mysql:host=' . DB_HOST, DB_USER, DB_PASS);
    foreach (explode(';', $sql_schema) as $stmt) {
        $stmt = trim($stmt);
        if ($stmt) $pdo->exec($stmt);
    }
    echo "✅ Schema tạo thành công!<br>";
} catch (PDOException $e) {
    echo "❌ Lỗi: " . $e->getMessage() . "<br>";
}

// Kiểm tra kết nối
$pdo2 = get_pdo();
$ver   = $pdo2->query("SELECT VERSION() as ver")->fetchColumn();
$db    = $pdo2->query("SELECT DATABASE() as db")->fetchColumn();
echo "MySQL: $ver | Database: $db<br>";"""
  ),
  (2, "INSERT – Thêm Dữ Liệu Hàng Loạt",
   "Thêm dữ liệu mẫu vào database bằng INSERT đơn lẻ và bulk insert.",
   ["INSERT một bản ghi với prepared statement",
    "Bulk INSERT nhiều records trong 1 query",
    "<code>ON DUPLICATE KEY UPDATE</code> – upsert",
    "Transaction để INSERT an toàn",
    "Dùng <code>lastInsertId()</code> lấy ID vừa tạo"],
   ["Bulk INSERT: <code>INSERT INTO t VALUES (?,?,?),(?,?,?)</code> – nhanh hơn nhiều vòng lặp",
    "<code>ON DUPLICATE KEY UPDATE</code>: nếu duplicate key thì UPDATE thay vì báo lỗi",
    "<code>INSERT IGNORE INTO</code>: bỏ qua nếu duplicate",
    "Prepared statement với batch: bind array, execute nhiều lần",
    "LAST_INSERT_ID(): hàm MySQL lấy ID cuối insert"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. INSERT đơn lẻ
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$stmt = $pdo->prepare("INSERT INTO danh_muc (ten, slug, mo_ta, thu_tu) VALUES (:ten, :slug, :mo_ta, :thu_tu)");
$danh_muc_data = [
    ['ten'=>'Thời trang nam',  'slug'=>'thoi-trang-nam',  'mo_ta'=>'Quần áo, giày dép nam', 'thu_tu'=>1],
    ['ten'=>'Thời trang nữ',   'slug'=>'thoi-trang-nu',   'mo_ta'=>'Quần áo, giày dép nữ', 'thu_tu'=>2],
    ['ten'=>'Điện tử',         'slug'=>'dien-tu',          'mo_ta'=>'Điện thoại, laptop...',  'thu_tu'=>3],
    ['ten'=>'Thực phẩm',       'slug'=>'thuc-pham',        'mo_ta'=>'Đồ ăn, thức uống',       'thu_tu'=>4],
];
foreach ($danh_muc_data as $dm) {
    $stmt->execute($dm);
    echo "Thêm danh mục #{$pdo->lastInsertId()}: {$dm['ten']}<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. Bulk INSERT (nhanh hơn)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$san_pham = [
    [1, 'Áo thun Polo',      'ao-thun-polo',  150_000, 135_000, 50],
    [1, 'Quần Jogger',       'quan-jogger',   350_000, null,    30],
    [3, 'iPhone 15 Pro',     'iphone-15-pro', 29_990_000, 27_990_000, 10],
    [3, 'Samsung Galaxy S24','samsung-s24',   22_000_000, null, 15],
    [4, 'Cafe Arabica 500g', 'cafe-arabica',  180_000, 150_000, 100],
    [4, 'Trà Olong túi lọc', 'tra-olong',     45_000,  null,    200],
    [2, 'Đầm Maxi Hoa',      'dam-maxi-hoa',  280_000, 220_000,  40],
    [2, 'Túi xách da',       'tui-xach-da',   450_000, null,     25],
];

// Build multi-row placeholders
$rows  = implode(',', array_fill(0, count($san_pham), '(?,?,?,?,?,?)'));
$vals  = array_merge(...array_map(fn($sp) => $sp, $san_pham));
$pdo->prepare("INSERT INTO san_pham (danh_muc_id, ten, slug, gia, gia_km, so_luong) VALUES $rows")->execute($vals);
echo "Bulk insert: " . count($san_pham) . " sản phẩm<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. UPSERT – ON DUPLICATE KEY UPDATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$upsert = $pdo->prepare("
    INSERT INTO danh_muc (ten, slug, thu_tu)
    VALUES (:ten, :slug, :thu_tu)
    ON DUPLICATE KEY UPDATE ten = VALUES(ten), thu_tu = VALUES(thu_tu)
");
$upsert->execute(['ten'=>'Thời trang nam (cập nhật)', 'slug'=>'thoi-trang-nam', 'thu_tu'=>10]);
echo "Upsert: " . $upsert->rowCount() . " hàng bị ảnh hưởng<br>";

// Kiểm tra
$total_sp = $pdo->query("SELECT COUNT(*) FROM san_pham")->fetchColumn();
$total_dm = $pdo->query("SELECT COUNT(*) FROM danh_muc")->fetchColumn();
echo "Tổng: $total_dm danh mục, $total_sp sản phẩm<br>";"""
  ),
  (3, "SELECT – Truy Vấn và Lọc Dữ Liệu",
   "Thực hiện SELECT với WHERE, ORDER BY, LIMIT, và các điều kiện lọc phức tạp.",
   ["SELECT đơn giản và với điều kiện WHERE",
    "Lọc theo khoảng giá, từ khóa tìm kiếm",
    "ORDER BY nhiều cột, LIMIT và OFFSET cho phân trang",
    "Các hàm tổng hợp: COUNT, SUM, AVG, MIN, MAX",
    "DISTINCT và GROUP BY"],
   ["<code>WHERE col BETWEEN 100 AND 500</code>: lọc trong khoảng",
    "<code>ORDER BY col1 ASC, col2 DESC</code>: sắp xếp nhiều cột",
    "<code>LIMIT 10 OFFSET 20</code>: lấy 10 hàng bắt đầu từ hàng 21 (trang 3)",
    "<code>COUNT(*)</code>: đếm tất cả; <code>COUNT(col)</code>: bỏ qua NULL",
    "<code>GROUP BY col HAVING COUNT(*) > 1</code>: nhóm và lọc nhóm"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. SELECT tất cả sản phẩm hoạt động
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ds = $pdo->query("SELECT ten, gia, so_luong FROM san_pham WHERE active = 1 ORDER BY ten ASC")->fetchAll();
echo "Tổng sản phẩm active: " . count($ds) . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. Lọc theo khoảng giá
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$stmt = $pdo->prepare("SELECT ten, gia FROM san_pham WHERE gia BETWEEN ? AND ? ORDER BY gia");
$stmt->execute([100_000, 500_000]);
echo "<br>Sản phẩm 100k-500k:<br>";
foreach ($stmt->fetchAll() as $sp) {
    echo "→ {$sp['ten']}: " . number_format($sp['gia'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. Tìm kiếm full-text đơn giản
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$kw = 'iphone';
$tm = $pdo->prepare("SELECT id, ten, gia FROM san_pham WHERE ten LIKE ? OR mo_ta LIKE ? LIMIT 10");
$tm->execute(["%$kw%", "%$kw%"]);
$ket_qua = $tm->fetchAll();
echo "<br>Tìm '$kw': " . count($ket_qua) . " kết quả<br>";
foreach ($ket_qua as $sp) echo "→ {$sp['ten']}<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. Phân trang (LIMIT + OFFSET)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$trang    = (int)($_GET['trang'] ?? 1);
$per_page = 3;
$offset   = ($trang - 1) * $per_page;
$total    = $pdo->query("SELECT COUNT(*) FROM san_pham WHERE active = 1")->fetchColumn();
$tong_trang = ceil($total / $per_page);

$page_data = $pdo->prepare("SELECT ten, gia FROM san_pham WHERE active=1 ORDER BY id LIMIT ? OFFSET ?");
$page_data->execute([$per_page, $offset]);
echo "<br>Trang $trang/$tong_trang (tổng $total sản phẩm):<br>";
foreach ($page_data->fetchAll() as $sp) echo "• {$sp['ten']}<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 5. Aggregate functions
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$agg = $pdo->query("
    SELECT
        COUNT(*) AS tong_sp,
        AVG(gia)  AS gia_tb,
        MIN(gia)  AS gia_thap_nhat,
        MAX(gia)  AS gia_cao_nhat,
        SUM(so_luong * gia) AS gia_tri_ton_kho
    FROM san_pham WHERE active = 1
")->fetch();
echo "<br>Thống kê:<br>";
echo "Tổng SP: {$agg['tong_sp']}<br>";
echo "Giá TB: " . number_format($agg['gia_tb'],0,',','.') . "đ<br>";
echo "Giá trị tồn kho: " . number_format($agg['gia_tri_ton_kho'],0,',','.') . "đ<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 6. GROUP BY – sản phẩm theo danh mục
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$group = $pdo->query("
    SELECT dm.ten AS danh_muc, COUNT(sp.id) AS so_san_pham, AVG(sp.gia) AS gia_tb
    FROM danh_muc dm
    LEFT JOIN san_pham sp ON sp.danh_muc_id = dm.id AND sp.active = 1
    GROUP BY dm.id, dm.ten
    HAVING so_san_pham > 0
    ORDER BY so_san_pham DESC
")->fetchAll();
echo "<br>Sản phẩm theo danh mục:<br>";
foreach ($group as $g) {
    echo "→ {$g['danh_muc']}: {$g['so_san_pham']} SP (TB: " . number_format($g['gia_tb'],0,',','.') . "đ)<br>";
}"""
  ),
  (4, "JOIN – Kết Hợp Nhiều Bảng",
   "Thành thạo các loại JOIN: INNER, LEFT, RIGHT và truy vấn dữ liệu từ nhiều bảng.",
   ["INNER JOIN: lấy sản phẩm kèm danh mục",
    "LEFT JOIN: danh mục kể cả không có sản phẩm",
    "Multi-table JOIN: đơn hàng + chi tiết + sản phẩm + khách hàng",
    "Self JOIN: tìm danh mục cha-con",
    "Subquery trong WHERE, FROM, SELECT"],
   ["<code>INNER JOIN</code>: chỉ hàng khớp cả 2 bảng",
    "<code>LEFT JOIN</code>: toàn bộ bảng trái, NULL ở cột phải nếu không khớp",
    "<code>RIGHT JOIN</code>: toàn bộ bảng phải (ít dùng – đổi thứ tự bảng dùng LEFT JOIN)",
    "Alias table: <code>FROM san_pham sp JOIN danh_muc dm ON sp.danh_muc_id = dm.id</code>",
    "Correlated subquery: subquery tham chiếu table bên ngoài"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. INNER JOIN – sản phẩm + danh mục
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ds = $pdo->query("
    SELECT sp.id, sp.ten AS san_pham, sp.gia,
           dm.ten AS danh_muc, dm.slug AS dm_slug
    FROM san_pham sp
    INNER JOIN danh_muc dm ON dm.id = sp.danh_muc_id
    WHERE sp.active = 1
    ORDER BY dm.thu_tu, sp.ten
")->fetchAll();
foreach ($ds as $row) {
    echo "[{$row['danh_muc']}] {$row['san_pham']}: " . number_format($row['gia'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. LEFT JOIN – danh mục + số sản phẩm (kể cả 0)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$dm_stats = $pdo->query("
    SELECT dm.ten, dm.slug,
           COUNT(sp.id) AS so_sp,
           COALESCE(SUM(sp.gia * sp.so_luong), 0) AS gia_tri
    FROM danh_muc dm
    LEFT JOIN san_pham sp ON sp.danh_muc_id = dm.id AND sp.active = 1
    GROUP BY dm.id, dm.ten, dm.slug
    ORDER BY so_sp DESC
")->fetchAll();
echo "<br>Danh mục (kể cả rỗng):<br>";
foreach ($dm_stats as $dm) {
    echo "• {$dm['ten']}: {$dm['so_sp']} SP | " . number_format($dm['gia_tri'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. Subquery – sản phẩm có giá > TB
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$above_avg = $pdo->query("
    SELECT ten, gia
    FROM san_pham
    WHERE gia > (SELECT AVG(gia) FROM san_pham WHERE active = 1)
      AND active = 1
    ORDER BY gia DESC
")->fetchAll();
$avg = $pdo->query("SELECT AVG(gia) FROM san_pham WHERE active=1")->fetchColumn();
echo "<br>Sản phẩm trên TB (" . number_format($avg,0,',','.') . "đ):<br>";
foreach ($above_avg as $sp) {
    echo "• {$sp['ten']}: " . number_format($sp['gia'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. EXISTS subquery
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Danh mục có ít nhất 1 sản phẩm
$has_sp = $pdo->query("
    SELECT ten FROM danh_muc dm
    WHERE EXISTS (
        SELECT 1 FROM san_pham sp WHERE sp.danh_muc_id = dm.id AND sp.active = 1
    )
")->fetchAll(PDO::FETCH_COLUMN);
echo "<br>Danh mục có hàng: " . implode(', ', $has_sp) . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 5. Sản phẩm đang khuyến mãi + % giảm giá
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$km = $pdo->query("
    SELECT ten, gia, gia_km,
           ROUND((gia - gia_km) / gia * 100) AS phan_tram_giam
    FROM san_pham
    WHERE gia_km IS NOT NULL AND gia_km < gia AND active = 1
    ORDER BY phan_tram_giam DESC
")->fetchAll();
echo "<br>KM hôm nay:<br>";
foreach ($km as $sp) {
    echo "🔥 {$sp['ten']}: " . number_format($sp['gia_km'],0,',','.') . "đ (-{$sp['phan_tram_giam']}%)<br>";
}"""
  ),
  (5, "UPDATE và DELETE An Toàn",
   "Thực hiện UPDATE và DELETE đúng cách: cập nhật có điều kiện, soft delete.",
   ["UPDATE một trường, nhiều trường",
    "UPDATE với JOIN từ bảng khác",
    "Soft delete bằng cột <code>deleted_at</code>",
    "Hard delete với CASCADE",
    "ROW_COUNT() kiểm tra số hàng bị ảnh hưởng"],
   ["Luôn kiểm tra <code>rowCount()</code> sau UPDATE/DELETE để biết có thành công không",
    "Soft delete: thêm cột <code>deleted_at TIMESTAMP NULL</code>, không xóa vật lý",
    "<code>UPDATE t1 JOIN t2 ON ... SET t1.col = t2.col</code>: UPDATE với JOIN",
    "<code>DELETE FROM t WHERE id = ?</code> – LUÔN có WHERE trừ khi muốn xóa tất cả",
    "<code>TRUNCATE TABLE t</code>: xóa tất cả, reset AUTO_INCREMENT (không có WHERE)"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. UPDATE một trường
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$stmt = $pdo->prepare("UPDATE san_pham SET luot_xem = luot_xem + 1 WHERE id = ?");
$stmt->execute([1]);
echo "Tăng lượt xem: " . $stmt->rowCount() . " hàng<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. UPDATE nhiều trường
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$upd = $pdo->prepare("UPDATE san_pham SET gia = ?, gia_km = ?, so_luong = ? WHERE id = ?");
$upd->execute([180_000, 150_000, 45, 1]);
echo "UPDATE: " . $upd->rowCount() . " hàng<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. UPDATE với CASE (batch update)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Cập nhật giá nhiều sản phẩm cùng lúc
$gia_moi = [1 => 199_000, 2 => 389_000, 3 => 28_990_000];
$ids     = array_keys($gia_moi);
$cases   = implode(' ', array_map(fn($id) => "WHEN id = $id THEN " . $gia_moi[$id], $ids));
$in_ids  = implode(',', $ids);
$pdo->exec("UPDATE san_pham SET gia = CASE $cases END, updated_at = NOW() WHERE id IN ($in_ids)");
echo "Batch update 3 giá sản phẩm<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. Soft Delete
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Thêm cột deleted_at nếu chưa có
try { $pdo->exec("ALTER TABLE san_pham ADD COLUMN deleted_at TIMESTAMP NULL DEFAULT NULL"); } catch(PDOException) {}

$soft_del = $pdo->prepare("UPDATE san_pham SET deleted_at = NOW(), active = 0 WHERE id = ? AND deleted_at IS NULL");
$soft_del->execute([8]);
echo "Soft delete: " . $soft_del->rowCount() . " hàng<br>";

// Chỉ lấy chưa xóa
$active = $pdo->query("SELECT ten FROM san_pham WHERE deleted_at IS NULL LIMIT 5")->fetchAll(PDO::FETCH_COLUMN);
echo "Còn active: " . implode(', ', $active) . "<br>";

// Restore
$restore = $pdo->prepare("UPDATE san_pham SET deleted_at = NULL, active = 1 WHERE id = ?");
$restore->execute([8]);
echo "Restore: " . $restore->rowCount() . " hàng<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 5. Hard DELETE (thật sự xóa)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Xóa sản phẩm hết hàng và đã bị soft delete > 30 ngày
$del = $pdo->exec("
    DELETE FROM san_pham
    WHERE deleted_at IS NOT NULL
      AND deleted_at < DATE_SUB(NOW(), INTERVAL 30 DAY)
      AND so_luong = 0
");
echo "Hard delete: $del hàng cũ<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 6. Kiểm tra rowCount
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$s = $pdo->prepare("UPDATE san_pham SET ten = ? WHERE id = ?");
$s->execute(['Áo thun Polo (mới)', 1]);
if ($s->rowCount() === 0) {
    echo "Không tìm thấy sản phẩm hoặc giá trị không đổi<br>";
} else {
    echo "Cập nhật thành công: " . $s->rowCount() . " hàng<br>";
}"""
  ),
  (6, "Tìm Kiếm và Lọc Nâng Cao",
   "Xây dựng tính năng tìm kiếm, lọc đa điều kiện và gợi ý từ khóa.",
   ["Lọc đa điều kiện: danh mục + khoảng giá + từ khóa",
    "Dynamic WHERE clause an toàn không SQL injection",
    "Sắp xếp theo nhiều tiêu chí",
    "Autocomplete – gợi ý từ khóa",
    "Full-text search với MATCH AGAINST"],
   ["Dynamic WHERE: build mảng <code>$where[]</code> và <code>$params[]</code> rồi join",
    "Column name KHÔNG parameterize được → dùng whitelist validation",
    "<code>MATCH(col) AGAINST('keyword' IN BOOLEAN MODE)</code>: full-text index",
    "Autocomplete: <code>SELECT DISTINCT ten FROM ... WHERE ten LIKE 'kw%' LIMIT 10</code>",
    "Relevance sorting: MATCH() trả về score, ORDER BY score DESC"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Hàm tìm kiếm đa điều kiện
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function search_san_pham(PDO $pdo, array $filters = [], int $page = 1, int $per_page = 6): array {
    $where  = ['sp.active = 1', 'sp.deleted_at IS NULL'];
    $params = [];

    // Từ khóa
    if (!empty($filters['q'])) {
        $where[] = '(sp.ten LIKE :q OR sp.mo_ta LIKE :q)';
        $params[':q'] = '%' . $filters['q'] . '%';
    }
    // Danh mục
    if (!empty($filters['dm_id'])) {
        $where[] = 'sp.danh_muc_id = :dm_id';
        $params[':dm_id'] = (int)$filters['dm_id'];
    }
    // Khoảng giá
    if (!empty($filters['gia_min'])) {
        $where[]         = 'sp.gia >= :gia_min';
        $params[':gia_min'] = (float)$filters['gia_min'];
    }
    if (!empty($filters['gia_max'])) {
        $where[]         = 'sp.gia <= :gia_max';
        $params[':gia_max'] = (float)$filters['gia_max'];
    }
    // Chỉ khuyến mãi
    if (!empty($filters['km_only'])) {
        $where[] = 'sp.gia_km IS NOT NULL AND sp.gia_km < sp.gia';
    }
    // Còn hàng
    if (!empty($filters['con_hang'])) {
        $where[] = 'sp.so_luong > 0';
    }

    // Sắp xếp (whitelist)
    $sortable = ['gia' => 'sp.gia', 'ten' => 'sp.ten', 'luot_xem' => 'sp.luot_xem', 'moi' => 'sp.created_at'];
    $sort_col = $sortable[$filters['sort'] ?? ''] ?? 'sp.created_at';
    $sort_dir = ($filters['dir'] ?? '') === 'asc' ? 'ASC' : 'DESC';

    $where_sql = implode(' AND ', $where);

    // Đếm tổng
    $count_stmt = $pdo->prepare("SELECT COUNT(*) FROM san_pham sp JOIN danh_muc dm ON dm.id = sp.danh_muc_id WHERE $where_sql");
    $count_stmt->execute($params);
    $total = (int)$count_stmt->fetchColumn();

    // Dữ liệu trang
    $offset = ($page - 1) * $per_page;
    $stmt   = $pdo->prepare("
        SELECT sp.id, sp.ten, sp.gia, sp.gia_km, sp.so_luong, sp.luot_xem,
               dm.ten AS danh_muc
        FROM san_pham sp
        JOIN danh_muc dm ON dm.id = sp.danh_muc_id
        WHERE $where_sql
        ORDER BY $sort_col $sort_dir
        LIMIT :limit OFFSET :offset
    ");
    $stmt->execute(array_merge($params, [':limit' => $per_page, ':offset' => $offset]));

    return [
        'items'      => $stmt->fetchAll(),
        'total'      => $total,
        'tong_trang' => (int)ceil($total / $per_page),
        'trang'      => $page,
    ];
}

// ── Test tìm kiếm ─────────────────
$ket_qua = search_san_pham($pdo, [
    'q'        => 'á',
    'gia_min'  => 100_000,
    'gia_max'  => 500_000,
    'con_hang' => true,
    'sort'     => 'gia',
    'dir'      => 'asc',
]);
echo "Tìm thấy {$ket_qua['total']} sản phẩm (trang {$ket_qua['trang']}/{$ket_qua['tong_trang']}):<br>";
foreach ($ket_qua['items'] as $sp) {
    $gia = $sp['gia_km'] ? number_format($sp['gia_km'],0,',','.') . "đ 🔥" : number_format($sp['gia'],0,',','.') . "đ";
    echo "• [{$sp['danh_muc']}] {$sp['ten']}: $gia (còn {$sp['so_luong']})<br>";
}

// ── Autocomplete gợi ý ────────────
$ac_kw = 'á';
$ac = $pdo->prepare("SELECT DISTINCT ten FROM san_pham WHERE ten LIKE ? AND active = 1 LIMIT 8");
$ac->execute([$ac_kw . '%']);
$suggestions = $ac->fetchAll(PDO::FETCH_COLUMN);
echo "<br>Gợi ý '$ac_kw': " . implode(', ', $suggestions) . "<br>";"""
  ),
  (7, "Phân Trang Chuẩn Và Đầy Đủ",
   "Xây dựng class Paginator tái sử dụng cho mọi truy vấn với đầy đủ thông tin trang.",
   ["Tạo class <code>Paginator</code> nhận PDO query",
    "Tính tổng, trang hiện tại, first/last/prev/next",
    "Render HTML pagination links",
    "Tích hợp với search params trong URL",
    "Cursor-based pagination (nâng cao)"],
   ["Offset pagination: đơn giản nhưng chậm với dữ liệu lớn (<code>LIMIT 10 OFFSET 10000</code>)",
    "Cursor pagination: dùng <code>WHERE id > last_id</code> – nhanh hơn",
    "Page info: trang hiện tại, tổng trang, tổng bản ghi, from, to",
    "URL query string: <code>?trang=2&q=keyword&sort=gia</code>",
    "Window function trong MySQL 8: <code>ROW_NUMBER() OVER(ORDER BY id)</code>"],
   """\
<?php
$pdo = get_pdo();

class Paginator {
    public readonly int   $total;
    public readonly int   $tong_trang;
    public readonly int   $tu;    // bản ghi bắt đầu
    public readonly int   $den;   // bản ghi kết thúc
    public readonly array $items;

    public function __construct(
        private PDO    $pdo,
        private string $count_sql,
        private string $data_sql,
        private array  $params     = [],
        public  int    $trang      = 1,
        public  int    $per_page   = 10,
    ) {
        // Đếm tổng
        $cs = $pdo->prepare($count_sql);
        $cs->execute($params);
        $this->total = (int)$cs->fetchColumn();
        $this->tong_trang = max(1, (int)ceil($this->total / $per_page));
        $this->trang = max(1, min($trang, $this->tong_trang));

        // Lấy dữ liệu trang
        $offset = ($this->trang - 1) * $per_page;
        $ds = $pdo->prepare($data_sql . " LIMIT :limit OFFSET :offset");
        $ds->execute(array_merge($params, [':limit' => $per_page, ':offset' => $offset]));
        $this->items = $ds->fetchAll();

        $this->tu  = $this->total === 0 ? 0 : $offset + 1;
        $this->den = min($offset + $per_page, $this->total);
    }

    public function hasPrev(): bool { return $this->trang > 1; }
    public function hasNext(): bool { return $this->trang < $this->tong_trang; }

    public function links(string $base_url = '?', array $extra_params = []): string {
        if ($this->tong_trang <= 1) return '';
        $params_str = http_build_query(array_filter($extra_params));
        if ($params_str) $params_str = '&' . $params_str;
        $html = '<nav class="pagination">';

        if ($this->hasPrev()) {
            $html .= "<a href='{$base_url}trang=" . ($this->trang-1) . $params_str . "'>← Trước</a> ";
        }
        // Trang đầu nếu không hiển thị
        if ($this->trang > 3) $html .= "<a href='{$base_url}trang=1$params_str'>1</a> ... ";
        // Các trang xung quanh
        for ($p = max(1, $this->trang-2); $p <= min($this->tong_trang, $this->trang+2); $p++) {
            $active = $p === $this->trang ? ' class="active"' : '';
            $html .= "<a href='{$base_url}trang=$p$params_str'$active>$p</a> ";
        }
        // Trang cuối
        if ($this->trang < $this->tong_trang - 2) $html .= "... <a href='{$base_url}trang={$this->tong_trang}$params_str'>{$this->tong_trang}</a> ";
        if ($this->hasNext()) {
            $html .= "<a href='{$base_url}trang=" . ($this->trang+1) . $params_str . "'>Sau →</a>";
        }
        return $html . '</nav>';
    }

    public function info(): string {
        return "Hiển thị {$this->tu}–{$this->den} trong {$this->total} kết quả";
    }
}

// ── Sử dụng Paginator ─────────────
$trang = (int)($_GET['trang'] ?? 1);
$pager = new Paginator(
    $pdo,
    "SELECT COUNT(*) FROM san_pham sp JOIN danh_muc dm ON dm.id = sp.danh_muc_id WHERE sp.active = 1",
    "SELECT sp.ten, sp.gia, dm.ten AS dm FROM san_pham sp JOIN danh_muc dm ON dm.id = sp.danh_muc_id WHERE sp.active = 1 ORDER BY sp.id",
    trang: $trang, per_page: 3
);

echo $pager->info() . "<br>";
foreach ($pager->items as $sp) echo "• [{$sp['dm']}] {$sp['ten']}: " . number_format($sp['gia'],0,',','.') . "đ<br>";
echo $pager->links();"""
  ),
  (8, "Authentication – Đăng Ký và Đăng Nhập",
   "Xây dựng hệ thống đăng ký, đăng nhập hoàn chỉnh với password hashing và session.",
   ["Đăng ký với validation và hash password",
    "Đăng nhập kiểm tra email + password",
    "Lưu session sau login",
    "Middleware bảo vệ route",
    "Remember me bằng cookie"],
   ["<code>password_hash($pass, PASSWORD_DEFAULT)</code>: hash bcrypt",
    "<code>password_verify($pass, $hash)</code>: verify hash",
    "KHÔNG bao giờ lưu plain-text password vào DB",
    "Session fixation attack: gọi <code>session_regenerate_id(true)</code> sau login",
    "Remember me: lưu secure token vào DB và cookie, verify khi quay lại"],
   """\
<?php
session_start();

$pdo = get_pdo();
// Tạo bảng users
$pdo->exec("
    CREATE TABLE IF NOT EXISTS users (
        id          INT AUTO_INCREMENT PRIMARY KEY,
        ho_ten      VARCHAR(100) NOT NULL,
        email       VARCHAR(150) UNIQUE NOT NULL,
        mat_khau    VARCHAR(255) NOT NULL,
        role        ENUM('user','admin') DEFAULT 'user',
        remember_token VARCHAR(64) NULL,
        last_login  TIMESTAMP NULL,
        created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
");

// ── Auth Service ──────────────────
class AuthService {
    public function __construct(private PDO $pdo) {}

    // Đăng ký
    public function register(string $ho_ten, string $email, string $mat_khau): array {
        // Validation
        if (strlen($ho_ten) < 2) throw new InvalidArgumentException("Họ tên ít nhất 2 ký tự");
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) throw new InvalidArgumentException("Email không hợp lệ");
        if (strlen($mat_khau) < 8) throw new InvalidArgumentException("Mật khẩu ít nhất 8 ký tự");

        // Kiểm tra email đã tồn tại
        $check = $this->pdo->prepare("SELECT id FROM users WHERE email = ?");
        $check->execute([$email]);
        if ($check->fetch()) throw new RuntimeException("Email đã được sử dụng");

        // Hash và insert
        $hash = password_hash($mat_khau, PASSWORD_DEFAULT);
        $stmt = $this->pdo->prepare("INSERT INTO users (ho_ten, email, mat_khau) VALUES (?,?,?)");
        $stmt->execute([$ho_ten, $email, $hash]);
        return $this->findById((int)$this->pdo->lastInsertId());
    }

    // Đăng nhập
    public function login(string $email, string $mat_khau, bool $remember = false): array {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE email = ? LIMIT 1");
        $stmt->execute([$email]);
        $user = $stmt->fetch();
        if (!$user || !password_verify($mat_khau, $user['mat_khau'])) {
            throw new RuntimeException("Email hoặc mật khẩu không đúng");
        }
        // Cập nhật thời gian login
        $this->pdo->prepare("UPDATE users SET last_login = NOW() WHERE id = ?")->execute([$user['id']]);
        // Session fixation prevention
        session_regenerate_id(true);
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['role']    = $user['role'];
        // Remember me
        if ($remember) {
            $token = bin2hex(random_bytes(32));
            $this->pdo->prepare("UPDATE users SET remember_token = ? WHERE id = ?")->execute([$token, $user['id']]);
            setcookie('remember_token', $token, time() + 30*24*3600, '/', '', true, true);
        }
        return $user;
    }

    public function logout(): void {
        if (isset($_COOKIE['remember_token'])) {
            $this->pdo->prepare("UPDATE users SET remember_token=NULL WHERE remember_token=?")->execute([$_COOKIE['remember_token']]);
            setcookie('remember_token', '', time()-1, '/');
        }
        session_destroy();
    }

    public function findById(int $id): array {
        $stmt = $this->pdo->prepare("SELECT id, ho_ten, email, role, created_at FROM users WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch() ?: throw new RuntimeException("User không tồn tại");
    }

    public function currentUser(): ?array {
        if (!isset($_SESSION['user_id'])) return null;
        try { return $this->findById($_SESSION['user_id']); }
        catch (RuntimeException) { return null; }
    }
}

// ── Test ──────────────────────────
$auth = new AuthService($pdo);
try {
    $user = $auth->register("Nguyễn Test", "test@demo.vn", "password123");
    echo "✅ Đăng ký: {$user['ho_ten']} (#{$user['id']})<br>";
} catch (Exception $e) { echo "ℹ️ {$e->getMessage()}<br>"; }

try {
    $logged = $auth->login("test@demo.vn", "password123");
    echo "✅ Đăng nhập: {$logged['ho_ten']} | Role: {$logged['role']}<br>";
} catch (Exception $e) { echo "❌ {$e->getMessage()}<br>"; }

try {
    $auth->login("test@demo.vn", "sai_mat_khau");
} catch (RuntimeException $e) { echo "❌ {$e->getMessage()}<br>"; }

$current = $auth->currentUser();
echo $current ? "Đang đăng nhập: {$current['ho_ten']}<br>" : "Chưa đăng nhập<br>";"""
  ),
  (9, "Stored Procedures và Views",
   "Tạo stored procedures, functions và views trong MySQL để tối ưu hóa truy vấn.",
   ["Tạo Stored Procedure: báo cáo doanh thu",
    "Tạo MySQL Function: tính phí ship",
    "Tạo VIEW: sản phẩm kèm danh mục",
    "CALL procedure từ PHP PDO",
    "OUT parameter trong stored procedure"],
   ["Stored Procedure: đoạn SQL lưu ở DB, gọi bằng CALL",
    "View: câu query lưu thành tên bảng ảo",
    "<code>DELIMITER //</code>: đổi delimiter để viết procedure",
    "IN/OUT/INOUT parameter: truyền vào, trả về, hay cả 2",
    "Views cải thiện readability nhưng có thể ảnh hưởng performance"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. Tạo VIEW
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$pdo->exec("
    CREATE OR REPLACE VIEW v_san_pham_day_du AS
    SELECT
        sp.id, sp.ten, sp.slug, sp.gia,
        COALESCE(sp.gia_km, sp.gia) AS gia_hien_tai,
        sp.gia_km IS NOT NULL AND sp.gia_km < sp.gia AS dang_khuyen_mai,
        sp.so_luong, sp.luot_xem,
        dm.ten AS danh_muc, dm.slug AS dm_slug,
        ROUND((sp.gia - COALESCE(sp.gia_km, sp.gia)) / sp.gia * 100) AS phan_tram_giam,
        sp.created_at
    FROM san_pham sp
    JOIN danh_muc dm ON dm.id = sp.danh_muc_id
    WHERE sp.active = 1 AND sp.deleted_at IS NULL
");

// Dùng như bảng thường
$ds = $pdo->query("SELECT ten, gia_hien_tai, danh_muc FROM v_san_pham_day_du ORDER BY gia_hien_tai")->fetchAll();
echo "View – tất cả SP:<br>";
foreach ($ds as $sp) echo "• [{$sp['danh_muc']}] {$sp['ten']}: " . number_format($sp['gia_hien_tai'],0,',','.') . "đ<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. Stored Procedure – báo cáo theo danh mục
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$pdo->exec("DROP PROCEDURE IF EXISTS sp_bao_cao_danh_muc");
$pdo->exec("
    CREATE PROCEDURE sp_bao_cao_danh_muc(IN p_dm_id INT)
    BEGIN
        SELECT
            dm.ten AS danh_muc,
            COUNT(sp.id) AS so_san_pham,
            SUM(sp.so_luong) AS tong_ton_kho,
            MIN(sp.gia) AS gia_thap_nhat,
            MAX(sp.gia) AS gia_cao_nhat,
            AVG(sp.gia) AS gia_trung_binh,
            SUM(sp.gia * sp.so_luong) AS gia_tri_ton_kho
        FROM danh_muc dm
        LEFT JOIN san_pham sp ON sp.danh_muc_id = dm.id AND sp.active = 1
        WHERE (p_dm_id IS NULL OR dm.id = p_dm_id)
        GROUP BY dm.id, dm.ten;
    END
");

// Gọi procedure
$stmt = $pdo->prepare("CALL sp_bao_cao_danh_muc(?)");
$stmt->execute([null]);  // null = tất cả danh mục
echo "<br>Báo cáo danh mục:<br>";
foreach ($stmt->fetchAll() as $row) {
    echo "📦 {$row['danh_muc']}: {$row['so_san_pham']} SP | kho: {$row['tong_ton_kho']} | TB: " . number_format($row['gia_trung_binh'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. Stored Function
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$pdo->exec("DROP FUNCTION IF EXISTS fn_tinh_phi_ship");
$pdo->exec("
    CREATE FUNCTION fn_tinh_phi_ship(p_tinh_thanh VARCHAR(50), p_tong_tien DECIMAL(15,2))
    RETURNS DECIMAL(15,2) DETERMINISTIC
    BEGIN
        DECLARE phi DECIMAL(15,2);
        IF p_tong_tien >= 500000 THEN SET phi = 0;
        ELSEIF p_tinh_thanh = 'Hà Nội' OR p_tinh_thanh = 'Hồ Chí Minh' THEN SET phi = 20000;
        ELSE SET phi = 35000;
        END IF;
        RETURN phi;
    END
");

// Dùng trong query
$phiShip = $pdo->prepare("SELECT fn_tinh_phi_ship(?, ?) AS phi_ship");
$phiShip->execute(['Đà Nẵng', 300_000]);
$phi = $phiShip->fetchColumn();
echo "<br>Phí ship Đà Nẵng (300k): " . number_format($phi,0,',','.') . "đ<br>";
$phiShip->execute(['Hà Nội', 600_000]);
echo "Phí ship Hà Nội (600k - miễn phí): " . number_format($phiShip->fetchColumn(),0,',','.') . "đ<br>";"""
  ),
  (10, "Báo Cáo và Thống Kê Nâng Cao",
   "Viết các truy vấn thống kê phức tạp: doanh thu theo thời gian, top sản phẩm, biểu đồ.",
   ["Doanh thu theo ngày/tháng/năm",
    "Top 10 sản phẩm bán chạy nhất",
    "Phân tích hành vi khách hàng",
    "Window functions: RANK, ROW_NUMBER, LAG",
    "Xuất dữ liệu ra CSV"],
   ["<code>DATE_FORMAT(col, '%Y-%m')</code>: nhóm theo tháng",
    "<code>YEAR(col)</code>, <code>MONTH(col)</code>, <code>DAY(col)</code>: tách thành phần ngày",
    "Window function: <code>RANK() OVER(PARTITION BY dm_id ORDER BY ban_chay DESC)</code>",
    "<code>LAG(col, 1) OVER(ORDER BY thang)</code>: giá trị kỳ trước để tính % tăng trưởng",
    "Xuất CSV: dùng <code>fputcsv()</code> với <code>php://output</code>"],
   """\
<?php
$pdo = get_pdo();
// Tạo bảng đơn hàng mẫu
$pdo->exec("
    CREATE TABLE IF NOT EXISTS doanh_thu_thang (
        thang DATE PRIMARY KEY,
        so_don INT DEFAULT 0,
        doanh_thu DECIMAL(15,2) DEFAULT 0
    );
    INSERT IGNORE INTO doanh_thu_thang VALUES
    ('2024-01-01', 45, 32500000),('2024-02-01', 38, 28000000),
    ('2024-03-01', 62, 48500000),('2024-04-01', 55, 41000000),
    ('2024-05-01', 70, 56000000),('2024-06-01', 68, 53500000),
    ('2024-07-01', 82, 65000000),('2024-08-01', 90, 71000000),
    ('2024-09-01', 75, 59000000),('2024-10-01', 95, 76500000),
    ('2024-11-01',120, 98000000),('2024-12-01',145,115000000);
");

// ── 1. Doanh thu từng tháng + % tăng trưởng ──
$ds = $pdo->query("
    SELECT
        DATE_FORMAT(thang, '%m/%Y') AS thang_hien,
        so_don, doanh_thu,
        LAG(doanh_thu) OVER(ORDER BY thang) AS dt_thang_truoc
    FROM doanh_thu_thang
    ORDER BY thang
")->fetchAll();
echo "Báo cáo doanh thu 2024:<br>";
foreach ($ds as $row) {
    $tang_truong = '';
    if ($row['dt_thang_truoc']) {
        $pct = round(($row['doanh_thu'] - $row['dt_thang_truoc']) / $row['dt_thang_truoc'] * 100, 1);
        $tang_truong = ($pct >= 0 ? " ↑$pct%" : " ↓$pct%");
    }
    $dt = number_format($row['doanh_thu'],0,',','.');
    echo "Tháng {$row['thang_hien']}: {$dt}đ ({$row['so_don']} đơn)$tang_truong<br>";
}

// ── 2. Tổng kết năm ──────────────
$nam = $pdo->query("
    SELECT
        SUM(doanh_thu) AS tong_dt,
        SUM(so_don)    AS tong_don,
        AVG(doanh_thu) AS dt_tb_thang,
        MAX(doanh_thu) AS thang_cao_nhat,
        MIN(doanh_thu) AS thang_thap_nhat
    FROM doanh_thu_thang
")->fetch();
echo "<br>Tổng 2024: " . number_format($nam['tong_dt'],0,',','.') . "đ | " . $nam['tong_don'] . " đơn<br>";
echo "Bình quân: " . number_format($nam['dt_tb_thang'],0,',','.') . "đ/tháng<br>";

// ── 3. Top sản phẩm theo lượt xem ──
$top_sp = $pdo->query("
    SELECT ten, gia, luot_xem, so_luong,
           RANK() OVER(ORDER BY luot_xem DESC) AS xep_hang
    FROM san_pham WHERE active = 1
    LIMIT 5
")->fetchAll();
echo "<br>Top 5 XEM NHIỀU NHẤT:<br>";
foreach ($top_sp as $sp) {
    echo "#{$sp['xep_hang']} {$sp['ten']}: {$sp['luot_xem']} lượt xem<br>";
}

// ── 4. Xuất CSV ───────────────────
function export_csv_doanh_thu(PDO $pdo): string {
    $rows = $pdo->query("SELECT DATE_FORMAT(thang,'%m/%Y'), so_don, doanh_thu FROM doanh_thu_thang ORDER BY thang")->fetchAll(PDO::FETCH_NUM);
    ob_start();
    $f = fopen('php://output', 'w');
    fprintf($f, chr(0xEF).chr(0xBB).chr(0xBF)); // UTF-8 BOM cho Excel
    fputcsv($f, ['Tháng','Số đơn','Doanh thu']);
    foreach ($rows as $row) fputcsv($f, $row);
    fclose($f);
    return ob_get_clean();
}
$csv = export_csv_doanh_thu($pdo);
echo "<br>CSV preview:<br><pre>" . htmlspecialchars(substr($csv,3,200)) . "</pre>";"""
  ),
  (11, "File Upload và Quản Lý Media",
   "Xây dựng hệ thống upload ảnh sản phẩm an toàn với validation và resize.",
   ["Validate file: loại, kích thước, extension",
    "Đổi tên file an toàn (UUID)",
    "Resize ảnh và tạo thumbnail",
    "Lưu thông tin file vào DB",
    "Xóa file khi xóa sản phẩm"],
   ["Validate MIME type bằng <code>finfo_file()</code> – không tin <code>$_FILES['type']</code>",
    "Đổi tên file thành UUID để tránh trùng và ẩn tên gốc",
    "Lưu ảnh gốc + thumbnail riêng thư mục",
    "<code>move_uploaded_file()</code>: di chuyển file từ tmpdir",
    "Giới hạn extension: chỉ cho phép jpg, png, webp, gif"],
   """\
<?php
$pdo = get_pdo();

class MediaUploader {
    private const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif'];
    private const MAX_SIZE      = 5 * 1024 * 1024; // 5 MB
    private const ALLOWED_EXT   = ['jpg','jpeg','png','webp','gif'];

    public function __construct(private string $upload_dir = 'uploads/') {
        foreach (['original','thumbnails'] as $sub) {
            $path = $upload_dir . $sub;
            if (!is_dir($path)) mkdir($path, 0755, true);
        }
    }

    public function upload(array $file, int $product_id): array {
        // 1. Kiểm tra lỗi upload
        if ($file['error'] !== UPLOAD_ERR_OK) throw new RuntimeException("Upload lỗi code: {$file['error']}");
        if ($file['size'] > self::MAX_SIZE) throw new InvalidArgumentException("File quá lớn (tối đa 5MB)");

        // 2. Validate MIME bằng finfo (an toàn hơn $_FILES['type'])
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        $mime  = finfo_file($finfo, $file['tmp_name']);
        finfo_close($finfo);
        if (!in_array($mime, self::ALLOWED_TYPES)) {
            throw new InvalidArgumentException("Loại file không hỗ trợ: $mime");
        }

        // 3. Kiểm tra extension
        $ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
        if (!in_array($ext, self::ALLOWED_EXT)) {
            throw new InvalidArgumentException("Extension không hợp lệ: $ext");
        }

        // 4. Tên file an toàn (UUID)
        $uuid     = sprintf('%04x%04x-%04x-%04x-%04x-%12s',
            mt_rand(0,0xffff), mt_rand(0,0xffff), mt_rand(0,0xffff),
            mt_rand(0,0x0fff)|0x4000, mt_rand(0,0x3fff)|0x8000, bin2hex(random_bytes(6)));
        $filename = $uuid . '.' . $ext;
        $dest     = $this->upload_dir . 'original/' . $filename;

        // 5. Move file
        if (!move_uploaded_file($file['tmp_name'], $dest)) {
            throw new RuntimeException("Không thể lưu file");
        }

        // 6. Tạo thumbnail
        $thumb_path = $this->upload_dir . 'thumbnails/' . $filename;
        $this->createThumbnail($dest, $thumb_path, 400, 400);

        return [
            'filename'   => $filename,
            'path'       => $dest,
            'thumb'      => $thumb_path,
            'size'       => filesize($dest),
            'mime'       => $mime,
        ];
    }

    private function createThumbnail(string $src, string $dest, int $maxW, int $maxH): void {
        [$w, $h, $type] = getimagesize($src);
        $ratio = min($maxW/$w, $maxH/$h);
        $nw = (int)($w*$ratio); $nh = (int)($h*$ratio);
        $orig  = match($type) {
            IMAGETYPE_JPEG => imagecreatefromjpeg($src),
            IMAGETYPE_PNG  => imagecreatefrompng($src),
            IMAGETYPE_WEBP => imagecreatefromwebp($src),
            default        => imagecreatefromjpeg($src),
        };
        $thumb = imagecreatetruecolor($nw, $nh);
        imagecopyresampled($thumb, $orig, 0,0,0,0,$nw,$nh,$w,$h);
        match($type) {
            IMAGETYPE_PNG  => imagepng($thumb, $dest, 8),
            IMAGETYPE_WEBP => imagewebp($thumb, $dest, 80),
            default        => imagejpeg($thumb, $dest, 85),
        };
        imagedestroy($orig); imagedestroy($thumb);
    }
}

// Giả lập upload (thay bằng $_FILES['anh'] trong thực tế)
$fake_file = [
    'name'     => 'product_photo.jpg',
    'type'     => 'image/jpeg',
    'tmp_name' => tempnam(sys_get_temp_dir(), 'upload'),
    'error'    => UPLOAD_ERR_OK,
    'size'     => 1_200_000,
];
// Tạo ảnh giả 1×1 pixel JPEG cho demo
imagejpeg(imagecreatetruecolor(800,600), $fake_file['tmp_name'], 90);

$uploader = new MediaUploader(__DIR__ . '/uploads/');
try {
    $result = $uploader->upload($fake_file, 1);
    echo "✅ Upload thành công:<br>";
    echo "File: {$result['filename']}<br>";
    echo "Size: " . number_format($result['size']) . " bytes<br>";
    echo "MIME: {$result['mime']}<br>";
} catch (Exception $e) {
    echo "❌ {$e->getMessage()}<br>";
}"""
  ),
  (12, "API Client – Gọi API Bên Thứ Ba",
   "Gọi API bên thứ ba với cURL và Guzzle, xử lý response và error handling.",
   ["Gọi API với <code>file_get_contents</code> và <code>stream_context</code>",
    "Gọi API với cURL (GET, POST, headers)",
    "Parse JSON response",
    "Retry logic khi API thất bại",
    "Gọi song song nhiều API (multi_curl)"],
   ["<code>curl_init(), curl_setopt(), curl_exec(), curl_close()</code>",
    "<code>CURLOPT_RETURNTRANSFER => true</code>: trả về string không in ra",
    "<code>curl_getinfo($ch, CURLINFO_HTTP_CODE)</code>: HTTP status code",
    "<code>curl_multi_exec()</code>: chạy nhiều requests song song",
    "Rate limiting: dùng <code>sleep(1)</code> hoặc token bucket giữa các requests"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// HTTP Client đơn giản bằng cURL
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class HttpClient {
    private array $default_headers = ['Content-Type: application/json', 'Accept: application/json'];
    private int   $timeout = 30;
    private int   $max_retries = 3;

    public function get(string $url, array $headers = []): array {
        return $this->request('GET', $url, null, $headers);
    }
    public function post(string $url, array $data, array $headers = []): array {
        return $this->request('POST', $url, json_encode($data), $headers);
    }
    public function put(string $url, array $data, array $headers = []): array {
        return $this->request('PUT', $url, json_encode($data), $headers);
    }
    public function delete(string $url, array $headers = []): array {
        return $this->request('DELETE', $url, null, $headers);
    }

    private function request(string $method, string $url, ?string $body, array $extra_headers, int $retry = 0): array {
        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL            => $url,
            CURLOPT_CUSTOMREQUEST  => $method,
            CURLOPT_HTTPHEADER     => array_merge($this->default_headers, $extra_headers),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => $this->timeout,
            CURLOPT_SSL_VERIFYPEER => true,
            CURLOPT_FOLLOWLOCATION => true,
        ]);
        if ($body) curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
        $response = curl_exec($ch);
        $code     = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error    = curl_error($ch);
        curl_close($ch);

        if ($error) {
            if ($retry < $this->max_retries) {
                sleep(pow(2, $retry));  // exponential backoff
                return $this->request($method, $url, $body, $extra_headers, $retry+1);
            }
            throw new RuntimeException("cURL Error: $error");
        }
        $data = json_decode($response, true);
        return ['status' => $code, 'data' => $data, 'raw' => $response];
    }

    // Multi-request song song
    public function parallel(array $requests): array {
        $mh   = curl_multi_init();
        $handles = [];
        foreach ($requests as $key => $req) {
            $ch = curl_init();
            curl_setopt_array($ch, [
                CURLOPT_URL => $req['url'], CURLOPT_RETURNTRANSFER => true,
                CURLOPT_TIMEOUT => $this->timeout,
            ]);
            curl_multi_add_handle($mh, $ch);
            $handles[$key] = $ch;
        }
        do { curl_multi_exec($mh, $active); curl_multi_select($mh); } while ($active);
        $results = [];
        foreach ($handles as $key => $ch) {
            $results[$key] = json_decode(curl_multi_getcontent($ch), true);
            curl_multi_remove_handle($mh, $ch);
        }
        curl_multi_close($mh);
        return $results;
    }
}

// ── Sử dụng ──────────────────────
$client = new HttpClient();

// GET request
$res = $client->get('https://jsonplaceholder.typicode.com/users/1');
if ($res['status'] === 200) {
    echo "User: {$res['data']['name']} | Email: {$res['data']['email']}<br>";
}

// POST request
$post = $client->post('https://jsonplaceholder.typicode.com/posts', [
    'title' => 'Bài viết PHP',
    'body'  => 'Học PHP với NenTang.vn',
    'userId'=> 1,
]);
echo "POST status: {$post['status']} | ID: {$post['data']['id']}<br>";

// Parallel requests (nhanh hơn tuần tự)
$t = microtime(true);
$results = $client->parallel([
    'user1' => ['url' => 'https://jsonplaceholder.typicode.com/users/1'],
    'user2' => ['url' => 'https://jsonplaceholder.typicode.com/users/2'],
    'posts' => ['url' => 'https://jsonplaceholder.typicode.com/posts?userId=1'],
]);
$ms = round((microtime(true)-$t)*1000);
echo "Parallel {$ms}ms: {$results['user1']['name']}, {$results['user2']['name']}, " . count($results['posts']) . " bài<br>";"""
  ),
  (13, "CRUD Hoàn Chỉnh với PDO và OOP",
   "Xây dựng CRUD hoàn chỉnh cho module Sản Phẩm theo kiến trúc OOP-PDO sạch.",
   ["ProductRepository với đầy đủ CRUD",
    "Validation với DTO (Data Transfer Object)",
    "Error handling với custom exceptions",
    "Pagination tích hợp trong repository",
    "Unit test cho repository"],
   ["DTO: object chuyên chứa dữ liệu truyền vào, có thể validate ngay",
    "Custom Exception: <code>class NotFoundException extends RuntimeException {}</code>",
    "Repository method: <code>findAll, findById, create, update, delete, paginate</code>",
    "<code>readonly</code> properties cho DTO: tránh thay đổi sau khi tạo",
    "Separation of concerns: Repository chỉ CRUD, không biết về HTTP"],
   """\
<?php
$pdo = get_pdo();

// ── Custom Exceptions ─────────────
class NotFoundException      extends RuntimeException {}
class ValidationException    extends InvalidArgumentException {
    public function __construct(private array $errors) {
        parent::__construct("Validation thất bại: " . implode(', ', $errors));
    }
    public function getErrors(): array { return $this->errors; }
}

// ── DTO ───────────────────────────
readonly class CreateProductDTO {
    public string $ten;
    public float  $gia;
    public int    $so_luong;
    public ?int   $danh_muc_id;

    public function __construct(array $data) {
        $errors = [];
        $this->ten       = trim($data['ten'] ?? '');
        if (strlen($this->ten) < 2) $errors[] = "Tên ít nhất 2 ký tự";
        $this->gia       = (float)($data['gia'] ?? 0);
        if ($this->gia < 0) $errors[] = "Giá không âm";
        $this->so_luong  = (int)($data['so_luong'] ?? 0);
        if ($this->so_luong < 0) $errors[] = "Số lượng không âm";
        $this->danh_muc_id = isset($data['danh_muc_id']) ? (int)$data['danh_muc_id'] : null;
        if ($errors) throw new ValidationException($errors);
    }
}

// ── Repository ────────────────────
class ProductRepository {
    public function __construct(private PDO $pdo) {}

    public function findAll(int $page = 1, int $per_page = 10): array {
        $offset = ($page-1) * $per_page;
        $items  = $this->pdo->prepare("SELECT * FROM san_pham WHERE active=1 ORDER BY id DESC LIMIT ? OFFSET ?");
        $items->execute([$per_page, $offset]);
        $total  = (int)$this->pdo->query("SELECT COUNT(*) FROM san_pham WHERE active=1")->fetchColumn();
        return ['items' => $items->fetchAll(), 'total' => $total, 'page' => $page, 'per_page' => $per_page];
    }

    public function findById(int $id): array {
        $stmt = $this->pdo->prepare("SELECT * FROM san_pham WHERE id = ? AND active = 1");
        $stmt->execute([$id]);
        $row = $stmt->fetch();
        if (!$row) throw new NotFoundException("Sản phẩm #$id không tồn tại");
        return $row;
    }

    public function create(CreateProductDTO $dto): array {
        $slug = $this->slugify($dto->ten);
        $stmt = $this->pdo->prepare(
            "INSERT INTO san_pham (ten, slug, gia, so_luong, danh_muc_id) VALUES (:ten,:slug,:gia,:sl,:dm)"
        );
        $stmt->execute([':ten'=>$dto->ten,':slug'=>$slug,':gia'=>$dto->gia,':sl'=>$dto->so_luong,':dm'=>$dto->danh_muc_id]);
        return $this->findById((int)$this->pdo->lastInsertId());
    }

    public function update(int $id, array $data): array {
        $this->findById($id);  // throws if not found
        $fields = []; $params = [];
        foreach (['ten','gia','so_luong','gia_km','danh_muc_id'] as $col) {
            if (array_key_exists($col, $data)) {
                $fields[] = "$col = :$col";
                $params[":$col"] = $data[$col];
            }
        }
        if (empty($fields)) return $this->findById($id);
        $params[':id'] = $id;
        $this->pdo->prepare("UPDATE san_pham SET " . implode(',', $fields) . ", updated_at=NOW() WHERE id=:id")->execute($params);
        return $this->findById($id);
    }

    public function delete(int $id): void {
        $this->findById($id);
        $this->pdo->prepare("UPDATE san_pham SET active=0, deleted_at=NOW() WHERE id=?")->execute([$id]);
    }

    private function slugify(string $text): string {
        $text = iconv('UTF-8','ASCII//TRANSLIT//IGNORE',$text);
        return strtolower(trim(preg_replace('/[^a-z0-9]+/','-',$text),'-')) . '-' . substr(md5(uniqid()),0,6);
    }
}

// ── Test CRUD ─────────────────────
$repo = new ProductRepository($pdo);

// Create
try {
    $new = $repo->create(new CreateProductDTO(['ten'=>'Sản phẩm test','gia'=>299000,'so_luong'=>10,'danh_muc_id'=>1]));
    echo "✅ Tạo: {$new['ten']} (#{$new['id']})<br>";

    // Read
    $found = $repo->findById($new['id']);
    echo "✅ Đọc: {$found['ten']}<br>";

    // Update
    $updated = $repo->update($new['id'], ['gia'=>399000,'so_luong'=>20]);
    echo "✅ Cập nhật: gia={$updated['gia']}, sl={$updated['so_luong']}<br>";

    // Delete
    $repo->delete($new['id']);
    echo "✅ Xóa thành công<br>";

    // 404
    $repo->findById(99999);
} catch (ValidationException $e) {
    echo "❌ Validation: " . implode(', ', $e->getErrors()) . "<br>";
} catch (NotFoundException $e) {
    echo "ℹ️  {$e->getMessage()}<br>";
}

// List + pagination
$list = $repo->findAll(1, 3);
echo "<br>Danh sách (tổng {$list['total']}):<br>";
foreach ($list['items'] as $sp) echo "• {$sp['ten']}: " . number_format($sp['gia'],0,',','.') . "đ<br>";"""
  ),
  (14, "Tối Ưu Hiệu Năng – Index và Query Optimization",
   "Tối ưu hiệu năng database với indexes, EXPLAIN và các kỹ thuật query tốt hơn.",
   ["Tạo index đơn và composite index",
    "Dùng EXPLAIN để phân tích query plan",
    "Tránh N+1 query problem",
    "Eager loading với JOIN thay vì nhiều query",
    "Query caching và connection pooling"],
   ["Index: cấu trúc dữ liệu tăng tốc SELECT nhưng chậm INSERT/UPDATE",
    "<code>EXPLAIN SELECT ...</code>: hiển thị query execution plan",
    "<code>type: ALL</code> trong EXPLAIN = full table scan (xấu); <code>ref</code> hay <code>const</code> = dùng index (tốt)",
    "N+1 problem: loop 100 sản phẩm, mỗi cái query thêm → 101 queries; Eager load = 2 queries",
    "Composite index: <code>INDEX(col1, col2)</code> – thứ tự column quan trọng"],
   """\
<?php
$pdo = get_pdo();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. Tạo Indexes
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Single column index
try {
    $pdo->exec("CREATE INDEX idx_sp_gia ON san_pham(gia)");
    $pdo->exec("CREATE INDEX idx_sp_active ON san_pham(active)");
    // Composite index (thường dùng cùng nhau)
    $pdo->exec("CREATE INDEX idx_sp_active_gia ON san_pham(active, gia)");
    // Full-text index cho tìm kiếm
    $pdo->exec("CREATE FULLTEXT INDEX ft_sp_ten ON san_pham(ten)");
    echo "✅ Indexes tạo thành công<br>";
} catch (PDOException $e) { echo "Index đã tồn tại hoặc lỗi: {$e->getMessage()}<br>"; }

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. EXPLAIN phân tích query
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$explain = $pdo->query("EXPLAIN SELECT * FROM san_pham WHERE active=1 AND gia BETWEEN 100000 AND 500000")->fetchAll();
echo "<br>EXPLAIN kết quả:<br>";
foreach ($explain as $row) {
    echo "type={$row['type']} | possible_keys={$row['possible_keys']} | key={$row['key']} | rows={$row['rows']}<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. N+1 Problem – BẬY ĐỪNG LÀM
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ❌ BAD: N+1 – 1 query lấy SP, N query lấy danh mục
$bad_start = microtime(true);
$sps = $pdo->query("SELECT id, ten, danh_muc_id FROM san_pham WHERE active=1 LIMIT 8")->fetchAll();
foreach ($sps as &$sp) {
    // 1 query mỗi sản phẩm để lấy danh mục ← N+1!
    $dm = $pdo->prepare("SELECT ten FROM danh_muc WHERE id = ?");
    $dm->execute([$sp['danh_muc_id']]);
    $sp['danh_muc'] = $dm->fetchColumn();
}
$bad_ms = round((microtime(true)-$bad_start)*1000, 2);

// ✅ GOOD: JOIN – chỉ 1 query
$good_start = microtime(true);
$sps_good = $pdo->query("
    SELECT sp.id, sp.ten, dm.ten AS danh_muc
    FROM san_pham sp
    LEFT JOIN danh_muc dm ON dm.id = sp.danh_muc_id
    WHERE sp.active = 1 LIMIT 8
")->fetchAll();
$good_ms = round((microtime(true)-$good_start)*1000, 2);

echo "<br>N+1: {$bad_ms}ms | JOIN: {$good_ms}ms<br>";
echo "JOIN " . ($bad_ms > $good_ms ? "nhanh hơn" : "tương đương") . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. Full-text search (nếu có FT index)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
try {
    $ft = $pdo->prepare("SELECT ten, MATCH(ten) AGAINST(? IN BOOLEAN MODE) AS score FROM san_pham WHERE MATCH(ten) AGAINST(? IN BOOLEAN MODE) ORDER BY score DESC LIMIT 5");
    $ft->execute(['áo*', 'áo*']);
    echo "<br>Full-text 'áo':<br>";
    foreach ($ft->fetchAll() as $sp) {
        echo "→ {$sp['ten']} (score: {$sp['score']})<br>";
    }
} catch (PDOException $e) { echo "Full-text: {$e->getMessage()}<br>"; }"""
  ),
  (15, "Project Mini – Hệ Thống Quản Lý Sản Phẩm Hoàn Chỉnh",
   "Kết hợp tất cả kiến thức để xây dựng hệ thống quản lý sản phẩm đầy đủ.",
   ["Kiến trúc MVC đầy đủ: Router, Controller, Model, View",
    "CRUD sản phẩm với upload ảnh",
    "Tìm kiếm + lọc + phân trang",
    "Authentication bảo vệ admin",
    "Dashboard thống kê"],
   ["Đây là bài tổng hợp – áp dụng tất cả kiến thức Module 3",
    "Cấu trúc thư mục: config/, src/{Controller,Model,View}, public/",
    "htaccess rewrite: mọi request → index.php để router xử lý",
    "Security checklist: PDO prepared stmt, password_hash, CSRF token, input validation",
    "Deploy: cấu hình .env cho production, tắt error display"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Cấu trúc project hoàn chỉnh
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// shop/
// ├── config/
// │   ├── database.php    (PDO connection)
// │   └── app.php         (constants, helpers)
// ├── src/
// │   ├── Model/
// │   │   ├── BaseModel.php
// │   │   ├── Product.php
// │   │   ├── Category.php
// │   │   └── User.php
// │   ├── Controller/
// │   │   ├── BaseController.php
// │   │   ├── ProductController.php
// │   │   ├── AuthController.php
// │   │   └── DashboardController.php
// │   ├── View/
// │   │   ├── layouts/main.php
// │   │   ├── products/index.php
// │   │   ├── products/form.php
// │   │   └── auth/login.php
// │   ├── Middleware/
// │   │   ├── AuthMiddleware.php
// │   │   └── CsrfMiddleware.php
// │   └── Router.php
// ├── public/
// │   ├── index.php       (entry point)
// │   ├── .htaccess
// │   └── uploads/
// └── composer.json

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// public/.htaccess
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Options -Indexes
// RewriteEngine On
// RewriteCond %{REQUEST_FILENAME} !-f
// RewriteCond %{REQUEST_FILENAME} !-d
// RewriteRule ^ index.php [L]

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// CSRF Protection
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function csrf_token(): string {
    if (empty($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }
    return $_SESSION['csrf_token'];
}
function csrf_verify(): void {
    if (($_POST['_token'] ?? '') !== ($_SESSION['csrf_token'] ?? '')) {
        http_response_code(419); die("CSRF token mismatch");
    }
}
// Trong form HTML: <input type="hidden" name="_token" value="<?= csrf_token() ?>">

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Dashboard Controller
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function dashboard_stats(PDO $pdo): array {
    return [
        'tong_sp'    => $pdo->query("SELECT COUNT(*) FROM san_pham WHERE active=1")->fetchColumn(),
        'tong_dm'    => $pdo->query("SELECT COUNT(*) FROM danh_muc WHERE active=1")->fetchColumn(),
        'sp_het_hang'=> $pdo->query("SELECT COUNT(*) FROM san_pham WHERE so_luong=0 AND active=1")->fetchColumn(),
        'sp_khuyen_mai' => $pdo->query("SELECT COUNT(*) FROM san_pham WHERE gia_km IS NOT NULL AND active=1")->fetchColumn(),
        'gia_tri_kho'=> $pdo->query("SELECT COALESCE(SUM(gia*so_luong),0) FROM san_pham WHERE active=1")->fetchColumn(),
        'top_san_pham'=> $pdo->query("SELECT ten, luot_xem FROM san_pham WHERE active=1 ORDER BY luot_xem DESC LIMIT 5")->fetchAll(),
    ];
}

$pdo = get_pdo();
$stats = dashboard_stats($pdo);

echo "=== DASHBOARD ===<br>";
echo "Tổng SP: {$stats['tong_sp']} | Danh mục: {$stats['tong_dm']}<br>";
echo "Hết hàng: {$stats['sp_het_hang']} | KM: {$stats['sp_khuyen_mai']}<br>";
echo "Giá trị kho: " . number_format($stats['gia_tri_kho'],0,',','.') . "đ<br>";
echo "<br>Top sản phẩm:<br>";
foreach ($stats['top_san_pham'] as $sp) echo "• {$sp['ten']}: {$sp['luot_xem']} lượt<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Security Checklist
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo "<br>=== Security Checklist ===<br>";
$checks = [
    'PDO Prepared Statements' => true,
    'password_hash() + verify()' => true,
    'CSRF Token trong form'    => true,
    'Input validation (filter_var)' => true,
    'File type validation (finfo)' => true,
    'SQL Column whitelist'     => true,
    'Session regenerate on login' => true,
    'Error display off (production)' => ini_get('display_errors') === '0',
    'HTTPS redirect (.htaccess)' => true,
];
foreach ($checks as $item => $ok) {
    echo ($ok ? '✅' : '⚠️ ') . " $item<br>";
}"""
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
    code_esc = code.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{short}">
  <meta name="author" content="Dương Nguyễn Phú Cường">
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Bài {n:02d} – {title} | NenTang.vn">
  <meta property="og:url" content="https://nentang.vn/">
  <meta property="og:site_name" content="Nền tảng Kiến thức">
  <title>Bài {n:02d} – {title} | NenTang.vn</title>
  <link rel="stylesheet" href="../../shared.css" />
</head>
<body>
  <div class="page-header module-php-3">
    <div class="breadcrumb">
      <a href="../../index.html">PHP Course</a> &rsaquo;
      <a href="../index.html">Module 3</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 3 – PHP &amp; MySQL Thực Chiến</p>
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
  <a href="../index.html" class="btn-back">&#8592; Quay lại Module 3</a>
{SHIKI_SCRIPT}
</body>
</html>"""

created = 0
for ex in EXERCISES:
    n, title, short, reqs, knows, code = ex
    folder = MOD / f"bai-{n:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(build(n,title,short,reqs,knows,code), encoding="utf-8")
    print(f"  ✓ bai-{n:02d}: {title}")
    created += 1

print(f"\n✅ Module 3 PHP: {created} bài tạo thành công tại {MOD}")
