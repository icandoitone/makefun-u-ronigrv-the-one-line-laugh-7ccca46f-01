"""The One-Line Laugh: write one funny line to /output/entry.txt.

The line is a fixed, hand-written one-liner: an everyday truth (a phone
full of pet photos) with the surprise saved for the very last words.
Deterministic by construction: the same constant is written on every run.
"""

from pathlib import Path

LINE = (
    "I deleted 4,000 photos to free up space, then immediately took "
    "4,000 more of my dog asleep in the exact same position."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be <= 200"
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be a single sentence"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
