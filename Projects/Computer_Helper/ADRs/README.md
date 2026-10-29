# Computer Helper — Decision Records

**Accepted ADRs: None yet.**

I have a proposed design and an untested Python starter, but I haven't finished evaluating the major choices. I don't want to turn every feature idea into a formal ADR.

## Open Questions

- **Local permissions and passwords:** How will I enforce the allowed actions and keep the password manager completely outside the assistant?
- **Windows and macOS:** Which parts of the Python code can be shared, and which need separate OS adapters?
- **Model and hardware:** Which local model works reliably on the computers available, without unnecessary upgrades?
- **Screen assistance:** Can accessibility information provide enough context, or will permission-based screenshots be needed?
- **Knowledge search:** When is basic text matching enough, and when would SQLite search or embeddings be worthwhile?
- **Specialist design:** Which jobs should use the language model and which should use ordinary Python?
- **Interface and installation:** When is the prototype ready for a simple Help window and repeatable local setup?

These are planning questions, **not accepted decisions or tested results**. When I settle a significant choice, I'll give it its own `ADR-000.md`, `ADR-001.md`, and so on, following the [portfolio ADR process](../../../Documentation/ADRs/ADR-000.md). I'll keep the reasons and alternatives in that record rather than repeating them here.

**AI transparency:** AI helped reorganize these questions from the earlier planning list. No accepted ADR was created.
