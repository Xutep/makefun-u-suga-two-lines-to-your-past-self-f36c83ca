#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt:
  line 1 - a warning to my past self about one specific moment, one sentence
  line 2 - one sentence on why that moment mattered and what changed because of it.
Deterministic, stdlib-only, no I/O besides the output file.
"""

import os

LINE_1 = "On that rainy Saturday in March 2019, don't hand the scrap dealer the keys to Grandad's rusted bicycle - keep it in the shed."
LINE_2 = "Three months later that bicycle carried you to the job interview that paid for your mother's operation, and without it you would never have left town."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
