#!/usr/bin/env python3
"""
Hand-curated service.html generator. Every entry below was reviewed
individually against the CV (papers/cv.pdf) and LinkedIn — no regex
classification. Each entry has a uniform 4-field shape:
  name, role, years, org (em-dash '&mdash;' where unknown)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

ED_BOARDS = [
    # (name, role, years, org)
    ("ACM Computing Surveys (CSUR)", "Editorial Board Member", "Oct 2016&ndash;Present", "ACM"),
    ("Empirical Software Engineering (EMSE)", "Board of Advisors", "Nov 2020", "Springer"),
    ("Advances in Computers", "Series Editor", "&mdash;", "Elsevier"),
    ("Empirical Software Engineering (EMSE)", "Editorial Board Member", "&mdash;", "Springer"),
    ("Software Testing, Verification and Reliability (STVR)", "Editorial Board Member", "&mdash;", "Wiley"),
    ("The Open Software Engineering Journal (OSE)", "Editorial Board Member", "&mdash;", "Bentham Science"),
    ("Canadian Journal of Pure and Applied Sciences (CJPAS)", "Editorial Board Member", "&mdash;", "SENRA Academic Publishers"),
    ("IEEE Transactions on Software Engineering", "Guest Associate Editor", "Oct 2003", "IEEE"),
]

MEMBERSHIPS = [
    ("Association for Computing Machinery (ACM)", "Member", "Aug 1997&ndash;Present", "ACM"),
    ("IEEE Computer Society", "Member", "Aug 1997&ndash;Present", "IEEE"),
]

# Chair, Steering Committee, Organizing, Awards Chair, PC Chair,
# PhD Symposium Chair, Workshops Chair, Session Chair, Panel Member,
# Mentoring Committee, Advisory Board, Publications Chair, Elected committees.
LEADERSHIP = [
    ("IEEE Computer Society — Technical Council on Software Engineering (TCSE)", "Executive Committee (Elected)", "2022&ndash;2025", "IEEE Computer Society"),
    ("16th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Panelist &mdash; Research, Industry, and Emerging Frontiers", "2025", "Naples, Italy"),
    ("16th IEEE ICST — Testing ML Systems and Fault Localisation session", "Session Chair", "2025", "Naples, Italy"),
    ("14th IEEE ICST", "Industry Co-Chair (Organizing Committee)", "2023", "&mdash;"),
    ("14th IEEE ICST — Industry Track", "Program Committee Co-Chair", "2023", "&mdash;"),
    ("International Conference on Software Testing, Verification and Validation (ICST)", "Steering Committee Member", "2020&ndash;2023", "IEEE"),
    ("12th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Technical Program Committee Co-Chair", "2019", "Xi'an, China"),
    ("10th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "General Chair", "2017", "Tokyo, Japan"),
    ("38th International Conference on Software Engineering (ICSE)", "Awards Chair", "2016", "Austin, Texas"),
    ("ICST 2016 PhD Symposium", "Panel Member", "2016", "&mdash;"),
    ("ICST 2015 — Grand Challenges in Software Testing, Verification &amp; Validation Panel", "Panel Member", "2015", "&mdash;"),
    ("ICST 2015 PhD Symposium", "Panel Member", "2015", "&mdash;"),
    ("6th IEEE International Workshop on Program Debugging", "Panel Member", "2015", "&mdash;"),
    ("36th International Conference on Software Engineering (ICSE)", "Awards Chair", "2014", "Hyderabad, India"),
    ("ICSE 2013 Mentoring Committee", "Member", "2013", "&mdash;"),
    ("ICST 2013 PhD Symposium", "Member", "2013", "&mdash;"),
    ("ICSE 2012 Mentoring Committee", "Member", "2012", "&mdash;"),
    ("9th Annual International Conference on Mobile Systems, Applications and Services (MobiSys)", "Workshops Co-Chair", "2011", "&mdash;"),
    ("4th IEEE ICST 2011 PhD Symposium Committee", "Member", "2011", "&mdash;"),
    ("ICSE 2011 Mentoring Committee", "Member", "2011", "&mdash;"),
    ("3rd International Workshop on TESTing Techniques &amp; Experimentation Benchmarks (TESTBEDS)", "General Chair", "2011", "GUI and Web Applications"),
    ("Workshop on Experimental Evaluation of Software and Systems in Computer Science (Evaluate)", "Organizing Committee", "2010", "Reno/Tahoe, NV (SPLASH'10)"),
    ("ICST 2010", "Session Chair", "2010", "&mdash;"),
    ("2nd International Workshop on TESTBEDS", "General Chair", "2010", "GUI and Rich Internet Applications"),
    ("3rd IEEE ICST 2010 PhD Symposium", "PhD Symposium Chair", "2010", "&mdash;"),
    ("1st International Workshop on TESTBEDS", "General Chair", "2009", "GUI Testing"),
    ("2nd IEEE ICST 2009 PhD Symposium", "PhD Symposium Chair", "2009", "&mdash;"),
    ("Proceedings of the 2004 IEEE International Conference on Information Reuse and Integration (IRI)", "Editor", "2004", "IEEE"),
    ("IEEE International Conference on Information Reuse and Integration (IRI)", "Publications Chair", "2004", "Las Vegas, NV"),
    ("11th IEEE Working Conference on Reverse Engineering (WCRE) — Platform &amp; Language-specific Re-engineering session", "Session Chair", "2004", "Delft, Netherlands"),
    ("IASTED International Conference on Artificial Intelligence and Applications (AIA)", "Session Chair", "2004", "Innsbruck, Austria"),
    ("Proceedings of the 2003 IEEE International Conference on Information Reuse and Integration (IRI)", "Associate Editor", "2003", "IEEE"),
    ("IEEE International Conference on Information Reuse and Integration (IRI)", "Publications Chair", "2003", "Las Vegas, NV"),
    ("10th International Symposium on the Foundations of Software Engineering (FSE-10) — Dynamic Program Analysis session", "Session Chair", "2002", "Charleston, SC"),
    ("15th International Internet &amp; Software Quality Week (QW)", "Advisory Board", "2002", "San Francisco, CA"),
    ("14th International Internet &amp; Software Quality Week (QW)", "Advisory Board", "2001", "San Francisco, CA"),
]

# All Program Committee memberships, newest first. Each hand-reviewed.
PROGRAM_COMMITTEES = [
    # From researchr.org / LinkedIn — post-CV
    ("ACM International Conference on the Foundations of Software Engineering (FSE 2026) — Ideas, Visions and Reflections Track", "Program Committee", "2026", "ACM"),
    ("ACM International Conference on the Foundations of Software Engineering (FSE 2024)", "Program Committee", "2024", "ACM"),
    ("46th International Conference on Software Engineering (ICSE 2024) — SEIP Track", "Program Committee", "2024", "ACM/IEEE"),
    ("ESEC/FSE 2023 — Industry Papers Track", "Program Committee", "2023", "ACM"),
    ("ESEC/FSE 2022 — Industry Paper Track", "Program Committee", "2022", "ACM"),
    ("13th IEEE ICST 2020 — Doctoral Symposium", "Program Committee", "2020", "&mdash;"),
    ("34th IEEE/ACM International Conference on Automated Software Engineering (ASE 2019) — Doctoral Symposium", "Program Committee", "2019", "&mdash;"),
    ("40th International Conference on Software Engineering (ICSE 2018) — Technical Papers Track", "Program Committee", "2018", "&mdash;"),
    # CV entries
    ("11th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee", "2018", "Västerås, Sweden"),
    ("3rd International Workshop on User Interface Test Automation (INTUITEST)", "Program Committee", "2017", "Berlin, Germany"),
    ("8th A-TEST Workshop (co-located with FSE)", "Program Committee", "2017", "Paderborn, Germany"),
    ("7th A-TEST Workshop (co-located with FSE)", "Program Committee", "2016", "Seattle, WA"),
    ("9th IEEE International Conference on Software Testing, Verification and Validation (ICST) — Regular Technical Papers Track", "Program Committee", "2016", "&mdash;"),
    ("9th IEEE ICST — Testing Tool Demo Track", "Program Committee", "2016", "&mdash;"),
    ("38th International Conference on Software Engineering (ICSE)", "Program Committee", "2016", "Austin, Texas"),
    ("1st International Workshop on User Interface Test Automation (INTUITEST)", "Program Committee", "2015", "&mdash;"),
    ("6th International Workshop on Automating Test Case Design, Selection and Evaluation (co-located with SEFM 2015)", "Programme Committee", "2015", "York, UK"),
    ("Workshop on Complex Faults and Failures in Large Software Systems (COUFLESS 2015)", "Program Committee", "2015", "Florence, Italy"),
    ("8th IEEE ICST", "Program Committee", "2015", "Graz, Austria"),
    ("10th IEEE/ACM International Workshop on Automation of Software Test (AST)", "Program Committee", "2015", "Firenze, Italy"),
    ("1st International Workshop on Complex Faults and Failures in Large Software Systems (co-located with FSE)", "Program Committee", "2014", "Hong Kong"),
    ("25th IEEE International Symposium on Software Reliability Engineering (ISSRE)", "Program Committee", "2014", "Naples, Italy"),
    ("9th International Conference on the Quality of Information and Communications Technology (QUATIC) — Quality in Agile Methods track", "Program Committee", "2014", "Guimarães, Portugal"),
    ("9th International Workshop on Automation of Software Test (AST'14)", "Program Committee", "2014", "&mdash;"),
    ("7th IEEE ICST", "Program Committee", "2014", "Cleveland, Ohio"),
    ("5th Workshop on Automated Test Case Design, Selection and Evaluation (ATSE)", "Program Committee", "2014", "&mdash;"),
    ("1st International Workshop on Future Internet Testing (FITTEST, co-located with ICTSS)", "Program Committee", "2013", "Istanbul, Turkey"),
    ("7th India Software Engineering Conference (ISEC)", "Program Committee", "2014", "Chennai, India"),
    ("Joining AcadeMiA and Industry Contributions to testing Automation (JAMAICA) Workshop (co-located with ISSTA)", "Program Committee", "2013", "Lugano, Switzerland"),
    ("4th Workshop on Automated Test Case Design, Selection and Evaluation (ATSE)", "Program Committee", "2013", "Kraków, Poland"),
    ("13th International Conference on Quality Software (QSIC)", "Program Committee", "2013", "Nanjing, China"),
    ("International Workshop on Regression Testing (co-located with ICST)", "Program Committee", "2013", "Luxembourg"),
    ("4th International Conference on Runtime Verification (RV)", "Program Committee", "2013", "&mdash;"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC PART)", "Program Committee", "2013", "&mdash;"),
    ("8th International Conference on the Quality of Information and Communications Technology (QUATIC) — Main Track", "Program Committee", "2012", "Lisbon, Portugal"),
    ("2nd International Workshop on End-to-end Test Script Engineering (ETSE, co-located with ISSTA)", "Program Committee", "2012", "&mdash;"),
    ("3rd International Conference on Runtime Verification (RV)", "Program Committee", "2012", "&mdash;"),
    ("8th QUATIC — Quality in Agile Methods track", "Program Committee", "2012", "Porto, Portugal"),
    ("Automation of Software Test (AST, co-located with ICSE)", "Program Committee", "2012", "&mdash;"),
    ("IEEE 20th International Requirements Engineering Conference — Industry Track", "Program Committee", "2012", "Chicago, USA"),
    ("2nd International Workshop on Regression Testing (co-located with ICST)", "Program Committee", "2012", "Montreal, Canada"),
    ("Testing Academic &amp; Industrial Conference (TAIC-PART, co-located with ICST)", "Program Committee", "2012", "Montreal, Canada"),
    ("12th International Conference on Quality Software (QSIC)", "Program Committee", "2012", "Xi'an, China"),
    ("ICSM Industry Track", "Program Committee", "2011", "Williamsburg, VA"),
    ("5th International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Program Committee", "2011", "Lisbon, Portugal"),
    ("6th IEEE International Workshop on Automation of Software Test (AST, co-located with ICSE)", "Program Committee", "2011", "&mdash;"),
    ("TAIC-PART (co-located with ICST)", "Program Committee", "2011", "Berlin, Germany"),
    ("3rd International Conference on Advances in System Testing and Validation Lifecycle (VALID)", "Program Committee", "2011", "Barcelona, Spain"),
    ("11th International Conference on Quality Software (QSIC)", "Program Committee", "2011", "Madrid, Spain"),
    ("Early Research Achievements Track, 26th IEEE International Conference on Software Maintenance (ICSM)", "Program Committee", "2010", "Timisoara, Romania"),
    ("ICIS 2010", "Program Committee", "2010", "Yamagata, Japan"),
    ("4th India Software Engineering Conference (ISEC)", "Program Committee", "2010", "Thiruvananthapuram, India"),
    ("TAIC-PART", "Program Committee", "2010", "Windsor, UK"),
    ("7th QUATIC — Quality in Agile Methods track", "Program Committee", "2010", "Porto, Portugal"),
    ("21st IEEE ISSRE", "Program Committee", "2010", "San Jose, CA"),
    ("5th Automation of Software Test (AST, co-located with ICSE)", "Program Committee", "2010", "&mdash;"),
    ("5th International Conference on Software and Data Technologies (ICSOFT)", "International Program Committee", "2010", "&mdash;"),
    ("4th International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Program Committee", "2010", "Florence, Italy"),
    ("8th ACIS International Conference on Software Engineering Research, Management and Applications (SERA)", "Program Committee", "2010", "&mdash;"),
    ("VALID 2010", "Program Committee", "2010", "Nice, France"),
    ("International Conference on Information Science and Applications (ICISA)", "Program Committee", "2010", "Seoul, Korea"),
    ("2nd International Conference on Intensive Applications and Services (INTENSIVE)", "Program Committee", "2010", "Cancun, Mexico"),
    ("10th International Conference on Quality Software (QSIC)", "Program Committee", "2010", "Zhangjiajie, China"),
    ("3rd IEEE ICST", "Program Committee", "2010", "&mdash;"),
    ("3rd India Software Engineering Conference (ISEC)", "Program Committee", "2010", "Mysore, India"),
    ("25th IEEE ICSM", "Program Committee", "2009", "Edmonton, Alberta, Canada"),
    ("WWW 2009 — Web Engineering Track", "Program Committee", "2009", "Madrid, Spain"),
    ("TAIC-PART", "Program Committee", "2009", "Windsor, UK"),
    ("1st International Conference on Advances in System Testing and Validation Lifecycle (VALID)", "Program Committee", "2009", "Porto, Portugal"),
    ("4th International Conference on Software Engineering Advances (ICSEA)", "Program Committee", "2009", "Porto, Portugal"),
    ("3rd ADVCOMP", "Program Committee", "2009", "Sliema, Malta"),
    ("10th ACIS International Conference on Software Engineering, AI, Networking, and Parallel/Distributed Computing (SNPD)", "Program Committee", "2009", "&mdash;"),
    ("9th International Conference on Quality Software (QSIC)", "Program Committee", "2009", "Jeju, Korea"),
    ("Software Engineering Symposium, 2009 World Congress on Computer Science and Information Engineering", "Program Committee", "2009", "Los Angeles / Anaheim"),
    ("8th IEEE/ACIS International Conference on Computer and Information Science (ICIS)", "Program Committee", "2009", "Shanghai, China"),
    ("4th International Conference on Software and Data Technologies (ICSOFT)", "International Program Committee", "2009", "&mdash;"),
    ("7th ACIS SERA", "International Program Committee", "2009", "Haikou, China"),
    ("1st International Conference on Intensive Applications and Services (INTENSIVE)", "Program Committee", "2009", "Valencia, Spain"),
    ("1st International Workshop on Web Testing (WebTest, co-located with ICST)", "Program Committee", "2009", "Denver, CO"),
    ("2nd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Technical Program Committee", "2009", "&mdash;"),
    ("2nd India Software Engineering Conference (ISEC)", "Program Committee", "2009", "Pune, India"),
    ("30th International Conference on Software Engineering (ICSE)", "Program Committee", "2008", "Leipzig, Germany"),
    ("TAIC-PART", "Program Committee", "2008", "Windsor, UK"),
    ("24th IEEE ICSM", "Program Committee", "2008", "Beijing, China"),
    ("Software Engineering Research, Management and Applications Conference (SERA)", "Program Committee", "2008", "Prague"),
    ("3rd International Conference on Software and Data Technologies (ICSOFT)", "Program Committee", "2008", "Porto, Portugal"),
    ("9th SNPD", "Program Committee", "2008", "Phuket, Thailand"),
    ("8th International Conference on Quality Software (QSIC)", "Program Committee", "2008", "Oxford, UK"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee", "2008", "Sliema, Malta"),
    ("7th IEEE/ACIS International Conference on Computer and Information Science (ICIS)", "Program Committee", "2008", "Portland, OR"),
    ("2nd International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Technical Program Committee", "2008", "Valencia, Spain"),
    ("2nd International Workshop on Software Test Evaluation (STEV, co-located with ICST)", "Program Committee", "2008", "Lillehammer, Norway"),
    ("17th International World Wide Web Conference (WWW) — Web Engineering Track", "Program Committee", "2008", "Beijing, China"),
    ("1st IEEE ICST — Industry Track", "Program Committee", "2008", "Lillehammer, Norway"),
    ("1st IEEE ICST — Research Track", "Technical Program Committee", "2008", "Lillehammer, Norway"),
    ("ADVCOMP 2007", "Technical Program Committee", "2007", "Tahiti, French Polynesia"),
    ("1st International Workshop on Software Test Evaluation (STEV)", "Program Committee", "2007", "Portland, OR"),
    ("7th International Conference on Quality Software (QSIC)", "Program Committee", "2007", "Portland, OR"),
    ("5th IEEE International Conference on Software Engineering Research, Management and Applications (SERA)", "Program Committee", "2007", "Busan, Korea"),
    ("International Workshop on Distance Education Technologies (DET, co-located with DMS)", "Program Committee", "2007", "San Francisco Bay"),
    ("8th SNPD", "Program Committee", "2007", "Qingdao, China"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee", "2007", "French Riviera, France"),
    ("IEEE International Workshop on Testing for Emerging Software Technology (TEST, part of 31st COMPSAC)", "Program Committee", "2007", "&mdash;"),
    ("23rd IEEE ICSM", "Program Committee", "2007", "&mdash;"),
    ("Workshop on Integrating System Environments into Software Testing (WISEST)", "Program Committee", "2007", "&mdash;"),
    ("1st International Workshop on Model-Based Testing and Object-Oriented Systems (M-TOOS, affiliated with OOPSLA)", "Program Committee", "2006", "Portland, OR"),
    ("6th International Conference on Quality Software (QSIC)", "Program Committee", "2006", "Beijing, China"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee", "2006", "Tahiti, French Polynesia"),
    ("21st IEEE/ACM International Conference on Automated Software Engineering (ASE) — Doctoral Symposium", "Program Committee", "2006", "Tokyo, Japan"),
    ("2nd International Workshop on Testing and Quality Assurance for Component-Based Systems (TQACBS, co-located with COMPSAC)", "Program Committee", "2006", "Chicago, IL"),
    ("15th International World Wide Web Conference (WWW) — Web Engineering Track", "Program Committee", "2006", "Edinburgh, Scotland"),
    ("3rd ACIS International Conference on Software Engineering Research, Management &amp; Applications (SERA)", "Program Committee", "2005", "Mount Pleasant, MI"),
    ("1st International Conference on Information and Communication Techniques (ICICT)", "Technical Committee", "2005", "Karachi, Pakistan"),
    ("1st International Workshop on Testing and Quality Assurance for Component-Based Systems (TQACBS, co-located with COMPSAC)", "Program Committee", "2005", "Edinburgh, Scotland"),
    ("14th International World Wide Web Conference (WWW) — Web Engineering Track", "Program Committee", "2005", "Chiba, Japan"),
    ("International Workshop on Frontiers of Information Technology (FIT)", "Program Committee", "2004", "Islamabad, Pakistan"),
    ("1st International Workshop on Web Quality (WQ, co-located with ICWE)", "Program Committee", "2004", "Munich, Germany"),
    ("Net.ObjectDays Workshop — Testing Component-based Systems (TECOS)", "Program Committee", "2004", "Erfurt, Germany"),
    ("11th IEEE Working Conference on Reverse Engineering (WCRE)", "Program Committee", "2004", "Delft, Netherlands"),
    ("5th SNPD", "Program Committee", "2004", "Beijing, China"),
    ("10th International Symposium on the Foundations of Software Engineering (FSE-10)", "Program Committee", "2002", "Charleston, SC"),
]

AGENCY = [
    ("National Academy of Sciences — PEER Program (NSF / USAID / National Academies partnership)", "Panelist", "&mdash;", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2011", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. S&amp;T Cooperative Program (USAID)", "Panelist (CS &amp; IT)", "2010", "USA"),
    ("NSF Research Proposals Review Panel", "Panelist", "2009", "National Science Foundation"),
    ("National Academy of Sciences — Pakistan-U.S. S&amp;T Cooperative Program (USAID)", "Panelist (CS &amp; IT)", "2009", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. S&amp;T Cooperative Program (USAID)", "Panelist (CS &amp; IT)", "2008", "USA"),
    ("NSF SEL CAREER Proposals Review Panel", "Panelist", "2007", "National Science Foundation"),
    ("National Academy of Sciences — Pakistan-U.S. S&amp;T Cooperative Program (USAID)", "Panelist (CS &amp; IT)", "2007", "USA"),
    ("Natural Sciences and Engineering Research Council (NSERC)", "Proposal Reviewer", "2006", "Canada"),
    ("NSF Research Proposals Review Panel", "Panelist", "2004", "National Science Foundation"),
    ("Swedish Research Council (VR)", "Proposal Reviewer", "2003", "Sweden"),
    ("Ph.D. Thesis — Teemu Kanstren (Prof. Ilkka Tervonen, University of Oulu, Finland)", "External Reader", "2009", "Finland"),
    ("Instructors, Department of Software Engineering, Singapore Management University", "Advisor", "2006&ndash;2007", "Singapore"),
    ("Two Master's students in Kabul", "Advisor", "2006&ndash;2007", "Afghanistan"),
]

REVIEWING_JOURNALS = [
    "ACM Transactions on Programming Languages and Systems (TOPLAS)",
    "ACM Transactions on Software Engineering and Methodology (TOSEM)",
    "IEEE Software",
    "IEEE Computer",
    "IEEE Transactions on Software Engineering (TSE)",
    "Parallel Computing",
    "Software: Practice &amp; Experience",
    "Software Testing, Verification &amp; Reliability Journal",
    "Software Quality Journal",
    "Information &amp; Software Technology (Elsevier)",
]

REVIEWING_CONFS = [
    "International Conference on Software Engineering (ICSE)",
    "International Conference on Dependable Systems and Networks",
    "International Conference on Software Engineering, Artificial Intelligence, Networking, Parallel/Distributed Computing (SNPD)",
    "European Conference on Planning (ECP)",
    "International Static Analysis Symposium (SAS)",
    "International Conference on Parallel Architectures and Compilation Techniques (PACT)",
    "International Symposium on the Foundations of Software Engineering (FSE)",
    "Software Technology Conference (STC)",
]

REVIEWING_BOOKS = [
    ("Building Quality into COTS Components &ndash; Testing and Debugging", "Book Reviewer", "&mdash;", "Eds. Sami Beydeda &amp; Volker Gruhn"),
    ("How to Break Security: A Practical Guide to Testing Your Software's Security", "Book Reviewer", "&mdash;", "James Whitaker &amp; Herbert H. Thompson"),
    ("The Information Systems Group Project", "Book Reviewer", "&mdash;", "David A. Deeks, Pearson Education"),
    ("Cambridge University Press — Book Proposal", "Reviewer", "15 Sep 2006", "Cambridge, UK"),
    ("Cambridge University Press — Book Proposal", "Reviewer", "24 Jul 2006", "Cambridge, UK"),
    ("Business Education Publishers Limited — Book Proposal", "Reviewer", "5 Dec 2003", "UK"),
]


def entry_html(name, role, years, org):
    meta_parts = []
    if years and years != "&mdash;":
        meta_parts.append(years)
    if org and org != "&mdash;":
        meta_parts.append(org)
    meta = " &middot; ".join(meta_parts) if meta_parts else "&mdash;"
    return (
        "      <li>\n"
        f'        <span class="pub-title">{name}</span>\n'
        f'        <span class="pub-authors">{role}</span>\n'
        f'        <span class="pub-venue">{meta}</span>\n'
        "      </li>"
    )


def section(heading, rows_html):
    return f"    <h2>{heading}</h2>\n    <ul class=\"pub-list\">\n{rows_html}\n    </ul>"


def flat_section(heading, items):
    lis = "\n".join(f"      <li>{x}</li>" for x in items)
    return f"    <h2>{heading}</h2>\n    <ul class=\"flat-list\">\n{lis}\n    </ul>"


def main():
    body_parts = ["    <h1>Service</h1>"]
    body_parts.append(section("Editorial Boards", "\n".join(entry_html(*e) for e in ED_BOARDS)))
    body_parts.append(section("Conference Leadership &amp; Chair Roles", "\n".join(entry_html(*e) for e in LEADERSHIP)))
    body_parts.append(section("Program Committees", "\n".join(entry_html(*e) for e in PROGRAM_COMMITTEES)))
    body_parts.append(section("Agency Review Panels &amp; External Service", "\n".join(entry_html(*e) for e in AGENCY)))
    body_parts.append(section("Professional Memberships", "\n".join(entry_html(*e) for e in MEMBERSHIPS)))
    body_parts.append(flat_section("Journals I Review For", REVIEWING_JOURNALS))
    body_parts.append(flat_section("Conferences I Review For (outside PC roles)", REVIEWING_CONFS))
    body_parts.append(section("Book &amp; Book-Proposal Reviewing", "\n".join(entry_html(*e) for e in REVIEWING_BOOKS)))

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Service — Atif Memon</title>
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body>
  <aside class="sidebar">
    <img src="assets/photo.jpg" alt="Atif Memon" class="avatar" />
    <h1>Atif Memon</h1>
    <p class="affiliation">Distinguished Engineer, Apple</p>
    <ul class="links">
      <li><a href="https://www.linkedin.com/in/memonatif/" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://scholar.google.com/citations?user=jJPSj0IAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
    </ul>
  </aside>

  <nav class="topnav">
    <a href="index.html">About</a>
    <a href="publications.html">Publications</a>
    <a href="service.html" class="active">Service</a>
    <a href="talks.html">Talks</a>
    <a href="awards.html">Awards</a>
    <a href="writing.html">Writing</a>
  </nav>

  <main>
{chr(10).join(body_parts)}
  </main>
</body>
</html>
"""
    (ROOT / "service.html").write_text(html, encoding="utf-8")
    counts = {
        "editorial": len(ED_BOARDS),
        "leadership": len(LEADERSHIP),
        "pc": len(PROGRAM_COMMITTEES),
        "agency": len(AGENCY),
        "journals_reviewed": len(REVIEWING_JOURNALS),
        "confs_reviewed": len(REVIEWING_CONFS),
        "books_reviewed": len(REVIEWING_BOOKS),
    }
    print(f"service.html written. Counts: {counts}")


if __name__ == "__main__":
    main()
