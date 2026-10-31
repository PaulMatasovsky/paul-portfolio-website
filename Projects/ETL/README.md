# Automated Sorting Template

*Spreadsheet-Based ETL Workflow for Inventory Reports*

**Project status:** **Complete** · **Activity:** Maintenance

## Why I Built It

Sorting our warehouse parts reports by hand could take more than an hour, and different part-number formats made ordinary alphabetical sorting unreliable.

I built a spreadsheet to handle that work. My manager can paste in the original report, let the formulas process it, and print one of three sorted reports: Part Number First, Line First, or Category First.

For reports with up to 2,000 parts, preparation went from over an hour to roughly **2–5 minutes**. The Google Sheets version is used in warehouse operations.

## How It Works

1. **Input:** Clear the RawData worksheet and paste in the new report, including its headers.
2. **Processing:** The workbook finds the required columns, cleans and sorts the records, and checks the results.
3. **Output:** Choose the report you need and print it.

## What It Handles

- **Part-number sorting:** Separates the pieces of complex part numbers so they sort more naturally than plain text.
- **Changing column order:** Matches columns by their headings rather than assuming every report has the same layout.
- **Built-in checks:** Looks for missing information, discrepancies, and data that exceeds the template's capacity.

## Workbook and Documentation

- [Google Sheets workbook](https://docs.google.com/spreadsheets/d/1-h7BjpiVBTfXUplCqvHsUb9QcV0sLdSG287sO5V9kcM/edit?usp=sharing) — a copy of the version I developed for warehouse use.
- [Excel version](https://github.com/PaulMatasovsky/paul-portfolio-website/blob/main/Projects/ETL/FINAL_Automated_Sorting_Template.xlsx) — available to download and inspect. I had to adjust some formulas for Excel, and it still prints extra blank rows. The working Google Sheets version does not have that problem.
- [Business Rules](Business_Rules.md) — what the workbook needs to do.
- [Technical Overview](Technical_Overview.md) — how the worksheets carry out those rules.
- [ADRs](ETL_Documentation/ETL_ADR/) — the main decisions behind the workbook.
- [Development History and Retrospective](ETL_Documentation/ETL_Learning_Journal/Retrospective.md) — how I built, tested, and refined it.
- [Screenshots](ETL_Documentation/Supporting_Evidence/Screenshots/) — examples of the data flow and finished reports.

## What I Might Add Later

The workbook is finished for its original purpose, but there are a few ways I could expand it:

- Move the data processing into a database, potentially using SQL.
- Build a more user-friendly dashboard.
- Import source reports automatically instead of relying on copy and paste.

## AI Transparency

I designed and developed the workbook. I used AI to help troubleshoot formula problems that I had already tried to fix through several revisions. AI also helped me prepare, review, and revise the GitHub documentation.

The workbook itself uses spreadsheet formulas and logic. **AI does not run behind the scenes when someone uses the template.**
