# Portfolio Website — Website 2.0

**Project status:** **In Progress** · **Activity:** Active

This repository supports my [personal portfolio website](https://paulmatasovsky.com/), which I am developing as part of a career transition. The website introduces my work to recruiters and hiring managers; GitHub holds the more technical details, documentation, and project evidence.

I want the portfolio to show not just what I built, but the problems I worked on, the decisions I made, and what I learned.

## Current Work

The projects below show what is available today, what each deliverable does, and what remains to be completed. Authorship and AI contributions are described separately in [AI Transparency](#ai-transparency).

| Area | Deliverable or current scope | Status | Where to look |
|---|---|---|---|
| Warehouse ETL sorting workbook | Google Sheets workbook used to organize and print warehouse parts reports. The Excel copy has a printing limitation. | **Complete · Maintenance** | [ETL project](Projects/ETL/) |
| Computer Science 050 teaching course | Introductory computer science curriculum and lab preparation; dated classroom evidence has not yet been published here. | **In Progress · Active** | [Teaching project](Projects/Computer_Science_050/) |
| QA Toolkit | Draft website QA checklists, test cases, and templates; no verified hands-on audit yet. | **In Progress · Paused** | [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit) |
| Computer Helper (Windows + macOS) | User requirements, design proposals, and safety boundaries; no working prototype or user tests. | **Not Started (implementation) · Active (planning)** | [Computer Helper project](Projects/Computer_Helper/) |
| Portfolio website | Live WordPress/Divi site being refined to present completed work and clear project limitations. | **In Progress · Active** | [Live website](https://paulmatasovsky.com/) and [decision records](Documentation/ADRs/) |

**Workflow stages:** Not Started (implementation has not begun), In Progress (work underway), Testing / Debugging (actively validating), Blocked (cannot proceed), and Complete (usable deliverable finished). **Activity** is a separate optional label: Active, Paused, or Maintenance. The stage describes the work, not a percentage.

The ETL documentation includes [business rules](Projects/ETL/Business_Rules.md), a [technical overview](Projects/ETL/Technical_Overview.md), [architectural decisions](Projects/ETL/ETL_Documentation/ETL_ADR/), a [retrospective journal](Projects/ETL/ETL_Documentation/ETL_Learning_Journal/Retrospective.md), and [screenshots](Projects/ETL/ETL_Documentation/Supporting_Evidence/Screenshots/).

This repository is primarily a place for portfolio and project documentation; it is **not a full export of the WordPress website's source code**.

## Why Website 2.0?

My first portfolio grew more complex and more AI-driven than I intended. I had trouble separating my own decisions and contributions from AI-generated work.

I started Website 2.0 to simplify the presentation and make that distinction clearer. I use *Shibumi*—purposeful simplicity—as a guide: keep what helps the reader understand the work, and avoid adding features or documentation simply to make the site look more elaborate.

## Technology

- **Website:** WordPress and Divi 5.
- **ETL project:** Google Sheets for the operational workbook; a downloadable Microsoft Excel version is also available.
- **Teaching project:** Scratch, Python, pseudocode, and preparation for an optional computer lab.
- **Project documentation:** GitHub and Markdown, with Google Docs used for planning and drafting.

## Documentation Approach

I use [Architecture Decision Records (ADRs)](Documentation/ADRs/) for meaningful website-level decisions and a [project journal](Documentation/Journal/) for learning and changes in perspective. Project-specific documentation stays with the project it describes.

Dated original decision records preserve how the documentation process developed over time. The distinct use of AI in later retrospective documentation is disclosed below.

## AI Transparency

AI has contributed in different ways across my projects. These are descriptions of who created or reviewed the material, **not claims that AI operates the finished tools**.

For authorship, **human-led** means I performed most of the development or creation while using AI in a limited supporting role. **AI-led** means AI generated most of the implementation or instructional materials under requirements and direction I provided. These are qualitative descriptions, not measured percentages; each project explains the actual contributions.

- **ETL (human-led):** I identified the warehouse problem, made the operational and platform decisions, and developed the spreadsheet. AI helped me troubleshoot specific persistent formula errors during development and later helped write and streamline GitHub documentation. The finished ETL workbook runs through spreadsheet formulas; **no AI runs behind the scenes when it processes a report**.
- **QA Toolkit (AI-led):** The resources were generated by AI as a learning exercise. I have not yet completed or validated the planned hands-on QA audit.
- **Computer Science 050 (AI-led drafting):** I direct the learning goals, course structure, examples, and teaching; AI has a substantial role in curriculum research, lesson drafting, exercise generation, and review. See the [contribution breakdown](Projects/Computer_Science_050/AI_Collaboration_and_Authorship.md).
- **Computer Helper (human-directed, AI-drafted planning):** I set the intended user's needs, platform scope, and limits on navigation and password access. AI generated the initial project documents and candidate architecture. No application has been built or tested; see the [authorship breakdown](Projects/Computer_Helper/AI_Collaboration_and_Authorship.md).
- **Portfolio website (human-led):** I use AI for learning, planning, critique, troubleshooting, and editorial support. The goal is to keep my own decisions and contributions distinguishable from AI's work.

## Next Steps

- Keep the portfolio website's project descriptions and links aligned with the evidence on GitHub.
- Carry out and document a hands-on QA audit when the site is ready.
- Publish selected teaching artifacts and dated delivery evidence as they become available.

## Links

- [Portfolio website](https://paulmatasovsky.com/)
- [LinkedIn](https://www.linkedin.com/in/paulmatasovsky)
- [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit)
