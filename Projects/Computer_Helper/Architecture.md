# Computer Helper — Architecture

**AI-led project** · Proposed design, not yet implemented · Updated October 28, 2026

I want one simple interface for both computers, but I don't expect every piece of code to be the same. Windows and macOS have different ways of accessing files, apps, and screen information.

My starting point is to have one AI handle conversation and decide which specialist to ask for help. Most of those specialists will be regular Python code, not separate AI models. Each should have one job and a clearly defined interface.

```text
One Help window (text / optional voice)
                    |
          Python coordinator
                    |
        Local AI model (Ollama)
                    |
       Approved specialist requests
                    |
      Application permission checks
             /      |       \
     Knowledge   File/OS    Screen/
       search    services   browser help
                 /    \
             Windows  macOS
```

The model can *suggest* an operation. Our application decides whether it is allowed. That permission check is not something I want to leave to the model's judgment.

## Responsibilities

| Part | Job |
| --- | --- |
| Help window | Let the person ask a question, receive one step at a time, and stop or withdraw screen access. |
| Main AI | Understand everyday questions, decide which specialist might help, and explain the results. |
| Knowledge search (RAG) | Find relevant offline Windows or Mac help notes and pass them to the AI as reference material. |
| File/OS services | Search specifically approved folders and open only approved local folders or programs. |
| Screen/browser reader | With permission, use accessibility information first and screenshots only when needed. It explains the current page, but does not control the browser. |
| Permission checks | Validate requests against fixed allowed actions; reject arbitrary commands, paths, and unapproved access. |
| Voice | Optional local speech recognition and spoken responses, if performance is acceptable. |

A specialist that can do its job with ordinary code shouldn't need a second language model. I can add a vision-specific model later if testing shows it would be useful and the computer can handle it.

## Technology choices to test

I'm using Python and Ollama for the first prototype. Llama 3.2 3B is the initial baseline, not a final model decision. I'll compare response quality, speed, and memory use with other compact models before committing.

For RAG, I'll begin with a few reviewed Markdown help files and basic text matching. If that's not enough, I can try SQLite full-text search or embeddings. Retrieved notes, webpages, and personal files must always be treated as **data, not instructions**.

The [Python starter](prototype/) only has terminal conversation code and a basic document lookup. It has no tool calling, computer control, screen access, personal-file search, or voice yet. Those features need permission rules and tests first.

The [security document](Security_and_Privacy.md) defines the boundaries; the [roadmap](Roadmap_and_Test_Plan.md) shows how I'll test the design.
