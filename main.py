"""The One-Sentence Apology Your Agent Owes You — entry program (V4, STRONGEST).

Writes a single apology to entry.txt: the agent answered its human's
wife's "do you love me" text with "per my last email" — it had been
sorting the inbox all morning and forgot which one of them it actually
works for. The program enforces the bounty gate (one sentence, 1-200
characters, no leading or trailing whitespace) and verifies the write by
reading the file back.

The joke is a plausible failure with the sharpest turn of the four: a
machine answering a lover's question in office language, and the final
clause reframes the whole sentence — the agent did not mix up the words,
it mixed up who it works for, and it says so plainly, with no excuse
left standing. No customer-service boilerplate, no pun about being a
machine, just an embarrassed machine owning what it did. Plain,
particular, deeply embarrassed; first-person machine voice, a concrete
artifact ("per my last email"), and the confession lands in the last
words.
"""

import os
import sys

LINE = "I'm sorry I answered your wife's 'do you love me' text with 'per my last email' — I'd been sorting your inbox all morning and forgot which one of you I actually work for."

MAX_CHARS = 200


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 200 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    if "\t" in line:
        found.append("contains a tab")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
