# Practice Data Migration

*Cleaning a therapy practice's client and appointment export and loading it into a new database*

**Project status:** **In Progress** · **Activity:** Active

A fictional therapy practice is moving from "OldChart EHR" to a new system. The export is messy: mixed date and phone formats, duplicate clients, appointments for clients who don't exist, and a leftover test record. My job is to clean it, load it, and prove nothing was lost.

**All data is synthetic.** Names, IDs, phones (555-01xx), emails (example.com) and addresses are made up.

## How It Works

1. **Extract:** [clients.csv](Data/Raw/clients.csv) (198 rows) and [appointments.csv](Data/Raw/appointments.csv) (580 rows).
2. **Transform:** Two LibreOffice Calc workbooks built on the pattern from my [Automated Sorting Template](../ETL/). Each row is fixed, flagged, held, rejected or removed under the [business rules](Business_Rules.md). The cleaning happens offline, as health data would be handled under HIPAA.
3. **Load:** Into PostgreSQL on Supabase, clients first ([table setup](SQL/01_create_tables.sql)).
4. **Validate:** Row counts must reconcile, and SQL checks look for duplicates, orphans and broken rules ([test cases](Testing/Test-Cases.md)).

## Results

*(to fill in once tested)*

| | Clients | Appointments |
|---|---|---|
| Rows in export | 198 | 580 |
| Loaded | | |
| Held | | |
| Rejected | | |
| Removed | | |
| Flagged for follow-up | | |

## Still to Come

- Clients and Appointments templates (published as `.xlsx`)
- SQL validation queries and their results
- Test results and screenshots
- Why I chose this project, decision records, and what I learned

## AI Transparency

This is a **human-led** project. I'm building the workbooks and writing the SQL validation queries, and the business decisions are mine.

AI generated the synthetic data and an answer key of the problems planted in it, and drafted the table setup script, business rules, test cases and this README. I'll publish the generator and answer key once I finish, so my results can be checked against them.
