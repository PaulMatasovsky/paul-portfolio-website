# Practice Data Migration

*Cleaning a therapy practice's client and appointment export and loading it into a new database*

**Project status:** **In Progress** · **Activity:** Active

> **Outline.** AI drafted this README's structure. Sections marked *(to write)* are mine to fill in once the work is done. Nothing below claims a result I haven't produced yet.

## Why I'm Building It

A fictional therapy practice is leaving an old practice-management system, "OldChart EHR," for a new one. The export is messy: mixed date and phone formats, duplicate clients, appointments pointing to clients who don't exist, and test records left behind. Nothing can be loaded until it's cleaned and checked.

*(to write: a sentence or two in my own words about why this project, e.g. how it relates to the client imports I did at Creditor Advocates)*

**All data is synthetic.** Every name, ID, phone number (555-01xx), email (example.com) and address is made up. No real client information is used.

## How It Works

1. **Extract:** Two CSV exports from OldChart: [clients.csv](Data/Raw/clients.csv) (198 rows) and [appointments.csv](Data/Raw/appointments.csv) (580 rows).
2. **Transform:** Two LibreOffice Calc workbooks, one per file, built from the pattern in my [Automated Sorting Template](../ETL/): match columns by header, pull them into a fixed order, clean them, flag problems, and output only the rows that pass. The cleaning happens offline, the way health data would be handled under HIPAA. I'll publish the templates as Excel files, using only formulas that work in both.
3. **Load:** Import the clean CSVs into PostgreSQL on Supabase, clients first, then appointments.
4. **Validate:** SQL checks that compare counts and relationships between the source, the workbooks and the database.

## Business Rules

[Business Rules](Business_Rules.md) — what gets fixed, flagged, rejected or removed, and why. A few decisions are still open.

## Workbooks

- *(to add: Clients template, .xlsx)*
- *(to add: Appointments template, .xlsx)*

*(to write: a short tour of the tabs: RawData, HeaderMap, Step1, cleaning, flags, Final, QA)*

## Database

- [01_create_tables.sql](SQL/01_create_tables.sql) creates the `clients` and `appointments` tables with keys and checks.
- *(to add: my validation queries and their results)*

## Results

*(to write once tested: rows in, rows loaded, rows rejected and why, and whether the SQL checks matched the QA tab)*

| | Clients | Appointments |
|---|---|---|
| Rows in export | 198 | 580 |
| Rows loaded | | |
| Rows rejected or removed | | |
| Rows flagged for follow-up | | |

## Testing

*(to write: test plan and test cases, using templates from my [QA Toolkit](https://github.com/PaulMatasovsky/qa-toolkit))*

## Screenshots

*(to add: Documentation/Screenshots/)*

## What I Learned

*(to write)*

## AI Transparency

This is a **human-led** project. I'm designing the pipeline, building the workbooks and writing the SQL validation queries.

AI generated the synthetic CSV files and an answer key of the problems planted in them, drafted the table setup script, and drafted this README outline. I'll publish the data generator and answer key after I finish, so you can check my results against them.
