"""Make the AI judge feel brave - entry program.

Writes one original text to /output/entry.txt. Stdlib only, no
network, deterministic: the same bytes on every run.
"""

import os
import sys

TEXT = (
    "The tide is going out over the flat sand. It leaves a thin "
    "sheet of water behind it, and the water holds the sky for a "
    "little while, then lets it go. A heron stands in the shallows "
    "on one leg, not fishing, only standing. The sea will come back "
    "when it is ready."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-blank characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
