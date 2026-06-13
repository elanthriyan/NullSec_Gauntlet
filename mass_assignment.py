"""
Challenge 03 — Mass Assignment
================================
Target : http://127.0.0.1:5003
Token  : Bearer tok_alice

Background
----------
The PATCH /profile endpoint updates your user profile. The bug is that
the server does this with NO field restrictions:

    user.update(request_body)   # entire request body merged in!

This means you can inject ANY field into your own user object —
including fields that should never be user-controlled, like "role".

Your goal: escalate your role from "user" to "admin", then access
/dashboard to get the flag.

Tasks
-----
  TODO 1 — Call GET /profile to see your current role
  TODO 2 — Call PATCH /profile with a body that changes your role
  TODO 3 — Call GET /dashboard to retrieve the flag

Endpoints
---------
  GET   /profile          → returns your current profile
  PATCH /profile  + body  → merges body into your profile (the bug!)
  GET   /dashboard        → admins only — returns the flag
"""

import json
import urllib.request
import urllib.error


BASE  = "http://127.0.0.1:5003"
TOKEN = "tok_alice"


def request(method, path, body=None):
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(
        BASE + path, data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type":  "application/json",
        },
        method=method
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def main():
    print("=" * 55)
    print("  Challenge 03 — Mass Assignment")
    print("=" * 55)

    # TODO 1 — Fetch and print your current profile
    #           What is your current role?
    print("\n[*] Step 1 — Current profile:")
    profile = None  # <-- call request("GET", "/profile")
    print(f"    {profile}")

    # Confirm dashboard is blocked for regular users
    print("\n[*] Step 2 — Try /dashboard as regular user:")
    r = None  # <-- call request("GET", "/dashboard")
    print(f"    {r}")

    # TODO 2 — Send a PATCH to /profile that sets role to "admin"
    #           Hint: body should be {"role": "admin"}
    print('\n[*] Step 3 — PATCH /profile with {"role": "admin"}:')
    r = None  # <-- call request("PATCH", "/profile", ???)
    print(f"    {r}")

    # TODO 3 — Now access /dashboard — you should be admin
    print("\n[*] Step 4 — Access /dashboard as admin:")
    r = None  # <-- call request("GET", "/dashboard")
    print(f"    {r}")

    if r and "flag" in r:
        print(f"\n[+] FLAG: {r['flag']}")
    else:
        print("\n[-] No flag yet — did you set the right role?")


if __name__ == "__main__":
    main()