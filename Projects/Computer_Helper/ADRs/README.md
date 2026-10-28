# Architecture Decisions to Work Through

**AI-led planning notes** · No decisions below have been accepted yet · Updated October 28, 2026

I use Architecture Decision Records (ADRs) to explain important choices and why I made them. These are questions I still need to research and test, not finished decisions. I'll follow the [existing ADR process](../../../Documentation/ADRs/ADR-000.md) when I'm ready to record a decision.

| ID | Decision to make |
| --- | --- |
| 000 — Local control | Which folders and apps can the assistant open, and how do I enforce that list? |
| 001 — Windows and Mac | What can share Python code, and what needs a separate OS adapter? |
| 002 — Local AI | Which small model gives clear, reliable help on the computers available? |
| 003 — Reading the screen | Can accessibility information do the job, or will screenshots or vision models be needed? How do I protect sensitive information? |
| 004 — Passwords | How do I keep password managers and account recovery entirely outside the assistant? |
| 005 — Specialists | Which tasks need AI, which need ordinary Python, and how should they communicate? |
| 006 — Knowledge search | When is simple text search enough, and when would SQLite FTS or embeddings help? How will I maintain the notes? |
| 007 — Hardware | How does the model perform on the existing i5-8500 and 16 GB RAM before I consider upgrades? |
| 008 — Packaging | When should the terminal prototype become a GUI and an offline installer? |

AI helped draft these questions based on my goals and our discussions. They are not accepted, independently authored ADRs.
