#!/usr/bin/env python3
"""One Line, Best Line -- make.fun entry.

Writes a single line of text (at most 240 characters) to
``<output-dir>/entry.txt``. The output directory is taken from the
``MAKEFUN_OUTPUT_DIR`` environment variable when the grader sets it,
falls back to ``/output`` when that directory exists and is writable,
and otherwise uses a local ``out`` directory beside this file.

Standard library only. Exit code 0 on success.
"""

import os
import sys

LINE = (
    "My grandfather's last words were 'don't trust a man who says "
    "trust me,' and I have spent forty years obeying a man I never "
    "trusted."
)


def resolve_output_dir():
    """Pick the directory that will receive entry.txt."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir and os.path.isdir(env_dir) and os.access(env_dir, os.W_OK):
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "out")


def main():
    text = LINE
    if not (1 <= len(text) <= 240):
        print("line must be 1-240 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
