# ETL Project — Retrospective Learning Journal

**Date Recorded:** October 26, 2026  
**Entry Type:** Retrospective

**AI Transparency:** AI helped me reconstruct and draft this retrospective from earlier project discussions. I also used it to troubleshoot difficult formulas during development and to revise this wording later. This is not an original journal entry written at the time.

## How It Started

We had been using a company website to sort our warehouse parts reports. When that website stopped working, IT considered the issue a low priority, so my boss started sorting the part numbers manually. It could take more than an hour, and at least once it took longer.

I thought I could put together a temporary workaround that would save him some time. I started with LibreOffice and worked on a spreadsheet where he could paste in the report, choose the order he wanted, and print it.

## Why I Switched to Google Sheets

Partway through, I kept getting unwanted blank rows in the printed LibreOffice reports. There was another practical issue: not every company computer had Excel installed, although they did have internet access.

I decided to restart the workbook in Google Sheets. That meant my manager could open it from different company computers with the appropriate account. More importantly, it solved the printing problem for the version we actually use.

The whole project took roughly two weeks, working during spare time between my regular warehouse duties. Almost all the work happened there. I spent only about half an hour to an hour at home on formatting and troubleshooting. That two-week period includes the time I spent restarting it in Google Sheets.

## Something I Learned Along the Way

While working on the printing issue, I found out that a formula in one Google Sheets cell could populate an entire row or column.

I hadn't known about that feature before. I used it to bring the headers from RawData into HeaderMap, and it turned out to be important in avoiding the extra blank printed rows.

It changed how I thought about the workbook. Rather than fill a large area with individual formulas, I could have a single formula produce the range I needed.

## The Hardest Part

I generally enjoy troubleshooting, but a few formula problems kept coming back even after I had revised them several times.

I eventually brought AI into the process as another troubleshooting resource. It helped me identify and resolve problems I hadn't been able to get past on my own.

## What I Took Away

This was a reminder that I need to choose tools based on where and how they'll actually be used, not just stick with the first one I picked.

I also learned a new approach to spreadsheet formulas and reinforced something I've found important in other work: a formula running without errors doesn't automatically mean the finished report is correct. I still need to check the output.

The Google Sheets workbook is used in warehouse operations. I later made an Excel copy for my portfolio, although that version still has the blank-row printing limitation.
