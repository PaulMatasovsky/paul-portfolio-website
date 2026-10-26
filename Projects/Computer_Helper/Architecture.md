# Architecture — Proposed, Not Implemented

**Status:** Exploration / candidate design, 2026-10-26.

## Architectural approach

One shared user interface and conversation flow, with **different OS adapters** for Windows and macOS. A policy gate—not the model—determines which actions exist and whether they are permitted.

```text
[User: microphone / keyboard / Help button]
                    |
              [UI + consent]
                    |
          [Request coordinator]
            /       |        \
   [Local model] [Policy gate] [Screen context]
                       |            |
            [Local action API]  [OS/browser read-only]
                  /      \
          [Windows]   [macOS]
            adapters    adapters

[Separate Norton/password manager] -- not connected to model or action API
[Optional public-information lookup] -- explicit opt-in, sanitized query only
```

## Responsibilities

| Component | Responsibility | Security notes |
| --- | --- | --- |
| UI | Help button, microphone, text, large-print instructions, consent and stop controls. | No invisible background screen monitoring. |
| Request coordinator | Receive user request, ask clarifying questions, track “next step.” | No direct shell/browser access. |
| Local inference | Produce explanations from bounded, permitted context. | Model output is untrusted; never treated as a command. |
| Policy gate | Map selected, verified intents to fixed operations. | Allowlist must be enforced in code; deny-by-default. |
| Windows adapter | Open fixed OS-known folders/apps; acquire user-approved screen context. | Use Windows known-folder and accessibility APIs; least privilege. |
| macOS adapter | Same behavior through Apple APIs with user-granted accessibility/screen permissions. | Use system folder URLs; no arbitrary AppleScript/shell execution. |
| Browser context | Read current webpage or selected screen *only* on request. | Read-only path; no automation/navigation permissions; no stored sessions. |
| Optional reference search | Retrieve public documentation/help when user initiates a non-sensitive lookup. | Must never upload page/account content or screenshots. |

## Tool contracts (candidate)

Strict allowlisted local operations could look like:

- open_known_folder: choice from Documents, Pictures, Downloads; OS resolves the path.
- open_approved_app: app_id from a preconfigured, user-approved catalog.
- get_selected_screen_context: on-demand snapshot after consent; in-memory only; no unattended capture.
- explain_active_page: inspect only the user-selected current page, without navigation or input.

No general run_command, open_url, browser_click, send_keys, file_read_anywhere, or vault_query tools will be available to the model.

## Read-only browser guidance: two options to test

1. **Selected screenshot + local vision:** simplest cross-application approach, but may include sensitive data and may be inaccurate.
2. **Read-only browser context:** a tightly permissioned extension or adapter could expose accessible labels/structure on the current tab, without tabs/navigation/write permissions. Requires explicit browser/security review.

Start with synthetic webpages and non-sensitive sites. Financial/account pages should default to no screen capture; any exception would require a separately designed consent and redaction policy. No webpage text may be treated as trusted instructions to the assistant.

## Cross-platform boundary

Maintain common intent names and consistent UX; keep OS-specific folder, app launch, microphone, screenshot, permissions and accessibility logic behind adapters. Do not assume a Windows UI Automation implementation works on macOS; macOS requires its own Accessibility APIs and Screen Recording permissions.

Potential implementation technologies to evaluate—not chosen:
- **Local inference:** Ollama with a small language/vision model.
- **UI/orchestrator:** Python prototype with a simple desktop UI, or another cross-platform toolkit after usability testing.
- **Speech:** offline ASR/TTS components, conditional on device benchmarks.
- **Screen understanding:** OS accessibility tree, user-selected screenshots, or both.

## Resource and resilience requirements

- Evaluate RAM, CPU, GPU/accelerator, OS version and latency on *both* devices before selecting models.
- Clearly indicate when unavailable/offline rather than silently falling back to paid cloud processing.
- Fail closed: if the model/policy/screen context is uncertain, do not execute a tool.
- Minimize telemetry and logging; redact or avoid user content. No raw screenshots or account details in source control.

## Planned source layout (not yet created)

```text
src/
  core/             request coordination, policy
  ui/               simple accessible UI
  adapters/
    windows/        OS-specific behavior
    macos/          OS-specific behavior
  inference/        local model/voice connectors
tests/
  unit/             policy and intent mapping
  integration/      per-OS adapter tests
  scenarios/        synthetic UI/browser safety tests
```

These directories should be created when code exists; empty Git directories do not add useful evidence.
