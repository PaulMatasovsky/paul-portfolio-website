# Computer Helper — Windows and macOS

**AI-led project** · **In progress:** planning and untested Python starter · Updated October 28, 2026

## Why I'm building it

I started thinking about this after helping a family member who was having trouble keeping track of passwords. Organizing those passwords helped with one problem, but it didn't help him figure out where things were or what to do next on his computer.

I want to build one place where he can ask for help without having to learn a new collection of programs. I'd like to offer the same kind of help on a Mac for another family member.

The assistant should explain things in plain English, one step at a time. Typing comes first, with voice as an option if the computers can handle it well.

For my uncle, the first priorities are finding documents that didn't land in Downloads, helping him get oriented when Windows gets confusing, and working with the LibreOffice program he uses to type letters. I've put the actual situations into [everyday task examples](Uncle_Use_Cases_and_Conversation_Tests.md).

## The plan

I'll start with a small local AI model through Ollama and use Python to connect it to specialists that each do one job. That follows the encapsulation approach I wanted: the conversational AI coordinates things, while ordinary code handles tasks that don't need another AI model.

- **Windows and Mac help:** Search a small offline library of instructions (RAG). Start with simple text search; consider more advanced search only if needed.
- **Files and programs:** Eventually find recent files in approved folders and open a short list of familiar folders or apps.
- **Screen and websites:** With permission, explain what's on screen or on the page the user already opened. The helper won't browse, click links, fill forms, or submit anything.
- **Privacy:** Keep processing local by default and leave passwords with the existing password manager. The helper won't access the vault.
- **Shared design:** Reuse the conversation and specialist logic across Windows and macOS, with separate code where the operating systems differ.

The first model to test is Llama 3.2 3B. I'll compare it with others rather than assume that the biggest or newest model is the best choice.

## Where it stands

I've worked through the requirements and security limits and added a [Python starter](prototype/). It contains terminal chat and a simple offline knowledge lookup. **I haven't run it on either family computer or tested it with users.** The file-search, screen, browser, voice, and operating-system specialists are still plans.

My uncle's Windows PC has an i5-8500, 16 GB of RAM, and integrated Intel graphics. I believe it's an OptiPlex 5070 Small Form Factor, but I still need to confirm that. My mother's Mac mini is newer; I haven't checked its chip or memory yet. I'm holding off on buying RAM or a graphics card until we have performance results.

The next step is to run the prototype with Ollama, test its answers and memory use, and then add a tightly limited file-search specialist.

## Documents

| Document | What it's for |
| --- | --- |
| [Requirements](Product_Requirements.md) | What the helper needs to do |
| [Uncle's everyday tasks](Uncle_Use_Cases_and_Conversation_Tests.md) | Real problems and proposed conversation tests |
| [Architecture](Architecture.md) | How the parts fit together |
| [Security and privacy](Security_and_Privacy.md) | What it can and cannot do |
| [Roadmap and tests](Roadmap_and_Test_Plan.md) | Build order and evidence |
| [Device survey](Device_Survey.md) | What I know and still need to check |
| [Decision questions](ADRs/README.md) | Choices that aren't settled yet |
| [Python starter](prototype/) | Initial code and setup instructions |
| [Portfolio summary](Portfolio_Summary.md) | Short project description |
| [AI collaboration](AI_Collaboration_and_Authorship.md) | Who did what |

## AI transparency

I set the goals, security boundaries, and modular approach. AI helped research the options and drafted most of the documentation and starter code. I'm reviewing that work and will test it before calling anything functional. This is an **AI-led project**, and I want that distinction to stay clear even when the writing sounds more like me.

I'm using the repository's [writing principles](../../Documentation/GitHub_Writing_Principles.md) to keep the documentation simple without leaving important things out.
