# Computer Helper — ADR preparation

**No accepted ADRs have been written for this project.**

The parent portfolio's [ADR-000](../../../Documentation/ADRs/ADR-000.md) requires the owner to author final decision-record prose personally, after considering real alternatives. These are research/interview prompts only, drafted by AI.

## Decision 000 — Security boundary and agency

- Context: Assistance should reduce computer confusion without granting authority over websites or sensitive accounts.
- Already specified by owner: limited approved local navigation; websites receive guidance only, no clicks or URL opening.
- Questions: What is the smallest required tool allowlist? How can negative permissions be tested? Should even app opening require confirmation?
- Alternatives worth verifying: guidance-only everywhere; limited local control; full autonomous agent (currently rejected as too risky).
- Final ADR: owner writes when ready.

## Decision 001 — Cross-platform implementation

- Context: initial user on Windows; another likely on macOS.
- Questions: Can a shared UI/orchestrator use separate adapters? Which macOS permissions are required? What will be tested before claiming compatibility?
- Explore simple cross-platform GUI approaches; do not select a toolkit solely from AI suggestion.

## Decision 002 — Local inference and optional internet lookup

- Context: no recurring AI subscription; screen privacy is important.
- Questions: What hardware is available? Does local text/vision perform well enough? Is sanitized public web search ever required?
- Research alternative models and costs with actual benchmarks before deciding.

## Decision 003 — Read-only website understanding

- Context: website guidance needs current context but must have no browser-action capability.
- Compare consented selected screenshots, browser accessibility metadata, and minimally permissioned read-only extension interfaces.
- Test hostile webpage text, sensitive-content exposure, and known failure modes.

## Decision 004 — Password-manager separation

- Context: password storage and authentication must remain outside model context and logs.
- Verify feasibility of separate user vaults/recovery workflows; keep actual credentials outside GitHub and the assistant.

For each accepted ADR, use the established title/date/status/context/decision/alternatives/reasoning format and document only alternatives genuinely evaluated.
