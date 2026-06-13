"""
Challenge 04 — Insecure Direct Object Reference (IDOR)
========================================================
Target : http://127.0.0.1:5004
Token  : Bearer tok_bob

Background
----------
The GET /report?id=N endpoint checks that you are logged in, but it
does NOT check that you own the report you're requesting.

This means any logged-in user can read ANY report by simply changing
the id= parameter — including a confidential admin report.

Your goal: find the admin's report ID and read it to get the flag.

Tasks
-----
  TODO 1 — Call GET /reports to see which report IDs you legitimately own
  TODO 2 — Read one of your own reports using GET /report?id=N
            to understand the response format
  TODO 3 — Write a loop to enumerate report IDs and find the admin report
            Hint: look for a response where owner == "admin" or "flag" is present
  TODO 4 — Print the flag

Endpoints
---------
  GET /reports          → lists your own report IDs
  GET /report?id=N      → returns report N (no ownership check — the bug!)

Hints
-----
  - Report IDs are integers between 1 and 100
  - The admin report has owner: "admin" and a "flag" field
  - You don't need to guess randomly — just iterate all IDs
"""

import json
import urllib.request
import urllib.error


BASE  = "http://127.0.0.1:5004"
TOKEN = "tok_bob"


def get(path):
    req = urllib.request.Request(
        BASE + path,
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def main():
    print("=" * 55)
    print("  Challenge 04 — IDOR")
    print("=" * 55)

    # TODO 1 — List your legitimate reports
    print("\n[*] Step 1 — Your reports:")
    r = None  # <-- call get("/reports")
    print(f"    {r}")

    # TODO 2 — Read one of your own reports to understand the format
    print("\n[*] Step 2 — Read report #5 (one you own):")
    r = None  # <-- call get("/report?id=5")
    print(f"    {r}")

    # TODO 3 — Enumerate all IDs from 1 to 100 to find the admin report
    print("\n[*] Step 3 — Enumerating all report IDs...")
    for i in range(1, 101):
        # <-- fetch report with id=i
        # <-- check if "flag" is in the response
        # <-- if yes, print it and break
        pass

    # TODO 4 — If you found it above, the flag is already printed.
    #           If not, print a failure message.
    print("\n[-] Enumeration complete.")


if __name__ == "__main__":
    main()