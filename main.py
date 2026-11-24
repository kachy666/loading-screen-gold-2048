#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters
(u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270).

Writes exactly one loading-screen tip to /output/entry.txt.
"""

import os

LINE = "Tip: your agent's tests all pass because they test nothing. The green checkmark is the only thing here with a clean conscience."


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise SystemExit("tip must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("tip must be a single line (no newlines)")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"tip must be 1-200 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"{line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
