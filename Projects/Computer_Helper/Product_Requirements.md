# Product Requirements

**Status:** Draft v0.1 · 2026-10-26

## Audience and goal

Two prospective family users—one on Windows and one on macOS—may benefit from help with everyday computer tasks. Their exact needs and hardware are not yet verified.

**Goal:** Make assistance available through one predictable, approachable interface, without adding a recurring AI subscription.

## Functional requirements

| ID | Priority | Requirement |
| --- | --- | --- |
| FR-01 | Must | One easy-to-find Help interface with large controls and readable text. |
| FR-02 | Must | Plain-language guidance: one actionable step, then wait for the user. |
| FR-03 | Must | Inspect the current screen only when requested and permitted. |
| FR-04 | Must | Open only approved local folders or applications. |
| FR-05 | Must | Explain the current user-opened webpage without interacting with it. |
| FR-06 | Must | Consistent experience across Windows and macOS with separate OS adapters. |
| FR-07 | Must | Keep credentials and password management outside the assistant. |
| FR-08 | Must | Make Stop, Exit, and permission withdrawal obvious. |
| FR-09 | Should | Offline voice input and spoken output if usable on the hardware. |
| FR-10 | Should | Explicit public-information search without sharing private screen content. |
| FR-11 | Should | Say when uncertain and offer a human-support fallback. |
| FR-12 | Should | Adjustable text size, contrast and speech speed. |

The exact allowed and prohibited operations are defined in [Security and Privacy](Security_and_Privacy.md), rather than repeated here.

## Usability acceptance criteria

In tests with consent, check that each participant can:
1. Open the helper and ask a question with minimal coaching.
2. Follow a single instruction without being overwhelmed.
3. Stop the assistant and understand when screen access is active.
4. Find a local folder or complete a low-risk task with guidance.

Record the observed outcome and any assistance needed; do not presume success. The [Roadmap and Test Plan](Roadmap_and_Test_Plan.md) contains the functional and adversarial cases.

## Questions before implementation

Which tasks actually cause difficulty? Do users prefer voice or text? Can their devices run a suitable local model? What screen and accessibility permissions will each OS require? Use the [Device Survey](Device_Survey.md) to collect answers privately.

**V1 is usable** only after the approved local actions, screen guidance, refusal behavior, and fallback have been demonstrated on a named operating-system version.
