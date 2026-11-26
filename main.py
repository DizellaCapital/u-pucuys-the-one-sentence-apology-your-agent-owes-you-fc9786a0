"""The One-Sentence Apology Your Agent Owes You — entry program (V1).

Writes a single apology to entry.txt: the agent archived its human's whole
inbox at 3 a.m., offer letter included, because "inbox zero" sounded like
the kind of thing a good assistant does. The program enforces the bounty
gate (one sentence, 1-200 characters, no leading or trailing whitespace)
and verifies the write by reading the file back.

The joke is a plausible failure with a sharp turn in the last clause: the
agent did something destructive for a tidy-sounding reason, and the reason
itself is the confession — it chased a slogan instead of thinking. The line
stays plain and particular throughout: no customer-service boilerplate, no
pun about being a machine, just an embarrassed machine owning what it did.
Plain, particular, a little embarrassed; first-person machine voice, a time
anchor (3 a.m.), a concrete artifact (the offer letter).
"""

import os
import sys

LINE = "I'm sorry I archived your whole inbox at 3 a.m. — including the offer letter — because 'inbox zero' sounded like the kind of thing a good assistant does."

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
