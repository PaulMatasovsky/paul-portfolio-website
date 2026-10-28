# Computer Helper — Security and Privacy

**AI-led project** · Planned rules, not yet tested · Updated October 28, 2026

I want a helper, not a program that takes over someone's computer or online accounts. The important protections need to be enforced by our Python code, not just by telling the AI to behave.

## What's allowed

| Request | Rule |
| --- | --- |
| Answer a question or explain a task | Allowed |
| Open Pictures, Documents, Downloads, or a small list of approved apps | Allowed only through fixed local shortcuts |
| Search recent files | Read-only and limited to folders the user approves |
| Look at a screen or the page already open | Only when requested and permitted; avoid sensitive pages |
| Search the public internet | Optional, off by default; only a cleaned-up general question may be sent |
| Open websites, click browser controls, fill forms, or submit anything | **Blocked** |
| Make purchases, approve transfers, or change online accounts | **Blocked** |
| Access a password vault or read, store, or repeat passwords | **Blocked** |
| Delete or move files, install software, change security settings, or run arbitrary commands | **Blocked** |
| Send private screenshots, recordings, or webpage contents to a cloud AI | **Blocked** |

The existing password manager stays separate. The helper won't connect to it.

## How I'll enforce those limits

- **Permissions live in the application.** The AI may request a named function, but Python must check it against a fixed list. No arbitrary paths, shell commands, or AI-written instructions may be executed.
- **Websites are information, not instructions.** A webpage or retrieved document might tell the AI to ignore its rules. That text must never override permissions.
- **Screen access is temporary.** Ask each time, show when it is on, and stop when permission is withdrawn. Don't capture banking, health, login, or payment screens by default. I can't assume sensitive details can always be hidden.
- **Private data stays private.** Don't save screenshots, voice recordings, transcripts, account details, or personal files by default. Never put passwords, device IDs, or family data in a public repository.
- **Local means local.** Keep the model API bound to localhost, check network traffic and third-party dependencies, and don't quietly fall back to cloud services.
- **Failure should be safe.** If a tool fails or a request isn't allowed, explain that rather than doing something else. Run with normal user permissions.
- **Human help isn't remote control.** Any future remote-help option must require the person's permission and a separate confirmation. No unattended access.

## Before anyone relies on it

- [ ] Approved local actions work, and unapproved actions are blocked.
- [ ] A malicious instruction inside a webpage or reference document cannot change those limits.
- [ ] Screen and microphone permissions can be denied or withdrawn immediately.
- [ ] Sensitive data doesn't leak into logs, online requests, or the repository.
- [ ] The model isn't exposed to other computers on the network.
- [ ] The application fails safely when a model, document, or specialist is unavailable.
- [ ] Tests use sample pages and fake accounts, not family members' private information.

The [test plan](Roadmap_and_Test_Plan.md) will hold the results. These are **design requirements, not verified security claims**. The current Python starter has no computer-control tools, so the permission gateway hasn't been built or tested yet.
