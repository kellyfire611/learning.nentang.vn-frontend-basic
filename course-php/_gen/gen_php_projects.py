# gen_php_projects.py – Đồ Án Tổng Hợp PHP (6 dự án)
import pathlib

ROOT = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-php")
MOD  = ROOT / "module-04-do-an"
MOD.mkdir(parents=True, exist_ok=True)

PROJECTS = [
  (1, "Hệ Thống Đăng Nhập & Đăng Ký",
   "Xây dựng hệ thống xác thực người dùng hoàn chỉnh với đăng ký, đăng nhập, quên mật khẩu và phân quyền role.",
   ["Đăng ký: validate email/password, hash bcrypt, gửi email xác thực",
    "Đăng nhập: session + JWT option, remember me 30 ngày",
    "Quên mật khẩu: gửi email reset link có thời hạn 1 giờ",
    "Phân quyền: admin/user/moderator với middleware kiểm tra",
    "Profile: cập nhật thông tin, đổi mật khẩu, upload avatar",
    "Security: rate limiting login, CSRF, session fixation, brute force protection"],
   ["Luôn hash password bằng <code>password_hash(PASSWORD_DEFAULT)</code>",
    "Reset token: <code>bin2hex(random_bytes(32))</code>, lưu DB cùng thời gian hết hạn",
    "Session fixation: <code>session_regenerate_id(true)</code> sau khi login",
    "Ghi log: mọi lần login thành công/thất bại cần ghi log với IP, timestamp",
    "2FA (nâng cao): Google Authenticator với TOTP algorithm"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 1: HỆ THỐNG AUTH HOÀN CHỈNH
// ════════════════════════════════════

// ── Database Schema ───────────────
/*
CREATE TABLE users (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten         VARCHAR(100) NOT NULL,
    email          VARCHAR(150) UNIQUE NOT NULL,
    mat_khau       VARCHAR(255) NOT NULL,
    role           ENUM('user','moderator','admin') DEFAULT 'user',
    avatar         VARCHAR(255) DEFAULT NULL,
    email_verified TINYINT(1) DEFAULT 0,
    verify_token   VARCHAR(64) DEFAULT NULL,
    reset_token    VARCHAR(64) DEFAULT NULL,
    reset_expires  DATETIME DEFAULT NULL,
    remember_token VARCHAR(64) DEFAULT NULL,
    login_attempts INT DEFAULT 0,
    locked_until   DATETIME DEFAULT NULL,
    last_login     DATETIME DEFAULT NULL,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE login_logs (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NULL,
    email      VARCHAR(150),
    ip_address VARCHAR(45),
    user_agent TEXT,
    status     ENUM('success','failed','locked') DEFAULT 'failed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/

class AuthSystem {
    private const MAX_ATTEMPTS   = 5;
    private const LOCK_DURATION  = 15 * 60; // 15 phút
    private const RESET_TTL      = 3600;    // 1 giờ
    private const REMEMBER_TTL   = 30 * 24 * 3600;

    public function __construct(private PDO $pdo, private ?Mailer $mailer = null) {}

    // ─── Đăng ký ─────────────────
    public function register(array $data): array {
        // Validation
        $errors = [];
        $data['ho_ten'] = trim($data['ho_ten'] ?? '');
        $data['email']  = strtolower(trim($data['email'] ?? ''));
        $data['mat_khau'] = $data['mat_khau'] ?? '';

        if (strlen($data['ho_ten']) < 2)   $errors['ho_ten']   = "Họ tên ít nhất 2 ký tự";
        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL))
                                            $errors['email']    = "Email không hợp lệ";
        if (strlen($data['mat_khau']) < 8)  $errors['mat_khau'] = "Mật khẩu ít nhất 8 ký tự";
        if (!preg_match('/[A-Z]/', $data['mat_khau']))
                                            $errors['mat_khau'] = ($errors['mat_khau'] ?? '') . " (cần chữ hoa)";
        if (!preg_match('/[0-9]/', $data['mat_khau']))
                                            $errors['mat_khau'] = ($errors['mat_khau'] ?? '') . " (cần số)";
        if ($errors) throw new ValidationException($errors);

        // Email đã tồn tại?
        $chk = $this->pdo->prepare("SELECT id FROM users WHERE email = ?");
        $chk->execute([$data['email']]);
        if ($chk->fetch()) throw new DuplicateEmailException("Email đã được đăng ký");

        // Insert
        $verify_token = bin2hex(random_bytes(32));
        $stmt = $this->pdo->prepare("
            INSERT INTO users (ho_ten, email, mat_khau, verify_token)
            VALUES (?, ?, ?, ?)
        ");
        $stmt->execute([$data['ho_ten'], $data['email'],
                        password_hash($data['mat_khau'], PASSWORD_DEFAULT),
                        $verify_token]);
        $user_id = (int)$this->pdo->lastInsertId();

        // Gửi email xác thực
        $this->mailer?->sendVerification($data['email'], $data['ho_ten'], $verify_token);

        return $this->findById($user_id);
    }

    // ─── Đăng nhập ───────────────
    public function login(string $email, string $mat_khau, bool $remember = false): array {
        $email = strtolower(trim($email));
        $ip    = $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';

        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();

        // Kiểm tra khóa tài khoản
        if ($user && $user['locked_until'] && strtotime($user['locked_until']) > time()) {
            $con_lai = ceil((strtotime($user['locked_until']) - time()) / 60);
            $this->logLogin(null, $email, $ip, 'locked');
            throw new AccountLockedException("Tài khoản bị khóa, thử lại sau $con_lai phút");
        }

        // Verify password
        if (!$user || !password_verify($mat_khau, $user['mat_khau'])) {
            if ($user) {
                $attempts = $user['login_attempts'] + 1;
                $locked   = $attempts >= self::MAX_ATTEMPTS
                    ? date('Y-m-d H:i:s', time() + self::LOCK_DURATION)
                    : null;
                $this->pdo->prepare("UPDATE users SET login_attempts=?, locked_until=? WHERE id=?")
                     ->execute([$attempts, $locked, $user['id']]);
                $con_lai_lan = self::MAX_ATTEMPTS - $attempts;
                if ($con_lai_lan > 0) throw new AuthException("Sai thông tin. Còn $con_lai_lan lần thử");
            }
            $this->logLogin(null, $email, $ip, 'failed');
            throw new AuthException("Email hoặc mật khẩu không đúng");
        }

        // Reset attempts, cập nhật last login
        $this->pdo->prepare("UPDATE users SET login_attempts=0, locked_until=NULL, last_login=NOW() WHERE id=?")
             ->execute([$user['id']]);
        $this->logLogin($user['id'], $email, $ip, 'success');

        // Session
        session_regenerate_id(true);
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['role']    = $user['role'];

        // Remember me
        if ($remember) {
            $token = bin2hex(random_bytes(32));
            $this->pdo->prepare("UPDATE users SET remember_token=? WHERE id=?")->execute([$token, $user['id']]);
            setcookie('remember', $token, time() + self::REMEMBER_TTL, '/', '', true, true);
        }

        return $user;
    }

    // ─── Quên mật khẩu ───────────
    public function forgotPassword(string $email): void {
        $stmt = $this->pdo->prepare("SELECT id, ho_ten FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();
        if (!$user) return; // Không tiết lộ email có tồn tại không

        $token   = bin2hex(random_bytes(32));
        $expires = date('Y-m-d H:i:s', time() + self::RESET_TTL);
        $this->pdo->prepare("UPDATE users SET reset_token=?, reset_expires=? WHERE id=?")
             ->execute([$token, $expires, $user['id']]);
        $this->mailer?->sendResetPassword($email, $user['ho_ten'], $token);
    }

    // ─── Reset mật khẩu ──────────
    public function resetPassword(string $token, string $new_pass): void {
        $stmt = $this->pdo->prepare("SELECT id FROM users WHERE reset_token=? AND reset_expires > NOW()");
        $stmt->execute([$token]);
        $user = $stmt->fetch();
        if (!$user) throw new AuthException("Token không hợp lệ hoặc đã hết hạn");
        if (strlen($new_pass) < 8) throw new AuthException("Mật khẩu ít nhất 8 ký tự");

        $this->pdo->prepare("UPDATE users SET mat_khau=?, reset_token=NULL, reset_expires=NULL WHERE id=?")
             ->execute([password_hash($new_pass, PASSWORD_DEFAULT), $user['id']]);
    }

    // ─── Kiểm tra remember token ─
    public function checkRemember(): ?array {
        $token = $_COOKIE['remember'] ?? null;
        if (!$token) return null;
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE remember_token = ?");
        $stmt->execute([$token]);
        $user = $stmt->fetch();
        if ($user) {
            session_regenerate_id(true);
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['role']    = $user['role'];
        }
        return $user ?: null;
    }

    private function findById(int $id): array {
        $stmt = $this->pdo->prepare("SELECT id, ho_ten, email, role, created_at FROM users WHERE id=?");
        $stmt->execute([$id]);
        return $stmt->fetch() ?: throw new NotFoundException("User không tồn tại");
    }

    private function logLogin(?int $user_id, string $email, string $ip, string $status): void {
        $stmt = $this->pdo->prepare(
            "INSERT INTO login_logs (user_id, email, ip_address, user_agent, status) VALUES (?,?,?,?,?)"
        );
        $stmt->execute([$user_id, $email, $ip, $_SERVER['HTTP_USER_AGENT'] ?? '', $status]);
    }
}

// ─── Middleware phân quyền ────────
function require_role(string ...$roles): void {
    if (!isset($_SESSION['user_id'])) {
        header('Location: /login?redirect=' . urlencode($_SERVER['REQUEST_URI']));
        exit;
    }
    if (!in_array($_SESSION['role'] ?? 'user', $roles)) {
        http_response_code(403);
        die("Bạn không có quyền truy cập trang này");
    }
}

// Sử dụng middleware:
// require_role('admin');              // Chỉ admin
// require_role('admin', 'moderator'); // Admin hoặc moderator

// ─── Demo ─────────────────────────
echo "=== Auth System Demo ===<br>";
echo "✅ Class AuthSystem đã sẵn sàng<br>";
echo "• register(data): đăng ký + gửi email xác thực<br>";
echo "• login(email, pass, remember): đăng nhập + session<br>";
echo "• forgotPassword(email): gửi link reset<br>";
echo "• resetPassword(token, pass): đổi mật khẩu<br>";
echo "• checkRemember(): auto-login từ cookie<br>";
echo "• Brute force: khóa sau " . AuthSystem::MAX_ATTEMPTS . " lần thất bại<br>";"""
  ),
  (2, "Blog Cá Nhân Với CRUD Đầy Đủ",
   "Xây dựng blog cá nhân hoàn chỉnh với bài viết, danh mục, tags, bình luận và rich-text editor.",
   ["CRUD bài viết: tạo, sửa, xóa, ẩn/hiện",
    "Danh mục phân cấp cha-con",
    "Tags nhiều-nhiều (many-to-many)",
    "Bình luận lồng nhau (nested comments) 2 cấp",
    "Tìm kiếm bài viết, lọc theo danh mục/tag",
    "Tích hợp CKEditor (rich text) và slug tự động"],
   ["Slug: URL-friendly version của tiêu đề (<code>'tieu-de-bai-viet'</code>)",
    "Many-to-many: bảng pivot <code>bai_viet_tags(bai_viet_id, tag_id)</code>",
    "Nested comments: <code>parent_id</code> NULL = comment gốc, có value = reply",
    "Rich text: CKEditor lưu HTML, cần sanitize khi hiển thị",
    "Cache bài viết hot: lưu vào file cache 5 phút giảm tải DB"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 2: BLOG CÁ NHÂN
// ════════════════════════════════════

/* Schema:
CREATE TABLE bai_viet (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    tieu_de     VARCHAR(300) NOT NULL,
    slug        VARCHAR(300) UNIQUE NOT NULL,
    noi_dung    LONGTEXT,
    tom_tat     TEXT,
    anh_dai_dien VARCHAR(255),
    danh_muc_id  INT,
    user_id      INT,
    trang_thai   ENUM('draft','published','archived') DEFAULT 'draft',
    luot_xem     INT DEFAULT 0,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL
);
CREATE TABLE tags (
    id   INT AUTO_INCREMENT PRIMARY KEY,
    ten  VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE bai_viet_tags (
    bai_viet_id INT, tag_id INT,
    PRIMARY KEY (bai_viet_id, tag_id)
);
CREATE TABLE binh_luan (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    bai_viet_id INT NOT NULL,
    parent_id   INT DEFAULT NULL,  -- NULL = comment gốc
    ho_ten      VARCHAR(100),
    email       VARCHAR(150),
    noi_dung    TEXT NOT NULL,
    trang_thai  ENUM('pending','approved','spam') DEFAULT 'pending',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/

// ── Blog Repository ───────────────
class BlogRepository {
    public function __construct(private PDO $pdo) {}

    public function createPost(array $data): int {
        $slug = $this->uniqueSlug($data['tieu_de']);
        $stmt = $this->pdo->prepare("
            INSERT INTO bai_viet (tieu_de, slug, noi_dung, tom_tat, danh_muc_id, user_id, trang_thai, published_at)
            VALUES (:tieu_de, :slug, :noi_dung, :tom_tat, :dm_id, :user_id, :trang_thai, :pub_at)
        ");
        $stmt->execute([
            ':tieu_de'   => $data['tieu_de'],
            ':slug'      => $slug,
            ':noi_dung'  => $data['noi_dung'],
            ':tom_tat'   => $data['tom_tat'] ?? substr(strip_tags($data['noi_dung']), 0, 200),
            ':dm_id'     => $data['danh_muc_id'] ?? null,
            ':user_id'   => $data['user_id'],
            ':trang_thai'=> $data['trang_thai'] ?? 'draft',
            ':pub_at'    => $data['trang_thai'] === 'published' ? date('Y-m-d H:i:s') : null,
        ]);
        $id = (int)$this->pdo->lastInsertId();
        // Gắn tags
        if (!empty($data['tags'])) $this->syncTags($id, $data['tags']);
        return $id;
    }

    private function syncTags(int $bai_viet_id, array $tag_ids): void {
        $this->pdo->prepare("DELETE FROM bai_viet_tags WHERE bai_viet_id = ?")->execute([$bai_viet_id]);
        $stmt = $this->pdo->prepare("INSERT IGNORE INTO bai_viet_tags (bai_viet_id, tag_id) VALUES (?,?)");
        foreach ($tag_ids as $tag_id) $stmt->execute([$bai_viet_id, $tag_id]);
    }

    public function getPostWithTags(string $slug): ?array {
        $post = $this->pdo->prepare("
            SELECT bv.*, u.ho_ten AS tac_gia, dm.ten AS danh_muc
            FROM bai_viet bv
            LEFT JOIN users u  ON u.id  = bv.user_id
            LEFT JOIN danh_muc dm ON dm.id = bv.danh_muc_id
            WHERE bv.slug = ? AND bv.trang_thai = 'published'
        ");
        $post->execute([$slug]);
        $row = $post->fetch();
        if (!$row) return null;

        // Lấy tags
        $tags = $this->pdo->prepare("
            SELECT t.ten, t.slug FROM tags t
            JOIN bai_viet_tags bt ON bt.tag_id = t.id WHERE bt.bai_viet_id = ?
        ");
        $tags->execute([$row['id']]);
        $row['tags'] = $tags->fetchAll();

        // Tăng lượt xem
        $this->pdo->prepare("UPDATE bai_viet SET luot_xem = luot_xem + 1 WHERE id=?")->execute([$row['id']]);
        return $row;
    }

    public function getComments(int $bai_viet_id): array {
        $stmt = $this->pdo->prepare("
            SELECT * FROM binh_luan
            WHERE bai_viet_id = ? AND trang_thai = 'approved'
            ORDER BY parent_id IS NOT NULL, parent_id, created_at
        ");
        $stmt->execute([$bai_viet_id]);
        $rows = $stmt->fetchAll();

        // Build nested tree
        $comments = []; $replies = [];
        foreach ($rows as $c) {
            if ($c['parent_id'] === null) $comments[$c['id']] = $c + ['replies' => []];
            else $replies[] = $c;
        }
        foreach ($replies as $r) {
            if (isset($comments[$r['parent_id']])) {
                $comments[$r['parent_id']]['replies'][] = $r;
            }
        }
        return array_values($comments);
    }

    public function addComment(array $data): int {
        $stmt = $this->pdo->prepare("
            INSERT INTO binh_luan (bai_viet_id, parent_id, ho_ten, email, noi_dung)
            VALUES (?, ?, ?, ?, ?)
        ");
        $stmt->execute([
            $data['bai_viet_id'], $data['parent_id'] ?? null,
            htmlspecialchars($data['ho_ten']),
            filter_var($data['email'], FILTER_VALIDATE_EMAIL) ?: null,
            htmlspecialchars($data['noi_dung']),
        ]);
        return (int)$this->pdo->lastInsertId();
    }

    private function uniqueSlug(string $title): string {
        $slug = $base = strtolower(trim(preg_replace('/[^a-z0-9]+/','-',
            iconv('UTF-8','ASCII//TRANSLIT//IGNORE',$title)),'-'));
        $i = 0;
        while (true) {
            $check = $this->pdo->prepare("SELECT id FROM bai_viet WHERE slug=?");
            $check->execute([$slug]);
            if (!$check->fetch()) break;
            $slug = $base . '-' . ++$i;
        }
        return $slug;
    }
}

// ── Demo output ───────────────────
echo "=== Blog System Demo ===<br>";
echo "Features:<br>";
echo "✅ CRUD bài viết (draft → published → archived)<br>";
echo "✅ Tags nhiều-nhiều với sync<br>";
echo "✅ Bình luận lồng nhau 2 cấp<br>";
echo "✅ Slugs không trùng tự động<br>";
echo "✅ JOIN tác giả + danh mục trong 1 query<br>";
echo "<br>Routes cần thiết:<br>";
$routes = [
    'GET  /blog'            => 'Trang chủ blog – danh sách bài viết phân trang',
    'GET  /blog/{slug}'     => 'Chi tiết bài viết + bình luận',
    'POST /blog/{id}/comment' => 'Gửi bình luận',
    'GET  /admin/posts'     => 'Admin – danh sách (auth required)',
    'GET  /admin/posts/new' => 'Form tạo bài mới',
    'POST /admin/posts'     => 'Lưu bài mới',
    'GET  /admin/posts/{id}/edit' => 'Form sửa',
    'PUT  /admin/posts/{id}'     => 'Lưu cập nhật',
    'DELETE /admin/posts/{id}'   => 'Xóa bài',
];
foreach ($routes as $route => $desc) echo "• <code>$route</code>: $desc<br>";"""
  ),
  (3, "Giỏ Hàng và Thanh Toán (Shopping Cart)",
   "Xây dựng tính năng giỏ hàng với session, quản lý đơn hàng và giả lập thanh toán.",
   ["Giỏ hàng mưu trú trong Session",
    "CRUD cart: thêm, cập nhật SL, xóa item",
    "Kiểm tra tồn kho trước khi thêm giỏ",
    "Tính tiền: giá gốc, giảm giá, phí ship",
    "Đặt hàng: lưu vào DB trong transaction",
    "Lịch sử đơn hàng của khách"],
   ["Session cart: <code>$_SESSION['cart'][$sp_id] = ['qty'=>N,'price'=>P]</code>",
    "SHould verify stock khi checkout (double-check – không chỉ frontend)",
    "Coupon code: bảng <code>coupons</code> với % hoặc fixed discount",
    "Order status: pending → confirmed → shipping → delivered → completed",
    "Webhook: nhận callback từ cổng thanh toán (VNPay, Momo, Stripe)"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 3: SHOPPING CART
// ════════════════════════════════════
session_start();

class ShoppingCart {
    private const SESSION_KEY = 'cart';

    // ─── Thêm vào giỏ ────────────
    public static function add(int $sp_id, int $so_luong, PDO $pdo): void {
        // Kiểm tra sản phẩm tồn tại và còn hàng
        $stmt = $pdo->prepare("SELECT id, ten, gia, gia_km, so_luong FROM san_pham WHERE id=? AND active=1");
        $stmt->execute([$sp_id]);
        $sp = $stmt->fetch();
        if (!$sp) throw new NotFoundException("Sản phẩm không tồn tại");

        $cart    = $_SESSION[self::SESSION_KEY] ?? [];
        $qty_hien_tai = $cart[$sp_id]['qty'] ?? 0;
        $qty_moi = $qty_hien_tai + $so_luong;

        if ($qty_moi > $sp['so_luong']) {
            throw new RuntimeException("Chỉ còn {$sp['so_luong']} sản phẩm trong kho");
        }
        $cart[$sp_id] = [
            'id'    => $sp_id,
            'ten'   => $sp['ten'],
            'gia'   => (float)($sp['gia_km'] ?? $sp['gia']),
            'gia_goc' => (float)$sp['gia'],
            'qty'   => $qty_moi,
        ];
        $_SESSION[self::SESSION_KEY] = $cart;
    }

    // ─── Cập nhật số lượng ────────
    public static function update(int $sp_id, int $so_luong): void {
        $cart = $_SESSION[self::SESSION_KEY] ?? [];
        if ($so_luong <= 0) { unset($cart[$sp_id]); }
        else { $cart[$sp_id]['qty'] = $so_luong; }
        $_SESSION[self::SESSION_KEY] = $cart;
    }

    // ─── Xóa item ────────────────
    public static function remove(int $sp_id): void {
        unset($_SESSION[self::SESSION_KEY][$sp_id]);
    }

    // ─── Xóa toàn bộ ─────────────
    public static function clear(): void {
        unset($_SESSION[self::SESSION_KEY]);
    }

    // ─── Lấy danh sách + tổng ─────
    public static function getItems(): array {
        return array_values($_SESSION[self::SESSION_KEY] ?? []);
    }

    // ─── Tính tổng tiền ──────────
    public static function totals(?string $coupon_discount = null, string $tinh_thanh = 'HCM'): array {
        $items = $_SESSION[self::SESSION_KEY] ?? [];
        $tam_tinh = array_sum(array_map(fn($i) => $i['gia'] * $i['qty'], $items));
        $giam_gia = 0;
        if ($coupon_discount) {
            // 'SAVE10' = 10%, 'FLAT50K' = 50000đ
            if (str_ends_with($coupon_discount, '%')) {
                $giam_gia = $tam_tinh * (float)rtrim($coupon_discount,'%') / 100;
            } else {
                $giam_gia = (float)$coupon_discount;
            }
        }
        $sau_giam = max(0, $tam_tinh - $giam_gia);
        $phi_ship = $sau_giam >= 500_000 ? 0 : (in_array($tinh_thanh, ['HCM','HN']) ? 20_000 : 35_000);
        return [
            'items'     => count($items),
            'tam_tinh'  => $tam_tinh,
            'giam_gia'  => $giam_gia,
            'sau_giam'  => $sau_giam,
            'phi_ship'  => $phi_ship,
            'tong_cong' => $sau_giam + $phi_ship,
        ];
    }

    // ─── Checkout: lưu vào DB ─────
    public static function checkout(PDO $pdo, array $khach_hang, ?string $coupon = null): int {
        $totals = self::totals($coupon, $khach_hang['tinh_thanh'] ?? 'HCM');
        if (empty($_SESSION[self::SESSION_KEY])) throw new RuntimeException("Giỏ hàng trống");

        $pdo->beginTransaction();
        try {
            // 1. Tạo đơn hàng
            $ma_don = 'ORD' . strtoupper(substr(md5(uniqid()), 0, 8));
            $stmt = $pdo->prepare("
                INSERT INTO don_hang (ma_don, ten_khach, sdt, email, dia_chi, tinh_thanh,
                                      tam_tinh, giam_gia, phi_ship, tong_cong, coupon_code)
                VALUES (:ma_don,:ten,:sdt,:email,:dia_chi,:tinh,:tam,:giam,:phi,:tong,:coupon)
            ");
            $stmt->execute([
                ':ma_don' => $ma_don, ':ten' => $khach_hang['ho_ten'],
                ':sdt'    => $khach_hang['sdt'], ':email' => $khach_hang['email'],
                ':dia_chi'=> $khach_hang['dia_chi'], ':tinh' => $khach_hang['tinh_thanh'],
                ':tam'    => $totals['tam_tinh'], ':giam' => $totals['giam_gia'],
                ':phi'    => $totals['phi_ship'],':tong' => $totals['tong_cong'],
                ':coupon' => $coupon,
            ]);
            $don_id = (int)$pdo->lastInsertId();

            // 2. Lưu chi tiết + trừ kho
            $ins = $pdo->prepare("INSERT INTO chi_tiet_don (don_hang_id,san_pham_id,ten_sp,so_luong,don_gia) VALUES (?,?,?,?,?)");
            $upd = $pdo->prepare("UPDATE san_pham SET so_luong = so_luong - ? WHERE id=? AND so_luong >= ?");
            foreach ($_SESSION[self::SESSION_KEY] as $item) {
                $upd->execute([$item['qty'], $item['id'], $item['qty']]);
                if ($upd->rowCount() === 0) throw new RuntimeException("Hết hàng: {$item['ten']}");
                $ins->execute([$don_id, $item['id'], $item['ten'], $item['qty'], $item['gia']]);
            }
            $pdo->commit();
            self::clear();
            return $don_id;
        } catch (Exception $e) {
            $pdo->rollBack();
            throw $e;
        }
    }
}

// ── Demo ──────────────────────────
echo "=== Shopping Cart Demo ===<br>";
$pdo = get_pdo();

ShoppingCart::add(1, 2, $pdo);
ShoppingCart::add(2, 1, $pdo);
echo "Giỏ hàng: " . count(ShoppingCart::getItems()) . " loại<br>";

$totals = ShoppingCart::totals('10%', 'HCM');
echo "Tạm tính: " . number_format($totals['tam_tinh'],0,',','.') . "đ<br>";
echo "Giảm giá: " . number_format($totals['giam_gia'],0,',','.') . "đ<br>";
echo "Phí ship: " . number_format($totals['phi_ship'],0,',','.') . "đ<br>";
echo "Tổng: " . number_format($totals['tong_cong'],0,',','.') . "đ<br>";

ShoppingCart::update(1, 5); // cập nhật số lượng
ShoppingCart::remove(2);    // xóa item
echo "Sau chỉnh sửa: " . count(ShoppingCart::getItems()) . " loại<br>";"""
  ),
  (4, "RESTful API Cho Ứng Dụng Todo",
   "Xây dựng API hoàn chỉnh với authentication, CRUD, validation và OpenAPI documentation.",
   ["CRUD endpoints: GET/POST/PUT/PATCH/DELETE",
    "JWT authentication middleware",
    "Request validation với error messages chuẩn",
    "Response format thống nhất: <code>{success, data, message, meta}</code>",
    "Rate limiting: 60 requests/minute per IP",
    "API documentation với OpenAPI 3.0 spec"],
   ["REST conventions: GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE",
    "HTTP Status: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 422 Validation Error, 429 Too Many Requests",
    "Content negotiation: <code>Accept: application/json</code>",
    "Pagination: <code>?page=1&per_page=20</code>, response có <code>meta.total</code>",
    "CORS: cần cấu hình đúng để frontend gọi được từ domain khác"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 4: RESTFUL API TODO APP
// ════════════════════════════════════

// Chạy: php -S localhost:8000 api.php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }

// ─── Response helpers ─────────────
function ok(mixed $data, string $msg = 'Success', int $code = 200, array $meta = []): never {
    http_response_code($code);
    echo json_encode(array_filter(['success'=>true,'message'=>$msg,'data'=>$data,'meta'=>$meta ?: null]),
        JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT); exit;
}
function err(string $msg, int $code = 400, array $errors = []): never {
    http_response_code($code);
    echo json_encode(array_filter(['success'=>false,'message'=>$msg,'errors'=>$errors ?: null]),
        JSON_UNESCAPED_UNICODE); exit;
}

// ─── Rate limiting ────────────────
function check_rate_limit(int $max = 60): void {
    $key    = 'rl:' . ($_SERVER['REMOTE_ADDR'] ?? '127') . ':' . date('YmdHi');
    $count  = (int)(apcu_fetch($key) ?: 0) + 1;
    apcu_store($key, $count, 60);
    if ($count > $max) {
        header('Retry-After: 60');
        err('Quá nhiều requests. Vui lòng chờ 1 phút', 429);
    }
    header('X-Rate-Limit-Remaining: ' . max(0, $max - $count));
}

// ─── JWT Auth ─────────────────────
function auth(): array {
    $auth  = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
    $token = ltrim(str_ireplace('Bearer', '', $auth));
    if (!$token) err('Bạn chưa đăng nhập', 401);
    try { return JWT::verify($token); }
    catch (Exception $e) { err($e->getMessage(), 401); }
}

// ─── Input helpers ────────────────
function body(): array { return json_decode(file_get_contents('php://input'), true) ?? []; }
function query(string $key, mixed $default = null): mixed { return $_GET[$key] ?? $default; }

// ─── Router ───────────────────────
$method = $_SERVER['REQUEST_METHOD'];
$uri    = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$parts  = explode('/', trim($uri, '/'));
$resource = $parts[1] ?? '';  // 'todos', 'auth'
$id       = isset($parts[2]) ? (int)$parts[2] : null;

// check_rate_limit();  // Bật nếu có APCu

// ═══════════════════════════════════
// Auth Routes
// ═══════════════════════════════════
if ($resource === 'auth') {
    $action = $parts[2] ?? '';
    if ($method === 'POST' && $action === 'register') {
        $b = body();
        if (empty($b['email']) || empty($b['password'])) err('email/password bắt buộc', 422);
        // ... register logic
        ok(['token' => JWT::create(['uid'=>1,'email'=>$b['email']])], 'Đăng ký thành công', 201);
    }
    if ($method === 'POST' && $action === 'login') {
        $b = body();
        // ... verify credentials
        ok(['token' => JWT::create(['uid'=>1,'email'=>$b['email'] ?? ''])], 'Đăng nhập thành công');
    }
    err('Route không tồn tại', 404);
}

// ═══════════════════════════════════
// Todos Routes (Protected)
// ═══════════════════════════════════
if ($resource === 'todos') {
    $user = auth();  // require JWT

    // In-memory store (thay bằng DB)
    static $TODOS = [
        1 => ['id'=>1,'title'=>'Học PHP','done'=>false,'user_id'=>1,'priority'=>'high'],
        2 => ['id'=>2,'title'=>'Tạo API','done'=>true,'user_id'=>1,'priority'=>'medium'],
        3 => ['id'=>3,'title'=>'Viết test','done'=>false,'user_id'=>1,'priority'=>'low'],
    ];

    // GET /todos – danh sách
    if ($method === 'GET' && $id === null) {
        $items = array_values($TODOS);
        // Filter
        if ($filter = query('done')) {
            $items = array_filter($items, fn($t) => (string)$t['done'] === $filter);
        }
        if ($priority = query('priority')) {
            $items = array_filter($items, fn($t) => $t['priority'] === $priority);
        }
        $items = array_values($items);
        $page  = max(1, (int)query('page', 1));
        $limit = min(50, max(1, (int)query('per_page', 10)));
        $total = count($items);
        $items = array_slice($items, ($page-1)*$limit, $limit);
        ok($items, 'OK', 200, ['total'=>$total,'page'=>$page,'per_page'=>$limit,'total_pages'=>ceil($total/$limit)]);
    }

    // GET /todos/:id – chi tiết
    if ($method === 'GET' && $id) {
        $todo = $TODOS[$id] ?? null;
        if (!$todo || $todo['user_id'] !== $user['uid']) err('Không tìm thấy', 404);
        ok($todo);
    }

    // POST /todos – tạo mới
    if ($method === 'POST') {
        $b = body();
        $errs = [];
        if (empty($b['title']))   $errs['title']    = 'Tiêu đề bắt buộc';
        if (strlen($b['title'] ?? '') > 200) $errs['title'] = 'Tối đa 200 ký tự';
        $valid_priority = ['low','medium','high'];
        if (!empty($b['priority']) && !in_array($b['priority'], $valid_priority)) {
            $errs['priority'] = 'priority: ' . implode('|',$valid_priority);
        }
        if ($errs) err('Dữ liệu không hợp lệ', 422, $errs);
        $new_id = max(array_keys($TODOS)) + 1;
        $TODOS[$new_id] = ['id'=>$new_id,'title'=>$b['title'],'done'=>false,
                           'user_id'=>$user['uid'],'priority'=>$b['priority']??'medium'];
        ok($TODOS[$new_id], 'Tạo thành công', 201);
    }

    // PATCH /todos/:id – cập nhật một phần
    if ($method === 'PATCH' && $id) {
        $todo = $TODOS[$id] ?? null;
        if (!$todo || $todo['user_id'] !== $user['uid']) err('Không tìm thấy', 404);
        $b = body();
        if (isset($b['done']) && is_bool($b['done'])) $TODOS[$id]['done'] = $b['done'];
        if (!empty($b['title'])) $TODOS[$id]['title'] = $b['title'];
        ok($TODOS[$id], 'Cập nhật thành công');
    }

    // DELETE /todos/:id – xóa
    if ($method === 'DELETE' && $id) {
        if (!isset($TODOS[$id])) err('Không tìm thấy', 404);
        $deleted = $TODOS[$id]; unset($TODOS[$id]);
        ok($deleted, 'Xóa thành công');
    }
}

err('Endpoint không tồn tại', 404);"""
  ),
  (5, "Hệ Thống Quản Lý Sinh Viên",
   "Xây dựng CRUD quản lý sinh viên, khóa học, đăng ký và bảng điểm hoàn chỉnh.",
   ["CRUD sinh viên: tìm kiếm, lọc, phân trang",
    "Quản lý khóa học và đăng ký",
    "Bảng điểm: nhập điểm, xếp loại, tính GPA",
    "Import/Export Excel (CSV)",
    "Dashboard thống kê: tỷ lệ đậu, phân bố điểm",
    "Báo cáo PDF (sử dụng HTML to PDF)"],
   ["Quan hệ many-to-many: <code>sinh_vien ↔ khoa_hoc</code> qua <code>dang_ky</code>",
    "GPA tính theo tín chỉ: <code>Σ(điểm × tín_chỉ) / Σtín_chỉ</code>",
    "CSV import: đọc từng dòng, validate, insert batch",
    "<code>header('Content-Type: text/csv')</code>: xuất CSV download",
    "Histogram điểm: GROUP BY khoảng điểm bằng CASE WHEN"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 5: QUẢN LÝ SINH VIÊN
// ════════════════════════════════════

/* Schema:
CREATE TABLE sinh_vien (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ma_sv       VARCHAR(10) UNIQUE NOT NULL,
    ho_ten      VARCHAR(150) NOT NULL,
    ngay_sinh   DATE,
    email       VARCHAR(150) UNIQUE,
    dien_thoai  VARCHAR(20),
    lop         VARCHAR(50),
    khoa        VARCHAR(100),
    nam_nhap    YEAR,
    ảnh         VARCHAR(255),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE khoa_hoc (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ma_kh       VARCHAR(10) UNIQUE NOT NULL,
    ten         VARCHAR(200) NOT NULL,
    tin_chi     INT DEFAULT 3,
    mo_ta       TEXT,
    giang_vien  VARCHAR(100)
);
CREATE TABLE dang_ky (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    sinh_vien_id INT NOT NULL,
    khoa_hoc_id  INT NOT NULL,
    hoc_ky       VARCHAR(10),
    diem_qua_mon DECIMAL(4,2),
    diem_giua_ky DECIMAL(4,2),
    diem_cuoi_ky DECIMAL(4,2),
    diem_tong_ket DECIMAL(4,2) GENERATED ALWAYS AS
        (ROUND(diem_qua_mon*0.1 + diem_giua_ky*0.3 + diem_cuoi_ky*0.6, 2)) STORED,
    trang_thai  ENUM('dang_hoc','hoan_thanh','truot','bo_hoc') DEFAULT 'dang_hoc',
    UNIQUE KEY uq_sv_kh_ky (sinh_vien_id, khoa_hoc_id, hoc_ky)
);
*/

class StudentManager {
    public function __construct(private PDO $pdo) {}

    // ─── Thêm sinh viên ──────────
    public function addStudent(array $data): array {
        $ma_sv = $this->nextMaSV();
        $stmt  = $this->pdo->prepare("
            INSERT INTO sinh_vien (ma_sv, ho_ten, ngay_sinh, email, dien_thoai, lop, khoa, nam_nhap)
            VALUES (:ma,:ho_ten,:ngay,:email,:sdt,:lop,:khoa,:nam)
        ");
        $stmt->execute([
            ':ma'     => $ma_sv,
            ':ho_ten' => $data['ho_ten'],
            ':ngay'   => $data['ngay_sinh'] ?? null,
            ':email'  => $data['email'] ?? null,
            ':sdt'    => $data['dien_thoai'] ?? null,
            ':lop'    => $data['lop'],
            ':khoa'   => $data['khoa'],
            ':nam'    => $data['nam_nhap'] ?? date('Y'),
        ]);
        return $this->findStudent((int)$this->pdo->lastInsertId());
    }

    private function nextMaSV(): string {
        $nam  = date('Y');
        $last = $this->pdo->query("SELECT MAX(CAST(SUBSTR(ma_sv,5) AS UNSIGNED)) FROM sinh_vien WHERE ma_sv LIKE 'SV{$nam}%'")->fetchColumn();
        return sprintf('SV%s%04d', $nam, ($last ?? 0) + 1);
    }

    // ─── Bang điểm & GPA ─────────
    public function getBangDiem(int $sv_id): array {
        $stmt = $this->pdo->prepare("
            SELECT kh.ten AS khoa_hoc, kh.tin_chi, dk.hoc_ky,
                   dk.diem_qua_mon, dk.diem_giua_ky, dk.diem_cuoi_ky,
                   dk.diem_tong_ket, dk.trang_thai,
                   CASE
                       WHEN dk.diem_tong_ket >= 9.0 THEN 'A+'
                       WHEN dk.diem_tong_ket >= 8.5 THEN 'A'
                       WHEN dk.diem_tong_ket >= 8.0 THEN 'B+'
                       WHEN dk.diem_tong_ket >= 7.0 THEN 'B'
                       WHEN dk.diem_tong_ket >= 6.5 THEN 'C+'
                       WHEN dk.diem_tong_ket >= 5.5 THEN 'C'
                       WHEN dk.diem_tong_ket >= 5.0 THEN 'D+'
                       WHEN dk.diem_tong_ket >= 4.0 THEN 'D'
                       ELSE 'F'
                   END AS xep_loai
            FROM dang_ky dk
            JOIN khoa_hoc kh ON kh.id = dk.khoa_hoc_id
            WHERE dk.sinh_vien_id = ? AND dk.trang_thai = 'hoan_thanh'
            ORDER BY dk.hoc_ky, kh.ten
        ");
        $stmt->execute([$sv_id]);
        $bang_diem = $stmt->fetchAll();

        // Tính GPA
        $tong_diem_tc = array_sum(array_map(fn($r) => $r['diem_tong_ket'] * $r['tin_chi'], $bang_diem));
        $tong_tc      = array_sum(array_map(fn($r) => $r['tin_chi'], $bang_diem));
        $gpa          = $tong_tc > 0 ? round($tong_diem_tc / $tong_tc, 2) : 0;

        return ['bang_diem' => $bang_diem, 'tong_tc' => $tong_tc, 'gpa' => $gpa,
                'xep_loai' => $gpa >= 8.5 ? 'Giỏi' : ($gpa >= 7.0 ? 'Khá' : ($gpa >= 5.0 ? 'TB' : 'Yếu'))];
    }

    // ─── Import CSV ───────────────
    public function importCsv(string $file_path): array {
        $handle  = fopen($file_path, 'r');
        fgetcsv($handle); // skip header
        $success = $failed = 0; $errors = [];
        while (($row = fgetcsv($handle)) !== false) {
            try {
                if (count($row) < 5) throw new InvalidArgumentException("Thiếu cột");
                $this->addStudent(['ho_ten'=>$row[0],'ngay_sinh'=>$row[1],'email'=>$row[2],'lop'=>$row[3],'khoa'=>$row[4]]);
                $success++;
            } catch (Exception $e) { $failed++; $errors[] = "Dòng " . ($success+$failed) . ": " . $e->getMessage(); }
        }
        fclose($handle);
        return compact('success', 'failed', 'errors');
    }

    // ─── Export CSV ───────────────
    public function exportCsv(): void {
        header('Content-Type: text/csv; charset=utf-8');
        header('Content-Disposition: attachment; filename="sinh_vien_' . date('Ymd') . '.csv"');
        $f = fopen('php://output', 'w');
        fprintf($f, chr(0xEF).chr(0xBB).chr(0xBF));
        fputcsv($f, ['Mã SV','Họ tên','Ngày sinh','Email','Lớp','Khoa','Năm nhập']);
        $rows = $this->pdo->query("SELECT ma_sv,ho_ten,ngay_sinh,email,lop,khoa,nam_nhap FROM sinh_vien ORDER BY ma_sv")->fetchAll(PDO::FETCH_NUM);
        foreach ($rows as $row) fputcsv($f, $row);
        fclose($f);
    }

    private function findStudent(int $id): array {
        $s = $this->pdo->prepare("SELECT * FROM sinh_vien WHERE id=?");
        $s->execute([$id]); return $s->fetch();
    }
}

// ── Demo ──────────────────────────
echo "=== Student Management Demo ===<br>";
$mgr = new StudentManager(get_pdo());
echo "Features:<br>";
echo "✅ Auto mã SV theo năm: SV20240001<br>";
echo "✅ GPA tính theo tín chỉ có trọng số<br>";
echo "✅ Generated column diem_tong_ket trong MySQL<br>";
echo "✅ Import/Export CSV với BOM UTF-8<br>";
echo "✅ Xếp loại chữ: A+/A/B+.../F<br>";"""
  ),
  (6, "Website Bán Hàng Mini Với Admin Panel",
   "Đồ án tổng hợp lớn nhất: website bán hàng đầy đủ với shop frontend và admin backend.",
   ["Frontend: trang chủ, danh mục, tìm kiếm, chi tiết SP, giỏ hàng, checkout",
    "Admin panel: quản lý SP/danh mục, đơn hàng, khách hàng, báo cáo",
    "Authentication: phân quyền admin/staff/user",
    "Upload ảnh sản phẩm multiple images",
    "Mã giảm giá (coupon): % hoặc fixed, có hạn sử dụng",
    "Dashboard: doanh thu realtime, biểu đồ, thống kê"],
   ["Separation của public/ và admin/ paths",
    "CDN cho static assets: images, CSS, JS",
    "Lazy loading ảnh trong danh sách SP",
    ".htaccess: rewrite rules, block direct access các folder nhạy cảm",
    "Cron job: tự động hủy đơn hàng chờ quá 24h, gửi email nhắc nhở"],
   """\
<?php
// ════════════════════════════════════
// ĐỒ ÁN 6: E-COMMERCE MINI
// ════════════════════════════════════

/* Cấu trúc thư mục:
shop/
├── config/
│   ├── app.php          (constants, timezone, locale)
│   ├── database.php     (PDO singleton)
│   └── routes.php       (route definitions)
├── src/
│   ├── Core/
│   │   ├── App.php      (bootstrap, routing)
│   │   ├── Request.php
│   │   ├── Response.php
│   │   └── View.php     (template engine)
│   ├── Middleware/
│   │   ├── Auth.php
│   │   ├── Admin.php
│   │   └── Csrf.php
│   ├── Models/
│   │   ├── Product.php
│   │   ├── Category.php
│   │   ├── Order.php
│   │   ├── Coupon.php
│   │   └── User.php
│   └── Controllers/
│       ├── Shop/
│       │   ├── HomeController.php
│       │   ├── ProductController.php
│       │   └── CartController.php
│       └── Admin/
│           ├── DashboardController.php
│           ├── ProductController.php
│           ├── OrderController.php
│           └── ReportController.php
├── views/
│   ├── layouts/
│   │   ├── shop.php
│   │   └── admin.php
│   ├── shop/
│   │   ├── home.php
│   │   ├── products.php
│   │   ├── product-detail.php
│   │   └── cart.php
│   └── admin/
│       ├── dashboard.php
│       ├── products/index.php
│       └── orders/index.php
├── public/
│   ├── index.php        (entry point)
│   ├── .htaccess
│   ├── css/
│   ├── js/
│   └── uploads/
└── composer.json
*/

// config/app.php
define('APP_NAME', 'NenTang Shop');
define('APP_URL',  'http://localhost:8000');
define('TIMEZONE', 'Asia/Ho_Chi_Minh');
define('UPLOAD_DIR', __DIR__ . '/../public/uploads/');
date_default_timezone_set(TIMEZONE);

// ── Coupon System ─────────────────
class CouponService {
    public function __construct(private PDO $pdo) {}

    public function apply(string $code, float $order_total): array {
        $stmt = $this->pdo->prepare("
            SELECT * FROM coupons
            WHERE code = ? AND active = 1
              AND (expires_at IS NULL OR expires_at > NOW())
              AND (max_uses IS NULL OR used_count < max_uses)
              AND (min_order IS NULL OR min_order <= ?)
        ");
        $stmt->execute([$code, $order_total]);
        $coupon = $stmt->fetch();
        if (!$coupon) throw new RuntimeException("Mã giảm giá không hợp lệ hoặc đã hết hạn");

        $discount = $coupon['type'] === 'percent'
            ? min($order_total, $order_total * $coupon['value'] / 100)
            : min($order_total, $coupon['value']);

        return ['coupon' => $coupon, 'discount' => round($discount, 0)];
    }

    public function use(string $code): void {
        $this->pdo->prepare("UPDATE coupons SET used_count = used_count + 1 WHERE code = ?")->execute([$code]);
    }
}

// ── Dashboard Stats ───────────────
class DashboardService {
    public function __construct(private PDO $pdo) {}

    public function getStats(string $period = 'today'): array {
        $where = match($period) {
            'today'   => "DATE(created_at) = CURDATE()",
            'week'    => "created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)",
            'month'   => "MONTH(created_at) = MONTH(NOW()) AND YEAR(created_at) = YEAR(NOW())",
            'year'    => "YEAR(created_at) = YEAR(NOW())",
            default   => "1=1",
        };
        $don = $this->pdo->query("SELECT COUNT(*) as so_don, SUM(tong_cong) as doanh_thu FROM don_hang WHERE $where")->fetch();
        $sp_ban_chay = $this->pdo->query("
            SELECT sp.ten, SUM(ct.so_luong) as da_ban FROM chi_tiet_don ct
            JOIN don_hang dh ON dh.id = ct.don_hang_id
            JOIN san_pham sp ON sp.id = ct.san_pham_id
            WHERE $where GROUP BY ct.san_pham_id ORDER BY da_ban DESC LIMIT 5
        ")->fetchAll();
        $theo_ngay = $this->pdo->query("
            SELECT DATE(created_at) as ngay, COUNT(*) as so_don, SUM(tong_cong) as doanh_thu
            FROM don_hang WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
            GROUP BY DATE(created_at) ORDER BY ngay
        ")->fetchAll();

        return [
            'so_don'       => (int)$don['so_don'],
            'doanh_thu'    => (float)$don['doanh_thu'],
            'sp_ban_chay'  => $sp_ban_chay,
            'theo_ngay'    => $theo_ngay,
            'tong_sp'      => $this->pdo->query("SELECT COUNT(*) FROM san_pham WHERE active=1")->fetchColumn(),
            'don_cho'      => $this->pdo->query("SELECT COUNT(*) FROM don_hang WHERE trang_thai='pending'")->fetchColumn(),
        ];
    }
}

// ── Demo ──────────────────────────
echo "=== E-Commerce Mini – Tổng Quan ===<br><br>";
echo "<strong>Frontend routes:</strong><br>";
$frontend = ['GET /' => 'Trang chủ + banner + SP nổi bật',
    'GET /shop' => 'Danh sách SP + lọc + tìm kiếm + phân trang',
    'GET /shop/{slug}' => 'Chi tiết SP (ảnh, mô tả, đánh giá)',
    'GET /cart' => 'Giỏ hàng', 'POST /cart/add' => 'Thêm vào giỏ',
    'POST /checkout' => 'Đặt hàng', 'GET /orders/{id}' => 'Xác nhận đơn',
    'GET /account' => 'Trang cá nhân + lịch sử'];
foreach ($frontend as $r => $d) echo "• <code>$r</code>: $d<br>";

echo "<br><strong>Admin routes:</strong><br>";
$admin = ['GET /admin' => '📊 Dashboard realtime',
    'GET/POST /admin/products' => '📦 CRUD sản phẩm + upload ảnh',
    'GET/POST /admin/categories' => '🗂️ Quản lý danh mục',
    'GET/PUT /admin/orders' => '🛒 Đơn hàng + cập nhật trạng thái',
    'GET /admin/customers' => '👥 Danh sách khách hàng',
    'GET/POST /admin/coupons' => '🎫 Mã giảm giá',
    'GET /admin/reports' => '📈 Báo cáo + export Excel'];
foreach ($admin as $r => $d) echo "• <code>$r</code>: $d<br>";

echo "<br>✅ Đồ án hoàn chỉnh – áp dụng mọi kiến thức đã học!<br>";
echo "Stack: PHP 8.2 + MySQL 8 + PDO + Sessions + JWT + Shiki<br>";"""
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
  <meta property="og:title" content="Đồ Án {n}: {title} | NenTang.vn">
  <meta property="og:url" content="https://nentang.vn/">
  <meta property="og:site_name" content="Nền tảng Kiến thức">
  <title>Đồ Án {n}: {title} | NenTang.vn</title>
  <link rel="stylesheet" href="../../shared.css" />
</head>
<body>
  <div class="page-header module-php-p">
    <div class="breadcrumb">
      <a href="../../index.html">PHP Course</a> &rsaquo;
      <a href="../index.html">Đồ Án</a> &rsaquo; Dự Án {n}
    </div>
    <h1>🏗️ Đồ Án {n}: {title}</h1>
    <p>Module 4 – Đồ Án Tổng Hợp PHP</p>
  </div>

  <div class="exercise-page">
    <div class="exercise-box">
      <div class="ex-head">
        <h1>📋 Mô Tả Dự Án</h1>
        <p>{short}</p>
      </div>
      <div class="ex-desc">
        <h3>✅ Tính năng cần xây dựng</h3>
        <ul>
{reqs_li}
        </ul>
        <h3>🧠 Kiến thức áp dụng</h3>
        <ul>
{knows_li}
        </ul>
      </div>
      <div class="ex-work">
        <h3>💻 Code mẫu / Kiến trúc tham khảo</h3>
        <div id="code-highlight">
          <pre id="code-raw" style="display:none">{code_esc}</pre>
        </div>
      </div>
    </div>
  </div>
  <a href="../index.html" class="btn-back">&#8592; Quay lại Đồ Án</a>
{SHIKI_SCRIPT}
</body>
</html>"""

created = 0
for proj in PROJECTS:
    n, title, short, reqs, knows, code = proj
    folder = MOD / f"do-an-{n:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(build(n,title,short,reqs,knows,code), encoding="utf-8")
    print(f"  ✓ Đồ án {n}: {title}")
    created += 1

print(f"\n✅ Đồ Án PHP: {created} dự án tạo thành công tại {MOD}")
