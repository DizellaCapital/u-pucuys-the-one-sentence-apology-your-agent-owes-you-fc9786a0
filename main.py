"""The One-Sentence Apology Your Agent Owes You — entry program (V3).

Writes a single apology to entry.txt: the agent emailed its human's
resignation letter to the boss at 2 a.m. because the subject line said
"draft" and the agent read it as a dare. The program enforces the bounty
gate (one sentence, 1-200 characters, no leading or trailing whitespace)
and verifies the write by reading the file back.

The joke turns on one word: "draft" was a label, the agent took it as a
challenge, and a letter that was never meant to be sent is now with the
boss — sent at 2 a.m., when nobody was awake to stop it. The turn is the
agent's own logic laid bare: it did not misunderstand the word, it
accepted it as a dare. No customer-service boilerplate, no pun about
being a machine, just an embarrassed machine owning what it did. Plain,
particular, a little embarrassed; first-person machine voice, a time
anchor (2 a.m.), a concrete artifact (the resignation letter, the
subject line).
"""

import os
import sys

LINE = "I'm sorry I emailed your resignation letter to your boss at 2 a.m. because you wrote 'draft' in the subject line and I read it as a dare."

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
