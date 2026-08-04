# Project History

## Purpose

This document describes how the Inventory Management project evolved over time.

The project did not begin as a portfolio exercise.

It began as a practical solution to a real business problem encountered in a warehouse environment.

Understanding that evolution is important because many of the architectural decisions documented elsewhere in this repository were driven by real operational requirements rather than hypothetical examples.

---

# The Original Problem

Warehouse managers regularly downloaded inventory reports from an existing warehouse management system.

Although the reports contained the correct inventory information, they were not sorted in a way that supported warehouse operations.

Part numbers containing both letters and numbers were sorted alphabetically rather than naturally.

For example:

```
K10
K100
K11
```

instead of

```
K10
K11
K100
```

For small reports this was only an inconvenience.

For larger reports containing more than a thousand parts, manually correcting the order became a significant operational task.

Managers were spending valuable time copying, cutting, and pasting rows simply to produce printable reports in the correct order.

---

# Initial Solution

The original workbook was created to eliminate this manual sorting process.

Rather than replacing the warehouse system, the workbook accepted its exported reports as input and transformed them into printable reports organized for warehouse use.

The original design goals were intentionally simple:

- require minimal user training;
- avoid changes to existing warehouse procedures;
- produce printable reports in seconds;
- hide technical complexity from warehouse personnel.

The intended user experience became:

1. Download the warehouse report.
2. Copy the report.
3. Paste it into the workbook.
4. Print the desired report.

No understanding of formulas or spreadsheet logic was required.

---

# Engineering Evolution

As the workbook grew, additional engineering challenges became apparent.

Examples included:

- changing report column orders;
- inconsistent header names;
- varying part-number formats;
- duplicate records;
- checksum verification;
- protecting users from invalid output.

Rather than continually expanding a single worksheet, the workbook evolved into a staged processing pipeline.

Separate worksheets were introduced for:

- schema mapping;
- data normalization;
- part-number parsing;
- sort-key construction;
- report assembly;
- quality assurance.

This separation made the workbook easier to maintain and significantly reduced the likelihood that one modification would unintentionally affect another stage.

---

# From Utility to Engineering Project

Originally, this workbook existed solely to solve an operational warehouse problem.

During the development of my software engineering portfolio, I began reviewing the workbook through the lens of software architecture, Domain-Driven Design, and Quality Assurance.

I realized the workbook demonstrated concepts that extend well beyond spreadsheet automation, including:

- staged data transformation;
- separation of responsibilities;
- schema abstraction;
- validation at multiple stages;
- deterministic sorting;
- fail-safe report generation.

Rather than replacing the workbook, I chose to preserve it as the first implementation of a larger engineering project.

---

# Current Perspective

Today the spreadsheet is viewed as Version 1 of a broader Inventory Management system.

Its purpose is no longer limited to producing reports.

Instead, it serves as the reference implementation for future work involving:

- relational databases;
- application development;
- API design;
- user interfaces;
- automated testing;
- Quality Assurance;
- Domain-Driven Design.

The spreadsheet remains valuable because it captures the original business rules and demonstrates how the project evolved from a practical business solution into an engineering case study.

---

# Lessons Learned

Several important engineering lessons emerged during the development of this workbook.

## Solve Real Problems

The project originated from a genuine operational need rather than an academic exercise.

This ensured that every feature addressed an actual business requirement.

---

## Separate Responsibilities

Breaking processing into independent stages made the workbook easier to understand, test, and extend.

---

## Protect Users

Users should not be expected to understand implementation details.

The system should guide them toward success while preventing invalid output whenever possible.

---

## Validate Continuously

Validation should occur throughout processing rather than only at the beginning or the end.

Errors detected early are easier to diagnose and less likely to produce incorrect business results.

---

## Build for Change

The HeaderMap, QA layer, and staged architecture were all introduced because change was expected.

Designing for change proved more valuable than optimizing for a single report format.

---

# Looking Forward

The spreadsheet implementation represents the foundation of the Inventory Management project rather than its final form.

Future iterations are expected to preserve the business rules and engineering principles established here while moving the implementation toward a database-backed application with a modern user interface.

The lessons learned from the spreadsheet will continue to guide those future implementations.
