"""
CTF Challenge 05 — CI/CD Workflow Injection (Static Analysis)
Category : CI/CD Pipeline Security
Difficulty: Expert (500 pts)

STORY
-----
A GitHub Actions workflow was found in a leaked repo backup.
A malicious pull request was merged that injected a payload
into the PR title field — which the workflow echoed directly
into a shell `run:` block.

The attacker's payload caused the runner to base64-encode
the contents of a secret env variable and write it to the
build log. The encoded value was captured in the log snippet.

YOUR MISSION
------------
No server needed. This is a pure static analysis + decoding challenge.

1. Read the workflow file:   workflow.yml
2. Read the captured log:    build_log.txt
3. Understand WHY the injection worked (find the vulnerable line)
4. Decode the exfiltrated value from the log to get the flag

HOW TO RUN
----------
  python solve.py
  (fill in the TODOs first)
"""
