#!/usr/bin/env python3
"""
Wrap every papers/*-abstract.html in the site shell (sidebar + top nav)
so abstract pages look like the rest of the site.

Idempotent: pages already wrapped (detected by presence of
`class="sidebar"`) are skipped.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"

SHELL_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Atif Memon</title>
  <link rel="stylesheet" href="../assets/styles.css" />
</head>
<body>
  <aside class="sidebar">
    <img src="../assets/photo.jpg" alt="Atif Memon" class="avatar" />
    <h1>Atif Memon</h1>
    <p class="affiliation">Distinguished Engineer, Apple</p>
    <ul class="links">
      <li><a href="https://www.linkedin.com/in/memonatif/" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://scholar.google.com/citations?user=jJPSj0IAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
    </ul>
  </aside>

  <nav class="topnav">
    <a href="../index.html">About</a>
    <a href="../publications.html" class="active">Publications</a>
    <a href="../service.html">Service</a>
    <a href="../talks.html">Talks</a>
    <a href="../awards.html">Awards</a>
    <a href="../writing.html">Writing</a>
  </nav>

  <main class="abstract">
{body}
  </main>
</body>
</html>
"""

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
BODY_RE = re.compile(r"<body[^>]*>(.*?)</body>", re.IGNORECASE | re.DOTALL)


def wrap(path: Path) -> bool:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")

    if 'class="sidebar"' in text:
        return False  # already wrapped

    title_m = TITLE_RE.search(text)
    body_m = BODY_RE.search(text)
    if not body_m:
        print(f"  skip (no <body>): {path.name}")
        return False

    title = (title_m.group(1).strip() if title_m else path.stem).replace("\n", " ")
    body = body_m.group(1).strip()
    body = "\n".join("    " + line for line in body.splitlines())

    out = SHELL_TEMPLATE.format(title=title, body=body)
    path.write_text(out, encoding="utf-8")
    return True


def main() -> int:
    wrapped = skipped = 0
    for path in sorted(PAPERS_DIR.glob("*-abstract.html")):
        if wrap(path):
            wrapped += 1
        else:
            skipped += 1
    print(f"Wrapped {wrapped}, skipped {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
