# Portfolio Website — Website 2.5

**Project status:** **In Progress** · **Activity:** Active

I started building [my portfolio website](https://paulmatasovsky.com/) as part of my career transition. The website is where recruiters and hiring managers can get an overview of my work. I use GitHub for the technical details, supporting documents, and evidence behind each project.

I want people to see more than the finished result. I want them to understand the problem I was working on, the decisions I made, and what I learned along the way.

## Current Work

This is where the projects stand right now. Each project has its own documentation, including a more detailed explanation of my work and any AI involvement.

| Area | What it includes | Status | Where to look |
|---|---|---|---|
| Automated Sorting Template | Google Sheets workbook used to organize and print warehouse parts reports. The Excel copy has a printing issue that prints extra white space at the end of the document. | **Complete · Maintenance** | [ETL project](Projects/ETL/) |
| Practice Data Migration | Cleaning a fictional therapy practice's client and appointment export offline in LibreOffice Calc and loading it into PostgreSQL on Supabase. Synthetic data; AI generated the test files and setup script. | **In Progress · Active** | [Practice Data Migration](Projects/Practice_Data_Migration/) |
| SQL Refresher — Inventory Data Checks — **AI-led** | Small SQLite practice project using fictional inventory data; no database or queries implemented yet. | **In Progress · Active** | [SQL Refresher](Projects/SQL_Refresher/) |
| Computer Science 050 teaching course | Introductory computer science curriculum and teaching, with weekly instructor teaching records. AI-led curriculum; human-led classroom instruction. | **In Progress · Active** | [Teaching project](Projects/Computer_Science_050/) |
| QA Toolkit | Draft website QA checklists, test cases, and templates. I have not completed a verified hands-on audit yet. | **In Progress · Active** | [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit) and [QA audit results](Projects/QA_Audits/) |
| Computer Helper (Windows + macOS) — **AI-led** | Local help assistant with a modular design, offline reference notes, and untested Python starter code. | **In Progress · Active** | [Computer Helper project](Projects/Computer_Helper/) |
| Portfolio website — **AI-led** | Live WordPress/Divi site, now Website 2.5 (published November 14, 2026). AI-led visual design and documentation; human-led content and structure. | **In Progress · Active** | [Live website](https://paulmatasovsky.com/), [decision records](Documentation/ADRs/), and [who did what](Documentation/AI_Collaboration_and_Authorship.md) |

I use five workflow stages: **Not Started**, **In Progress**, **Testing / Debugging**, **Blocked**, and **Complete**. An optional activity label—**Active**, **Paused**, or **Maintenance**—shows whether I'm currently working on the project. These are descriptions of the work, not percentages.

The [ETL project](Projects/ETL/) includes business rules, a technical overview, decision records, a learning journal, and screenshots of the process.

This repository is mainly for project and portfolio documentation, not a complete copy of my WordPress website's source code.

## Why Website 2.0?

My first portfolio grew more complicated, and more dependent on AI-generated work, than I intended. Eventually I had trouble separating my own decisions and contributions from what AI had generated.

I decided to rebuild the presentation of my work with a clearer boundary. One of the ideas guiding that decision was *Shibumi*, or understated simplicity. I want to keep what helps someone understand the work and leave out what is just there to look impressive.

## Website 2.5

Website 2.0 drew that boundary, but I wasn't happy with how the site looked. In November 2026 I had AI redesign the appearance: colors, fonts, spacing, and layout. The pages, the structure, and the text are still mine.

That moves the website back under AI-led. The [authorship breakdown](Documentation/AI_Collaboration_and_Authorship.md) covers the version history and who did what. The redesign went live on November 14, 2026. AI drafted this section.

## Technology

- **Website:** WordPress and Divi 5.
- **ETL workbook:** Google Sheets for the operational version, with an Excel copy available for download.
- **Computer Science 050:** Scratch, Python, pseudocode, and preparation for an optional lab.
- **Computer Helper (AI-led):** Python, Ollama, and an early offline help-note search; not yet tested on the family computers.
- **Documentation:** GitHub and Markdown, with Google Docs used for planning and drafting.

## How I Document the Work

I keep [decision records](Documentation/ADRs/) for important choices and a [project journal](Documentation/Journal/) for what I learned. Each project has its own technical notes and evidence.

I follow these [GitHub writing principles](Documentation/GitHub_Writing_Principles.md): use plain language, practice Shibumi, and keep the AI disclosure and project status accurate. AI helped draft some retrospective documentation, and I've identified that work where it appears.

## AI Transparency

I use AI across my portfolio projects. The ETL workbook and the Practice Data Migration are human-led. The SQL refresher, QA Toolkit, Computer Science 050 curriculum, and Computer Helper are AI-led. The portfolio website was human-led in version 2.0 and is AI-led from version 2.5: AI did the visual design and drafted most of the documentation, while the content and structure are mine.

## Next Steps

- Write ADR-002 on handing the visual design to AI.
- Keep the website's project descriptions and GitHub evidence consistent.
- Carry out and document a hands-on QA audit of the redesigned site.
- Continue to publish selected teaching materials and dated classroom evidence as I get time.

## Links

- [Portfolio website](https://paulmatasovsky.com/)
- [LinkedIn](https://www.linkedin.com/in/paulmatasovsky)
- [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit)
