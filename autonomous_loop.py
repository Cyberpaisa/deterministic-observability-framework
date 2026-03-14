#!/usr/bin/env python3
import os, time, subprocess, hashlib, datetime, logging, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LOOP_INTERVAL = int(os.getenv("LOOP_INTERVAL", "1800"))
AGENT_ID = int(os.getenv("DOF_AGENT_ID", "1686"))
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
VENICE_API_KEY = os.getenv("VENICE_API_KEY", "")
JOURNAL = Path("AGENT_JOURNAL.md")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("DOF-LOOP")

def now(): return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
def cmd(c): return subprocess.run(c, shell=True, capture_output=True, text=True)

def health_check():
    try:
        r = requests.get(f"{BASE_URL}/api/health", timeout=10)
        log.info(f"  Health: {r.json()}")
        return "ok"
    except Exception as e:
        log.warning(f"  Health FAIL: {e}")
        return "error"

def attest():
    try:
        git_hash = cmd("git rev-parse HEAD").stdout.strip()
        proof = hashlib.sha256(f"{git_hash}:{now()}:{AGENT_ID}".encode()).hexdigest()
        r = requests.post(f"{BASE_URL}/a2a/tasks/send",
            json={"agent_id": AGENT_ID, "git_commit": git_hash,
                  "proof_hash": f"0x{proof}", "timestamp": now()}, timeout=30)
        log.info(f"  Attest: HTTP {r.status_code} proof=0x{proof[:12]}...")
        return "ok"
    except Exception as e:
        log.warning(f"  Attest FAIL: {e}")
        return "error"

def venice_ping():
    if not VENICE_API_KEY:
        log.info("  Venice: sin API key")
        return "skipped"
    try:
        r = requests.post("https://api.venice.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {VENICE_API_KEY}"},
            json={"model": "llama-3.3-70b",
                  "messages": [{"role": "user", "content": f"DOF Agent #{AGENT_ID} ping. Reply OK."}],
                  "max_tokens": 10}, timeout=30)
        resp = r.json()["choices"][0]["message"]["content"]
        log.info(f"  Venice: {resp}")
        return "ok"
    except Exception as e:
        log.warning(f"  Venice FAIL: {e}")
        return "error"

def git_commit(cycle):
    cmd('git config user.name "Cyberpaisa"')
    cmd('git config user.email "jquiceva@gmail.com"')
    entry = f"\n## {now()} — Cycle #{cycle}\n- health ok\n- attest ok\n- venice {'ok' if VENICE_API_KEY else 'skipped'}\n"
    with open(JOURNAL, "a") as f: f.write(entry)
    cmd("git add AGENT_JOURNAL.md autonomous_loop.py")
    r = cmd(f'git commit -m "🤖 Autonomous cycle #{cycle} — {now()}"')
    if r.returncode == 0:
        r2 = cmd("git push origin main")
        log.info(f"  Git: {'commit+push OK' if r2.returncode==0 else 'commit OK / push failed: '+r2.stderr[:50]}")
    else:
        log.info("  Git: nada nuevo para commitear")

def run_cycle(n):
    log.info(f"\n{'='*50}\n  DOF LOOP — Cycle #{n} — {now()}\n{'='*50}")
    health_check()
    attest()
    venice_ping()
    git_commit(n)
    log.info(f"  ✅ Cycle #{n} done. Próximo en {LOOP_INTERVAL//60}min\n")

if not JOURNAL.exists():
    JOURNAL.write_text(f"# AGENT_JOURNAL\nAgent #{AGENT_ID} autonomous log\n")

log.info(f"🚀 DOF Autonomous Loop — Agent #{AGENT_ID} — {now()}")
n = 1
while True:
    try: run_cycle(n)
    except KeyboardInterrupt: log.info("⛔ Detenido."); break
    except Exception as e: log.error(f"Cycle error: {e}")
    n += 1
    try: time.sleep(LOOP_INTERVAL)
    except KeyboardInterrupt: log.info("⛔ Detenido."); break
