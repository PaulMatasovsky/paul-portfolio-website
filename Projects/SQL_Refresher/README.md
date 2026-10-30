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

Inventory will connect a part to a warehouse and hold both the **quantity on hand** and the **minimum quantity for that specific warehouse**. My selected starting fields are `Product_ID`, `Warehouse_ID`, `Quantity_On_Hand`, and `Minimum_Quantity`. The minimum belongs here because each warehouse sets stock levels according to its own demand, rather than sharing one minimum for the part everywhere.

The combination of product and warehouse is a candidate for a composite key, since one part can have inventory in several warehouses but should normally have one current quantity record per warehouse. The exact SQLite schema and constraints are not yet written.

### Warehouses — columns I've chosen

My current `Warehouses` design has **six confirmed columns**:

- `Warehouse_ID` — identifies the location.
- `Warehouse_Name` — the location's name.
- `Warehouse_Address` — its address (whether to split this into address components is not yet decided).
- `Is_Hub` — Boolean-style indicator: `1` for a hub and `0` for a spoke.
- `Primary_Hub_ID` — identifies the one hub responsible for a spoke's automatic replenishment; this will reference another warehouse.
- `Route_ID` — identifies the one delivery route assigned to a warehouse.

I deliberately left stock on hand and minimum stock out of this table; those belong in `Inventory` for each part-and-warehouse combination.

### Warehouses — initial data type ideas

My first pass at the SQLite types is:

- `Warehouse_ID`: an integer identifier (`INTEGER`).
- `Warehouse_Name`: text (`TEXT`).
- `Warehouse_Address`: text (`TEXT`).
- `Route_ID`: text (`TEXT`), assuming route codes may contain letters.
- `Is_Hub`: **required `INTEGER`, limited to `0` or `1`**. I chose `1` for a hub and `0` for a spoke because each warehouse must be one or the other; leaving the status blank or allowing another value would undermine the business rule.
- `Primary_Hub_ID`: `INTEGER` referencing a warehouse ID. I decided that it **must be present for spokes** and **must be `NULL` for hubs** in this version.

I had momentarily forgotten `Primary_Hub_ID` while listing the types. It answers a different question from `Is_Hub`: **which hub supplies this spoke**, rather than **is this warehouse a hub**. SQLite commonly represents Boolean-style fields as integer values 0 and 1. I decided that the schema **must use both `NOT NULL` and `CHECK (Is_Hub IN (0, 1))`**: the first requires a value, and the second rejects values other than 0 and 1. These are planning notes only; no `CREATE TABLE` statement or constraints have been written yet.

### Design consideration — warehouse routes

I considered whether a warehouse might belong to several delivery routes. If that were necessary, a separate junction table could represent a many-to-many relationship. **I decided instead that each warehouse will belong to only one route in this project**, and several warehouses can share the same route. This is technically a **one-to-many relationship from routes to warehouses**, rather than a strict one-to-one relationship. Storing `Route_ID` directly in `Warehouses` is sufficient for the chosen rule; I am not introducing a route-membership junction table.

The exact SQLite types, constraints, and whether to create a separate `Routes` lookup table are still to be decided. I also plan to add more sanitized or fictional locations so route groupings can be demonstrated.

### Replenishment rule I described

The operation uses a **hub-and-spoke** distribution model. Hubs receive inventory from suppliers and hold additional stock to replenish spoke warehouses. Spokes avoid unnecessary excess stock and are replenished according to their own minimum-on-hand needs. At my location, a part sold today will typically appear in stock replenishment about **2–3 days later**. The on-hand quantity changes as sales and replenishments occur.

I decided from the outset that each warehouse should be identified as a **hub** or **spoke** in the Warehouses table. I confirmed this is worth including because it adds little complexity and demonstrates understanding of how the operation works. I chose `Is_Hub` as a Boolean-style integer flag instead of storing the words `Hub` and `Spoke`; the SQL constraints are not yet finalized.

**Automatic replenishment, customer-specific orders, and stock transfers are different processes.** Each spoke has exactly **one primary hub responsible for its automatic replenishment**. That hub supplies the spoke **from the hub's own stock**; it does not specially order inventory from another location in order to fulfill the automatic replenishment. A location may receive stock through separately authorized transfers from other warehouses, but those transfers are not an unrestricted way for spoke locations to replenish themselves. Customer-specific orders follow a different workflow from routine stock transfers. The public project describes these as generalized business rules, without publishing internal company permission details.

I chose `Primary_Hub_ID` as a fifth Warehouses field so a spoke can point to its one assigned automatic-replenishment hub. **I decided that a spoke (`Is_Hub = 0`) requires a primary hub ID, while a hub (`Is_Hub = 1`) leaves that column `NULL`.** This models the replenishment relationships I know about; I have not assumed any additional upstream warehouse tier. My current understanding is that hubs receive supplies from external suppliers, but the supplier structure is outside this small project's scope. If I later modeled supplier sourcing, that would be a different relationship and would need its own business rules.

When writing the schema, I can enforce the missing-versus-present rule with a conditional table-level `CHECK`, and use a self-referencing foreign key to require an existing warehouse ID. An ordinary foreign key **does not by itself guarantee that the referenced warehouse is actually a hub**; enforcing that would require another validation approach. I still need to write and test the constraints myself. I do not need a separate transfer-history table just to practice the joins. This is business context, not a claim that this project already tracks shipments, transfers, orders, user permissions, or replenishment events.

## Demonstration

Start with readable SQL files and examples here on GitHub. If the queries work and the project stays manageable, I may make a small interactive demo for my portfolio.

Any interactive example should use **fictional or verified-public-safe sanitized records only** and should not expose the WordPress site's database or accept arbitrary SQL on the server. One option to evaluate later is a disposable SQLite database running entirely in a visitor's browser.

## My Next Step

Work out how to validate `Primary_Hub_ID`, including making it present for spokes and empty for hubs, then write the SQLite table definitions and tests myself. Before publishing source data, verify that all part numbers, addresses, and other details are suitable for public release.

## AI Transparency

I chose the goal and existing inventory dataset, clarified what line codes represent, selected **Parts, Warehouses, and Brands**, and chose **Inventory** as the fourth table with warehouse-specific quantities and minimum stock levels. I also explained the hub-and-spoke replenishment process, confirmed that I wanted the hub/spoke distinction recorded on each warehouse from the beginning, and distinguished each spoke's single automatic-replenishment hub from optional interwarehouse transfers. AI inspected the source workbook, asked about the business rules, and helped update these planning notes. I selected the warehouse columns, confirmed `Primary_Hub_ID` as the fifth column, decided to include `Route_ID` as the sixth, and chose `Is_Hub` (0 or 1) instead of the text-based `Warehouse_Type`. I considered multiple-route membership but chose one assigned route per warehouse for this project. I also required `Is_Hub` to be non-null and limited to 0 or 1, and chose to require `Primary_Hub_ID` for spokes while leaving it `NULL` for hubs in the current project model. I intend to design the schema and write and verify the SQL myself, using AI for explanations, review, and troubleshooting when needed.
