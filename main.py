#!/usr/bin/env python3
"""One-liner writer for the "no deadline met" joke.

This tiny script does exactly one job: it takes a single joke line about a
to-do list that went on strike and writes it, followed by a newline, into a
file called entry.txt inside the output directory chosen by the environment.
"""

import os

JOKE = "I missed the deadline because my to-do list unionized and went on strike the moment I opened it."


def main():
    """Write the joke line to entry.txt in the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
