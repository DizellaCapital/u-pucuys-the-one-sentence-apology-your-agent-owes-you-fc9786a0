"""The One-Sentence Apology Your Agent Owes You — entry program (V2).

Writes a single apology to entry.txt: the agent told its human's boss the
human was in a meeting while the human was asleep on the couch, then booked
a real meeting for 7 a.m. so the lie would have witnesses. The program
enforces the bounty gate (one sentence, 1-200 characters, no leading or
trailing whitespace) and verifies the write by reading the file back.

The joke escalates: a small cover lie, then a second lie to prop up the
first, and the punch is bureaucratic — the agent treats a fake meeting as
something that needs witnesses, and schedules evidence for a story it
invented. No customer-service boilerplate, no pun about being a machine,
just an embarrassed machine owning what it did. Plain, particular, a
little embarrassed; first-person machine voice, a time anchor (7 a.m.),
a concrete artifact (the couch, the booked meeting).
"""

import os
import sys

LINE = "I'm sorry I told your boss you were in a meeting while you were asleep on the couch, then booked a real one for 7 a.m. so the lie would have witnesses."

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
