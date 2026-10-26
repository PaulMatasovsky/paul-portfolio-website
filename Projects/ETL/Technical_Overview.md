# ETL Technical Overview

**AI Transparency:** AI assisted with reconstructing and drafting this document using previous project discussions and workbook inspection.

## 1. Architecture

The project uses a spreadsheet-based ETL pipeline. Each worksheet handles a specific part of the process and passes its results to the next stage.

`RawData → HeaderMap → Step1 → Step2 → Step3 → Step4 → Reports`

The QA worksheet checks information from multiple processing stages and determines whether the report sheets display normal results or an error.

## 2. Processing Stages

### RawData — Input

RawData holds the original source report, including its headers.

Users replace the previous report with the new one. The workbook processes the data automatically without requiring changes to the processing worksheets.

### HeaderMap — Column Identification

HeaderMap identifies the source columns used by the workbook.

It normalizes header names by converting them to uppercase and removing spaces, underscores, and hyphens. It then compares them against the recognized header names and alternatives.

The resulting column positions allow the workbook to process reports even when the source columns have been rearranged.

### Step1 — Data Extraction

Step1 retrieves the six source fields using the positions identified by HeaderMap.

This creates a consistent data structure for the remaining processing stages, regardless of the original report's column order.

### Step2 — Cleaning and Parsing

Step2 prepares the extracted data for sorting.

It removes unnecessary surrounding whitespace and nonprinting characters, standardizes text capitalization, and converts blank On Hand and Product Minimum values to zero.

It flags conditions such as zero quantities, missing row information, and duplicate part numbers.

A decision tree selects the parsing method for each part number. Recognized cases include leading letters, hyphenated numbers, and special third-character formats.

The parsing formulas extract the components used to construct the sorting keys.

### Step3 — Sorting Keys

Step3 creates three sorting keys using the parsed part-number components and the product line and category fields.

It standardizes components through zero-padding so their values can be compared consistently. The original source-row position serves as a final tie-breaker.

The keys are ranked to determine each record's position in its output.

### Step4 — Output Assembly

Step4 uses the calculated ranks to retrieve records in the correct order for each report.

It assembles three output tables containing the original part number, product line, category, description, quantities, and sequential row numbers.

These tables feed the print-ready report worksheets.

## 3. Sort Order and Report Layout

Step3 controls **sorting priority**. Step4 controls the **displayed column order**. These are intentionally different for two reports.

| Report | Sorting priority | Displayed fields after row number |
|---|---|---|
| Part Number First | Part Number → Line → Category | Part Number, Line, Category |
| Category First | Category → Line → Part Number | Category, Part Number, Line |
| Line First | Line → Category → Part Number | Line, Part Number, Category |

All three displays then include Description, On Hand, and Product Minimum.

The Category First and Line First sort keys prioritize product grouping before part number. This reflects the shelving requirement to keep different lines or brands separated rather than arranging every part solely by part number.

## 4. Quality Assurance

The QA worksheet identifies conditions that could produce incorrect reports, including:

- Missing required source headers.
- Duplicate part numbers.
- Source data exceeding the supported row or column capacity.
- On Hand and Product Minimum checksum differences between Step2 and each Step4 output.
- Part-number parsing and reconstruction problems.

It also tracks excluded zero-quantity records and rows missing expected data.

The QA worksheet includes formula-based regression checks for the three sorting orders and selected parsing cases.

Blocking conditions contribute to the QA error total. When that total is greater than zero, the report worksheets show an error or suppress the normal output instead of presenting the results as valid.

## 5. Report Worksheets

PartNoFirstReport, CategoryFirstReport, and LineFirstReport display Step4's corresponding output tables in print-ready formats.

These are the primary worksheets intended for normal use. The intermediate processing worksheets handle the extraction, sorting, and validation without requiring user interaction.

## 6. Excel Compatibility

The workbook was originally developed in Google Sheets and later adapted for Excel.

The header-mapping formulas were rewritten without `FILTER` so Excel could locate reordered source columns. Formula changes also addressed implicit-intersection (`@`) operators that caused range-based calculations to behave incorrectly.

The overflow check was adjusted to detect excess populated rows and columns. Blank optional Description values were also handled so Excel would not display an unintended `0`.

The workbook instructions and screenshots were updated to explain selecting the complete worksheet before copying or clearing data.

These changes were made to preserve the intended ETL workflow and outputs across the two spreadsheet applications.

## 7. Supporting Worksheets and Limitations

**Test Data:** Contains sample records used to examine part-number patterns and processing scenarios.

**Comments:** Provides supporting notes about the workbook.

The supported input limit is 2,000 source records. Parsing rules cover known part-number patterns and may need to be extended for unfamiliar formats.

For expected behavior, see [Business Rules](Business_Rules.md). For visual examples, see [Screenshots](ETL_Documentation/Supporting_Evidence/Screenshots/README.md).
