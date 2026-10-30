# SQL Refresher — Inventory Data Checks

**Project status:** **In Progress** · **Activity:** Active (planning; implementation not started)  
**Approach:** **Human-led** — I plan to design the database, write the SQL, and check the results myself.

## Why I'm Doing This

I have used SQL in coursework and in earlier technical work, but I want more practice writing queries without relying on notes. I'm keeping this project small so I can focus on the SQL and on checking whether the results make business sense.

## Starting Idea

Reuse the sanitized test data from my existing inventory workbook instead of building a separate fictional dataset. My starting three tables are **Parts**, **Warehouses**, and **Brands**. I originally said Vendors, but I meant Brands. A **line code identifies the brand under which a part is sold**, not necessarily the supplier or manufacturer. I chose to keep suppliers out of this first version so the SQL refresher stays manageable.

The source workbook is [InventoryDataValidation&ETLPipeline](https://docs.google.com/spreadsheets/d/1uV_BQui4tErYduIn34nPwPPoZCLOXqWDLpxW0HUBWQA/edit). It contains `Parts`, `Warehouses`, `Suppliers`, `LINES`, and `Categories` tabs. These are source data, not yet finished SQLite tables. `Parts` already has separate `Line_ID` and `Supplier_ID` fields. The line code is my sanitized identifier for a resale brand. One brand can have parts produced by multiple manufacturers, so I should not equate the brand with the manufacturer or supplier. Some reference tabs are incomplete or contain duplicates; I need to inspect and clean them before importing anything.

I want to practice writing queries that answer practical questions, including:

- Finding items with missing or mismatched records.
- Checking counts and totals after joins.
- Investigating duplicates without hiding data problems.
- Filtering, grouping, and explaining query results.
- Using parameterized queries when an application accepts a value such as a part number.

I will record the question, the SQL I wrote, the result, and what I found. No query results or tests have been completed yet.

## Table Design Decisions

I have now chosen a fourth table: **Inventory**. The first three are **Parts**, **Warehouses**, and **Brands**.

Inventory will connect a part to a warehouse and hold the **quantity on hand at that location**. My proposed fields are `Product_ID`, `Warehouse_ID`, and `Quantity_On_Hand`. I am also considering putting `Minimum_Quantity` in Inventory for simplicity. Before finalizing that choice, I need to establish whether the minimum is specific to each warehouse or the same across all warehouses.

The combination of product and warehouse is a candidate for a composite key, since one part can have inventory in several warehouses but should normally have one current quantity record per warehouse. The exact SQLite schema and constraints are not yet written.

## Demonstration

Start with readable SQL files and examples here on GitHub. If the queries work and the project stays manageable, I may make a small interactive demo for my portfolio.

Any interactive example should use **fictional records only** and should not expose the WordPress site's database or accept arbitrary SQL on the server. One option to evaluate later is a disposable SQLite database running entirely in a visitor's browser.

## My Next Step

Decide whether minimum stock levels vary by warehouse, then define the SQLite tables and write the first query myself. Before publishing source data, verify that all part numbers, addresses, and other details are suitable for public release.

## AI Transparency

I chose the goal and existing inventory dataset, clarified what line codes represent, selected **Parts, Warehouses, and Brands**, and proposed **Inventory** as the fourth table with warehouse-specific quantities and a possible minimum stock field. AI inspected the source workbook, asked about the business rules, and helped update these planning notes. I intend to design the schema and write and verify the SQL myself, using AI for explanations, review, and troubleshooting when needed.
