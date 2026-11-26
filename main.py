#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport the Olympics turned down.

The program writes exactly one one-liner to /output/entry.txt:
a named athlete, a concrete count, and a second twist in a single frame.
"""

import os

LINE = (
    "Finland's Aino Korhonen won gold in the 100-metre Competitive Nap "
    "\u2014 asleep in 41 seconds, before the starting gun \u2014 and the IOC "
    "rejected it after all three judges dozed off mid-final."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must fit in 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
