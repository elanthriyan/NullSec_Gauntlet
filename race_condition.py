"""
Challenge 02 — Race Condition (TOCTOU)
=======================================
Target : http://127.0.0.1:5002/redeem

Background
----------
TOCTOU = Time Of Check, Time Of Use.

The /redeem endpoint has this flow:
  Step A — Read:    used = promo["used"]        ← checks here
  Step B — Sleep:   time.sleep(0.15)            ← 150 ms gap !!
  Step C — Check:   if used: return 409
  Step D — Count:   promo["redeem_count"] += 1
  Step E — Write:   promo["used"] = True        ← marks here

If TWO requests arrive at the same time, both read used=False at
Step A before either reaches Step E. Both pass the check → both
succeed → the code is redeemed more than once → flag is revealed.

Your goal: send concurrent requests so that redeem_count > 1.

Tasks
-----
  TODO 1 — Write the redeem() function that posts to /redeem
  TODO 2 — Use threading to fire multiple requests simultaneously
  TODO 3 — Use threading.Barrier so all threads start at the same instant
  TODO 4 — Find the flag in the responses

Hints
-----
  - Use threading.Thread and threading.Barrier
  - The more threads you fire at once the higher your chance of winning
  - If it doesn't work first time, just run the script again
    (the /reset endpoint resets the code for you)

Endpoints
---------
  POST /reset   {"code": "SAVE20"}              → resets the promo
  POST /status  {"code": "SAVE20"}              → check current state
  POST /redeem  {"code": "SAVE20", "user_id": "you"} → redeem attempt
"""

import json
import threading
import urllib.request
import urllib.error


BASE = "http://127.0.0.1:5002"


def post(path, body):
    data = json.dumps(body).encode()
    req  = urllib.request.Request(
        BASE + path, data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def main():
    CODE        = "SAVE20"
    NUM_THREADS = 5   # try increasing this if you don't win first time

    print("=" * 55)
    print("  Challenge 02 — Race Condition / TOCTOU")
    print("=" * 55)

    # Reset and verify
    print("\n[*] Resetting promo code...")
    print(f"    {post('/reset', {'code': CODE})}")
    print(f"    Status: {post('/status', {'code': CODE})}")

    results = []
    lock    = threading.Lock()

    # TODO 3 — Create a Barrier so all threads release at the same instant
    # Hint: barrier = threading.Barrier(NUM_THREADS)
    barrier = None  # <-- replace with threading.Barrier(...)

    # TODO 1 — Complete this function
    def redeem(uid):
        # TODO 1a — Wait at the barrier so all threads start together
        # Hint: barrier.wait()
        pass

        # TODO 1b — POST to /redeem with the promo code and user_id
        resp = None  # <-- call post() here

        # TODO 1c — Save the response thread-safely
        with lock:
            results.append(resp)

    # TODO 2 — Create NUM_THREADS threads, each calling redeem(f"racer_{i}")
    #           start them all, then join them all
    print(f"\n[*] Launching {NUM_THREADS} concurrent requests...")
    threads = []
    # <-- create and start threads here
    # <-- join threads here

    print("\n[*] Responses:")
    for i, r in enumerate(results, 1):
        print(f"    [{i}] {r}")

    # TODO 4 — Find and print the flag from any response that contains it
    print()
    found = False
    for r in results:
        if r and "flag" in r:
            print(f"[+] FLAG: {r['flag']}")
            found = True
            break
    if not found:
        print("[-] Race not won — try again!")


if __name__ == "__main__":
    main()