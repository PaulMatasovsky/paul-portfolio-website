# Computer Helper — Windows and macOS

**Project status:** **Not Started** (implementation) · **Activity:** Active (planning)

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

**Next step:** Check both computers' specifications, find out which tasks are most frustrating for the intended users, and test local AI options.

## AI transparency

I set the goals and boundaries for this project. AI helped turn our discussions into these documents and revise the wording. I have not built or tested the application. [More on AI's involvement](AI_Collaboration_and_Authorship.md).
