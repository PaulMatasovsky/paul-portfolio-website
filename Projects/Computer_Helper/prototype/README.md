# Computer Helper — Python Starter

**AI-led project** · Starter code; not yet tested on the family computers · Updated October 28, 2026

This is my first step toward the family computer helper. I set the goals and boundaries; AI drafted the initial Python code for me to review and test.

For now, it does three things: lets me chat with a local Ollama model in the terminal, remembers a few recent messages, and looks through a small set of example Windows help notes using keyword matching.

**It is not a working computer assistant yet.** It can't search personal folders, see a screen, use the browser, listen or speak, or change anything in Windows or macOS. It doesn't have tool calling. It also doesn't save conversations between runs.

## Before running it

Install Python 3.10 or newer and [Ollama](https://ollama.com/download). Start Ollama and download the small baseline model:

```sh
ollama pull llama3.2:3b
```

I'm starting with Llama 3.2 3B to get a baseline, not because I've settled on it for the finished helper.

## Windows (PowerShell)

Open a terminal **in this prototype folder** and run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Mac (Terminal)

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Type a question, or type `exit` to quit. You can change the model later by setting `ASSISTANT_MODEL`, provided that model is already downloaded.

For example, in PowerShell:

```powershell
$env:ASSISTANT_MODEL = "llama3.2:3b"
.\.venv\Scripts\python.exe main.py
```

If Ollama isn't available, the script reports an error. It doesn't quietly switch to an online AI.

## Test the non-AI pieces

From the prototype folder:

```powershell
py -m unittest discover -s tests -v
```

These unit tests check conversation history and local knowledge lookup without needing Ollama. They are included in the repository, but I haven't run them on the intended computers. They don't tell us whether the model gives good answers.

## Where the code lives

| File | What it does |
| --- | --- |
| `main.py` | Connects terminal chat to Ollama. |
| `core/conversation.py` | Handles instructions and short conversation history. |
| `core/knowledge.py` | Searches example Markdown notes by keyword. It's not a finished RAG system. |
| `knowledge/` | Holds sample Windows 11 notes that still need checking against current guidance. |
| `tests/` | Contains basic offline unit tests. |

I'm keeping the first version small so I can understand and test it before adding more features. Future computer-control specialists will need permission checks and security tests first.

Don't commit passwords, private documents, screenshots, transcripts, tokens, or device identifiers to this repository.

See the [requirements](../Product_Requirements.md), [architecture](../Architecture.md), and [security rules](../Security_and_Privacy.md).
