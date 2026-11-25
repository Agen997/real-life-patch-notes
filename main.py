#!/usr/bin/env python3
"""Real-Life Patch Notes entry: writes one funny patch note to /output/entry.txt.

The note is a single-line changelog entry for a bug in human biology,
in the terse register of a real release note.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where the brain stored every song lyric from 2007 "
    "but forgot why you walked into this room."
)

# Gate: the entry must be 1-160 UTF-8 characters, one line, not only whitespace.
assert 1 <= len(LINE) <= 160, f"entry length {len(LINE)} outside 1-160"
assert LINE.strip(), "entry must not be only whitespace"
assert "\n" not in LINE, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
