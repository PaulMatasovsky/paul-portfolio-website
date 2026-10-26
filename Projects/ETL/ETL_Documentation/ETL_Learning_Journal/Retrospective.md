# ETL Project — Retrospective Learning Journal

**Date Recorded:** October 26, 2026  
**Entry Type:** Retrospective

**AI Transparency:** AI assisted with reconstructing and drafting this journal entry from earlier project discussions. AI also helped me troubleshoot and resolve persistent errors during workbook development.

## Where I Started

We had been using a company website to sort our warehouse parts reports, but one day it stopped working. IT considered the problem a low priority, so my boss started sorting the part numbers by hand. That could take over an hour, and on at least one occasion it took even longer.

I thought I could make a temporary workaround to save him time. I started building a spreadsheet in LibreOffice that would let him paste in the report, select a sorted output, and print it.

## Development and the Decision to Change Platforms

Partway through the project, I kept running into blank rows in the printed LibreOffice reports. I also wanted the workbook to be accessible from different company computers, not all of which had Excel installed, even though they all had internet access.

I restarted the project in Google Sheets. That gave my manager access from any company computer with the appropriate login and, more importantly, solved the blank-row printing problem for the operational version.

The project took roughly two weeks of work during spare time between my regular duties. Nearly all of that work happened at the warehouse. I spent only about half an hour to an hour at home, mainly working on formatting and troubleshooting. That two-week period included restarting the workbook in Google Sheets.

## The Most Important Technical Discovery

While looking for a way around the printing problem, I learned how to use Google Sheets formulas that populate an entire row or column from a single starting cell.

I had not known that capability existed. I used it to bring the header row from RawData into HeaderMap, and it was central to avoiding the unwanted blank rows when printing.

That discovery changed how I approached the workbook. Instead of filling large areas with individual formulas, I could let a formula produce the range of results needed.

## The Hardest Challenge

Troubleshooting has always been one of my strengths, but several persistent formula errors continued to cause problems even after multiple revisions.

I used AI as an additional troubleshooting resource to identify and resolve those issues. That allowed me to move past problems I had repeatedly worked on without getting the results I needed.

## What I Took Away

This project reinforced the importance of choosing a tool based on the actual work environment, not just the tool I started with.

It also taught me a new way to work with spreadsheet formulas and reinforced the importance of checking the finished output instead of assuming that a working formula always produces a reliable report.

The Google Sheets version is used for warehouse operations. I later made an Excel version available for downloading and viewing as part of my portfolio, although it still has the blank-row printing limitation.
