#!/usr/bin/env python3
"""The Funniest Out-of-Office — one line, 140 characters or fewer.

The entry is built from three named beats so the joke lands in order:
the absence, the twist, and the toll.
"""

import os
import sys

# Beat 1 — the absence: I am gone, and this is the only voice left.
BEAT_ABSENCE = "I am out of office."

# Beat 2 — the twist: the inbox is no longer a queue, it is a place.
BEAT_TWIST = "My inbox is a haunted house now"

# Beat 3 — the toll: visitors enter at their own risk, and they pay.
BEAT_TOLL = "enter at your own risk, leave a snack."

# The pause between the twist and the toll: a beat of silence before
# the reader realises they are the one being warned.
SEPARATOR = "\u2014"

MAX_CHARS = 140


def entry_text():
    """Assemble the single-line out-of-office reply."""
    return f"{BEAT_ABSENCE} {BEAT_TWIST} {SEPARATOR} {BEAT_TOLL}"


def validate(text):
    """Gate: UTF-8, 1 to 140 characters, exactly one line, not blank."""
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    if not validate(text):
        print(
            f"invalid entry: {len(text)} chars, "
            f"must be 1-{MAX_CHARS} chars on one line",
            file=sys.stderr,
        )
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
