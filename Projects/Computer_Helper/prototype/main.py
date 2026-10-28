"""Early AI-led Computer Helper terminal prototype.

Only local model chat and curated public-document retrieval are implemented.
No screen access, browser control, or personal-file tools are available.
"""

import os
from pathlib import Path

from core.conversation import add_turn, build_messages
from core.knowledge import retrieve_notes


BASE_DIR = Path(__file__).resolve().parent
MODEL = os.environ.get("ASSISTANT_MODEL", "llama3.2:3b")
OLLAMA_HOST = "http://127.0.0.1:11434"
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def main() -> None:
    try:
        from ollama import Client
    except ImportError:
        print("Install the Python dependency first: python -m pip install -r requirements.txt")
        return

    client = Client(host=OLLAMA_HOST)
    history: list[dict] = []
    print(f"Computer Helper prototype — {MODEL}")
    print("Type a question, or 'exit' to quit. No computer-control features are enabled.")

    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not question:
            continue

        # Retrieve only curated, checked-in public help notes.
        reference = retrieve_notes(question, KNOWLEDGE_DIR)
        messages = build_messages(history, question, reference)

        try:
            reply = client.chat(
                model=MODEL,
                messages=messages,
                options={"num_ctx": 4096},
            )
            answer = (reply.message.content or "").strip() or "I don't have an answer yet."
        except Exception as error:
            print(f"Local Ollama request failed: {error}")
            print("Make sure Ollama is running and the model is downloaded.")
            continue

        print(f"\nHelper: {answer}")
        history = add_turn(history, question, answer)


if __name__ == "__main__":
    main()
