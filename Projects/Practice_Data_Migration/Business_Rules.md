# Practice Data Migration — Business Rules

**AI Transparency:** AI drafted these rules from my conversation with it about the data, and I reviewed them. Rules under [Open Decisions](#open-decisions) are not settled yet.

These rules say what happens to every row in the OldChart export. Each row ends up in one of four places:

| Handling | What happens |
|---|---|
| **Fix** | Cleaned automatically. Formatting only; the meaning doesn't change. |
| **Flag** | Loaded, and listed in QA with a reason so someone can follow up. |
| **Reject** | Kept out of the load and listed in QA with a reason. |
| **Remove** | Dropped and counted: exact duplicates, blank rows and test records. |

## 1. Input

**BR-01 — Source Files**

The source is two CSV exports from OldChart EHR: `clients.csv` and `appointments.csv`. Each is imported into its own workbook as plain text, without letting Sheets convert numbers and dates.

**BR-02 — Header Recognition**

Columns are found by their headings, not their position. Capitalization, spaces, dashes and underscores don't prevent a match.

**BR-03 — Fields Kept and Dropped**

| File | Kept | Dropped |
|---|---|---|
| Clients | Client ID, first name, last name, date of birth, phone, email, street address, city, state, ZIP, insurance provider, member ID, primary clinician, status, intake date | Last Modified (the old system's own timestamp). Referral Source is an open decision. |
| Appointments | Appointment ID, client ID, date, start time, duration, service code, clinician, location, status, copay | Booked By (inconsistent free text, not used for billing or scheduling) |

**BR-04 — Required Fields**

- **Clients:** Client ID, first name, last name, date of birth, primary clinician and status.
- **Appointments:** appointment ID, client ID, date, start time, service code, clinician and status.

A row missing any required field is rejected, with the missing field as the reason.

## 2. Sources of Truth

**BR-05 — Client Details**

The clients file is the only source for who a client is. Appointments carry only the client ID and get everything else from the clients table.

**BR-06 — Clinician Names**

There is one approved list of four clinicians, written first name then last name, with no title or license letters: Sarah Lindqvist, Marcus Bell, Elena Ruiz and Daniel Okafor. Every spelling in either file maps to one of these through a lookup tab. A spelling not on the lookup tab is flagged, never guessed.

**BR-07 — Assigned vs. Rendering Clinician**

A client's primary clinician and the clinician who held an appointment can be different people. Both are kept. Neither overwrites the other.

**BR-08 — Status Values**

- **Client status:** Active, Inactive or Discharged.
- **Appointment status:** Scheduled, Completed, No Show, Cancelled or Late Cancel.

Every variant spelling maps to one of these through a lookup tab. An unmapped value is flagged.

## 3. Formats

**BR-09 — Names**

Extra spaces are trimmed and names are put in proper case. Names are otherwise stored as given; suffixes such as Jr. are not split into their own field.

Known limitation: proper case would change names like McDonald or O'Brien. None are in this data.

**BR-10 — Dates**

All dates are converted to one format, YYYY-MM-DD. Two-digit years follow Google Sheets: 00–29 means 2000s, 30–99 means 1900s.

**BR-11 — Phone Numbers**

Phone numbers are stored as 10 digits only. A leading country code of 1 and any extension are removed. A number that doesn't come out to 10 digits is left blank, and the row is flagged.

**BR-12 — Email Addresses**

Emails are trimmed and lowercased. The format check is one @ with a dot somewhere after it and no spaces; it can't confirm the mailbox exists. An email that fails is left blank, and the row is flagged.

**BR-13 — State and ZIP**

States become two-letter codes. ZIP codes become five digits: the +4 part is dropped, and lost leading zeros are restored. Out-of-state addresses are allowed.

**BR-14 — Times, Durations, Copays and Locations**

- Start times are converted to 24-hour time.
- Durations become whole minutes.
- Copays become numbers without $ signs.
- Location is Office or Telehealth.

## 4. Valid Values

**BR-15 — Dates That Can't Be Right**

A date that doesn't exist (such as June 31) or a birth date in the future is rejected.

**BR-16 — Durations**

A duration from 15 to 180 minutes is valid. Anything outside that range is rejected.

**BR-17 — Service Codes**

The service code must be one of 90791, 90832, 90834, 90837 or 90847. Anything else, including a blank, is rejected.

**BR-18 — Status vs. Date**

A future appointment marked Completed, or a past appointment still marked Scheduled, is flagged.

**BR-19 — Other Flags**

These are flagged rather than rejected, because the record may still be real:

- An appointment before the client's intake date.
- A clinician booked for two appointments at the same date and time.
- A negative copay.
- A missing intake date.

## 5. Duplicates and Identity

**BR-20 — Exact Duplicates**

When a row is an exact copy of another, one copy is kept and the extras are removed and counted.

**BR-21 — Possible Duplicate Clients**

The same first name, last name and date of birth under two different client IDs is flagged on both rows. Records are never merged automatically; a person decides which one wins.

**BR-22 — Test Records**

Rows whose first or last name is TEST are removed.

## 6. Relationships

**BR-23 — Orphan Appointments**

An appointment whose client ID doesn't exist in the clients file is rejected.

**BR-24 — Load Order**

Clients load before appointments, so the database can confirm every appointment belongs to a client.

## 7. Checks

**BR-25 — Every Row Accounted For**

For each file, rows in must equal rows loaded plus rows rejected plus rows removed. If they don't match, nothing loads until the difference is found.

**BR-26 — Every Exception Has a Reason**

Every flagged, rejected or removed row appears in QA with a reason.

## Open Decisions

These need a decision before the rules are final.

1. **Referral Source:** drop it, or keep it for the practice's marketing?
2. **Appointments for a rejected client:** reject them too, or hold them until the client record is fixed?
3. **One client ID used for two different people:** reject the newer row, or hold both until someone checks?
4. **Blank duration:** fill it in from the service code's usual length, or flag it and leave it blank?
5. **Blank or "N/A" copay:** store it as 0 or leave it empty? Zero means "nothing owed"; empty means "unknown."
