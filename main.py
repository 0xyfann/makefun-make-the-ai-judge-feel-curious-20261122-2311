#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The text is a small mystery: a lighthouse signalling in a pattern
it has never used in forty years, and a keeper who almost
recognises the word hidden in the pauses between the blinks.
Nothing is explained. The reader is left with the blinks and
the almost-word, and the question of who — or what — is sending it.
"""

from __future__ import annotations

import os
import sys

ENTRY_TEXT = (
    "The lighthouse blinked twice, then once, then twice again \u2014 "
    "a pattern it has never used in forty years. The keeper logged "
    "it, made tea, and waited. Tonight it did it again, and the "
    "pauses between the blinks spelled a word he almost recognised."
)

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> str:
    """Check the entry text against the competition rules.

    The text must be 1-280 Unicode code points, not only whitespace,
    free of control characters, and encodable as UTF-8. Returns the
    text unchanged when every check passes, otherwise raises.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be a string")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry text must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    bad = [ch for ch in text if ord(ch) < 0x20]
    if bad:
        raise ValueError(
            "entry text must not contain control characters, "
            f"found {bad[0]!r} (U+{ord(bad[0]):04X})"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def main() -> int:
    """Validate the entry text and write it exactly to entry.txt."""
    text = validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
