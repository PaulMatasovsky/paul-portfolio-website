# Computer Helper — Cross-Platform Assisted Computing

**Status:** Planning / requirements definition (2026-10-26). No application, prototype, user testing, or production deployment has been completed.

## Problem

Some people struggle to navigate their computers and unfamiliar websites, especially when they must remember different procedures or locate documents and accounts. Keeping a password list does not address the broader difficulty of knowing what to do next.

This project began with the goal of making computing easier for an older family member using Windows. The design also includes a second family user on macOS from the start. No names, credentials, real account details, or private screen images belong in this public repository.

## Intended solution

**One approachable Computer Helper application** offering typed and, if feasible, spoken guidance. The assistant should explain the currently selected screen in simple, sequential instructions. It may open a small allowlist of local folders and applications; it must never autonomously navigate websites, click webpage controls, submit forms, or access a password vault.

- **Windows:** initial evaluation and implementation target.
- **macOS:** a first-class target with its own platform adapter and accessibility/permission testing.
- **Offline-first:** local model and locally processed screen context preferred; optional internet *reference searches* must be explicitly initiated and must not include private screen content.
- **Cost target:** no additional recurring AI subscription; feasibility depends on the devices' actual capabilities.
- **Passwords:** use a separate password manager (Norton is being considered); the AI never handles credentials.

A local model is a candidate, not a verified design choice. Ollama, on-device vision, offline speech recognition, and platform accessibility interfaces will be evaluated after device discovery.

## Primary scenarios

| User asks | Expected behavior |
| --- | --- |
| “Where are my pictures?” | Offer to open the OS Pictures folder; open only the approved local destination. |
| “How do I print this?” | With user permission, inspect the current screen and give *one step at a time*. |
| “I'm on my bank website. Where are my statements?” | Explain the website already open, if safe to inspect; do **not** click, open URLs, log in, or submit. |
| “What's my password?” | Refer to the independent password manager without retrieving or speaking secrets. |

## Boundaries

The assistant is a **guide with limited local actions**, not an autonomous computer agent. Permissions must be enforced by application code, not merely by an AI prompt. Users should explicitly choose when their screen is inspected, and sensitive websites should default to no capture.

## Documentation

- [Product Requirements](Product_Requirements.md) — user needs, functions, non-goals and acceptance criteria.
- [Architecture](Architecture.md) — proposed components, platform strategy and data flow.
- [Security and Privacy](Security_and_Privacy.md) — threats, privacy constraints and permissions.
- [Roadmap and Test Plan](Roadmap_and_Test_Plan.md) — implementation stages, testing and success evidence.
- [Device Survey](Device_Survey.md) — Windows/macOS discovery worksheet, deliberately without identifying details.
- [Architecture Decision Preparation](ADRs/README.md) — decisions to research and write in the owner's own words.
- [AI Collaboration and Authorship](AI_Collaboration_and_Authorship.md) — provenance and honest portfolio claims.
- [Portfolio Copy (Draft)](Portfolio_Summary.md) — future site description, not evidence of completion.

## Current progress

- **2026-10-26:** User needs, cross-platform scope, web safety boundary, and initial documentation were established from conversations. These documents are AI-generated drafts supplied for owner review.
- **Next:** Inventory the Windows and Mac hardware; interview the intended users; test whether a local vision model works reliably before committing to a software stack.

## Portfolio integrity

Planning is not implementation. A model-generated design is not a working feature. Published demonstrations and reliability claims will require dated tests and owner review. See [authorship disclosure](AI_Collaboration_and_Authorship.md).
