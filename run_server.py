"""
run_server.py  — Participant tool
===================================
Decrypts server_all.enc and starts all 4 CTF challenge servers.

USAGE:
    python run_server.py <password>

Servers started:
    Challenge 01 — JWT None Algorithm  → http://127.0.0.1:5001
    Challenge 02 — Race Condition      → http://127.0.0.1:5002
    Challenge 03 — Mass Assignment     → http://127.0.0.1:5003
    Challenge 04 — IDOR                → http://127.0.0.1:5004

Press Ctrl+C to stop all servers.
"""

import sys, os, json, hashlib, base64, struct, types

ENC_FILE = "server_all.enc"

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)

def xor_decrypt(data: bytes, key: bytes) -> bytes:
    ks = b"".join(
        hashlib.sha256(key + struct.pack(">I", i)).digest()
        for i in range((len(data) // 32) + 2)
    )
    return bytes(a ^ b for a, b in zip(data, ks))

def decrypt(password: str) -> str:
    if not os.path.exists(ENC_FILE):
        print(f"[!] '{ENC_FILE}' not found. Place it in the same folder.")
        sys.exit(1)

    with open(ENC_FILE) as f:
        payload = json.load(f)

    salt       = base64.b64decode(payload["salt"])
    mac_stored = base64.b64decode(payload["mac"])
    ciphertext = base64.b64decode(payload["ciphertext"])

    key = derive_key(password, salt)

    mac_computed = hashlib.sha256(key + ciphertext).digest()
    if mac_computed != mac_stored:
        print("[!] Wrong password. Ask your organizer for the correct password.")
        sys.exit(1)

    return xor_decrypt(ciphertext, key).decode("utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_server.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    print("[*] Decrypting server bundle...")
    source = decrypt(password)
    print("[+] Decryption successful. Starting servers...\n")

    # Execute the decrypted server code directly in memory
    mod = types.ModuleType("ctf_servers")
    mod.__name__ = "__main__"
    exec(compile(source, "<ctf_servers>", "exec"), mod.__dict__)
