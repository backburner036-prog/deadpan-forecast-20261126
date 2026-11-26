#!/usr/bin/env python3
"""Deadpan weather forecast for a city that does not exist.

Writes a single forecast line (at most 160 characters) to /output/entry.txt.
Deterministic, no network, no external input.
"""

import os

ENTRY = (
    "Tomorrow in Port Sullen: 22 degrees, light winds, and a 100 percent "
    "chance of rain \u2014 the clouds have filed the paperwork and there "
    "is no appeal."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 160


def main() -> None:
    text = " ".join(ENTRY.split())
    assert 1 <= len(text) <= MAX_LENGTH, (
        f"entry must be 1-{MAX_LENGTH} characters, got {len(text)}"
    )
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "round-trip check failed"
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
