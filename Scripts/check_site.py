"""Check the small static site without installing dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "index.html", ROOT / "support/index.html", ROOT / "privacy/index.html")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = 0
        self.has_language = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            assert values["id"] not in self.ids, f"Duplicate id: {values['id']}"
            self.ids.add(values["id"])
        if tag == "html":
            self.has_language = values.get("lang") == "en"
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "h1":
            self.headings += 1
        for attr in ("href", "src"):
            if values.get(attr):
                self.links.append(values[attr])


parsed = {}
for path in PAGES:
    page = Page()
    page.feed(path.read_text())
    assert page.has_language and page.has_viewport and page.headings == 1, path
    assert "main" in page.ids, path
    parsed[path] = page

for path, page in parsed.items():
    for link in page.links:
        target = urlsplit(link)
        if target.scheme or target.netloc:
            continue
        assert not target.path.startswith("/"), f"Base-path-unsafe link in {path}: {link}"
        local = (path.parent / unquote(target.path)).resolve()
        if local.is_dir():
            local = local / "index.html"
        assert local.is_relative_to(ROOT), f"Link escapes site: {link}"
        assert local.exists(), f"Missing target in {path}: {link}"
        if target.fragment and local in parsed:
            assert unquote(target.fragment) in parsed[local].ids, f"Missing anchor in {path}: {link}"

all_html = "\n".join(path.read_text() for path in PAGES)
assert "yellowdevjay@gmail.com" in all_html
assert "jeric614@yahoo.com" not in all_html
assert "<script" not in all_html
assert "Download on the App Store" not in all_html
print("Three static pages: headings, language, viewport, relative links, assets, anchors, and contact checks passed.")
