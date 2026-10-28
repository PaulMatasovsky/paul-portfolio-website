# ETL Technical Overview

**AI Transparency:** AI helped reconstruct and draft this document from previous discussions and workbook inspection. I also used AI to revise the wording.

## 1. How the Workbook Is Organized

I built the workbook as a series of processing steps. Each worksheet has a particular job and passes its results to the next one:

`RawData → HeaderMap → Step1 → Step2 → Step3 → Step4 → Reports`

The QA worksheet checks several stages of that process. If something important doesn't match, the report sheets show an error or block the normal results.

## 2. Processing Stages

### RawData — Original Report

RawData holds whatever was in the source report, including its headers. To run the next report, the user replaces the old input. There is no need to edit the processing formulas.

### HeaderMap — Finding the Columns

I didn't want to rely on every report having its columns in exactly the same order.

HeaderMap converts headings to uppercase and removes spaces, underscores, and hyphens. It then looks for the required names or recognized alternatives. The positions it finds are used by the other worksheets.

### Step1 — Pulling Out the Needed Data

Step1 uses those column positions to collect the six required fields. This gives the remaining steps a consistent layout even when the original report is arranged differently.

### Step2 — Cleaning and Parsing

Step2 removes extra spaces and nonprinting characters, standardizes capitalization, and treats blank On Hand and Product Minimum values as zero.

It flags zero-quantity records, missing information, and duplicate part numbers.

A decision tree chooses the parsing rule for each part number. It handles recognized patterns such as leading letters, hyphenated numbers, and special third-character formats, then separates the components needed for sorting.

### Step3 — Building the Sort Keys

Step3 creates three different sort keys from the parsed part-number pieces, Product Line, and Category.

It uses zero-padding so the pieces can be compared consistently, and the original source-row number is the last tie-breaker. It then ranks each record for its position in each output.

### Step4 — Putting the Reports Together

Step4 uses those ranks to assemble the three sorted tables. Each contains the original part number, line, category, description, quantities, and sequential row numbers.

The report worksheets use these tables for printing.

## 3. Sorting Versus Display Order

The order used for **sorting** is not always the order of the **columns on the printed report**. Step3 handles the sort; Step4 determines what the user sees.

| Report | Sorting priority | Displayed fields after row number |
|---|---|---|
| Part Number First | Part Number → Line → Category | Part Number, Line, Category |
| Category First | Category → Line → Part Number | Category, Part Number, Line |
| Line First | Line → Category → Part Number | Line, Part Number, Category |

Each report also includes Description, On Hand, and Product Minimum.

The Category First and Line First versions group parts by category or product line before considering part number. That makes more sense for shelves that need different brands or lines kept together.

## 4. Quality Checks

I added QA checks because a sorted report isn't useful if records are missing or the quantities don't match.

The QA worksheet checks:

- Missing required headers.
- Duplicate part numbers.
- Input beyond the supported row or column limits.
- Differences in On Hand or Product Minimum totals between Step2 and each Step4 output.
- Problems parsing a part number or rebuilding its original structure.

It also keeps track of excluded zero-quantity records and rows with missing information. Formula-based regression checks cover the three sort orders and selected parsing cases.

Blocking problems add to the QA error total. If that total is greater than zero, the reports show an error or suppress their normal output instead of presenting questionable data.

## 5. Printed Reports

PartNoFirstReport, CategoryFirstReport, and LineFirstReport display the matching Step4 tables in a print-ready format.

These are the sheets my manager needs to use. The intermediate sheets do the work in the background without requiring user interaction.

## 6. Excel Compatibility

I first started in LibreOffice, but I restarted the project in Google Sheets after running into blank rows on printed reports. Google Sheets solved that printing issue for the working version and let the workbook be opened from different company computers with internet access and the proper login.

After completing that version, I adapted it for Excel so I could provide a downloadable copy.

That required some changes. I rewrote the header mapping without `FILTER` so it could still find rearranged columns, and I corrected formulas affected by Excel's implicit-intersection (`@`) operators. I also adjusted overflow checks for extra populated rows and columns, and made sure a blank optional Description would not appear as `0`.

The processing approach stayed the same, but **the Excel version still prints unwanted blank rows**. The operational Google Sheets workbook does not. I documented the platform decision in [ADR-001](ETL_Documentation/ETL_ADR/ADR-001.md).

## 7. Other Sheets and Limits

- **Test Data:** Sample part numbers and records used to check different parsing and processing cases.
- **Comments:** Notes about the workbook.

The workbook supports **2,000 source records**. New part-number formats may require changes to the parsing rules.

The [Business Rules](Business_Rules.md) describe the expected behavior, and the [Screenshots](ETL_Documentation/Supporting_Evidence/Screenshots/README.md) show examples of the worksheets and reports.
