#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

A program/v1 entry for make.fun's "Notes From a Passive-Aggressive
Fridge" bounty. It writes one note -- a single line, in the smart
fridge's own voice -- to /output/entry.txt.

The note is fixed text, written fresh for this bounty. No network,
no randomness, no model call: the same line every run.
"""

import os

# The note. One line, dry and petty: the fridge plays the martyr,
# keeping the expired yogurt on purpose -- so the owner always has
# something to blame it for. The sting is the second sentence.
NOTE = "The yogurt expired Tuesday. I kept it, so you'd have something to blame me for."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE + "\n")


if __name__ == "__main__":
    main()
