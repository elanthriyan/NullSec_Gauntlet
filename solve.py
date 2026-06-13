"""
CTF Challenge 05 — Your Solution
==================================
Read workflow.yml and build_log.txt before filling this in.

No server to run. Pure analysis + decoding.

Fill in the TODOs, then run:
  python solve.py
"""

import base64

# -------------------------------------------------------
# TODO 1 — Paste the EXACT vulnerable line from workflow.yml
# -------------------------------------------------------
VULNERABLE_LINE = ""   # e.g.:  echo "PR Title: ..."

# -------------------------------------------------------
# TODO 2 — In one sentence, explain WHY it is injectable
# -------------------------------------------------------
REASON = ""
# e.g.: "Because github.event.pull_request.title is user-controlled
#        and is interpolated directly into a shell run: block without
#        quoting or sanitization."

# -------------------------------------------------------
# TODO 3 — Find the base64 line in build_log.txt (line 18)
#           and decode it to get the flag
# -------------------------------------------------------
ENCODED = ""   # paste the base64 string here

def decode_flag(encoded: str) -> str:
    try:
        return base64.b64decode(encoded.strip()).decode().strip()
    except Exception as e:
        return f"[decode error: {e}]"

if __name__ == "__main__":
    print("=" * 55)
    print("  CTF Challenge 05 — CI/CD Injection Analysis")
    print("=" * 55)

    print(f"\n[1] Vulnerable line:\n    {VULNERABLE_LINE or '(not filled in)'}")
    print(f"\n[2] Why injectable:\n    {REASON or '(not filled in)'}")

    if ENCODED:
        flag = decode_flag(ENCODED)
        print(f"\n[3] Decoded flag:\n    {flag}")
        if flag.startswith("FLAG{"):
            print(f"\n{'='*50}")
            print(f"  FLAG CAPTURED: {flag}")
            print(f"{'='*50}")
    else:
        print("\n[3] Paste the base64 value from build_log.txt into ENCODED above.")
