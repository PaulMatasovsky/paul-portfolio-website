# Test Cases

- **Area:** LibreOffice Calc templates (built in Google Sheets), Supabase load
- **Author / date:** Paul Matasovsky, 2026-11-17. AI drafted these from our discussion; I reviewed them.

Not run yet. Results go in the [execution log](Execution-Log.md).

## TC-001: Every row is accounted for

- **Why:** BR-28.
- **Setup:** `clients.csv` and `appointments.csv` imported into their templates.

| Step | Action | Expected result |
|---|---|---|
| 1 | Count RawData rows, without the header. | Clients 198, appointments 580. |
| 2 | Read the QA tab. | Loaded + held + rejected + removed equals the RawData count. |
| 3 | Blank out one row's outcome so it's counted nowhere, then undo. | The QA tab shows a mismatch, then matches again. |

## TC-002: Columns are found by heading, not position

- **Why:** BR-02.
- **Setup:** Clients template with `clients.csv` loaded; Final saved as a reference copy.

| Step | Action | Expected result |
|---|---|---|
| 1 | Move two columns in RawData to new positions. | Final is unchanged. |
| 2 | Rename a heading to a style variant (for example `Last Name` to `last_name`). | Final is unchanged. |
| 3 | Rename a required heading to something unrecognized. | An error shows; Final doesn't quietly output incomplete data. |

## TC-003: Duplicates are removed or flagged

- **Why:** BR-21, BR-22.
- **Setup:** Clients template with `clients.csv` loaded.

| Step | Action | Expected result |
|---|---|---|
| 1 | Check the exact duplicate rows. | One copy stays; the extras are removed and counted. |
| 2 | Check clients with the same name and birth date under different IDs. | Both rows are flagged; neither is merged or dropped. |
| 3 | Check the client ID that belongs to two different people. | The client with the earlier intake date loads; the other is held with a reason asking for a new ID (BR-23). |

## TC-004: Orphan appointments are held

- **Why:** BR-25.
- **Setup:** Appointments template loaded; client-ID tab filled from the clients Final.

| Step | Action | Expected result |
|---|---|---|
| 1 | Check appointments whose client ID isn't on the client-ID tab. | Each is held with a reason to check the client ID or add the client. |
| 2 | Check client IDs written differently (`42`, `C-42`, `c0042`). | They match the right client after cleaning, not counted as orphans. |
| 3 | Check appointments for clients who were rejected or held. | Each is held, not rejected, with a reason naming the client to fix (BR-26). |
| 4 | Check appointments under the client ID that belongs to two people. | Each loads with the client who loaded, flagged to confirm whose visit it was (BR-23). |

## TC-005: Values at the limits

- **Why:** BR-05, BR-16, BR-17.
- **Setup:** Appointments and clients templates; add test rows, then remove them afterward.

| Step | Action | Expected result |
|---|---|---|
| 1 | Enter durations of 14, 15, 180 and 181 minutes. | 15 and 180 pass; 14 and 181 are held with a reason to correct the duration. |
| 2 | Enter a birth date of today, then tomorrow. | Today passes; tomorrow is held with a reason to collect the correct birth date. |
| 3 | Enter an appointment date that doesn't exist, such as 06/31/2026. | Held with a reason to correct the date. |

## TC-006: Same input, same output

- **Why:** Same input should always give the same output.
- **Setup:** Clients template with `clients.csv` loaded; Final saved as a reference copy.

| Step | Action | Expected result |
|---|---|---|
| 1 | Make a fresh copy of the blank template and import the same file. | Final matches the reference copy exactly. |

## TC-007: The database refuses bad data

- **Why:** The database checks are a second safety net.
- **Setup:** Supabase tables created with `01_create_tables.sql`.

| Step | Action | Expected result |
|---|---|---|
| 1 | Insert an appointment for a client ID that doesn't exist. | Refused by the foreign key. |
| 2 | Insert a client with a status of `Pending`. | Refused by the status check. |

## TC-008: Records match field by field

- **Why:** Counts can match while values are wrong.
- **Setup:** Both tables loaded in Supabase.

| Step | Action | Expected result |
|---|---|---|
| 1 | Pick 10 client IDs at random and compare each field in the source, Final and Supabase. | Every field matches after the cleaning rules are applied. |

## TC-009: SQL counts match the QA tab

- **Why:** The database and the spreadsheet should agree.
- **Setup:** Both tables loaded; validation queries written.

| Step | Action | Expected result |
|---|---|---|
| 1 | Count rows in each table. | Matches the Final counts on each QA tab. |
| 2 | Run each validation query. | Each returns 0 rows. |

## TC-010: Templates work outside Google Sheets

- **Why:** The finished templates run in LibreOffice Calc and are published as `.xlsx`, so every formula has to survive the move from Google Sheets.
- **Setup:** Both finished templates, cleared of data.

| Step | Action | Expected result |
|---|---|---|
| 1 | Download each template as `.xlsx` and open it in LibreOffice Calc. | No warning about lost features, or the warning is noted. |
| 2 | Import its CSV again. | No error values (#NAME?, #VALUE!, Err:); Final and QA match the Google Sheets results. |
| 3 | If Excel is available, open the `.xlsx` there too. | Same results as step 2. |

## TC-011: Every exception has a record

- **Why:** BR-29, BR-32.
- **Setup:** Both templates loaded.

| Step | Action | Expected result |
|---|---|---|
| 1 | Compare each Exceptions tab with the QA counts. | Held + rejected + removed + flagged rows on Exceptions match the QA tab. |
| 2 | Pick 5 exception rows and find each one in RawData by source row number. | Each matches its source row, and its reason says what to do. |
| 3 | Check an appointment with status "Kept". | It shows as Completed in Final (BR-09). |

## TC-012: Shared sessions are caught, not loaded wrong

- **Why:** BR-33.
- **Setup:** Both templates loaded; add test rows, then remove them afterward.

| Step | Action | Expected result |
|---|---|---|
| 1 | Change a client's first name to "John & Jane", then to "John and Jane". | Each time the client is held with a reason to split the record into two clients, and their appointments are held (BR-26). |
| 2 | Check a client whose name contains "and" inside a word, such as Anderson or Sandra. | Not held. |
| 3 | Check a 90847 appointment with one client ID. | Loads under that client. |
| 4 | Book two clients with the same clinician, date and start time. | Both are flagged as a double booking, and the reason asks whether it was one shared session. |
