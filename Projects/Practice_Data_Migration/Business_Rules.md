# Practice Data Migration — Business Rules

**AI Transparency:** AI drafted these rules from my conversation with it about the data. I made the decisions and reviewed the wording. Rules marked *confirm with client* are my choice for this project; on a real job I'd check them with the client first.

These rules say what happens to every row in the OldChart export. Each row ends up in one of five places:

| Handling | What happens |
|---|---|
| **Fix** | Cleaned automatically. Formatting only; the meaning doesn't change. |
| **Flag** | Loaded, and listed in QA with a reason so someone can follow up. |
| **Hold** | Not loaded yet, and listed with a reason so someone can fix it and release it. |
| **Reject** | Kept out of the load and listed in QA with a reason. |
| **Remove** | Dropped and counted: exact duplicates, blank rows and test records. |

## 1. Input

**BR-01 — Source Files**

The source is two CSV exports from OldChart EHR: `clients.csv` and `appointments.csv`. Each is opened in its own LibreOffice Calc workbook as plain text, without letting Calc convert numbers and dates. Cleaning happens offline; the data isn't put in a cloud spreadsheet.

**BR-02 — Header Recognition**

Columns are found by their headings, not their position. Capitalization, spaces, dashes and underscores don't prevent a match.

**BR-03 — Fields Kept and Dropped**

| File | Kept | Dropped |
|---|---|---|
| Clients | Client ID, first name, last name, date of birth, phone, email, street address, city, state, ZIP, insurance provider, member ID, primary clinician, status, intake date, referral source | Last Modified (the old system's own timestamp) |
| Appointments | Appointment ID, client ID, date, start time, duration, service code, clinician, location, status, copay | Booked By (inconsistent free text, not used for billing or scheduling) |

**BR-04 — Referral Source**

Referral Source is kept because it shows the practice where its clients come from, which helps it decide where to spend on marketing. It's optional, so a blank is fine.

**BR-05 — Required Fields**

- **Clients:** Client ID, first name, last name, date of birth, primary clinician and status.
- **Appointments:** appointment ID, client ID, date, start time, service code, clinician and status.

- **A client** missing a required field, or with a birth date that's impossible or in the future, is **held**, not rejected. It's most likely a clerical error, and the client shouldn't miss an appointment because of it. The reason tells the front desk what to collect, for example "Birth date missing: get it at check-in before the appointment." The record should be fixed right away.
- **An appointment** missing a required field is rejected, with the missing field as the reason.

## 2. Sources of Truth

**BR-06 — Client Details**

The clients file is the only source for who a client is. Appointments carry only the client ID and get everything else from the clients table.

**BR-07 — Clinician Names**

There is one approved list of four clinicians, written first name then last name, with no title or license letters: Sarah Lindqvist, Marcus Bell, Elena Ruiz and Daniel Okafor. Every spelling in either file maps to one of these through a lookup tab. A spelling not on the lookup tab is flagged, never guessed.

**BR-08 — Assigned vs. Rendering Clinician**

A client's primary clinician and the clinician who held an appointment can be different people. Both are kept. Neither overwrites the other.

**BR-09 — Status Values**

- **Client status:** Active, Inactive or Discharged.
- **Appointment status:** Scheduled, Completed, No Show, Cancelled or Late Cancel.

Every variant spelling maps to one of these through a lookup tab. An unmapped value is flagged.

## 3. Formats

**BR-10 — Names**

Extra spaces are trimmed and names are put in proper case. Names are otherwise stored as given; suffixes such as Jr. are not split into their own field.

Known limitation: proper case would change names like McDonald or O'Brien. None are in this data.

**BR-11 — Dates**

All dates are converted to one format, YYYY-MM-DD. Two-digit years follow LibreOffice's default setting: 00–29 means 2000s, 30–99 means 1900s.

**BR-12 — Phone Numbers**

Phone numbers are stored as 10 digits only. A leading country code of 1 and any extension are removed. A number that doesn't come out to 10 digits is left blank, and the row is flagged.

**BR-13 — Email Addresses**

Emails are trimmed and lowercased. The format check is one @ with a dot somewhere after it and no spaces; it can't confirm the mailbox exists. An email that fails is left blank, and the row is flagged.

**BR-14 — State and ZIP**

States become two-letter codes. ZIP codes become five digits: the +4 part is dropped, and lost leading zeros are restored. Out-of-state addresses are allowed.

**BR-15 — Times, Durations, Copays and Locations**

- Start times are converted to 24-hour time.
- Durations become whole minutes.
- Copays become numbers without $ signs.
- Location is Office or Telehealth.

## 4. Valid Values

**BR-16 — Dates That Can't Be Right**

An appointment date that doesn't exist (such as June 31) is rejected. A client's birth date that doesn't exist or is in the future is held (BR-05).

**BR-17 — Durations**

A duration from 15 to 180 minutes is valid. Anything outside that range is rejected.

A blank duration doesn't hold up the appointment. It defaults to 60 minutes so the schedule blocks enough time and nothing gets double-booked, and the row is flagged so billing can confirm the real length.

**BR-18 — Service Codes**

The service code must be one of 90791, 90832, 90834, 90837 or 90847. Anything else, including a blank, is rejected.

**BR-19 — Status vs. Date**

A future appointment marked Completed, or a past appointment still marked Scheduled, is flagged.

**BR-20 — Other Flags**

These are flagged rather than rejected, because the record may still be real:

- An appointment before the client's intake date.
- A clinician booked for two appointments at the same date and time.
- A negative copay.
- A missing intake date.
- A blank or "N/A" copay. It's stored as 0 so the client keeps the appointment, and flagged so billing can follow up. *Confirm with client:* some practices won't see a client until the copay is settled.

## 5. Duplicates and Identity

**BR-21 — Exact Duplicates**

When a row is an exact copy of another, one copy is kept and the extras are removed and counted.

**BR-22 — Possible Duplicate Clients**

The same first name, last name and date of birth under two different client IDs is flagged on both rows. Records are never merged automatically; a person decides which one wins.

**BR-23 — One ID, Two People**

When two different people share a client ID, the first row in the export loads. Any later row with that ID is held with a reason asking for a new ID. *Confirm with client.*

**BR-24 — Test Records**

Rows whose first or last name is TEST are removed.

## 6. Relationships

**BR-25 — Orphan Appointments**

An appointment whose client ID doesn't exist in the clients file is rejected.

**BR-26 — Appointments for a Client Who Didn't Load**

If a client is rejected or held, that client's appointments are held, not rejected. They're real visits and real revenue, and often all that's missing is something like a birth date. Once the client record is fixed, the appointments can be released. What to do with them is the practice's decision, not the pipeline's.

**BR-27 — Load Order**

Clients load before appointments, so the database can confirm every appointment belongs to a client.

## 7. Checks

**BR-28 — Every Row Accounted For**

For each file, rows in must equal rows loaded plus rows held plus rows rejected plus rows removed. If they don't match, nothing loads until the difference is found.

**BR-29 — Every Exception Has a Reason**

Every flagged, held, rejected or removed row appears in QA with a reason in plain language that says what's wrong and what someone needs to do. The person reading the list shouldn't need to know how the data was cleaned or loaded. It's the same idea as commenting code.
