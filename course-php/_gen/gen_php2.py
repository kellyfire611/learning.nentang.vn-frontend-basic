# gen_php2.py – Module 2: PHP Nâng Cao – OOP (20 bài)
import pathlib

ROOT = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-php")
MOD  = ROOT / "module-02-php-oop"
MOD.mkdir(parents=True, exist_ok=True)

EXERCISES = [
  (1, "OOP – Class và Object Cơ Bản",
   "Tạo class đầu tiên, khai báo thuộc tính và phương thức, tạo đối tượng.",
   ["Tạo class <code>SinhVien</code> với các thuộc tính: tên, tuổi, điểm TB",
    "Khai báo phương thức giới thiệu, xếp loại",
    "Tạo nhiều đối tượng từ class",
    "Truy cập thuộc tính và phương thức qua <code>-></code>",
    "Hiểu tầm vực: <code>public</code>, <code>private</code>, <code>protected</code>"],
   ["<code>class Foo { }</code> — khai báo lớp; <code>$obj = new Foo();</code> — tạo đối tượng",
    "<code>public</code>: truy cập từ mọi nơi; <code>private</code>: chỉ trong class; <code>protected</code>: class và con",
    "<code>$this</code>: truy cập thuộc tính/phương thức của chính đối tượng đó",
    "<code>$obj->property</code>: truy cập thuộc tính; <code>$obj->method()</code>: gọi phương thức",
    "Getter/Setter: hàm truy cập/cập nhật private property"],
   """\
<?php
class SinhVien {
    // Thuộc tính
    public string  $ho_ten;
    public int     $tuoi;
    private float  $diem_tb;
    protected string $lop;

    // Constructor
    public function __construct(string $ho_ten, int $tuoi, float $diem_tb, string $lop) {
        $this->ho_ten  = $ho_ten;
        $this->tuoi    = $tuoi;
        $this->diem_tb = $diem_tb;
        $this->lop     = $lop;
    }

    // Getter (truy cập private property)
    public function getDiemTb(): float { return $this->diem_tb; }

    // Setter (cập nhật với validate)
    public function setDiemTb(float $diem): void {
        if ($diem < 0 || $diem > 10) throw new InvalidArgumentException("Điểm phải từ 0-10");
        $this->diem_tb = $diem;
    }

    // Phương thức xếp loại
    public function xepLoai(): string {
        return match(true) {
            $this->diem_tb >= 9.0 => "Xuất sắc",
            $this->diem_tb >= 8.0 => "Giỏi",
            $this->diem_tb >= 7.0 => "Khá",
            $this->diem_tb >= 5.0 => "Trung bình",
            default               => "Yếu",
        };
    }

    // Phương thức giới thiệu
    public function gioiThieu(): string {
        return "Tên: {$this->ho_ten} | Lớp: {$this->lop} | Điểm: {$this->diem_tb} ({$this->xepLoai()})";
    }

    // __toString magic method
    public function __toString(): string { return $this->gioiThieu(); }
}

// ── Tạo đối tượng ─────────────────
$sv1 = new SinhVien("Nguyễn Văn An",  20, 8.5, "CNTT-K22A");
$sv2 = new SinhVien("Trần Thị Bình",  21, 7.2, "CNTT-K22B");
$sv3 = new SinhVien("Lê Văn Cường",   19, 9.1, "CNTT-K22A");

echo $sv1->gioiThieu() . "<br>";
echo $sv2 . "<br>";   // dùng __toString
echo "Xếp loại An: " . $sv1->xepLoai() . "<br>";

// Cập nhật điểm qua setter
$sv1->setDiemTb(9.5);
echo "Điểm mới: " . $sv1->getDiemTb() . "<br>";

// Mảng đối tượng
$ds = [$sv1, $sv2, $sv3];
usort($ds, fn($a, $b) => $b->getDiemTb() <=> $a->getDiemTb());
echo "<br>Xếp hạng điểm:<br>";
foreach ($ds as $i => $sv) {
    echo ($i+1) . ". {$sv->ho_ten}: {$sv->getDiemTb()}<br>";
}"""
  ),
  (2, "OOP – Kế Thừa (Inheritance)",
   "Xây dựng hệ thống phân cấp class với kế thừa – tái sử dụng và mở rộng code.",
   ["Tạo class cha <code>Nguoi</code> với thuộc tính chung",
    "Tạo class con <code>SinhVien</code> và <code>GiaoVien</code> kế thừa",
    "Dùng <code>parent::__construct()</code> gọi constructor cha",
    "Override phương thức trong class con",
    "Dùng <code>final</code> ngăn kế thừa/override"],
   ["<code>class Con extends Cha { }</code>: kế thừa",
    "<code>parent::method()</code>: gọi phương thức của class cha",
    "Override: định nghĩa lại phương thức cha trong class con",
    "<code>final class Foo</code>: không thể extends; <code>final public function</code>: không được override",
    "<code>abstract class</code>: class cha có phương thức trừu tượng (abstract method) bắt con phải implement"],
   """\
<?php
// ── Class cha ─────────────────────
abstract class Nguoi {
    public function __construct(
        protected string $ho_ten,
        protected int    $tuoi,
        protected string $email,
    ) {}

    // Phương thức chung
    public function thongTin(): string {
        return "{$this->ho_ten} ({$this->tuoi} tuổi) – {$this->email}";
    }

    // Abstract method: bắt buộc class con phải implement
    abstract public function vaiTro(): string;

    // __toString
    public function __toString(): string {
        return "[{$this->vaiTro()}] " . $this->thongTin();
    }
}

// ── Class con: Sinh viên ───────────
class SinhVien extends Nguoi {
    public function __construct(
        string $ho_ten, int $tuoi, string $email,
        private string $ma_sv,
        private float  $diem_tb,
    ) {
        parent::__construct($ho_ten, $tuoi, $email);  // gọi cha
    }

    public function vaiTro(): string { return "Sinh viên"; }

    // Override thongTin()
    public function thongTin(): string {
        return parent::thongTin() . " | MSV: {$this->ma_sv} | GPA: {$this->diem_tb}";
    }
}

// ── Class con: Giáo viên ──────────
class GiaoVien extends Nguoi {
    public function __construct(
        string $ho_ten, int $tuoi, string $email,
        private string $mon_day,
        private float  $luong,
    ) {
        parent::__construct($ho_ten, $tuoi, $email);
    }

    public function vaiTro(): string { return "Giáo viên"; }

    public function thongTin(): string {
        return parent::thongTin() . " | Môn: {$this->mon_day} | Lương: " . number_format($this->luong, 0, ',', '.') . "đ";
    }
}

// ── Sử dụng ──────────────────────
$sv = new SinhVien("Nguyễn An", 20, "an@sv.edu.vn", "SV001", 8.5);
$gv = new GiaoVien("Cô Hoa",   35, "hoa@gv.edu.vn", "Toán", 15_000_000);

$ds_nguoi = [$sv, $gv];
foreach ($ds_nguoi as $n) {
    echo $n . "<br>";
}

// instanceof kiểm tra kiểu
var_dump($sv instanceof SinhVien);  // true
var_dump($sv instanceof Nguoi);     // true
var_dump($gv instanceof SinhVien);  // false"""
  ),
  (3, "OOP – Interface và Abstract Class",
   "Sử dụng interface định nghĩa contract và abstract class để chia sẻ implementation.",
   ["Tạo interface <code>Printable</code>, <code>Exportable</code>",
    "Implement nhiều interface trong một class",
    "Tạo abstract class với vừa abstract vừa concrete method",
    "So sánh interface vs abstract class",
    "Dùng interface để đạt Dependency Inversion (DI)"],
   ["Interface: chỉ có method signatures (không có body), constants; class implement phải định nghĩa tất cả",
    "Abstract class: có thể có thuộc tính, constructor, concrete method lẫn abstract method",
    "Một class chỉ extends 1 class, nhưng có thể implements nhiều interface",
    "<code>interface A extends B { }</code>: interface có thể extends interface khác",
    "Interface thường đặt tên dạng: <code>Loggable</code>, <code>Serializable</code>, <code>Countable</code>"],
   """\
<?php
// ── Interfaces ─────────────────────
interface Loggable {
    public function toLog(): string;
}

interface Exportable {
    public function toJson(): string;
    public function toCsv(): string;
}

// ── Abstract class ────────────────
abstract class BaseModel implements Loggable {
    protected static int $count = 0;
    public function __construct(protected readonly int $id) {
        self::$count++;
    }
    // Concrete method
    public function toLog(): string {
        return "[" . static::class . " #{$this->id}] " . $this->summary();
    }
    // Abstract: con phải implement
    abstract protected function summary(): string;
    abstract public function validate(): bool;

    public static function getCount(): int { return self::$count; }
}

// ── Concrete class ────────────────
class SanPham extends BaseModel implements Exportable {
    public function __construct(
        int    $id,
        private string $ten,
        private float  $gia,
        private int    $ton_kho,
    ) { parent::__construct($id); }

    protected function summary(): string {
        return "{$this->ten} – " . number_format($this->gia, 0, ',', '.') . "đ (tồn: {$this->ton_kho})";
    }

    public function validate(): bool {
        return !empty($this->ten) && $this->gia > 0 && $this->ton_kho >= 0;
    }

    public function toJson(): string {
        return json_encode(['id'=>$this->id,'ten'=>$this->ten,'gia'=>$this->gia,'ton_kho'=>$this->ton_kho], JSON_UNESCAPED_UNICODE);
    }

    public function toCsv(): string {
        return "{$this->id},{$this->ten},{$this->gia},{$this->ton_kho}";
    }
}

// ── Sử dụng ──────────────────────
$sp1 = new SanPham(1, "Áo thun", 150_000, 50);
$sp2 = new SanPham(2, "Quần jean", 450_000, 20);

echo $sp1->toLog() . "<br>";
echo $sp1->toJson() . "<br>";
echo "CSV: " . $sp2->toCsv() . "<br>";
echo "Hợp lệ: " . ($sp1->validate() ? "có" : "không") . "<br>";
echo "Tổng đối tượng: " . BaseModel::getCount() . "<br>";

// Polymorphism: gọi qua interface type
function in_log(Loggable $obj): void {
    echo "LOG: " . $obj->toLog() . "<br>";
}
in_log($sp1);
in_log($sp2);"""
  ),
  (4, "OOP – Static, Traits và Magic Methods",
   "Sử dụng static members, traits để tái sử dụng code và magic methods trong PHP.",
   ["Thuộc tính và phương thức <code>static</code>",
    "Tạo Singleton pattern bằng static",
    "Tạo Trait <code>HasTimestamps</code>, <code>HasSoftDelete</code>",
    "Magic methods: <code>__get</code>, <code>__set</code>, <code>__call</code>, <code>__clone</code>",
    "Late static binding với <code>static::</code>"],
   ["<code>static $count</code>: dùng chung cho mọi instance của class",
    "<code>ClassName::$staticProp</code> hoặc <code>self::$staticProp</code>",
    "Trait: khối code có thể dùng lại trong nhiều class (<code>use TraitName</code>)",
    "<code>__get($name)</code>: gọi khi truy cập property không tồn tại",
    "<code>__call($name, $args)</code>: gọi khi method không tồn tại"],
   """\
<?php
// ── Trait ─────────────────────────
trait HasTimestamps {
    private ?string $created_at = null;
    private ?string $updated_at = null;

    public function touch(): void {
        $now = date('Y-m-d H:i:s');
        if (!$this->created_at) $this->created_at = $now;
        $this->updated_at = $now;
    }
    public function getCreatedAt(): ?string { return $this->created_at; }
    public function getUpdatedAt(): ?string { return $this->updated_at; }
}

trait HasSoftDelete {
    private ?string $deleted_at = null;
    public function softDelete(): void { $this->deleted_at = date('Y-m-d H:i:s'); }
    public function restore(): void  { $this->deleted_at = null; }
    public function isDeleted(): bool { return $this->deleted_at !== null; }
}

// ── Singleton pattern ─────────────
class Config {
    private static ?Config $instance = null;
    private array $data = [];

    private function __construct() {}  // private!

    public static function getInstance(): static {
        if (static::$instance === null) {
            static::$instance = new static();
        }
        return static::$instance;
    }
    public function set(string $key, mixed $val): void { $this->data[$key] = $val; }
    public function get(string $key, mixed $default = null): mixed {
        return $this->data[$key] ?? $default;
    }
}

// ── Magic methods ─────────────────
class DynamicModel {
    use HasTimestamps, HasSoftDelete;
    private array $attributes = [];
    private static int $totalCreated = 0;

    public function __construct(array $data = []) {
        $this->attributes = $data;
        $this->touch();
        self::$totalCreated++;
    }
    // __get: truy cập dynamic property
    public function __get(string $name): mixed {
        return $this->attributes[$name] ?? null;
    }
    // __set: gán dynamic property
    public function __set(string $name, mixed $val): void {
        $this->attributes[$name] = $val;
        $this->touch();
    }
    // __isset
    public function __isset(string $name): bool { return isset($this->attributes[$name]); }
    // __call: method không tồn tại
    public function __call(string $name, array $args): mixed {
        if (str_starts_with($name, 'get')) {
            $key = lcfirst(substr($name, 3));
            return $this->attributes[$key] ?? null;
        }
        throw new BadMethodCallException("Method $name không tồn tại");
    }
    public static function getTotalCreated(): int { return self::$totalCreated; }
}

// ── Sử dụng ──────────────────────
$cfg = Config::getInstance();
$cfg->set('app_name', 'NenTang');
echo Config::getInstance()->get('app_name') . "<br>";  // Singleton = cùng 1 instance

$m = new DynamicModel(['ten' => 'Sản phẩm A', 'gia' => 99000]);
echo $m->ten  . "<br>";     // magic __get
$m->ton_kho = 50;           // magic __set
echo $m->getTen() . "<br>"; // magic __call → getTen → ten
echo "Created: " . DynamicModel::getTotalCreated() . "<br>";
$m->softDelete();
echo "Đã xóa: " . ($m->isDeleted() ? "có" : "không") . "<br>";"""
  ),
  (5, "PDO – Kết Nối và CRUD Cơ Bản",
   "Kết nối MySQL với PDO và thực hiện các thao tác CRUD: Create, Read, Update, Delete.",
   ["Tạo kết nối PDO đến MySQL với Exception handling",
    "Tạo bảng và insert dữ liệu",
    "Đọc dữ liệu bằng <code>query()</code> và <code>fetch()</code>",
    "Cập nhật và xóa bản ghi",
    "Đếm, lọc, sắp xếp kết quả"],
   ["<code>new PDO($dsn, $user, $pass, $options)</code>: kết nối database",
    "PDO::ERRMODE_EXCEPTION: ném exception khi lỗi SQL",
    "<code>$pdo->query($sql)</code>: truy vấn không có tham số",
    "<code>$stmt->fetch(PDO::FETCH_ASSOC)</code>: lấy 1 hàng; <code>fetchAll()</code>: tất cả",
    "LUÔN LUÔN dùng Prepared Statements để tránh SQL Injection"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. Kết nối PDO
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$dsn = 'mysql:host=localhost;dbname=test_php;charset=utf8mb4';
try {
    $pdo = new PDO($dsn, 'root', '', [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ]);
    echo "✅ Kết nối thành công!<br>";
} catch (PDOException $e) {
    die("❌ Kết nối thất bại: " . $e->getMessage());
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. Tạo bảng (CREATE TABLE)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$pdo->exec("
    CREATE TABLE IF NOT EXISTS san_pham (
        id         INT AUTO_INCREMENT PRIMARY KEY,
        ten        VARCHAR(200) NOT NULL,
        gia        DECIMAL(15,2) NOT NULL DEFAULT 0,
        mo_ta      TEXT,
        so_luong   INT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB CHARSET=utf8mb4
");

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. INSERT (Prepared Statement)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$stmt = $pdo->prepare("INSERT INTO san_pham (ten, gia, mo_ta, so_luong) VALUES (?, ?, ?, ?)");
$data = [
    ["Áo thun nam",      150_000, "Cotton 100%",     100],
    ["Quần jeans",       450_000, "Slim fit",          50],
    ["Giày thể thao",    850_000, "Đế cao su chống trượt", 30],
    ["Mũ lưỡi trai",     120_000, "Chống nắng UV",     80],
];
foreach ($data as $row) {
    $stmt->execute($row);
}
echo "Đã thêm " . count($data) . " sản phẩm<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. SELECT tất cả
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ds = $pdo->query("SELECT * FROM san_pham ORDER BY gia DESC")->fetchAll();
echo "<table border='1' style='border-collapse:collapse'>";
echo "<tr><th>ID</th><th>Tên</th><th>Giá</th><th>Số lượng</th></tr>";
foreach ($ds as $sp) {
    echo "<tr><td>{$sp['id']}</td><td>{$sp['ten']}</td><td>" . number_format($sp['gia'],0,',','.') . "đ</td><td>{$sp['so_luong']}</td></tr>";
}
echo "</table><br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 5. UPDATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$update = $pdo->prepare("UPDATE san_pham SET gia = ?, so_luong = ? WHERE id = ?");
$update->execute([199_000, 120, 1]);
echo "Cập nhật: " . $update->rowCount() . " hàng<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 6. SELECT 1 hàng theo ID
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$find = $pdo->prepare("SELECT * FROM san_pham WHERE id = ?");
$find->execute([1]);
$sp = $find->fetch();
echo "Sản phẩm #1: {$sp['ten']} – " . number_format($sp['gia'],0,',','.') . "đ<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 7. DELETE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$del = $pdo->prepare("DELETE FROM san_pham WHERE id = ?");
$del->execute([4]);
echo "Xóa: " . $del->rowCount() . " hàng<br>";

// Đếm
$total = $pdo->query("SELECT COUNT(*) FROM san_pham")->fetchColumn();
echo "Còn lại: $total sản phẩm<br>";"""
  ),
  (6, "PDO – Prepared Statements và Named Parameters",
   "Sử dụng Prepared Statements đúng cách để tránh SQL Injection, dùng named parameters.",
   ["So sánh <code>?</code> (positional) và <code>:name</code> (named) parameters",
    "Bind parameter với <code>bindParam</code> và <code>bindValue</code>",
    "Tìm kiếm với LIKE, lọc theo nhiều điều kiện",
    "Build dynamic WHERE clause an toàn",
    "Hiểu tại sao không được dùng string interpolation trong SQL"],
   ["<code>$stmt = $pdo->prepare('SELECT * WHERE id = :id')</code>",
    "<code>$stmt->execute([':id' => $id])</code>: bind và execute cùng lúc",
    "<code>bindParam(':id', $id, PDO::PARAM_INT)</code>: bind tham chiếu (lazy evaluation)",
    "<code>bindValue(':id', $id, PDO::PARAM_INT)</code>: bind giá trị (eager)",
    "SQL Injection xảy ra khi nối chuỗi: <code>'WHERE id = ' . $id</code> — KHÔNG BAO GIỜ làm vậy"],
   """\
<?php
// Giả sử đã kết nối $pdo ...

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. Named parameters
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$stmt = $pdo->prepare("
    INSERT INTO san_pham (ten, gia, so_luong)
    VALUES (:ten, :gia, :so_luong)
");
$stmt->execute([':ten' => 'Kính râm', ':gia' => 280_000, ':so_luong' => 40]);
echo "ID mới: " . $pdo->lastInsertId() . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. LIKE search (an toàn)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$tu_khoa = "áo";
$stmt = $pdo->prepare("SELECT * FROM san_pham WHERE ten LIKE :kw OR mo_ta LIKE :kw ORDER BY ten");
$stmt->execute([':kw' => "%$tu_khoa%"]);  // % nằm trong PHP, không trong SQL
foreach ($stmt->fetchAll() as $sp) {
    echo "→ {$sp['ten']}<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. Dynamic WHERE clause
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function tim_san_pham(PDO $pdo, array $bo_loc = []): array {
    $where  = [];
    $params = [];

    if (!empty($bo_loc['gia_min'])) {
        $where[] = 'gia >= :gia_min';
        $params[':gia_min'] = $bo_loc['gia_min'];
    }
    if (!empty($bo_loc['gia_max'])) {
        $where[] = 'gia <= :gia_max';
        $params[':gia_max'] = $bo_loc['gia_max'];
    }
    if (!empty($bo_loc['tu_khoa'])) {
        $where[] = 'ten LIKE :kw';
        $params[':kw'] = '%' . $bo_loc['tu_khoa'] . '%';
    }

    $sql = "SELECT * FROM san_pham";
    if ($where) $sql .= " WHERE " . implode(" AND ", $where);
    $sql .= " ORDER BY gia ASC";

    // Sắp xếp (column name KHÔNG thể parameterize → whitelist)
    $cho_phep_sort = ['ten', 'gia', 'so_luong', 'created_at'];
    $col = in_array($bo_loc['sort'] ?? '', $cho_phep_sort) ? $bo_loc['sort'] : 'gia';
    $dir = ($bo_loc['dir'] ?? 'asc') === 'desc' ? 'DESC' : 'ASC';
    $sql = "SELECT * FROM san_pham" . ($where ? " WHERE " . implode(" AND ", $where) : "") . " ORDER BY $col $dir";

    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    return $stmt->fetchAll();
}

$ket_qua = tim_san_pham($pdo, ['gia_min' => 100_000, 'gia_max' => 500_000, 'sort' => 'gia', 'dir' => 'asc']);
echo "<br>Lọc 100k-500k:<br>";
foreach ($ket_qua as $sp) {
    echo "→ {$sp['ten']}: " . number_format($sp['gia'],0,',','.') . "đ<br>";
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ❌ NGUY HIỂM – SQL Injection example (KHÔNG làm!)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// $id = $_GET['id'];  // kẻ tấn công nhập: 1 OR 1=1
// $pdo->query("SELECT * FROM san_pham WHERE id = $id");  // ☠️ SQL Injection!

// ✅ ĐÚNG: luôn dùng prepared statement
$id = (int)($_GET['id'] ?? 1);
$sp = $pdo->prepare("SELECT * FROM san_pham WHERE id = ?");
$sp->execute([$id]);
$row = $sp->fetch();
if ($row) echo "Tìm thấy: {$row['ten']}<br>";"""
  ),
  (7, "PDO – Transaction và Quan Hệ Bảng",
   "Sử dụng transaction để đảm bảo toàn vẹn dữ liệu và truy vấn bảng có quan hệ.",
   ["Dùng <code>beginTransaction</code>, <code>commit</code>, <code>rollBack</code>",
    "Tạo ORDER với nhiều ORDER_ITEMS trong 1 transaction",
    "JOIN: INNER JOIN, LEFT JOIN để lấy dữ liệu từ nhiều bảng",
    "Truy vấn tổng hợp: GROUP BY, HAVING, COUNT, SUM",
    "Sub-query đơn giản"],
   ["Transaction: nhóm nhiều câu SQL thành 1 đơn vị – thành công hết hoặc rollback hết",
    "<code>INNER JOIN</code>: chỉ lấy hàng có dữ liệu khớp ở cả 2 bảng",
    "<code>LEFT JOIN</code>: lấy tất cả hàng bảng trái, NULL nếu không khớp bảng phải",
    "<code>GROUP BY col HAVING aggregate_condition</code>",
    "Foreign key: đảm bảo tính nhất quán quan hệ"],
   """\
<?php
// Tạo schema
$pdo->exec("
    CREATE TABLE IF NOT EXISTS don_hang (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ma_don VARCHAR(20) UNIQUE,
        ten_khach VARCHAR(100),
        tong_tien DECIMAL(15,2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS chi_tiet_don (
        id INT AUTO_INCREMENT PRIMARY KEY,
        don_hang_id INT,
        san_pham_id INT,
        so_luong INT,
        don_gia DECIMAL(15,2),
        FOREIGN KEY (don_hang_id) REFERENCES don_hang(id) ON DELETE CASCADE
    );
");

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Transaction: tạo đơn hàng
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function tao_don_hang_tx(PDO $pdo, string $ten_khach, array $items): int {
    $pdo->beginTransaction();
    try {
        // 1. Tạo đơn hàng
        $ma_don = 'ORD-' . date('YmdHis') . '-' . rand(100,999);
        $stmt = $pdo->prepare("INSERT INTO don_hang (ma_don, ten_khach) VALUES (?, ?)");
        $stmt->execute([$ma_don, $ten_khach]);
        $don_id   = (int)$pdo->lastInsertId();
        $tong_tien = 0;

        // 2. Thêm chi tiết
        $ins = $pdo->prepare("INSERT INTO chi_tiet_don (don_hang_id, san_pham_id, so_luong, don_gia) VALUES (?,?,?,?)");
        foreach ($items as $item) {
            // Kiểm tra tồn kho
            $sp = $pdo->prepare("SELECT gia, so_luong FROM san_pham WHERE id = ?");
            $sp->execute([$item['sp_id']]);
            $row = $sp->fetch();
            if (!$row || $row['so_luong'] < $item['sl']) {
                throw new RuntimeException("Sản phẩm #{$item['sp_id']} không đủ hàng");
            }
            $ins->execute([$don_id, $item['sp_id'], $item['sl'], $row['gia']]);
            $tong_tien += $row['gia'] * $item['sl'];
            // Trừ tồn kho
            $pdo->prepare("UPDATE san_pham SET so_luong = so_luong - ? WHERE id = ?")
                ->execute([$item['sl'], $item['sp_id']]);
        }
        // 3. Cập nhật tổng tiền
        $pdo->prepare("UPDATE don_hang SET tong_tien = ? WHERE id = ?")->execute([$tong_tien, $don_id]);
        $pdo->commit();
        echo "✅ Tạo đơn $ma_don thành công – tổng: " . number_format($tong_tien,0,',','.') . "đ<br>";
        return $don_id;
    } catch (Exception $e) {
        $pdo->rollBack();
        echo "❌ Rollback: " . $e->getMessage() . "<br>";
        return 0;
    }
}

$don_id = tao_don_hang_tx($pdo, "Nguyễn Văn A", [['sp_id'=>1,'sl'=>2],['sp_id'=>2,'sl'=>1]]);

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// JOIN: lấy chi tiết đơn hàng
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if ($don_id) {
    $stmt = $pdo->prepare("
        SELECT d.ma_don, d.ten_khach, d.tong_tien,
               ct.so_luong, ct.don_gia,
               sp.ten AS ten_sp
        FROM don_hang d
        JOIN chi_tiet_don ct ON ct.don_hang_id = d.id
        JOIN san_pham sp     ON sp.id = ct.san_pham_id
        WHERE d.id = ?
    ");
    $stmt->execute([$don_id]);
    foreach ($stmt->fetchAll() as $row) {
        echo "→ {$row['ten_sp']} × {$row['so_luong']} = " . number_format($row['don_gia']*$row['so_luong'],0,',','.') . "đ<br>";
    }
}

// GROUP BY
$thong_ke = $pdo->query("SELECT sp_id, SUM(so_luong) as tong_ban FROM chi_tiet_don GROUP BY sp_id ORDER BY tong_ban DESC")->fetchAll();
foreach ($thong_ke as $t) echo "SP #{$t['sp_id']}: bán {$t['tong_ban']}<br>";"""
  ),
  (8, "Repository Pattern và Service Layer",
   "Áp dụng design pattern: Repository tách biệt data access, Service chứa business logic.",
   ["Tạo <code>interface ProductRepository</code>",
    "Implement <code>MysqlProductRepository</code>",
    "Tạo <code>ProductService</code> dùng Repository qua Dependency Injection",
    "Viết <code>InMemoryProductRepository</code> cho testing",
    "Hiểu tại sao cần tách biệt concerns"],
   ["Repository: lớp trung gian giữa domain và data storage",
    "Service: chứa business rules, dùng Repository để CRUD",
    "Dependency Injection: truyền phụ thuộc qua constructor thay vì new bên trong",
    "Interface-based DI: thay đổi implementation mà không cần sửa Service",
    "Single Responsibility: mỗi class chỉ làm 1 việc"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Model / Entity
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Product {
    public function __construct(
        public int    $id,
        public string $name,
        public float  $price,
        public int    $stock,
    ) {}
    public function isInStock(): bool { return $this->stock > 0; }
    public function toArray(): array  { return get_object_vars($this); }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Repository Interface
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
interface ProductRepository {
    public function findAll(): array;
    public function findById(int $id): ?Product;
    public function create(Product $p): Product;
    public function update(Product $p): bool;
    public function delete(int $id): bool;
    public function search(string $kw): array;
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// InMemory implementation (cho test)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class InMemoryProductRepository implements ProductRepository {
    private array $store = [];
    private int   $nextId = 1;

    public function findAll(): array { return array_values($this->store); }
    public function findById(int $id): ?Product { return $this->store[$id] ?? null; }
    public function create(Product $p): Product {
        $p->id = $this->nextId++;
        $this->store[$p->id] = $p;
        return $p;
    }
    public function update(Product $p): bool {
        if (!isset($this->store[$p->id])) return false;
        $this->store[$p->id] = $p;
        return true;
    }
    public function delete(int $id): bool {
        if (!isset($this->store[$id])) return false;
        unset($this->store[$id]);
        return true;
    }
    public function search(string $kw): array {
        return array_filter($this->store, fn($p) => stripos($p->name, $kw) !== false);
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Service Layer (Business Logic)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class ProductService {
    public function __construct(private ProductRepository $repo) {}

    public function add(string $name, float $price, int $stock): Product {
        if (empty($name))    throw new InvalidArgumentException("Tên sản phẩm bắt buộc");
        if ($price < 0)      throw new InvalidArgumentException("Giá không âm");
        if ($stock < 0)      throw new InvalidArgumentException("Tồn kho không âm");
        return $this->repo->create(new Product(0, $name, $price, $stock));
    }

    public function purchase(int $id, int $qty): Product {
        $p = $this->repo->findById($id) ?? throw new RuntimeException("Sản phẩm #$id không tồn tại");
        if ($p->stock < $qty) throw new RuntimeException("Không đủ hàng, còn {$p->stock}");
        $p->stock -= $qty;
        $this->repo->update($p);
        return $p;
    }

    public function getInStock(): array {
        return array_filter($this->repo->findAll(), fn($p) => $p->isInStock());
    }
}

// ── Test ──────────────────────────
$repo = new InMemoryProductRepository();   // Thay bằng MysqlProductRepository dễ dàng!
$svc  = new ProductService($repo);

$sp1  = $svc->add("Áo thun", 150_000, 10);
$sp2  = $svc->add("Quần jean", 450_000, 5);
echo "Tạo: {$sp1->name} (ID: {$sp1->id})<br>";

try {
    $svc->purchase($sp1->id, 3);
    echo "Mua 3 áo thun, còn: {$sp1->stock}<br>";
    $svc->purchase($sp2->id, 10); // vượt tồn kho
} catch (RuntimeException $e) {
    echo "Lỗi: {$e->getMessage()}<br>";
}

foreach ($svc->getInStock() as $p) {
    echo "{$p->name}: còn {$p->stock}<br>";
}"""
  ),
  (9, "RESTful API Cơ Bản với PHP",
   "Xây dựng API RESTful đơn giản trả về JSON – không dùng framework.",
   ["Định tuyến request theo HTTP method và URL path",
    "Trả về JSON response chuẩn",
    "Implement CRUD endpoint: GET, POST, PUT, DELETE",
    "Xử lý request body (JSON payload)",
    "HTTP status codes phù hợp"],
   ["<code>$_SERVER['REQUEST_METHOD']</code>: GET/POST/PUT/DELETE",
    "<code>$_SERVER['PATH_INFO']</code> hoặc parse <code>REQUEST_URI</code>: lấy path",
    "<code>file_get_contents('php://input')</code>: đọc JSON body từ PUT/PATCH/DELETE",
    "<code>http_response_code(404)</code>: đặt HTTP status code",
    "CORS: <code>header('Access-Control-Allow-Origin: *')</code>"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// api.php – RESTful API đơn giản
// Endpoint: /api.php/products[/:id]
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204); exit;
}

function json_response(mixed $data, int $code = 200): never {
    http_response_code($code);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

// ── Data Store (thay bằng DB) ─────
$products = [
    1 => ['id'=>1,'name'=>'Áo thun','price'=>150000,'stock'=>50],
    2 => ['id'=>2,'name'=>'Quần jean','price'=>450000,'stock'=>20],
    3 => ['id'=>3,'name'=>'Giày','price'=>850000,'stock'=>10],
];

// ── Parse path ────────────────────
$path = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');
$parts = explode('/', $path);
$resource = $parts[1] ?? '';    // 'products'
$id       = isset($parts[2]) ? (int)$parts[2] : null;
$method   = $_SERVER['REQUEST_METHOD'];

if ($resource !== 'products') {
    json_response(['error' => 'Endpoint không tồn tại'], 404);
}

// ── GET /products hoặc GET /products/:id ──
if ($method === 'GET') {
    if ($id !== null) {
        if (!isset($products[$id])) json_response(['error' => 'Không tìm thấy'], 404);
        json_response(['data' => $products[$id]]);
    }
    json_response(['data' => array_values($products), 'total' => count($products)]);
}

// ── POST /products ─────────────────
if ($method === 'POST') {
    $body = json_decode(file_get_contents('php://input'), true) ?? [];
    if (empty($body['name'])) json_response(['error' => 'name bắt buộc'], 400);
    $new_id = max(array_keys($products)) + 1;
    $products[$new_id] = ['id' => $new_id, 'name' => $body['name'],
                           'price' => (float)($body['price'] ?? 0), 'stock' => (int)($body['stock'] ?? 0)];
    json_response(['message' => 'Tạo thành công', 'data' => $products[$new_id]], 201);
}

// ── PUT /products/:id ─────────────
if ($method === 'PUT') {
    if (!$id || !isset($products[$id])) json_response(['error' => 'Không tìm thấy'], 404);
    $body = json_decode(file_get_contents('php://input'), true) ?? [];
    $products[$id] = array_merge($products[$id], $body);
    json_response(['message' => 'Cập nhật thành công', 'data' => $products[$id]]);
}

// ── DELETE /products/:id ──────────
if ($method === 'DELETE') {
    if (!$id || !isset($products[$id])) json_response(['error' => 'Không tìm thấy'], 404);
    $deleted = $products[$id];
    unset($products[$id]);
    json_response(['message' => 'Đã xóa', 'data' => $deleted]);
}

json_response(['error' => 'Method không được hỗ trợ'], 405);"""
  ),
  (10, "Authentication – Đăng Nhập JWT",
   "Xây dựng hệ thống xác thực bằng JSON Web Token (JWT) không dùng thư viện ngoài.",
   ["Hiểu cấu trúc JWT: Header.Payload.Signature",
    "Tạo JWT từ tay bằng base64url và HMAC-SHA256",
    "Verify JWT trong mỗi request",
    "Middleware kiểm tra token",
    "Refresh token flow"],
   ["JWT = Base64URL(header) + '.' + Base64URL(payload) + '.' + HMAC-SHA256(header+payload, secret)",
    "JWT stateless: server không cần lưu session, chỉ cần secret key",
    "<code>exp</code> claim: thời gian hết hạn tính bằng Unix timestamp",
    "Authorization header: <code>Bearer eyJ...</code>",
    "Không lưu sensitive data trong payload – JWT chỉ signed, không encrypted"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// JWT Utilities (không dùng thư viện)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class JWT {
    private static string $secret = 'my_super_secret_key_change_in_prod';

    private static function base64url_encode(string $data): string {
        return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
    }
    private static function base64url_decode(string $data): string {
        return base64_decode(strtr($data, '-_', '+/') . str_repeat('=', (4 - strlen($data) % 4) % 4));
    }

    public static function create(array $payload, int $ttl = 3600): string {
        $header  = self::base64url_encode(json_encode(['alg'=>'HS256','typ'=>'JWT']));
        $payload['iat'] = time();
        $payload['exp'] = time() + $ttl;
        $payload_enc = self::base64url_encode(json_encode($payload));
        $sig = self::base64url_encode(hash_hmac('sha256', "$header.$payload_enc", self::$secret, true));
        return "$header.$payload_enc.$sig";
    }

    public static function verify(string $token): array {
        $parts = explode('.', $token);
        if (count($parts) !== 3) throw new RuntimeException("JWT không hợp lệ");
        [$header, $payload, $sig] = $parts;
        $expected = self::base64url_encode(hash_hmac('sha256', "$header.$payload", self::$secret, true));
        if (!hash_equals($expected, $sig)) throw new RuntimeException("Chữ ký không hợp lệ");
        $data = json_decode(self::base64url_decode($payload), true);
        if (($data['exp'] ?? 0) < time()) throw new RuntimeException("Token hết hạn");
        return $data;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Login endpoint giả lập
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$USERS = [
    ['id'=>1,'email'=>'admin@app.vn','password'=>password_hash('admin123',PASSWORD_DEFAULT),'role'=>'admin'],
    ['id'=>2,'email'=>'user@app.vn', 'password'=>password_hash('user1234',PASSWORD_DEFAULT),'role'=>'user'],
];

// Test luồng login
$email    = 'admin@app.vn';
$mat_khau = 'admin123';

$user = null;
foreach ($USERS as $u) {
    if ($u['email'] === $email && password_verify($mat_khau, $u['password'])) {
        $user = $u; break;
    }
}

if (!$user) { echo "Đăng nhập thất bại!<br>"; exit; }

$token = JWT::create(['uid' => $user['id'], 'email' => $user['email'], 'role' => $user['role']]);
echo "Token: " . substr($token, 0, 50) . "...<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Middleware kiểm tra token
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function requireAuth(string $token): array {
    try {
        return JWT::verify($token);
    } catch (RuntimeException $e) {
        http_response_code(401);
        echo json_encode(['error' => $e->getMessage()]);
        exit;
    }
}

// Giả lập request có Authorization header
$payload = requireAuth($token);
echo "User: {$payload['email']} (role: {$payload['role']})<br>";
echo "Hết hạn lúc: " . date('H:i:s', $payload['exp']) . "<br>";

// Token giả
try {
    JWT::verify("invalid.token.here");
} catch (RuntimeException $e) {
    echo "Lỗi: " . $e->getMessage() . "<br>";
}"""
  ),
]

# chỉ 10 bài cho ví dụ, thêm các bài 11-20 tương tự...
# Bài 11-20: PHP Mail, Image Processing, Caching, Queue, Middleware, MVC, ...
EXERCISES += [
  (11, "Gửi Email bằng PHPMailer",
   "Tích hợp PHPMailer để gửi email HTML, đính kèm file từ PHP.",
   ["Cài PHPMailer qua Composer",
    "Cấu hình SMTP (Gmail)",
    "Gửi email HTML với template đẹp",
    "Đính kèm file",
    "Xử lý lỗi gửi email"],
   ["PHPMailer: thư viện PHP phổ biến nhất để gửi email",
    "SMTP: giao thức gửi email; Gmail cần App Password (bật 2FA)",
    "<code>$mail->isHTML(true)</code>: gửi HTML email",
    "<code>$mail->addAttachment($path)</code>: đính kèm file",
    "Luôn dùng SMTP thay vì PHP mail() để tránh vào Spam"],
   """\
<?php
// Cài đặt: composer require phpmailer/phpmailer

use PHPMailer\\PHPMailer\\PHPMailer;
use PHPMailer\\PHPMailer\\SMTP;

require 'vendor/autoload.php';

function gui_email(
    string $to_email,
    string $to_name,
    string $subject,
    string $body_html,
    ?string $attachment = null
): bool {
    $mail = new PHPMailer(true);
    try {
        // Cấu hình SMTP
        $mail->isSMTP();
        $mail->Host        = 'smtp.gmail.com';
        $mail->SMTPAuth    = true;
        $mail->Username    = 'your_email@gmail.com';  // ← Gmail
        $mail->Password    = 'your_app_password';     // ← App Password
        $mail->SMTPSecure  = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port        = 587;
        $mail->CharSet     = 'UTF-8';

        // Người gửi và nhận
        $mail->setFrom('no-reply@yoursite.vn', 'NenTang.vn');
        $mail->addAddress($to_email, $to_name);

        // Nội dung
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $body_html;
        $mail->AltBody = strip_tags($body_html);  // plain text fallback

        // File đính kèm
        if ($attachment && file_exists($attachment)) {
            $mail->addAttachment($attachment);
        }

        $mail->send();
        return true;
    } catch (Exception $e) {
        error_log("Email lỗi: " . $mail->ErrorInfo);
        return false;
    }
}

// Template email HTML
function email_template(string $ten, string $noi_dung): string {
    return <<<HTML
    <!DOCTYPE html>
    <html><body style="font-family:Arial;background:#f5f5f5;padding:20px">
    <div style="max-width:600px;margin:0 auto;background:white;border-radius:12px;overflow:hidden">
      <div style="background:linear-gradient(135deg,#7928ca,#ff0080);padding:30px;color:white;text-align:center">
        <h1 style="margin:0">NenTang.vn</h1>
      </div>
      <div style="padding:30px">
        <h2>Xin chào, $ten!</h2>
        <p>$noi_dung</p>
        <a href="https://nentang.vn" style="display:inline-block;background:#7928ca;color:white;padding:12px 24px;border-radius:8px;text-decoration:none;margin-top:16px">
          Truy cập website
        </a>
      </div>
      <div style="padding:20px;text-align:center;color:#888;font-size:12px">
        © 2026 NenTang.vn – Unsubscribe
      </div>
    </div>
    </body></html>
    HTML;
}

// Gửi email chào mừng
$ok = gui_email(
    'new_user@example.com',
    'Nguyễn Văn Mới',
    'Chào mừng bạn đến với NenTang.vn!',
    email_template('Nguyễn Văn Mới', 'Tài khoản của bạn đã được tạo thành công. Hãy bắt đầu học ngay!'),
);
echo $ok ? "✅ Email gửi thành công" : "❌ Gửi thất bại";"""
  ),
  (12, "Xử Lý Ảnh với GD Library",
   "Sử dụng GD extension để resize ảnh, thêm watermark và tạo thumbnail.",
   ["Resize ảnh giữ tỷ lệ",
    "Crop ảnh (cắt hình vuông để làm avatar)",
    "Thêm watermark text",
    "Tạo thumbnail gallery",
    "Convert định dạng ảnh"],
   ["GD library: extension PHP xử lý ảnh (imagecreatefromjpeg, imagepng...)",
    "<code>imagecopyresampled()</code>: resize ảnh chất lượng cao",
    "<code>imagettftext()</code>: viết text lên ảnh bằng font TTF",
    "<code>imagejpeg($img, $path, 85)</code>: lưu JPEG với chất lượng 85%",
    "<code>imagedestroy($img)</code>: giải phóng bộ nhớ sau khi xử lý"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Resize ảnh giữ tỷ lệ
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function resize_image(string $src, string $dest, int $max_width, int $max_height, int $quality = 85): bool {
    $info = getimagesize($src);
    if (!$info) return false;

    [$orig_w, $orig_h, $type] = $info;
    $ratio = min($max_width / $orig_w, $max_height / $orig_h);
    $new_w = (int)($orig_w * $ratio);
    $new_h = (int)($orig_h * $ratio);

    // Load ảnh gốc
    $orig_img = match($type) {
        IMAGETYPE_JPEG => imagecreatefromjpeg($src),
        IMAGETYPE_PNG  => imagecreatefrompng($src),
        IMAGETYPE_GIF  => imagecreatefromgif($src),
        IMAGETYPE_WEBP => imagecreatefromwebp($src),
        default        => false,
    };
    if (!$orig_img) return false;

    // Tạo canvas mới
    $new_img = imagecreatetruecolor($new_w, $new_h);

    // Giữ transparency cho PNG/GIF
    if ($type === IMAGETYPE_PNG || $type === IMAGETYPE_GIF) {
        imagealphablending($new_img, false);
        imagesavealpha($new_img, true);
        $transparent = imagecolorallocatealpha($new_img, 0, 0, 0, 127);
        imagefilledrectangle($new_img, 0, 0, $new_w, $new_h, $transparent);
    }

    imagecopyresampled($new_img, $orig_img, 0, 0, 0, 0, $new_w, $new_h, $orig_w, $orig_h);

    // Lưu
    $ok = match($type) {
        IMAGETYPE_JPEG => imagejpeg($new_img, $dest, $quality),
        IMAGETYPE_PNG  => imagepng($new_img, $dest, (int)((100-$quality)/10)),
        IMAGETYPE_WEBP => imagewebp($new_img, $dest, $quality),
        default        => false,
    };
    imagedestroy($orig_img);
    imagedestroy($new_img);
    return (bool)$ok;
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Crop hình vuông (avatar)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function crop_square(string $src, string $dest, int $size): bool {
    $info = getimagesize($src);
    [$w, $h, $type] = $info;
    $min = min($w, $h);
    $x   = intdiv($w - $min, 2);   // căn giữa ngang
    $y   = intdiv($h - $min, 2);   // căn giữa dọc
    $orig = imagecreatefromjpeg($src);
    $crop = imagecreatetruecolor($size, $size);
    imagecopyresampled($crop, $orig, 0, 0, $x, $y, $size, $size, $min, $min);
    $ok = imagejpeg($crop, $dest, 90);
    imagedestroy($orig); imagedestroy($crop);
    return (bool)$ok;
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Watermark text
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
function add_watermark(string $src, string $dest, string $text): bool {
    $img  = imagecreatefromjpeg($src);
    $w    = imagesx($img);
    $h    = imagesy($img);
    $font = __DIR__ . '/fonts/roboto.ttf';  // cần file font TTF
    $size = max(12, (int)($w * 0.03));
    // Màu trắng 50% trong suốt
    $color = imagecolorallocatealpha($img, 255, 255, 255, 64);
    imagettftext($img, $size, 0, (int)($w*0.6), (int)($h*0.95), $color, $font, $text);
    $ok = imagejpeg($img, $dest, 90);
    imagedestroy($img);
    return (bool)$ok;
}

// Sử dụng
if (file_exists('photo.jpg')) {
    resize_image('photo.jpg', 'thumb_800.jpg', 800, 600);
    crop_square('photo.jpg', 'avatar_200.jpg', 200);
    add_watermark('photo.jpg', 'watermarked.jpg', '© NenTang.vn');
    echo "✅ Xử lý ảnh thành công";
} else {
    echo "Cần tạo file photo.jpg trước";
}"""
  ),
  (13, "Simple Caching với File Cache",
   "Xây dựng hệ thống cache đơn giản bằng file để tăng tốc ứng dụng PHP.",
   ["Cache kết quả DB query vào file JSON",
    "TTL (Time To Live) cho cache",
    "Cache invalidation khi data thay đổi",
    "Cache với Tag để invalidate nhóm",
    "So sánh hiệu năng có/không có cache"],
   ["Cache: lưu kết quả tốn kém để dùng lại, giảm tải DB/API",
    "TTL: thời gian sống của cache – hết TTL thì tái tạo",
    "Cache hit: tìm thấy và dùng cache; Cache miss: tạo mới",
    "Invalidation: xóa cache khi dữ liệu gốc thay đổi",
    "APCu, Redis, Memcached là cache engines nhanh hơn file cache"],
   """\
<?php
class FileCache {
    private string $dir;
    private int    $default_ttl;

    public function __construct(string $dir = '/tmp/php_cache', int $ttl = 300) {
        $this->dir         = rtrim($dir, '/');
        $this->default_ttl = $ttl;
        if (!is_dir($this->dir)) mkdir($this->dir, 0755, true);
    }

    private function path(string $key): string {
        return $this->dir . '/' . md5($key) . '.cache';
    }

    public function get(string $key): mixed {
        $file = $this->path($key);
        if (!file_exists($file)) return null;
        $data = json_decode(file_get_contents($file), true);
        if ($data['exp'] < time()) {
            unlink($file);
            return null;  // Cache miss (hết hạn)
        }
        return $data['val'];
    }

    public function set(string $key, mixed $value, ?int $ttl = null): void {
        file_put_contents($this->path($key), json_encode([
            'val' => $value,
            'exp' => time() + ($ttl ?? $this->default_ttl),
            'key' => $key,
        ], JSON_UNESCAPED_UNICODE));
    }

    public function delete(string $key): void {
        $file = $this->path($key);
        if (file_exists($file)) unlink($file);
    }

    public function remember(string $key, callable $callback, ?int $ttl = null): mixed {
        $val = $this->get($key);
        if ($val !== null) {
            echo "(cache HIT) ";
            return $val;
        }
        echo "(cache MISS) ";
        $val = $callback();
        $this->set($key, $val, $ttl);
        return $val;
    }

    public function flush(): int {
        $count = 0;
        foreach (glob($this->dir . '/*.cache') as $f) {
            unlink($f); $count++;
        }
        return $count;
    }
}

// ── Sử dụng ──────────────────────
$cache = new FileCache(__DIR__ . '/cache', 60);

// Hàm giả lập query DB tốn kém
function lay_du_lieu_tu_db(int $id): array {
    sleep(0);  // Giả lập delay
    return ['id' => $id, 'ten' => "Sản phẩm #$id", 'gia' => rand(100, 999) * 1000, 'ts' => time()];
}

// Lần 1: cache miss → tính toán
$t1 = microtime(true);
$sp  = $cache->remember("product_1", fn() => lay_du_lieu_tu_db(1), 30);
echo number_format((microtime(true)-$t1)*1000, 2) . "ms | {$sp['ten']}<br>";

// Lần 2: cache hit → nhanh hơn
$t2 = microtime(true);
$sp2 = $cache->remember("product_1", fn() => lay_du_lieu_tu_db(1), 30);
echo number_format((microtime(true)-$t2)*1000, 2) . "ms | {$sp2['ten']}<br>";

// Xóa cache khi cập nhật
// $cache->delete("product_1");

echo "Cache flush: " . $cache->flush() . " files xóa<br>";"""
  ),
  (14, "MVC Pattern – Model View Controller",
   "Xây dựng ứng dụng PHP theo MVC pattern để tách biệt logic khỏi giao diện.",
   ["Tạo Router đơn giản",
    "Tạo BaseController với render/redirect",
    "Model kết nối DB qua PDO",
    "View template PHP thuần",
    "Full CRUD với MVC"],
   ["MVC: Model (data) – View (UI) – Controller (xử lý request)",
    "Router: map URL path → Controller action",
    "<code>ob_start() / ob_get_clean()</code>: buffer output để render view",
    "Controller không chứa HTML; View không chứa business logic",
    "Model không biết về Controller hay View"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Router
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Router {
    private array $routes = [];
    public function get(string $path, callable $handler): void  { $this->routes['GET'][$path]    = $handler; }
    public function post(string $path, callable $handler): void  { $this->routes['POST'][$path]   = $handler; }
    public function delete(string $path, callable $handler): void{ $this->routes['DELETE'][$path] = $handler; }

    public function dispatch(): void {
        $method = $_SERVER['REQUEST_METHOD'];
        $path   = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        $path   = '/' . trim($path, '/');
        
        // Match dynamic route (vd: /products/42)
        foreach ($this->routes[$method] ?? [] as $route => $handler) {
            $pattern = preg_replace('/{[^}]+}/', '([^/]+)', $route);
            if (preg_match("#^$pattern$#", $path, $m)) {
                array_shift($m);
                call_user_func_array($handler, $m);
                return;
            }
        }
        http_response_code(404);
        echo "404 – Không tìm thấy trang";
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BaseController
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
abstract class BaseController {
    protected function view(string $tpl, array $data = []): void {
        extract($data);  // $data['ten'] → $ten
        $tpl_file = __DIR__ . "/views/{$tpl}.php";
        if (!file_exists($tpl_file)) throw new RuntimeException("View không tồn tại: $tpl");
        include $tpl_file;
    }
    protected function json(mixed $data, int $code = 200): never {
        http_response_code($code);
        header('Content-Type: application/json');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        exit;
    }
    protected function redirect(string $url): never {
        header("Location: $url"); exit;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Model
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class ProductModel {
    public function __construct(private PDO $pdo) {}
    public function all(): array { return $this->pdo->query("SELECT * FROM san_pham ORDER BY id DESC")->fetchAll(); }
    public function find(int $id): ?array {
        $s = $this->pdo->prepare("SELECT * FROM san_pham WHERE id = ?");
        $s->execute([$id]); return $s->fetch() ?: null;
    }
    public function create(array $d): int {
        $s = $this->pdo->prepare("INSERT INTO san_pham (ten, gia, so_luong) VALUES (:ten, :gia, :sl)");
        $s->execute([':ten'=>$d['ten'],':gia'=>$d['gia'],':sl'=>$d['so_luong']]);
        return (int)$this->pdo->lastInsertId();
    }
    public function delete(int $id): bool {
        $s = $this->pdo->prepare("DELETE FROM san_pham WHERE id = ?");
        $s->execute([$id]); return $s->rowCount() > 0;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Controller
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class ProductController extends BaseController {
    private ProductModel $model;
    public function __construct(PDO $pdo) { $this->model = new ProductModel($pdo); }

    public function index(): void {
        $products = $this->model->all();
        $this->view('products/index', compact('products'));
    }
    public function show(string $id): void {
        $product = $this->model->find((int)$id);
        if (!$product) { http_response_code(404); echo "404"; return; }
        $this->view('products/show', compact('product'));
    }
    public function store(): void {
        $id = $this->model->create($_POST);
        $this->redirect('/products');
    }
    public function destroy(string $id): void {
        $this->model->delete((int)$id);
        $this->json(['success' => true]);
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Bootstrap (index.php)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// $pdo = new PDO('mysql:host=localhost;dbname=test;charset=utf8mb4', 'root', '');
// $ctrl = new ProductController($pdo);
// $router = new Router();
// $router->get('/products',          [$ctrl, 'index']);
// $router->get('/products/{id}',     [$ctrl, 'show']);
// $router->post('/products',         [$ctrl, 'store']);
// $router->delete('/products/{id}',  [$ctrl, 'destroy']);
// $router->dispatch();
echo "MVC pattern: Router → Controller → Model → View<br>";"""
  ),
  (15, "Composer và Dependency Management",
   "Sử dụng Composer để quản lý thư viện bên thứ ba trong dự án PHP.",
   ["Khởi tạo <code>composer.json</code> với <code>composer init</code>",
    "Cài thư viện: <code>composer require</code>",
    "Sử dụng autoloading PSR-4",
    "Cài Guzzle để gọi API, Faker để tạo dữ liệu test",
    "Dev dependencies: <code>PHPUnit</code>"],
   ["Composer: package manager của PHP – quản lý thư viện và autoloading",
    "<code>composer require vendor/package</code>: cài thư viện",
    "<code>composer require --dev vendor/package</code>: chỉ cho dev",
    "<code>require 'vendor/autoload.php'</code>: include autoloader của Composer",
    "Packagist.org: kho thư viện PHP công khai"],
   """\
<?php
// composer.json
// {
//     "name": "myapp/my-project",
//     "description": "Dự án PHP với Composer",
//     "require": {
//         "php": ">=8.1",
//         "guzzlehttp/guzzle": "^7.0",
//         "vlucas/phpdotenv": "^5.4",
//         "monolog/monolog": "^3.0"
//     },
//     "require-dev": {
//         "phpunit/phpunit": "^10.0",
//         "fakerphp/faker": "^1.21"
//     },
//     "autoload": {
//         "psr-4": { "App\\\\": "src/" }
//     },
//     "autoload-dev": {
//         "psr-4": { "Tests\\\\": "tests/" }
//     }
// }

// Sau khi chạy: composer install
require_once 'vendor/autoload.php';

// ── Guzzle: gọi HTTP API ──────────
use GuzzleHttp\\Client;

$client = new Client(['timeout' => 10]);
try {
    $response = $client->get('https://jsonplaceholder.typicode.com/users/1');
    $user = json_decode($response->getBody(), true);
    echo "Tên: {$user['name']}, Email: {$user['email']}<br>";
} catch (Exception $e) {
    echo "Lỗi API: " . $e->getMessage() . "<br>";
}

// ── Faker: dữ liệu test ───────────
use Faker\\Factory;

$fake = Factory::create('vi_VN');
for ($i = 0; $i < 5; $i++) {
    echo $fake->name() . " – " . $fake->email() . " – " . $fake->phoneNumber() . "<br>";
}

// ── Monolog: logging ──────────────
use Monolog\\Logger;
use Monolog\\Handler\\StreamHandler;

$log = new Logger('app');
$log->pushHandler(new StreamHandler('app.log', Logger::DEBUG));
$log->info('Ứng dụng khởi động', ['env' => 'production', 'version' => '1.0']);
$log->error('Lỗi kết nối DB', ['host' => 'localhost']);
echo "Log đã ghi vào app.log<br>";

// ── .env với phpdotenv ────────────
use Dotenv\\Dotenv;
// Dotenv::createImmutable(__DIR__)->load();
// $db_host = $_ENV['DB_HOST'];
// .env file:
// DB_HOST=localhost
// DB_NAME=myapp
// DB_USER=root
// DB_PASS=secret
// APP_SECRET=mysecretkey
echo "Composer giúp quản lý thư viện dễ dàng!";"""
  ),
  (16, "Unit Testing với PHPUnit",
   "Viết unit test cho code PHP bằng PHPUnit để đảm bảo chất lượng phần mềm.",
   ["Cài PHPUnit qua Composer",
    "Viết test case cho class Calculator",
    "Test exception throwing",
    "Data Provider để test nhiều cases",
    "Mock object (stub/spy)"],
   ["PHPUnit: framework test phổ biến nhất trong PHP",
    "<code>$this->assertEquals($expected, $actual)</code>: assertion cơ bản",
    "<code>$this->expectException(RuntimeException::class)</code>: test exception",
    "<code>@dataProvider</code>: cung cấp nhiều bộ dữ liệu test",
    "Test coverage: % code được test – mục tiêu > 80%"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// src/Calculator.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Calculator {
    public function add(float $a, float $b): float       { return $a + $b; }
    public function subtract(float $a, float $b): float  { return $a - $b; }
    public function multiply(float $a, float $b): float  { return $a * $b; }
    public function divide(float $a, float $b): float {
        if ($b == 0) throw new DivisionByZeroError("Không chia được cho 0");
        return $a / $b;
    }
    public function factorial(int $n): int {
        if ($n < 0) throw new InvalidArgumentException("n phải >= 0");
        return $n <= 1 ? 1 : $n * $this->factorial($n - 1);
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// tests/CalculatorTest.php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// <?php
// use PHPUnit\\Framework\\TestCase;
// use PHPUnit\\Framework\\Attributes\\DataProvider;
//
// class CalculatorTest extends TestCase {
//     private Calculator $calc;
//
//     protected function setUp(): void {
//         $this->calc = new Calculator();  // chạy trước mỗi test
//     }
//
//     // ── Basic assertions ─────────
//     public function testAdd(): void {
//         $this->assertEquals(5.0,  $this->calc->add(2, 3));
//         $this->assertEquals(-1.0, $this->calc->add(2, -3));
//         $this->assertEquals(0.3,  $this->calc->add(0.1, 0.2), delta: 0.0001);
//     }
//
//     public function testDivide(): void {
//         $this->assertEquals(2.5, $this->calc->divide(5, 2));
//     }
//
//     // ── Test exception ────────────
//     public function testDivideByZeroThrows(): void {
//         $this->expectException(DivisionByZeroError::class);
//         $this->calc->divide(10, 0);
//     }
//
//     // ── Data Provider ─────────────
//     #[DataProvider('factorialProvider')]
//     public function testFactorial(int $n, int $expected): void {
//         $this->assertEquals($expected, $this->calc->factorial($n));
//     }
//     public static function factorialProvider(): array {
//         return [[0,1],[1,1],[5,120],[10,3628800]];
//     }
// }
//
// ── Chạy test: ───────────────────
// vendor/bin/phpunit tests/
// vendor/bin/phpunit --coverage-html coverage/  (cần Xdebug)

// Demo chạy tay (không qua PHPUnit)
$calc = new Calculator();
$tests = [
    ['add', [2,3], 5],
    ['subtract', [10,4], 6],
    ['multiply', [3,4], 12],
    ['divide', [10,4], 2.5],
    ['factorial', [5], 120],
];
$pass = $fail = 0;
foreach ($tests as [$method, $args, $expected]) {
    $result = $calc->$method(...$args);
    if ($result == $expected) { echo "✅ PASS: $method(" . implode(',',$args) . ") = $result<br>"; $pass++; }
    else { echo "❌ FAIL: $method(" . implode(',',$args) . ") = $result (expected $expected)<br>"; $fail++; }
}
echo "<br>Kết quả: $pass pass, $fail fail";"""
  ),
  (17, "Middleware và Request Pipeline",
   "Xây dựng middleware pipeline để xử lý authentication, logging, rate limiting.",
   ["Định nghĩa interface Middleware",
    "AuthMiddleware kiểm tra token",
    "LoggingMiddleware ghi log request",
    "RateLimitMiddleware giới hạn requests",
    "Chain middleware theo thứ tự"],
   ["Middleware: layer trung gian xử lý request trước/sau controller",
    "Pipeline pattern: middleware(1) → middleware(2) → ... → controller",
    "<code>$next($request)</code>: chuyển sang middleware tiếp theo",
    "Order matters: Auth trước, rồi mới RateLimit, rồi Log",
    "Laravel, Symfony đều dùng middleware pipeline tương tự"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Request & Response
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Request {
    public function __construct(
        public readonly string $method,
        public readonly string $path,
        public readonly array  $headers = [],
        public readonly array  $body    = [],
    ) {}
    public function header(string $name): ?string {
        return $this->headers[strtolower($name)] ?? null;
    }
}

class Response {
    public int    $status = 200;
    public string $body   = '';
    public array  $headers = [];
    public function json(mixed $data, int $status = 200): static {
        $this->status = $status;
        $this->headers['Content-Type'] = 'application/json';
        $this->body = json_encode($data, JSON_UNESCAPED_UNICODE);
        return $this;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Middleware Interface
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
interface Middleware {
    public function handle(Request $req, callable $next): Response;
}

// ── Auth Middleware ────────────────
class AuthMiddleware implements Middleware {
    private array $valid_tokens = ['token123' => ['id'=>1,'role'=>'admin']];
    public function handle(Request $req, callable $next): Response {
        $auth = $req->header('authorization') ?? '';
        $token = str_replace('Bearer ', '', $auth);
        if (!isset($this->valid_tokens[$token])) {
            return (new Response())->json(['error' => 'Unauthorized'], 401);
        }
        return $next($req);
    }
}

// ── Logging Middleware ─────────────
class LoggingMiddleware implements Middleware {
    public function handle(Request $req, callable $next): Response {
        $start = microtime(true);
        $response = $next($req);
        $ms = round((microtime(true) - $start) * 1000, 2);
        echo "[LOG] {$req->method} {$req->path} → {$response->status} ({$ms}ms)<br>";
        return $response;
    }
}

// ── Rate Limit Middleware ──────────
class RateLimitMiddleware implements Middleware {
    private static array $counter = [];
    public function __construct(private int $maxPerMinute = 60) {}
    public function handle(Request $req, callable $next): Response {
        $key = $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
        $minute = date('YmdHi');
        self::$counter["$key:$minute"] = (self::$counter["$key:$minute"] ?? 0) + 1;
        if (self::$counter["$key:$minute"] > $this->maxPerMinute) {
            return (new Response())->json(['error' => 'Too Many Requests'], 429);
        }
        return $next($req);
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Pipeline
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class Pipeline {
    private array $middleware = [];
    public function pipe(Middleware $mw): static { $this->middleware[] = $mw; return $this; }
    public function handle(Request $req, callable $destination): Response {
        $chain = array_reduce(
            array_reverse($this->middleware),
            fn($next, $mw) => fn($req) => $mw->handle($req, $next),
            $destination
        );
        return $chain($req);
    }
}

// ── Test ──────────────────────────
$pipeline = (new Pipeline())
    ->pipe(new LoggingMiddleware())
    ->pipe(new RateLimitMiddleware(100))
    ->pipe(new AuthMiddleware());

$request = new Request('GET', '/api/products', ['authorization' => 'Bearer token123']);
$response = $pipeline->handle($request, function(Request $req) {
    return (new Response())->json(['data' => ['Sản phẩm A', 'Sản phẩm B'], 'count' => 2]);
});
echo $response->body . "<br>";

// Request không có token
$req2 = new Request('GET', '/api/products', []);
$res2 = $pipeline->handle($req2, fn($r) => (new Response())->json(['data' => []]));
echo $res2->body . "<br>";"""
  ),
  (18, "Queue và Background Jobs",
   "Xây dựng hệ thống hàng đợi (queue) đơn giản để xử lý tác vụ nặng ở background.",
   ["Tạo Job interface và Queue class",
    "SendEmailJob, ResizeImageJob",
    "Lưu queue vào file/DB",
    "Worker script xử lý queue",
    "Retry khi job thất bại"],
   ["Queue: xử lý tác vụ nặng (email, resizing) không đồng bộ để response nhanh hơn",
    "Job: một đơn vị công việc cần thực hiện",
    "Worker: process chạy ngầm lấy job từ queue và thực thi",
    "Retry: chạy lại job thất bại N lần trước khi báo lỗi",
    "Redis Queue, Database Queue là phổ biến nhất trong production"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Job Interface
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
interface Job {
    public function handle(): bool;
    public function getMaxRetries(): int;
    public function getName(): string;
}

// ── Concrete Jobs ─────────────────
class SendEmailJob implements Job {
    public function __construct(
        private string $to,
        private string $subject,
        private string $body,
    ) {}
    public function handle(): bool {
        // Giả lập gửi email
        echo "📧 Gửi email đến {$this->to}: {$this->subject}<br>";
        return rand(0,9) > 1;  // 90% thành công
    }
    public function getMaxRetries(): int { return 3; }
    public function getName(): string { return "SendEmailJob"; }
}

class ResizeImageJob implements Job {
    public function __construct(private string $path, private int $width) {}
    public function handle(): bool {
        echo "🖼️  Resize {$this->path} → {$this->width}px<br>";
        return true;
    }
    public function getMaxRetries(): int { return 1; }
    public function getName(): string { return "ResizeImageJob"; }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// File-based Queue
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class FileQueue {
    private string $file;
    public function __construct(string $file = '/tmp/php_queue.json') {
        $this->file = $file;
        if (!file_exists($file)) file_put_contents($file, '[]');
    }
    private function load(): array { return json_decode(file_get_contents($this->file), true) ?: []; }
    private function save(array $data): void { file_put_contents($this->file, json_encode($data, JSON_PRETTY_PRINT)); }

    public function push(Job $job): void {
        $queue = $this->load();
        $queue[] = ['job' => serialize($job), 'retries' => 0, 'queued_at' => time()];
        $this->save($queue);
        echo "✅ Job '{$job->getName()}' thêm vào queue<br>";
    }

    public function process(int $limit = 5): void {
        $queue   = $this->load();
        $failed  = [];
        $done    = 0;
        foreach ($queue as $item) {
            if ($done >= $limit) { $failed[] = $item; continue; }
            $job = unserialize($item['job']);
            echo "▶️  Xử lý: {$job->getName()} (lần {$item['retries']})<br>";
            if ($job->handle()) {
                $done++;
            } else {
                $item['retries']++;
                if ($item['retries'] < $job->getMaxRetries()) {
                    $failed[] = $item;
                    echo "⚠️  Thất bại, sẽ retry (lần {$item['retries']})<br>";
                } else {
                    echo "❌ Job '{$job->getName()}' thất bại hoàn toàn<br>";
                }
            }
        }
        $this->save($failed);
        echo "Queue còn: " . count($failed) . " jobs<br>";
    }
    public function count(): int { return count($this->load()); }
}

// ── Sử dụng ──────────────────────
$queue = new FileQueue('/tmp/demo_queue.json');

// Dispatch jobs (thêm vào queue nhanh → response ngay)
$queue->push(new SendEmailJob('user@demo.vn', 'Chào mừng!', 'Nội dung email'));
$queue->push(new ResizeImageJob('/uploads/photo.jpg', 800));
$queue->push(new SendEmailJob('admin@demo.vn', 'Đơn hàng mới', 'Chi tiết...'));
echo "Queue size: " . $queue->count() . "<br><br>";

// Worker chạy (thường chạy ở CLI: php worker.php)
echo "=== Worker chạy ===<br>";
$queue->process(10);"""
  ),
  (19, "WebSocket với Ratchet PHP",
   "Tích hợp WebSocket real-time vào PHP bằng thư viện Ratchet.",
   ["Cài Ratchet qua Composer",
    "Tạo WebSocket server lắng nghe kết nối",
    "Broadcast message đến tất cả client",
    "Chat room đơn giản",
    "Client HTML kết nối WebSocket"],
   ["WebSocket: kết nối 2 chiều thời gian thực giữa client và server",
    "Ratchet: thư viện PHP WebSocket server dựa trên ReactPHP",
    "Event-based: onOpen, onMessage, onClose, onError",
    "<code>SplObjectStorage</code>: lưu danh sách clients đang kết nối",
    "Chạy server: <code>php server.php</code> từ CLI"],
   """\
<?php
// Cài đặt: composer require cboden/ratchet

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// server.php – WebSocket Server
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
use Ratchet\\MessageComponentInterface;
use Ratchet\\ConnectionInterface;

class ChatRoom implements MessageComponentInterface {
    private SplObjectStorage $clients;

    public function __construct() {
        $this->clients = new SplObjectStorage;
    }

    public function onOpen(ConnectionInterface $conn): void {
        $this->clients->attach($conn);
        $count = count($this->clients);
        echo "🔵 Kết nối mới: #{$conn->resourceId} | Online: $count\\n";
        $conn->send(json_encode([
            'type'   => 'system',
            'msg'    => "Chào mừng! Đang có $count người online",
            'online' => $count,
        ]));
        $this->broadcast(['type'=>'join','msg'=>"User #{$conn->resourceId} tham gia",'online'=>$count], $conn);
    }

    public function onMessage(ConnectionInterface $from, string $msg): void {
        $data = json_decode($msg, true) ?: ['type'=>'chat','msg'=>$msg];
        $data['from'] = "User #{$from->resourceId}";
        $data['time'] = date('H:i:s');
        echo "💬 #{$from->resourceId}: {$data['msg']}\\n";
        $this->broadcast($data, null);  // broadcast cho mọi người kể cả người gửi
    }

    public function onClose(ConnectionInterface $conn): void {
        $this->clients->detach($conn);
        $count = count($this->clients);
        echo "🔴 Ngắt kết nối: #{$conn->resourceId} | Online: $count\\n";
        $this->broadcast(['type'=>'leave','msg'=>"User #{$conn->resourceId} rời phòng",'online'=>$count], null);
    }

    public function onError(ConnectionInterface $conn, \\Exception $e): void {
        echo "❌ Lỗi: " . $e->getMessage() . "\\n";
        $conn->close();
    }

    private function broadcast(array $data, ?ConnectionInterface $except): void {
        $json = json_encode($data, JSON_UNESCAPED_UNICODE);
        foreach ($this->clients as $client) {
            if ($client !== $except) $client->send($json);
        }
    }
}

// Khởi động server (chạy từ CLI)
// use Ratchet\\Server\\IoServer;
// use Ratchet\\Http\\HttpServer;
// use Ratchet\\WebSocket\\WsServer;
// $server = IoServer::factory(new HttpServer(new WsServer(new ChatRoom())), 8080);
// echo "WebSocket server chạy tại ws://localhost:8080\\n";
// $server->run();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// client.html – Kết nối WebSocket
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// <script>
// const ws = new WebSocket('ws://localhost:8080');
// ws.onopen = () => ws.send(JSON.stringify({type:'chat',msg:'Xin chào!'}));
// ws.onmessage = e => { const d = JSON.parse(e.data); console.log(d.msg); };
// ws.onclose = () => console.log('Kết nối đóng');
// </script>
echo "Xem code để biết cách chạy Ratchet WebSocket Server!";"""
  ),
  (20, "PHP 8.x Features – Fibers và Async",
   "Khám phá các tính năng mới nhất của PHP 8.1/8.2/8.3 bao gồm Fibers.",
   ["Fibers: concurrency không cần async/await",
    "Readonly classes (PHP 8.2)",
    "DNF types (Disjunctive Normal Form)",
    "Enums nâng cao với methods và implements",
    "First-class callable syntax"],
   ["Fiber: coroutine trong PHP – cho phép tạm dừng và tiếp tục thực thi",
    "<code>$fiber->start(); $fiber->resume($val);</code>",
    "Readonly class PHP 8.2: tất cả properties đều readonly",
    "First-class callable: <code>strlen(...)</code> thay cho <code>fn($s) => strlen($s)</code>",
    "PHP 8.3: <code>json_validate()</code>, Typed class constants"],
   """\
<?php
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Fibers (PHP 8.1) – Coroutines
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$fiber = new Fiber(function(): string {
    $val1 = Fiber::suspend('Fiber tạm dừng lần 1');
    echo "Fiber nhận: $val1<br>";
    $val2 = Fiber::suspend('Fiber tạm dừng lần 2');
    echo "Fiber nhận: $val2<br>";
    return 'Fiber hoàn thành';
});

$v1 = $fiber->start();             // bắt đầu chạy đến suspend đầu tiên
echo "Main nhận: $v1<br>";
$v2 = $fiber->resume('Dữ liệu A'); // tiếp tục đến suspend tiếp theo
echo "Main nhận: $v2<br>";
$fiber->resume('Dữ liệu B');       // tiếp tục đến kết thúc
echo "Fiber return: " . $fiber->getReturn() . "<br><br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Enums với methods và interface (PHP 8.1)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
enum TrangThaiDonHang: string {
    case ChoXacNhan = 'pending';
    case DangGiao   = 'shipping';
    case HoanThanh  = 'completed';
    case HuyBo      = 'cancelled';

    public function label(): string {
        return match($this) {
            self::ChoXacNhan => '⏳ Chờ xác nhận',
            self::DangGiao   => '🚚 Đang giao',
            self::HoanThanh  => '✅ Hoàn thành',
            self::HuyBo      => '❌ Đã hủy',
        };
    }
    public function isTerminal(): bool {
        return in_array($this, [self::HoanThanh, self::HuyBo]);
    }
    public static function fromLabel(string $label): self {
        foreach (self::cases() as $case) {
            if ($case->label() === $label) return $case;
        }
        throw new ValueError("Label không hợp lệ: $label");
    }
}

$ts = TrangThaiDonHang::DangGiao;
echo $ts->label() . "<br>";
echo "Terminal: " . ($ts->isTerminal() ? "có" : "không") . "<br>";
echo "Value: " . $ts->value . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Readonly class (PHP 8.2)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
readonly class Money {
    public function __construct(
        public int    $amount,   // VND
        public string $currency = 'VND',
    ) {}
    public function add(Money $other): self {
        if ($this->currency !== $other->currency) throw new InvalidArgumentException("Khác tiền tệ");
        return new self($this->amount + $other->amount, $this->currency);
    }
    public function format(): string {
        return number_format($this->amount, 0, ',', '.') . ' ' . $this->currency;
    }
}

$gia = new Money(150_000);
$phi = new Money(15_000);
$tong = $gia->add($phi);
echo $tong->format() . "<br>";  // 165.000 VND

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// First-class callable (PHP 8.1)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$cac_ten = ['Bình', 'an', 'CÚC', 'dũng'];
$chuan_hoa = array_map(mb_strtolower(...), $cac_ten);     // first-class callable
echo implode(', ', $chuan_hoa) . "<br>";

$chuan_hoa2 = array_map(ucfirst(...), $chuan_hoa);
echo implode(', ', $chuan_hoa2) . "<br>";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// json_validate (PHP 8.3)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if (function_exists('json_validate')) {
    var_dump(json_validate('{"name":"An","age":20}'));   // true
    var_dump(json_validate('{invalid json}'));             // false
} else {
    echo "json_validate cần PHP 8.3+<br>";
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
  <meta name="keywords" content="PHP OOP,PDO,MySQL,NenTang,Lập trình PHP nâng cao">
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
  <div class="page-header module-php-2">
    <div class="breadcrumb">
      <a href="../../index.html">PHP Course</a> &rsaquo;
      <a href="../index.html">Module 2</a> &rsaquo; Bài {n:02d}
    </div>
    <h1>Bài {n:02d}: {title}</h1>
    <p>Module 2 – PHP OOP &amp; Nâng Cao</p>
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
  <a href="../index.html" class="btn-back">&#8592; Quay lại Module 2</a>
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

print(f"\n✅ Module 2 PHP: {created} bài tạo thành công tại {MOD}")
