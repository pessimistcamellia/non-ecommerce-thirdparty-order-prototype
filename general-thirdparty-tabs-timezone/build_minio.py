"""由 GitHub Pages 版评审包派生内网 MinIO 版。

差异只有两处：原型链接指向 MinIO 对象、恢复 review-package/template.html 的
window.__SAVE__ 注入位（由 publish_minio.py 写入真实预签名 PUT URL）。
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
GITHUB_PROTOTYPE = "https://pessimistcamellia.github.io/non-ecommerce-thirdparty-order-prototype/general-thirdparty-tabs-timezone/prototype.html"
MINIO_PROTOTYPE = "https://minio.yc345.tv/onionext/review-pkg-demos/general-thirdparty-tabs-timezone-prototype-20260828-v3.html"
SAVE_LINE = 'window.__SAVE__={url:"__SAVE_URL__",exp:0/*__SAVE_EXP__*/};\n'
ANCHOR = "(function(){\nvar FILE=location.pathname.split('/').pop()||'pkg';"

html = (ROOT / "review-package.html").read_text(encoding="utf-8")
assert GITHUB_PROTOTYPE in html
html = html.replace(GITHUB_PROTOTYPE, MINIO_PROTOTYPE).replace("外网原型", "内网原型")

assert "window.__SAVE__={" not in html
assert html.count(ANCHOR) == 1
html = html.replace(ANCHOR, SAVE_LINE + ANCHOR)

out = ROOT / "review-package.minio.html"
out.write_text(html, encoding="utf-8")
print("written", out, len(html))
