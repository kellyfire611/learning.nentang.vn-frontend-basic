const playground = document.querySelector("[data-playground]");

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

    code.textContent = `.container {
  display: flex;
  flex-direction: ${css["flex-direction"]};
  justify-content: ${css["justify-content"]};
  align-items: ${css["align-items"]};
  flex-wrap: ${css["flex-wrap"]};
  gap: ${css.gap}px;
}`;
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
