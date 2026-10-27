# Computer Helper — Windows and macOS

**Project status:** **Not Started** (implementation) · **Activity:** Active (planning)

## The problem

Remembering passwords is only one challenge for people unfamiliar with computers. Finding files, using applications, and navigating websites can also require help.

## Proposed solution

A single, accessible assistant for Windows and macOS that explains tasks **one step at a time** through text or, if feasible, voice.

- **Local tasks:** May open a small set of approved folders and applications.
- **Websites:** Gives guidance about a page the user has already opened; does not navigate, click, or submit anything.
- **Privacy:** Requests permission to inspect the screen. Passwords remain in a separate manager.
- **Cost:** Target $0 in additional recurring AI subscriptions; local-model feasibility depends on both computers' hardware.

**Example:** “Open my pictures” could open the Pictures folder. “Where are my bank statements?” would receive guidance—not an automated banking action.

## Documentation

| Document | Purpose |
| --- | --- |
| [Requirements](Product_Requirements.md) | User needs and desired capabilities |
| [Architecture](Architecture.md) | Candidate design and platform integration |
| [Security and Privacy](Security_and_Privacy.md) | **Authoritative permissions and privacy rules** |
| [Roadmap and Tests](Roadmap_and_Test_Plan.md) | Milestones, test cases and evidence |
| [Device Survey](Device_Survey.md) | Hardware and user-interview template |
| [ADR Preparation](ADRs/README.md) | Open decisions, not accepted ADRs |
| [AI Collaboration](AI_Collaboration_and_Authorship.md) | Roles, authorship and claim boundaries |
| [Portfolio Draft](Portfolio_Summary.md) | Concise copy for a future site entry |

**Next:** Collect Windows and Mac specifications, speak with the intended users, and benchmark local models before choosing a stack.

## AI transparency

I defined the users, scope and safety boundaries. AI drafted these initial documents; no application has been implemented or tested. [Contribution details](AI_Collaboration_and_Authorship.md).
