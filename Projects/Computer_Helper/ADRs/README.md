# Decisions I Still Need to Make

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

I use ADRs to record important choices and why I made them. I'm keeping these as questions for now, because I haven't researched the alternatives or made the technical decisions yet. My [ADR process](../../../Documentation/ADRs/ADR-000.md) explains how I handle accepted records.

| Decision | What I need to figure out |
| --- | --- |
| 000 — Local control | Which folders and programs should the assistant be allowed to open, and how will I test those limits? |
| 001 — Windows and Mac | Which parts can share code, and which need a separate solution for each system? |
| 002 — Local AI | Which model works well enough on the computers available, without a monthly subscription? |
| 003 — Reading the screen | Should I use screenshots, accessibility information, or both? How can I avoid sensitive information? |
| 004 — Passwords | How will I keep each person's password manager separate from the assistant and plan for account recovery? |

These notes were drafted with AI. They aren't accepted ADRs.

## Additional decisions under review (not accepted ADRs)

| Decision | What I need to evaluate |
| --- | --- |
| 005 — Orchestrator and specialists | Which requests are handled by Python services versus separate AI models; how do modules communicate and fail safely? |
| 006 — Knowledge retrieval | Start with local text search; compare with SQLite FTS and embeddings only when needed. How will reference documents be reviewed and updated? |
| 007 — CPU performance and hardware | Benchmark 3B/4B models with 16 GB RAM and the browser open before approving RAM or low-profile GPU purchases. |
| 008 — Development and packaging | Begin with Ollama + Python CLI, then introduce GUI and offline installers only after functionality works. |

The approach above emerged from user-directed planning with AI help. It is not an accepted, user-authored ADR. The current source scaffold is not proof of model performance or security.

