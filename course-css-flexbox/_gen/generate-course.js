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
  const mode = ["center", "space", "wrap", "column", "grow", "order"][seed % 6];
  return `<div class="mini-demo ${mode}">
    <div class="mini-item">1</div>
    <div class="mini-item">2</div>
    <div class="mini-item">3</div>
    <div class="mini-item">4</div>
    <div class="axis-label main-axis">main axis</div>
    <div class="axis-label cross-axis">cross axis</div>
  </div>`;
}

function htmlExample(moduleIndex, lessonIndex, title) {
  const variants = [
`<header class="site-header">
  <a class="logo" href="#">NenTang</a>
  <nav class="site-nav">
    <a href="#">Khóa học</a>
    <a href="#">Bài tập</a>
    <a href="#">Liên hệ</a>
  </nav>
  <button class="login-button">Đăng nhập</button>
</header>`,
`<section class="cards">
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
</section>`,
`<main class="app-layout">
  <aside class="sidebar">Menu quản trị</aside>
  <section class="content">
    <header class="content-header">
      <h2>Dashboard</h2>
      <button>Thêm mới</button>
    </header>
  </section>
</main>`,
`<article class="comment">
  <img class="avatar" src="avatar.png" alt="Avatar">
  <div class="comment-body">
    <h3>Nguyễn Văn A</h3>
    <p>Bố cục này dùng Flexbox để avatar cố định, nội dung co giãn.</p>
  </div>
  <time>09:30</time>
</article>`
  ];
  return variants[(moduleIndex + lessonIndex) % variants.length];
}

function cssExample(moduleIndex, lessonIndex, title) {
  const focus = title.toLowerCase();
  if (focus.includes("grow") || focus.includes("search") || focus.includes("co giãn")) {
    return `.search-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-row input {
  flex: 1;
  min-width: 0;
}

.search-row button {
  flex: 0 0 auto;
}`;
  }
  if (focus.includes("wrap") || focus.includes("gallery") || focus.includes("product") || focus.includes("card")) {
    return `.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
}

.card {
  flex: 1 1 240px;
  display: flex;
  flex-direction: column;
  min-height: 220px;
}

.card button {
  margin-top: auto;
}`;
  }
  if (focus.includes("sidebar") || focus.includes("dashboard") || focus.includes("admin")) {
    return `.app-layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  flex: 0 0 240px;
}

.content {
  flex: 1;
  min-width: 0;
}

@media (max-width: 768px) {
  .app-layout {
    flex-direction: column;
  }
}`;
  }
  if (focus.includes("center") || focus.includes("giữa")) {
    return `.page-center {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}`;
  }
  return `.site-header {
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
}`;
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
          <p>Sau bài này, bạn sẽ biết cách dùng chủ đề <strong>${lesson}</strong> trong một layout thật, hiểu thuộc tính nào đặt ở container, thuộc tính nào đặt ở item và biết tự kiểm tra lỗi thường gặp.</p>
          <ul>
            <li>Nhận diện đúng flex container và flex item trong HTML.</li>
            <li>Viết được CSS tối thiểu để tạo bố cục mong muốn.</li>
            <li>Biết thử nghiệm bằng DevTools hoặc playground trước khi sửa code lớn.</li>
          </ul>
        </section>

        <section class="lesson" id="theory">
          <h2>Lý thuyết cho người mới</h2>
          <p>Flexbox hoạt động theo quan hệ cha con trực tiếp. Phần tử cha giữ vai trò điều phối hướng, căn chỉnh và khoảng cách; phần tử con nhận kích thước, thứ tự hoặc mức co giãn. Khi học ${lesson.toLowerCase()}, hãy luôn hỏi: thuộc tính này đặt ở container hay item?</p>
          <ol class="steps">
            <li>Tạo HTML rõ ràng trước, chưa vội viết nhiều CSS.</li>
            <li>Đặt <code>display: flex</code> cho phần tử cha cần sắp xếp con trực tiếp.</li>
            <li>Chọn hướng bằng <code>flex-direction</code> nếu layout không phải hàng ngang mặc định.</li>
            <li>Căn theo main axis bằng <code>justify-content</code>, căn theo cross axis bằng <code>align-items</code>.</li>
            <li>Kiểm soát item bằng <code>flex</code>, <code>order</code>, <code>align-self</code> khi cần.</li>
          </ol>
        </section>

        <section class="lesson" id="demo">
          <h2>Minh họa trực quan</h2>
          <p>Khung nét đứt là flex container. Các ô màu là flex item. Thay đổi thuộc tính trong code ví dụ bên dưới sẽ làm item đổi vị trí, khoảng cách hoặc kích thước.</p>
          ${miniDemo(moduleIndex + lessonIndex)}
        </section>

        <section class="lesson" id="code">
          <h2>Code ví dụ</h2>
          <p>Ví dụ tách HTML và CSS để dễ nhìn. Khi luyện tập, hãy tự gõ lại từng dòng để nhớ vai trò của từng thuộc tính.</p>
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
        </section>

        <section class="exercise" id="exercise">
          <span class="level">Bài tập thực hành</span>
          <h2>Yêu cầu</h2>
          <p>Dựng lại ví dụ <strong>${lesson}</strong> trong một thư mục riêng. Bài làm cần chạy được khi mở file HTML trực tiếp trên trình duyệt.</p>
          <ol class="steps">
            <li>Tạo thư mục <code>bai-${pad(number)}-${module.slug}</code>.</li>
            <li>Tạo 2 file <code>index.html</code> và <code>style.css</code>.</li>
            <li>Viết HTML theo đúng cấu trúc cha con trong phần ví dụ.</li>
            <li>Viết CSS Flexbox, kiểm tra desktop trước.</li>
            <li>Thu nhỏ màn hình còn khoảng 360px và sửa lỗi tràn ngang nếu có.</li>
          </ol>
          <h3>Tiêu chí đạt</h3>
          <ul>
            <li>Không dùng table hoặc float để tạo layout chính.</li>
            <li>Khoảng cách giữa item dùng <code>gap</code> khi phù hợp.</li>
            <li>Không có chữ hoặc nút bị chồng lên nhau trên mobile.</li>
          </ul>
        </section>

        <section class="lesson solution" id="solution">
          <h2>Bài giải tham khảo</h2>
          <p>Đây là một lời giải gọn để đối chiếu sau khi bạn đã tự làm. Có thể có nhiều cách đúng; quan trọng là bạn giải thích được vì sao đặt từng thuộc tính ở vị trí đó.</p>
          <pre><code data-lang="html">${esc(solutionCode(moduleIndex, lessonIndex, lesson))}</code></pre>
        </section>

        <section class="callout">
          <h2>Lỗi thường gặp</h2>
          <ul>
            <li>Đặt thuộc tính container như <code>justify-content</code> vào item nên không có tác dụng.</li>
            <li>Quên <code>min-width: 0</code> với item chứa text dài, làm layout bị tràn.</li>
            <li>Dùng margin rời rạc quá nhiều thay vì <code>gap</code>, khiến khoảng cách khó kiểm soát.</li>
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
