# Project Overview
Manually sorting warehouse parts reports could take over an hour and was prone to errors. Different part-number formats and inconsistent source layouts made the process more complicated.

I developed an automated spreadsheet workflow that interprets and sorts the data with minimal user interaction. The system produces three print-ready reports, organized by part number, product line, or category, for warehouse planning and operations.
 
 
## How it Works
- Input: Obtain the source report, clear the RawData worksheet, and paste the entire report, including its headers.
- Processing: The workbook automatically processes the data and prepares three sorted reports.
- Output: Select the desired report (Part Number, Line, or Category) and print it.

 
## Key Features
- Part-number sorting: Handles complex part-number structures, including prefixes, numbers, and suffixes.
- Dynamic header mapping: Accommodates changes in source column positions.
- Built-in validation: Checks for missing fields, data discrepancies, and template overflow.
 
 
## Project Files and Documentation
- [Workbook](https://github.com/PaulMatasovsky/paul-portfolio-website/blob/main/Projects/ETL/FINAL_Automated_Sorting_Template.xlsx): The downloadable Excel file and Google Sheets demonstration.
- [Business Rules](https://github.com/PaulMatasovsky/paul-portfolio-website/blob/main/Projects/ETL/Business_Rules.md): What the system is required to do.
- [Technical Overview](https://github.com/PaulMatasovsky/paul-portfolio-website/blob/main/Projects/ETL/Technical_Overview): How the system implements those requirements.
- [ADRs](https://github.com/PaulMatasovsky/paul-portfolio-website/tree/main/Projects/ETL/ETL_Documentation/ETL_ADR) and [Project Journal](https://github.com/PaulMatasovsky/paul-portfolio-website/tree/main/Projects/ETL/ETL_Documentation/ETL_Learning_Journal): Design decisions and lessons learned.
- [Screenshots](https://github.com/PaulMatasovsky/paul-portfolio-website/tree/main/Projects/ETL/ETL_Documentation/Supporting_Evidence/Screenshots): Visual evidence of the workflow and results.

 
## Status & Future Development
### Current Status
The spreadsheet workflow is complete and is currently used in actual warehouse operations.
The project remains available for maintenance and improvements.
- [Google Sheets](https://docs.google.com/spreadsheets/d/1-h7BjpiVBTfXUplCqvHsUb9QcV0sLdSG287sO5V9kcM/edit?usp=sharing) is a copy of the original.
- [Excel](https://github.com/PaulMatasovsky/paul-portfolio-website/blob/main/Projects/ETL/FINAL_Automated_Sorting_Template.xlsx) version for downloading and viewing.

### Future Development
Add a database backend, potentially using SQL.
Develop a user-friendly dashboard.
Automate importing source data, eliminating the manual copy-and-paste process.
