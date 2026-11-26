"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt. Python standard library only; deterministic.
"""

import os

ENTRY = (
    "The Roomba Stones \u2014 hit single 'Start Me Up, Then Vacuum' "
    "topped the charts, then ate them."
)


def validate(text: str) -> str:
    """The house gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
