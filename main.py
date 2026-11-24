"""Fortune in a Pot — entry writer.

Writes the houseplant fortune to /output/entry.txt exactly as specified,
byte for byte, with no trailing newline.
"""

import os
from pathlib import Path

ENTRY = "You will outgrow this pot by spring, and your keeper will pretend she planned it all along."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
