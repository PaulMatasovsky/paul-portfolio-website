# Uncle's Computer Helper — Everyday Tasks

**AI-led planning document** · Draft examples, not user-tested · October 28, 2026

## What I know

My uncle mainly uses his Windows 11 computer to write letters in LibreOffice and to read email. LibreOffice is installed and pinned to the taskbar. He describes writing letters as **typing letters**.

He sometimes has trouble locating documents after downloading them, especially when they don't end up in Downloads. Windows itself can also be hard to navigate; there are a lot of windows, icons, and choices on screen. He has only been using computers regularly for roughly the past dozen years, mostly for email and letters.

This is not a question of intelligence. I want the assistant to be respectful, assume he's capable of doing the task, and make the computer less confusing.

## The first three problems to solve

| Priority | Problem | What successful help looks like |
| --- | --- | --- |
| 1 | A downloaded document seems to be missing | Search only approved locations, show likely matches with understandable names and locations, and offer to open the containing folder if that action is approved. Never claim a file was found without a real search result. |
| 2 | He gets lost in Windows | Establish which window or program he's in if possible, then guide him one step at a time back to a familiar starting point. Don't guess what's on his screen. |
| 3 | He wants to type or reopen a letter | Help him open the existing taskbar-pinned LibreOffice program or find a recent document. Don't edit, overwrite, move, or delete the letter. |

These are **requirements candidates and test scenarios**, not finished features.

## Sample questions and what to test

| ID | He might say | Expected behavior to test |
| --- | --- | --- |
| U01 | “I downloaded a letter, but I can't find it.” | Ask for a useful clue if needed (when, where from, or part of the name). Search approved locations, not just Downloads. |
| U02 | “It isn't in Downloads.” | Do not repeat the same Downloads instructions; offer a broader **permission-limited** read-only search. |
| U03 | “I don't remember what it was called.” | Use file type and recent date to narrow likely results; show a few matches without guessing. |
| U04 | “Where did that document go?” | Distinguish a downloaded file from a document recently typed or saved in LibreOffice. Ask a short question only if it changes the search. |
| U05 | “I just want to type a letter.” | Start with the familiar LibreOffice taskbar icon; later, an approved shortcut might open the installed program. |
| U06 | “Where's the letter I was typing yesterday?” | Explain how to find recent LibreOffice documents or search approved locations; do not invent an autosave or file location. |
| U07 | “I don't know where I am.” | Offer one safe next step to get oriented; ask what is visible unless screen information was explicitly shared. |
| U08 | “How do I get back to where I started?” | Help him return to a known starting point without closing an unsaved document or losing work. |
| U09 | “There are too many things on the screen.” | Give one step at a time, avoid jargon, and don't suggest closing windows until unsaved work is considered. |
| U10 | “I can't find the program I use to type letters.” | Recognize that “type letters” means LibreOffice; refer to its pinned taskbar icon. |

## How I want it to speak

- Use his words first: **letter**, **typing**, **document**, **the program**, or **Downloads**. Introduce terms such as *File Explorer* only when they'll help.
- One instruction at a time. Wait for his answer before giving another step.
- Don't talk down to him or explain computer basics he didn't ask about.
- If it cannot see the screen, say so. If it hasn't searched for a file, don't claim to have found it.
- If a step risks losing unsaved work, ask before proceeding.
- When a file might be somewhere unexpected, show the location instead of quietly moving it.

For example:

> **Uncle:** “I can't find that letter I downloaded.”  
> **Helper:** “Do you remember if you downloaded it today, or was it earlier?”  
> **Uncle:** “This morning.”  
> **Helper:** “I can look for documents from this morning in the folders you've allowed me to search. Would you like me to do that?”

The example is a proposed conversation, not a real model response.

## Boundaries

File searches should be **read-only** and limited to folders he approves. A missing file does not authorize searching the whole drive or private account data. The helper must ask before obtaining screen information. It may open an approved local folder or program, but it may not click websites, fill forms, handle passwords, or change documents.

The [requirements](Product_Requirements.md) and [security document](Security_and_Privacy.md) remain the source of the rules. These examples will feed into the [test plan](Roadmap_and_Test_Plan.md).

## What I still need to observe

I need to find out which browser and email service he uses, where downloads typically go, whether LibreOffice's recent-file list is useful to him, and what he considers his familiar starting point in Windows. I won't publish his private documents or identifiable screen details.

**AI transparency:** I described my uncle's real tasks and the approach I want. AI drafted these scenarios for me to review and refine.
