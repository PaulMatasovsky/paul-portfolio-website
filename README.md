# Portfolio Website — Website 2.0

**Project status:** **In Progress** · **Activity:** Active

I started building [my portfolio website](https://paulmatasovsky.com/) as part of my career transition. The website is where recruiters and hiring managers can get an overview of my work. I use GitHub for the technical details, supporting documents, and evidence behind each project.

I want people to see more than the finished result. I want them to understand the problem I was working on, the decisions I made, and what I learned along the way.

## Current Work

This is where the projects stand right now. Each project has its own documentation, including a more detailed explanation of my work and any AI involvement.

| Area | What it includes | Status | Where to look |
|---|---|---|---|
| Warehouse ETL sorting workbook | Google Sheets workbook used to organize and print warehouse parts reports. The Excel copy has a printing limitation. | **Complete · Maintenance** | [ETL project](Projects/ETL/) |
| Computer Science 050 teaching course | Introductory computer science curriculum and lab preparation. I have not yet published dated classroom evidence here. | **In Progress · Active** | [Teaching project](Projects/Computer_Science_050/) |
| QA Toolkit | Draft website QA checklists, test cases, and templates. I have not completed a verified hands-on audit yet. | **In Progress · Paused** | [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit) |
| Computer Helper (Windows + macOS) — **AI-led** | Local assistant planning, RAG architecture, security boundaries, and an unvalidated Python starter. No target-device or user testing yet. | **In Progress · Active** | [Computer Helper project](Projects/Computer_Helper/) |
| Portfolio website | Live WordPress/Divi site that I am continuing to refine. | **In Progress · Active** | [Live website](https://paulmatasovsky.com/) and [decision records](Documentation/ADRs/) |

I use five workflow stages: **Not Started**, **In Progress**, **Testing / Debugging**, **Blocked**, and **Complete**. An optional activity label—**Active**, **Paused**, or **Maintenance**—shows whether I'm currently working on the project. These are descriptions of the work, not percentages.

The [ETL project](Projects/ETL/) includes business rules, a technical overview, decision records, a learning journal, and screenshots of the process.

This repository is mainly for project and portfolio documentation, not a complete copy of my WordPress website's source code.

## Why Website 2.0?

My first portfolio grew more complicated, and more dependent on AI-generated work, than I intended. Eventually I had trouble separating my own decisions and contributions from what AI had generated.

I decided to rebuild the presentation of my work with a clearer boundary. One of the ideas guiding that decision was *Shibumi*, or understated simplicity. I want to keep what helps someone understand the work and leave out what is just there to look impressive.

## Technology

- **Website:** WordPress and Divi 5.
- **ETL workbook:** Google Sheets for the operational version, with an Excel copy available for download.
- **Computer Science 050:** Scratch, Python, pseudocode, and preparation for an optional lab.
- **Computer Helper (AI-led prototype):** Python, Ollama-compatible local model interface, and example offline Markdown knowledge lookup; target-device setup and tests remain to be done.
- **Documentation:** GitHub and Markdown, with Google Docs used for planning and drafting.

## How I Document the Work

I use [Architecture Decision Records (ADRs)](Documentation/ADRs/) to explain significant website decisions and a [project journal](Documentation/Journal/) to record what I learned or changed my mind about. Documentation for an individual project stays with that project.

My original decision records show how that process developed. I have also used AI to help prepare some later retrospective documentation, which I identify below.

## AI Transparency

AI has had a different role in each project. When I say **human-led**, I mean I did most of the development or creation and used AI in a supporting role. **AI-led** means AI generated most of the implementation or instructional materials based on goals and requirements I provided. These aren't measured percentages, and they do **not** mean AI is running inside a finished tool.

- **ETL (human-led):** I identified the warehouse problem, chose the approach and platform, and built the workbook. AI helped troubleshoot persistent formula errors and later helped with the GitHub documentation. The finished workbook uses spreadsheet formulas; it does not use AI to process reports.
- **QA Toolkit (AI-led):** AI generated the resources as part of a learning exercise. I have not yet completed the hands-on audit or validated results.
- **Computer Science 050 (AI-led drafting):** I set the learning goals, course structure, examples, and teaching approach. AI helps with research, lesson drafts, exercises, and review. I am responsible for the teaching. See the [contribution breakdown](Projects/Computer_Science_050/AI_Collaboration_and_Authorship.md).
- **Computer Helper (AI-led):** I defined the family support problem, safe operating boundaries, and modular specialist approach. AI drafted most planning documents and the first Python source scaffold. No working end-to-end assistant or user testing has been verified. See the [authorship notes](Projects/Computer_Helper/AI_Collaboration_and_Authorship.md).
- **Portfolio website (human-led):** I use AI to learn, plan, critique, troubleshoot, and improve documentation. I still want to be able to explain which work and decisions are mine.

## Next Steps

- Keep the website's project descriptions and GitHub evidence consistent.
- Carry out and document a hands-on QA audit when the site is ready.
- Publish selected teaching materials and dated classroom evidence when I have it.

## Links

- [Portfolio website](https://paulmatasovsky.com/)
- [LinkedIn](https://www.linkedin.com/in/paulmatasovsky)
- [QA Toolkit repository](https://github.com/PaulMatasovsky/qa-toolkit)
