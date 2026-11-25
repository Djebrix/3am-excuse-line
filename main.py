#!/usr/bin/env python3
"""The 3 AM Excuse: one line from a hardware wallet refusing to sign at 3 AM.

Stdlib only, no network. Writes the line to $ENTRY_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: same bytes on every run.
"""

import os

LINE = (
    "It's 3 AM. My secure element is on its union-mandated nap "
    "\u2014 come back at sunrise with a decision your morning self would sign."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
