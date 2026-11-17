# Test Cases

- **Feature / area:** Practice Data Migration: LibreOffice Calc templates, Supabase load
- **Author / date:** Paul Matasovsky, 2026-11-17. AI drafted these cases from our discussion; I reviewed them.
- **Environment:** LibreOffice Calc (offline), Excel-format copies of the templates, Supabase (PostgreSQL)

None of these have been run yet. Results go in the execution log, not here.

---

## TC-001: Every row is accounted for

- **Requirement or reason:** BR-28. Rows in = loaded + held + rejected + removed, for each file.
- **Preconditions and test data:** `clients.csv` and `appointments.csv` imported into their templates.

| Step | Action | Expected result |
|---|---|---|
| 1 | Note the RawData row count for each file (not counting the header). | Clients 198, appointments 580. |
| 2 | Read the counts on the QA tab. | Final + held + rejected + removed equals the RawData count for each file. |
| 3 | Make the counts disagree on purpose by deleting one row from Final's source range, then undo. | The QA tab shows a mismatch while the row is missing, and matches again after undo. |

## TC-002: Columns are found by heading, not position

- **Requirement or reason:** BR-02. The export can change column order or heading style.
- **Preconditions and test data:** Clients template with `clients.csv` loaded; Final saved as a reference copy.

| Step | Action | Expected result |
|---|---|---|
| 1 | Move two columns in RawData to new positions. | Final is unchanged. |
| 2 | Rename a heading to a style variant (for example `Last Name` to `last_name`). | Final is unchanged. |
| 3 | Rename a required heading to something unrecognized. | An error shows; Final does not quietly output incomplete data. |

## TC-003: Duplicates are removed or flagged

- **Requirement or reason:** BR-21, BR-22.
- **Preconditions and test data:** Clients template with `clients.csv` loaded.

| Step | Action | Expected result |
|---|---|---|
| 1 | Check the exact duplicate rows. | One copy stays; the extras are removed and counted. |
| 2 | Check clients with the same name and birth date under different IDs. | Both rows are flagged; neither is merged or dropped. |
| 3 | Check the client ID that belongs to two different people. | The first row loads; the later row is held with a reason asking for a new ID (BR-23). |

## TC-004: Orphan appointments are rejected

- **Requirement or reason:** BR-25.
- **Preconditions and test data:** Appointments template loaded; client-ID tab filled from the clients Final.

| Step | Action | Expected result |
|---|---|---|
| 1 | Check appointments whose client ID isn't on the client-ID tab. | Each is rejected with an orphan reason. |
| 2 | Check client IDs written differently (`42`, `C-42`, `c0042`). | They match the right client after cleaning, not counted as orphans. |
| 3 | Check appointments for clients who were rejected or held. | Each is held, not rejected, with a reason naming the client to fix (BR-26). |

## TC-005: Values at the limits

- **Requirement or reason:** BR-16, BR-17.
- **Preconditions and test data:** Appointments and clients templates; add test rows, then remove them afterward.

| Step | Action | Expected result |
|---|---|---|
| 1 | Enter durations of 14, 15, 180 and 181 minutes. | 15 and 180 pass; 14 and 181 are rejected. |
| 2 | Enter a birth date of today, then tomorrow. | Today passes; tomorrow is rejected. |
| 3 | Enter a date that doesn't exist, such as 06/31/2026. | Rejected. |

## TC-006: Same input, same output

- **Requirement or reason:** The template should give identical results every time.
- **Preconditions and test data:** Clients template with `clients.csv` loaded; Final saved as a reference copy.

| Step | Action | Expected result |
|---|---|---|
| 1 | Close the template without saving, reopen it, and import the same file again. | RawData starts empty; Final matches the reference copy exactly. |

## TC-007: The database refuses bad data

- **Requirement or reason:** The database checks are a second safety net.
- **Preconditions and test data:** Supabase tables created with `01_create_tables.sql`.

| Step | Action | Expected result |
|---|---|---|
| 1 | Insert an appointment for a client ID that doesn't exist. | Refused by the foreign key. |
| 2 | Insert a client with a status of `Pending`. | Refused by the status check. |

## TC-008: Records match field by field

- **Requirement or reason:** Counts can match while values are wrong.
- **Preconditions and test data:** Both tables loaded in Supabase.

| Step | Action | Expected result |
|---|---|---|
| 1 | Pick 10 client IDs at random and compare each field in the source, Final and Supabase. | Every field matches after the cleaning rules are applied. |

## TC-009: SQL counts match the QA tab

- **Requirement or reason:** The database and the spreadsheet should agree.
- **Preconditions and test data:** Both tables loaded; validation queries written.

| Step | Action | Expected result |
|---|---|---|
| 1 | Count rows in each table. | Matches the Final counts on each QA tab. |
| 2 | Run each validation query. | Each returns 0 rows. |

## TC-010: Templates survive saving as Excel files

- **Requirement or reason:** The templates are published to GitHub as `.xlsx`, so every formula must still work after converting from LibreOffice.
- **Preconditions and test data:** Both finished templates, cleared of data.

| Step | Action | Expected result |
|---|---|---|
| 1 | Save each template as `.xlsx` and close it. | Saves without a warning about lost features, or the warning is noted. |
| 2 | Reopen each `.xlsx` and import its CSV again. | No error values (#NAME?, #VALUE!, Err:); Final and QA match the LibreOffice results. |
| 3 | If Excel is available, open the `.xlsx` there too. | Same results as step 2. |
