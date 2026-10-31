# ETL Project — Development History and Retrospective

**Recorded:** October 26, 2026 (retrospective)  
**Expanded:** October 30, 2026

**AI transparency:** AI helped me reconstruct and draft this history from our conversations, and helped revise the wording. During development, I used AI for research and troubleshooting, including a later review of the workbook. This is a retrospective, not a journal I kept at the time. The working template does not use AI to process reports.

## How It Started

My supervisor mentioned how much time he was spending sorting an inventory report by hand. I asked why, and he explained that the company's website used to sort the parts correctly, but something had changed. The manual sorting had taken over an hour. He had already contacted IT, but the fix wasn't a high priority.

I figured there had to be a better way, so I decided to see what I could do about it.

I developed the first usable version over about two weeks, finding time between pulling parts, dispatching, answering phones, and my other work. That included restarting the workbook in Google Sheets after beginning in LibreOffice. I had something he could use before the original website's sorting problem was fixed. The later troubleshooting and refinements continued after that first version.

## Making It Easy to Use

From the beginning, I wanted a low-tech, paste-and-print process. Some of the people at work aren't particularly comfortable with spreadsheets, and I didn't want them to have to touch formulas to print an inventory report.

I kept the three report choices from the original website: Part Number, Line, and Category. Those weren't new features I invented; they were options people already knew. I hoped managers at other branches could eventually use the template too, although I haven't confirmed that it spread beyond my supervisor and possibly one other person.

## Figuring Out the Part Numbers

The hardest problem at first wasn't the final sort. It was separating the different part-number formats into a prefix, numeric root, and suffix so they could be sorted properly.

After years of working with these parts, I already recognized most of the troublesome formats. The challenge was turning that knowledge into spreadsheet logic. I tried several approaches before settling on a decision tree that handles the different patterns.

Most reports would probably never include all those formats together, but I figured anything worth doing was worth doing correctly. I didn't want the next unusual part number to break the results.

## Changing Tools

I started building the workbook in LibreOffice. Partway through, I ran into unwanted blank rows when printing the reports. There was also a practical limitation: not every company computer had Excel installed, but they did have internet access.

I restarted the workbook in Google Sheets. That fixed the printing problem in the version we use and let my supervisor access it from different computers with the appropriate account.

While figuring out the printing issue, I learned that a formula in one Google Sheets cell could populate an entire range. I used that approach to bring the headers from RawData into HeaderMap, and it became useful elsewhere in the workbook.

I later adapted the workbook for Excel so I could provide a downloadable copy on my portfolio. That copy still prints extra blank rows, so Google Sheets remains the operational version. The reasons for the platform change are in [ADR-001](../ETL_ADR/ADR-001.md).

## Testing, Feedback, and Validation

I kept pasting in different test part numbers, checking one section of the formulas at a time and setting aside unrelated errors while I worked on that piece. Eventually I made a dedicated test data sheet because I was doing this so often.

The validation checks grew over time. My first one was a template overflow check. At a previous job, I'd learned how serious a cut-off report could be. In this case, missing rows could make the parts list and inventory counts inaccurate, even if the report looked normal. I added other checks as I thought of things that could go wrong.

I also wanted the workbook to be easier to repair if a source header changed. The columns weren't routinely moving around, but different capitalization or an altered header could break a formula. After researching possible approaches through Google and AI, I adopted header mapping. It recognizes supported header variations and helps identify an unrecognized one instead of relying on fixed column positions.

I tested the first usable version before handing it to my supervisor. He found issues during actual use, returned it, and we went through that process a few more times.

Some sorting inconsistencies were stubborn. At first I used AI in a separate chat to talk through possible causes while I worked on the formulas myself. Much later, when the workbook was already usable but the sort order still wasn't consistently right, I had AI examine the workbook directly. It helped find a mistake: I'd added leading zeros for certain letter-based sorting values when I needed trailing zeros. AI also suggested some additional validation checks during that review.

## What I Took Away

The template reduced a task taking over an hour to less than five minutes, and my supervisor still uses it.

This project reminded me that getting a formula to run isn't the same as getting the right report. I needed to test the output, listen when the person using it found a problem, and keep the process simple enough that it actually helped.

For the detailed formula flow and expected behavior, see the [Technical Overview](../../Technical_Overview.md) and [Business Rules](../../Business_Rules.md).
