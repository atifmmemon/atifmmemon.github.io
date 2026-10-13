#!/usr/bin/env python3
"""
Parse the CV plaintext (papers/cv.pdf -> pdftotext) and emit three
HTML pages: service.html, talks.html, awards.html.

Design:
  - Each entry rendered in the same pub-list style used on publications.
  - Fields extracted: name/title, role/type, year(s), org/location.
  - Entries grouped by subsection within each page.
"""
from __future__ import annotations
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CV_PDF = ROOT / "papers" / "cv.pdf"
CV_TXT = Path("/tmp/cv_parsed.txt")

SIDEBAR = """  <aside class="sidebar">
    <img src="assets/photo.jpg" alt="Atif Memon" class="avatar" />
    <h1>Atif Memon</h1>
    <p class="affiliation">Apple</p>
    <ul class="links">
      <li><a href="https://www.linkedin.com/in/memonatif/" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://scholar.google.com/citations?user=jJPSj0IAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
    </ul>
  </aside>"""


def topnav(active: str) -> str:
    items = [
        ("index.html", "About"),
        ("publications.html", "Publications"),
        ("service.html", "Service"),
        ("talks.html", "Talks"),
        ("awards.html", "Awards"),
    ]
    links = []
    for href, label in items:
        cls = ' class="active"' if href.replace(".html", "") == active else ""
        links.append(f'    <a href="{href}"{cls}>{label}</a>')
    return "  <nav class=\"topnav\">\n" + "\n".join(links) + "\n  </nav>"


