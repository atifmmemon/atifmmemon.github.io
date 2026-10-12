#!/usr/bin/env python3
"""
Mirror every UMD paper PDF and abstract referenced in publications.html
into local ./papers/, then rewrite the links to local paths.

Idempotent: skips files that are already present with non-zero size.
"""
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
PUBS_HTML = ROOT / "publications.html"
PAPERS_DIR = ROOT / "papers"
UMD_PREFIX = "https://www.cs.umd.edu/~atif/papers/"

UA = "Mozilla/5.0 (compatible; atifmmemon.github.io mirror)"


def fetch(url: str, dest: Path) -> bool:
    """Return True on success (or already-present), False on failure."""
    if dest.exists() and dest.stat().st_size > 0:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = Request(url, headers={"User-Agent": UA})
    try:
        with urlopen(req, timeout=30) as r:
            data = r.read()
        if not data:
            print(f"  empty: {url}")
            return False
        dest.write_bytes(data)
        return True
    except Exception as e:
        print(f"  FAIL {url}: {e}")
        return False


def main() -> int:
    html = PUBS_HTML.read_text(encoding="utf-8")

    urls = sorted(set(re.findall(
        r'https://www\.cs\.umd\.edu/~atif/papers/[^"\s]+',
        html,
    )))

    print(f"Found {len(urls)} UMD URLs in publications.html")
    PAPERS_DIR.mkdir(exist_ok=True)

    ok = fail = 0
    for i, url in enumerate(urls, 1):
        name = os.path.basename(urlparse(url).path)
        dest = PAPERS_DIR / name
        print(f"[{i}/{len(urls)}] {name}")
        if fetch(url, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.1)

    print(f"\nDone: {ok} ok, {fail} failed")

    # Rewrite abstract back-links (`href="./"` → repo-local publications.html).
    fixed = 0
    for html_path in PAPERS_DIR.glob("*-abstract.html"):
        try:
            text = html_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        new_text = text.replace(
            'href="./">Atif Memon',
            'href="../publications.html">Atif Memon',
        )
        if new_text != text:
            html_path.write_text(new_text, encoding="utf-8")
            fixed += 1
    if fixed:
        print(f"Fixed back-links in {fixed} abstract pages")

    # Rewrite publications.html: swap UMD prefix with local relative path.
    new_html = html.replace(UMD_PREFIX, "papers/")
    if new_html != html:
        PUBS_HTML.write_text(new_html, encoding="utf-8")
        print("Rewrote publications.html to use local papers/ paths")

    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
