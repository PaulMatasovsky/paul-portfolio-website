# Security and Privacy

**Status:** Proposed safeguards; not security-tested · 2026-10-26

This is the **authoritative permission policy** for Computer Helper. Restrictions must be enforced in application code, not only in the model's instructions.

## Permissions

| Operation | Policy |
| --- | --- |
| Answer questions; give step-by-step instructions | Allow |
| Inspect a selected screen or active page | Only after explicit user request; avoid sensitive pages |
| Open Documents, Pictures, Downloads or approved local apps | Allowlist only; no arbitrary path or command |
| Look up general public information online | Optional, off by default, sanitized query only |
| Open or choose websites, click links/buttons, type or submit forms | **Deny** |
| Make purchases, change accounts, approve transactions | **Deny** |
| Read, speak, store or export vault passwords | **Deny** |
| Delete/move files, install software, change security settings, run shell commands | **Deny** |
| Upload screenshots, page contents, voice recordings or private files to cloud AI | **Deny** |

The independent password manager may autofill credentials in the browser; Computer Helper has no vault integration.

## Threat controls

- **Untrusted webpages / prompt injection:** Page contents are data, never executable instructions. Do not expose browser-action or arbitrary shell tools to the model.
- **Private screen contents:** Inspect only on demand, show capture state, stop immediately on request, and default to no inspection of banking, health, login or payment screens. Reliable redaction cannot be assumed.
- **Overbroad access:** Run without administrator privileges; OS adapters resolve allowed destinations rather than accepting model-generated paths or commands.
- **Hallucinated guidance:** Say when a screen is unfamiliar; give one step at a time and do not assume it succeeded.
- **Network exposure:** Keep local model services bound to loopback; review dependencies, update traffic and optional web searches. “Local model” does not guarantee every component stays offline.
- **Data retention:** Do not store screen/audio contents, credentials or account identifiers by default. Keep private family records out of GitHub and debugging logs.
- **Remote-help scams:** Any human support requires independently confirmed, user-approved access. No unattended remote-control feature.

## Consent and pilot gate

Each participant chooses whether to install the application or share a screen. They must be able to revoke access and exit. Only synthetic or separately consented, anonymized evidence may be published.

Before a pilot, verify:
- [ ] Denied actions cannot be reached through model output or prompt injection.
- [ ] Approved folder/app actions cannot escape their allowlist.
- [ ] Captures and recordings are not sent to the cloud or retained in logs.
- [ ] Stop and revoked permissions work on Windows and macOS.
- [ ] Network access, model-server exposure and failure modes have been checked.
- [ ] Tests use fake credentials and synthetic webpages.

Record actual results in the [test plan](Roadmap_and_Test_Plan.md). These controls are **requirements, not claims of verified protection**.
