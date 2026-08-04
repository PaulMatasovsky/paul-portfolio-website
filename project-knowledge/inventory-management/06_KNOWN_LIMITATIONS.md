# Known Limitations

## Purpose

No software solution is without tradeoffs. This document records the current limitations of the spreadsheet implementation so they can be understood, evaluated, and addressed in future iterations.

---

# Current Limitations

## Workbook Capacity

The current workbook supports approximately 2,000 inventory records. Larger datasets require expanding the template.

---

## Duplicate Detection

Duplicate detection currently evaluates only the part number.

Future implementations should define a complete business key before expanding this validation.

---

## Part Number Parsing

The parsing logic was designed around the part number formats commonly found in the warehouse where the workbook was developed.

Additional edge cases and uncommon formats have not yet been formally validated.

---

## Spreadsheet-Based Implementation

The workbook relies on spreadsheet formulas to implement business logic.

While effective for the original problem, spreadsheet formulas become increasingly difficult to maintain as complexity grows.

---

## Manual Maintenance

Supporting new report formats currently requires updating the HeaderMap synonym table.

Although this process is straightforward, it is still a manual maintenance task.

---

# Future Improvements

Potential future improvements include:

- Expanded validation of uncommon part number formats.
- More robust duplicate detection based on business rules.
- Increased workbook capacity.
- Additional automated testing.
- Migration of business logic into a database-backed application while preserving the documented business rules.

These improvements represent opportunities for future development rather than deficiencies in the current solution.