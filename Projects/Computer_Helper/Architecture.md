# Architecture — Working Plan

**Status:** Proposed, not built · 2026-10-26

I want one interface for both Windows and Mac, but I don't expect the code that interacts with each operating system to be the same. The assistant can share its conversation logic while using a different adapter for each computer.

```text
User (text / optional voice)
          |
     Help window
          |
   Request coordinator ---- Local AI model
          |
      Permission check ---- Screen information (when approved)
          |
     Allowed local actions
       /        \
    Windows     macOS
    adapter    adapter
```

The AI can suggest an action, but the application must check whether that action is allowed before doing anything. A password manager stays separate.

## Main parts

| Part | Job |
| --- | --- |
| Help window | Accept questions, show or speak one step, and provide clear Stop and screen-access controls. |
| Local AI | Understand the question and explain the screen or task. |
| Permission check | Accept only actions from an approved list. |
| Windows/Mac adapters | Open known folders or programs and get screen information with permission. |
| Website reader | Help explain the current page without controlling the browser. |
| Optional web search | Look up general help information when asked, without sending private screen content. |

For example, the permitted operations might be `open_known_folder` (Pictures, Documents, Downloads) and `open_approved_app` (a program from a list I set up). [Security and Privacy](Security_and_Privacy.md) holds the rules.

## What I still need to decide

**How to understand the screen:** A screenshot analyzed locally may be the simplest approach, but it could capture information the assistant does not need. Reading an application's accessible controls may be better in some situations. I'll compare both with test screens.

**Which model and interface to use:** Ollama and a small vision-capable model are possibilities, not decisions. I need to see how well they work on the actual computers before choosing them.

**Windows and Mac support:** I want the same user experience, but each operating system has its own ways of opening folders, inspecting screens, and granting permissions.

**Voice:** I'd like the option to talk to the helper, but it has to be understandable and responsive enough to be useful.

If any part fails or is uncertain, the helper should explain that rather than guess or quietly send information to an online service.

I'll choose the actual code structure once I've tried these options. The [roadmap](Roadmap_and_Test_Plan.md) describes the order I plan to work in.
