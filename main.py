"""Fortune in a Pot - v2 entry writer.

Writes a single-line fortune for a houseplant, in the voice of a
fortune-cookie prediction, to /output/entry.txt (no trailing newline).
Repotting is coming -- the roots have already started packing.
"""

import os

ENTRY = "You will be repotted into something bigger soon. Your roots already know; they have been packing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
