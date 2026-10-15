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
    ("Empirical Software Engineering (EMSE)", "Board of Advisors (past)", "through Nov 2020", "Springer"),
    ("Advances in Computers", "Series Editor (past)", "&mdash;", "Elsevier"),
    ("Software Testing, Verification and Reliability (STVR)", "Editorial Board Member (past)", "&mdash;", "Wiley"),
    ("The Open Software Engineering Journal (OSE)", "Editorial Board Member (past)", "&mdash;", "Bentham Science"),
    ("Canadian Journal of Pure and Applied Sciences (CJPAS)", "Editorial Board Member (past)", "&mdash;", "SENRA Academic Publishers"),
    ("IEEE Transactions on Software Engineering", "Guest Associate Editor", "Oct 2003", "&mdash;"),
]

MEMBERSHIPS = [
    ("Association for Computing Machinery (ACM)", "Member", "Aug 1997&ndash;Present", "ACM"),
    ("IEEE Computer Society", "Member", "Aug 1997&ndash;Present", "IEEE"),
]

# Chair, Steering Committee, Organizing, Awards Chair, PC Chair,
# PhD Symposium Chair, Workshops Chair, Session Chair, Panel Member,
# Mentoring Committee, Advisory Board, Publications Chair, Elected committees.
LEADERSHIP = [
    ("IEEE Computer Society — Technical Council on Software Engineering (TCSE)", "Executive Committee Member (Elected)", "2022&ndash;2025", "&mdash;"),
    ("16th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Panelist &mdash; Research, Industry, and Emerging Frontiers", "2025", "Naples, Italy"),
    ("16th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Session Chair &mdash; Testing ML Systems and Fault Localisation", "2025", "Naples, Italy"),
    ("14th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Industry Co-Chair &mdash; Organizing Committee", "2023", "&mdash;"),
    ("14th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Co-Chair &mdash; Industry Track", "2023", "&mdash;"),
    ("International Conference on Software Testing, Verification and Validation (ICST)", "Steering Committee Member", "2020&ndash;2023", "IEEE"),
    ("12th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Technical Program Committee Co-Chair", "2019", "Xi'an, China"),
    ("10th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "General Chair", "2017", "Tokyo, Japan"),
    ("38th International Conference on Software Engineering (ICSE)", "Awards Chair", "2016", "Austin, Texas"),
    ("9th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Panel Member &mdash; PhD Symposium", "2016", "&mdash;"),
    ("8th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Panel Member &mdash; Grand Challenges in Software Testing, Verification &amp; Validation", "2015", "&mdash;"),
    ("8th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Panel Member &mdash; PhD Symposium", "2015", "&mdash;"),
    ("6th IEEE International Workshop on Program Debugging", "Panel Member", "2015", "&mdash;"),
    ("36th International Conference on Software Engineering (ICSE)", "Awards Chair", "2014", "Hyderabad, India"),
    ("35th International Conference on Software Engineering (ICSE)", "Mentoring Committee Member", "2013", "San Francisco, CA"),
    ("6th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; PhD Symposium", "2013", "Luxembourg"),
    ("34th International Conference on Software Engineering (ICSE)", "Mentoring Committee Member", "2012", "Zurich, Switzerland"),
    ("9th Annual International Conference on Mobile Systems, Applications and Services (MobiSys)", "Workshops Co-Chair", "2011", "Bethesda, MD"),
    ("4th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "PhD Symposium Committee Member", "2011", "Berlin, Germany"),
    ("33rd International Conference on Software Engineering (ICSE)", "Mentoring Committee Member", "2011", "Honolulu, HI"),
    ("3rd International Workshop on TESTing Techniques &amp; Experimentation Benchmarks for Event-Driven Software (TESTBEDS)", "General Chair &mdash; GUI and Web Applications", "2011", "Honolulu, HI (co-located with ICSE)"),
    ("Workshop on Experimental Evaluation of Software and Systems in Computer Science (Evaluate)", "Organizing Committee Member", "2010", "Reno/Tahoe, NV (co-located with SPLASH)"),
    ("3rd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Session Chair", "2010", "Paris, France"),
    ("2nd International Workshop on TESTing Techniques &amp; Experimentation Benchmarks for Event-Driven Software (TESTBEDS)", "General Chair &mdash; GUI and Rich Internet Applications", "2010", "Cape Town, South Africa (co-located with ICSE)"),
    ("3rd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "PhD Symposium Chair", "2010", "Paris, France"),
    ("1st International Workshop on TESTing Techniques &amp; Experimentation Benchmarks for Event-Driven Software (TESTBEDS)", "General Chair &mdash; GUI Testing", "2009", "Vancouver, Canada (co-located with ICSE)"),
    ("2nd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "PhD Symposium Chair", "2009", "Denver, CO"),
    ("Proceedings of the 2004 IEEE International Conference on Information Reuse and Integration (IRI)", "Editor", "2004", "Las Vegas, NV"),
    ("IEEE International Conference on Information Reuse and Integration (IRI)", "Publications Chair", "2004", "Las Vegas, NV"),
    ("11th IEEE Working Conference on Reverse Engineering (WCRE)", "Session Chair &mdash; Platform &amp; Language-specific Re-engineering", "2004", "Delft, Netherlands"),
    ("IASTED International Conference on Artificial Intelligence and Applications (AIA)", "Session Chair", "2004", "Innsbruck, Austria"),
    ("Proceedings of the 2003 IEEE International Conference on Information Reuse and Integration (IRI)", "Associate Editor", "2003", "Las Vegas, NV"),
    ("IEEE International Conference on Information Reuse and Integration (IRI)", "Publications Chair", "2003", "Las Vegas, NV"),
    ("10th International Symposium on the Foundations of Software Engineering (FSE-10)", "Session Chair &mdash; Dynamic Program Analysis", "2002", "Charleston, SC"),
    ("15th International Internet &amp; Software Quality Week (QW)", "Advisory Board Member", "2002", "San Francisco, CA"),
    ("14th International Internet &amp; Software Quality Week (QW)", "Advisory Board Member", "2001", "San Francisco, CA"),
]

# All Program Committee memberships, newest first. Each hand-reviewed.
PROGRAM_COMMITTEES = [
    # From researchr.org / LinkedIn — post-CV
    ("ACM International Conference on the Foundations of Software Engineering (FSE)", "Program Committee Member &mdash; Ideas, Visions and Reflections Track", "2026", "ACM"),
    ("ACM International Conference on the Foundations of Software Engineering (FSE)", "Program Committee Member", "2024", "ACM"),
    ("46th International Conference on Software Engineering (ICSE)", "Program Committee Member &mdash; SEIP Track", "2024", "ACM/IEEE"),
    ("ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)", "Program Committee Member &mdash; Industry Papers Track", "2023", "ACM"),
    ("ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)", "Program Committee Member &mdash; Industry Paper Track", "2022", "ACM"),
    ("13th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; Doctoral Symposium", "2020", "&mdash;"),
    ("34th IEEE/ACM International Conference on Automated Software Engineering (ASE)", "Program Committee Member &mdash; Doctoral Symposium", "2019", "&mdash;"),
    ("40th International Conference on Software Engineering (ICSE)", "Program Committee Member &mdash; Technical Papers Track", "2018", "&mdash;"),
    # CV entries
    ("11th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member", "2018", "Västerås, Sweden"),
    ("3rd International Workshop on User Interface Test Automation (INTUITEST)", "Program Committee Member", "2017", "Berlin, Germany"),
    ("8th International Workshop on Automating Test Case Design, Selection and Evaluation (A-TEST)", "Program Committee Member", "2017", "Paderborn, Germany"),
    ("7th International Workshop on Automating Test Case Design, Selection and Evaluation (A-TEST)", "Program Committee Member", "2016", "Seattle, WA"),
    ("9th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; Regular Technical Papers Track", "2016", "&mdash;"),
    ("9th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; Testing Tool Demo Track", "2016", "&mdash;"),
    ("38th International Conference on Software Engineering (ICSE)", "Program Committee Member", "2016", "Austin, Texas"),
    ("1st International Workshop on User Interface Test Automation (INTUITEST)", "Program Committee Member", "2015", "&mdash;"),
    ("6th International Workshop on Automating Test Case Design, Selection and Evaluation (co-located with SEFM 2015)", "Program Committee Member", "2015", "York, UK"),
    ("Workshop on Complex Faults and Failures in Large Software Systems (COUFLESS 2015)", "Program Committee Member", "2015", "Florence, Italy"),
    ("8th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member", "2015", "Graz, Austria"),
    ("10th IEEE/ACM International Workshop on Automation of Software Test (AST)", "Program Committee Member", "2015", "Firenze, Italy"),
    ("1st International Workshop on Complex Faults and Failures in Large Software Systems (co-located with FSE)", "Program Committee Member", "2014", "Hong Kong"),
    ("25th IEEE International Symposium on Software Reliability Engineering (ISSRE)", "Program Committee Member", "2014", "Naples, Italy"),
    ("9th International Conference on the Quality of Information and Communications Technology (QUATIC)", "Program Committee Member &mdash; Quality in Agile Methods Thematic Track", "2014", "Guimarães, Portugal"),
    ("9th International Workshop on Automation of Software Test (AST)", "Program Committee Member", "2014", "Hyderabad, India (co-located with ICSE)"),
    ("7th IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member", "2014", "Cleveland, Ohio"),
    ("7th India Software Engineering Conference (ISEC)", "Program Committee Member", "2014", "Chennai, India"),
    ("5th Workshop on Automated Test Case Design, Selection and Evaluation (ATSE)", "Program Committee Member", "2014", "&mdash;"),
    ("1st International Workshop on Future Internet Testing (FITTEST, co-located with ICTSS)", "Program Committee Member", "2013", "Istanbul, Turkey"),
    ("Joining AcadeMiA and Industry Contributions to testing Automation (JAMAICA) Workshop (co-located with ISSTA)", "Program Committee Member", "2013", "Lugano, Switzerland"),
    ("4th Workshop on Automated Test Case Design, Selection and Evaluation (ATSE)", "Program Committee Member", "2013", "Kraków, Poland"),
    ("13th International Conference on Quality Software (QSIC)", "Program Committee Member", "2013", "Nanjing, China"),
    ("International Workshop on Regression Testing (co-located with ICST)", "Program Committee Member", "2013", "Luxembourg"),
    ("4th International Conference on Runtime Verification (RV)", "Program Committee Member", "2013", "&mdash;"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2013", "&mdash;"),
    ("8th International Conference on the Quality of Information and Communications Technology (QUATIC)", "Program Committee Member &mdash; Main Track", "2012", "Lisbon, Portugal"),
    ("2nd International Workshop on End-to-end Test Script Engineering (ETSE, co-located with ISSTA)", "Program Committee Member", "2012", "&mdash;"),
    ("3rd International Conference on Runtime Verification (RV)", "Program Committee Member", "2012", "&mdash;"),
    ("8th International Conference on the Quality of Information and Communications Technology (QUATIC)", "Program Committee Member &mdash; Quality in Agile Methods Thematic Track", "2012", "Porto, Portugal"),
    ("7th International Workshop on Automation of Software Test (AST)", "Program Committee Member", "2012", "Zurich, Switzerland (co-located with ICSE)"),
    ("IEEE 20th International Requirements Engineering Conference", "Program Committee Member &mdash; Industry Track", "2012", "Chicago, USA"),
    ("2nd International Workshop on Regression Testing (co-located with ICST)", "Program Committee Member", "2012", "Montreal, Canada"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2012", "Montreal, Canada"),
    ("12th International Conference on Quality Software (QSIC)", "Program Committee Member", "2012", "Xi'an, China"),
    ("27th IEEE International Conference on Software Maintenance (ICSM)", "Program Committee Member &mdash; Industry Track", "2011", "Williamsburg, VA"),
    ("5th International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Program Committee Member", "2011", "Lisbon, Portugal"),
    ("6th IEEE International Workshop on Automation of Software Test (AST)", "Program Committee Member", "2011", "Honolulu, HI (co-located with ICSE)"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2011", "Berlin, Germany"),
    ("3rd International Conference on Advances in System Testing and Validation Lifecycle (VALID)", "Program Committee Member", "2011", "Barcelona, Spain"),
    ("11th International Conference on Quality Software (QSIC)", "Program Committee Member", "2011", "Madrid, Spain"),
    ("26th IEEE International Conference on Software Maintenance (ICSM)", "Program Committee Member &mdash; Early Research Achievements Track", "2010", "Timisoara, Romania"),
    ("IEEE/ACIS International Conference on Computer and Information Science (ICIS)", "Program Committee Member", "2010", "Yamagata, Japan"),
    ("4th India Software Engineering Conference (ISEC)", "Program Committee Member", "2010", "Thiruvananthapuram, India"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2010", "Windsor, UK"),
    ("7th International Conference on the Quality of Information and Communications Technology (QUATIC)", "Program Committee Member &mdash; Quality in Agile Methods Thematic Track", "2010", "Porto, Portugal"),
    ("21st IEEE International Symposium on Software Reliability Engineering (ISSRE)", "Program Committee Member", "2010", "San Jose, CA"),
    ("5th International Workshop on Automation of Software Test (AST)", "Program Committee Member", "2010", "Cape Town, South Africa (co-located with ICSE)"),
    ("5th International Conference on Software and Data Technologies (ICSOFT)", "Program Committee Member", "2010", "&mdash;"),
    ("4th International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Program Committee Member", "2010", "Florence, Italy"),
    ("8th ACIS International Conference on Software Engineering Research, Management and Applications (SERA)", "Program Committee Member", "2010", "&mdash;"),
    ("2nd International Conference on Advances in System Testing and Validation Lifecycle (VALID)", "Program Committee Member", "2010", "Nice, France"),
    ("International Conference on Information Science and Applications (ICISA)", "Program Committee Member", "2010", "Seoul, Korea"),
    ("2nd International Conference on Intensive Applications and Services (INTENSIVE)", "Program Committee Member", "2010", "Cancun, Mexico"),
    ("10th International Conference on Quality Software (QSIC)", "Program Committee Member", "2010", "Zhangjiajie, China"),
    ("3rd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member", "2010", "&mdash;"),
    ("3rd India Software Engineering Conference (ISEC)", "Program Committee Member", "2010", "Mysore, India"),
    ("25th IEEE International Conference on Software Maintenance (ICSM)", "Program Committee Member", "2009", "Edmonton, Alberta, Canada"),
    ("18th International World Wide Web Conference (WWW)", "Program Committee Member", "2009", "Madrid, Spain"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2009", "Windsor, UK"),
    ("1st International Conference on Advances in System Testing and Validation Lifecycle (VALID)", "Program Committee Member", "2009", "Porto, Portugal"),
    ("4th International Conference on Software Engineering Advances (ICSEA)", "Program Committee Member", "2009", "Porto, Portugal"),
    ("3rd International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Program Committee Member", "2009", "Sliema, Malta"),
    ("10th ACIS International Conference on Software Engineering, AI, Networking, and Parallel/Distributed Computing (SNPD)", "Program Committee Member", "2009", "&mdash;"),
    ("9th International Conference on Quality Software (QSIC)", "Program Committee Member", "2009", "Jeju, Korea"),
    ("Software Engineering Symposium at the World Congress on Computer Science and Information Engineering", "Program Committee Member", "2009", "Los Angeles / Anaheim"),
    ("8th IEEE/ACIS International Conference on Computer and Information Science (ICIS)", "Program Committee Member", "2009", "Shanghai, China"),
    ("4th International Conference on Software and Data Technologies (ICSOFT)", "Program Committee Member", "2009", "&mdash;"),
    ("7th ACIS International Conference on Software Engineering Research, Management and Applications (SERA)", "Program Committee Member", "2009", "Haikou, China"),
    ("1st International Conference on Intensive Applications and Services (INTENSIVE)", "Program Committee Member", "2009", "Valencia, Spain"),
    ("1st International Workshop on Web Testing (WebTest)", "Program Committee Member", "2009", "Denver, CO"),
    ("2nd IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Technical Program Committee Member", "2009", "&mdash;"),
    ("2nd India Software Engineering Conference (ISEC)", "Program Committee Member", "2009", "Pune, India"),
    ("30th International Conference on Software Engineering (ICSE)", "Program Committee Member", "2008", "Leipzig, Germany"),
    ("Testing: Academic &amp; Industrial Conference — Practice and Research Techniques (TAIC-PART)", "Program Committee Member", "2008", "Windsor, UK"),
    ("24th IEEE International Conference on Software Maintenance (ICSM)", "Program Committee Member", "2008", "Beijing, China"),
    ("Software Engineering Research, Management and Applications Conference (SERA)", "Program Committee Member", "2008", "Prague"),
    ("3rd International Conference on Software and Data Technologies (ICSOFT)", "Program Committee Member", "2008", "Porto, Portugal"),
    ("9th International Conference on Software Engineering, Artificial Intelligence, Networking, and Parallel/Distributed Computing (SNPD)", "Program Committee Member", "2008", "Phuket, Thailand"),
    ("8th International Conference on Quality Software (QSIC)", "Program Committee Member", "2008", "Oxford, UK"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee Member", "2008", "Sliema, Malta"),
    ("7th IEEE/ACIS International Conference on Computer and Information Science (ICIS)", "Program Committee Member", "2008", "Portland, OR"),
    ("2nd International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Technical Program Committee Member", "2008", "Valencia, Spain"),
    ("2nd International Workshop on Software Test Evaluation (STEV, co-located with ICST)", "Program Committee Member", "2008", "Lillehammer, Norway"),
    ("17th International World Wide Web Conference (WWW)", "Program Committee Member &mdash; Web Engineering Track", "2008", "Beijing, China"),
    ("1st IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; Industry Track", "2008", "Lillehammer, Norway"),
    ("1st IEEE International Conference on Software Testing, Verification and Validation (ICST)", "Program Committee Member &mdash; Research Track", "2008", "Lillehammer, Norway"),
    ("International Conference on Advanced Engineering Computing and Applications in Sciences (ADVCOMP)", "Technical Program Committee Member", "2007", "Tahiti, French Polynesia"),
    ("1st International Workshop on Software Test Evaluation (STEV)", "Program Committee Member", "2007", "Portland, OR"),
    ("7th International Conference on Quality Software (QSIC)", "Program Committee Member", "2007", "Portland, OR"),
    ("5th IEEE International Conference on Software Engineering Research, Management and Applications (SERA)", "Program Committee Member", "2007", "Busan, Korea"),
    ("International Workshop on Distance Education Technologies (DET, co-located with DMS)", "Program Committee Member", "2007", "San Francisco Bay"),
    ("8th International Conference on Software Engineering, Artificial Intelligence, Networking, and Parallel/Distributed Computing (SNPD)", "Program Committee Member", "2007", "Qingdao, China"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee Member", "2007", "French Riviera, France"),
    ("IEEE International Workshop on Testing for Emerging Software Technology (TEST, part of 31st COMPSAC)", "Program Committee Member", "2007", "Beijing, China"),
    ("23rd IEEE International Conference on Software Maintenance (ICSM)", "Program Committee Member", "2007", "&mdash;"),
    ("Workshop on Integrating System Environments into Software Testing (WISEST)", "Program Committee Member", "2007", "&mdash;"),
    ("1st International Workshop on Model-Based Testing and Object-Oriented Systems (M-TOOS, affiliated with OOPSLA)", "Program Committee Member", "2006", "Portland, OR"),
    ("6th International Conference on Quality Software (QSIC)", "Program Committee Member", "2006", "Beijing, China"),
    ("International Conference on Software Engineering Advances (ICSEA)", "Technical Program Committee Member", "2006", "Tahiti, French Polynesia"),
    ("21st IEEE/ACM International Conference on Automated Software Engineering (ASE)", "Program Committee Member &mdash; Doctoral Symposium", "2006", "Tokyo, Japan"),
    ("2nd International Workshop on Testing and Quality Assurance for Component-Based Systems (TQACBS, co-located with COMPSAC)", "Program Committee Member", "2006", "Chicago, IL"),
    ("15th International World Wide Web Conference (WWW)", "Program Committee Member &mdash; Web Engineering Track", "2006", "Edinburgh, Scotland"),
    ("3rd ACIS International Conference on Software Engineering Research, Management &amp; Applications (SERA)", "Program Committee Member", "2005", "Mount Pleasant, MI"),
    ("1st International Conference on Information and Communication Techniques (ICICT)", "Program Committee Member", "2005", "Karachi, Pakistan"),
    ("1st International Workshop on Testing and Quality Assurance for Component-Based Systems (TQACBS, co-located with COMPSAC)", "Program Committee Member", "2005", "Edinburgh, Scotland"),
    ("14th International World Wide Web Conference (WWW)", "Program Committee Member &mdash; Web Engineering Track", "2005", "Chiba, Japan"),
    ("International Workshop on Frontiers of Information Technology (FIT)", "Program Committee Member", "2004", "Islamabad, Pakistan"),
    ("1st International Workshop on Web Quality (WQ, co-located with ICWE)", "Program Committee Member", "2004", "Munich, Germany"),
    ("Net.ObjectDays Workshop — Testing Component-based Systems (TECOS)", "Program Committee Member", "2004", "Erfurt, Germany"),
    ("11th IEEE Working Conference on Reverse Engineering (WCRE)", "Program Committee Member", "2004", "Delft, Netherlands"),
    ("5th International Conference on Software Engineering, Artificial Intelligence, Networking, and Parallel/Distributed Computing (SNPD)", "Program Committee Member", "2004", "Beijing, China"),
    ("10th International Symposium on the Foundations of Software Engineering (FSE-10)", "Program Committee Member", "2002", "Charleston, SC"),
]

AGENCY = [
    ("National Academy of Sciences — PEER Program (NSF / USAID / National Academies partnership)", "Panelist (one-time)", "&mdash;", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2011", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2010", "USA"),
    ("NSF Research Proposals Review Panel", "Panelist", "2009", "National Science Foundation"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2009", "USA"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2008", "USA"),
    ("NSF SEL CAREER Proposals Review Panel", "Panelist", "2007", "National Science Foundation"),
    ("National Academy of Sciences — Pakistan-U.S. Science and Technology Cooperative Program (USAID)", "Panelist (Computer Science &amp; Information Technology)", "2007", "USA"),
    ("Natural Sciences and Engineering Research Council (NSERC)", "Proposal Reviewer", "2006", "Canada"),
    ("NSF Research Proposals Review Panel", "Panelist", "2004", "National Science Foundation"),
    ("Swedish Research Council (VR)", "Proposal Reviewer", "2003", "Sweden"),
    ("Ph.D. Thesis — Teemu Kanstren (Prof. Ilkka Tervonen, University of Oulu, Finland)", "External Reader", "2009", "&mdash;"),
    ("Instructors, Department of Software Engineering, Singapore Management University", "Advisor", "2006&ndash;2007", "&mdash;"),
    ("M.S. student advising (Kabul, Afghanistan)", "Advisor", "2006&ndash;2007", "&mdash;"),
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
    ("Building Quality into COTS Components &ndash; Testing and Debugging (eds. Sami Beydeda &amp; Volker Gruhn)", "Book Reviewer", "&mdash;", "&mdash;"),
    ("How to Break Security: A Practical Guide to Testing Your Software's Security (James Whitaker &amp; Herbert H. Thompson)", "Book Reviewer", "&mdash;", "&mdash;"),
    ("The Information Systems Group Project (David A. Deeks, Pearson Education)", "Book Reviewer", "&mdash;", "&mdash;"),
    ("Cambridge University Press — Book Proposal", "Book Proposal Reviewer", "15 Sep 2006", "Cambridge, UK"),
    ("Cambridge University Press — Book Proposal", "Book Proposal Reviewer", "24 Jul 2006", "Cambridge, UK"),
    ("Business Education Publishers Limited — Book Proposal", "Book Proposal Reviewer", "5 Dec 2003", "UK"),
]


def entry_html(name, role, years, org):
    """Render one service entry.

    Layout: role (bold) -> name (grey) -> meta (italic).
    This re-orders the visual hierarchy so the role is the strongest
    signal, with the body/conference name as subtitle.
    """
    meta_parts = []
    if years and years != "&mdash;":
        meta_parts.append(years)
    if org and org != "&mdash;":
        meta_parts.append(org)
    meta = " &middot; ".join(meta_parts) if meta_parts else "&mdash;"
    return (
        "      <li>\n"
        f'        <span class="pub-title">{role}</span>\n'
        f'        <span class="pub-authors">{name}</span>\n'
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
      <li><a href="https://dblp.org/pid/m/AtifMMemon.html" target="_blank" rel="noopener">DBLP</a></li>
      <li><a href="https://www.semanticscholar.org/author/144660366" target="_blank" rel="noopener">Semantic Scholar</a></li>
    </ul>  </aside>

  <nav class="topnav">
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
