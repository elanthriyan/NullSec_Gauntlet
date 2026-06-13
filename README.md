# CTF — Trace Security Risks Across Feature Implementation Flow
## Workshop Edition · Advanced · 5 Challenges · 1800 pts total

---

## Requirements

- Python 3.8+ (no external libraries needed for most challenges)
- Works on macOS, Linux, Windows (Command Prompt or PowerShell)

---

## Challenge Overview

| # | Title                        | Category       | Pts | Mechanic                              |
|---|------------------------------|----------------|-----|---------------------------------------|
| 01| JWT None Algorithm           | Auth           | 300 | Forge a JWT, hit a protected endpoint |
| 02| Race Condition (TOCTOU)      | Design Flaw    | 400 | Win a thread race to redeem code 2x   |
| 03| Mass Assignment Escalation   | Auth           | 400 | PATCH unexpected fields to become admin|
| 04| IDOR Enumeration             | Access Control | 400 | Loop report IDs to find the admin one |
| 05| CI/CD Workflow Injection     | CI/CD          | 300 | Read a log, find the vuln, decode flag |

---

## How Each Challenge Works

### Each challenge folder contains:
- `server.py`  — intentionally vulnerable local server (challenges 01–04)
- `exploit.py` / `solve.py` — skeleton with TODOs participants must complete
- Participants run the server in terminal 1, write their exploit in terminal 2

### Participants must:
- **Read** the scenario and understand the vulnerability class
- **Write real code** to fill in TODOs — the exploit skeleton won't work as-is
- **Run their exploit** against the local server to receive the flag in the response
- The flag only appears when the exploit **actually works**

---

## Running a Challenge (all OS)

```bash
# Terminal 1 — start the vulnerable server
cd challenge_01
python run_server.py        # Windows: py server.py

# Terminal 2 — write and run your exploit
cd challenge_01
# edit exploit.py — fill in all TODOs
python exploit.py
```

---

## Flags (Organizer Reference)

| # | Flag                                              |
|---|---------------------------------------------------|
| 01| FLAG{RACE_COND_OVERFLOW} (base64 in response)     |
| 02| Decoded from XOR in server at runtime             |
| 03| FLAG{M4ss_4ss1gnm3nt_0wned}                       |
| 04| FLAG{IDOR_<sha256 prefix>} (computed at runtime)  |
| 05| FLAG{GHtHub_Actions_Injection}  (base64 decoded)  |

---

## Organizer Notes

- All servers bind to `127.0.0.1` only — no network exposure
- Challenge 04 uses `random.seed(42)` so the admin report ID is deterministic
- Challenge 02 has a `/reset` endpoint so participants can retry the race
- Encourage participants to read the full docstring at the top of each file

