"""Local Markdown knowledge retrieval; no network or private-file crawling.

This first pass uses basic keyword overlap. It is not semantic vector search.
"""

from pathlib import Path
import re

STOP_WORDS = {
    "a", "an", "and", "are", "can", "do", "for", "how", "i", "in",
    "is", "it", "my", "of", "on", "or", "the", "to", "what", "where",
    "with", "you",
}


def retrieve_notes(question: str, directory: Path, limit: int = 2) -> str:
    """Return limited matching sections from a curated directory of Markdown notes."""
    if limit < 1:
        return ""
    terms = set(re.findall(r"[a-z0-9]+", question.lower())) - STOP_WORDS
    if not terms or not directory.is_dir():
        return ""

    matches: list[tuple[int, str, str]] = []
    for path in sorted(directory.rglob("*.md")):
        if not path.is_file():
            continue
        # Only read our packaged public notes; do not follow links outside the directory.
        if path.is_symlink():
            continue
        content = path.read_text(encoding="utf-8")
        sections = re.split(r"(?=^#{1,3}\s)", content, flags=re.MULTILINE)
        for section in sections:
            section = section.strip()
            if not section:
                continue
            score = sum(1 for term in terms if re.search(r"\b" + re.escape(term) + r"\b", section.lower()))
            if score:
                matches.append((score, path.name, section[:1100]))

    matches.sort(key=lambda item: (-item[0], item[1]))
    return "\n\n".join(
        f"Source: {filename}\n{text}" for _, filename, text in matches[:limit]
    )
