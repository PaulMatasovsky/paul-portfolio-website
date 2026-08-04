# ETL Workflow

## Purpose

This document describes the complete Extract, Transform, Load (ETL) workflow implemented in the current spreadsheet version of the Inventory Management project.

Rather than documenting individual formulas, this document focuses on how data flows through the system, the responsibility of each processing stage, and the engineering decisions behind the workflow.

---

# Overview

The ETL pipeline transforms a downloaded warehouse inventory report into three printable reports organized for different warehouse tasks.

The pipeline was designed around a series of independent processing stages.

Each stage performs one primary responsibility before passing its output to the next stage.

```
Warehouse Report
        │
        ▼
RawData
        │
        ▼
HeaderMap
        │
        ▼
Step 1
        │
        ▼
Step 2
        │
        ▼
Step 3
        │
        ▼
Step 4
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
Category PartNo Line
Reports  Report Report
```

---

# Stage 1 — Data Extraction

## RawData

RawData serves as the entry point into the workbook.

Users copy an entire warehouse report—including the header row—and paste it into this worksheet.

No transformation occurs here.

RawData intentionally preserves the original report so that every downstream operation begins from the same source.

---

# Stage 2 — Header Mapping

## HeaderMap

Warehouse reports occasionally change.

Columns may move or header names may change.

HeaderMap isolates the remainder of the workbook from those changes by locating the required business fields regardless of their physical position.

Required fields currently include:

- LINE
- CAT
- PARTNO
- ONHAND
- PRDMIN

DESCRIPTION is also mapped when available.

The mapping process normalizes header names by:

- converting to uppercase
- removing spaces
- removing underscores
- removing hyphens

The result is a stable internal schema used by the remainder of the ETL.

---

# Stage 3 — Canonical Column Selection

## Step 1

Step 1 retrieves the required columns identified by HeaderMap.

The output is always the same six business fields in the same order:

1. LINE
2. CAT
3. PARTNO
4. DESCRIPTION
5. ONHAND
6. PRDMIN

No cleaning, validation, or filtering occurs during this stage.

Its only responsibility is establishing a consistent internal structure.

---

# Stage 4 — Data Normalization

## Step 2

Step 2 performs the majority of the workbook's business processing.

Responsibilities include:

- trimming whitespace
- converting text to uppercase
- normalizing numeric values
- preparing QA checks
- parsing part numbers

Part numbers are separated into:

- Prefix
- Numeric Root
- Suffix

These values are not displayed to the user.

They exist solely to support proper natural sorting later in the workflow.

Step 2 also prepares information used by the QA worksheet, including duplicate detection and quantity validation.

---

# Stage 5 — Key Construction

## Step 3

Step 3 constructs three unique sort keys.

Each key is optimized for one report.

Category Report

Category → Prefix → Root → Suffix → Line → Row

Part Number Report

Prefix → Root → Suffix → Line → Category → Row

Line Report

Line → Prefix → Root → Suffix → Category → Row

The original row number is appended to every key to guarantee deterministic ordering.

Blank rows are excluded from the sorting process.

---

# Stage 6 — Report Assembly

## Step 4

Step 4 reconstructs complete business records from the sorted keys.

Rather than displaying helper columns, it retrieves the original cleaned business fields:

- Part Number
- Description
- On Hand
- Product Minimum
- Line Code
- Category

Three independent datasets are assembled.

Each becomes the source for one printable report.

---

# Stage 7 — Report Generation

Three report layouts are produced.

## CategoryFirstReport

Groups inventory by category before sorting by part number.

Used when warehouse personnel need similar product categories stored together.

---

## PartNoFirstReport

Sorts inventory by natural part-number order.

This is the report most commonly used by warehouse managers.

---

## LineFirstReport

Groups inventory by manufacturer line code before sorting by part number.

Used for situations where products are organized primarily by manufacturer.

---

# Quality Assurance

Quality validation is performed throughout the ETL.

Rather than validating only the input or only the output, the workbook verifies each major processing stage.

Current validation includes:

- Required headers
- Template overflow
- Duplicate part numbers
- Quantity checksums
- Blank records
- Zero-quantity records

Blocking validation failures prevent reports from being generated.

Informational findings are reported without stopping the workflow.

---

# Design Philosophy

The workflow follows several guiding principles.

## Single Responsibility

Each worksheet performs one primary responsibility.

Transformation is distributed rather than concentrated.

---

## Progressive Processing

Data becomes increasingly structured at each stage.

Each worksheet builds upon the output of the previous worksheet.

---

## Data Preservation

The original business fields are preserved throughout processing.

Internal helper values are used only for sorting.

Managers always view the original business information.

---

## Fail Before Printing

The workbook prefers producing no report over producing an incorrect report.

Validation occurs before printable reports are displayed.

---

# Future Evolution

Although implemented as a spreadsheet, this workflow was intentionally designed around processing stages rather than spreadsheet features.

Future implementations are expected to replace individual worksheets with database operations, application services, and user interface components while preserving the overall workflow documented here.