const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const author = "Dương Nguyễn Phú Cường";
const siteName = "Nền tảng Kiến thức";
const baseUrl = "https://nentang.vn/";

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function pad(number) {
  return String(number).padStart(2, "0");
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function write(file, content) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, content, "utf8");
}

function list(items) {
  return items.map((item) => `            <li>${item}</li>`).join("\n");
}

function steps(items) {
  return items.map((item) => `            <li>${item}</li>`).join("\n");
}

function fullSolution(lesson) {
  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${lesson.title}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 24px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      color: #172033;
      background: #f5f7fb;
    }
    a { color: #0f766e; text-decoration: none; font-weight: 700; }
    button {
      border: 0;
      border-radius: 8px;
      padding: 10px 14px;
      color: white;
      background: #0f766e;
      font-weight: 800;
    }
    input, textarea, select {
      min-height: 40px;
      border: 1px solid #ccd6e0;
      border-radius: 8px;
      padding: 8px 10px;
      font: inherit;
    }
${lesson.baseCss ? lesson.baseCss.split("\n").map((line) => `    ${line}`).join("\n") : ""}
${lesson.css.split("\n").map((line) => `    ${line}`).join("\n")}
  </style>
</head>
<body>
${lesson.html.split("\n").map((line) => `  ${line}`).join("\n")}
</body>
</html>`;
}

function previewFrame(lesson, label) {
  return `<div class="result-panel">
            <div class="result-head">
              <h3>${label}</h3>
              <span>Preview chạy trực tiếp từ HTML/CSS của bài</span>
            </div>
            <iframe class="result-frame" title="${esc(label)}" srcdoc="${esc(fullSolution(lesson))}"></iframe>
          </div>`;
}

function seo(title, description, cssHref) {
  return `  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="${esc(description)}" />
  <meta name="keywords" content="CSS Flexbox, học CSS, layout web, frontend, bài tập CSS, responsive, NenTang.vn" />
  <meta name="author" content="${author}" />
  <meta property="og:locale" content="vi_VN" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="${esc(title)}" />
  <meta property="og:description" content="${esc(description)}" />
  <meta property="og:url" content="${baseUrl}" />
  <meta property="og:site_name" content="${siteName}" />
  <title>${esc(title)}</title>
  <link rel="stylesheet" href="${cssHref}" />`;
}

function topbar(prefix) {
  return `<header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="${prefix}index.html"><span class="brand-mark">F</span><span>CSS Flexbox</span></a>
      <nav class="nav-links" aria-label="Điều hướng khóa học">
        <a href="${prefix}../index.html">Trang chủ</a>
        <a href="${prefix}index.html#modules">Module</a>
        <a href="${prefix}index.html#playground">Playground</a>
      </nav>
    </div>
  </header>`;
}

const baseBoxCss = `.demo-surface {
  border: 2px dashed #94a3b8;
  border-radius: 10px;
  padding: 16px;
  background: #ffffff;
}

.demo-box {
  border: 1px solid #ccd6e0;
  border-radius: 8px;
  padding: 14px;
  background: #ffffff;
}

.demo-item {
  border: 2px solid #0f766e;
  border-radius: 8px;
  padding: 12px;
  background: #ccfbf1;
  color: #115e59;
  font-weight: 800;
  text-align: center;
}`;

const componentBaseCss = `${baseBoxCss}
.card, .panel, .toolbar, .site-header, .comment, .form-row, .tabs, .footer-col, .product-card, .profile-card, .chat-row, .summary-box {
  border: 1px solid #d9e2ec;
  border-radius: 10px;
  background: #ffffff;
  padding: 14px;
}
.muted { color: #64748b; }
.avatar {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #e85d4f;
  color: white;
  font-weight: 900;
}
.badge {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 5px 10px;
  background: #e0f2fe;
  color: #075985;
  font-weight: 800;
}`;

const lessons = {
  flexIntro: {
    title: "Flexbox là gì và khi nào nên dùng",
    description: "Hiểu Flexbox là công cụ bố cục một chiều, biết khi nào dùng Flexbox thay vì float, table hoặc CSS Grid.",
    objectives: [
      "Nhận ra Flexbox phù hợp cho menu, toolbar, hàng avatar, card list và các bố cục một chiều.",
      "Phân biệt bài toán một chiều của Flexbox với bài toán hai chiều của CSS Grid.",
      "Chọn đúng phần tử cha để bật <code>display: flex</code>."
    ],
    theory: [
      "Flexbox giải quyết việc sắp xếp các phần tử con trên một hàng hoặc một cột. Nó mạnh ở việc căn giữa, chia khoảng cách, cho item co giãn và xuống dòng.",
      "Nếu layout cần kiểm soát cả hàng lẫn cột như bảng ảnh đều nhau, CSS Grid thường phù hợp hơn. Nếu bạn đang xử lý một hàng menu, một nhóm nút, một card có header-body-footer, Flexbox thường là lựa chọn nhanh và rõ."
    ],
    workflow: [
      "Nhìn giao diện và khoanh vùng nhóm phần tử cần xếp theo một hàng hoặc một cột.",
      "Xác định phần tử cha trực tiếp của nhóm đó.",
      "Bật <code>display: flex</code> trên phần tử cha, sau đó mới thêm căn chỉnh."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 12px;
}`,
    html: `<section class="demo-surface">
  <div class="demo-item">Logo</div>
  <div class="demo-item">Menu</div>
  <div class="demo-item">Nút đăng nhập</div>
</section>`,
    css: `.demo-surface {
  display: flex;
  align-items: center;
  gap: 12px;
}`,
    baseCss: baseBoxCss,
    exercise: "Tạo một header đơn giản gồm logo, 3 link menu và một nút đăng nhập. Không cần responsive ở bài này, chỉ cần chứng minh bạn chọn đúng flex container.",
    practice: [
      "Tạo <code>header.site-header</code> chứa logo, nav và button.",
      "Bật <code>display: flex</code> trên header.",
      "Thêm <code>gap</code> để tạo khoảng cách giữa các item.",
      "Dùng DevTools kiểm tra các phần tử con trực tiếp của header."
    ],
    criteria: [
      "Logo, nav và button nằm trên một hàng.",
      "CSS không dùng float hoặc table.",
      "Bạn chỉ ra được phần tử nào là container và phần tử nào là item."
    ],
    mistakes: [
      "Bật <code>display: flex</code> trên từng link thay vì trên header.",
      "Dùng margin cho mọi item trước khi thử <code>gap</code>.",
      "Chọn CSS Grid cho một hàng đơn giản không cần thiết."
    ]
  },
  displayFlex: {
    title: "display: flex, inline-flex và quan hệ container/item",
    description: "Hiểu cách bật Flexbox, sự khác nhau giữa flex và inline-flex, và giới hạn con trực tiếp.",
    objectives: [
      "Dùng đúng <code>display: flex</code> cho container dạng block.",
      "Dùng <code>inline-flex</code> cho badge, button hoặc cụm nhỏ không chiếm cả dòng.",
      "Hiểu chỉ các phần tử con trực tiếp mới trở thành flex item."
    ],
    theory: [
      "<code>display: flex</code> tạo flex formatting context bên trong và bản thân container cư xử như block. <code>inline-flex</code> cũng tạo Flexbox bên trong, nhưng container chỉ rộng theo nội dung.",
      "Flexbox không tự động tác động đến cháu. Nếu một item chứa nhóm nhỏ cần căn riêng, item đó phải được bật flex thêm một lần nữa."
    ],
    workflow: [
      "Tạo hai cụm giống nhau: một cụm block và một cụm inline.",
      "Đặt border cho container để quan sát chiều rộng.",
      "Thêm một nhóm con lồng bên trong và kiểm tra nó có cần flex riêng không."
    ],
    demoCss: `.demo-surface {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}`,
    html: `<p>
  Học viên:
  <span class="badge-line">
    <span>CSS</span>
    <strong>Flexbox</strong>
  </span>
</p>`,
    css: `.badge-line {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid #0f766e;
  border-radius: 999px;
  padding: 6px 10px;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo badge trạng thái gồm icon text và label. Badge phải nằm cùng dòng với một đoạn văn, không chiếm toàn bộ hàng.",
    practice: [
      "Tạo đoạn văn có một <code>span.status-badge</code> bên trong.",
      "Đặt badge là <code>display: inline-flex</code>.",
      "Dùng <code>align-items: center</code> và <code>gap</code>.",
      "So sánh với khi dùng <code>display: flex</code>."
    ],
    criteria: [
      "Badge nằm cùng dòng với text xung quanh.",
      "Icon và label trong badge căn giữa theo chiều dọc.",
      "Bạn giải thích được vì sao dùng inline-flex."
    ],
    mistakes: [
      "Dùng <code>display: flex</code> làm badge chiếm nguyên dòng.",
      "Kỳ vọng Flexbox tác động đến phần tử cháu chưa được bật flex.",
      "Dùng line-height lớn để căn dọc thay vì <code>align-items</code>."
    ]
  },
  axis: {
    title: "Main axis, cross axis và flex-direction",
    description: "Nắm trục chính, trục phụ và cách flex-direction làm thay đổi ý nghĩa căn chỉnh.",
    objectives: [
      "Giải thích được main axis và cross axis bằng ví dụ trực quan.",
      "Dự đoán được tác động của <code>row</code>, <code>column</code>, <code>row-reverse</code>.",
      "Biết vì sao <code>justify-content</code> không phải lúc nào cũng là căn ngang."
    ],
    theory: [
      "Main axis là hướng item chạy chính. Với <code>row</code>, item chạy ngang. Với <code>column</code>, item chạy dọc. Cross axis luôn vuông góc với main axis.",
      "Khi đổi <code>flex-direction</code>, ý nghĩa trực quan của <code>justify-content</code> và <code>align-items</code> cũng đổi theo. Đây là nguồn gây nhầm lẫn phổ biến nhất."
    ],
    workflow: [
      "Tạo container có 3 item.",
      "Thử <code>row</code> rồi <code>column</code>.",
      "Quan sát item di chuyển theo trục nào khi đổi <code>justify-content</code>."
    ],
    demoCss: `.demo-surface {
  min-height: 220px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
}`,
    html: `<section class="demo-surface">
  <div class="demo-item">Bước 1</div>
  <div class="demo-item">Bước 2</div>
  <div class="demo-item">Bước 3</div>
</section>`,
    css: `.demo-surface {
  min-height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
}`,
    baseCss: baseBoxCss,
    exercise: "Tạo một quy trình 3 bước. Desktop hiển thị theo hàng ngang, mobile hiển thị theo cột dọc.",
    practice: [
      "Tạo container <code>.steps</code> chứa 3 item.",
      "Desktop dùng <code>flex-direction: row</code>.",
      "Trong media query dưới 640px, chuyển sang <code>column</code>.",
      "Thử thêm <code>justify-content</code> và mô tả nó đang căn theo trục nào."
    ],
    criteria: [
      "Desktop xếp ngang, mobile xếp dọc.",
      "Không dùng reverse để sửa thứ tự HTML sai.",
      "Bạn mô tả được main axis ở mỗi trạng thái."
    ],
    mistakes: [
      "Nghĩ <code>justify-content</code> luôn là căn ngang.",
      "Dùng <code>column</code> nhưng vẫn căn chỉnh theo tư duy row.",
      "Đảo thứ tự bằng reverse làm thứ tự đọc khó hiểu."
    ]
  },
  justify: {
    title: "justify-content: phân phối item trên trục chính",
    description: "Dùng justify-content để căn cụm item hoặc phân phối khoảng trống trên main axis.",
    objectives: [
      "Dùng đúng <code>justify-content</code> khi container còn khoảng trống.",
      "Phân biệt <code>center</code>, <code>space-between</code>, <code>space-around</code>, <code>space-evenly</code>.",
      "Áp dụng vào pagination, toolbar hoặc menu phụ."
    ],
    theory: [
      "<code>justify-content</code> phân phối khoảng trống trên main axis. Nếu tổng kích thước item đã chiếm hết container, bạn sẽ không thấy nhiều khác biệt.",
      "<code>space-between</code> đẩy item đầu và cuối ra hai biên. <code>center</code> gom cụm item vào giữa. Với UI thật, đôi khi auto margin rõ nghĩa hơn justify-content."
    ],
    workflow: [
      "Đảm bảo container rộng hơn tổng item.",
      "Thử từng giá trị justify-content và ghi lại khác biệt.",
      "Chọn giá trị theo mục tiêu giao diện, không chọn theo cảm giác."
    ],
    demoCss: `.demo-surface {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}`,
    html: `<nav class="pager">
  <a href="#">Trước</a>
  <a href="#">1</a>
  <a href="#">2</a>
  <a href="#">3</a>
  <a href="#">Sau</a>
</nav>`,
    css: `.pager {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.pager a:first-child {
  margin-right: auto;
}

.pager a:last-child {
  margin-left: auto;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo thanh phân trang: nút Trước sát trái, các số trang ở giữa, nút Sau sát phải.",
    practice: [
      "Tạo <code>nav.pager</code> với 5 link.",
      "Đặt <code>display: flex</code> và <code>gap</code>.",
      "Dùng <code>justify-content</code> cho nhóm số trang.",
      "Dùng auto margin cho nút Trước/Sau nếu cần tách biên."
    ],
    criteria: [
      "Các số trang nằm cân đối ở giữa.",
      "Nút Trước và Sau không dính vào nhóm số.",
      "Không dùng position absolute."
    ],
    mistakes: [
      "Dùng justify-content nhưng container không còn khoảng trống.",
      "Cố xử lý mọi thứ bằng margin tay.",
      "Nhầm main axis sau khi đổi flex-direction."
    ]
  },
  align: {
    title: "align-items và align-self: căn theo trục phụ",
    description: "Căn item theo cross axis và xử lý item riêng biệt bằng align-self.",
    objectives: [
      "Căn các item cao thấp khác nhau theo đầu, giữa hoặc cuối hàng.",
      "Dùng <code>align-self</code> cho item đặc biệt.",
      "Hiểu vì sao container cần chiều cao để thấy rõ căn dọc."
    ],
    theory: [
      "<code>align-items</code> đặt trên container và căn toàn bộ item theo cross axis. Với row, nó thường là căn dọc. Với column, nó thường là căn ngang.",
      "<code>align-self</code> đặt trên một item để ghi đè align-items cho riêng item đó. Dùng nó cho badge, nút hoặc nhãn trạng thái cần lệch khỏi nhóm."
    ],
    workflow: [
      "Tạo hàng có avatar, text và badge.",
      "Đặt container cao hơn nội dung để thấy cross axis.",
      "Thử <code>align-items: center</code>, sau đó dùng <code>align-self</code> cho badge."
    ],
    demoCss: `.demo-surface {
  min-height: 180px;
  display: flex;
  align-items: center;
  gap: 12px;
}`,
    html: `<article class="comment">
  <div class="avatar">A</div>
  <div>
    <strong>Nguyễn Văn A</strong>
    <p class="muted">Đang học CSS Flexbox</p>
  </div>
  <span class="badge">Online</span>
</article>`,
    css: `.comment {
  min-height: 120px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.comment .badge {
  align-self: flex-start;
  margin-left: auto;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo một dòng user gồm avatar, tên, mô tả và badge. Avatar/text căn giữa theo chiều dọc, badge nằm trên cùng bên phải.",
    practice: [
      "Tạo <code>article.user-row</code> gồm avatar, content và badge.",
      "Đặt row là flex container.",
      "Dùng <code>align-items: center</code> cho toàn hàng.",
      "Dùng <code>align-self: flex-start</code> cho badge."
    ],
    criteria: [
      "Avatar và text căn giữa theo chiều dọc.",
      "Badge nằm trên cùng, không kéo lệch cả hàng.",
      "Không dùng padding giả để căn dọc."
    ],
    mistakes: [
      "Đặt <code>align-items</code> trên item.",
      "Không đặt chiều cao nên không thấy khác biệt.",
      "Dùng <code>vertical-align</code> trong flex layout."
    ]
  },
  gapWrap: {
    title: "gap, flex-wrap và align-content",
    description: "Tạo khoảng cách sạch, cho item xuống dòng và căn nhiều dòng flex.",
    objectives: [
      "Dùng <code>gap</code> thay cho margin rời rạc.",
      "Cho item xuống dòng bằng <code>flex-wrap: wrap</code>.",
      "Phân biệt <code>align-items</code> với <code>align-content</code> khi có nhiều dòng."
    ],
    theory: [
      "<code>gap</code> tạo khoảng cách giữa item, không tạo khoảng ngoài container. Khi item wrap, gap kiểm soát cả khoảng ngang và dọc.",
      "<code>align-content</code> chỉ rõ khi có nhiều dòng flex và container còn khoảng trống theo cross axis. Nếu chỉ có một dòng, nó gần như không có tác dụng."
    ],
    workflow: [
      "Tạo nhiều tag hoặc card nhỏ.",
      "Bật <code>flex-wrap: wrap</code>.",
      "Dùng <code>gap</code> để kiểm soát khoảng cách.",
      "Tăng chiều cao container rồi thử <code>align-content</code>."
    ],
    demoCss: `.demo-surface {
  min-height: 220px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  gap: 12px;
}`,
    html: `<section class="tags">
  <span>HTML</span><span>CSS</span><span>Flexbox</span>
  <span>Responsive</span><span>Layout</span><span>UI</span>
</section>`,
    css: `.tags {
  min-height: 220px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  gap: 10px;
}

.tags span {
  border-radius: 999px;
  padding: 8px 12px;
  background: #ccfbf1;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo danh sách 12 kỹ năng. Các tag tự xuống dòng và được căn thành nhóm ở giữa khung cao 260px.",
    practice: [
      "Tạo container <code>.tags</code> chứa ít nhất 12 span.",
      "Bật <code>display: flex</code> và <code>flex-wrap: wrap</code>.",
      "Dùng <code>gap</code> thay vì margin cho từng tag.",
      "Đặt container đủ cao rồi thử <code>align-content</code>."
    ],
    criteria: [
      "Tag không tràn ngang trên mobile.",
      "Khoảng cách ngang/dọc đều.",
      "Bạn giải thích được khi nào align-content có tác dụng."
    ],
    mistakes: [
      "Quên <code>flex-wrap</code> làm item bị ép một dòng.",
      "Dùng margin khiến khoảng cách dòng khó đều.",
      "Dùng align-content khi chỉ có một dòng item."
    ]
  },
  flexItem: {
    title: "flex-grow, flex-shrink, flex-basis và shorthand flex",
    description: "Kiểm soát cách từng item chiếm phần trống, co lại và có kích thước khởi đầu.",
    objectives: [
      "Đọc được <code>flex: grow shrink basis</code>.",
      "Dùng <code>flex: 1</code> cho vùng cần chiếm phần còn lại.",
      "Dùng <code>flex: 0 0 ...</code> cho item cần giữ kích thước."
    ],
    theory: [
      "<code>flex-grow</code> chia phần trống còn lại. <code>flex-shrink</code> cho phép item co khi thiếu chỗ. <code>flex-basis</code> là kích thước khởi đầu trên main axis.",
      "Các công thức hay dùng: content chính <code>flex: 1</code>, sidebar <code>flex: 0 0 240px</code>, card responsive <code>flex: 1 1 220px</code>."
    ],
    workflow: [
      "Chọn item nào cần cố định và item nào cần co giãn.",
      "Đặt item cố định bằng <code>flex: 0 0 kích-thước</code>.",
      "Đặt item co giãn bằng <code>flex: 1</code>.",
      "Thêm <code>min-width: 0</code> cho item chứa text dài."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 12px;
}
.demo-item:nth-child(2) {
  flex: 1;
}`,
    html: `<div class="search-row">
  <a class="logo" href="#">NenTang</a>
  <input type="search" placeholder="Tìm bài học Flexbox">
  <button>Tìm</button>
</div>`,
    css: `.search-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-row input {
  flex: 1;
  min-width: 0;
}

.search-row .logo,
.search-row button {
  flex: 0 0 auto;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo thanh tìm kiếm: logo giữ kích thước, input chiếm phần còn lại, button giữ kích thước tự nhiên.",
    practice: [
      "Tạo container gồm logo, input và button.",
      "Đặt container là flex row.",
      "Gán input <code>flex: 1</code> và <code>min-width: 0</code>.",
      "Gán logo/button <code>flex: 0 0 auto</code>."
    ],
    criteria: [
      "Input co giãn theo chiều rộng màn hình.",
      "Logo và button không bị ép méo.",
      "Không dùng width cố định cho input."
    ],
    mistakes: [
      "Gán <code>flex: 1</code> cho toàn bộ item.",
      "Quên <code>min-width: 0</code> khi text dài.",
      "Nhầm <code>flex-basis</code> với width trong mọi tình huống."
    ]
  },
  orderAutoNested: {
    title: "order, auto margin, nested flex và debug thực tế",
    description: "Dùng các kỹ thuật thường gặp sau khi đã nắm nền tảng Flexbox.",
    objectives: [
      "Dùng auto margin để đẩy item trong flex layout.",
      "Tạo nested flex khi một item cần căn chỉnh con bên trong.",
      "Dùng <code>order</code> có kiểm soát và biết rủi ro accessibility."
    ],
    theory: [
      "Auto margin hấp thụ khoảng trống trên trục tương ứng. <code>margin-left: auto</code> thường đẩy item sang cuối hàng; <code>margin-top: auto</code> đẩy nút xuống cuối card dạng column.",
      "Một flex item có thể là flex container khác. Đây là cách làm card có header/body/footer, toolbar có nhiều nhóm nút, dashboard có nhiều vùng.",
      "<code>order</code> chỉ nên dùng khi thật sự cần đổi hiển thị. Thứ tự DOM vẫn quan trọng với keyboard và screen reader."
    ],
    workflow: [
      "Dùng auto margin trước khi nghĩ đến position absolute.",
      "Nếu cần căn nội dung bên trong item, bật flex trên item đó.",
      "Khi dùng order, kiểm tra thứ tự đọc và thứ tự tab."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 12px;
}
.demo-item:nth-child(4) {
  margin-left: auto;
}`,
    html: `<article class="task-card">
  <header>
    <h3>Bài tập Flexbox</h3>
    <span class="badge">Cần làm</span>
  </header>
  <p>Đọc lý thuyết, tự code lại ví dụ và so sánh với bài giải.</p>
  <button>Đánh dấu xong</button>
</article>`,
    css: `.task-card {
  min-height: 240px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.task-card header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.task-card .badge {
  margin-left: auto;
}

.task-card button {
  margin-top: auto;
  align-self: flex-start;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo task card có header gồm tiêu đề và badge bên phải, nút hành động luôn nằm cuối card.",
    practice: [
      "Đặt card là flex column.",
      "Đặt header trong card là nested flex.",
      "Dùng <code>margin-left: auto</code> cho badge.",
      "Dùng <code>margin-top: auto</code> cho button.",
      "Mở DevTools để kiểm tra container lồng nhau."
    ],
    criteria: [
      "Badge nằm bên phải header.",
      "Button nằm cuối card dù mô tả ngắn hay dài.",
      "Không dùng absolute positioning."
    ],
    mistakes: [
      "Dùng <code>order</code> thay cho HTML đúng thứ tự.",
      "Quên nested flex cho header.",
      "Đẩy nút bằng margin cố định làm vỡ khi nội dung dài."
    ]
  }
};

function withTitle(lesson, title, description) {
  return { ...lesson, title, description: description || lesson.description };
}

function cardListLesson(title, description, exerciseTitle) {
  return {
    title,
    description,
    objectives: [
      "Tạo danh sách card tự chia cột theo chiều rộng container.",
      "Dùng <code>flex-wrap</code>, <code>gap</code> và <code>flex: 1 1 ...</code> đúng cách.",
      "Giữ footer/nút trong card nằm cuối để các card nhìn đều."
    ],
    theory: [
      "Danh sách card là pattern Flexbox rất thực tế. Container quyết định wrap và gap; từng card quyết định kích thước tối thiểu bằng flex-basis.",
      "Nếu card có nội dung dài ngắn khác nhau, đặt card là flex column và dùng <code>margin-top: auto</code> cho khu vực action."
    ],
    workflow: [
      "Xác định kích thước card tối thiểu hợp lý.",
      "Đặt container <code>display: flex</code>, <code>flex-wrap: wrap</code>.",
      "Đặt card <code>flex: 1 1 220px</code> hoặc tương tự.",
      "Kiểm tra mobile để card xuống một cột khi cần."
    ],
    demoCss: `.demo-surface {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.demo-item {
  flex: 1 1 140px;
}`,
    html: `<section class="card-list">
  <article class="card">
    <h3>Gói Cơ bản</h3>
    <p class="muted">Phù hợp người mới bắt đầu.</p>
    <button>Chọn gói</button>
  </article>
  <article class="card featured">
    <h3>Gói Thực hành</h3>
    <p class="muted">Có bài tập và bài giải.</p>
    <button>Chọn gói</button>
  </article>
  <article class="card">
    <h3>Gói Dự án</h3>
    <p class="muted">Luyện giao diện thực tế.</p>
    <button>Chọn gói</button>
  </article>
</section>`,
    css: `.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
}

.card {
  flex: 1 1 220px;
  display: flex;
  flex-direction: column;
  min-height: 220px;
}

.card button {
  margin-top: auto;
  align-self: flex-start;
}

.featured {
  border-color: #0f766e;
}`,
    baseCss: componentBaseCss,
    exercise: exerciseTitle || "Tạo 6 card khóa học tự chia cột và xuống dòng. Mỗi card có tiêu đề, mô tả và nút nằm cuối.",
    practice: [
      "Tạo container chứa ít nhất 6 card.",
      "Dùng <code>display: flex</code>, <code>flex-wrap: wrap</code>, <code>gap</code>.",
      "Đặt từng card <code>flex: 1 1 220px</code>.",
      "Đặt card là flex column và đẩy button xuống cuối.",
      "Kiểm tra ở desktop, tablet và mobile."
    ],
    criteria: [
      "Card xuống dòng mượt, không tràn ngang.",
      "Khoảng cách ngang/dọc đồng nhất.",
      "Button trong các card nằm thẳng hàng tương đối."
    ],
    mistakes: [
      "Đặt width cố định khiến mobile tràn.",
      "Quên <code>flex-wrap</code>.",
      "Đẩy nút bằng margin cố định thay vì <code>margin-top: auto</code>."
    ]
  };
}

function navbarLesson(title = "Navbar responsive thực tế") {
  return {
    title,
    description: "Tạo header responsive có logo, menu, nút hành động và hành vi xuống dòng rõ ràng.",
    objectives: [
      "Tạo navbar gồm logo, nhóm link và nút hành động bằng Flexbox.",
      "Dùng auto margin để tách nhóm menu/action.",
      "Cho navbar xuống dòng hợp lý trên màn hình nhỏ."
    ],
    theory: [
      "Navbar thường là một flex row gồm logo, nav và action. Logo giữ kích thước tự nhiên; nav hoặc action được đẩy sang phải bằng auto margin.",
      "Trên mobile, ép toàn bộ link vào một hàng thường làm vỡ giao diện. Cho phép wrap hoặc chuyển nav thành hàng riêng là lựa chọn thực tế."
    ],
    workflow: [
      "Viết HTML theo thứ tự logo, nav, action.",
      "Bật flex trên header.",
      "Dùng <code>margin-left: auto</code> cho nav hoặc action.",
      "Thêm <code>flex-wrap: wrap</code> và media query."
    ],
    demoCss: `.demo-surface {
  display: flex;
  align-items: center;
  gap: 12px;
}
.demo-item:nth-child(2) {
  margin-left: auto;
}`,
    html: `<header class="site-header">
  <a class="logo" href="#">NenTang</a>
  <nav class="site-nav">
    <a href="#">Khóa học</a>
    <a href="#">Bài tập</a>
    <a href="#">Liên hệ</a>
  </nav>
  <button>Đăng nhập</button>
</header>`,
    css: `.site-header {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}

.site-nav {
  display: flex;
  gap: 12px;
  margin-left: auto;
}

@media (max-width: 640px) {
  .site-nav {
    width: 100%;
    margin-left: 0;
    flex-wrap: wrap;
  }
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo navbar cho trang khóa học: logo trái, menu phải, nút đăng nhập. Mobile menu xuống hàng riêng.",
    practice: [
      "Tạo <code>header.site-header</code> với logo, nav và button.",
      "Đặt header là flex container.",
      "Dùng <code>margin-left: auto</code> cho nav.",
      "Bật wrap và xử lý nav trên mobile.",
      "Kiểm tra khi tên link dài hơn bình thường."
    ],
    criteria: [
      "Desktop nằm gọn một hàng.",
      "Mobile không tràn ngang.",
      "Thứ tự HTML vẫn tự nhiên."
    ],
    mistakes: [
      "Dùng position absolute để đẩy menu.",
      "Không bật wrap nên link bị tràn.",
      "Đặt margin trái cho từng link thay vì dùng gap."
    ]
  };
}

function toolbarLesson() {
  return {
    title: "Toolbar và nhóm nút hành động",
    description: "Tạo toolbar có nhiều nhóm nút, nút nguy hiểm nằm tách về cuối hàng.",
    objectives: [
      "Sắp xếp nhiều button trong toolbar bằng Flexbox.",
      "Tách nhóm nút bằng auto margin.",
      "Cho toolbar wrap khi không đủ chiều ngang."
    ],
    theory: [
      "Toolbar là nhóm thao tác, khác menu điều hướng. Các nút cần khoảng cách đều, dễ bấm và có thể chia nhóm chính/phụ.",
      "Auto margin phù hợp để đẩy một nhóm nút sang cuối hàng mà không phải dùng position."
    ],
    workflow: [
      "Tạo một container toolbar chứa các button.",
      "Bật flex, align center và gap.",
      "Gán <code>margin-left: auto</code> cho nhóm cuối.",
      "Bật wrap để không tràn mobile."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 10px;
}
.demo-item:nth-child(4) {
  margin-left: auto;
}`,
    html: `<div class="toolbar">
  <button>Lưu</button>
  <button>Xem trước</button>
  <button>Xuất bản</button>
  <button class="danger">Xóa</button>
</div>`,
    css: `.toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.toolbar .danger {
  margin-left: auto;
  background: #e85d4f;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo toolbar soạn bài có Lưu, Xem trước, Xuất bản và Xóa. Nút Xóa nằm tách sang phải trên desktop.",
    practice: [
      "Tạo <code>.toolbar</code> chứa 4 button.",
      "Bật flex và gap.",
      "Gán class <code>.danger</code> cho nút Xóa.",
      "Dùng <code>margin-left: auto</code> cho nút Xóa.",
      "Bật wrap để mobile không vỡ."
    ],
    criteria: [
      "Các nút chính nằm cạnh nhau.",
      "Nút Xóa tách sang phải ở desktop.",
      "Mobile vẫn hiển thị đủ nút."
    ],
    mistakes: [
      "Dùng float cho nút cuối.",
      "Không wrap khiến nút bị cắt.",
      "Dùng nhiều margin cố định giữa từng nút."
    ]
  };
}

function mediaLesson(title = "Media object: avatar và nội dung") {
  return {
    title,
    description: "Tạo hàng avatar cố định, nội dung co giãn và action/time nằm cuối hàng.",
    objectives: [
      "Tạo layout avatar + nội dung bằng Flexbox.",
      "Giữ avatar không bị co lại.",
      "Cho phần nội dung chiếm phần còn lại và xử lý text dài."
    ],
    theory: [
      "Media object xuất hiện ở comment, chat row, notification và profile snippet. Avatar/icon thường cố định; nội dung co giãn; action hoặc thời gian nằm cuối.",
      "<code>min-width: 0</code> trên phần nội dung giúp text dài không làm vỡ layout."
    ],
    workflow: [
      "Tạo item gồm avatar, body và time/action.",
      "Bật flex trên item.",
      "Avatar dùng <code>flex: 0 0 52px</code>.",
      "Body dùng <code>flex: 1</code> và <code>min-width: 0</code>."
    ],
    demoCss: `.demo-surface {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.demo-item:nth-child(2) {
  flex: 1;
}`,
    html: `<article class="comment">
  <div class="avatar">A</div>
  <div class="comment-body">
    <strong>Nguyễn Văn A</strong>
    <p class="muted">Bố cục này giữ avatar cố định và nội dung co giãn.</p>
  </div>
  <time>09:30</time>
</article>`,
    css: `.comment {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.avatar {
  flex: 0 0 52px;
}

.comment-body {
  flex: 1;
  min-width: 0;
}

.comment time {
  margin-left: auto;
  color: #64748b;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo một comment row gồm avatar, tên, nội dung và thời gian. Nội dung dài không được đẩy thời gian ra khỏi khung.",
    practice: [
      "Avatar dùng kích thước cố định.",
      "Body dùng <code>flex: 1</code>.",
      "Thêm <code>min-width: 0</code> cho body.",
      "Time dùng <code>margin-left: auto</code>.",
      "Thử nội dung dài để kiểm tra."
    ],
    criteria: [
      "Avatar không bị méo.",
      "Nội dung co giãn đúng.",
      "Time nằm bên phải và không chồng text."
    ],
    mistakes: [
      "Không khóa avatar khiến avatar bị ép nhỏ.",
      "Quên <code>min-width: 0</code>.",
      "Dùng width cố định cho body."
    ]
  };
}

function formLesson() {
  return {
    title: "Form row và newsletter form responsive",
    description: "Tạo form có input co giãn, button giữ kích thước và chuyển thành cột trên mobile.",
    objectives: [
      "Sắp xếp label, input và button bằng Flexbox.",
      "Cho input chiếm phần còn lại.",
      "Chuyển form thành cột trên màn hình nhỏ."
    ],
    theory: [
      "Form ngang thường có input cần co giãn và button cần giữ kích thước. Flexbox xử lý tốt bằng <code>flex: 1</code> cho input wrapper.",
      "Mobile cần ưu tiên dễ nhập liệu, nên form thường chuyển thành cột và các control rộng 100%."
    ],
    workflow: [
      "Tạo form gồm label, input, button.",
      "Bật flex và gap.",
      "Input wrapper dùng <code>flex: 1</code>.",
      "Media query chuyển sang column."
    ],
    demoCss: `.demo-surface {
  display: flex;
  align-items: center;
  gap: 12px;
}
.demo-item:nth-child(2) {
  flex: 1;
}`,
    html: `<form class="newsletter">
  <label for="email">Nhận bài mới</label>
  <input id="email" type="email" placeholder="email@example.com">
  <button>Đăng ký</button>
</form>`,
    css: `.newsletter {
  display: flex;
  align-items: center;
  gap: 12px;
}

.newsletter input {
  flex: 1;
  min-width: 0;
}

@media (max-width: 640px) {
  .newsletter {
    align-items: stretch;
    flex-direction: column;
  }
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo form đăng ký nhận tin. Desktop label-input-button nằm ngang; mobile chuyển thành cột.",
    practice: [
      "Viết HTML form có label, input và button.",
      "Bật flex trên form.",
      "Gán input <code>flex: 1</code>.",
      "Trong media query, chuyển form sang column.",
      "Đảm bảo input/button dễ bấm trên mobile."
    ],
    criteria: [
      "Input co giãn đúng trên desktop.",
      "Mobile không tràn ngang.",
      "Label vẫn liên kết đúng với input."
    ],
    mistakes: [
      "Đặt width cố định cho input.",
      "Không chuyển layout trên mobile.",
      "Bỏ label làm form kém accessibility."
    ]
  };
}

function sidebarLesson(title = "Sidebar và content layout") {
  return {
    title,
    description: "Tạo layout sidebar cố định và content co giãn cho dashboard hoặc trang quản trị.",
    objectives: [
      "Tạo layout hai vùng: sidebar cố định và content chiếm phần còn lại.",
      "Dùng <code>flex: 0 0 ...</code> và <code>flex: 1</code> đúng vai trò.",
      "Chuyển layout sang cột trên mobile."
    ],
    theory: [
      "Dashboard thường có sidebar cần ổn định chiều rộng và content cần co giãn. Đây là ví dụ kinh điển của flex item sizing.",
      "Content nên có <code>min-width: 0</code> để bảng, card hoặc text dài bên trong không làm cả layout tràn ngang."
    ],
    workflow: [
      "Tạo container <code>.app-layout</code>.",
      "Sidebar dùng kích thước cố định bằng flex-basis.",
      "Content dùng <code>flex: 1</code>.",
      "Media query chuyển container thành column."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 12px;
}
.demo-item:first-child {
  flex: 0 0 120px;
}
.demo-item:nth-child(2) {
  flex: 1;
}`,
    html: `<main class="app-layout">
  <aside class="sidebar">Menu quản trị</aside>
  <section class="content">
    <header class="content-header">
      <h2>Dashboard</h2>
      <button>Thêm mới</button>
    </header>
    <p class="muted">Khu vực nội dung chính chiếm phần còn lại.</p>
  </section>
</main>`,
    css: `.app-layout {
  display: flex;
  min-height: 300px;
}

.sidebar {
  flex: 0 0 220px;
  color: white;
  background: #172033;
}

.content {
  flex: 1;
  min-width: 0;
}

.content-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

@media (max-width: 768px) {
  .app-layout {
    flex-direction: column;
  }
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo dashboard shell gồm sidebar, header nội dung và đoạn mô tả. Mobile sidebar nằm trên content.",
    practice: [
      "Tạo <code>.app-layout</code> gồm sidebar và content.",
      "Đặt layout là flex.",
      "Sidebar dùng <code>flex: 0 0 220px</code>.",
      "Content dùng <code>flex: 1</code> và <code>min-width: 0</code>.",
      "Media query chuyển layout sang column."
    ],
    criteria: [
      "Sidebar giữ chiều rộng trên desktop.",
      "Content chiếm phần còn lại.",
      "Mobile không tạo thanh cuộn ngang."
    ],
    mistakes: [
      "Dùng width cho sidebar nhưng quên content co giãn.",
      "Không thêm <code>min-width: 0</code> cho content.",
      "Sidebar vẫn nằm ngang trên mobile."
    ]
  };
}

function footerLesson() {
  return {
    title: "Footer nhiều cột bằng Flexbox",
    description: "Tạo footer nhiều cột tự xuống dòng khi màn hình hẹp.",
    objectives: [
      "Chia footer thành các cột nội dung có chiều rộng tối thiểu.",
      "Dùng <code>flex-wrap</code> để footer không tràn trên mobile.",
      "Giữ khoảng cách giữa các nhóm link/form nhất quán bằng <code>gap</code>."
    ],
    theory: [
      "Footer thường có các nhóm nội dung độc lập: thương hiệu, link, hỗ trợ, form nhận tin. Đây là bài toán flex-wrap điển hình.",
      "Mỗi cột nên dùng <code>flex: 1 1 220px</code>: được chia phần trống, được xuống dòng, nhưng không bị ép quá hẹp."
    ],
    workflow: [
      "Tạo footer gồm 3 hoặc 4 section.",
      "Bật flex, wrap và gap trên footer.",
      "Đặt từng cột <code>flex: 1 1 220px</code>.",
      "Kiểm tra mobile để mỗi cột vẫn đọc tốt."
    ],
    demoCss: `.demo-surface {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.demo-item {
  flex: 1 1 150px;
}`,
    html: `<footer class="site-footer">
  <section class="footer-col">
    <h3>NenTang</h3>
    <p class="muted">Học lập trình web qua ví dụ thực tế.</p>
  </section>
  <section class="footer-col">
    <h3>Khóa học</h3>
    <a href="#">HTML</a>
    <a href="#">CSS</a>
    <a href="#">JavaScript</a>
  </section>
  <section class="footer-col">
    <h3>Nhận tin</h3>
    <input placeholder="Email của bạn">
    <button>Đăng ký</button>
  </section>
</footer>`,
    css: `.site-footer {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.footer-col {
  flex: 1 1 220px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo footer gồm thông tin thương hiệu, danh sách link và form nhận tin. Các cột tự xuống dòng trên mobile.",
    practice: [
      "Tạo <code>footer.site-footer</code> chứa ít nhất 3 section.",
      "Đặt footer <code>display: flex</code>, <code>flex-wrap: wrap</code>, <code>gap</code>.",
      "Đặt mỗi section <code>flex: 1 1 220px</code>.",
      "Trong từng section, dùng flex column để link/form xếp dọc.",
      "Kiểm tra mobile không có cột nào bị bó quá hẹp."
    ],
    criteria: [
      "Footer chia cột rõ trên desktop.",
      "Các cột xuống dòng tự nhiên trên mobile.",
      "Form nhận tin không làm footer tràn ngang."
    ],
    mistakes: [
      "Đặt width phần trăm cứng khiến cột quá hẹp.",
      "Quên wrap nên footer tràn ngang.",
      "Dùng margin rời rạc thay vì gap."
    ]
  };
}

function modalActionsLesson() {
  return {
    title: "Modal footer và action alignment",
    description: "Căn các nút trong modal footer bằng Flexbox và auto margin.",
    objectives: [
      "Căn nhóm nút hành động về cuối modal.",
      "Tách nút phụ hoặc nút hủy sang trái bằng auto margin.",
      "Giữ thứ tự nút rõ ràng trên mobile."
    ],
    theory: [
      "Modal footer thường có nút phụ và nút chính. Flexbox giúp căn các nút về bên phải, đồng thời vẫn có thể đẩy nút Hủy sang trái.",
      "Auto margin là cách rõ nghĩa hơn position absolute cho trường hợp này."
    ],
    workflow: [
      "Tạo footer chứa nút Hủy, Xóa, Lưu.",
      "Bật flex và gap.",
      "Đẩy nút Hủy bằng <code>margin-right: auto</code> hoặc đẩy nhóm chính bằng <code>margin-left: auto</code>.",
      "Kiểm tra mobile để nút không chồng nhau."
    ],
    demoCss: `.demo-surface {
  display: flex;
  gap: 10px;
}
.demo-item:first-child {
  margin-right: auto;
}`,
    html: `<footer class="modal-actions">
  <button class="secondary">Hủy</button>
  <button class="danger">Xóa</button>
  <button>Lưu thay đổi</button>
</footer>`,
    css: `.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  flex-wrap: wrap;
}

.modal-actions .secondary {
  margin-right: auto;
  background: #64748b;
}

.modal-actions .danger {
  background: #e85d4f;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo modal footer có nút Hủy bên trái, nút Xóa và Lưu thay đổi bên phải. Khi hẹp, các nút được wrap chứ không tràn.",
    practice: [
      "Tạo <code>footer.modal-actions</code> chứa 3 button.",
      "Đặt footer là flex container.",
      "Dùng gap cho khoảng cách giữa nút.",
      "Dùng auto margin để tách nút Hủy.",
      "Bật wrap để mobile an toàn."
    ],
    criteria: [
      "Nút Hủy tách trái, nhóm nút chính ở phải.",
      "Không dùng absolute positioning.",
      "Mobile không tràn nút."
    ],
    mistakes: [
      "Dùng float cho nút Hủy.",
      "Đặt margin cố định lớn làm vỡ mobile.",
      "Đổi thứ tự HTML làm thao tác keyboard khó hiểu."
    ]
  };
}

function navControlsLesson() {
  return {
    title: "Tabs, breadcrumb và pagination",
    description: "Dùng Flexbox để căn các control điều hướng nhỏ.",
    objectives: [
      "Tạo các control điều hướng nhỏ bằng flex row.",
      "Dùng gap và wrap để control không dính hoặc tràn.",
      "Biết khi nào cần auto margin trong pagination."
    ],
    theory: [
      "Tabs, breadcrumb và pagination đều là danh sách item nhỏ theo một hàng. Flexbox phù hợp vì cần căn giữa, chia khoảng cách và wrap khi thiếu chỗ.",
      "Với pagination, auto margin có thể tách nút Trước/Sau khỏi nhóm số trang."
    ],
    workflow: [
      "Chọn control cần xây: tabs, breadcrumb hoặc pagination.",
      "Dùng semantic element như <code>nav</code>.",
      "Bật flex, align center, gap và wrap.",
      "Kiểm tra text dài hoặc nhiều item."
    ],
    demoCss: `.demo-surface {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}`,
    html: `<nav class="tabs">
  <button class="active">Tổng quan</button>
  <button>Bài học</button>
  <button>Bài tập</button>
  <button>Hỏi đáp</button>
</nav>`,
    css: `.tabs {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  border-bottom: 1px solid #d9e2ec;
}

.tabs button {
  border-radius: 8px 8px 0 0;
}

.tabs .active {
  background: #172033;
}`,
    baseCss: componentBaseCss,
    exercise: "Tạo tabs điều hướng cho trang khóa học gồm Tổng quan, Bài học, Bài tập, Hỏi đáp. Các tab wrap khi màn hình hẹp.",
    practice: [
      "Tạo <code>nav.tabs</code> chứa 4 button.",
      "Bật flex, gap và wrap.",
      "Tạo trạng thái active cho tab hiện tại.",
      "Thêm border-bottom để thấy tab gắn với nội dung.",
      "Kiểm tra khi label tab dài hơn."
    ],
    criteria: [
      "Tabs nằm trên một hàng ở desktop.",
      "Tabs wrap tự nhiên ở mobile.",
      "Active state rõ ràng."
    ],
    mistakes: [
      "Dùng width cố định cho mỗi tab.",
      "Không wrap làm tab bị cắt.",
      "Dùng khoảng trắng text thay cho gap."
    ]
  };
}

function mobileLayoutLesson() {
  return {
    ...lessons.axis,
    title: "Đổi bố cục mobile mà không phá thứ tự đọc",
    description: "Chuyển row sang column an toàn trên mobile, hạn chế lạm dụng order/reverse.",
    objectives: [
      "Chuyển layout desktop ngang thành mobile dọc bằng media query.",
      "Giữ HTML theo thứ tự đọc tự nhiên.",
      "Biết khi nào không nên dùng <code>order</code> hoặc reverse."
    ],
    exercise: "Tạo layout gồm nội dung chính và sidebar. Desktop nằm ngang, mobile nội dung chính vẫn đọc trước sidebar.",
    practice: [
      "Viết HTML theo thứ tự content trước, sidebar sau.",
      "Desktop dùng flex row.",
      "Mobile chuyển container sang column.",
      "Không dùng <code>column-reverse</code> để sửa thứ tự.",
      "Dùng keyboard Tab để kiểm tra thứ tự focus."
    ],
    criteria: [
      "Desktop có hai cột.",
      "Mobile nội dung chính đọc trước sidebar.",
      "Không dùng order nếu không có lý do rõ."
    ],
    mistakes: [
      "Dùng reverse làm thứ tự đọc và thứ tự nhìn khác nhau.",
      "Chỉ test desktop.",
      "Ẩn sidebar thay vì sắp xếp lại hợp lý."
    ]
  };
}

function nestedFlexLesson() {
  return {
    ...lessons.orderAutoNested,
    title: "Nested flex trong component phức tạp",
    description: "Tạo component có nhiều flex container lồng nhau nhưng vẫn dễ đọc.",
    objectives: [
      "Tách layout component thành container ngoài và container trong.",
      "Dùng flex column cho card tổng thể, flex row cho header/footer.",
      "Tránh một flex container xử lý quá nhiều trách nhiệm."
    ],
    exercise: "Tạo course card có header gồm title và badge, body mô tả, footer gồm nút và link. Header/footer là flex row, card là flex column.",
    criteria: [
      "Card tổng thể dùng flex column.",
      "Header và footer dùng nested flex.",
      "Button/footer không bị lệch khi mô tả dài."
    ],
    mistakes: [
      "Chỉ bật flex ở card ngoài rồi cố căn mọi thứ.",
      "Dùng position absolute cho badge.",
      "Không chia vùng header/body/footer rõ ràng."
    ]
  };
}

function projectLesson({ title, description, html, css, exercise, practice, criteria }) {
  return {
    title,
    description,
    objectives: [
      "Phân tích yêu cầu đề thành các vùng layout rõ ràng.",
      "Dùng Flexbox đúng vai trò cho từng vùng, không gượng ép một container xử lý mọi thứ.",
      "Hoàn thiện bản desktop và mobile có thể chạy trực tiếp trong trình duyệt."
    ],
    theory: [
      "Với bài thực hành, hãy chia giao diện thành các khối nhỏ: header, danh sách, card, action bar, footer. Mỗi khối có thể là một flex container riêng.",
      "Không phải phần nào cũng cần Flexbox. Chỉ bật flex khi có nhu cầu căn hàng/cột, chia khoảng cách, co giãn hoặc đẩy item."
    ],
    workflow: [
      "Đọc đề và liệt kê các vùng UI cần có.",
      "Viết HTML có nghĩa trước, chưa viết CSS.",
      "Bật Flexbox từng vùng một và kiểm tra preview.",
      "Thêm responsive sau khi desktop ổn."
    ],
    demoCss: `.demo-surface {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.demo-item {
  flex: 1 1 160px;
}`,
    html,
    css,
    baseCss: componentBaseCss,
    exercise,
    practice,
    criteria,
    mistakes: [
      "Viết HTML thiếu vùng nên CSS phải vá bằng class khó hiểu.",
      "Bật flex ở quá nhiều cấp không cần thiết.",
      "Không kiểm tra mobile trước khi xem là hoàn thành."
    ]
  };
}

const modules = [
  {
    slug: "module-01-nen-tang-flexbox",
    className: "m1",
    short: "Module 1",
    title: "Nền tảng Flexbox cần nắm",
    subtitle: "Các khái niệm và thuộc tính cốt lõi, không học lan man.",
    lessons: [
      lessons.flexIntro,
      lessons.displayFlex,
      lessons.axis,
      lessons.justify,
      lessons.align,
      lessons.gapWrap,
      lessons.flexItem,
      lessons.orderAutoNested
    ]
  },
  {
    slug: "module-02-pattern-giao-dien",
    className: "m2",
    short: "Module 2",
    title: "Pattern giao diện dùng Flexbox",
    subtitle: "Những bố cục gặp thường xuyên khi làm web thật.",
    lessons: [
      navbarLesson("Navbar responsive"),
      toolbarLesson(),
      mediaLesson("Media object: avatar, nội dung và thời gian"),
      formLesson(),
      cardListLesson("Card list và pricing cards", "Dùng Flexbox để tạo các card cùng hàng, xuống dòng và có nút nằm cuối."),
      footerLesson(),
      modalActionsLesson(),
      navControlsLesson()
    ]
  },
  {
    slug: "module-03-responsive-thuc-te",
    className: "m3",
    short: "Module 3",
    title: "Responsive và layout thực tế",
    subtitle: "Áp dụng Flexbox vào các layout có ràng buộc thật.",
    lessons: [
      cardListLesson("Fluid cards với flex: 1 1 240px", "Tạo card co giãn và xuống dòng bằng flex shorthand."),
      sidebarLesson("Sidebar và content layout"),
      withTitle(lessons.orderAutoNested, "Card cao bằng nhau, nút nằm cuối", "Dùng flex column và margin-top auto trong card."),
      withTitle(lessons.flexItem, "Search bar co giãn trong header", "Tạo search bar có input chiếm phần còn lại."),
      mediaLesson("Comment row và chat list"),
      mobileLayoutLesson(),
      nestedFlexLesson(),
      projectLesson({
        title: "Khi nào dùng Flexbox, khi nào dùng Grid",
        description: "So sánh nhanh Flexbox và CSS Grid qua cùng một bố cục card.",
        html: `<section class="comparison">
  <article class="panel">
    <h3>Dùng Flexbox</h3>
    <p class="muted">Tốt cho hàng card tự xuống dòng và nội dung một chiều.</p>
  </article>
  <article class="panel">
    <h3>Dùng Grid</h3>
    <p class="muted">Tốt cho bố cục hai chiều cần hàng/cột rõ ràng.</p>
  </article>
</section>`,
        css: `.comparison {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.comparison .panel {
  flex: 1 1 260px;
}`,
        exercise: "Tạo hai phiên bản danh sách card: một bản bằng Flexbox, một bản bằng Grid. Ghi chú trường hợp nào dễ kiểm soát hơn.",
        practice: [
          "Tạo cùng một HTML cho 6 card.",
          "Viết bản Flexbox dùng wrap và flex-basis.",
          "Viết bản Grid dùng repeat(auto-fit, minmax()).",
          "So sánh khi card có nội dung dài ngắn khác nhau."
        ],
        criteria: [
          "Bạn chỉ ra được lý do chọn Flexbox hoặc Grid.",
          "Hai bản đều responsive.",
          "Không gượng ép Flexbox cho bài toán hai chiều phức tạp."
        ]
      })
    ]
  },
  {
    slug: "module-04-bai-thuc-hanh",
    className: "m4",
    short: "Module 4",
    title: "Bài thực hành Flexbox",
    subtitle: "Đề bài thực tế, yêu cầu rõ ràng, lời giải khớp với đề.",
    lessons: [
      projectLesson({
        title: "Dự án 1: Navbar khóa học responsive",
        description: "Thực hành header có logo, menu, nút đăng nhập và trạng thái mobile.",
        html: navbarLesson().html,
        css: navbarLesson().css,
        exercise: "Xây navbar cho trang khóa học. Desktop: logo trái, menu phải, nút đăng nhập cuối hàng. Mobile: menu xuống hàng riêng, không tràn ngang.",
        practice: navbarLesson().practice,
        criteria: navbarLesson().criteria
      }),
      projectLesson({
        title: "Dự án 2: Pricing section 3 gói",
        description: "Thực hành pricing card cao bằng nhau, có gói nổi bật và nút nằm cuối.",
        html: cardListLesson("Pricing").html,
        css: cardListLesson("Pricing").css,
        exercise: "Tạo section giá gồm 3 gói: Cơ bản, Thực hành, Dự án. Gói giữa nổi bật. Nút trong các card phải nằm cuối card.",
        practice: cardListLesson("Pricing").practice,
        criteria: cardListLesson("Pricing").criteria
      }),
      projectLesson({
        title: "Dự án 3: Product catalog có filter bar",
        description: "Thực hành hàng filter và danh sách sản phẩm responsive.",
        html: `<section class="catalog">
  <div class="toolbar">
    <strong>Sản phẩm</strong>
    <button>Danh mục</button>
    <button>Sắp xếp</button>
  </div>
  <div class="product-list">
    <article class="product-card"><h3>Áo thun</h3><p class="muted">199.000đ</p><button>Thêm</button></article>
    <article class="product-card"><h3>Balo</h3><p class="muted">399.000đ</p><button>Thêm</button></article>
    <article class="product-card"><h3>Giày</h3><p class="muted">599.000đ</p><button>Thêm</button></article>
  </div>
</section>`,
        css: `.catalog {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.toolbar {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.toolbar strong {
  margin-right: auto;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.product-card {
  flex: 1 1 220px;
  display: flex;
  flex-direction: column;
  min-height: 180px;
}

.product-card button {
  margin-top: auto;
  align-self: flex-start;
}`,
        exercise: "Tạo catalog có filter bar phía trên và danh sách sản phẩm phía dưới. Filter bar wrap trên mobile, product card tự xuống dòng.",
        practice: [
          "Tạo toolbar có tiêu đề và 2 nút filter.",
          "Tạo ít nhất 6 product card.",
          "Toolbar dùng flex wrap, tiêu đề đẩy các nút sang phải.",
          "Product list dùng flex-wrap và flex-basis.",
          "Nút trong card nằm cuối."
        ],
        criteria: [
          "Toolbar không tràn mobile.",
          "Product card xuống dòng hợp lý.",
          "Card có cấu trúc rõ: title, price, action."
        ]
      }),
      projectLesson({
        title: "Dự án 4: Admin dashboard shell",
        description: "Thực hành sidebar, header nội dung và các ô thống kê.",
        html: `<main class="app-layout">
  <aside class="sidebar">Admin menu</aside>
  <section class="content">
    <header class="content-header">
      <h2>Dashboard</h2>
      <button>Tạo báo cáo</button>
    </header>
    <section class="stats">
      <article class="panel"><strong>128</strong><span class="muted">Đơn hàng</span></article>
      <article class="panel"><strong>64</strong><span class="muted">Học viên</span></article>
      <article class="panel"><strong>12</strong><span class="muted">Bài nộp</span></article>
    </section>
  </section>
</main>`,
        css: `${sidebarLesson().css}

.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 16px;
}

.stats .panel {
  flex: 1 1 160px;
}`,
        exercise: "Xây dashboard shell gồm sidebar, header nội dung và 3 ô thống kê. Mobile sidebar nằm trên content.",
        practice: sidebarLesson().practice,
        criteria: [
          "Sidebar/content đúng tỉ lệ trên desktop.",
          "Stats card tự xuống dòng.",
          "Mobile không tràn ngang."
        ]
      }),
      projectLesson({
        title: "Dự án 5: Profile card và skill chips",
        description: "Thực hành avatar cố định, thông tin co giãn và danh sách skill wrap.",
        html: `<article class="profile-card">
  <div class="profile-head">
    <div class="avatar">P</div>
    <div>
      <h3>Phạm Minh</h3>
      <p class="muted">Frontend learner</p>
    </div>
    <button>Liên hệ</button>
  </div>
  <div class="skills">
    <span>HTML</span><span>CSS</span><span>Flexbox</span><span>Responsive</span>
  </div>
</article>`,
        css: `.profile-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.profile-head {
  display: flex;
  align-items: center;
  gap: 12px;
}

.profile-head button {
  margin-left: auto;
}

.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.skills span {
  border-radius: 999px;
  padding: 6px 10px;
  background: #ccfbf1;
}`,
        exercise: "Tạo profile card có avatar, tên, mô tả, nút liên hệ và danh sách kỹ năng tự xuống dòng.",
        practice: [
          "Header profile dùng flex row.",
          "Avatar cố định, thông tin co giãn.",
          "Nút liên hệ đẩy sang phải bằng auto margin.",
          "Skill list dùng flex-wrap và gap.",
          "Mobile vẫn đọc tốt khi tên dài."
        ],
        criteria: [
          "Profile head căn giữa đẹp.",
          "Skill chips xuống dòng đều.",
          "Không dùng absolute positioning."
        ]
      }),
      projectLesson({
        title: "Dự án 6: Chat list",
        description: "Thực hành danh sách chat có avatar, nội dung co giãn và thời gian bên phải.",
        html: `<section class="chat-list">
  <article class="chat-row">
    <div class="avatar">A</div>
    <div class="chat-body"><strong>An</strong><p class="muted">Bài Flexbox đã xong chưa?</p></div>
    <time>09:30</time>
  </article>
  <article class="chat-row">
    <div class="avatar">B</div>
    <div class="chat-body"><strong>Bình</strong><p class="muted">Mình đang kiểm tra responsive.</p></div>
    <time>10:15</time>
  </article>
</section>`,
        css: `.chat-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.chat-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.chat-body {
  flex: 1;
  min-width: 0;
}

.chat-row time {
  margin-left: auto;
  color: #64748b;
}`,
        exercise: "Tạo danh sách chat ít nhất 5 dòng. Mỗi dòng có avatar, tên, tin nhắn cuối và thời gian.",
        practice: mediaLesson().practice,
        criteria: mediaLesson().criteria
      }),
      projectLesson({
        title: "Dự án 7: Checkout summary",
        description: "Thực hành layout checkout có danh sách sản phẩm và box tổng tiền.",
        html: `<main class="checkout">
  <section class="cart-list">
    <article class="cart-row"><span>Khóa Flexbox</span><strong>299.000đ</strong></article>
    <article class="cart-row"><span>Khóa CSS Grid</span><strong>399.000đ</strong></article>
  </section>
  <aside class="summary-box">
    <h3>Tổng cộng</h3>
    <strong>698.000đ</strong>
    <button>Thanh toán</button>
  </aside>
</main>`,
        css: `.checkout {
  display: flex;
  align-items: flex-start;
  gap: 18px;
}

.cart-list {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cart-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  border: 1px solid #d9e2ec;
  border-radius: 10px;
  padding: 14px;
  background: white;
}

.summary-box {
  flex: 0 0 260px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

@media (max-width: 720px) {
  .checkout {
    flex-direction: column;
  }

  .summary-box {
    width: 100%;
    flex-basis: auto;
  }
}`,
        exercise: "Tạo checkout gồm danh sách sản phẩm bên trái và box tổng tiền bên phải. Mobile chuyển thành một cột.",
        practice: [
          "Tạo container checkout gồm cart-list và summary.",
          "Cart-list dùng <code>flex: 1</code>.",
          "Summary dùng <code>flex: 0 0 260px</code>.",
          "Mỗi cart row dùng flex để tên và giá tách hai bên.",
          "Media query chuyển checkout sang column."
        ],
        criteria: [
          "Desktop có hai cột rõ.",
          "Mobile summary không bị bó hẹp.",
          "Tên và giá trong từng dòng căn hợp lý."
        ]
      }),
      projectLesson({
        title: "Dự án 8: Landing page mini",
        description: "Tổng hợp navbar, hero, card list và footer bằng Flexbox.",
        html: `<main class="landing">
  <header class="site-header">
    <a class="logo" href="#">FlexCourse</a>
    <nav class="site-nav"><a href="#">Bài học</a><a href="#">Bài tập</a><a href="#">Liên hệ</a></nav>
    <button>Học ngay</button>
  </header>
  <section class="hero-row">
    <div><h1>Học Flexbox thực tế</h1><p class="muted">Code, xem preview và tự luyện qua dự án.</p></div>
    <div class="panel">Preview layout</div>
  </section>
  <section class="card-list">
    <article class="card"><h3>Nền tảng</h3><p class="muted">Trục, căn chỉnh, wrap.</p><button>Xem</button></article>
    <article class="card"><h3>Pattern</h3><p class="muted">Navbar, form, card.</p><button>Xem</button></article>
    <article class="card"><h3>Dự án</h3><p class="muted">Dashboard, checkout.</p><button>Xem</button></article>
  </section>
</main>`,
        css: `${navbarLesson().css}

.landing {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.hero-row {
  display: flex;
  align-items: center;
  gap: 24px;
}

.hero-row > * {
  flex: 1;
}

${cardListLesson("Cards").css}

@media (max-width: 720px) {
  .hero-row {
    flex-direction: column;
  }
}`,
        exercise: "Tạo landing page mini gồm navbar, hero hai cột, 3 card nội dung. Mobile hero chuyển thành cột, card tự xuống dòng.",
        practice: [
          "Dựng HTML theo 3 vùng: header, hero, card list.",
          "Header dùng pattern navbar đã học.",
          "Hero dùng flex row và chuyển column trên mobile.",
          "Card list dùng wrap và flex-basis.",
          "Kiểm tra toàn trang không tràn ngang."
        ],
        criteria: [
          "Kết hợp được ít nhất 3 pattern Flexbox.",
          "Responsive hoạt động ở mobile.",
          "Code chia vùng rõ ràng, không gom mọi thứ vào một flex container."
        ]
      })
    ]
  }
];

function appJs() {
  return `const playground = document.querySelector("[data-playground]");

async function highlightCode() {
  const blocks = Array.from(document.querySelectorAll("pre code[data-lang]"));
  if (!blocks.length) return;

  try {
    const { codeToHtml } = await import("https://esm.sh/shiki@1");
    await Promise.all(blocks.map(async (block) => {
      const raw = block.dataset.raw || block.textContent;
      if (block.dataset.highlighted === raw) return;
      const html = await codeToHtml(raw, { lang: block.dataset.lang || "text", theme: "github-dark" });
      const wrapper = document.createElement("div");
      wrapper.innerHTML = html;
      const highlightedPre = wrapper.querySelector("pre");
      const highlightedCode = wrapper.querySelector("code");
      const pre = block.closest("pre");

      block.dataset.raw = raw;
      block.dataset.highlighted = raw;
      block.innerHTML = highlightedCode ? highlightedCode.innerHTML : block.innerHTML;

      if (highlightedPre) {
        pre.className = highlightedPre.className;
        pre.style.cssText = highlightedPre.getAttribute("style") || "";
      }

      pre.style.borderRadius = "8px";
      pre.style.padding = "18px";
      pre.style.overflowX = "auto";
      pre.style.margin = "0";
      pre.style.lineHeight = "1.65";
    }));
  } catch (error) {
    console.warn("Không tải được Shiki, giữ nguyên code block mặc định.", error);
  }
}

if (playground) {
  const demo = playground.querySelector("[data-demo]");
  const code = playground.querySelector("[data-code]");
  const controls = Array.from(playground.querySelectorAll("[data-css-prop]"));

  const render = () => {
    const css = {};
    controls.forEach((control) => {
      css[control.dataset.cssProp] = control.value;
    });

    demo.style.flexDirection = css["flex-direction"];
    demo.style.justifyContent = css["justify-content"];
    demo.style.alignItems = css["align-items"];
    demo.style.flexWrap = css["flex-wrap"];
    demo.style.gap = css.gap + "px";

    code.textContent = \`.container {
  display: flex;
  flex-direction: \${css["flex-direction"]};
  justify-content: \${css["justify-content"]};
  align-items: \${css["align-items"]};
  flex-wrap: \${css["flex-wrap"]};
  gap: \${css.gap}px;
}\`;
    delete code.dataset.raw;
    delete code.dataset.highlighted;
  };

  controls.forEach((control) => {
    control.addEventListener("input", () => {
      render();
      highlightCode();
    });
  });

  render();
}

highlightCode();
`;
}

function sharedCss() {
  return `*,
*::before,
*::after {
  box-sizing: border-box;
}

:root {
  --ink: #172033;
  --muted: #5e6b7a;
  --line: #d9e2ec;
  --paper: #ffffff;
  --soft: #f4f7fb;
  --teal: #0f766e;
  --coral: #e85d4f;
  --blue: #2563eb;
  --amber: #d97706;
  --shadow: 0 14px 34px rgba(23, 32, 51, 0.1);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  color: var(--ink);
  background: var(--soft);
  line-height: 1.6;
}

a {
  color: inherit;
}

code,
pre {
  font-family: Consolas, "Courier New", monospace;
}

code {
  padding: 2px 6px;
  border-radius: 5px;
  background: #e9eef5;
  color: #b42318;
  font-size: 0.92em;
}

pre {
  margin: 0;
  padding: 18px;
  overflow-x: auto;
  border-radius: 8px;
  background: #111827;
  color: #e5e7eb;
  font-size: 0.9rem;
  line-height: 1.65;
}

pre code {
  padding: 0;
  background: transparent;
  color: inherit;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(255, 255, 255, 0.94);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(12px);
}

.topbar-inner,
.container {
  max-width: 1160px;
  margin: 0 auto;
}

.topbar-inner {
  padding: 12px 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  text-decoration: none;
  white-space: nowrap;
}

.brand-mark {
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  color: white;
  background: var(--teal);
  font-weight: 900;
}

.nav-links,
.hero-actions,
.tag-row,
.pager {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.nav-links {
  justify-content: flex-end;
}

.nav-links a,
.btn {
  min-height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 12px;
  background: white;
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  font-size: 0.92rem;
}

.btn.primary {
  border-color: var(--teal);
  background: var(--teal);
  color: white;
}

.hero {
  color: white;
  background: linear-gradient(135deg, #0f766e, #172033);
}

.hero-inner {
  max-width: 1160px;
  margin: 0 auto;
  padding: 58px 22px 44px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(330px, 0.9fr);
  gap: 34px;
  align-items: center;
}

.eyebrow {
  margin: 0 0 10px;
  color: #fde68a;
  font-size: 0.86rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero h1,
.module-hero h1 {
  margin: 0;
  line-height: 1.08;
  letter-spacing: 0;
}

.hero h1 {
  max-width: 760px;
  font-size: clamp(2.15rem, 4.6vw, 4.2rem);
}

.hero p,
.module-hero p {
  max-width: 760px;
  color: rgba(255, 255, 255, 0.88);
}

.hero .btn {
  border-color: rgba(255, 255, 255, 0.34);
  background: rgba(255, 255, 255, 0.12);
  color: white;
}

.hero .btn.primary {
  border-color: white;
  background: white;
  color: #115e59;
}

.hero-visual {
  min-height: 310px;
  padding: 18px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
}

.visual-stage,
.demo-box {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  gap: 12px;
  min-height: 274px;
  padding: 16px;
  border: 2px dashed rgba(255, 255, 255, 0.42);
  border-radius: 8px;
}

.visual-item,
.demo-item {
  min-width: 86px;
  min-height: 58px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: #fef3c7;
  color: #78350f;
  font-weight: 900;
}

.section {
  padding: 44px 22px;
}

.section.alt {
  background: white;
}

.section-head {
  max-width: 780px;
  margin-bottom: 24px;
}

.section-head h2,
.module-article h2 {
  margin: 0 0 8px;
  font-size: clamp(1.5rem, 2.8vw, 2.2rem);
  line-height: 1.16;
}

.section-head p,
.module-article p,
.lesson p,
.exercise p {
  margin: 0;
  color: var(--muted);
}

.stats-grid,
.module-grid,
.exercise-grid,
.code-grid,
.playground-layout,
.lesson-layout {
  display: grid;
  gap: 18px;
}

.stats-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.module-grid,
.code-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.module-list {
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
}

.playground-layout,
.lesson-layout {
  grid-template-columns: minmax(230px, 0.34fr) minmax(0, 1fr);
  align-items: start;
}

.stat,
.module-link,
.lesson,
.exercise,
.callout,
.playground,
.exercise-card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: var(--shadow);
}

.stat {
  padding: 18px;
}

.stat strong {
  display: block;
  color: var(--teal);
  font-size: 1.7rem;
}

.stat span {
  color: var(--muted);
}

.module-link {
  overflow: hidden;
  color: inherit;
  text-decoration: none;
}

.module-link header {
  padding: 22px;
  color: white;
}

.module-link.m1 header,
.module-hero.m1 {
  background: var(--teal);
}

.module-link.m2 header,
.module-hero.m2 {
  background: var(--coral);
}

.module-link.m3 header,
.module-hero.m3 {
  background: var(--blue);
}

.module-link.m4 header,
.module-hero.m4 {
  background: var(--amber);
}

.module-link h3 {
  margin: 0;
  font-size: 1.24rem;
}

.module-link header p {
  margin: 6px 0 0;
  color: rgba(255, 255, 255, 0.88);
}

.module-body,
.lesson,
.exercise,
.callout,
.playground {
  padding: 22px;
}

.module-body ul,
.lesson ul,
.exercise ul,
.steps {
  margin: 12px 0 0;
  padding-left: 20px;
}

.module-body li,
.lesson li,
.exercise li,
.steps li {
  margin: 6px 0;
  color: var(--muted);
}

.tag {
  display: inline-flex;
  align-items: center;
  min-height: 28px;
  padding: 4px 10px;
  border-radius: 999px;
  background: #edf7f6;
  color: #115e59;
  font-size: 0.82rem;
  font-weight: 800;
}

.module-hero .container {
  padding: 42px 22px;
}

.module-hero h1 {
  max-width: 900px;
  font-size: clamp(2rem, 4vw, 3.25rem);
}

.breadcrumb {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 12px;
  color: rgba(255, 255, 255, 0.82);
}

.breadcrumb a {
  color: white;
  font-weight: 800;
  text-decoration: none;
}

.side-nav {
  position: sticky;
  top: 74px;
  display: grid;
  gap: 8px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: white;
}

.side-nav a {
  padding: 8px 10px;
  border-radius: 8px;
  color: var(--muted);
  text-decoration: none;
  font-weight: 700;
}

.side-nav a:hover {
  background: #edf7f6;
  color: #115e59;
}

.module-article {
  display: grid;
  gap: 20px;
}

.lesson h3,
.exercise h3,
.callout h3 {
  margin: 18px 0 8px;
}

.demo-surface {
  margin-top: 16px;
}

.demo-code,
.result-panel {
  margin-top: 18px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #f8fafc;
  padding: 16px;
}

.result-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

.result-head h3,
.demo-code h3 {
  margin: 0 0 6px;
}

.result-head span,
.demo-code p {
  color: var(--muted);
  font-size: 0.9rem;
}

.result-frame {
  width: 100%;
  min-height: 340px;
  display: block;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  background: white;
}

.exercise-card {
  display: flex;
  gap: 14px;
  padding: 18px;
  color: inherit;
  text-decoration: none;
  border-left: 5px solid var(--teal);
}

.exercise-card.m2 {
  border-left-color: var(--coral);
}

.exercise-card.m3 {
  border-left-color: var(--blue);
}

.exercise-card.m4 {
  border-left-color: var(--amber);
}

.card-num {
  flex: 0 0 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: #edf7f6;
  color: #115e59;
  font-weight: 900;
}

.card-info h3 {
  margin: 0 0 4px;
  font-size: 1rem;
}

.card-info p {
  margin: 0;
  color: var(--muted);
  font-size: 0.88rem;
}

.level {
  display: inline-flex;
  margin-bottom: 10px;
  padding: 3px 10px;
  border-radius: 999px;
  background: #fff7ed;
  color: #9a3412;
  font-size: 0.82rem;
  font-weight: 900;
}

.steps {
  counter-reset: step;
  list-style: none;
  padding-left: 0;
}

.steps li {
  position: relative;
  padding-left: 42px;
}

.steps li::before {
  counter-increment: step;
  content: counter(step);
  position: absolute;
  left: 0;
  top: 1px;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--teal);
  color: white;
  font-weight: 900;
}

.solution {
  border-color: #bbf7d0;
  background: #f0fdf4;
}

.pager {
  justify-content: space-between;
}

.controls {
  display: grid;
  gap: 14px;
}

.control label {
  display: block;
  margin-bottom: 6px;
  font-weight: 800;
}

.control select,
.control input {
  width: 100%;
  min-height: 40px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 10px;
  font: inherit;
}

.demo-box {
  border-color: #94a3b8;
  background: white;
}

.footer {
  padding: 28px 22px;
  background: #172033;
  color: rgba(255, 255, 255, 0.78);
  text-align: center;
}

@media (max-width: 900px) {
  .hero-inner,
  .playground-layout,
  .lesson-layout,
  .stats-grid,
  .module-grid,
  .code-grid {
    grid-template-columns: 1fr;
  }

  .side-nav {
    position: static;
  }
}

@media (max-width: 640px) {
  .topbar-inner {
    align-items: flex-start;
    flex-direction: column;
  }

  .nav-links {
    justify-content: flex-start;
  }
}
`;
}

function lessonDescription(lesson) {
  return lesson.description || `Bài học CSS Flexbox: ${lesson.title}.`;
}

function indexPage() {
  const totalLessons = modules.reduce((sum, module) => sum + module.lessons.length, 0);
  const moduleCards = modules.map((module) => `<a class="module-link ${module.className}" href="${module.slug}/index.html">
            <header>
              <h3>${module.short}: ${module.title}</h3>
              <p>${module.subtitle}</p>
            </header>
            <div class="module-body">
              <ul>
                ${module.lessons.slice(0, 4).map((lesson) => `<li>${lesson.title}</li>`).join("\n                ")}
              </ul>
              <div class="tag-row">
                <span class="tag">${module.lessons.length} bài</span>
                <span class="tag">Có preview</span>
                <span class="tag">Có bài giải</span>
              </div>
            </div>
          </a>`).join("\n");

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo("Học CSS Flexbox Thực Tế | NenTang.vn", `Khóa học CSS Flexbox tinh gọn gồm ${totalLessons} bài cần thiết, ví dụ thực tế, bài tập và bài giải đúng đề.`, "shared.css")}
</head>
<body>
  ${topbar("")}
  <main>
    <section class="hero">
      <div class="hero-inner">
        <div>
          <p class="eyebrow">Khóa học thực hành, không học lan man</p>
          <h1>Học CSS Flexbox qua layout thật</h1>
          <p>Lộ trình được cắt lại chỉ giữ các bài cần thiết: nền tảng, pattern giao diện, responsive thực tế và bài thực hành có đề/lời giải khớp nhau.</p>
          <div class="hero-actions">
            <a class="btn primary" href="#modules">Xem module</a>
            <a class="btn" href="#playground">Thử Playground</a>
          </div>
        </div>
        <div class="hero-visual" aria-label="Minh họa Flexbox">
          <div class="visual-stage">
            <div class="visual-item">logo</div>
            <div class="visual-item">nav</div>
            <div class="visual-item">search</div>
            <div class="visual-item">action</div>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="stats-grid">
          <div class="stat"><strong>${modules.length}</strong><span>Module</span></div>
          <div class="stat"><strong>${totalLessons}</strong><span>Bài học cần thiết</span></div>
          <div class="stat"><strong>8</strong><span>Bài thực hành dự án</span></div>
          <div class="stat"><strong>Shiki</strong><span>Code highlight</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="modules">
      <div class="container">
        <div class="section-head">
          <h2>Lộ trình mới</h2>
          <p>Mỗi module chỉ giữ những bài thực sự phục vụ việc học và dùng Flexbox trong giao diện thực tế.</p>
        </div>
        <div class="module-grid">
          ${moduleCards}
        </div>
      </div>
    </section>

    <section class="section alt" id="playground">
      <div class="container">
        <div class="section-head">
          <h2>Flexbox Playground</h2>
          <p>Thử thay đổi thuộc tính và quan sát item di chuyển trước khi đọc code chi tiết trong bài.</p>
        </div>
        <div class="playground" data-playground>
          <div class="playground-layout">
            <div class="controls">
              <div class="control"><label for="direction">flex-direction</label><select id="direction" data-css-prop="flex-direction"><option value="row">row</option><option value="column">column</option><option value="row-reverse">row-reverse</option><option value="column-reverse">column-reverse</option></select></div>
              <div class="control"><label for="justify">justify-content</label><select id="justify" data-css-prop="justify-content"><option value="flex-start">flex-start</option><option value="center">center</option><option value="space-between">space-between</option><option value="space-evenly">space-evenly</option><option value="flex-end">flex-end</option></select></div>
              <div class="control"><label for="align">align-items</label><select id="align" data-css-prop="align-items"><option value="stretch">stretch</option><option value="center">center</option><option value="flex-start">flex-start</option><option value="flex-end">flex-end</option></select></div>
              <div class="control"><label for="wrap">flex-wrap</label><select id="wrap" data-css-prop="flex-wrap"><option value="nowrap">nowrap</option><option value="wrap">wrap</option></select></div>
              <div class="control"><label for="gap">gap</label><input id="gap" data-css-prop="gap" type="range" min="0" max="42" value="12" /></div>
            </div>
            <div>
              <div class="demo-box" data-demo>
                <div class="demo-item">1</div>
                <div class="demo-item">2</div>
                <div class="demo-item">3</div>
                <div class="demo-item">4</div>
              </div>
              <pre style="margin-top:14px"><code data-code data-lang="css"></code></pre>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <footer class="footer"><p>CSS Flexbox Course - NenTang.vn</p></footer>
  <script type="module" src="app.js"></script>
</body>
</html>`;
}

function modulePage(module) {
  const cards = module.lessons.map((lesson, index) => `<a href="bai-${pad(index + 1)}/index.html" class="exercise-card ${module.className}">
        <div class="card-num">${pad(index + 1)}</div>
        <div class="card-info">
          <h3>${lesson.title}</h3>
          <p>${lessonDescription(lesson)}</p>
        </div>
      </a>`).join("\n");

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo(`${module.short}: ${module.title} | CSS Flexbox | NenTang.vn`, module.subtitle, "../shared.css")}
</head>
<body>
  ${topbar("../")}
  <section class="module-hero ${module.className}">
    <div class="container">
      <div class="breadcrumb"><a href="../index.html">CSS Flexbox</a><span>/</span><span>${module.short}</span></div>
      <h1>${module.short}: ${module.title}</h1>
      <p>${module.subtitle}</p>
    </div>
  </section>
  <main class="section">
    <div class="container">
      <div class="section-head">
        <h2>Danh sách bài học</h2>
        <p>Các bài trong module này được giữ lại vì có giá trị trực tiếp khi xây giao diện thực tế.</p>
      </div>
      <div class="exercise-grid module-list">${cards}</div>
    </div>
  </main>
  <footer class="footer"><p><a href="../index.html">Quay lại khóa CSS Flexbox</a></p></footer>
  <script type="module" src="../app.js"></script>
</body>
</html>`;
}

function lessonPage(module, lesson, index) {
  const number = index + 1;
  const prev = number > 1 ? `../bai-${pad(number - 1)}/index.html` : "../index.html";
  const next = number < module.lessons.length ? `../bai-${pad(number + 1)}/index.html` : "../../index.html";

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo(`Bài ${pad(number)} - ${lesson.title} | ${module.short} CSS Flexbox | NenTang.vn`, lessonDescription(lesson), "../../shared.css")}
</head>
<body>
  ${topbar("../../")}
  <section class="module-hero ${module.className}">
    <div class="container">
      <div class="breadcrumb"><a href="../../index.html">CSS Flexbox</a><span>/</span><a href="../index.html">${module.short}</a><span>/</span><span>Bài ${pad(number)}</span></div>
      <h1>Bài ${pad(number)}: ${lesson.title}</h1>
      <p>${lessonDescription(lesson)}</p>
    </div>
  </section>
  <main class="section">
    <div class="container lesson-layout">
      <aside class="side-nav" aria-label="Mục lục bài học">
        <a href="#goal">Mục tiêu</a>
        <a href="#theory">Lý thuyết</a>
        <a href="#demo">Minh họa</a>
        <a href="#code">Code ví dụ</a>
        <a href="#exercise">Thực hành</a>
        <a href="#solution">Bài giải</a>
      </aside>
      <article class="module-article">
        <section class="lesson" id="goal">
          <h2>Mục tiêu bài học</h2>
          <ul>
${list(lesson.objectives)}
          </ul>
        </section>

        <section class="lesson" id="theory">
          <h2>Lý thuyết thực tế</h2>
          ${lesson.theory.map((paragraph) => `<p>${paragraph}</p>`).join("\n          ")}
          <ol class="steps">
${steps(lesson.workflow)}
          </ol>
        </section>

        <section class="lesson" id="demo">
          <h2>Minh họa trực quan</h2>
          <p>Minh họa này tập trung vào cơ chế chính của bài. Code bên dưới chính là phần điều khiển layout.</p>
          <style>${lesson.baseCss || baseBoxCss}${lesson.demoCss}</style>
          ${lesson.html}
          <div class="demo-code">
            <h3>Code tạo minh họa</h3>
            <pre><code data-lang="css">${esc(lesson.demoCss)}</code></pre>
          </div>
        </section>

        <section class="lesson" id="code">
          <h2>Code ví dụ</h2>
          <p>Ví dụ này là một tình huống giao diện thật, không phải đoạn CSS rời rạc.</p>
          <div class="code-grid">
            <div><h3>HTML</h3><pre><code data-lang="html">${esc(lesson.html)}</code></pre></div>
            <div><h3>CSS</h3><pre><code data-lang="css">${esc(lesson.css)}</code></pre></div>
          </div>
          ${previewFrame(lesson, "Kết quả khi chạy code ví dụ")}
        </section>

        <section class="exercise" id="exercise">
          <span class="level">Bài tập thực hành</span>
          <h2>Yêu cầu đề bài</h2>
          <p>${lesson.exercise}</p>
          <ol class="steps">
${steps(lesson.practice)}
          </ol>
          <h3>Tiêu chí chấm</h3>
          <ul>
${list(lesson.criteria)}
          </ul>
        </section>

        <section class="lesson solution" id="solution">
          <h2>Bài giải tham khảo</h2>
          <p>Lời giải dưới đây bám đúng yêu cầu đề. Hãy tự làm trước, sau đó mới đối chiếu.</p>
          <pre><code data-lang="html">${esc(fullSolution(lesson))}</code></pre>
          ${previewFrame(lesson, "Kết quả bài giải")}
        </section>

        <section class="callout">
          <h2>Lỗi thường gặp</h2>
          <ul>
${list(lesson.mistakes)}
          </ul>
        </section>

        <div class="pager">
          <a class="btn" href="${prev}">Bài trước</a>
          <a class="btn primary" href="${next}">Bài tiếp theo</a>
        </div>
      </article>
    </div>
  </main>
  <footer class="footer"><p><a href="../index.html">Quay lại ${module.short}</a></p></footer>
  <script type="module" src="../../app.js"></script>
</body>
</html>`;
}

function cleanOldModules() {
  fs.readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name.startsWith("module-"))
    .forEach((entry) => fs.rmSync(path.join(root, entry.name), { recursive: true, force: true }));
}

cleanOldModules();
write(path.join(root, "shared.css"), sharedCss());
write(path.join(root, "app.js"), appJs());
write(path.join(root, "index.html"), indexPage());

modules.forEach((module) => {
  write(path.join(root, module.slug, "index.html"), modulePage(module));
  module.lessons.forEach((lesson, index) => {
    write(path.join(root, module.slug, `bai-${pad(index + 1)}`, "index.html"), lessonPage(module, lesson, index));
  });
});

console.log(`Generated ${modules.length} modules and ${modules.reduce((sum, module) => sum + module.lessons.length, 0)} lessons.`);
