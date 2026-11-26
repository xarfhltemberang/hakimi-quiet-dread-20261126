#!/usr/bin/env python3
"""Write one code-review comment that approves a pull request with quiet dread.

The entry is a single line of 1-140 characters, written to /output/entry.txt
with no trailing newline. The laugh comes from the dread itself: cheerful
approval up front, then the flat fact that the code outlives its authors.
"""

import os

ENTRY = "LGTM. This will outlive us all, and it won't even remember our names."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
