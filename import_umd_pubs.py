#!/usr/bin/env python3
"""
import_umd_pubs.py

Usage:
  python3 import_umd_pubs.py

Requirements:
  python3
  pip install requests beautifulsoup4
  git configured with GitHub auth (SSH or HTTPS credential helper)

This script:
  - fetches the UMD publications page,
  - follows detail links,
  - downloads linked PDFs,
  - stores them under ./publications/,
  - creates a simple publications index page,
  - commits and pushes to origin/main.
"""
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE = "https://www.cs.umd.edu"
PUBS_URL = BASE + "/~atif/publications.shtml"
REPO_NWO = "atifmmemon/atifmmemon.github.io"
CLONE_DIR = "atifmmemon.github.io"
OUT_DIR = os.path.join(CLONE_DIR, "publications")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
DETAILS_DIR = os.path.join(OUT_DIR, "details")
COMMIT_MSG = "Import UMD publications page and PDFs"
MAX_PDF_SIZE_BYTES = 100 * 1024 * 1024


def run(cmd, cwd=None):
    print(">", " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print("Command failed:", cmd)
        sys.exit(1)


def safe_mkdir(path):
    os.makedirs(path, exist_ok=True)


def slugify_filename(url):
    path = urlparse(url).path
    name = re.sub(r"[^0-9A-Za-z._-]+", "_", path.strip("/"))
    if not name:
        name = "file"
    return name


def clone_repo():
    if os.path.exists(CLONE_DIR):
        print("Removing existing clone:", CLONE_DIR)
        shutil.rmtree(CLONE_DIR)
    run(["git", "clone", f"https://github.com/{REPO_NWO}.git", CLONE_DIR])


def download_url(url, dest_path, stream=False):
    print("GET", url)
    with requests.get(url, stream=stream, allow_redirects=True, timeout=30) as r:
        r.raise_for_status()
        if stream:
            total = 0
            with open(dest_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        total += len(chunk)
                        if total > MAX_PDF_SIZE_BYTES:
                            raise RuntimeError(f"File exceeds {MAX_PDF_SIZE_BYTES} bytes: {url}")
        else:
            with open(dest_path, "wb") as f:
                f.write(r.content)


def find_detail_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        text = a.get_text(" ", strip=True)
        if not href:
            continue
        full = urljoin(base_url, href)
        is_candidate = (
            "/papers/" in href
            or "Details" in text
            or href.endswith("-abstract.html")
            or "detail" in href.lower()
        )
        if is_candidate and full not in seen:
            seen.add(full)
            links.append((text or href, full))
    return links


def find_pdf_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    pdfs = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.lower().endswith(".pdf"):
            full = urljoin(base_url, href)
            if full not in seen:
                seen.add(full)
                pdfs.append(full)
    return pdfs


def build_publications_index(papers):
    html = [
        "<!doctype html>",
        "<html><head><meta charset=\"utf-8\" /><title>Publications</title></head><body>",
        "<h1>Publications</h1>",
        "<ul>",
    ]

    for p in papers:
        title = p.get("title") or p.get("detail_url")
        html.append("<li>")
        pdfs = p.get("pdfs", [])
        if pdfs:
            first_pdf = pdfs[0]
            # make relative link based on repo root: /publications/pdfs/...
            pdf_rel = os.path.relpath(first_pdf, CLONE_DIR)
            html.append(f'<a href="/{pdf_rel}">{title}</a>')
            html.append(f' (<a href="/{pdf_rel}">pdf</a>)')
        else:
            html.append(title)
        if p.get("local_detail"):
            detail_rel = os.path.relpath(p["local_detail"], CLONE_DIR)
            html.append(f' - <a href="/{detail_rel}">details</a>')
        html.append("</li>")

    html.append("</ul>")
    html.append("</body></html>")
    return "\n".join(html)


def main():
    clone_repo()
    safe_mkdir(PDF_DIR)
    safe_mkdir(DETAILS_DIR)

    r = requests.get(PUBS_URL, timeout=30)
    r.raise_for_status()
    main_html = r.text

    detail_links = find_detail_links(main_html, PUBS_URL)
    print(f"Found {len(detail_links)} detail links")
    papers = []

    for text, link in detail_links:
        item = {"title": text or link, "detail_url": link, "pdfs": []}
        try:
            dr = requests.get(link, timeout=30)
            dr.raise_for_status()
            detail_html = dr.text

            filename = slugify_filename(link) + ".html"
            local_detail = os.path.join(DETAILS_DIR, filename)
            with open(local_detail, "w", encoding="utf-8") as f:
                f.write(detail_html)
            item["local_detail"] = local_detail

            pdf_links = find_pdf_links(detail_html, link)
            for pdf_link in pdf_links:
                pdf_name = os.path.basename(urlparse(pdf_link).path)
                if not pdf_name:
                    pdf_name = slugify_filename(pdf_link) + ".pdf"
                local_pdf = os.path.join(PDF_DIR, pdf_name)
                if not os.path.exists(local_pdf):
                    try:
                        download_url(pdf_link, local_pdf, stream=True)
                    except Exception as exc:
                        print(f"Warning: failed to download {pdf_link}: {exc}")
                        continue
                item["pdfs"].append(local_pdf)

        except Exception as exc:
            print(f"Warning: failed to fetch {link}: {exc}")

        papers.append(item)

    index_path = os.path.join(OUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(build_publications_index(papers))

    run(["git", "-C", CLONE_DIR, "add", "publications"], cwd=None)
    run(["git", "-C", CLONE_DIR, "commit", "-m", COMMIT_MSG], cwd=None)
    run(["git", "-C", CLONE_DIR, "push", "origin", "main"], cwd=None)

    print("Done. Visit https://atifmmemon.github.io/publications/ after the Pages build completes.")


if __name__ == "__main__":
    main()
