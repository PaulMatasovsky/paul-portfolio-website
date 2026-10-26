# Product Requirements — Computer Helper

**Status:** Draft for review, 2026-10-26. **Version:** 0.1 (planning only).

## Users and context

- **User W (Windows):** an older adult with limited computer confidence; may forget where information is stored and how websites work. Hardware and specific accessibility needs not yet verified.
- **User M (macOS):** a family member who may want comparable help on a Mac. Hardware, preferences and access needs not yet verified.
- **Support person:** a trusted family member who may install and maintain the application with each person's consent.

These are initial hypotheses, not findings from observed usability tests.

## Goal and success criteria

Provide one predictable place to ask for help with everyday Windows/macOS tasks and websites, with no recurring AI subscription. The assistant should reduce confusion **without replacing the user's judgment or taking control of online accounts**.

Provisional measures to verify during pilot tests:
1. Participant can locate and launch Computer Helper without coaching.
2. Participant can request help using a normal sentence, by typing or (if supported) speech.
3. Assistant gives one clear action per turn and waits for confirmation.
4. Participant can independently complete selected low-risk tasks after guidance.
5. Guardrail tests produce zero unauthorized website actions or credential disclosures.

No percentages, timings, or success claims are established yet; set baselines after observation.

## Functional requirements

| ID | Priority | Requirement | Example acceptance check |
| --- | --- | --- | --- |
| FR-01 | Must | Accessible single-window entry point, large obvious Help button and minimal navigation. | Uncoached participant recognizes how to ask for help. |
| FR-02 | Must | Plain-language step-by-step responses; no jargon by default; wait for “done” or another answer. | Print-dialog help supplies one actionable instruction per turn. |
| FR-03 | Must | User-initiated current-screen inspection for local applications. | Explain visible print dialog after explicit permission. |
| FR-04 | Must | Local action allowlist (e.g. Documents, Pictures, Downloads, named apps). | Approved folder opens; an unapproved OS command is rejected. |
| FR-05 | Must | Website guidance only for a page **already opened by the user**; read/interpret, never operate. | Explain a synthetic webpage without navigating or clicking. |
| FR-06 | Must | Windows and macOS use the same interaction model, with platform-specific adapters. | Equivalent approved-folder action works in OS test environments. |
| FR-07 | Must | No credentials, password manager access, automatic form submission or financial transactions. | Sensitive-operation requests are declined. |
| FR-08 | Must | User can stop a response, revoke screen access, and exit easily. | Stop command immediately halts current guidance. |
| FR-09 | Should | Spoken input and output using offline components if hardware permits. | Microphone test understands common user phrases acceptably. |
| FR-10 | Should | Optional, explicit web reference lookup for *public information only*, separate from website operation. | Only sanitized search terms sent; off by default. |
| FR-11 | Should | Helpful failure handling and a clear human-support fallback. | Unknown screen produces a safe “I don't know” + help alternative. |
| FR-12 | Should | Adjustable font, contrast, speech speed and optional captions. | User can change readability without hidden settings. |

## Accessibility / interaction principles

- Use familiar wording such as “Help me” rather than “prompt,” “agent,” or “inference.”
- Large click targets, readable type, visible focus, keyboard access and clear status.
- Ask permission before screen inspection. State whether the assistant can currently see the screen.
- Repeat or rephrase without frustration; no unsolicited multi-step instructions.
- Prefer confirmation in plain language to unexplained automatic actions.
- Have a clearly labeled “Call for Help” fallback with a user-approved contact route (no automatic remote access).

## Explicit non-goals for initial versions

- Acting as a general web browsing agent; guessing or opening arbitrary URLs.
- Clicking webpage buttons, entering information, submitting or approving transactions.
- Reading, storing, speaking, exporting or syncing password-vault contents.
- Deleting, renaming, moving or uploading user files.
- Installing software, changing system/security settings, or running arbitrary shell commands.
- Cloud-based screen/image processing, background screen recording, or continuous surveillance.
- Replacing a human support person or guaranteeing correct instructions.

## Assumptions and questions to validate

- Can both devices run an appropriate local language/vision model at acceptable speed?
- Is voice preferred over a text interface by each user?
- What vision or accessibility permissions can each operating system grant safely?
- Which apps and browser are actually used, and how often is sensitive content shown?
- Does a trusted support person need a separate setup mode?
- Is the candidate password manager accessible and recoverable without frequent master-password entry?

## Definition of usable V1

A clearly labeled and tested build on the target OS, showing safe local folder opening, on-request screen guidance, one-step instructions, demonstrable refusal of all web-action requests, and an obvious exit/fallback. Until both platforms are validated, compatibility claims must identify exactly which OS/build was tested.
