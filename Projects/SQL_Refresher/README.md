# SQL Refresher — Inventory Data Checks

**Project status:** **In Progress** · **Activity:** Active (planning; implementation not started)  
**Approach:** **Human-led** — I plan to design the database, write the SQL, and check the results myself.

## Why I'm Doing This

I have used SQL in coursework and in earlier technical work, but I want more practice writing queries without relying on notes. I'm keeping this project small so I can focus on the SQL and on checking whether the results make business sense.

## Starting Idea

Reuse the sanitized test data from my existing inventory workbook instead of building a separate fictional dataset. I chose to begin with three tables: **Parts**, **Warehouses**, and **Vendors**, using the inventory line code to connect vendors to parts if the underlying business rules support that relationship.

The source workbook is [InventoryDataValidation&ETLPipeline](https://docs.google.com/spreadsheets/d/1uV_BQui4tErYduIn34nPwPPoZCLOXqWDLpxW0HUBWQA/edit). It contains `Parts`, `Warehouses`, `Suppliers`, `LINES`, and `Categories` tabs. These are source data, not yet finished SQLite tables. In particular, `Parts` has both `Line_ID` and `Supplier_ID`, so I still need to decide whether a line code identifies a vendor or a product line. Some reference tabs are incomplete or contain duplicates; I need to inspect and clean them before importing anything.

I want to practice writing queries that answer practical questions, including:

- Finding items with missing or mismatched records.
- Checking counts and totals after joins.
- Investigating duplicates without hiding data problems.
- Filtering, grouping, and explaining query results.
- Using parameterized queries when an application accepts a value such as a part number.

I will record the question, the SQL I wrote, the result, and what I found. No query results or tests have been completed yet.

## Demonstration

Start with readable SQL files and examples here on GitHub. If the queries work and the project stays manageable, I may make a small interactive demo for my portfolio.

Any interactive example should use **fictional records only** and should not expose the WordPress site's database or accept arbitrary SQL on the server. One option to evaluate later is a disposable SQLite database running entirely in a visitor's browser.

## My Next Step

Review how `Line_ID` relates to `Supplier_ID` in the existing data, and decide how parts should be connected to warehouses. Then I will define my SQLite tables and write the first query myself. Before publishing source data, verify that all part numbers, addresses, and other details are suitable for public release.

## AI Transparency

I chose the goal, selected the inventory dataset from my existing work, and proposed the first three tables and intended line-code relationship. AI inspected the source workbook, flagged an ambiguity between line codes and supplier identifiers, and helped draft these planning notes. I intend to make the schema decisions and write and verify the SQL myself, using AI for explanations, review, and troubleshooting when needed.
