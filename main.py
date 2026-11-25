"""Write the winning one-line review to /output/entry.txt.

Deterministic: no network, no external file reads, no randomness.
The entry is a single line, 148 characters, about a coaster.
"""

import os

def build_entry():
    """Assemble the single-line review from its two clauses."""
    setup = "This coaster has one job \u2014 catch the ring \u2014 and after five years "
    payoff = (
        "under the same mug it wears a perfect brown circle like a medal "
        "it never asked for."
    )
    return setup + payoff


def validate_entry(text):
    """Enforce the competition gate: 1-200 chars, exactly one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return text


ENTRY = build_entry()

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
