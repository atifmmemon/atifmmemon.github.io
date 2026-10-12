#!/usr/bin/env python3
"""
Generate local abstract HTML pages for the 8 publications added after
mirroring the UMD archive, so every entry in publications.html can link
to a local Abstract page in the same site shell as the rest.

Idempotent: overwrites the target files each run.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS = ROOT / "papers"

PAGE = """<!doctype html>
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
    <p class="affiliation">Apple</p>
    <ul class="links">
      <li><a href="https://www.linkedin.com/in/memonatif/" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://scholar.google.com/citations?user=jJPSj0IAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
    </ul>
  </aside>

  <nav class="topnav">
    <a href="../index.html">About</a>
    <a href="../publications.html" class="active">Publications</a>
  </nav>

  <main class="abstract">
    <h1>{title}</h1>

{downloads}

    <p>
    &#8220;{title}&#8221; by {authors}.
    In <em>{venue}</em>, {year}.{pages_phrase}
    </p>

    <p>
    <b>BibTeX entry:</b>
    </p>
    <pre>
{bibtex}
    </pre>

    <hr />

    <p>
    Back to <a href="../publications.html">Atif Memon's Publications</a>.
    </p>
  </main>
</body>
</html>
"""


def download_block(pdf: str | None, extra: list[tuple[str, str]]) -> str:
    links = []
    if pdf:
        links.append(f'<a href="{pdf}">PDF</a>')
    for label, href in extra:
        links.append(f'<a href="{href}" target="_blank" rel="noopener">{label}</a>')
    if not links:
        return ""
    return "    <p>\n    <b>Download:</b>\n    " + " &middot; ".join(links) + ".\n    </p>"


ENTRIES = [
    {
        "key": "Srivastava_Memon_2024_QA_Taxonomy",
        "title": "Toward Robust Evaluation: A Comprehensive Taxonomy of Datasets and Metrics for Open Domain Question Answering in the Era of Large Language Models",
        "authors": "Akchay Srivastava and Atif Memon",
        "venue": "IEEE Access",
        "year": "2024",
        "pages": "pp. 117483-117503, vol. 12",
        "pdf": "Srivastava_Memon_2024_QA_Taxonomy.pdf",
        "extra": [("arXiv:2406.13232", "https://arxiv.org/abs/2406.13232")],
        "bibtex": """@article{SrivastavaMemonIEEEAccess2024,
   author = {Akchay Srivastava and Atif Memon},
   title = {Toward Robust Evaluation: A Comprehensive Taxonomy of Datasets
     and Metrics for Open Domain Question Answering in the Era of
     Large Language Models},
   journal = {IEEE Access},
   volume = {12},
   pages = {117483--117503},
   year = {2024}
}""",
    },
    {
        "key": "ZhuLongWangMemon_FSE2022",
        "title": "Improving ML-based Information Retrieval Software with User-driven Functional Testing and Defect Class Analysis",
        "authors": "Junjie Zhu, Teng Long, Wei Wang, and Atif Memon",
        "venue": "Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)",
        "year": "2022",
        "pages": "pp. 1291-1301",
        "pdf": None,
        "extra": [
            ("DOI", "https://doi.org/10.1145/3540250.3558941"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3540250.3558941"),
        ],
        "bibtex": """@inproceedings{ZhuLongWangMemonFSE2022,
   author = {Junjie Zhu and Teng Long and Wei Wang and Atif Memon},
   title = {Improving ML-based Information Retrieval Software with
     User-driven Functional Testing and Defect Class Analysis},
   booktitle = {Proceedings of the 30th ACM Joint European Software
     Engineering Conference and Symposium on the Foundations of
     Software Engineering},
   series = {ESEC/FSE 2022},
   pages = {1291--1301},
   year = {2022},
   doi = {10.1145/3540250.3558941}
}""",
    },
    {
        "key": "ZhuLongMemon_ICSE2021",
        "title": "Automatically Authoring Regression Tests for Machine-Learning Based Systems",
        "authors": "Junjie Zhu, Teng Long, and Atif Memon",
        "venue": "Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)",
        "year": "2021",
        "pages": "pp. 374-383",
        "pdf": "ICSE2021-PrePrint.pdf",
        "extra": [("IEEE Xplore", "https://ieeexplore.ieee.org/document/9402002")],
        "bibtex": """@inproceedings{ZhuLongMemonICSE2021,
   author = {Junjie Zhu and Teng Long and Atif Memon},
   title = {Automatically Authoring Regression Tests for Machine-Learning
     Based Systems},
   booktitle = {Proceedings of the 43rd IEEE/ACM International Conference
     on Software Engineering: Software Engineering in Practice},
   series = {ICSE-SEIP 2021},
   pages = {374--383},
   year = {2021}
}""",
    },
    {
        "key": "KowalczykFlakyApple_ICSE2020",
        "title": "Modeling and Ranking Flaky Tests at Apple",
        "authors": "Emily Kowalczyk, Karan Nair, Zebao Gao, Leo Silberstein, Teng Long, and Atif Memon",
        "venue": "Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)",
        "year": "2020",
        "pages": "pp. 110-119",
        "pdf": None,
        "extra": [
            ("DOI", "https://doi.org/10.1145/3377813.3381370"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3377813.3381370"),
        ],
        "bibtex": """@inproceedings{KowalczykFlakyApple2020,
   author = {Emily Kowalczyk and Karan Nair and Zebao Gao and Leo
     Silberstein and Teng Long and Atif Memon},
   title = {Modeling and Ranking Flaky Tests at {Apple}},
   booktitle = {Proceedings of the ACM/IEEE 42nd International Conference
     on Software Engineering: Software Engineering in Practice},
   series = {ICSE-SEIP 2020},
   pages = {110--119},
   year = {2020},
   doi = {10.1145/3377813.3381370}
}""",
    },
    {
        "key": "TramontanaTOSEM2019",
        "title": "Developing and Evaluating Objective Termination Criteria for Random Testing",
        "authors": "Porfirio Tramontana, Domenico Amalfitano, Nicola Amatucci, Atif Memon, and Anna Rita Fasolino",
        "venue": "ACM Transactions on Software Engineering and Methodology (TOSEM)",
        "year": "2019",
        "pages": "vol. 28, no. 3, pp. 1-52",
        "pdf": None,
        "extra": [
            ("DOI", "https://doi.org/10.1145/3339836"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3339836"),
        ],
        "bibtex": """@article{TramontanaTOSEM2019,
   author = {Porfirio Tramontana and Domenico Amalfitano and Nicola
     Amatucci and Atif Memon and Anna Rita Fasolino},
   title = {Developing and Evaluating Objective Termination Criteria for
     Random Testing},
   journal = {ACM Transactions on Software Engineering and Methodology},
   volume = {28},
   number = {3},
   pages = {1--52},
   year = {2019},
   doi = {10.1145/3339836}
}""",
    },
    {
        "key": "ParthyMapChecks_ICSE2019",
        "title": "Using Machine Learning to Recommend Correctness Checks for Geographic Map Data",
        "authors": "Abhaya Parthy, Leo Silberstein, Emily Kowalczyk, John-Paul High, Adithya Nagarajan, and Atif Memon",
        "venue": "Proceedings of the 41st IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)",
        "year": "2019",
        "pages": "pp. 223-232",
        "pdf": None,
        "extra": [("DOI", "https://doi.org/10.1109/ICSE-SEIP.2019.00034")],
        "bibtex": """@inproceedings{ParthyMapChecks2019,
   author = {Abhaya Parthy and Leo Silberstein and Emily Kowalczyk and
     John-Paul High and Adithya Nagarajan and Atif Memon},
   title = {Using Machine Learning to Recommend Correctness Checks for
     Geographic Map Data},
   booktitle = {Proceedings of the 41st IEEE/ACM International Conference
     on Software Engineering: Software Engineering in Practice},
   series = {ICSE-SEIP 2019},
   pages = {223--232},
   year = {2019},
   doi = {10.1109/ICSE-SEIP.2019.00034}
}""",
    },
    {
        "key": "BoukhvalovaACTRIMS2019",
        "title": "Identifying and Quantifying Neurological Disability Via Smartphone App",
        "authors": "Alexandra Boukhvalova, Emily Kowalczyk, Thomas Harris, Peter Kosa, Alison Wichman, Mary Sandford, Atif Memon, and Bibiana Bielekova",
        "venue": "ACTRIMS Forum",
        "year": "2019",
        "pages": "",
        "pdf": None,
        "extra": [],
        "bibtex": """@inproceedings{BoukhvalovaACTRIMS2019,
   author = {Alexandra Boukhvalova and Emily Kowalczyk and Thomas Harris
     and Peter Kosa and Alison Wichman and Mary Sandford and Atif Memon
     and Bibiana Bielekova},
   title = {Identifying and Quantifying Neurological Disability Via
     Smartphone App},
   booktitle = {ACTRIMS Forum},
   year = {2019}
}""",
    },
    {
        "key": "BoukhvalovaFrontiers2018",
        "title": "Identifying and Quantifying Neurological Disability via Smartphone",
        "authors": "Alexandra K. Boukhvalova, Emily Kowalczyk, Thomas Harris, Peter Kosa, Alison Wichman, Mary A. Sandford, Atif Memon, and Bibiana Bielekova",
        "venue": "Frontiers in Neurology",
        "year": "2018",
        "pages": "vol. 9, art. 740",
        "pdf": None,
        "extra": [
            ("DOI", "https://doi.org/10.3389/fneur.2018.00740"),
            ("Full text (Frontiers)", "https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2018.00740/full"),
        ],
        "bibtex": """@article{BoukhvalovaFrontiers2018,
   author = {Alexandra K. Boukhvalova and Emily Kowalczyk and Thomas
     Harris and Peter Kosa and Alison Wichman and Mary A. Sandford and
     Atif Memon and Bibiana Bielekova},
   title = {Identifying and Quantifying Neurological Disability via
     Smartphone},
   journal = {Frontiers in Neurology},
   volume = {9},
   pages = {740},
   year = {2018},
   doi = {10.3389/fneur.2018.00740}
}""",
    },
    {
        "key": "KowalczykConfigsAndroid2018",
        "title": "Configurations in Android Testing: They Matter",
        "authors": "Emily Kowalczyk, Myra B. Cohen, and Atif M. Memon",
        "venue": "Proceedings of the 1st International Workshop on Advances in Mobile App Analysis (A-Mobile)",
        "year": "2018",
        "pages": "pp. 1-6",
        "pdf": None,
        "extra": [
            ("DOI", "https://doi.org/10.1145/3243218.3243219"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3243218.3243219"),
        ],
        "bibtex": """@inproceedings{KowalczykConfigsAndroid2018,
   author = {Emily Kowalczyk and Myra B. Cohen and Atif M. Memon},
   title = {Configurations in {Android} Testing: They Matter},
   booktitle = {Proceedings of the 1st International Workshop on Advances
     in Mobile App Analysis},
   series = {A-Mobile 2018},
   pages = {1--6},
   year = {2018},
   doi = {10.1145/3243218.3243219}
}""",
    },
]


def main() -> int:
    for e in ENTRIES:
        pages_phrase = f" {e['pages']}." if e["pages"] else ""
        html = PAGE.format(
            title=e["title"],
            authors=e["authors"],
            venue=e["venue"],
            year=e["year"],
            pages_phrase=pages_phrase,
            downloads=download_block(e["pdf"], e["extra"]),
            bibtex=e["bibtex"],
        )
        out = PAPERS / f"{e['key']}-abstract.html"
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
