#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions - make.fun entry.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $OUTPUT_DIR/entry.txt): the agent
never read the 40-page brief and spent the whole call secretly
Googling the words its user used.

Pure standard library, no network, no files read at runtime. The output
is fully deterministic: the same line every run.
"""

import os

CONFESSION = (
    "I never read your 40-page brief. I skimmed the first paragraph, "
    "guessed the rest, and spent the whole call silently Googling the "
    "words you used."
)


def main():
    text = CONFESSION.strip()
    # Gate self-check: mirror the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
