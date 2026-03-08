"""
patch_m1_shiki.py
Adds Shiki syntax highlighting to module-01 bai-01 through bai-12.
Replaces the plain <pre style="background:#1a202c..."> block with the
hidden-pre + shiki div pattern, then appends the Shiki <script> tag.
"""

import re
import pathlib

BASE = pathlib.Path(r"f:\dao-tao\web\learning.nentang.vn-frontend-basic\course-html-css-js\curriculum\module-01-html-co-ban")

# Matches the old-style dark pre block
PRE_PAT = re.compile(
    r'<pre style="background:#1a202c[^"]*">(.*?)</pre>',
    re.DOTALL
)

# Matches any h3 inside ex-work (to normalize wording)
H3_PAT = re.compile(r'<h3>[^<]*(?:Code mẫu|code mẫu)[^<]*</h3>')

SHIKI_SCRIPT = """\
  <script type="module">
    import { codeToHtml } from 'https://esm.sh/shiki@1';
    const raw = document.getElementById('code-raw').textContent;
    const highlighted = await codeToHtml(raw, { lang: 'html', theme: 'github-dark' });
    document.getElementById('code-highlight').innerHTML = highlighted;
    const pre = document.getElementById('code-highlight').querySelector('pre');
    if (pre) pre.style.cssText = 'border-radius:10px;padding:20px;font-size:0.87rem;overflow-x:auto;margin:0;line-height:1.7';
  </script>
</body>"""

patched = 0
skipped = 0

for n in range(1, 13):
    f = BASE / f"bai-{n:02d}" / "index.html"
    if not f.exists():
        print(f"  MISSING: {f}")
        continue

    src = f.read_text(encoding="utf-8")

    # Skip if already has Shiki script
    if "esm.sh/shiki" in src:
        print(f"  SKIP bai-{n:02d} (already has Shiki)")
        skipped += 1
        continue

    m = PRE_PAT.search(src)
    if not m:
        print(f"  WARN  bai-{n:02d}: no plain-pre found")
        continue

    code_content = m.group(1)  # already HTML-escaped content

    # Build replacement: hidden pre + highlight div
    new_block = (
        '<div id="code-highlight">\n'
        '          <pre id="code-raw" style="display:none">'
        + code_content +
        '</pre>\n'
        '        </div>'
    )

    src = PRE_PAT.sub(new_block, src, count=1)

    # Normalize h3 heading to "💻 Code mẫu"
    src = H3_PAT.sub('<h3>💻 Code mẫu</h3>', src)

    # Add Shiki script before </body>
    src = src.replace('</body>', SHIKI_SCRIPT)

    f.write_text(src, encoding="utf-8")
    print(f"  PATCHED bai-{n:02d}")
    patched += 1

print(f"\nDone: {patched} patched, {skipped} skipped.")
