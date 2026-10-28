# Computer Helper — Windows and macOS

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

**Project status:** **In Progress** (starter source, not validated) · **Activity:** Active

## Why I'm doing this

I started thinking about this project while helping a family member who kept losing track of passwords. I put the passwords into one document, but that did not solve the problem. He still had trouble knowing where to find things and what to do on the computer.

I began looking at a more useful solution: one place to ask for help with the computer itself. I also want it to work on a Mac, since another family member could use similar help.

## What I want to build

A simple assistant that can explain what someone is looking at and guide them **one step at a time**. I want it to work by typing, with voice as an option if the computers can handle it.

There is an important limit to what I want the assistant doing:

- **On the computer:** It could open familiar folders, such as Pictures or Documents, or a few approved applications.
- **On websites:** It could explain the page someone is already viewing, but it would not click links, fill out forms, or navigate for them.
- **With passwords:** A separate password manager would handle them. The assistant would not see or retrieve passwords.

I also want to keep screen information on the computer and avoid adding a monthly AI subscription. Whether a local model can do the job well enough is something I still need to test.

## Documentation

| Document | What's in it |
| --- | --- |
| [Requirements](Product_Requirements.md) | What the helper needs to do |
| [Architecture](Architecture.md) | How I might put it together |
| [Security and Privacy](Security_and_Privacy.md) | What the helper is and isn't allowed to do |
| [Roadmap and Tests](Roadmap_and_Test_Plan.md) | The steps and tests I plan to use |
| [Device Survey](Device_Survey.md) | What I need to learn about both computers and their users |
| [ADR Preparation](ADRs/README.md) | Design decisions I still need to make |
| [AI Collaboration](AI_Collaboration_and_Authorship.md) | My contributions and AI's involvement |
| [Portfolio Draft](Portfolio_Summary.md) | Draft description for my portfolio site |
| [Python starter](prototype/) | Unvalidated CLI and offline-knowledge search example |

**Next step:** Run the starter source with Ollama, measure performance with existing hardware, and validate retrieval and safety before adding computer-control features.

## AI transparency

I set the goals and boundaries for this project. AI helped turn our discussions into these documents and revise the wording. I have added unvalidated starter Python code, but have not run or tested the application on either family computer. [More on AI's involvement](AI_Collaboration_and_Authorship.md).

## Current direction (October 2026)

I want to build one simple helper, not a collection of separate apps that family members have to learn. My working design is a local language model for conversation and task selection, with small specialists behind it. Most specialists should be ordinary Python services, not additional AI models.

- **First prototype:** Python terminal chat connected to Ollama and a small downloadable model. Llama 3.2 3B is the starting baseline; Qwen and other candidates will be compared rather than assumed best.
- **Knowledge:** Start with a small offline Windows 11 knowledge library, using basic text retrieval before introducing SQLite FTS or vector search. Reference text is data, not instructions.
- **Specialists:** File finding, approved local shortcuts, operating-system help, screen interpretation, and voice can be separate modules with clear responsibilities. The application, not the model, enforces permission rules.
- **Browser:** Explain only the page already open. No automatic site navigation, clicking, form filling, or submission.
- **Privacy:** Process locally by default. The password manager remains separate, and personal files/screenshots do not go into this repository.
- **Hardware:** The Windows test machine has an i5-8500, 16 GB RAM, and Intel UHD 630 integrated graphics. It is *believed* to be an OptiPlex 5070 SFF, pending confirmation. Additional RAM or a GPU is deferred until performance testing. The Mac mini's chip and RAM still need verification.

A starter Python scaffold is under [prototype/](prototype/). It includes terminal chat and a small example local-document search service; **it has not been tested on either family computer or validated with users**.

## Project status and evidence

- **Done:** Requirements discussion, architecture exploration, security boundaries, and starter code committed for review.
- **Not done:** Local model installation on a target PC, end-to-end runtime checks, live Windows/macOS integration, speech, screen reading, tool calls, packaging, and user testing.
- **Still provisional:** Final AI model, documentation search method, computer permissions, GUI toolkit, and hardware purchases.

This is an **AI-led** project: I supplied the problem, boundaries, and direction; AI has produced most of the current documentation and starter code. I am reviewing the work and will verify it before claiming functionality.

