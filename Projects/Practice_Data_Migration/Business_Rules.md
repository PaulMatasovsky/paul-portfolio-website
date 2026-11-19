# Practice Data Migration — Business Rules

Every row in the OldChart export ends in exactly one of four outcomes:

| Outcome | Meaning |
|---|---|
| **Remove** | Dropped and counted: duplicates, blank rows, test records. |
| **Reject** | Doesn't belong in the new system, and no fix would make it belong (BR-31). Listed and kept out. |
| **Hold** | Belongs, but someone has to supply or correct something first. Listed for the practice to fix and release. |
| **Load** | Goes into the new system. |

Two markers sit on top of the outcome:

- **Fixed:** formatting was cleaned. Any row can be fixed; it isn't counted.
- **Flagged:** loaded, but listed for follow-up. Only loaded rows are flagged; a held or rejected row lists all its problems in its reason.

If a row meets more than one outcome, the first one in this order wins: Remove, Reject, Hold, Load.

My guiding rule: **hold what belongs, reject only what doesn't.** These are real people with real appointments, so a clerical error shouldn't cost anyone a visit.

Rules marked *(confirm with client)* are my call for this project; on a real job I'd check them first.

## Input

| ID | Rule |
|---|---|
| BR-01 | Each CSV is imported into its own LibreOffice Calc template, offline, with every column as text. While I build, they live in Google Sheets so my progress is public. Every formula has to work in Google Sheets, LibreOffice and Excel. |
| BR-02 | Columns are found by heading, not position. Case, spaces, dashes and underscores don't matter. |
| BR-03 | Dropped: Last Modified (the old system's timestamp) and Booked By (inconsistent free text). Everything else is kept. |
| BR-04 | Referral Source is kept, optional, because it shows the practice where to spend on marketing. |
| BR-05 | Required for clients: ID, first and last name, birth date, primary clinician, status. Missing or impossible → **Hold**, with a reason telling the front desk what to collect. Required for appointments: ID, client ID, date, start time, service code, clinician, status. Missing → **Hold**, with a reason saying what to look up. |

## Sources of Truth

| ID | Rule |
|---|---|
| BR-06 | The clients file is the only source for who a client is. Appointments carry just the client ID. |
| BR-07 | Clinicians are written first name, last name, with no titles: Sarah Lindqvist, Marcus Bell, Elena Ruiz, Daniel Okafor. Every variant maps through a lookup tab; an unknown spelling → **Flag**, never guessed. |
| BR-08 | A client's primary clinician and an appointment's clinician can differ. Both are kept. |
| BR-09 | Client status: Active, Inactive, Discharged. Appointment status: Scheduled, Completed, No Show, Cancelled, Late Cancel. Variants map through a lookup tab; unknown → **Flag**. "Kept" is the old system's word for a visit the client attended, so it maps to Completed *(confirm with client)*. |

## Formats (Fix)

| ID | Rule |
|---|---|
| BR-10 | Names are trimmed and proper-cased; suffixes stay in the name. Limitation: proper case would break names like McDonald (none here). |
| BR-11 | Dates become YYYY-MM-DD. Two-digit years: 00–29 → 2000s, 30–99 → 1900s. |
| BR-12 | Phones become 10 digits, without a leading 1 or extension. Anything else is left blank → **Flag**. |
| BR-13 | Emails are trimmed and lowercased, and must have one @ and a dot after it. Invalid → blank → **Flag**. |
| BR-14 | States become two-letter codes. ZIPs become five digits, with lost leading zeros restored. |
| BR-15 | Times become 24-hour, durations whole minutes, copays plain numbers; location is Office or Telehealth. |

## Valid Values

| ID | Rule |
|---|---|
| BR-16 | An appointment date that doesn't exist (such as 06/31) or an impossible or future birth date → **Hold** with a reason to correct it (BR-05). |
| BR-17 | Durations of 15–180 minutes are valid; outside → **Hold** to correct the duration. Blank → 60 minutes, so nothing gets double-booked → **Flag** for billing. |
| BR-18 | Service code must be 90791, 90832, 90834, 90837 or 90847; missing, TBD or anything else → **Hold** for billing to supply the code. |
| BR-19 | A future appointment marked Completed, or a past one still Scheduled → **Flag**. |
| BR-20 | Also **Flag**: an appointment before intake, a double-booked clinician, a negative copay, a missing intake date, and a blank or "N/A" copay (stored as 0 so the client keeps the visit) *(confirm with client)*. |

## Duplicates and Identity

| ID | Rule |
|---|---|
| BR-21 | Exact duplicate rows: keep one → **Remove** the rest. |
| BR-22 | Same name and birth date under two IDs → **Flag** both. Never merge automatically. |
| BR-23 | One ID on two different people: the client with the earlier intake date loads (if tied or blank, the first row). The other → **Hold** for a new ID. The loaded client did nothing wrong, so their appointments load too → **Flag** to confirm whose visit it was *(confirm with client)*. |
| BR-24 | Rows named TEST → **Remove**. |

## Relationships

| ID | Rule |
|---|---|
| BR-25 | An appointment whose client ID isn't in the clients file → **Hold**, with a reason to check the ID or add the client. |
| BR-26 | An appointment whose client was held or rejected → **Hold**. It's still a real visit; the practice decides. |
| BR-27 | Clients load before appointments, so the database can confirm every link. |

## Checks

| ID | Rule |
|---|---|
| BR-28 | Rows in = loaded + held + rejected + removed, for each file. If not, nothing loads. |
| BR-29 | Every exception has a plain-language reason saying what to do. The reader shouldn't need to know how the pipeline works, the same idea as commenting code. |
| BR-30 | One hold list covers held clients and held appointments. It lives in the appointments template, which has both, and shows each client's next appointment, soonest first, so urgent fixes happen before check-in. |
| BR-31 | A row is rejected only if the record is out of scope, not allowed to move (retention period or deletion request), or impossible to identify *(confirm with client)*. Never for unpaid balances or missed visits. None occur in this export. |
| BR-32 | The two files stay separate, since one client has many appointments. Each template has a Final tab of loaded rows and an Exceptions tab listing every held, rejected, removed and flagged row with its source row, record ID, outcome and reason. The Exceptions tabs can also load into a text-only `migration_exceptions` table, so every source row has a record in the database. |

**AI transparency:** AI drafted these rules from my conversation with it; the decisions are mine.
