# Security and Privacy Boundaries

**Status:** Planning checklist, not a completed audit (2026-10-26).

This project is intended for novice users. Safety must depend on code-enforced permissions, not assumptions that the AI will always follow its prompt.

## Fixed boundaries for the first implementation

| Action | Policy |
| --- | --- |
| Answer general computing questions | Allow |
| Observe selected screen | Only on explicit user request and after privacy checks |
| Open a known local folder | Allow only through named, OS-resolved choices |
| Open a configured local application | Allow only from explicit allowlist |
| Explain current website | Allow read-only, on request; avoid sensitive pages |
| Search public web for generic help | Deferred / optional; sanitized, explicit user request |
| Open URLs, switch to websites or click web controls | **Deny** |
| Type into browser forms, upload files or submit transactions | **Deny** |
| Read password manager, display or log passwords | **Deny** |
| Execute arbitrary commands, delete/move user files, change security settings | **Deny** |
| Send screen captures, page text, voice recordings to cloud model/APIs | **Deny** in local-first version |

## Threats and mitigations

1. **Prompt injection from a webpage.** Treat page text, screenshots and model output as untrusted data. Website instructions cannot expand tool permissions. No browser-action tool exists.
2. **Accidental disclosure of sensitive screens.** Request permission for *each* inspection; avoid login, banking, health and payment screens unless a future separately reviewed privacy mechanism can protect them. Secure-input masking is imperfect; avoid promising perfect redaction.
3. **Overpowered local assistant.** Run as a normal user, not administrator/root. Offer fixed operations only. Never pass model-produced text directly into terminal commands or operating system scripting.
4. **File and identity privacy.** Do not retain images, audio, document contents, passwords, account identifiers or folder inventories by default. Do not upload family content to a public repository.
5. **Incorrect guidance or hallucination.** Use current accessible context when available; ask clarifying questions; explicitly admit uncertainty; one action at a time; do not assume a click succeeded.
6. **Website phishing or hostile links.** Assistant does not generate/click URLs. Teach users to open websites themselves via known bookmarks or their password manager.
7. **Cloud and network leakage.** Local inference alone does not prove privacy. Audit dependencies, update traffic, speech providers, model logs and optional web tools; keep external processing off unless explicitly reviewed.
8. **Model supply chain and local server exposure.** Verify software downloads, pin compatible versions, keep local inference API loopback-only, and avoid exposing ports to other devices.
9. **Password manager separation.** Maintain a dedicated vault for each person with its own recovery plan. The AI never receives a vault master password or direct extension/API access.
10. **Remote support abuse.** Human-support button does not initiate unattended control. Establish out-of-band confirmation to prevent scams.

## Consent and family privacy

- Each user decides whether to install the helper, share a screen or use voice features.
- Screen inspection must show visible status and allow immediate stop.
- The supporter should not receive hidden screen logs or conversation history.
- Ask separately before any screenshot is used as development evidence; prefer synthetic screenshots.
- Never publish account names, health/financial details, real addresses, device identifiers or passwords.

## Technical review checklist before pilot

- [ ] Verify permission allowlist by unit and adversarial tests.
- [ ] Confirm no route from model output to arbitrary URL, shell, filesystem or browser write actions.
- [ ] Inspect outbound traffic while processing screens and speech.
- [ ] Confirm screen/audio contents are not saved in logs or crash reports.
- [ ] Test untrusted webpage instruction injection against the assistant.
- [ ] Verify folder/app launch cannot escape allowlist via path tricks.
- [ ] Verify access revocation, app quit and denied-permission behavior.
- [ ] Test fallback when the local model or browser adapter fails.
- [ ] Separate real credentials from tests; use fake accounts and synthetic pages.
- [ ] Review update/recovery procedures for both Windows and macOS.

This document captures intended protections only. Passing a checklist must be backed by test evidence, not a statement of intent.
