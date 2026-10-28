# Computer Helper — Requirements

**AI-led project** · Draft requirements, not yet verified · Updated October 28, 2026

I'm building this for two family members, one on Windows 11 and the other on a Mac. I still need to watch how they use their computers and find out where each of them gets stuck.

The goal is one easy place to ask for help, without a monthly AI subscription. The assistant should guide people, not take over their computers.

## Requirements

These are the things I want the finished helper to do. None of them should be treated as tested just because they're written down.

| ID | Priority | Requirement |
| --- | --- | --- |
| FR-01 | Must | One Help window that's easy to find, with readable text and clear controls. |
| FR-02 | Must | Give one instruction at a time, then wait for a response. |
| FR-03 | Must | Ask permission before inspecting a screen or current page. |
| FR-04 | Must | Open only a fixed list of approved local folders and programs. |
| FR-05 | Must | Explain the website already open without controlling the browser. |
| FR-06 | Must | Offer the same basic experience on Windows and Mac, with OS-specific code where needed. |
| FR-07 | Must | Leave passwords and sign-ins to a separate password manager. |
| FR-08 | Must | Make it obvious how to stop the assistant or withdraw screen access. |
| FR-09 | Should | Support local spoken questions and answers if the hardware can handle it. |
| FR-10 | Should | Allow optional public-information searches without sharing private screen contents. |
| FR-11 | Should | Admit uncertainty and provide a way to get human help. |
| FR-12 | Should | Offer larger text, stronger contrast, and adjustable speech speed. |
| FR-13 | Must | Run the main AI locally, without requiring a recurring cloud AI subscription. |
| FR-14 | Must | Let the AI request only registered specialist functions, with the application checking permission before any action. |
| FR-15 | Must | Search offline Windows/Mac help notes as reference material, never as commands. |
| FR-16 | Must | Let me change language models without rewriting every specialist. |
| FR-17 | Must | Never connect to a password vault or collect passwords. |
| FR-18 | Should | Find recent documents, photos, or downloads in approved folders using read-only searches—even when they aren't in Downloads. |
| FR-19 | Should | Prefer OS accessibility information when it can answer a screen question; use screenshots only with permission. |
| FR-20 | Should | Test useful performance on the existing 16 GB Windows computer before spending money on upgrades. |
| FR-21 | Must | Help someone who is lost in Windows get oriented or return to a familiar starting point without risking unsaved work. |
| FR-22 | Should | Recognize everyday language such as “type a letter” and guide the person to a familiar tool such as taskbar-pinned LibreOffice. |

## How I'll tell whether it works

It isn't enough for the program to respond. I need to see whether someone can find Help, ask a question, follow the next step, and stop or deny screen access without confusion.

I'll test actual tasks with each person's permission. I'll record what works, what causes trouble, and what needs to change—without uploading private information to GitHub. See the [test plan](Roadmap_and_Test_Plan.md), [uncle's everyday examples](Uncle_Use_Cases_and_Conversation_Tests.md), and [security limits](Security_and_Privacy.md).

The current [Python starter](prototype/) does not meet these requirements yet. It's a starting point for testing the conversation and local knowledge search, not a finished assistant.
