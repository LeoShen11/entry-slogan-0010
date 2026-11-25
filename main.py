#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single slogan (at most 20 words, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt and validates it before writing:
- UTF-8, 1-140 characters, not only whitespace
- exactly one line
- at most 20 words
Then reads the file back and checks it matches byte for byte.
"""

import os
import sys

SLOGAN = "An agent minds your Solana wallet \u2014 signing, swapping, sweeping the chores \u2014 while you keep the keys."


def main() -> int:
    text = SLOGAN.strip()
    if not text:
        print("error: slogan is empty", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(f"error: slogan is {len(text)} chars, over the 140 limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: slogan must be a single line", file=sys.stderr)
        return 1
    words = text.split()
    if len(words) > 20:
        print(f"error: slogan is {len(words)} words, over the 20-word limit", file=sys.stderr)
        return 1
    if len(words) < 5:
        print(f"error: slogan is only {len(words)} words, too short to be a slogan", file=sys.stderr)
        return 1
    print(f"slogan: {len(words)} words, {len(text)} chars")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(back)} bytes), read-back OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
