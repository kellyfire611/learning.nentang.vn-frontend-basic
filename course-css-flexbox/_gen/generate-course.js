const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const author = "Dương Nguyễn Phú Cường";
const siteName = "Nền tảng Kiến thức";
const baseUrl = "https://nentang.vn/";

const modules = [
  {
    slug: "module-01-nhap-mon-flexbox",
    short: "Module 1",
    className: "m1",
    title: "Nhập môn CSS Flexbox",
    subtitle: "Nền tảng container, item, trục chính, trục phụ và các thuộc tính căn bản.",
    lessons: [
      "Flexbox là gì và khi nào nên dùng",
      "display: flex và inline-flex",
      "Flex container và flex item",
      "Main axis và cross axis",
      "flex-direction: row, column, reverse",
      "gap và cách tạo khoảng cách sạch",
      "justify-content: căn theo trục chính",
      "align-items: căn theo trục phụ",
      "align-self: căn riêng từng item",
      "flex-wrap: cho item xuống dòng",
      "align-content: căn nhiều dòng",
      "order: đổi thứ tự hiển thị",
      "flex-grow: chia phần trống",
      "flex-shrink: kiểm soát co lại",
      "flex-basis: kích thước khởi đầu",
      "flex shorthand: grow shrink basis",
      "margin auto trong Flexbox",
      "Nested flex: lồng nhiều container",
      "Debug Flexbox bằng DevTools",
      "Mini project: menu và toolbar"
    ]
  },
  {
    slug: "module-02-truc-can-chinh",
    short: "Module 2",
    className: "m2",
    title: "Căn chỉnh và pattern thường gặp",
    subtitle: "Ứng dụng Flexbox vào menu, card, form, tab, footer và các hàng dữ liệu.",
    lessons: [
      "Căn giữa một khối trong màn hình",
      "Navbar logo trái, menu phải",
      "Toolbar có nhóm nút hành động",
      "Card row cao bằng nhau",
      "Media object: avatar và nội dung",
      "Form row: label, input, button",
      "Button group và segmented control",
      "Breadcrumb và pagination",
      "Tabs điều hướng bằng Flexbox",
      "Gallery dùng flex-wrap",
      "Pricing cards 3 cột",
      "Stepper quy trình từng bước",
      "Sticky footer bằng Flexbox",
      "Split hero text và media",
      "List item có icon, text, action",
      "Modal footer căn nút",
      "Hàng dữ liệu kiểu table nhẹ",
      "Header responsive tự xuống dòng",
      "Spacing scale với gap",
      "Mini project: landing header"
    ]
  },
  {
    slug: "module-03-flex-item-responsive",
    short: "Module 3",
    className: "m3",
    title: "Flex item và responsive layout",
    subtitle: "Làm chủ co giãn item, layout nhiều cột, sidebar, dashboard và mobile-first.",
    lessons: [
      "Fluid cards với flex: 1 1 240px",
      "Product grid không dùng CSS Grid",
      "Sidebar và content layout",
      "Dashboard shell",
      "Card cao bằng nhau, nút nằm cuối",
      "Holy grail layout đơn giản",
      "Đổi thứ tự trên mobile bằng order",
      "Chip list tự xuống dòng",
      "Search bar co giãn",
      "Comment row với avatar cố định",
      "Chat list căn thời gian bên phải",
      "Profile header responsive",
      "Stats cards co giãn",
      "Feed item nhiều vùng nội dung",
      "Layout cột giả masonry bằng flex",
      "Article layout có aside",
      "Newsletter form responsive",
      "Footer nhiều cột",
      "Responsive utilities nhỏ",
      "Mini project: dashboard quản trị"
    ]
  },
  {
    slug: "module-04-thuc-hanh-du-an",
    short: "Module 4",
    className: "m4",
    title: "Thực hành dự án và bài giải",
    subtitle: "20 bài thực hành có yêu cầu, hướng dẫn từng bước, code lời giải và tiêu chí tự kiểm tra.",
    lessons: [
      "Dự án menu responsive",
      "Dự án pricing section",
      "Dự án product card list",
      "Dự án admin dashboard",
      "Dự án trang cá nhân",
      "Dự án trang liên hệ",
      "Dự án trang khóa học",
      "Dự án checkout summary",
      "Dự án kanban board",
      "Dự án chat sidebar",
      "Dự án notification list",
      "Dự án timeline sự kiện",
      "Dự án portfolio gallery",
      "Dự án blog layout",
      "Dự án account settings",
      "Dự án table action bar",
      "Dự án file manager",
      "Dự án mobile bottom nav",
      "Dự án FAQ accordion layout",
      "Đồ án cuối khóa: landing page hoàn chỉnh"
    ]
  }
];

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function write(file, content) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, content, "utf8");
}

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function pad(num) {
  return String(num).padStart(2, "0");
}

function lessonDescription(module, lesson, number) {
  return `Bài ${pad(number)} CSS Flexbox: ${lesson.toLowerCase()}. Có lý thuyết, ví dụ minh họa, bài tập thực hành và bài giải chi tiết.`;
}

