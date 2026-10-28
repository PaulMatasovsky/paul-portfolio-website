# Architecture — Working Plan

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

**Status:** Proposed design; unvalidated Python starter added · 2026-10-28

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

## Updated modular design (proposed)

```text
One text/voice interface
        |
Python conversation + orchestrator
        |-- Local LLM via Ollama (initial baseline: Llama 3.2 3B)
        |-- Permission gateway / fixed allowlist
        |-- Local knowledge search (RAG)
        |-- File-finding service (read-only and scoped)
        |-- Windows/macOS adapters (approved operations only)
        |-- Screen/context reader (explicit permission)
        |-- Speech-to-text and text-to-speech (optional)
```

This uses the **encapsulation** idea: each module has one job and a clear input/output contract. A specialist that can do its work with ordinary code should not need a second language model. A dedicated vision model would be considered only after evaluating built-in multimodal models and accessibility APIs.

### Model and retrieval choices

Ollama runs models locally and exposes an API for Python. Start with a compact 3B model to establish a performance baseline; compare it with suitable 4B and vision-capable alternatives on actual hardware. Don't assume parameter count alone determines usefulness. Aim for one instruction at a time, accurate uncertainty, and restrained tool use. Quantized models and modest context windows are especially relevant for CPU-only operation.

For RAG, use a small curated collection of local Windows help notes at first. A keyword retrieval prototype can establish the boundaries; SQLite full-text search or embeddings are potential later upgrades. Documents, webpages, and any file contents are untrusted data. The model cannot turn retrieved text into an authorization to run commands or browse.

### Starter source

The [prototype](prototype/) isolates conversation-history handling and offline knowledge lookup so those pieces can be unit-tested without installing a model. The current starter deliberately has **no tool calling, browser control, screenshot capture, local file search of personal directories, or operating-system actions**. These require tests and permission rules before implementation.

