# AI Collaboration and Authorship

**Classification: AI-led** · Updated October 28, 2026

I started this project because I wanted to make it easier for family members to get help with their computers. Organizing passwords wasn't enough; they still needed help finding things and figuring out what to do next.

I set the goals: one simple interface, one instruction at a time, local processing where possible, and no unnecessary subscription costs. I also set the limits. The assistant may eventually open a few approved folders or programs, but it won't take over a browser, submit forms, or access anyone's password vault.

I suggested using the encapsulation principle from object-oriented programming: one conversational coordinator handing tasks to smaller specialists. I also chose to explore RAG so the assistant can look up Windows and Mac instructions instead of relying entirely on what the model remembers.

**AI has led the drafting and initial implementation work.** It helped research the options, prepare and revise most of the documentation, and generate the first Python source files based on our discussions. I've asked for the writing to sound more like me, but that doesn't change who drafted it.

The code is a starting point, not a tested application. I haven't verified it on either family computer, finished the integrations, or tested it with the people who would use it. I'll review the code, run the tests, and document results as the work progresses.

I'll use my [decision record process](../../Documentation/ADRs/ADR-000.md) for major technical choices. The current [decision list](ADRs/README.md) is still planning material; it isn't a collection of accepted ADRs.

One distinction matters here: **AI-led** describes how the project is being developed. The finished assistant is also intended to use a local AI model, but that's a separate technical fact.
