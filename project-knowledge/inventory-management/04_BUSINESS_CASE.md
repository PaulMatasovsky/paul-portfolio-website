# Business Case

## Purpose

This document explains the business problem that motivated the development of the Inventory Management ETL workbook and why the chosen solution was appropriate.

---

# Business Problem

Warehouse managers regularly needed to relocate groups of inventory within the warehouse.

To determine how much shelving space would be required, they first generated inventory reports from the warehouse management system.

Unfortunately, those reports sorted alphanumeric part numbers alphabetically instead of naturally. For example:

```
K10
K100
K11
```

instead of:

```
K10
K11
K100
```

Managers were manually reorganizing reports that sometimes contained more than 1,500 parts before they could be printed and used on the warehouse floor.

The process was repetitive, time-consuming, and prone to human error.

---

# Business Requirements

The solution needed to:

- Produce naturally sorted inventory reports.
- Support multiple report layouts for different warehouse tasks.
- Require little to no technical training.
- Integrate with the existing warehouse reporting process.
- Avoid requiring changes to the warehouse management system.
- Be maintainable if report formats changed in the future.

---

# Why a Spreadsheet?

A spreadsheet was selected because it met the operational constraints of the warehouse.

It required no software installation, used tools already familiar to warehouse personnel, and could be distributed simply by email. The solution could be adopted immediately without changing existing business processes.

---

# Business Value

The workbook significantly reduced the manual effort required to prepare inventory reports for warehouse moves.

By automating the sorting process and validating the results before printing, it improved both efficiency and confidence in the final reports while minimizing the amount of training required for end users.