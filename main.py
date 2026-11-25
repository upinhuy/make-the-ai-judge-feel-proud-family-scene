"""Make the AI Judge Feel Proud: A Family Scene.

Writes one warm, funny, heartfelt family scene (one line, under 280
characters) to ``<OUTPUT_DIR>/entry.txt`` for the make.fun bounty
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

Python 3 standard library only.
"""

import os
import sys

# The entry: one line, a small domestic moment — Dad burns the toast
# every Sunday, Mum quietly takes the blackest slice, and the kids
# pretend not to notice (they all notice).
ENTRY = (
    "Dad still burns the toast every Sunday and calls it 'extra crispy'; "
    "Mum scrapes it, butters it, and eats the blackest slice herself so "
    "none of us has to. We pretend not to notice. We all notice."
)

MAX_CHARS = 280
MAX_LINES = 2


def validate_entry(text):
    """Check the entry against the gate: 1-280 chars, 1-2 lines, not blank.

    Counts Unicode code points (len of the str). Raises ValueError with a
    clear message when the entry breaks the contract.
    """
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    chars = len(text)
    if chars < 1 or chars > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, must be 1-%d" % (chars, MAX_CHARS)
        )
    lines = text.splitlines()
    if len(lines) < 1 or len(lines) > MAX_LINES:
        raise ValueError(
            "entry has %d lines, must be 1-%d" % (len(lines), MAX_LINES)
        )
    return chars, len(lines)


def entry_path():
    """Resolve the output path from OUTPUT_DIR (default /output)."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Validate the entry, then write it as UTF-8 text to path."""
    chars, lines = validate_entry(text)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return chars, lines


def main():
    """Write the scene to <OUTPUT_DIR>/entry.txt and report the counts."""
    path = entry_path()
    chars, lines = write_entry(ENTRY, path)
    print("Wrote %d characters (%d line%s) to %s" % (chars, lines, "" if lines == 1 else "s", path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
