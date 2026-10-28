# Computer Helper — Python Starter

**Project classification: AI-led** · **Status: Prototype scaffold (not validated on target hardware)** · 2026-10-28

This is a small starting point for the proposed family computer helper. The project owner supplied the goals and safety boundaries; AI drafted this code for review and testing.

What this version **does**:
- Runs a basic terminal conversation against an Ollama model on **localhost**.
- Keeps a short in-memory conversation history.
- Looks up relevant sections of the local example Windows help notes using simple keyword matching.
- Provides an initial separation between conversation logic, knowledge lookup, and the terminal interface.

What this version **does not do**:
- Read personal folders, see the screen, inspect a browser, use a microphone, or control Windows/macOS.
- Execute model-requested commands or arbitrary tool calls.
- Connect to any cloud service or retain conversations between runs.
- Demonstrate that an AI model is installed, fast, accurate, or secure on the intended computers.

## Prerequisites

Python 3.10 or later and [Ollama](https://ollama.com/download) installed locally. Start Ollama, then download a compact baseline model:

```sh
ollama pull llama3.2:3b
```

The model can be changed later. This initial choice is for baseline testing, not a final recommendation.

## Windows setup (PowerShell)

Run these commands **inside this prototype folder**:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## macOS setup (Terminal)

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Type a question, or `exit` to stop. The optional `ASSISTANT_MODEL` environment variable changes the model; it must already be downloaded in Ollama.

Example, PowerShell:

```powershell
$env:ASSISTANT_MODEL = "llama3.2:3b"
.\.venv\Scripts\python.exe main.py
```

If Ollama is not running, the program reports the error rather than silently using an online AI.

## Offline unit tests

These check the Python conversation and retrieval helpers **without requiring Ollama**:

```powershell
py -m unittest discover -s tests -v
```

The tests are provided but have not been executed on either intended family computer. They do **not** prove the generated AI answers are correct.

## Design notes

- `main.py`: Terminal entry point and Ollama connection.
- `core/conversation.py`: Basic behavior instructions, limited conversation history, and prompt assembly.
- `core/knowledge.py`: Simple keyword retrieval of local Markdown notes. This is a learning baseline, **not** a finished RAG engine.
- `knowledge/`: Example public Windows help notes. Expand and verify against current Microsoft documentation before using them for family support.
- `tests/`: Standard-library unit tests for the non-AI components.

Never put passwords, family documents, screenshots, transcripts, tokens, or device identifiers in this repository. Future specialists need permission checks, tests, and explicit read-only bounds before connecting them to the AI.

See the [project requirements](../Product_Requirements.md), [architecture](../Architecture.md), and [security rules](../Security_and_Privacy.md).
