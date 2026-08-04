# Lessons Learned

## Purpose

This document captures the most important engineering lessons learned while developing the spreadsheet ETL. Many of these insights influenced how I now approach software development projects.

---

# Design for the User

The workbook was built for warehouse managers rather than technical users.

Keeping the workflow simple proved more valuable than exposing additional functionality. A successful solution is one that people are comfortable using correctly.

---

# Separate Responsibilities

As the workbook evolved, responsibilities were divided across multiple worksheets instead of adding more logic to a single location.

This made the system easier to understand, maintain, and troubleshoot.

---

# Expect Change

The introduction of HeaderMap came from the realization that report formats eventually change.

Designing for change early reduced future maintenance and made the workbook more resilient.

---

# Validate Continuously

One of the most valuable additions was the QA worksheet.

Rather than assuming each processing stage worked correctly, the workbook verifies its inputs and outputs before allowing reports to be printed.

---

# Preserve Business Knowledge

The spreadsheet now represents more than a working solution.

It documents business rules, operational assumptions, and engineering decisions that can guide future implementations using different technologies.

---

# Looking Back

Developing this project helped change the way I think about software engineering.

Today I place greater emphasis on understanding the business problem first, documenting assumptions, separating responsibilities, and designing systems that can evolve over time.