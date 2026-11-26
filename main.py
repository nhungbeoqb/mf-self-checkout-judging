#!/usr/bin/env python3
"""Write the judgmental self-checkout one-liner to $OUTPUT_DIR/entry.txt.

The line is a single message, 105 characters, no trailing newline:
the till as a nightclub bouncer — twelve yoghurts, no spoon, no bag,
and the bagging area has a dress code the shopper's dinner is not on.
"""
import os
import sys

LINE = "Twelve yoghurts, no spoon, no bag. The bagging area has a dress code \u2014 and your dinner isn\u2019t on the list."


def main() -> int:
    # Gate self-check, mirroring the sealed scorer: 1-200 chars,
    # single line, UTF-8, not only whitespace.
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Post-write check: what landed on disk must be exactly LINE,
    # with no trailing newline added by the writer.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("written entry.txt does not match LINE exactly", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
