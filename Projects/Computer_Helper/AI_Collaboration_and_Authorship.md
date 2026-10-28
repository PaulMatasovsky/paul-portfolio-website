# AI Collaboration and Authorship

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

**Status:** Working disclosure · 2026-10-28

I started looking into this project because I wanted a better way to help family members who have trouble using their computers.

I set the goal of having one simple place to ask for help. I also decided that the assistant should only open approved local folders and programs. When someone is on a website, it should explain what to do rather than take over the browser. I wanted to keep passwords separate and avoid adding monthly AI fees.

I used AI to help work through the design, consider possible tools, organize the repository, and draft the requirements, architecture, security notes, and tests. I also used it to revise the documentation so it reads more like the way I normally explain things.

**The documentation is still AI-drafted and needs my review.** Writing it in my preferred style does not make it independently authored.

AI has drafted starter source, but I haven't run or tested it on a target computer. At this point I can show requirements, plans, and an initial code scaffold—not a working product or results from users.

For the major design choices, I'll follow my [existing ADR process](../../Documentation/ADRs/ADR-000.md): research the alternatives and write the final accepted decisions myself. The [ADR notes](ADRs/README.md) are preparation for that work.

## Project classification update — AI-led

**Computer Helper is an AI-led project.** I identified the problem and set the user experience, operating limits, and goals. I proposed a modular, encapsulated approach with a conversation coordinator and small specialists, and chose to investigate RAG for Windows and macOS help. AI helped research alternatives, write and revise most of the planning documents, and draft the first Python scaffold.

I will review the design and code, test the work on real machines, and record problems and changes rather than treating AI-generated code as verified. **This classification describes how the project is being created; it does not mean a finished assistant is already running AI behind the scenes.** A future running application *is intended* to use a local AI model; that is separate from the authorship disclosure.

As of 2026-10-28, only planning materials and unvalidated starter source are in this repository. There are no verified target-device runs, user trials, or completed integrations. New decisions have been documented as *proposals*, not accepted ADRs.

