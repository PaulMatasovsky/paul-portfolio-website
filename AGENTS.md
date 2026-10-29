# Guidance for AI Contributors

Before editing this repository, read [GitHub Writing Principles](Documentation/GitHub_Writing_Principles.md).

- Write project documentation in a natural, direct voice close to the owner's style. Use first person for the owner's perspective, but never invent actions, decisions, observations, or completed tests.
- Practice Shibumi: remove filler, repeated sections, and needless complexity without dropping requirements, security boundaries, technical details, or evidence.
- Keep AI involvement explicit and accurate. Describe **AI-led** and **human-led** contributions without obscuring who did the work. Writing in the owner's voice does not change authorship.
- Distinguish proposed design, drafted source, verified behavior, and deployed work. Do not mark something complete without evidence.
- Keep a standard status line near the top of every project README: `**Project status:** **<stage>** · **Activity:** <activity>`. Use only **Not Started**, **In Progress**, **Testing / Debugging**, **Blocked**, or **Complete** for stage; use **Active**, **Paused**, or **Maintenance** for activity when applicable. Add a short parenthetical qualifier only when it clarifies the actual work. Don't invent progress or change a status without evidence.
- When creating or updating a project, check that its README status matches the main repository README's Current Work table. Keep the **AI-led/human-led** authorship label separate from implementation status, so neither gets lost.
- Preserve project documentation, links, and test IDs. For ADRs, keep one file per accepted decision and a short index in that project's ADR folder. Clearly separate open questions from accepted records. Follow [the original ADR process](Documentation/ADRs/ADR-000.md): do not rewrite an accepted decision except to mark it superseded, and do not pass off AI-drafted prose as independently authored by the owner.
- Keep private family information and secrets out of commits.
- Don't modify the separate QA Toolkit repository unless explicitly asked.

These guidelines were drafted with AI at the owner's request. They are repository guidance, not a claim that any project has been independently written or tested.
