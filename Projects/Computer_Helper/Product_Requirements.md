# Product Requirements

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

**Status:** Draft v0.2 · 2026-10-28

## Who it's for

I'm planning this for two family members: one uses Windows, and the other uses a Mac. Both could benefit from a simpler way to get computer help, although I still need to find out exactly what each person struggles with.

My goal is to give them **one place to ask questions** without requiring another monthly subscription.

## Requirements

| ID | Priority | What I want |
| --- | --- | --- |
| FR-01 | Must | A Help window that's easy to find, with large buttons and readable text. |
| FR-02 | Must | One clear instruction at a time, then wait for the person's response. |
| FR-03 | Must | Screen help only when the person asks for it and gives permission. |
| FR-04 | Must | The ability to open a short list of approved local folders and programs. |
| FR-05 | Must | Guidance for the website already open, without controlling the browser. |
| FR-06 | Must | The same basic experience on Windows and macOS, using separate OS-specific code where necessary. |
| FR-07 | Must | Passwords and sign-ins handled outside the assistant. |
| FR-08 | Must | An obvious way to stop, close, or withdraw screen access. |
| FR-09 | Should | Spoken questions and answers, preferably offline, if the hardware supports it. |
| FR-10 | Should | Optional searches for general public information, without sharing private screen content. |
| FR-11 | Should | An honest “I don't know” and a way to get human help. |
| FR-12 | Should | Options for larger text, stronger contrast, and slower speech. |

[Security and Privacy](Security_and_Privacy.md) defines which actions are allowed and which are blocked.

## How I'll judge whether it helps

I'll need to watch each person try a few everyday tasks, with their permission. Can they find Help, ask a question, follow the instructions, and stop the assistant when they want to? Do they know when it can see their screen?

I don't have answers to those questions yet. The [test plan](Roadmap_and_Test_Plan.md) is where I'll record the results.

Before choosing the software, I also need to check both computers' hardware and find out whether typing or talking feels more natural to each person. The [device survey](Device_Survey.md) covers that work.

I won't call the first version usable until the local actions, screen guidance, and safety restrictions have been tested on the actual operating system.

## Additional implementation requirements (proposed)

| ID | Priority | What I want |
| --- | --- | --- |
| FR-13 | Must | Local model inference for the baseline assistant, with no recurring cloud AI subscription. |
| FR-14 | Must | A main conversation component that can request only explicitly registered specialist functions, after application-side validation. |
| FR-15 | Must | Offline Windows/macOS reference documents retrievable as data, not as instructions to the AI. |
| FR-16 | Must | The ability to replace the language model without rewriting OS-specific specialists. |
| FR-17 | Must | No direct access to a password vault, and no collection of passwords. |
| FR-18 | Should | Search approved local folders for recent photos or downloads using read-only, bounded queries. |
| FR-19 | Should | Prefer OS accessibility descriptions over screenshots when sufficient; ask before any screen inspection. |
| FR-20 | Should | Work at acceptable speed with the uncle's existing 16 GB of RAM before evaluating upgrades. |

The **initial Python scaffold is not an accepted implementation of these requirements**. These are criteria for later tests, not completed features.