function seo(title, description, cssHref, extra = "") {
  return `  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="${esc(description)}" />
  <meta name="keywords" content="CSS Flexbox, học CSS, layout web, frontend, NenTang.vn, bài tập CSS, responsive" />
  <meta name="author" content="${author}" />
  <meta property="og:locale" content="vi_VN" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="${esc(title)}" />
  <meta property="og:description" content="${esc(description)}" />
  <meta property="og:url" content="${baseUrl}" />
  <meta property="og:site_name" content="${siteName}" />
  <title>${esc(title)}</title>
  <link rel="stylesheet" href="${cssHref}" />${extra}`;
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

function miniDemo(seed) {
  const modes = ["center", "space", "wrap", "column", "grow", "order", "basis", "shrink", "auto", "nested"];
  const mode = typeof seed === "string" ? seed : modes[seed % modes.length];
  return `<div class="mini-demo ${mode}">
    <div class="mini-item">1</div>
    <div class="mini-item">2</div>
    <div class="mini-item">3</div>
    <div class="mini-item">4</div>
    <div class="axis-label main-axis">main axis</div>
    <div class="axis-label cross-axis">cross axis</div>
  </div>`;
}

function visualCss(seed) {
  const modes = ["center", "space", "wrap", "column", "grow", "order", "basis", "shrink", "auto", "nested"];
  const mode = typeof seed === "string" ? seed : modes[seed % modes.length];
  const rules = {
    center: `.mini-demo {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}`,
    space: `.mini-demo {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}`,
    wrap: `.mini-demo {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  gap: 10px;
}`,
    column: `.mini-demo {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
}`,
    grow: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item:nth-child(2) {
  flex: 1;
}`,
    order: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item:nth-child(1) {
  order: 3;
}

.mini-item:nth-child(3) {
  order: 1;
}`,
    basis: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item {
  flex: 1 1 120px;
}`,
    shrink: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item {
  flex: 0 1 160px;
  min-width: 0;
}`,
    auto: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item:nth-child(4) {
  margin-left: auto;
}`,
    nested: `.mini-demo {
  display: flex;
  gap: 10px;
}

.mini-item:nth-child(2) {
  display: flex;
  align-items: center;
  justify-content: center;
}`
  };

  return rules[mode];
}

function normalizeTitle(title) {
  return title.toLowerCase();
}

function hasAny(text, keywords) {
  return keywords.some((keyword) => text.includes(keyword));
}

function lessonKind(title, moduleIndex) {
  const focus = normalizeTitle(title);

  if (hasAny(focus, ["inline-flex"])) return "inline-flex";
  if (hasAny(focus, ["container", "item"])) return "container-item";
  if (hasAny(focus, ["main axis", "cross axis"])) return "axis";
  if (hasAny(focus, ["flex-direction", "row", "column", "reverse"])) return "direction";
  if (hasAny(focus, ["gap", "spacing"])) return "gap";
  if (hasAny(focus, ["justify-content"])) return "justify";
  if (hasAny(focus, ["align-items"])) return "align-items";
  if (hasAny(focus, ["align-self"])) return "align-self";
  if (hasAny(focus, ["flex-wrap", "wrap", "xuống dòng"])) return "wrap";
  if (hasAny(focus, ["align-content"])) return "align-content";
  if (hasAny(focus, ["order", "thứ tự"])) return "order";
  if (hasAny(focus, ["flex-grow", "grow", "co giãn", "fluid", "stats"])) return "grow";
  if (hasAny(focus, ["flex-shrink", "shrink", "co lại"])) return "shrink";
  if (hasAny(focus, ["flex-basis", "basis"])) return "basis";
  if (hasAny(focus, ["shorthand", "1 1 240"])) return "flex-shorthand";
  if (hasAny(focus, ["margin auto"])) return "margin-auto";
  if (hasAny(focus, ["nested", "lồng"])) return "nested";
  if (hasAny(focus, ["debug", "devtools"])) return "debug";
  if (hasAny(focus, ["navbar", "menu responsive", "landing header", "header responsive", "menu và toolbar"])) return "navbar";
  if (hasAny(focus, ["toolbar", "action bar"])) return "toolbar";
  if (hasAny(focus, ["media object", "avatar", "comment", "chat", "profile"])) return "media";
  if (hasAny(focus, ["form", "newsletter", "checkout", "liên hệ"])) return "form";
  if (hasAny(focus, ["button group", "segmented"])) return "button-group";
  if (hasAny(focus, ["breadcrumb", "pagination"])) return "breadcrumb";
  if (hasAny(focus, ["tabs"])) return "tabs";
  if (hasAny(focus, ["gallery", "portfolio"])) return "gallery";
  if (hasAny(focus, ["pricing"])) return "pricing";
  if (hasAny(focus, ["stepper", "timeline"])) return "stepper";
  if (hasAny(focus, ["sticky footer", "footer"])) return "footer";
  if (hasAny(focus, ["split hero", "hero"])) return "hero";
  if (hasAny(focus, ["list item", "notification", "file manager"])) return "list-item";
  if (hasAny(focus, ["modal footer"])) return "modal-footer";
  if (hasAny(focus, ["table", "hàng dữ liệu"])) return "table-row";
  if (hasAny(focus, ["product", "card", "cards", "khóa học", "account settings"])) return "cards";
  if (hasAny(focus, ["sidebar", "dashboard", "admin", "holy grail", "aside", "blog layout"])) return "sidebar";
  if (hasAny(focus, ["chip"])) return "chips";
  if (hasAny(focus, ["search"])) return "search";
  if (hasAny(focus, ["masonry", "kanban"])) return "board";
  if (hasAny(focus, ["bottom nav"])) return "bottom-nav";
  if (hasAny(focus, ["faq", "accordion"])) return "faq";
  if (hasAny(focus, ["cuối khóa", "landing page hoàn chỉnh"])) return "final-project";
  if (hasAny(focus, ["căn giữa"])) return "center";

  return moduleIndex === 3 ? "project" : "intro";
}

function visualModeForKind(kind) {
  const map = {
    "axis": "center",
    "direction": "column",
    "gap": "space",
    "justify": "space",
    "align-items": "center",
    "align-self": "center",
    "wrap": "wrap",
    "align-content": "wrap",
    "order": "order",
    "grow": "grow",
    "shrink": "shrink",
    "basis": "basis",
    "flex-shorthand": "basis",
    "margin-auto": "auto",
    "nested": "nested",
    "cards": "wrap",
    "pricing": "wrap",
    "gallery": "wrap",
    "sidebar": "basis",
    "navbar": "auto",
    "toolbar": "auto",
    "media": "grow",
    "form": "grow",
    "chips": "wrap",
    "board": "wrap",
    "footer": "basis"
  };

  return map[kind] || "center";
}

function renderList(items) {
  return items.map((item) => `            <li>${item}</li>`).join("\n");
}

function renderSteps(items) {
  return items.map((item) => `            <li>${item}</li>`).join("\n");
}

function workflowForKind(kind, title, module, number) {
  const defaults = {
    steps: [
      `Khoanh vùng phần layout liên quan đến <strong>${title}</strong>.`,
      "Chọn phần tử cha làm flex container và kiểm tra các item con trực tiếp.",
      "Viết CSS tối thiểu trước, sau đó mới thêm màu, padding, border hoặc hiệu ứng.",
      "Thu nhỏ màn hình để kiểm tra item có tràn, chồng chữ hoặc mất khoảng cách không."
    ],
    exercise: `Dựng một ví dụ nhỏ cho chủ đề <strong>${title}</strong>, đặt trong thư mục <code>bai-${pad(number)}-${module.slug}</code>. Bài làm cần có ít nhất một trạng thái desktop và một trạng thái mobile.`,
    practiceSteps: [
      "Tạo file <code>index.html</code> và <code>style.css</code>.",
      "Viết HTML đúng vai trò nội dung, không đặt class chỉ để trang trí.",
      `Áp dụng đúng thuộc tính Flexbox chính của bài <strong>${title}</strong>.`,
      "So sánh kết quả với phần preview và tự ghi chú điểm khác nhau.",
      "Kiểm tra ở chiều rộng khoảng 360px, 768px và desktop."
    ],
    criteria: [
      "Layout chính dùng Flexbox, không dùng table hoặc float để giả lập.",
      "Khoảng cách, căn chỉnh và thứ tự item đúng với mục tiêu bài học.",
      "Không có nội dung bị tràn ngang hoặc nút bị chồng lên chữ trên màn hình nhỏ."
    ],
    mistakes: [
      "Chọn sai container nên thuộc tính Flexbox không tác động đến item mong muốn.",
      "Thêm quá nhiều CSS trang trí trước khi kiểm tra bố cục cơ bản.",
      "Không kiểm tra responsive nên layout chỉ đúng trên một kích thước màn hình."
    ]
  };

  const map = {
    "direction": {
      steps: [
        "Tạo một container có 3 item theo thứ tự đọc tự nhiên.",
        "Thử lần lượt <code>row</code>, <code>column</code>, <code>row-reverse</code> và ghi lại sự thay đổi main axis.",
        "Thêm media query để desktop dùng hàng ngang, mobile dùng cột dọc.",
        "Kiểm tra thứ tự đọc có còn hợp lý khi dùng reverse không."
      ],
      exercise: "Tạo một layout gồm header, content và sidebar. Desktop xếp ngang, mobile xếp dọc bằng <code>flex-direction</code>.",
      practiceSteps: [
        "Viết HTML theo thứ tự: header, content, sidebar.",
        "Đặt container <code>display: flex</code> và <code>flex-direction: row</code>.",
        "Trong media query dưới 640px, chuyển container sang <code>column</code>.",
        "Không dùng <code>row-reverse</code> để sửa thứ tự HTML sai.",
        "Chụp hoặc ghi chú sự khác nhau giữa desktop và mobile."
      ],
      mistakes: [
        "Nhầm <code>column</code> với căn giữa theo chiều dọc.",
        "Dùng reverse khiến thứ tự hiển thị khác thứ tự đọc tự nhiên.",
        "Quên rằng đổi direction cũng làm main axis đổi theo."
      ]
    },
    "justify": {
      steps: [
        "Tạo container rộng hơn tổng chiều rộng item để thấy khoảng trống.",
        "Thử <code>flex-start</code>, <code>center</code>, <code>space-between</code>, <code>space-evenly</code>.",
        "Quan sát item di chuyển trên main axis, không phải lúc nào cũng là chiều ngang.",
        "Áp dụng vào một pagination hoặc toolbar thật."
      ],
      exercise: "Tạo thanh pagination có nút Trước nằm sát trái, các số trang ở giữa và nút Sau nằm sát phải.",
      practiceSteps: [
        "Tạo 5 link trong một <code>nav</code>.",
        "Đặt <code>display: flex</code> và <code>gap</code> cho nav.",
        "Dùng <code>justify-content</code> để căn cụm link.",
        "Dùng auto margin cho nút đầu/cuối nếu cần tách biên.",
        "Thử đổi sang <code>space-between</code> và so sánh kết quả."
      ],
      mistakes: [
        "Không thấy tác dụng vì container không còn khoảng trống.",
        "Dùng <code>justify-content</code> để căn cross axis.",
        "Lạm dụng nhiều margin thay vì chọn đúng kiểu phân phối."
      ]
    },
    "align-items": {
      steps: [
        "Tạo hàng có avatar, text và badge với chiều cao khác nhau.",
        "Đặt container cao hơn nội dung để thấy cross axis.",
        "Thử <code>flex-start</code>, <code>center</code>, <code>flex-end</code>.",
        "Dùng <code>align-self</code> cho một item đặc biệt nếu cần."
      ],
      exercise: "Tạo một dòng thông tin người dùng: avatar, tên, mô tả và badge trạng thái. Avatar và text căn giữa theo chiều dọc, badge nằm trên cùng.",
      mistakes: [
        "Container không có chiều cao nên khó thấy sự khác nhau.",
        "Đặt <code>align-items</code> trên item thay vì container.",
        "Dùng padding để căn dọc thay vì để Flexbox xử lý."
      ]
    },
    "align-self": {
      exercise: "Tạo một hàng 3 card nhỏ, trong đó card thứ hai tự căn xuống cuối container bằng <code>align-self</code>.",
      practiceSteps: [
        "Tạo container cao tối thiểu 180px.",
        "Đặt container <code>display: flex</code> và <code>align-items: flex-start</code>.",
        "Gán <code>align-self: flex-end</code> cho item cần nổi bật.",
        "Thử đổi item đó sang <code>center</code> và quan sát.",
        "Ghi chú vì sao thuộc tính này phải đặt trên item."
      ]
    },
    "wrap": {
      exercise: "Tạo danh sách 12 tag kỹ năng. Tag tự xuống dòng, giữ khoảng cách ngang/dọc đều và không tràn màn hình.",
      practiceSteps: [
        "Tạo container <code>.tags</code> chứa ít nhất 12 <code>span</code>.",
        "Đặt <code>display: flex</code>, <code>flex-wrap: wrap</code> và <code>gap</code>.",
        "Đặt padding cho từng tag, không đặt width cố định quá lớn.",
        "Thử thêm tag có text dài để kiểm tra wrap.",
        "Kiểm tra ở mobile xem có thanh cuộn ngang không."
      ],
      mistakes: [
        "Quên <code>flex-wrap: wrap</code> làm toàn bộ tag bị ép trên một dòng.",
        "Đặt item width quá lớn khiến mobile bị tràn.",
        "Dùng margin cho từng tag rồi khó kiểm soát khoảng dọc."
      ]
    },
    "align-content": {
      exercise: "Tạo một bảng tag nhiều dòng trong khung cao 320px, sau đó căn toàn bộ nhóm dòng vào giữa khung bằng <code>align-content</code>.",
      practiceSteps: [
        "Tạo container có <code>min-height: 320px</code>.",
        "Bật <code>display: flex</code> và <code>flex-wrap: wrap</code>.",
        "Đặt mỗi item có <code>flex-basis</code> cố định để tạo nhiều dòng.",
        "Thử <code>align-content: flex-start</code>, <code>center</code>, <code>space-between</code>.",
        "So sánh với <code>align-items</code> để thấy khác biệt."
      ]
    },
    "grow": {
      exercise: "Tạo thanh tìm kiếm gồm logo, input và button. Input phải chiếm toàn bộ phần trống còn lại.",
      practiceSteps: [
        "Tạo container gồm logo, input search và button.",
        "Đặt container <code>display: flex</code>, <code>align-items: center</code>, <code>gap</code>.",
        "Gán input <code>flex: 1</code> và <code>min-width: 0</code>.",
        "Giữ logo và button bằng <code>flex: 0 0 auto</code>.",
        "Nhập placeholder dài để kiểm tra không tràn layout."
      ],
      mistakes: [
        "Gán <code>flex: 1</code> cho sai item.",
        "Quên <code>min-width: 0</code> làm input hoặc text dài gây tràn.",
        "Đặt width cố định cho input nên không co giãn theo container."
      ]
    },
    "shrink": {
      exercise: "Tạo notification row có avatar, nội dung dài và nút Xem. Avatar và nút không được bị co nhỏ.",
      practiceSteps: [
        "Tạo HTML gồm avatar, đoạn nội dung dài và button.",
        "Đặt row <code>display: flex</code> và <code>gap</code>.",
        "Gán avatar/button <code>flex-shrink: 0</code>.",
        "Gán phần nội dung <code>flex: 1 1 auto</code> và <code>min-width: 0</code>.",
        "Thu nhỏ màn hình để kiểm tra nội dung co lại đúng."
      ]
    },
    "basis": {
      exercise: "Tạo danh sách khóa học có card bắt đầu ở 220px, được co giãn và xuống dòng khi thiếu chỗ.",
      practiceSteps: [
        "Tạo container chứa ít nhất 6 card.",
        "Đặt container <code>display: flex</code>, <code>flex-wrap: wrap</code>, <code>gap</code>.",
        "Gán card <code>flex: 1 1 220px</code>.",
        "Thử đổi basis sang 180px và 300px để quan sát số cột.",
        "Ghi chú khi nào nên tăng hoặc giảm basis."
      ]
    },
    "flex-shorthand": {
      exercise: "Tạo layout gồm sidebar và content, dùng shorthand <code>flex</code> để sidebar cố định còn content co giãn.",
      practiceSteps: [
        "Sidebar dùng <code>flex: 0 0 240px</code>.",
        "Content dùng <code>flex: 1 1 auto</code> và <code>min-width: 0</code>.",
        "Thêm media query để layout thành cột trên mobile.",
        "Thử đổi sidebar sang <code>flex: 1</code> để thấy lỗi.",
        "Giải thích ý nghĩa grow, shrink, basis trong bài làm."
      ]
    },
    "margin-auto": {
      exercise: "Tạo card có nội dung dài ngắn khác nhau nhưng nút hành động luôn nằm cuối card.",
      practiceSteps: [
        "Tạo card dùng <code>display: flex</code> và <code>flex-direction: column</code>.",
        "Thêm tiêu đề, mô tả và button.",
        "Gán button <code>margin-top: auto</code>.",
        "Tạo 3 card có độ dài mô tả khác nhau để kiểm tra.",
        "So sánh với cách dùng padding/margin cố định."
      ]
    },
    "navbar": {
      exercise: "Tạo navbar gồm logo, 4 link menu và nút Đăng nhập. Desktop nằm một hàng, mobile menu xuống hàng riêng.",
      practiceSteps: [
        "Tạo <code>header</code> chứa logo, <code>nav</code> và button.",
        "Đặt header <code>display: flex</code>, <code>align-items: center</code>, <code>gap</code>.",
        "Dùng <code>margin-left: auto</code> cho nav hoặc nhóm action.",
        "Bật <code>flex-wrap: wrap</code> để mobile không tràn.",
        "Đặt nav width 100% trong media query nếu muốn link nằm hàng riêng."
      ]
    },
    "toolbar": {
      exercise: "Tạo toolbar soạn bài gồm Lưu, Xem trước, Xuất bản và Xóa. Nút Xóa nằm tách về cuối hàng.",
      practiceSteps: [
        "Tạo 4 button trong <code>.toolbar</code>.",
        "Đặt toolbar <code>display: flex</code>, <code>align-items: center</code>, <code>gap</code>.",
        "Gán nút Xóa <code>margin-left: auto</code>.",
        "Bật <code>flex-wrap</code> để các nút xuống dòng khi hẹp.",
        "Kiểm tra khoảng cách giữa các nhóm nút."
      ]
    },
    "media": {
      exercise: "Tạo comment row gồm avatar, tên, nội dung và thời gian. Nội dung co giãn, thời gian nằm bên phải.",
      practiceSteps: [
        "Avatar dùng <code>flex: 0 0 48px</code>.",
        "Phần nội dung dùng <code>flex: 1</code> và <code>min-width: 0</code>.",
        "Thời gian dùng <code>margin-left: auto</code>.",
        "Thêm nội dung dài để kiểm tra dòng không phá layout.",
        "Mobile vẫn phải đọc được avatar, text và thời gian."
      ]
    },
    "form": {
      exercise: "Tạo form newsletter gồm label, input email và button. Input chiếm phần còn lại trên desktop, form thành cột trên mobile.",
      practiceSteps: [
        "Tạo <code>form</code> chứa label, input và button.",
        "Đặt form <code>display: flex</code>, <code>align-items: end</code>, <code>gap</code>.",
        "Gán nhóm input <code>flex: 1</code>.",
        "Trong media query, đổi form sang <code>flex-direction: column</code>.",
        "Đảm bảo input và button rộng 100% trên mobile."
      ]
    },
    "cards": {
      exercise: "Tạo danh sách 6 card khóa học tự chia cột, các nút trong card nằm cuối.",
      practiceSteps: [
        "Container card dùng <code>display: flex</code>, <code>flex-wrap: wrap</code>, <code>gap</code>.",
        "Mỗi card dùng <code>flex: 1 1 220px</code>.",
        "Card dùng <code>display: flex</code>, <code>flex-direction: column</code>.",
        "Button trong card dùng <code>margin-top: auto</code>.",
        "Kiểm tra card xuống dòng ở tablet và mobile."
      ]
    },
    "sidebar": {
      exercise: "Tạo layout dashboard gồm sidebar, content header và đoạn nội dung. Sidebar cố định trên desktop, nằm trên content ở mobile.",
      practiceSteps: [
        "Tạo <code>.app-layout</code> chứa <code>.sidebar</code> và <code>.content</code>.",
        "Đặt layout <code>display: flex</code>.",
        "Sidebar dùng <code>flex: 0 0 220px</code>, content dùng <code>flex: 1</code>.",
        "Thêm <code>min-width: 0</code> cho content.",
        "Media query dưới 768px đổi layout sang column."
      ]
    },
    "board": {
      exercise: "Tạo board 3 cột Todo, Doing, Done. Mỗi cột rộng cố định và có thể cuộn ngang khi màn hình nhỏ.",
      practiceSteps: [
        "Tạo container <code>.board</code> chứa 3 cột.",
        "Đặt <code>display: flex</code>, <code>gap</code>, <code>overflow-x: auto</code>.",
        "Mỗi cột dùng <code>flex: 0 0 240px</code>.",
        "Thêm vài card nhỏ trong mỗi cột.",
        "Kiểm tra mobile: board không làm trang bị vỡ chiều ngang."
      ]
    }
  };

  const alias = {
    "pricing": "cards",
    "gallery": "wrap",
    "footer": "basis",
    "hero": "direction",
    "list-item": "media",
    "table-row": "media",
    "modal-footer": "toolbar",
    "button-group": "toolbar",
    "breadcrumb": "toolbar",
    "tabs": "toolbar",
    "stepper": "wrap",
    "chips": "wrap",
    "bottom-nav": "toolbar",
    "faq": "nested",
    "final-project": "project",
    "project": "nested",
    "debug": "intro",
    "inline-flex": "navbar",
    "container-item": "nested",
    "axis": "direction",
    "align-self": "align-items",
    "align-content": "wrap"
  };
  const practiceKind = alias[kind] || kind;

  return { ...defaults, ...(map[practiceKind] || {}) };
}

function lessonContent(module, moduleIndex, lesson, lessonIndex) {
  const number = lessonIndex + 1;
  const kind = lessonKind(lesson, moduleIndex);
  const title = lesson;
  const base = {
    objectives: [
      `Hiểu chính xác bài <strong>${title}</strong> giải quyết vấn đề bố cục nào trong giao diện web.`,
      `Xác định thuộc tính cần đặt ở flex container và thuộc tính cần đặt ở flex item cho chủ đề này.`,
      `Tự dựng được một ví dụ nhỏ, kiểm tra trên desktop và mobile, rồi giải thích được vì sao layout hoạt động.`
    ],
    theory: [
      `Trong bài này, trọng tâm là biến yêu cầu giao diện thành cấu trúc cha con rõ ràng. Flexbox chỉ tác động lên các phần tử con trực tiếp, vì vậy bước quan trọng nhất là chọn đúng container.`,
      `Khi code, hãy đi theo thứ tự: viết HTML có nghĩa, bật <code>display: flex</code>, chọn hướng, căn chỉnh, sau đó mới xử lý co giãn hoặc responsive. Cách này giúp bạn không phải thử thuộc tính một cách ngẫu nhiên.`
    ],
    steps: [
      `Khoanh vùng phần layout liên quan đến <strong>${title}</strong>.`,
      `Chọn phần tử cha làm flex container và kiểm tra các item con trực tiếp.`,
      `Viết CSS tối thiểu trước, sau đó mới thêm màu, padding, border hoặc hiệu ứng.`,
      `Thu nhỏ màn hình để kiểm tra item có tràn, chồng chữ hoặc mất khoảng cách không.`
    ],
    exercise: `Dựng một ví dụ nhỏ cho chủ đề <strong>${title}</strong>, đặt trong thư mục <code>bai-${pad(number)}-${module.slug}</code>. Bài làm cần có ít nhất một trạng thái desktop và một trạng thái mobile.`,
    practiceSteps: [
      `Tạo file <code>index.html</code> và <code>style.css</code>.`,
      `Viết HTML đúng vai trò nội dung, không đặt class chỉ để trang trí.`,
      `Áp dụng đúng thuộc tính Flexbox chính của bài <strong>${title}</strong>.`,
      `So sánh kết quả với phần preview và tự ghi chú điểm khác nhau.`,
      `Kiểm tra ở chiều rộng khoảng 360px, 768px và desktop.`
    ],
    criteria: [
      `Layout chính dùng Flexbox, không dùng table hoặc float để giả lập.`,
      `Khoảng cách, căn chỉnh và thứ tự item đúng với mục tiêu bài học.`,
      `Không có nội dung bị tràn ngang hoặc nút bị chồng lên chữ trên màn hình nhỏ.`
    ],
    mistakes: [
      `Chọn sai container nên thuộc tính Flexbox không tác động đến item mong muốn.`,
      `Thêm quá nhiều CSS trang trí trước khi kiểm tra bố cục cơ bản.`,
      `Không kiểm tra responsive nên layout chỉ đúng trên một kích thước màn hình.`
    ],
    demo: `Minh họa bên dưới tập trung vào cơ chế chính của bài <strong>${title}</strong>. Hãy nhìn hướng di chuyển, khoảng cách và kích thước của từng item trước khi đọc code.`,
    codeNote: `Ví dụ này dùng một tình huống gần với giao diện thật để bạn thấy <strong>${title}</strong> được áp dụng trong thực tế, không chỉ là các ô vuông mẫu.`,
    solutionNote: `Bài giải tham khảo ưu tiên CSS ngắn và dễ đọc. Sau khi xem lời giải, hãy tự chỉ ra dòng nào điều khiển container và dòng nào điều khiển item.`
  };

  const profiles = {
    "intro": {
      objectives: [
        "Phân biệt khi nào Flexbox phù hợp hơn float, inline-block hoặc table layout.",
        "Nhìn một giao diện đơn giản và chỉ ra phần nào nên là flex container.",
        "Tạo được hàng item đầu tiên bằng <code>display: flex</code> và giải thích item con trực tiếp."
      ],
      theory: [
        "Flexbox phù hợp nhất cho bố cục một chiều: một hàng hoặc một cột. Menu ngang, toolbar, hàng avatar và nội dung, nhóm nút, card row là các ví dụ điển hình.",
        "Nếu cần bố cục hai chiều phức tạp theo cả hàng và cột, CSS Grid thường phù hợp hơn. Trong khóa này, ta dùng Flexbox để hiểu cách căn chỉnh và co giãn item trong một trục chính."
      ]
    },
    "inline-flex": {
      objectives: [
        "Phân biệt <code>display: flex</code> và <code>display: inline-flex</code> về cách container chiếm chiều ngang.",
        "Tạo được badge, button group hoặc cụm icon nhỏ không chiếm cả dòng.",
        "Biết khi nào cần container là block-level và khi nào cần inline-level."
      ],
      theory: [
        "<code>display: flex</code> làm container cư xử như block: mặc định chiếm toàn bộ chiều ngang còn lại. <code>inline-flex</code> vẫn tạo flex formatting context bên trong, nhưng bản thân container chỉ rộng theo nội dung.",
        "Dùng <code>inline-flex</code> cho các thành phần nhỏ như badge có icon, nhãn trạng thái, cụm sao đánh giá hoặc nút có biểu tượng."
      ],
      steps: [
        "Tạo hai cụm link giống nhau, một cụm dùng <code>display: flex</code>, cụm còn lại dùng <code>inline-flex</code>.",
        "Thêm nền và border để quan sát chiều rộng thật của từng container.",
        "Đặt hai container cạnh đoạn text để thấy sự khác nhau khi xuống dòng."
      ]
    },
    "container-item": {
      objectives: [
        "Xác định đúng flex container và các flex item con trực tiếp.",
        "Hiểu vì sao phần tử cháu không tự động bị căn chỉnh bởi container ông.",
        "Biết thêm một flex container lồng bên trong khi cần căn nội dung sâu hơn."
      ],
      theory: [
        "Flexbox chỉ áp dụng trực tiếp cho con cấp một của container. Nếu một item chứa nhiều phần tử bên trong và bạn muốn căn chúng, item đó cần được đặt <code>display: flex</code> riêng.",
        "Nhầm container là lỗi phổ biến nhất của người mới. Trước khi viết CSS, hãy gạch chân phần tử cha và đánh số các con trực tiếp."
      ]
    },
    "axis": {
      objectives: [
        "Giải thích được main axis và cross axis bằng lời của mình.",
        "Biết vì sao <code>justify-content</code> không luôn luôn là căn ngang.",
        "Dự đoán được layout thay đổi thế nào khi đổi <code>flex-direction</code>."
      ],
      theory: [
        "Main axis là hướng item chạy chính. Với <code>row</code>, main axis nằm ngang; với <code>column</code>, main axis nằm dọc. Cross axis luôn vuông góc với main axis.",
        "Khi bạn đổi <code>flex-direction</code>, vai trò trực quan của <code>justify-content</code> và <code>align-items</code> cũng đổi theo. Đây là lý do nhiều bạn căn giữa sai khi chuyển từ row sang column."
      ]
    },
    "direction": {
      objectives: [
        "Dùng được <code>flex-direction</code> để đổi hướng item theo hàng, cột và đảo chiều.",
        "Hiểu tác động của <code>row-reverse</code> và <code>column-reverse</code> đến thứ tự hiển thị.",
        "Biết chọn hướng phù hợp cho menu, form dọc, sidebar hoặc mobile layout."
      ],
      theory: [
        "<code>flex-direction</code> quyết định main axis. Giá trị mặc định là <code>row</code>. Khi dùng <code>column</code>, item xếp từ trên xuống dưới và <code>justify-content</code> bắt đầu điều khiển chiều dọc.",
        "Không nên dùng reverse chỉ để sửa HTML viết sai thứ tự. Hãy giữ HTML theo thứ tự đọc tự nhiên, chỉ dùng reverse khi thiết kế thật sự cần đảo chiều hiển thị."
      ]
    },
    "gap": {
      objectives: [
        "Tạo khoảng cách đều giữa item bằng <code>gap</code> thay vì margin rời rạc.",
        "Phân biệt khoảng cách giữa item và padding bên trong container.",
        "Thiết lập spacing scale nhất quán cho menu, card list và chip list."
      ],
      theory: [
        "<code>gap</code> là khoảng cách giữa các flex item. Nó không tạo khoảng ngoài container và không cần xử lý item đầu/cuối như khi dùng margin.",
        "Với layout có <code>flex-wrap</code>, <code>gap</code> kiểm soát cả khoảng ngang lẫn khoảng dọc, giúp card hoặc tag xuống dòng gọn hơn."
      ]
    },
    "justify": {
      objectives: [
        "Dùng đúng <code>justify-content</code> để phân phối item trên main axis.",
        "Phân biệt <code>space-between</code>, <code>space-around</code> và <code>space-evenly</code>.",
        "Biết chọn kiểu căn phù hợp cho toolbar, navbar và pagination."
      ],
      theory: [
        "<code>justify-content</code> chỉ có tác dụng rõ khi container còn khoảng trống trên main axis. Nếu tổng kích thước item đã chiếm hết chiều ngang, bạn sẽ khó thấy sự thay đổi.",
        "<code>space-between</code> thường dùng để đẩy item đầu và cuối ra hai biên; <code>center</code> dùng khi muốn cụm item nằm giữa container."
      ]
    },
    "align-items": {
      objectives: [
        "Căn item theo cross axis bằng <code>align-items</code>.",
        "Xử lý hàng có item cao thấp khác nhau như avatar, badge, nút và text.",
        "Biết khi nào cần đặt chiều cao container để quan sát căn dọc."
      ],
      theory: [
        "<code>align-items</code> căn toàn bộ item theo cross axis. Với hàng ngang, nó thường điều khiển vị trí dọc: trên, giữa, dưới hoặc kéo giãn.",
        "Giá trị <code>stretch</code> là mặc định trong nhiều trường hợp, khiến item tự cao bằng container nếu không đặt chiều cao riêng."
      ]
    },
    "align-self": {
      objectives: [
        "Căn riêng một item khác với các item còn lại bằng <code>align-self</code>.",
        "Biết dùng <code>align-self</code> cho badge, nút hoặc item đặc biệt.",
        "Không lạm dụng <code>align-self</code> khi có thể chỉnh bằng cấu trúc container rõ hơn."
      ],
      theory: [
        "<code>align-self</code> đặt trên flex item, ghi đè <code>align-items</code> của container cho riêng item đó.",
        "Thuộc tính này hữu ích khi một hàng có một item cần nằm trên cùng hoặc dưới cùng, trong khi các item còn lại vẫn căn giữa."
      ]
    },
    "wrap": {
      objectives: [
        "Cho item xuống dòng bằng <code>flex-wrap: wrap</code> khi không đủ chiều ngang.",
        "Kết hợp <code>gap</code> và <code>flex-basis</code> để tạo danh sách card responsive.",
        "Tránh layout tràn ngang trên màn hình nhỏ."
      ],
      theory: [
        "Mặc định Flexbox cố giữ tất cả item trên một dòng. <code>flex-wrap: wrap</code> cho phép item chuyển sang dòng mới khi không còn đủ chỗ.",
        "Để wrap hoạt động đẹp, mỗi item nên có kích thước khởi đầu hợp lý, ví dụ <code>flex: 1 1 220px</code> cho card."
      ]
    },
    "align-content": {
      objectives: [
        "Hiểu <code>align-content</code> chỉ rõ khi container có nhiều dòng flex.",
        "Căn các dòng flex theo cross axis khi dùng <code>flex-wrap</code>.",
        "Phân biệt <code>align-content</code> với <code>align-items</code>."
      ],
      theory: [
        "<code>align-items</code> căn item trong từng dòng; <code>align-content</code> căn cả nhóm dòng trong container. Nếu chỉ có một dòng, <code>align-content</code> gần như không tạo khác biệt.",
        "Muốn thấy tác dụng, container cần có chiều cao lớn hơn tổng chiều cao các dòng và có <code>flex-wrap: wrap</code>."
      ]
    },
    "order": {
      objectives: [
        "Đổi thứ tự hiển thị bằng <code>order</code> mà không sửa HTML.",
        "Hiểu rủi ro accessibility khi thứ tự hiển thị khác thứ tự đọc.",
        "Dùng <code>order</code> có kiểm soát cho layout mobile."
      ],
      theory: [
        "<code>order</code> đặt trên flex item. Item có order nhỏ hơn hiển thị trước. Mặc định mọi item có <code>order: 0</code>.",
        "Không nên dùng <code>order</code> để che cấu trúc HTML lộn xộn. Screen reader và thứ tự tab vẫn có thể đi theo DOM, không theo thứ tự bạn nhìn thấy."
      ]
    },
    "grow": {
      objectives: [
        "Dùng <code>flex-grow</code> hoặc <code>flex: 1</code> để item chiếm phần trống còn lại.",
        "Tạo search bar, content area hoặc card co giãn đúng ý.",
        "Biết vì sao cần <code>min-width: 0</code> trong nhiều layout có text dài."
      ],
      theory: [
        "<code>flex-grow</code> quyết định item có được lớn thêm khi container còn khoảng trống hay không. Giá trị là tỉ lệ chia phần trống giữa các item có grow.",
        "<code>flex: 1</code> là cách viết ngắn phổ biến cho item cần chiếm phần còn lại, nhưng vẫn cần kiểm soát <code>min-width</code> khi nội dung dài."
      ]
    },
    "shrink": {
      objectives: [
        "Hiểu cách <code>flex-shrink</code> làm item co lại khi thiếu chỗ.",
        "Bảo vệ item quan trọng như avatar, icon hoặc nút không bị ép quá nhỏ.",
        "Xử lý text dài bằng <code>min-width: 0</code> và overflow phù hợp."
      ],
      theory: [
        "<code>flex-shrink</code> mặc định là 1, nghĩa là item được phép co lại. Đặt <code>flex-shrink: 0</code> cho item cần giữ kích thước như avatar.",
        "Một item chứa chữ dài có thể làm layout tràn nếu không cho nó co đúng cách. Khi đó <code>min-width: 0</code> trên item nội dung thường là dòng CSS quan trọng."
      ]
    },
    "basis": {
      objectives: [
        "Dùng <code>flex-basis</code> để đặt kích thước khởi đầu của item trước khi co giãn.",
        "Tạo card responsive có chiều rộng tối thiểu hợp lý.",
        "Phân biệt <code>basis</code> với <code>width</code> trong flex layout."
      ],
      theory: [
        "<code>flex-basis</code> là kích thước ban đầu trên main axis. Với <code>row</code>, nó giống chiều rộng khởi đầu; với <code>column</code>, nó giống chiều cao khởi đầu.",
        "Công thức hay dùng cho card là <code>flex: 1 1 240px</code>: bắt đầu ở 240px, được phép co và giãn theo container."
      ]
    },
    "flex-shorthand": {
      objectives: [
        "Đọc được cú pháp <code>flex: grow shrink basis</code>.",
        "Viết được các cấu hình phổ biến như <code>flex: 1</code>, <code>flex: 0 0 240px</code>.",
        "Chọn shorthand phù hợp cho card, sidebar và content."
      ],
      theory: [
        "<code>flex</code> là shorthand cho ba giá trị: grow, shrink và basis. Dùng shorthand giúp CSS ngắn, nhưng bạn cần hiểu từng phần để tránh item co giãn sai.",
        "Ví dụ sidebar cố định thường dùng <code>flex: 0 0 240px</code>, còn content chính thường dùng <code>flex: 1</code>."
      ]
    },
    "margin-auto": {
      objectives: [
        "Dùng <code>margin-left: auto</code> hoặc <code>margin-top: auto</code> để đẩy item trong flex layout.",
        "Tạo navbar có nút nằm sát phải hoặc card có nút nằm cuối.",
        "Biết khi nào auto margin đơn giản hơn <code>justify-content</code>."
      ],
      theory: [
        "Trong flex layout, auto margin hấp thụ phần trống trên trục tương ứng. <code>margin-left: auto</code> thường dùng để đẩy một item sang phải trong hàng ngang.",
        "<code>margin-top: auto</code> rất hữu ích trong card dạng column để nút hành động nằm cuối card dù nội dung dài ngắn khác nhau."
      ]
    },
    "nested": {
      objectives: [
        "Tạo flex container lồng nhau để xử lý bố cục nhiều cấp.",
        "Phân tách layout tổng thể và layout bên trong từng item.",
        "Tránh viết một container quá lớn ôm quá nhiều trách nhiệm."
      ],
      theory: [
        "Một flex item có thể đồng thời là flex container cho các phần tử con của nó. Đây là cách xây navbar có nhóm link, card có header/body/footer hoặc dashboard có nhiều vùng.",
        "Nguyên tắc là mỗi container chỉ nên giải quyết một trục bố cục chính. Nếu cần căn tiếp bên trong item, tạo một flex context mới."
      ]
    },
    "debug": {
      objectives: [
        "Dùng DevTools để nhận diện flex container, trục và kích thước item.",
        "Kiểm tra nhanh thuộc tính nào đang bị ghi đè hoặc đặt sai phần tử.",
        "Tạo thói quen debug layout thay vì đoán mò."
      ],
      theory: [
        "DevTools của trình duyệt có overlay cho Flexbox. Bạn có thể bật đường trục, xem khoảng gap, kích thước item và các thuộc tính đang áp dụng.",
        "Khi layout sai, hãy kiểm tra theo thứ tự: container đã <code>display: flex</code> chưa, item có phải con trực tiếp không, thuộc tính đang đặt ở container hay item."
      ]
    }
  };

  const patternProfiles = {
    "navbar": {
      objectives: [
        "Tạo header có logo, menu và nút hành động bằng Flexbox.",
        "Đẩy nhóm menu hoặc nút sang phải bằng <code>margin-left: auto</code>.",
        "Cho menu tự xuống dòng trên mobile mà không tràn ngang."
      ],
      theory: [
        "Navbar thường là một hàng flex gồm logo, nhóm link và nhóm action. Logo nên giữ kích thước tự nhiên, còn nhóm link có thể dùng <code>margin-left: auto</code> để tách khỏi logo.",
        "Khi mobile, đừng ép tất cả link nằm trên một hàng. Cho container <code>flex-wrap: wrap</code> hoặc chuyển nhóm link thành một hàng riêng."
      ]
    },
    "toolbar": {
      objectives: [
        "Tạo toolbar có nhiều nhóm nút và hành động chính/phụ.",
        "Dùng <code>gap</code> để quản lý khoảng cách giữa nút.",
        "Đẩy nhóm hành động nguy hiểm hoặc lưu thay đổi sang cuối hàng."
      ],
      theory: [
        "Toolbar khác navbar ở chỗ các nút thường là thao tác trực tiếp. Bạn nên chia nhóm bằng wrapper nhỏ, mỗi nhóm là một flex container riêng.",
        "Dùng auto margin cho nhóm cuối giúp toolbar vẫn rõ ràng khi thêm hoặc bớt nút."
      ]
    },
    "media": {
      objectives: [
        "Tạo bố cục avatar cố định và nội dung co giãn.",
        "Căn thời gian, badge hoặc action về cuối hàng.",
        "Xử lý text dài trong phần nội dung bằng <code>min-width: 0</code>."
      ],
      theory: [
        "Media object là pattern gồm hình/biểu tượng bên trái và nội dung bên phải. Avatar thường dùng <code>flex: 0 0 48px</code>, nội dung dùng <code>flex: 1</code>.",
        "Nếu có thời gian hoặc nút action bên phải, dùng <code>margin-left: auto</code> để đẩy nó ra cuối hàng."
      ]
    },
    "form": {
      objectives: [
        "Sắp xếp label, input và button trên cùng một hàng bằng Flexbox.",
        "Cho input co giãn, button giữ kích thước tự nhiên.",
        "Chuyển form thành cột trên mobile."
      ],
      theory: [
        "Form row thường cần input chiếm phần còn lại. Đặt input wrapper <code>flex: 1</code> và nút <code>flex: 0 0 auto</code>.",
        "Trên mobile, chuyển <code>flex-direction: column</code> giúp label, input và button dễ đọc hơn."
      ]
    },
    "cards": {
      objectives: [
        "Tạo danh sách card tự co giãn theo chiều rộng màn hình.",
        "Dùng <code>flex-wrap</code> và <code>flex: 1 1 ...</code> để card xuống dòng đẹp.",
        "Giữ nút trong card nằm cuối bằng <code>margin-top: auto</code>."
      ],
      theory: [
        "Card list là bài thực tế tốt để kết hợp wrap, gap và flex shorthand. Container dùng <code>display: flex</code>, <code>flex-wrap: wrap</code>, item dùng <code>flex: 1 1 220px</code>.",
        "Nếu card có nội dung dài ngắn khác nhau, đặt card là flex column và dùng <code>margin-top: auto</code> cho nút."
      ]
    },
    "sidebar": {
      objectives: [
        "Tạo layout sidebar cố định và content co giãn.",
        "Biết dùng <code>flex: 0 0 240px</code> cho sidebar và <code>flex: 1</code> cho main.",
        "Chuyển sidebar lên trên hoặc xuống dưới nội dung trên mobile."
      ],
      theory: [
        "Layout sidebar/content là pattern cốt lõi của dashboard. Sidebar cần kích thước ổn định; content cần chiếm toàn bộ phần còn lại.",
        "Đặt <code>min-width: 0</code> cho content để bảng, text dài hoặc card bên trong không làm layout tràn ngang."
      ]
    },
    "pricing": {
      objectives: [
        "Xây pricing section nhiều gói dịch vụ bằng Flexbox.",
        "Giữ các pricing card cao bằng nhau và nút nằm cuối.",
        "Cho pricing card xuống dòng hợp lý trên tablet/mobile."
      ],
      theory: [
        "Pricing card cần so sánh dễ đọc, vì vậy khoảng cách và chiều cao card phải nhất quán. Flexbox giúp các card cùng hàng tự cân bằng chiều cao.",
        "Đặt từng card là flex column để phần mô tả có thể dài ngắn khác nhau nhưng nút hành động vẫn nằm cùng vị trí."
      ]
    },
    "gallery": {
      objectives: [
        "Tạo gallery hoặc portfolio list tự xuống dòng.",
        "Kiểm soát khoảng cách ngang/dọc bằng <code>gap</code>.",
        "Đặt kích thước item đủ linh hoạt để ảnh không vỡ layout."
      ],
      theory: [
        "Gallery dùng Flexbox phù hợp khi item có kích thước gần giống nhau và chỉ cần tự xuống dòng. Dùng <code>flex-wrap: wrap</code> và basis phù hợp.",
        "Nếu cần căn theo cả hàng và cột rất chặt, CSS Grid có thể tốt hơn; nhưng Flexbox vẫn rất ổn cho gallery đơn giản."
      ]
    },
    "stepper": {
      objectives: [
        "Tạo stepper/timeline có các bước nằm trên một hàng hoặc xuống dòng.",
        "Dùng Flexbox để căn số bước, nhãn và đường nối.",
        "Giữ các bước dễ đọc trên mobile."
      ],
      theory: [
        "Stepper là danh sách các bước theo thứ tự. Container dùng flex để phân phối các bước, mỗi step có thể là flex column để căn số và nhãn.",
        "Khi không đủ chỗ, nên cho step xuống dòng hoặc chuyển thành cột để tránh chữ bị ép quá nhỏ."
      ]
    },
    "footer": {
      objectives: [
        "Tạo footer nhiều cột bằng Flexbox.",
        "Cho từng cột có kích thước tối thiểu và tự xuống dòng.",
        "Giữ khoảng cách đều giữa các nhóm link/footer form."
      ],
      theory: [
        "Footer nhiều cột thường dùng <code>flex-wrap</code>. Mỗi cột có thể đặt <code>flex: 1 1 220px</code> để tự chia hàng.",
        "Đừng cố nhồi mọi cột trên mobile; cho cột xuống dòng giúp footer dễ đọc và không tràn ngang."
      ]
    },
    "project": {
      objectives: [
        `Phân tích yêu cầu của bài <strong>${title}</strong> thành các khối layout nhỏ.`,
        "Chọn đúng container cho từng vùng giao diện thay vì viết một flex container quá lớn.",
        "Hoàn thiện layout có desktop, mobile, code bài giải và tiêu chí tự chấm."
      ],
      theory: [
        "Với bài dự án, hãy bắt đầu bằng cách chia giao diện thành các vùng: header, nội dung chính, danh sách item, footer hoặc action bar. Mỗi vùng thường cần một flex container riêng.",
        "Làm từ ngoài vào trong: layout tổng thể trước, sau đó mới căn từng card, từng dòng thông tin hoặc từng nhóm nút."
      ]
    }
  };

  const workflow = workflowForKind(kind, title, module, number);
  const merged = { ...base, ...workflow, ...(profiles[kind] || patternProfiles[kind] || {}) };

  if (!profiles[kind] && !patternProfiles[kind]) {
    merged.objectives = [
      `Phân tích bài <strong>${title}</strong> thành các flex container nhỏ, dễ kiểm soát.`,
      "Chọn đúng thuộc tính căn chỉnh, khoảng cách và co giãn cho từng vùng.",
      "Tạo được bản responsive không tràn ngang và có code dễ đọc."
    ];
    merged.theory = [
      `Chủ đề <strong>${title}</strong> là một tình huống thực hành. Điều quan trọng không phải nhớ nhiều thuộc tính, mà là biết tách giao diện thành các hàng/cột một chiều.`,
      "Khi một vùng có nhiều trách nhiệm, hãy chia nhỏ: container ngoài xử lý bố cục tổng thể, container trong xử lý căn nội dung."
    ];
  }

  if (!merged.objectives[0].includes(title)) {
    merged.objectives[0] = `${merged.objectives[0]} Trọng tâm áp dụng trong bài này là <strong>${title}</strong>.`;
  }

  if (!merged.exercise.includes(title)) {
    merged.exercise = `${merged.exercise} Chủ đề cần thể hiện rõ trong sản phẩm cuối: <strong>${title}</strong>.`;
  }

  return { ...merged, kind, visualMode: visualModeForKind(kind) };
}

function exampleBlock(moduleIndex, lessonIndex, title) {
  const focus = title.toLowerCase();
  const kind = lessonKind(title, moduleIndex);

  if (kind === "direction" || kind === "axis") {
    return {
      html: `<section class="direction-demo">
  <article>Header</article>
  <article>Nội dung chính</article>
  <article>Sidebar</article>
</section>`,
      css: `.direction-demo {
  display: flex;
  flex-direction: row;
  gap: 12px;
}

.direction-demo article {
  flex: 1;
}

@media (max-width: 640px) {
  .direction-demo {
    flex-direction: column;
  }
}`
    };
  }

  if (kind === "justify") {
    return {
      html: `<nav class="pagination">
  <a href="#">Trước</a>
  <a href="#">1</a>
  <a href="#">2</a>
  <a href="#">3</a>
  <a href="#">Sau</a>
</nav>`,
      css: `.pagination {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.pagination a:first-child {
  margin-right: auto;
}

.pagination a:last-child {
  margin-left: auto;
}`
    };
  }

  if (kind === "align-items" || kind === "align-self") {
    return {
      html: `<div class="user-row">
  <div class="avatar">A</div>
  <div>
    <strong>Nguyễn Văn A</strong>
    <p>Đang học Flexbox</p>
  </div>
  <span class="status">Online</span>
</div>`,
      css: `.user-row {
  min-height: 110px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.status {
  align-self: flex-start;
  margin-left: auto;
}`
    };
  }

  if (kind === "align-content") {
    return {
      html: `<section class="tag-board">
  <span>HTML</span><span>CSS</span><span>Flexbox</span>
  <span>Responsive</span><span>Layout</span><span>UI</span>
</section>`,
      css: `.tag-board {
  min-height: 220px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  gap: 10px;
}

.tag-board span {
  flex: 0 0 120px;
}`
    };
  }

  if (kind === "order") {
    return {
      html: `<section class="mobile-order">
  <aside class="filters">Bộ lọc</aside>
  <main class="results">Danh sách sản phẩm</main>
  <aside class="summary">Tóm tắt</aside>
</section>`,
      css: `.mobile-order {
  display: flex;
  gap: 12px;
}

.results {
  flex: 1;
}

@media (max-width: 640px) {
  .mobile-order {
    flex-direction: column;
  }

  .results {
    order: -1;
  }
}`
    };
  }

  if (kind === "shrink") {
    return {
      html: `<article class="notice-row">
  <div class="avatar">N</div>
  <p>Nội dung thông báo rất dài cần được co lại thay vì đẩy avatar ra khỏi màn hình.</p>
  <button>Xem</button>
</article>`,
      css: `.notice-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.notice-row .avatar,
.notice-row button {
  flex-shrink: 0;
}

.notice-row p {
  flex: 1 1 auto;
  min-width: 0;
}`
    };
  }

  if (kind === "basis" || kind === "flex-shorthand") {
    return {
      html: `<section class="course-list">
  <article>HTML cơ bản</article>
  <article>CSS Flexbox</article>
  <article>Responsive UI</article>
</section>`,
      css: `.course-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.course-list article {
  flex: 1 1 220px;
}`
    };
  }

  if (kind === "margin-auto") {
    return {
      html: `<article class="task-card">
  <h3>Hoàn thành bài Flexbox</h3>
  <p>Đọc lý thuyết, tự code lại ví dụ và so sánh với bài giải.</p>
  <button>Đánh dấu xong</button>
</article>`,
      css: `.task-card {
  min-height: 240px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.task-card button {
  margin-top: auto;
  align-self: flex-start;
}`
    };
  }

  if (kind === "nested") {
    return {
      html: `<article class="course-card">
  <header>
    <h3>CSS Flexbox</h3>
    <span>20 bài</span>
  </header>
  <p>Học layout bằng các ví dụ trực quan.</p>
  <footer>
    <button>Học ngay</button>
    <a href="#">Chi tiết</a>
  </footer>
</article>`,
      css: `.course-card {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.course-card header,
.course-card footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}`
    };
  }

  if (kind === "debug") {
    return {
      html: `<section class="debug-layout">
  <div class="debug-item">Item 1</div>
  <div class="debug-item wide">Item 2 dài hơn</div>
  <div class="debug-item">Item 3</div>
</section>`,
      css: `.debug-layout {
  display: flex;
  gap: 12px;
  outline: 2px dashed #e85d4f;
}

.debug-item {
  flex: 1;
  outline: 2px solid #0f766e;
}

.debug-item.wide {
  flex: 2;
}`
    };
  }

  if (kind === "toolbar" || kind === "button-group") {
    return {
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
}`
    };
  }

  if (kind === "breadcrumb") {
    return {
      html: `<nav class="breadcrumb-demo">
  <a href="#">Trang chủ</a>
  <span>/</span>
  <a href="#">CSS</a>
  <span>/</span>
  <strong>Flexbox</strong>
</nav>`,
      css: `.breadcrumb-demo {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}`
    };
  }

  if (kind === "tabs") {
    return {
      html: `<nav class="tabs">
  <button class="active">Tổng quan</button>
  <button>Bài học</button>
  <button>Bài tập</button>
</nav>`,
      css: `.tabs {
  display: flex;
  gap: 8px;
  border-bottom: 1px solid #d9e2ec;
}

.tabs button {
  border-radius: 8px 8px 0 0;
}

.tabs .active {
  background: #18212f;
}`
    };
  }

  if (kind === "stepper") {
    return {
      html: `<ol class="stepper">
  <li><span>1</span>Chọn khóa</li>
  <li><span>2</span>Thực hành</li>
  <li><span>3</span>Nộp bài</li>
</ol>`,
      css: `.stepper {
  display: flex;
  gap: 12px;
  padding: 0;
  list-style: none;
}

.stepper li {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
}`
    };
  }

  if (kind === "footer") {
    return {
      html: `<footer class="site-footer">
  <section><h3>NenTang</h3><p>Học lập trình web.</p></section>
  <section><h3>Khóa học</h3><a href="#">HTML</a><a href="#">CSS</a></section>
  <section><h3>Nhận tin</h3><input placeholder="Email"></section>
</footer>`,
      css: `.site-footer {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}

.site-footer section {
  flex: 1 1 220px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}`
    };
  }

  if (kind === "hero") {
    return {
      html: `<section class="split-hero">
  <div>
    <h2>Học Flexbox trực quan</h2>
    <p>Code, xem kết quả và tự luyện bài tập.</p>
    <button>Bắt đầu</button>
  </div>
  <div class="hero-preview">Preview</div>
</section>`,
      css: `.split-hero {
  display: flex;
  align-items: center;
  gap: 24px;
}

.split-hero > * {
  flex: 1;
}

@media (max-width: 700px) {
  .split-hero {
    flex-direction: column;
  }
}`
    };
  }

  if (kind === "list-item" || kind === "table-row") {
    return {
      html: `<article class="data-row">
  <span class="file-icon">CSS</span>
  <div>
    <strong>shared.css</strong>
    <p>Đã cập nhật 2 phút trước</p>
  </div>
  <button>Mở</button>
</article>`,
      css: `.data-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.data-row div {
  flex: 1;
  min-width: 0;
}

.data-row button {
  margin-left: auto;
}`
    };
  }

  if (kind === "modal-footer") {
    return {
      html: `<footer class="modal-actions">
  <button class="secondary">Hủy</button>
  <button>Lưu thay đổi</button>
</footer>`,
      css: `.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.modal-actions .secondary {
  margin-right: auto;
  background: #64748b;
}`
    };
  }

  if (kind === "chips") {
    return {
      html: `<div class="chips">
  <span>HTML</span><span>CSS</span><span>Flexbox</span>
  <span>Responsive</span><span>UI</span><span>Project</span>
</div>`,
      css: `.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.chips span {
  padding: 6px 10px;
  border-radius: 999px;
  background: #ccfbf1;
}`
    };
  }

  if (kind === "board") {
    return {
      html: `<section class="board">
  <article><h3>Todo</h3><p>Học lý thuyết</p></article>
  <article><h3>Doing</h3><p>Làm bài tập</p></article>
  <article><h3>Done</h3><p>So sánh bài giải</p></article>
</section>`,
      css: `.board {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  overflow-x: auto;
}

.board article {
  flex: 0 0 240px;
}`
    };
  }

  if (kind === "bottom-nav") {
    return {
      html: `<nav class="bottom-nav">
  <a href="#">Home</a>
  <a href="#">Bài học</a>
  <a href="#">Bài tập</a>
  <a href="#">Hồ sơ</a>
</nav>`,
      css: `.bottom-nav {
  display: flex;
  justify-content: space-around;
  gap: 8px;
}

.bottom-nav a {
  flex: 1;
  text-align: center;
}`
    };
  }

  if (kind === "faq") {
    return {
      html: `<section class="faq-list">
  <article>
    <h3>Flexbox dùng để làm gì?</h3>
    <p>Dùng để căn chỉnh item theo một hàng hoặc một cột.</p>
  </article>
  <article>
    <h3>Khi nào dùng Grid?</h3>
    <p>Khi layout cần kiểm soát cả hàng và cột rõ ràng.</p>
  </article>
</section>`,
      css: `.faq-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.faq-list article {
  display: flex;
  flex-direction: column;
  gap: 6px;
}`
    };
  }

  if (focus.includes("grow") || focus.includes("search") || focus.includes("co giãn")) {
    return {
      html: `<div class="search-row">
  <a class="logo" href="#">NenTang</a>
  <input type="search" placeholder="Tìm bài học Flexbox">
  <button>Tìm kiếm</button>
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

.search-row button,
.search-row .logo {
  flex: 0 0 auto;
}`
    };
  }

  if (focus.includes("wrap") || focus.includes("gallery") || focus.includes("product") || focus.includes("card") || focus.includes("pricing")) {
    return {
      html: `<section class="card-list">
  <article class="card">
    <h3>Gói Cơ bản</h3>
    <p>Phù hợp người mới học HTML/CSS.</p>
    <button>Chọn gói</button>
  </article>
  <article class="card featured">
    <h3>Gói Thực hành</h3>
    <p>Có bài tập, bài giải và dự án nhỏ.</p>
    <button>Chọn gói</button>
  </article>
  <article class="card">
    <h3>Gói Dự án</h3>
    <p>Luyện layout qua các giao diện thực tế.</p>
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
}`
    };
  }

  if (focus.includes("sidebar") || focus.includes("dashboard") || focus.includes("admin")) {
    return {
      html: `<main class="app-layout">
  <aside class="sidebar">Menu quản trị</aside>
  <section class="content">
    <header class="content-header">
      <h2>Dashboard</h2>
      <button>Thêm mới</button>
    </header>
    <p>Khu vực nội dung chính tự chiếm phần còn lại.</p>
  </section>
</main>`,
      css: `.app-layout {
  display: flex;
  min-height: 280px;
}

.sidebar {
  flex: 0 0 220px;
}

.content {
  flex: 1;
  min-width: 0;
}

@media (max-width: 768px) {
  .app-layout {
    flex-direction: column;
  }
}`
    };
  }

  if (focus.includes("comment") || focus.includes("chat") || focus.includes("avatar") || focus.includes("profile")) {
    return {
      html: `<article class="comment">
  <div class="avatar">A</div>
  <div class="comment-body">
    <h3>Nguyễn Văn A</h3>
    <p>Bố cục này dùng Flexbox để avatar cố định, nội dung co giãn.</p>
  </div>
  <time>09:30</time>
</article>`,
      css: `.comment {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.avatar {
  flex: 0 0 48px;
}

.comment-body {
  flex: 1;
  min-width: 0;
}

.comment time {
  margin-left: auto;
}`
    };
  }

  if (focus.includes("center") || focus.includes("giữa")) {
    return {
      html: `<main class="page-center">
  <form class="login-box">
    <h2>Đăng nhập</h2>
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Mật khẩu">
    <button>Vào học</button>
  </form>
</main>`,
      css: `.page-center {
  min-height: 320px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  width: min(100%, 320px);
  display: flex;
  flex-direction: column;
  gap: 10px;
}`
    };
  }

  return {
    html: `<header class="site-header">
  <a class="logo" href="#">NenTang</a>
  <nav class="site-nav">
    <a href="#">Khóa học</a>
    <a href="#">Bài tập</a>
    <a href="#">Liên hệ</a>
  </nav>
  <button class="login-button">Đăng nhập</button>
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
}`
  };
}

function htmlExample(moduleIndex, lessonIndex, title) {
  return exampleBlock(moduleIndex, lessonIndex, title).html;
}

function cssExample(moduleIndex, lessonIndex, title) {
  return exampleBlock(moduleIndex, lessonIndex, title).css;
}

function previewDocument(moduleIndex, lessonIndex, title) {
  const block = exampleBlock(moduleIndex, lessonIndex, title);
  const css = block.css;
  const html = block.html;

  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 18px;
      font-family: "Segoe UI", Tahoma, sans-serif;
      color: #18212f;
      background: #f8fafc;
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
    input {
      min-height: 40px;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 8px 10px;
      font: inherit;
    }
    .site-header,
    .search-row,
    .comment,
    .card,
    .content,
    .sidebar,
    .login-box {
      border: 1px solid #d9e2ec;
      border-radius: 8px;
      background: white;
      padding: 14px;
    }
    .logo {
      color: #18212f;
      font-size: 1.05rem;
      font-weight: 900;
    }
    .featured {
      border-color: #0f766e;
      box-shadow: 0 10px 24px rgba(15, 118, 110, 0.14);
    }
    .sidebar {
      color: white;
      background: #18212f;
    }
    .content-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    .content-header h2,
    .comment h3,
    .card h3,
    .login-box h2 {
      margin: 0 0 8px;
    }
    .avatar {
      width: 48px;
      height: 48px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      color: white;
      background: #e85d4f;
      font-weight: 900;
    }
    .direction-demo article,
    .tag-board span,
    .course-list article,
    .board article,
    .debug-item,
    .hero-preview,
    .file-icon,
    .stepper span,
    .chips span,
    .faq-list article {
      border: 1px solid #d9e2ec;
      border-radius: 8px;
      background: white;
      padding: 12px;
    }
    .hero-preview,
    .file-icon,
    .stepper span {
      display: grid;
      place-items: center;
      color: white;
      background: #2563eb;
      font-weight: 900;
    }
    .file-icon,
    .stepper span {
      width: 44px;
      height: 44px;
      flex: 0 0 auto;
    }
    .tag-board span,
    .chips span {
      text-align: center;
    }
    .bottom-nav {
      border: 1px solid #d9e2ec;
      border-radius: 12px;
      background: white;
      padding: 10px;
    }
${css.split("\n").map((line) => "    " + line).join("\n")}
  </style>
</head>
<body>
${html.split("\n").map((line) => "  " + line).join("\n")}
</body>
</html>`;
}

function previewFrame(moduleIndex, lessonIndex, title, label) {
  return `<div class="result-panel">
            <div class="result-head">
              <h3>${label}</h3>
              <span>Preview chạy từ HTML/CSS bên trên</span>
            </div>
            <iframe class="result-frame" title="${esc(label)}" srcdoc="${esc(previewDocument(moduleIndex, lessonIndex, title))}"></iframe>
          </div>`;
}

function solutionCode(moduleIndex, lessonIndex, title) {
  const css = cssExample(moduleIndex, lessonIndex, title);
  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <style>
${css.split("\n").map((line) => "    " + line).join("\n")}
  </style>
</head>
<body>
${htmlExample(moduleIndex, lessonIndex, title).split("\n").map((line) => "  " + line).join("\n")}
</body>
</html>`;
}

function lessonPage(module, moduleIndex, lesson, lessonIndex) {
  const number = lessonIndex + 1;
  const title = `Bài ${pad(number)} - ${lesson} | ${module.short} CSS Flexbox | NenTang.vn`;
  const description = lessonDescription(module, lesson, number);
  const prev = number > 1 ? `../bai-${pad(number - 1)}/index.html` : "../index.html";
  const next = number < module.lessons.length ? `../bai-${pad(number + 1)}/index.html` : "../../index.html";
  const content = lessonContent(module, moduleIndex, lesson, lessonIndex);

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo(title, description, "../../shared.css")}
</head>
<body>
  ${topbar("../../")}

  <section class="module-hero ${module.className}">
    <div class="container">
      <div class="breadcrumb">
        <a href="../../index.html">CSS Flexbox</a>
        <span>/</span>
        <a href="../index.html">${module.short}</a>
        <span>/</span>
        <span>Bài ${pad(number)}</span>
      </div>
      <h1>Bài ${pad(number)}: ${lesson}</h1>
      <p>${description}</p>
    </div>
  </section>

  <main class="section">
    <div class="container lesson-layout">
      <aside class="side-nav" aria-label="Mục lục bài học">
        <a href="#goal">Mục tiêu</a>
        <a href="#theory">Lý thuyết</a>
        <a href="#demo">Minh họa</a>
        <a href="#code">Code ví dụ</a>
        <a href="#exercise">Bài tập</a>
        <a href="#solution">Bài giải</a>
      </aside>

      <article class="module-article">
        <section class="lesson" id="goal">
          <h2>Mục tiêu bài học</h2>
          <p>${content.objectives[0]}</p>
          <ul>
${renderList(content.objectives.slice(1))}
          </ul>
        </section>

        <section class="lesson" id="theory">
          <h2>Lý thuyết cho người mới</h2>
          ${content.theory.map((paragraph) => `<p>${paragraph}</p>`).join("\n          ")}
          <ol class="steps">
${renderSteps(content.steps)}
          </ol>
        </section>

        <section class="lesson" id="demo">
          <h2>Minh họa trực quan</h2>
          <p>${content.demo}</p>
          ${miniDemo(content.visualMode)}
          <div class="demo-code">
            <h3>Code tạo minh họa</h3>
            <p>Đoạn CSS này là phần quan trọng điều khiển cách các item trong khung minh họa được sắp xếp.</p>
            <pre><code data-lang="css">${esc(visualCss(content.visualMode))}</code></pre>
          </div>
        </section>

        <section class="lesson" id="code">
          <h2>Code ví dụ</h2>
          <p>${content.codeNote}</p>
          <div class="code-grid">
            <div>
              <h3>HTML</h3>
              <pre><code data-lang="html">${esc(htmlExample(moduleIndex, lessonIndex, lesson))}</code></pre>
            </div>
            <div>
              <h3>CSS</h3>
              <pre><code data-lang="css">${esc(cssExample(moduleIndex, lessonIndex, lesson))}</code></pre>
            </div>
          </div>
          ${previewFrame(moduleIndex, lessonIndex, lesson, "Kết quả khi chạy code ví dụ")}
        </section>

        <section class="exercise" id="exercise">
          <span class="level">Bài tập thực hành</span>
          <h2>Yêu cầu</h2>
          <p>${content.exercise}</p>
          <ol class="steps">
${renderSteps(content.practiceSteps)}
          </ol>
          <h3>Tiêu chí đạt</h3>
          <ul>
${renderList(content.criteria)}
          </ul>
        </section>

        <section class="lesson solution" id="solution">
          <h2>Bài giải tham khảo</h2>
          <p>${content.solutionNote}</p>
          <pre><code data-lang="html">${esc(solutionCode(moduleIndex, lessonIndex, lesson))}</code></pre>
          ${previewFrame(moduleIndex, lessonIndex, lesson, "Kết quả bài giải")}
        </section>

        <section class="callout">
          <h2>Lỗi thường gặp</h2>
          <ul>
${renderList(content.mistakes)}
          </ul>
        </section>

        <div class="pager">
          <a class="btn" href="${prev}">Bài trước</a>
          <a class="btn primary" href="${next}">Bài tiếp theo</a>
        </div>
      </article>
    </div>
  </main>

  <footer class="footer">
    <p><a href="../index.html">Quay lại ${module.short}</a></p>
  </footer>
  <script type="module" src="../../app.js"></script>
</body>
</html>
`;
}

function modulePage(module, moduleIndex) {
  const title = `${module.short}: ${module.title} | CSS Flexbox | NenTang.vn`;
  const description = `${module.title}: 20 bài học CSS Flexbox có ví dụ, bài tập, bài giải và code highlight bằng Shiki.`;
  const lessonCards = module.lessons.map((lesson, index) => {
    const number = index + 1;
    return `<a href="bai-${pad(number)}/index.html" class="exercise-card ${module.className}">
        <div class="card-num">${pad(number)}</div>
        <div class="card-info">
          <h3>${lesson}</h3>
          <p>${lessonDescription(module, lesson, number)}</p>
        </div>
      </a>`;
  }).join("\n");

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo(title, description, "../shared.css")}
</head>
<body>
  ${topbar("../")}
  <section class="module-hero ${module.className}">
    <div class="container">
      <div class="breadcrumb">
        <a href="../index.html">CSS Flexbox</a>
        <span>/</span>
        <span>${module.short}</span>
      </div>
      <h1>${module.short}: ${module.title}</h1>
      <p>${module.subtitle}</p>
    </div>
  </section>

  <main class="section">
    <div class="container">
      <div class="section-head">
        <h2>Danh sách 20 bài học</h2>
        <p>Mỗi bài có phần lý thuyết cho người mới, minh họa trực quan, code ví dụ, bài tập và bài giải tham khảo.</p>
      </div>
      <div class="exercise-grid module-list">
        ${lessonCards}
      </div>
    </div>
  </main>

  <footer class="footer">
    <p><a href="../index.html">Quay lại khóa CSS Flexbox</a></p>
  </footer>
  <script type="module" src="../app.js"></script>
</body>
</html>
`;
}

function indexPage() {
  const moduleCards = modules.map((module) => `<a class="module-link ${module.className}" href="${module.slug}/index.html">
            <header>
              <h3>${module.short}: ${module.title}</h3>
              <p>${module.subtitle}</p>
            </header>
            <div class="module-body">
              <ul>
                ${module.lessons.slice(0, 5).map((lesson) => `<li>${lesson}</li>`).join("\n                ")}
              </ul>
              <div class="tag-row">
                <span class="tag">20 bài học</span>
                <span class="tag">20 bài tập</span>
                <span class="tag">Có bài giải</span>
              </div>
            </div>
          </a>`).join("\n");

  return `<!DOCTYPE html>
<html lang="vi">
<head>
${seo("Học CSS Flexbox Toàn Tập | NenTang.vn", "Khóa học CSS Flexbox gồm 4 module, 80 bài học, ví dụ trực quan, bài tập, bài giải và code highlight bằng Shiki.", "shared.css")}
</head>
<body>
  ${topbar("")}
  <main>
    <section class="hero">
      <div class="hero-inner">
        <div>
          <p class="eyebrow">Khóa học thực hành cho người mới</p>
          <h1>Học CSS Flexbox từ nền tảng đến dự án</h1>
          <p>80 bài học theo 4 module. Mỗi bài có giải thích dễ hiểu, minh họa trực quan, code HTML/CSS, bài tập thực hành và bài giải tham khảo.</p>
          <div class="hero-actions">
            <a class="btn primary" href="#modules">Xem 4 module</a>
            <a class="btn" href="#playground">Thử Playground</a>
          </div>
        </div>
        <div class="hero-visual" aria-label="Minh họa Flexbox">
          <div class="visual-stage">
            <div class="visual-item">logo</div>
            <div class="visual-item">nav</div>
            <div class="visual-item">main</div>
            <div class="visual-item">aside</div>
            <div class="visual-item">cta</div>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="stats-grid">
          <div class="stat"><strong>4</strong><span>Module từ cơ bản đến dự án</span></div>
          <div class="stat"><strong>80</strong><span>Bài học chi tiết</span></div>
          <div class="stat"><strong>80</strong><span>Bài tập kèm bài giải</span></div>
          <div class="stat"><strong>Shiki</strong><span>Highlight HTML/CSS đầy đủ</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="modules">
      <div class="container">
        <div class="section-head">
          <h2>Lộ trình học theo module</h2>
          <p>Lộ trình được thiết kế giống cấu trúc khóa PHP trong repo: module riêng, bài học riêng, bài tập riêng và bài giải để người học có thể tự luyện.</p>
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
          <p>Thay đổi thuộc tính để thấy item dịch chuyển ngay. Code bên dưới cũng được Shiki highlight sau khi trang tải xong.</p>
        </div>
        <div class="playground" data-playground>
          <div class="playground-layout">
            <div class="controls">
              <div class="control">
                <label for="direction">flex-direction</label>
                <select id="direction" data-css-prop="flex-direction">
                  <option value="row">row</option>
                  <option value="row-reverse">row-reverse</option>
                  <option value="column">column</option>
                  <option value="column-reverse">column-reverse</option>
                </select>
              </div>
              <div class="control">
                <label for="justify">justify-content</label>
                <select id="justify" data-css-prop="justify-content">
                  <option value="flex-start">flex-start</option>
                  <option value="center">center</option>
                  <option value="flex-end">flex-end</option>
                  <option value="space-between">space-between</option>
                  <option value="space-around">space-around</option>
                  <option value="space-evenly">space-evenly</option>
                </select>
              </div>
              <div class="control">
                <label for="align">align-items</label>
                <select id="align" data-css-prop="align-items">
                  <option value="stretch">stretch</option>
                  <option value="flex-start">flex-start</option>
                  <option value="center">center</option>
                  <option value="flex-end">flex-end</option>
                  <option value="baseline">baseline</option>
                </select>
              </div>
              <div class="control">
                <label for="wrap">flex-wrap</label>
                <select id="wrap" data-css-prop="flex-wrap">
                  <option value="nowrap">nowrap</option>
                  <option value="wrap">wrap</option>
                  <option value="wrap-reverse">wrap-reverse</option>
                </select>
              </div>
              <div class="control">
                <label for="gap">gap</label>
                <input id="gap" data-css-prop="gap" type="range" min="0" max="42" value="12" />
              </div>
            </div>
            <div class="demo-shell">
              <div class="demo-box" data-demo>
                <div class="demo-item">1</div>
                <div class="demo-item">2</div>
                <div class="demo-item">3</div>
                <div class="demo-item">4</div>
              </div>
              <pre><code data-code data-lang="css"></code></pre>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <footer class="footer">
    <p>CSS Flexbox Course - NenTang.vn</p>
  </footer>
  <script type="module" src="app.js"></script>
</body>
</html>
`;
}

function sharedCss() {
  return `*,
*::before,
*::after {
  box-sizing: border-box;
}

:root {
  --ink: #18212f;
  --muted: #5e6b7a;
  --line: #d9e2ec;
  --paper: #ffffff;
  --soft: #f4f7fb;
  --teal: #0f766e;
  --teal-dark: #115e59;
  --coral: #e85d4f;
  --amber: #d97706;
  --blue: #2563eb;
  --shadow: 0 14px 34px rgba(24, 33, 47, 0.1);
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
pre,
kbd {
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
  background: rgba(255, 255, 255, 0.92);
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
  border-radius: 8px;
  display: grid;
  place-items: center;
  color: white;
  background: var(--teal);
  font-weight: 900;
}

.nav-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: flex-end;
}

.nav-links a,
.btn {
  min-height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 12px;
  background: white;
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
}

.btn.primary {
  border-color: var(--teal);
  background: var(--teal);
  color: white;
}

.hero {
  background: linear-gradient(135deg, rgba(15, 118, 110, 0.96), rgba(24, 33, 47, 0.94));
  color: white;
}

.hero-inner {
  max-width: 1160px;
  margin: 0 auto;
  padding: 58px 22px 44px;
  display: grid;
  grid-template-columns: minmax(0, 1.04fr) minmax(330px, 0.96fr);
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

.hero h1 {
  margin: 0;
  max-width: 760px;
  font-size: clamp(2.15rem, 4.6vw, 4.2rem);
  line-height: 1.04;
  letter-spacing: 0;
}

.hero p,
.module-hero p {
  max-width: 760px;
  color: rgba(255, 255, 255, 0.88);
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 26px;
}

.hero .btn {
  border-color: rgba(255, 255, 255, 0.38);
  background: rgba(255, 255, 255, 0.12);
  color: white;
}

.hero .btn.primary {
  border-color: white;
  background: white;
  color: var(--teal-dark);
}

.hero-visual {
  min-height: 310px;
  padding: 18px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
}

.visual-stage {
  min-height: 274px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  gap: 12px;
  padding: 16px;
  border: 2px dashed rgba(255, 255, 255, 0.42);
  border-radius: 8px;
}

.visual-item,
.demo-item,
.mini-item {
  display: grid;
  place-items: center;
  border-radius: 8px;
  font-weight: 900;
}

.visual-item {
  min-width: 88px;
  min-height: 62px;
  background: #fef3c7;
  color: #78350f;
}

.visual-item:nth-child(2),
.visual-item:nth-child(5) {
  min-height: 94px;
  background: #bbf7d0;
  color: #14532d;
}

.visual-item:nth-child(3) {
  min-height: 74px;
  background: #fecaca;
  color: #7f1d1d;
}

.visual-item:nth-child(4) {
  min-height: 120px;
  background: #bfdbfe;
  color: #1e3a8a;
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
  font-size: clamp(1.55rem, 2.8vw, 2.25rem);
  line-height: 1.15;
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
.code-grid {
  display: grid;
  gap: 18px;
}

.stats-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.stat,
.module-link,
.lesson,
.exercise,
.callout,
.playground {
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
  font-size: 1.8rem;
  line-height: 1;
}

.stat span {
  display: block;
  margin-top: 6px;
  color: var(--muted);
  font-size: 0.9rem;
}

.module-grid,
.exercise-grid,
.code-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.module-list {
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
}

.module-link,
.exercise-card {
  overflow: hidden;
  text-decoration: none;
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.module-link:hover,
.exercise-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 38px rgba(24, 33, 47, 0.16);
}

.module-link header {
  padding: 22px;
  color: white;
}

.m1 header,
.module-hero.m1,
.module-hero:not(.m2):not(.m3):not(.m4) {
  background: #0f766e;
}

.m2 header,
.module-hero.m2 {
  background: #e85d4f;
}

.m3 header,
.module-hero.m3 {
  background: #2563eb;
}

.m4 header,
.module-hero.m4 {
  background: #d97706;
}

.module-link h3 {
  margin: 0;
  font-size: 1.28rem;
}

.module-link header p {
  margin: 5px 0 0;
  color: rgba(255, 255, 255, 0.86);
}

.module-body {
  padding: 18px 22px 22px;
}

.module-body ul,
.exercise ul,
.lesson ul,
.steps {
  margin: 12px 0 0;
  padding-left: 20px;
}

.module-body li,
.exercise li,
.lesson li,
.steps li {
  margin: 6px 0;
  color: var(--muted);
}

.tag-row {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 16px;
}

.tag {
  display: inline-flex;
  align-items: center;
  min-height: 28px;
  padding: 4px 10px;
  border-radius: 999px;
  background: #edf7f6;
  color: var(--teal-dark);
  font-size: 0.82rem;
  font-weight: 800;
}

.playground,
.lesson,
.exercise,
.callout {
  padding: 22px;
}

.playground-layout,
.lesson-layout {
  display: grid;
  grid-template-columns: minmax(240px, 0.34fr) minmax(0, 1fr);
  gap: 22px;
  align-items: start;
}

.controls {
  display: grid;
  gap: 14px;
}

.control label {
  display: block;
  margin-bottom: 6px;
  color: var(--ink);
  font-weight: 800;
  font-size: 0.9rem;
}

.control select,
.control input {
  width: 100%;
  min-height: 40px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 10px;
  background: white;
  color: var(--ink);
  font: inherit;
}

.demo-shell {
  display: grid;
  gap: 14px;
}

.demo-box {
  min-height: 310px;
  display: flex;
  gap: 12px;
  padding: 14px;
  border: 3px dashed #94a3b8;
  border-radius: 8px;
  background:
    linear-gradient(90deg, rgba(148, 163, 184, 0.18) 1px, transparent 1px),
    linear-gradient(rgba(148, 163, 184, 0.18) 1px, transparent 1px);
  background-size: 24px 24px;
}

.demo-item {
  width: 82px;
  min-height: 58px;
  border: 2px solid var(--teal);
  background: white;
  color: var(--teal-dark);
}

.module-hero .container {
  padding: 42px 22px;
}

.breadcrumb {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 12px;
  color: rgba(255, 255, 255, 0.82);
  font-size: 0.92rem;
}

.breadcrumb a {
  color: white;
  font-weight: 800;
  text-decoration: none;
}

.module-hero h1 {
  max-width: 890px;
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.35rem);
  line-height: 1.08;
  letter-spacing: 0;
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
  color: var(--teal-dark);
}

.module-article {
  display: grid;
  gap: 20px;
}

.lesson h3,
.exercise h3,
.callout h3 {
  margin: 18px 0 8px;
  font-size: 1.08rem;
}

.mini-demo {
  position: relative;
  min-height: 180px;
  display: flex;
  gap: 10px;
  padding: 18px;
  margin-top: 16px;
  border: 2px dashed #94a3b8;
  border-radius: 8px;
  background: #f8fafc;
}

.mini-demo.center {
  justify-content: center;
  align-items: center;
}

.mini-demo.space {
  justify-content: space-between;
  align-items: center;
}

.mini-demo.wrap {
  flex-wrap: wrap;
  align-content: flex-start;
}

.mini-demo.column {
  flex-direction: column;
  justify-content: center;
}

.mini-demo.grow .mini-item:nth-child(2) {
  flex: 1;
}

.mini-demo.order .mini-item:nth-child(1) {
  order: 3;
}

.mini-demo.order .mini-item:nth-child(3) {
  order: 1;
}

.mini-demo.basis .mini-item {
  flex: 1 1 120px;
}

.mini-demo.shrink .mini-item {
  flex: 0 1 160px;
  min-width: 0;
}

.mini-demo.auto .mini-item:nth-child(4) {
  margin-left: auto;
}

.mini-demo.nested .mini-item:nth-child(2) {
  display: flex;
  align-items: center;
  justify-content: center;
}

.mini-item {
  min-width: 58px;
  min-height: 46px;
  background: #ccfbf1;
  border: 2px solid var(--teal);
  color: var(--teal-dark);
}

.mini-item:nth-child(2) {
  background: #fee2e2;
  border-color: var(--coral);
  color: #991b1b;
}

.mini-item:nth-child(3) {
  background: #fef3c7;
  border-color: var(--amber);
  color: #92400e;
}

.mini-item:nth-child(4) {
  background: #dbeafe;
  border-color: var(--blue);
  color: #1e40af;
}

.axis-label {
  position: absolute;
  padding: 2px 8px;
  border-radius: 999px;
  background: #18212f;
  color: white;
  font-size: 0.75rem;
  font-weight: 800;
}

.main-axis {
  right: 12px;
  bottom: 12px;
}

.cross-axis {
  left: 12px;
  top: 12px;
}

.exercise-card {
  display: flex;
  gap: 14px;
  padding: 18px;
  border: 1px solid var(--line);
  border-left: 5px solid var(--teal);
  border-radius: 8px;
  background: white;
  color: inherit;
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
  color: var(--teal-dark);
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

.demo-code,
.result-panel {
  margin-top: 18px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #f8fafc;
  padding: 16px;
}

.demo-code h3,
.result-head h3 {
  margin: 0 0 6px;
}

.demo-code p,
.result-head span {
  color: var(--muted);
  font-size: 0.9rem;
}

.result-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

.result-frame {
  width: 100%;
  min-height: 340px;
  display: block;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  background: white;
}

.steps {
  counter-reset: step;
  list-style: none;
  padding-left: 0;
}

.steps li {
  position: relative;
  margin: 10px 0;
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
  display: flex;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.footer {
  padding: 28px 22px;
  background: #18212f;
  color: rgba(255, 255, 255, 0.78);
  text-align: center;
}

@media (max-width: 900px) {
  .hero-inner,
  .playground-layout,
  .lesson-layout,
  .stats-grid,
  .module-grid,
  .exercise-grid,
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

  .hero-inner {
    padding-top: 38px;
  }

  .visual-item {
    min-width: 74px;
  }

  .demo-item {
    width: 66px;
  }
}
`;
}

function appJs() {
  return `const playground = document.querySelector("[data-playground]");

async function highlightCode() {
  const blocks = Array.from(document.querySelectorAll("pre code[data-lang]"));
  if (!blocks.length) return;

  try {
    const { codeToHtml } = await import("https://esm.sh/shiki@1");
    await Promise.all(blocks.map(async (block) => {
      const lang = block.dataset.lang || "text";
      const raw = block.dataset.raw || block.textContent;
      if (block.dataset.highlighted === raw) return;

      const html = await codeToHtml(raw, { lang, theme: "github-dark" });
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

document.querySelectorAll("[data-progress]").forEach((box) => {
  const key = "flexbox-course:" + box.dataset.progress;
  const inputs = Array.from(box.querySelectorAll("input[type='checkbox']"));
  const saved = JSON.parse(localStorage.getItem(key) || "[]");

  inputs.forEach((input, index) => {
    input.checked = saved.includes(index);
    input.addEventListener("change", () => {
      const checked = inputs
        .map((item, itemIndex) => (item.checked ? itemIndex : null))
        .filter((itemIndex) => itemIndex !== null);
      localStorage.setItem(key, JSON.stringify(checked));
    });
  });
});

highlightCode();
`;
}

write(path.join(root, "shared.css"), sharedCss());
write(path.join(root, "app.js"), appJs());
write(path.join(root, "index.html"), indexPage());

modules.forEach((module, moduleIndex) => {
  write(path.join(root, module.slug, "index.html"), modulePage(module, moduleIndex));
  module.lessons.forEach((lesson, lessonIndex) => {
    write(
      path.join(root, module.slug, `bai-${pad(lessonIndex + 1)}`, "index.html"),
      lessonPage(module, moduleIndex, lesson, lessonIndex)
    );
  });
});

console.log(`Generated ${modules.length} modules and ${modules.length * 20} lesson pages.`);
