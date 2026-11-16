# Portfolio Website — AI Collaboration and Authorship

**Project type:** AI-led visual design and documentation; human-led content and structure.  
**Documentation:** AI drafted this document from our working sessions and my decisions. It is not independently authored prose.

## Version History

| Version | When | What happened | Who led |
|---|---|---|---|
| 1.0 | July 2026 | I built the site. AI wrote most of the GitHub documentation, and it grew past what I could clearly call mine, so I started over. | AI-led |
| 2.0 | August 2026 | I rebuilt the site and wrote the documentation, using AI where I got stuck or to interview me and draft from my answers. | Human-led |
| 2.5 | November 2026 | AI redesigned how the site looks. The pages, structure, and text stayed mine. | AI-led |

I call this 2.5 and not 3.0 because the purpose, pages, and structure of the site did not change. Only the presentation did.

**Status of 2.5:** Published. I reviewed the drafts and published all ten pages on November 14, 2026. The old pages are unpublished and held for review.

## Who Did What in Website 2.5

| Area | My role | AI's role | What the current evidence shows |
|---|---|---|---|
| Goal | Asked for a professional look that keeps Shibumi, and for the site to show my skills, not describe them | Asked what roles I'm aiming for | I set the brief |
| Critique of 2.0 | Asked for a blunt review and supplied four screenshots | Wrote the critique | AI's assessment, from my screenshots |
| Colors, fonts, spacing, layout | Went with the palette AI recommended | Proposed all of it, including two alternative palettes | AI's design; my approval |
| Mockup | Reviewed it | Built a Home page mockup in three color versions | AI-built |
| Site structure and pages | Decided these in Website 2.0; unchanged | None in 2.5 | Mine |
| Page text | Existing text carried over as written | Rewrote the Home headline and two project headlines; removed empty headings and leftover editor markup | Mine, except the three Home headlines, which are AI's wording and which I kept |
| Stylesheet | None | Wrote it | AI-written CSS |
| Building the pages | Set the limits: drafts only, nothing published or deleted, no changes to existing pages, backup first | Built ten draft pages in WordPress by script and checked that no original text was dropped | AI-built drafts |
| Review and publishing | Reviewed the drafts, fixed the page addresses, and published each page | None | Live site, November 14, 2026 |
| Fixes after launch | Asked for them | Fixed the Insights page, restyled the blog post and 404 templates, and corrected one page address and a menu color | Done by AI at my request, November 15, 2026 |
| Accuracy check | Asked AI to list every inconsistency between the site and this repository, then had AI correct the ones on the site | Listed them and made the site corrections | Site corrected November 15, 2026 |
| Blog post about 2.5 | Reviewed it and approved publishing | Wrote it; the post says so in its first line | Published November 15, 2026 |

I can't honestly put a percentage on who contributed what, so I'm not going to.

## What I Can Claim

The structure of the site, the choice of projects, and what each page says are mine. So are the limits I set for how AI could work on the live site, and the decision to publish.

The way the site looks in 2.5 is not my design. I can explain the choices, but I did not make them. The stylesheet is not my code.

Most of the documentation in this repository's `Documentation` folder was drafted by AI from my decisions. The ADRs are the exception: I write those myself, as [ADR-000](ADRs/ADR-000.md) requires.

## Known Limits

- The redesign is one custom stylesheet applied to standard Divi modules. It is stored in Divi's Theme Options and is not yet set up as Divi design variables or presets.
- The header, footer, blog post, and 404 templates were not rebuilt. The stylesheet restyles the existing ones.
- I have not yet run a QA audit of the redesigned site.

## Evidence

Screenshots and the build record are in [Evidence/Website_2.5](Evidence/Website_2.5/).
