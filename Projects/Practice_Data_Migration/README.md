# Practice Data Migration

*Cleaning a therapy practice's client and appointment export and loading it into a new database*

**Project status:** **In Progress** · **Activity:** Active

A fictional therapy practice is moving from "OldChart EHR" to a new system. The export is messy: mixed date and phone formats, duplicate clients, appointments for clients who don't exist, and a leftover test record. My job is to clean it, load it, and prove nothing was lost.

**All data is synthetic.** Names, IDs, phones (555-01xx), emails (example.com) and addresses are made up.

**Out of scope:** couples and family sessions. Each appointment belongs to one client, and records that look shared are held or flagged for review ([BR-33](Business_Rules.md#hold)).

Supporting them would mean a separate participants table, with one row for each person in each session. Before any session could be assigned, the practice would have to decide:

- **Billing:** which person the claim is billed under, whose insurance and copay apply, and what happens when the partners have different plans.
- **Clinicians:** what to do when the partners have different primary clinicians.
- **Records and privacy:** whether a shared note goes in one chart or both, and how to keep one partner from seeing the other's individual records.
- **Splitting combined records:** which person keeps the original ID and appointment history, and who gets the new one.

Each of these needs the practice's sign-off, so I've left them out rather than guess.

**Not in this export:** clinical notes, diagnoses, treatment plans, uploaded documents, and billing and payment history. A full EHR switch moves these too; this project covers client and appointment records only. Gaps in what the export does have (guardians, policyholders, preferred names and pronouns, recurring series) are handled in [BR-34 to BR-37](Business_Rules.md#missing-from-the-export).

## How It Works

1. **Extract:** [clients.csv](Data/Raw/clients.csv) (198 rows) and [appointments.csv](Data/Raw/appointments.csv) (580 rows).
2. **Transform:** Two templates, one per file, built on the pattern from my [Automated Sorting Template](../ETL/). Each row is loaded, held, rejected or removed under the [business rules](Business_Rules.md), and loaded rows that need follow-up are flagged. The finished templates run in LibreOffice Calc, offline, the way health data should be handled under HIPAA. I'm building them in Google Sheets only so anyone can watch the build and check my progress: [Clients template](https://docs.google.com/spreadsheets/d/15_gGBT6n25xQkl7i5VrP8VnQGjEmgo6A4orhkXxSW0g/edit?usp=sharing) and [Appointments template](https://docs.google.com/spreadsheets/d/17NDmtSCEUpI52yS8T974IYPIfXCzRfhJUM-9XUC5G0g/edit?usp=sharing) (view only). Each handles up to 1,000 rows and checks for overflow.
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
| Flagged (part of Loaded) | | |

## Still to Come

- `.xlsx` downloads of the finished templates
- SQL validation queries and their results
- Test results and screenshots
- Why I chose this project, decision records, and what I learned

## AI Transparency

This is a **human-led** project. I write every formula in the templates and the SQL validation queries, and the business decisions are mine. AI acts as a guide while I build: hints and which functions to look at, not finished formulas.

AI generated the synthetic data and an answer key of the problems planted in it. It also drafted the table setup script, business rules, test cases and this README from my discussions with it; the decisions in them are mine, and I review every change. I'll publish the generator and answer key once I finish, so my results can be checked against them.