def page_shell(title: str, active: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Atif Memon</title>
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body>
{SIDEBAR}

{topnav(active)}

  <main>
{body}
  </main>
</body>
</html>
"""


def extract_cv_text():
    subprocess.run(
        ["pdftotext", "-layout", str(CV_PDF), str(CV_TXT)],
        check=True,
    )


# A CV bullet is a line that starts with optional whitespace, "•", then text,
# optionally continuing on subsequent lines that start with whitespace but no "•".
BULLET_RE = re.compile(r"^\s*•\s*(.+?)$")


def read_bullets(section_start: int, section_end: int) -> list[str]:
    """Return cleaned bullet text (one string per bullet) between the given
    1-indexed line numbers (inclusive)."""
    lines = CV_TXT.read_text(encoding="utf-8").splitlines()
    bullets: list[str] = []
    current: list[str] | None = None
    for i, raw in enumerate(lines[section_start - 1 : section_end], start=section_start):
        if "November 8, 2018" in raw:  # page footer
            continue
        if raw.strip().startswith("Atif M. Memon"):
            continue
        m = BULLET_RE.match(raw)
        if m:
            if current:
                bullets.append(" ".join(current))
            current = [m.group(1).strip()]
        elif current is not None and raw.strip() and not raw.lstrip().startswith((
            "i.", "ii.", "iii.", "iv.", "v.", "vi.", "vii.", "viii.", "ix.", "x.",
            "A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "V.",
        )):
            current.append(raw.strip())
        elif current and (not raw.strip() or raw.lstrip()[:3] in ("i. ", "ii.", "A. ")):
            bullets.append(" ".join(current))
            current = None
    if current:
        bullets.append(" ".join(current))
    # Clean: collapse whitespace, remove weird hyphens
    cleaned = []
    for b in bullets:
        b = re.sub(r"-\s+", "", b)  # un-hyphenate line breaks
        b = re.sub(r"\s+", " ", b).strip().rstrip(".")
        if b:
            cleaned.append(b)
    return cleaned


YEAR_RE = re.compile(r"(?:19|20)\d{2}")


def extract_year(text: str) -> str:
    years = YEAR_RE.findall(text)
    if not years:
        return "&mdash;"
    if len(years) >= 2 and years[0] != years[-1]:
        # year range like 2000-2001
        return f"{years[0]}&ndash;{years[-1]}"
    return years[-1]


def pub_item(name: str, role: str, meta: str) -> str:
    return (
        "      <li>\n"
        f'        <span class="pub-title">{name}</span>\n'
        f'        <span class="pub-authors">{role}</span>\n'
        f'        <span class="pub-venue">{meta}</span>\n'
        "      </li>"
    )


ROLE_PATTERNS = [
    # (regex, role label)
    (re.compile(r"\bGeneral Chair\b", re.I), "General Chair"),
    (re.compile(r"\bProgram Committee Chair\b|\bPC Chair\b|\bTechnical Program Committee Chair\b", re.I), "PC Chair"),
    (re.compile(r"\bAwards? Chair\b", re.I), "Awards Chair"),
    (re.compile(r"\bProceedings Chair\b", re.I), "Proceedings Chair"),
    (re.compile(r"\bPublications? Chair\b", re.I), "Publications Chair"),
    (re.compile(r"\bWorkshops? Co-?Chair\b", re.I), "Workshops Chair"),
    (re.compile(r"\bPhD Symposium Chair\b", re.I), "PhD Symposium Chair"),
    (re.compile(r"\bSession Chair\b", re.I), "Session Chair"),
    (re.compile(r"\bSteering Committee\b", re.I), "Steering Committee"),
    (re.compile(r"\bOrganizing Committee\b", re.I), "Organizing Committee"),
    (re.compile(r"\bMentoring Committee\b", re.I), "Mentoring Committee"),
    (re.compile(r"\bPanel Member\b|\bPanelist\b", re.I), "Panel Member"),
    (re.compile(r"\bAssociate Editor\b", re.I), "Associate Editor"),
    (re.compile(r"\bGuest (Associate )?Editor\b", re.I), "Guest Editor"),
    (re.compile(r"\bEditor\b", re.I), "Editor"),
    (re.compile(r"\bProgram Committee\b|\bPC\b", re.I), "Program Committee"),
    (re.compile(r"\bReader\b", re.I), "Thesis Reader"),
    (re.compile(r"\bNational Academy of Sciences panelist\b", re.I), "NAS Panelist"),
    (re.compile(r"\bNSF.*review panel\b|\bNSF proposals\b", re.I), "NSF Review Panel"),
]


def classify(text: str) -> tuple[str, str]:
    """Return (role, cleaned_name) for a service bullet."""
    for pat, role in ROLE_PATTERNS:
        if pat.search(text):
            return role, text
    return "Service", text


def build_service():
    # Section line ranges derived from grep earlier
    editorial = read_bullets(1515, 1545)   # IV.A.i Editorial Boards (approx)
    other_committees = read_bullets(1640, 2115)  # IV.A.vii

    editorial_entries = [
        {
            "name": "ACM Computing Surveys",
            "role": "Editorial Board Member",
            "years": "2016&ndash;Present",
            "org": "ACM &middot; <em>Source: LinkedIn</em>",
        },
        {
            "name": "Advances in Computers",
            "role": "Series Editor",
            "years": "&mdash;",
            "org": "Elsevier",
        },
        {
            "name": "Empirical Software Engineering Journal",
            "role": "Editorial Board Member",
            "years": "&mdash;",
            "org": "Springer",
        },
        {
            "name": "Software Testing, Verification and Reliability (STVR)",
            "role": "Editorial Board Member",
            "years": "&mdash;",
            "org": "Wiley",
        },
        {
            "name": "The Open Software Engineering Journal",
            "role": "Editorial Board Member",
            "years": "&mdash;",
            "org": "Bentham Science",
        },
        {
            "name": "Canadian Journal of Pure and Applied Sciences",
            "role": "Editorial Board Member",
            "years": "&mdash;",
            "org": "SENRA Academic Publishers",
        },
    ]

    # LinkedIn-sourced newer entries not in the 2018 CV
    linkedin_newer = [
        ("IEEE Computer Society — Technical Council on Software Engineering (TCSE)",
         "Executive Committee (Elected)", "2022&ndash;2025", "IEEE Computer Society"),
        ("ACM Joint European Software Engineering Conference (ESEC/FSE)",
         "Program Committee", "2022&ndash;Present", "ACM"),
        ("International Conference on Software Engineering (ICSE 2024) — SEIP Track",
         "Program Committee", "2024", "ACM/IEEE"),
        ("ACM International Conference on the Foundations of Software Engineering (FSE) — Industry Papers Track",
         "Program Committee", "2023&ndash;Present", "ACM"),
    ]

    # Classify committee entries and split chairs from PC
    chairs: list[dict] = []
    pcs: list[dict] = []
    for b in other_committees:
        role, name = classify(b)
        year = extract_year(b)
        chair_like = any(k in role for k in ["Chair", "Steering", "Organizing", "Mentoring", "Panel"])
        entry = {"name": name, "role": role, "years": year, "org": ""}
        if chair_like:
            chairs.append(entry)
        else:
            pcs.append(entry)

    def rows(entries: list[dict]) -> str:
        out = []
        for e in entries:
            parts = []
            if e.get("years") and e["years"] != "&mdash;":
                parts.append(e["years"])
            if e.get("org"):
                parts.append(e["org"])
            meta = " &middot; ".join(parts) if parts else "&mdash;"
            out.append(pub_item(e["name"], e["role"] or "&mdash;", meta))
        return "\n".join(out)

    body = ["    <h1>Service</h1>",
            "    <h2>Editorial Boards</h2>",
            "    <ul class=\"pub-list\">",
            rows(editorial_entries),
            "    </ul>",
            "    <h2>Recent Service &amp; Leadership (post-2018)</h2>",
            "    <ul class=\"pub-list\">",
            rows([{"name": n, "role": r, "years": y, "org": o} for n, r, y, o in linkedin_newer]),
            "    </ul>",
            "    <h2>Conference Leadership &amp; Chair Roles</h2>",
            "    <ul class=\"pub-list\">",
            rows(chairs),
            "    </ul>",
            "    <h2>Program Committees</h2>",
            "    <ul class=\"pub-list\">",
            rows(pcs),
            "    </ul>"]
    (ROOT / "service.html").write_text(page_shell("Service", "service", "\n".join(body)), encoding="utf-8")
    print(f"service.html: {len(editorial_entries)} editorial + {len(linkedin_newer)} recent + {len(chairs)} chairs + {len(pcs)} PC")


def build_talks():
    # II.D — approx lines 693-905
    talks_text = CV_TXT.read_text(encoding="utf-8").splitlines()[692:905]
    # Split keynotes vs invited talks by subsection header
    keynote_text = []
    invited_text = []
    bucket = None
    for line in talks_text:
        if "Keynote Speeches" in line:
            bucket = keynote_text
            continue
        if "Invited Talks" in line:
            bucket = invited_text
            continue
        if bucket is not None:
            bucket.append(line)

    def bullets_from(lines: list[str]) -> list[str]:
        joined = "\n".join(lines)
        # Use the same bullet logic
        temp = Path("/tmp/talks_tmp.txt")
        temp.write_text(joined, encoding="utf-8")
        # Instead of re-reading, parse inline
        bullets: list[str] = []
        current: list[str] | None = None
        for raw in lines:
            if "November 8, 2018" in raw or raw.strip().startswith("Atif M. Memon"):
                continue
            m = BULLET_RE.match(raw)
            # Also allow lines starting with "1. " etc. for keynotes
            m_num = re.match(r"^\s*\d+\.\s+(.+)$", raw)
            if m or m_num:
                if current:
                    bullets.append(" ".join(current))
                current = [(m or m_num).group(1).strip()]
            elif current is not None and raw.strip():
                current.append(raw.strip())
            elif current and not raw.strip():
                bullets.append(" ".join(current))
                current = None
        if current:
            bullets.append(" ".join(current))
        cleaned = []
        for b in bullets:
            b = re.sub(r"-\s+", "", b)
            b = re.sub(r"\s+", " ", b).strip().rstrip(".")
            if b:
                cleaned.append(b)
        return cleaned

    keynotes = bullets_from(keynote_text)
    invited = bullets_from(invited_text)

    def talk_rows(bullets: list[str], role: str) -> str:
        out = []
        for b in bullets:
            year = extract_year(b)
            # title is in quotes if present
            title_m = re.match(r'^[“"]([^"”]+)[”"],?\s*(.*)$', b)
            if title_m:
                title = title_m.group(1).strip()
                rest = title_m.group(2).strip().rstrip(",")
            else:
                # Use first clause before first comma as title
                parts = b.split(",", 1)
                title = parts[0].strip()
                rest = (parts[1] if len(parts) > 1 else "").strip().rstrip(",")
            title = title.rstrip(",")
            # Strip trailing year from rest so meta doesn't duplicate the year prefix
            if year != "&mdash;":
                plain_year = year.replace("&ndash;", "-")
                rest = re.sub(rf",?\s*{re.escape(plain_year)}\s*$", "", rest).strip().rstrip(",")
            meta = f"{year} &middot; {rest}" if rest and year != "&mdash;" else (year if year != "&mdash;" else rest or "&mdash;")
            out.append(pub_item(title, role, meta))
        return "\n".join(out)

    body = ["    <h1>Talks &amp; Keynotes</h1>",
            "    <h2>Keynote Addresses</h2>",
            "    <ul class=\"pub-list\">",
            talk_rows(keynotes, "Keynote"),
            "    </ul>",
            "    <h2>Invited Talks</h2>",
            "    <ul class=\"pub-list\">",
            talk_rows(invited, "Invited Talk"),
            "    </ul>"]
    (ROOT / "talks.html").write_text(page_shell("Talks", "talks", "\n".join(body)), encoding="utf-8")
    print(f"talks.html: {len(keynotes)} keynotes + {len(invited)} invited")


def main() -> int:
    extract_cv_text()
    build_service()
    build_talks()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
