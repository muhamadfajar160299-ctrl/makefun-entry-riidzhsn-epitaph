"""Write the epitaph entry to the grader output directory.

Reads entry.txt next to this script, strips surrounding whitespace,
and writes the single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only; runs under python3 -S.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        with open(src, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print("cannot read entry.txt: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    line = text.strip()
    if not line:
        print("entry.txt is empty", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    try:
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError as exc:
        print("cannot write output: %s" % exc, file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
