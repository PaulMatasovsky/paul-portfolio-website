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

The rules are grouped by what they do to a row, so you can see at a glance what gets held or flagged. A rule that leads to more than one outcome appears in each group, with the part that applies there. The numbers show the order I worked them out.

## Remove

| ID | File | Rule |
|---|---|---|
| BR-21 | Both | Exact duplicate rows: keep one, remove the rest. |
| BR-24 | Clients | Rows named TEST. |

## Reject

| ID | File | Rule |
|---|---|---|
| BR-31 | Both | Only if the record is out of scope, not allowed to move (retention period or deletion request), or impossible to identify. Out of scope means the practice didn't ask to move it: a clinician who isn't joining the new system, appointments before the history cutoff date the practice chooses, or records from another location or practice that ended up in the same export *(confirm with client)*. An unknown clinician spelling is flagged, not rejected (BR-07), since a typo can't be told apart from someone who left. Never for unpaid balances or missed visits. None occur in this export. |

## Hold

| ID | File | Rule |
|---|---|---|
| BR-05 | Clients | Missing or impossible ID, first or last name, birth date, primary clinician or status. The reason tells the front desk what to collect. |
| BR-05 | Appointments | Missing ID, client ID, date, start time, service code, clinician or status. The reason says what to look up. |
| BR-16 | Clients | An impossible or future birth date. The reason asks for the correct date. |
| BR-16 | Appointments | A date that doesn't exist, such as 06/31. The reason asks for the correct date. |
| BR-17 | Appointments | A duration outside 15–180 minutes. The reason asks to correct it. |
| BR-18 | Appointments | A service code that's missing, TBD, or not 90791, 90832, 90834, 90837 or 90847. The reason asks billing to supply it. |
| BR-23 | Clients | One ID on two different people: the client with the earlier intake date loads (if tied or blank, the first row), and the other is held for a new ID. |
| BR-25 | Appointments | A client ID that isn't in the clients file. The reason says to check the ID or add the client. |
| BR-26 | Appointments | The client was held or rejected. It's still a real visit; the practice decides. |
| BR-33 | Clients | A record that holds two people (a name with "&" or " and "). The reason asks the practice to split it into two clients. Couples and family sessions are out of scope. |
| BR-34 | Clients | Under 18 on the migration date. The export has no guardian fields, so the reason asks to add a parent or guardian before the next visit. None occur in this export *(confirm with client)*. |

## Flag

| ID | File | Rule |
|---|---|---|
| BR-07 | Both | A clinician spelling that isn't in the lookup tab. Never guessed. |
| BR-09 | Both | A status that isn't in the lookup tab. |
| BR-12 | Clients | A phone that can't become 10 digits. Left blank. |
| BR-13 | Clients | An invalid email. Left blank. |
| BR-17 | Appointments | A blank duration. Set to 60 minutes so nothing gets double-booked, and flagged for billing. |
| BR-19 | Appointments | A future appointment marked Completed, or a past one still Scheduled. |
| BR-20 | Clients | A missing intake date. |
| BR-20 | Appointments | An appointment before intake, a double-booked clinician, a negative copay, or a blank or "N/A" copay (stored as 0 so the client keeps the visit) *(confirm with client)*. |
| BR-22 | Clients | The same name and birth date under two IDs: flag both. Never merge automatically. |
| BR-23 | Appointments | Appointments under the ID that belongs to two people load with the client who loaded, flagged to confirm whose visit it was *(confirm with client)*. |
| BR-33 | Appointments | Two clients with the same clinician at the same start time are flagged as a double booking (BR-20), and the reason asks whether it was one shared session. Each appointment belongs to one client; a 90847 session loads under the client billed for it *(confirm with client)*. |

## Fix

| ID | File | Rule |
|---|---|---|
| BR-07 | Both | Clinicians are written first name, last name, with no titles: Sarah Lindqvist, Marcus Bell, Elena Ruiz, Daniel Okafor. Every variant maps through a lookup tab. |
| BR-09 | Clients | Status: Active, Inactive, Discharged. Variants map through a lookup tab. |
| BR-09 | Appointments | Status: Scheduled, Completed, No Show, Cancelled, Late Cancel. Variants map through a lookup tab. "Kept" is the old system's word for a visit the client attended, so it maps to Completed *(confirm with client)*. |
| BR-10 | Clients | Names are trimmed and proper-cased; suffixes stay in the name. Limitation: proper case would break names like McDonald (none here). |
| BR-11 | Both | Dates become YYYY-MM-DD. Two-digit years: 00–29 → 2000s, 30–99 → 1900s. |
| BR-12 | Clients | Phones become 10 digits, without a leading 1 or extension. |
| BR-13 | Clients | Emails are trimmed and lowercased, and must have one @ and a dot after it. |
| BR-14 | Clients | States become two-letter codes. ZIPs become five digits, with lost leading zeros restored. |
| BR-15 | Appointments | Times become 24-hour, durations whole minutes, copays plain numbers; location is Office or Telehealth. |

## How the Templates Work

| ID | File | Rule |
|---|---|---|
| BR-01 | Both | Each CSV is imported into its own LibreOffice Calc template, offline, with every column as text. While I build, they live in Google Sheets so my progress is public. Every formula has to work in Google Sheets, LibreOffice and Excel. |
| BR-02 | Both | Columns are found by heading, not position. Case, spaces, dashes and underscores don't matter. |
| BR-03 | Both | Dropped: Last Modified (the old system's timestamp) and Booked By (inconsistent free text). Everything else is kept. |
| BR-04 | Clients | Referral Source is kept, optional, because it shows the practice where to spend on marketing. |
| BR-06 | Both | The clients file is the only source for who a client is. Appointments carry just the client ID. |
| BR-08 | Both | A client's primary clinician and an appointment's clinician can differ. Both are kept. |
| BR-27 | Both | Clients load before appointments, so the database can confirm every link. |
| BR-28 | Both | Rows in = loaded + held + rejected + removed, for each file. If not, nothing loads. |
| BR-29 | Both | Every exception has a plain-language reason saying what to do. The reader shouldn't need to know how the pipeline works, the same idea as commenting code. |
| BR-30 | Appointments | One hold list covers held clients and held appointments. It lives in the appointments template, which has both, and shows each client's next appointment, soonest first, so urgent fixes happen before check-in. |
| BR-32 | Both | The two files stay separate, since one client has many appointments. Each template has a Final tab of loaded rows and an Exceptions tab listing every held, rejected, removed and flagged row with its source row, record ID, outcome and reason. The Exceptions tabs can also load into a text-only `migration_exceptions` table, so every source row has a record in the database. |
| BR-35 | Clients | The export has the insurance provider and member ID, but not who holds the policy. Both load as they are, and the practice confirms the policyholder (often a spouse or parent) before the first claim. Not flagged row by row, since it applies to every insured client *(confirm with client)*. |
| BR-36 | Clients | The export has legal names only, with no preferred name or pronouns. The legal name loads; preferred name and pronouns stay blank for the practice to ask the client. They are never guessed from a name. |
| BR-37 | Appointments | Each appointment loads as a single visit. The export doesn't show which visits belong to a recurring series, so the practice sets up repeating appointments again in the new system *(confirm with client)*. |

**AI transparency:** AI drafted these rules from my conversation with it; the decisions are mine.
