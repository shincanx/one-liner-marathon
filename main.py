"""One-Liner Marathon — entry program.

Writes one one-line comedy joke, at most 280 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. Deterministic: no randomness, no network,
no input files.
"""

import os

JOKE = (
    "I asked my smart speaker for a joke. "
    "It said, 'You — for buying a smart speaker.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
