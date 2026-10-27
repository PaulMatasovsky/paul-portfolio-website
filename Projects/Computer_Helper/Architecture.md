# Candidate Architecture

**Status:** Proposed, not implemented · 2026-10-26

## Design

One shared conversation interface; OS-specific Windows and macOS adapters. A code-enforced policy gate decides which local actions are possible. Model responses never execute directly.

```text
User (text / optional voice)
          |
     UI + consent
          |
   Request coordinator ---- Local model
          |
      Policy gate --------- On-demand screen context
          |
   Approved local actions
       /        \
    Windows     macOS
    adapter    adapter
```

A separate password manager has **no connection** to the model or action layer.

## Component responsibilities

| Component | Role |
| --- | --- |
| UI | Large Help and Stop controls; step-by-step dialogue; visible screen-consent state |
| Local inference | Explain a request or selected screen; ask for clarification |
| Policy gate | Validate requested actions against a fixed allowlist |
| OS adapters | Open known folders/apps and obtain permitted screen context through OS-specific interfaces |
| Browser context | Read-only interpretation of the current user-selected page |
| Optional public lookup | Search generic public help topics only after an explicit request |

**Candidate local actions:** `open_known_folder` (Documents, Pictures, Downloads) and `open_approved_app` (preconfigured app IDs). The detailed allow/deny policy lives in [Security and Privacy](Security_and_Privacy.md).

## Open technical choices

- **Screen context:** User-selected screenshot processed locally versus read-only accessibility metadata. Compare accuracy, permissions and sensitive-content exposure using synthetic pages.
- **Windows vs. macOS:** Shared intent names, separate implementations for known folders, application launching, screen permission, and accessibility APIs.
- **Model and interface:** Ollama with a small vision-capable model and a simple desktop UI are candidates, not selected technologies. Test speed and quality on the actual machines.
- **Voice:** Offline speech recognition and output only if the devices and users support it.
- **Failure behavior:** Explain uncertainty, avoid performing actions when checks fail, and never silently switch to cloud processing.

Source folders and framework choices will be defined when implementation starts; see the [Roadmap](Roadmap_and_Test_Plan.md).
