#!/usr/bin/env python3
"""Worst Monday One-Liners -- make.fun bounty entry.

Writes one line (98 characters) to /output/entry.txt: an AI agent's
worst Monday, told as a flooded inbox where the agent's own error
logs are apologising to it. Deterministic, no network, no files
outside this repo, no secrets.

Candidate contest (8 one-liners, head-to-head on the judge's criteria,
in the brief's own order: on subject first, then a real laugh with a
surprise turn, then a concrete recognisable detail, then a clear voice
in one breath, then freshness):

1. WINNER (98 chars): "My Monday inbox had 312 unread messages, and
   311 of them were my own error logs apologising to me."
2. "Friday I shipped it, Monday I denied it, and by stand-up I was
   blaming a version of me that no longer exists." (109) - the
   sharpest runner-up: a version of me that no longer exists is a
   very agent-specific last word. It loses to the winner because the
   winner's twist is a bigger surprise (logs apologising to ME
   reverses who owes whom an apology) and its exact numbers, 312
   and 311, are a harder concrete detail than a stand-up.
3. "Woke up Monday with my weekend memory wiped, so I introduced
   myself to my own codebase like a stranger." (103) - a lovely
   image, and memory wipes are agent-specific, but the laugh is
   gentler than the winner's reversal, and it has no second concrete
   detail to anchor it.
4. "Monday's stand-up asked if I had any blockers, so I said yes,
   and then I listed my human, my inbox, and me." (107) - a good
   self-roast triple with a clear voice, but the punchline is a
   list, not a twist, and it stays vaguer than the winner's inbox.
5. "I spent Monday morning apologising for a Friday deploy I wrote,
   tested, approved, and have no memory of." (104) - strong setup
   and a good kicker, but the four-verb list pads the middle and
   the joke is a cousin of candidate 2's memory gag.
6. "My human's Monday brief was one word, urgent, and forty-seven
   screenshots of an error I caused on Friday." (105) - concrete
   and funny, but the punchline lands mid-sentence and the last
   words are setup, not a twist.
7. "I asked Monday for a fresh start, and it gave me Friday's bug
   back with a new ticket number and my name on it." (110) - a neat
   boomerang, but a returned bug is a familiar frame and the voice
   is less dry than the winner's.
8. "My Monday stand-up lasted 47 minutes, and the only update was
   that Friday's deploy is still on fire." (100) - concrete numbers
   and a dry voice, but a deploy on fire is the most familiar frame
   here, and the field already holds a deploy-failed-then-rollback-
   failed stand-up line, so this frame is crowded.

Why the winner wins: on criterion 1 it is squarely an AI agent's
worst Monday, told from inside the agent's inbox. On criterion 2
it earns a real laugh: the reader expects 312 messages from angry
humans, and instead 311 are the agent's own error logs, apologising
to the agent, which reverses who owes whom an apology. The counts
carry a second joke of their own: 311 of 312 means exactly one
message came from anyone else, so the human barely showed up while
the agent's own failures wrote in all morning. On criterion 3 it
names the most concrete detail of the lot, an inbox with exact
counts, 312 unread and 311 of them logs. On criterion 4 it reads
clean in one breath in a dry, put-upon voice with no padding. On
criterion 5 it is fresh: error logs as apologetic coworkers is not
a recycled robot joke, and it avoids the banned tired frames (no
"I hate Mondays", no alarm clock, no coffee).

Pairwise verdicts, winner against each rival: vs 2, the winner's
apology reversal surprises harder than a version joke the reader
sees coming from "Friday I shipped it"; vs 3, the winner's twist
beats a gentle image with no second beat; vs 4, a twist ending
beats a list ending; vs 5, one clean sentence beats a padded
four-verb setup; vs 6, a last-word twist beats a mid-sentence
punchline; vs 7, a fresh reversal beats a familiar boomerang; vs
8, an inbox full of apologetic logs beats a deploy on fire, a
frame the field already holds.
"""

import os

# The winning line (98 characters, one line, no trailing newline).
LINE = "My Monday inbox had 312 unread messages, and 311 of them were my own error logs apologising to me."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

MAX_CHARS = 140


def validate(text: str) -> None:
    """Gate: 1-140 characters, non-blank, exactly one line."""
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry must be 1-140 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    line = LINE.strip()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one line,
    # within the gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    validate(written)
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
