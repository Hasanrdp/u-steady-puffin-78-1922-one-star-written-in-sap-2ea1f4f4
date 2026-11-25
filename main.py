#!/usr/bin/env python3
"""One Star, Written in Sap — entry program.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The review is one fixed line, chosen by pre-judging five fresh candidates
against the kit's published judge brief (houseplant voice, grievance at
the centre, surprising turn, genuine one-star review, no stock phrases).
It is deterministic: the same line, byte for byte, on every run.
"""
import hashlib
import os
import sys

LINE = "One star. He named me after his ex, waters me when he remembers her, and wonders why I keep dropping leaves like evidence."

# Pinned fingerprint of the exact bytes this program must write.
# The program refuses to report success unless the file it just wrote
# reads back byte-identical to this fingerprint.
EXPECTED_SHA256 = "309edc6d9ba11f80bec54193be14ce1d9958da4d3f52c6022dbafc9ee856a29a"
EXPECTED_BYTES = 122

OUTPUT_PATH = "/output/entry.txt"


def verify(path, data):
    """Read the written file back and check it against the pinned values."""
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit(f"read-back mismatch: file differs from the line in memory")
    if len(back) != EXPECTED_BYTES:
        raise SystemExit(f"byte count {len(back)} != expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(back).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"sha256 {digest} != expected {EXPECTED_SHA256}")
    text = back.decode("utf-8")
    if not 1 <= len(text) <= 279 or text.strip() == "" or "\n" in text:
        raise SystemExit("gate failed: entry must be 1-279 chars, one line, not blank")
    return digest


def main():
    data = LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    digest = verify(OUTPUT_PATH, data)
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}")
    print(f"sha256: {digest}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
