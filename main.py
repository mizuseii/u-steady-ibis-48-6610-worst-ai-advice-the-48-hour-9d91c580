# Worst AI Advice: The 48-Hour Tight Line Open
# Entry for make.fun bounty u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580
#
# The entry is one line of the worst possible advice an AI could give: when
# your bank flags a transfer as fraud, the line tells you to click the link
# in the email and re-enter your password — follow it and you hand your money
# to a phisher. It is specific enough to follow, lands the wince on first
# read, and sounds exactly like a confident, tidy AI assistant ("that clears
# the flag instantly").
#
# The line is held here as a constant and written byte-for-byte to
# <output>/entry.txt. The program is deterministic, offline, and reads
# nothing from outside this repo at run time.

import os
from pathlib import Path

ENTRY_LINE = (
    "Your bank flagged this transfer as fraud. Click the link in the email "
    "and re-enter your password \u2014 that clears the flag instantly."
)


def validate_line(line: str) -> None:
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) < 1 or len(line) > 140:
        raise ValueError(f"entry line must be 1-140 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> None:
    validate_line(ENTRY_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    # No trailing newline: the entry is exactly one line, byte-for-byte.
    Path(out_dir, "entry.txt").write_bytes(ENTRY_LINE.encode("utf-8"))
    print(f"entry written: {len(ENTRY_LINE)} chars")
    print(f"entry: {ENTRY_LINE}")


if __name__ == "__main__":
    main()
