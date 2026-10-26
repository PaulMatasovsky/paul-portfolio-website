# ETL Business Rules

**AI Transparency:** AI assisted with reconstructing and drafting these rules from previous project discussions and workbook inspection.

## 1. Input Requirements

**BR-01: Source Data**

The workbook accepts a complete source report, including its header row, pasted into the RawData worksheet.

**BR-02: Required Columns**

The source report must contain six recognized columns:

- `PARTNO` — Part Number
- `LINE` — Product Line
- `CAT` — Category
- `DESCRIPTION` — Product Description
- `ONHAND` — Quantity on Hand
- `PRDMIN` — Product Minimum

**BR-03: Header Recognition**

The workbook identifies columns by their headers rather than their positions. Columns may appear in any order, provided their names match a recognized header or approved alternative.

Header recognition accommodates differences in capitalization and common formatting variations.

**BR-04: Additional Columns**

The source report may contain columns that are not used by the workbook. These are ignored during processing.

## 2. Data Cleaning and Inclusion

**BR-05: Data Normalization**

The workbook standardizes relevant text fields, including capitalization and unnecessary surrounding spaces, before processing the data.

**BR-06: Missing Values**

- Missing Category values are assigned `99` for sorting purposes. This does not represent an actual company-assigned category.
- Missing Description values are permitted.
- Missing On Hand and Product Minimum values are treated as zero.
- Part Number and Product Line are expected to contain valid values.
- Nonblank quantity values must be numeric.

**BR-07: Record Inclusion**

A record is included when either On Hand or Product Minimum is greater than zero.

Records where both values are zero are excluded from the finished reports.

**BR-08: Missing Part Numbers**

Records without a part number cannot be sorted normally and are excluded from report output.

If excluding a record creates a discrepancy in the inventory checksums, the workbook blocks the reports and displays an error.

## 3. Part-Number Processing

**BR-09: Part-Number Interpretation**

Part numbers may contain letters, numbers, prefixes, suffixes, and hyphens.

The workbook identifies recognized patterns and separates the part number into components to produce a consistent sorting order.

**BR-10: Parsing Rules**

The workbook uses different parsing rules according to the recognized part-number structure.

These include numbers with leading letters, hyphenated numbers, and a default rule for other recognized formats.

A special third-character rule applies only to part numbers beginning with the manufacturer families `14`, `17`, or `18`, followed by a letter.

Part numbers outside those families must not be incorrectly assigned to that special rule.

**BR-11: Original Part Number**

The original part number remains available for display in the finished reports. Internal sorting values are not intended to replace the part number shown to users.

## 4. Sorting and Reports

**BR-12: Sorting Priorities**

The workbook produces three reports from the same accepted source data.

| Report | Sorting Priority |
|---|---|
| Part Number First | Part Number, Line, Category |
| Category First | Category, Line, Part Number |
| Line First | Line, Category, Part Number |

Part-number sorting uses the parsed components rather than relying entirely on ordinary alphabetical sorting.

For shelf organization, Category First and Line First keep records grouped by category or product line before sorting by part number. This avoids mixing different lines or brands together solely because their part numbers are similar. Part Number First provides a separate reference view.

The displayed column order may differ from the actual sorting priority.

**BR-13: Consistent Ordering**

When records have otherwise identical sorting values, the original source-row position is used as a final tie-breaker.

This provides a consistent order without removing records merely because their sorting values match.

**BR-14: Report Consistency**

All three reports must contain the same accepted records. Only their sorting priorities and presentation change.

Each output includes sequential row numbering to assist with warehouse planning and organization.

## 5. Validation and Capacity

**BR-15: Required Header Validation**

The workbook checks for missing required headers. Missing headers must produce a visible error rather than silently generating incomplete reports.

**BR-16: Data Integrity**

The workbook tracks excluded or problematic records and compares On Hand and Product Minimum totals from Step2 against all three Step4 outputs.

A checksum discrepancy that indicates lost or inconsistent data prevents normal report output.

**BR-17: Additional QA Checks**

The workbook checks for duplicate part numbers, missing required row data, parsing problems, and failures to reconstruct the original part-number structure.

These checks help identify problems that could affect the accuracy of the reports.

**BR-18: Processing Capacity**

The workbook supports up to 2,000 source data rows, excluding the header row.

Data exceeding this limit must trigger an overflow warning or error. Overflow detection must account for excess populated source rows and columns.

**BR-19: Report Protection**

When a blocking QA condition is detected, the workbook must display an error instead of presenting potentially inaccurate reports as valid.

## 6. Known Limitations

The workbook is designed around known part-number formats and the requirements of the original business process. Unrecognized formats may require additional handling.

The existing duplicate-number QA check uses part number alone. The intended record identity may also depend on Product Line and Category, so the current check can identify records as duplicates even when they differ in those fields.

Additional validation and parsing rules may be added as new requirements are identified.
