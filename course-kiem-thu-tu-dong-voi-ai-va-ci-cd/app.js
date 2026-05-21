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

highlightCode();
