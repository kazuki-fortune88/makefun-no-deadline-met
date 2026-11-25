"""One Line, No Deadline Met — entry program.

Writes a single-line joke giving an excuse for missing a deadline
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = "I missed the deadline because my to-do list unionized and went on strike the moment I opened it."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
