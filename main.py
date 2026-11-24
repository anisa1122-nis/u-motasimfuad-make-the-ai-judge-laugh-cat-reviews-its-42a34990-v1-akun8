#!/usr/bin/env python3
"""Cat Reviews Its Human — one-line entry.

Writes one funny single-line one-star review from a house cat about
its human, under 200 characters, to /output/entry.txt.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The review: the human bought a bed; the cat sleeps in the box.
# Deadpan one-star shape, feline voice, sting in the last words.
# Counted at 85 characters — inside the 1..200 window.
LINE = (
    "One star. He bought me a bed. I sleep in the box it came in. "
    "He still hasn't learned."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the review to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
