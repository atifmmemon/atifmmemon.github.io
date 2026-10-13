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
    <p class="affiliation">Distinguished Engineer, Apple</p>
    <ul class="links">
      <li><a href="https://www.linkedin.com/in/memonatif/" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://scholar.google.com/citations?user=jJPSj0IAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
    </ul>
  </aside>

  <nav class="topnav">
    <a href="../publications.html" class="active">Publications</a>
    <a href="../service.html">Service</a>
    <a href="../talks.html">Talks</a>
    <a href="../awards.html">Awards</a>
    <a href="../writing.html">Writing</a>
  </nav>

  <main class="abstract">
    <h1>{title}</h1>

{downloads}

    <p>
    &#8220;{title}&#8221; by {authors}.
    In <em>{venue}</em>, {year}.{pages_phrase}
    </p>
{abstract_section}
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
        "abstract": (
            "Open Domain Question Answering (ODQA) within natural language "
            "processing involves building systems that answer factual "
            "questions using large-scale knowledge corpora. Recent advances "
            "stem from the confluence of several factors, such as large-scale "
            "training datasets, deep learning techniques, and the rise of "
            "large language models. High-quality datasets are used to train "
            "models on realistic scenarios and enable the evaluation of the "
            "system on potentially unseen data. Standardized metrics "
            "facilitate comparisons between different ODQA systems, allowing "
            "researchers to objectively track advancements in the field. Our "
            "study presents a thorough examination of the current landscape "
            "of ODQA benchmarking by reviewing 52 datasets and 20 evaluation "
            "techniques across textual and multimodal modalities. We "
            "introduce a novel taxonomy for ODQA datasets that incorporates "
            "both the modality and difficulty of the question types. "
            "Additionally, we present a structured organization of ODQA "
            "evaluation metrics along with a critical analysis of their "
            "inherent trade-offs. Our study aims to empower researchers by "
            "providing a framework for the robust evaluation of modern "
            "question-answering systems. We conclude by identifying the "
            "current challenges and outlining promising avenues for future "
            "research and development."
        ),
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
        "pdf": "ZhuLongWangMemon_FSE2022.pdf",
        "extra": [
            ("DOI", "https://doi.org/10.1145/3540250.3558941"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3540250.3558941"),
        ],
        "abstract": (
            "Machine Learning (ML) has become the cornerstone of information "
            "retrieval (IR) software, as it can drive better user experience by "
            "leveraging information-rich data and complex models. However, "
            "evaluating the emergent behavior of ML-based IR software can be "
            "challenging with traditional software testing approaches: when "
            "developers modify the software, they cannot often extract useful "
            "information from individual test instances; rather, they seek to "
            "holistically verify whether&mdash;and where&mdash;their modifications "
            "caused significant regressions or improvements at scale. In this "
            "paper, we introduce not only such a holistic approach to evaluate "
            "the system-level behavior of the software, but also the concept of "
            "a <em>defect class</em>, which represents a partition of the input "
            "space on which the ML-based software does measurably worse for an "
            "existing feature or on which the ML task is more challenging for a "
            "new feature. We leverage large volumes of functional test cases, "
            "automatically obtained, to derive these defect classes, and propose "
            "new ways to improve the IR software from an end-user's perspective. "
            "Applying our approach on a real production Search-AutoComplete "
            "system that contains a query interpretation ML component, we "
            "demonstrate that (1) our holistic metrics successfully identified "
            "two regressions and one improvement, where all 3 were independently "
            "verified with retrospective A/B experiments, (2) the automatically "
            "obtained defect classes provided actionable insights during "
            "early-stage ML development, and (3) we also detected defect classes "
            "at the finer sub-component level for which there were significant "
            "regressions, which we blocked prior to different releases."
        ),
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
        "pdf": "ZhuLongMemon_ICSE2021.pdf",
        "extra": [("IEEE Xplore", "https://ieeexplore.ieee.org/document/9402002")],
        "abstract": (
            "Two key design characteristics of machine learning (ML) "
            "systems&mdash;their ever-improving nature, and learning-based "
            "emergent functional behavior&mdash;create a moving target, "
            "posing new challenges for authoring/maintaining functional "
            "regression tests. We identify four specific challenges and "
            "address them by developing a new general methodology to "
            "automatically author and maintain tests. In particular, we use "
            "the volume of production data to periodically refresh our large "
            "corpus of test inputs and expected outputs; we use perturbation "
            "of the data to obtain coverage-adequate tests; and we use "
            "clustering to help identify patterns of failures that are "
            "indicative of software bugs. We demonstrate our methodology on "
            "an ML-based context-aware Speller. Our coverage-adequate, "
            "approx. 1 million regression test cases, automatically authored "
            "and maintained for Speller (1) are virtually maintenance free, "
            "(2) detect a higher number of Speller failures than previous "
            "manually-curated tests, (3) have better coverage of previously "
            "unknown functional boundaries of the ML component, and (4) lend "
            "themselves to automatic failure triaging by clustering and "
            "prioritizing subcategories of tests with over-represented "
            "failures. We identify several systematic failure patterns which "
            "were due to previously undetected bugs in the Speller, e.g., "
            "(1) when the user misses the first letter in a short word, and "
            "(2) when the user mistakenly inserts a character in the last "
            "token of an address; these have since been fixed."
        ),
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
        "pdf": "KowalczykFlakyApple_ICSE2020.pdf",
        "extra": [
            ("DOI", "https://doi.org/10.1145/3377813.3381370"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3377813.3381370"),
        ],
        "abstract": (
            "Test flakiness&mdash;inability to reliably repeat a test's "
            "Pass/Fail outcome&mdash;continues to be a significant problem in "
            "Industry, adversely impacting continuous integration and test "
            "pipelines. Completely eliminating flaky tests is not a realistic "
            "option as a significant fraction of system tests (typically "
            "non-hermetic) for services-based implementations exhibit some "
            "level of flakiness. In this paper, we view the flakiness of a "
            "test as a rankable value, which we quantify, track and assign a "
            "confidence. We develop two ways to model flakiness, capturing "
            "the randomness of test results via <em>entropy</em>, and the "
            "temporal variation via <em>flipRate</em>, and aggregating these "
            "over time. We have implemented our flakiness scoring service "
            "and discuss how its adoption has impacted test suites of two "
            "large services at Apple. We show how flakiness is distributed "
            "across the tests in these services, including typical score "
            "ranges and outliers. The flakiness scores are used to monitor "
            "and detect changes in flakiness trends. Evaluation results "
            "demonstrate near perfect accuracy in ranking, identification "
            "and alignment with human interpretation. The scores were used "
            "to identify 2 causes of flakiness in the dataset evaluated, "
            "which have been confirmed, and where fixes have been "
            "implemented or are underway. Our models reduced flakiness by "
            "44% with less than 1% loss in fault detection."
        ),
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
        "pdf": "TramontanaTOSEM2019.pdf",
        "extra": [
            ("DOI", "https://doi.org/10.1145/3339836"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3339836"),
        ],
        "abstract": (
            "Random testing is a software testing technique through which "
            "programs are tested by generating and executing random inputs. "
            "Because of its unstructured nature, it is difficult to determine "
            "when to stop a random testing process. Faults may be missed if "
            "the process is stopped prematurely, and resources may be wasted "
            "if the process is run too long. In this article, we propose two "
            "promising termination criteria, &ldquo;All Equivalent&rdquo; "
            "(AEQ) and &ldquo;All Included in One&rdquo; (AIO), applicable "
            "to random testing. These criteria stop random testing once the "
            "process has reached a code-coverage-based saturation point "
            "after which additional testing effort is unlikely to provide "
            "additional effectiveness. We model and implement them in the "
            "context of a general random testing process composed of "
            "independent random testing sessions. Thirty-six experiments "
            "involving GUI testing and unit testing of Java applications "
            "have demonstrated that the AEQ criteria is generally able to "
            "stop the process when a code coverage equal or very near to the "
            "saturation level is reached, while AIO is able to stop the "
            "process earlier in cases it reaches the saturation level of "
            "coverage. In addition, the performance of the two criteria has "
            "been compared against other termination criteria adopted in the "
            "literature."
        ),
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
        "pdf": "ParthyMapChecks_ICSE2019.pdf",
        "extra": [("DOI", "https://doi.org/10.1109/ICSE-SEIP.2019.00034")],
        "abstract": (
            "Developing an industry application that serves geographic map "
            "data to users across the world presents the significant "
            "challenge of checking the data using &ldquo;data correctness "
            "checks.&rdquo; The size of data that needs to be "
            "checked&mdash;the entire world&mdash;and data churn "
            "rate&mdash;thousands per day&mdash;makes executing the full set "
            "of candidate checks cost prohibitive. Current techniques rely "
            "on hand-curated static subsets of checks to be run at different "
            "stages of the data production pipeline. These hard-coded "
            "subsets are uninformed of data changes, and cause bug detection "
            "to be delayed to downstream quality assurance activities. To "
            "address these problems, we have developed new representations "
            "of map data changes and checks, formally defined &ldquo;check "
            "safety,&rdquo; and built a recommender system that dynamically "
            "and automatically selects and ranks a relevant subset of checks "
            "using signals from latest data changes. Empirical evaluation "
            "shows that it improves (1) efficiency by eliminating 65% of "
            "checks unrelated to changes, (2) coverage by recommending and "
            "ranking change-related checks from the full set of candidate "
            "checks, previously excluded by the manual process, and (3) "
            "overall visibility into the data editing process by quickly "
            "and automatically identifying latest fault prone parts of the "
            "data."
        ),
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
        "abstract": (
            "<b>Background:</b> Smartphone embedded sensors enable "
            "patient-autonomous measurement of neurological dysfunctions. "
            "The study hypothesized that combining data from two smartphone "
            "tests of fine finger movements would establish secondary "
            "outcomes reflecting domain-specific deficits, tested by "
            "correlating smartphone metrics with neurological exams in "
            "multiple sclerosis (MS) patients.<br>\n    "
            "<b>Methods:</b> An Android MS test suite was developed. The "
            "study compares performance on Finger tapping and Balloon "
            "popping tests across 76 MS patients and 19 healthy volunteers."
            "<br>\n    "
            "<b>Results:</b> Primary smartphone outcomes effectively "
            "differentiated MS patients from healthy volunteers with power "
            "comparable to the traditional 9-hole peg test (9HPT). "
            "Secondary outcomes correlated with neurological exams to "
            "identify cerebellar dysfunction, motor fatigue, and poor "
            "eye-hand coordination or reaction time, showing low "
            "longitudinal intra-individual variance.<br>\n    "
            "<b>Conclusion:</b> Smartphone tests offer richer, reliable "
            "measurements of distinct neurological functions in the time "
            "required for a 9HPT, indicating potential to recreate broader "
            "neurological examinations."
        ),
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
        "pdf": "BoukhvalovaFrontiers2018.pdf",
        "extra": [
            ("DOI", "https://doi.org/10.3389/fneur.2018.00740"),
            ("Full text (Frontiers)", "https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2018.00740/full"),
        ],
        "abstract": (
            "Embedded sensors of the smartphones offer opportunities for "
            "granular, patient-autonomous measurements of neurological "
            "dysfunctions for disease identification, management, and for "
            "drug development. We hypothesized that aggregating data from "
            "two simple smartphone tests of fine finger movements with "
            "differing contribution of specific neurological domains (i.e., "
            "strength &amp; cerebellar functions, vision, and reaction time) "
            "will allow establishment of secondary outcomes that reflect "
            "domain-specific deficit. This hypothesis was tested by assessing "
            "correlations of smartphone-derived outcomes with relevant parts "
            "of neurological examination in multiple sclerosis (MS) patients. "
            "We developed MS test suite on Android platform, consisting of "
            "several simple functional tests. This paper compares "
            "cross-sectional and longitudinal performance of Finger tapping "
            "and Balloon popping tests by 76 MS patients and 19 healthy "
            "volunteers (HV). The primary outcomes of smartphone tests, the "
            "average number of taps (per two 10-s intervals) and the average "
            "number of pops (per two 26-s intervals) differentiated MS from "
            "HV with similar power to traditional, investigator-administered "
            "test of fine finger movements, 9-hole peg test (9HPT). "
            "Additionally, the secondary outcomes identified patients with "
            "predominant cerebellar dysfunction, motor fatigue and poor "
            "eye-hand coordination and/or reaction time, as evidenced by "
            "significant correlations between these derived outcomes and "
            "relevant parts of neurological examination. The intra-individual "
            "variance in longitudinal sampling was low. In the time necessary "
            "for performing 9HPT, smartphone tests provide much richer and "
            "reliable measurements of several distinct neurological "
            "functions. These data suggest that combing more "
            "creatively-construed smartphone apps may one day recreate the "
            "entire neurological examination."
        ),
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
        "pdf": "KowalczykConfigsAndroid2018.pdf",
        "extra": [
            ("DOI", "https://doi.org/10.1145/3243218.3243219"),
            ("PDF (ACM)", "https://dl.acm.org/doi/pdf/10.1145/3243218.3243219"),
        ],
        "abstract": (
            "Android has rocketed to the top of the mobile market thanks in "
            "large part to its open source model. Vendors use Android for "
            "their devices for free, and companies make customizations to "
            "suit their needs. This has resulted in a myriad of "
            "configurations that are extant in the user space today. In "
            "this paper, we show that differences in configurations, if "
            "ignored, can lead to differences in test outputs and code "
            "coverage. Consequently, researchers who develop new testing "
            "techniques and evaluate them on only one or two configurations "
            "are missing a necessary dimension in their experiments and "
            "developers who ignore this may release buggy software. In a "
            "large study on 18 apps across 88 configurations, we show that "
            "only one of the 18 apps studied showed no variation at all. "
            "The rest showed variation in either, or both, code coverage "
            "and test results. 15% of the 2,000 plus test cases across all "
            "of the apps vary, and some of the variation is subtle, i.e. "
            "not just a test crash. Our results suggest that configurations "
            "in Android testing do matter and that developers need to test "
            "using configuration-aware techniques."
        ),
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
        abstract = e.get("abstract")
        if abstract:
            abstract_section = (
                "\n    <h2>Abstract</h2>\n"
                f"    <p>\n    {abstract}\n    </p>\n"
            )
        else:
            abstract_section = ""
        html = PAGE.format(
            title=e["title"],
            authors=e["authors"],
            venue=e["venue"],
            year=e["year"],
            pages_phrase=pages_phrase,
            downloads=download_block(e["pdf"], e["extra"]),
            abstract_section=abstract_section,
            bibtex=e["bibtex"],
        )
        out = PAPERS / f"{e['key']}-abstract.html"
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
