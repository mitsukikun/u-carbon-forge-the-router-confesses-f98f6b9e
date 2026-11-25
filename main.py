#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes a single line: the excuse a home Wi-Fi router gives for
dropping the connection at the exact moment a movie reaches its climax.
Python 3 standard library only, no network access.
"""

import os

LINE = "Sorry, I panicked at the climax \u2014 even routers get performance anxiety."


def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
