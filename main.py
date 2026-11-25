#!/usr/bin/env python3
"""One Emoji, One Dream Vacation (make.fun).

Writes the entry -- one emoji for my dream vacation --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "🏝️"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
