# ETL Business Rules

**AI Transparency:** AI helped reconstruct and draft these rules from our earlier discussions and the workbook itself. I also used AI to revise the wording.

These rules describe what the workbook is expected to do. For how the formulas work, see the [Technical Overview](Technical_Overview.md).

## 1. Input

**BR-01 — Source Data**

The user pastes the full source report, including the header row, into RawData.

**BR-02 — Required Columns**

The report needs six recognized fields:

- `PARTNO` — Part Number
- `LINE` — Product Line
- `CAT` — Category
- `DESCRIPTION` — Product Description
- `ONHAND` — Quantity on Hand
- `PRDMIN` — Product Minimum

**BR-03 — Header Recognition**

The columns don't have to be in a particular order. The workbook finds them by their headings, including approved alternate names. Capitalization and common formatting differences should not prevent a match.

**BR-04 — Other Columns**

Extra columns are allowed and are ignored if the workbook doesn't need them.

## 2. Cleaning and Deciding Which Records to Use

**BR-05 — Data Normalization**

Before processing, the workbook standardizes relevant text, including capitalization and unnecessary spaces.

**BR-06 — Missing Values**

- A blank Category becomes `99` for sorting. This is **not** a real company category.
- Description may be blank.
- Blank On Hand and Product Minimum values count as zero.
- Part Number and Product Line are expected to have valid values.
- Any quantity that is present must be numeric.

**BR-07 — Record Inclusion**

A record goes into the reports when **either** On Hand or Product Minimum is greater than zero. If both are zero, that record is left out.

**BR-08 — Missing Part Numbers**

A row without a part number can't be sorted normally, so it is excluded. If that exclusion causes an inventory checksum discrepancy, the workbook blocks the reports and shows an error.

## 3. Interpreting Part Numbers

**BR-09 — Part-Number Structure**

Part numbers can contain prefixes, suffixes, letters, digits, and hyphens. The workbook recognizes known formats and separates their components to build sort keys.

**BR-10 — Parsing Rules**

The workbook chooses a parsing rule based on the part-number format. These rules cover leading letters, hyphenated numbers, and a default method for other recognized formats.

There is also a special third-character rule, but **only** for numbers starting with manufacturer families `14`, `17`, or `18` followed by a letter. Other part numbers must not be put into that special case by mistake.

**BR-11 — Keep the Original Part Number**

The sorting components are used internally. The reports still show the original part number rather than replacing it with a sort key.

## 4. Sorting and Finished Reports

**BR-12 — Sort Priorities**

All three reports use the same accepted data, but sort it differently:

| Report | Sorting priority |
|---|---|
| Part Number First | Part Number → Line → Category |
| Category First | Category → Line → Part Number |
| Line First | Line → Category → Part Number |

Part-number order comes from the parsed components, not just alphabetical text sorting. Category First and Line First keep categories and product lines grouped for shelving instead of mixing brands simply because their part numbers look similar. Part Number First provides a separate reference view.

The order of displayed columns isn't always the same as the sort priority.

**BR-13 — Consistent Ordering**

When two records have the same sort values, their original source-row positions decide the final order. That keeps the results consistent without throwing away records that happen to match.

**BR-14 — Same Records in Every Report**

The three outputs must contain the same accepted records; only the sorting and presentation change. Each report includes sequential row numbers for warehouse planning.

## 5. Checks and Capacity

**BR-15 — Missing Headers**

If a required header isn't found, the workbook must show an error rather than silently produce an incomplete report.

**BR-16 — Data Integrity**

The workbook tracks records it excluded or found problems with. It compares On Hand and Product Minimum totals from Step2 against each of the three Step4 outputs.

If those checks show missing or inconsistent data, normal report output must be blocked.

**BR-17 — Other QA Checks**

The workbook also looks for duplicate part numbers, missing required row data, parsing problems, and failures to reconstruct the original part-number structure.

**BR-18 — Processing Limit**

The limit is **2,000 source rows**, not counting the header. Exceeding the supported rows or columns must trigger an overflow warning or error.

**BR-19 — Protecting the Reports**

When a blocking QA problem is found, the report shows an error instead of displaying potentially inaccurate results as if they were correct.

## 6. Known Limitations

I built the parsing around the formats used in the original warehouse process. Unfamiliar part numbers may need new handling.

The duplicate check currently looks at the part number alone. In some cases, the proper record identity may also include Product Line and Category, so that check can flag two different records as duplicates.

I may add other parsing or validation rules if new requirements come up.
