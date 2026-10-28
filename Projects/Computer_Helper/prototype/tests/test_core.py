"""Offline unit checks for the AI-led Computer Helper starter."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.conversation import add_turn, build_messages
from core.knowledge import retrieve_notes


class ConversationTests(unittest.TestCase):
    def test_system_instructions_are_first(self):
        messages = build_messages([], "Where are my downloads?")
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[-1]["role"], "user")

    def test_reference_is_marked_untrusted(self):
        messages = build_messages([], "How do I open Settings?", "Settings guidance")
        self.assertIn("untrusted content", messages[-1]["content"])
        self.assertIn("<reference>", messages[-1]["content"])

    def test_history_stays_bounded(self):
        history = []
        for number in range(10):
            history = add_turn(history, f"Q{number}", f"A{number}", max_turns=3)
        self.assertEqual(len(history), 6)
        self.assertEqual(history[0]["content"], "Q7")

    def test_history_limit_rejected(self):
        with self.assertRaises(ValueError):
            add_turn([], "a", "b", max_turns=0)


class KnowledgeTests(unittest.TestCase):
    def test_retrieves_matching_local_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "help.md").write_text(
                "# Notes\n## Downloads\nUse File Explorer to find downloaded pictures.\n"
                "## Settings\nUse the Settings application.",
                encoding="utf-8",
            )
            result = retrieve_notes("Where are my downloaded pictures?", directory)
            self.assertIn("File Explorer", result)
            self.assertIn("Source: help.md", result)

    def test_does_not_read_unrelated_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "not-there"
            self.assertEqual(retrieve_notes("Downloads", directory), "")

    def test_no_keywords_returns_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "doc.md").write_text("# Help\nTest", encoding="utf-8")
            self.assertEqual(retrieve_notes("and the", directory), "")


if __name__ == "__main__":
    unittest.main()
