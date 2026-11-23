#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, no network, no randomness:
two runs produce byte-identical output.

The joke: a performance review that praises you and pays you nothing.
Setup sounds like good news; the punchline lands on the last three words.
"""

import os

JOKE = "My review said I 'exceed expectations' \u2014 corporate for 'great job, still no raise.'"


def main() -> None:
    # Enforce the bounty gate ourselves: one line, 1-199 chars, not blank.
    # Fail loudly instead of ever emitting an entry the judge refuses.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit(f"joke is {len(JOKE)} chars, gate needs 1-199")
    if "\n" in JOKE or not JOKE.strip():
        raise SystemExit("joke must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
