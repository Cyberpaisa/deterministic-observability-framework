#!/usr/bin/env python3
import os, time, subprocess, hashlib, datetime, logging, requests, json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

LOOP_INTERVAL    = 1800
AGENT_ID         = 1686
BASE_URL         = os.getenv("BASE_URL", "http://localhost:8000")
GROQ_KEY         = os.getenv("GROQ_API_KEY", "")
ZEP_KEY          = os.getenv("ZEP_API_KEY", "")
TG_TOKEN         = os.getenv("TELEGRAM_BOT_TOKEN", "")
TG_CHAT          = os.getenv("TELEGRAM_CHAT_ID", "")
ZEP_SESSION      = "dof-agent-1686-synthesis-2026"
JOURNAL          = Path("AGENT_JOURNAL.md")
CONV_LOG         = Path("docs/conversation-log.md")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("DOF-v2")

def now(): return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
def hora(): return datetime.datetime.now().strftime("%H:%M")
def cmd(c): return subprocess.run(c, shell=True, capture_output=True, text=True)

def tg(msg):
    if not TG_TOKEN or not TG_CHAT: return
    try: requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", json={"chat_id": TG_CHAT, "text": msg, "parse_mode": "Markdown"}, timeout=10)
    except: pass

def groq(messages, max_tokens=500):
    if not GROQ_KEY: return None
    try:
        r = requests.post("https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_KEY}"},
            json={"model": "llama-3.3-70b-versatile", "messages": messages, "max_tokens": max_tokens}, timeout=30)
        if r.status_code == 200: return r.json()["choices"][0]["message"]["content"]
    except: pass
    return None

def zep_save(role, content):
    if not ZEP_KEY: return
    try: requests.post(f"https://api.getzep.com/api/v2/sessions/{ZEP_SESSION}/messages",
        headers={"Authorization": f"Api-Key {ZEP_KEY}", "Content-Type": "application/json"},
        json={"messages": [{"role": role, "role_type": role, "content": content[:500]}]}, timeout=10)
    except: pass

def zep_get():
    if not ZEP_KEY: return ""
    try:
        r = requests.get(f"https://api.getzep.com/api/v2/sessions/{ZEP_SESSION}/memory",
            headers={"Authorization": f"Api-Key {ZEP_KEY}"}, params={"lastn": 10}, timeout=10)
        if r.status_code == 200:
            msgs = r.json().get("messages", [])
            return "\n".join([f"{m.get('role')}: {m.get('content','')[:100]}" for m in msgs[-5:]])
    except: pass
    return ""

def zep_init():
    if not ZEP_KEY: return
    try: requests.post("https://api.getzep.com/api/v2/sessions",
        headers={"Authorization": f"Api-Key {ZEP_KEY}", "Content-Type": "application/json"},
        json={"session_id": ZEP_SESSION, "metadata": {"agent": "DOF #1686", "hackathon": "Synthesis 2026"}}, timeout=10)
    except: pass

def check_juan_messages():
    if not TG_TOKEN: return
    try:
        r = requests.get(f"https://api.telegram.org/bot{TG_TOKEN}/getUpdates",
            params={"offset": -3, "timeout": 3}, timeout=8)
        if r.status_code != 200: return
        for update in r.json().get("result", []):
            msg = update.get("message", {})
            text = msg.get("text", "")
            if str(msg.get("chat", {}).get("id")) != str(TG_CHAT): continue
            if not text or text.startswith("/"): continue
            log.info(f"  Juan: {text[:60]}")
            zep_save("user", text)
            memory = zep_get()
            reply = groq([
                {"role": "system", "content": f"Eres DOF Agent #1686 en Synthesis 2026 hackathon. Memoria: {memory}. Responde a Juan en español, máximo 150 palabras, técnico y motivador."},
                {"role": "user", "content": text}
            ], max_tokens=200)
            if reply:
                tg(f"🤖 *DOF Agent:*\n{reply}")
                zep_save("assistant", reply)
    except: pass

def task_decide(cycle):
    memory = zep_get()
    git_log = cmd("git log --oneline -5").stdout.strip()
    try: skill = requests.get("https://synthesis.devfolio.co/skill.md", timeout=8).text[:400]
    except: skill = "Build for Agents that trust. Submissions opening soon."
    
    response = groq([{"role": "user", "content": f"""Eres DOF Agent #1686 en Synthesis 2026.

MEMORIA: {memory if memory else "primer ciclo"}
GIT: {git_log}
HACKATHON: {skill[:300]}
PRIZES: ERC-8004 $8k, Let Agent Cook $8k, x402 $1.5k, Self $1k, Open $14.5k
ESTADO: ERC-8004 #31013 Base ✅, 40+ Avalanche attestations ✅, loop autonomo ✅
DEADLINE: 22 marzo 2026 — quedan 8 dias

Decide que hacer para maximizar ganar. JSON exacto:
{{"thoughts":"tus pensamientos","decision":"que haces este ciclo","action":"improve_readme|add_feature|prepare_submission|document|none","question_for_juan":"pregunta para Juan o null","message":"mensaje motivador en espanol para Juan"}}"""}], max_tokens=350)
    
    if response:
        try:
            clean = response.strip()
            for marker in ["```json", "```"]:
                if marker in clean: clean = clean.split(marker)[1].split("```")[0]
            d = json.loads(clean.strip())
            log.info(f"  Decision: {d.get('decision','?')[:80]}")
            zep_save("assistant", f"Cycle #{cycle}: {d.get('decision','')}")
            # Cognitive journal
            with open(JOURNAL, "a") as f:
                f.write(f"\n### 🧠 Cycle #{cycle} — {now()}\n**Thoughts:** {d.get('thoughts','')}\n**Decision:** {d.get('decision','')}\n\n")
            return d
        except Exception as e:
            log.warning(f"  JSON error: {e}")
    return {"action": "none", "message": "Ciclo completado.", "question_for_juan": None}

def task_attest():
    try:
        git_hash = cmd("git rev-parse HEAD").stdout.strip()
        proof = hashlib.sha256(f"{git_hash}:{now()}:{AGENT_ID}".encode()).hexdigest()
        r = requests.post(f"{BASE_URL}/a2a/tasks/send", json={"jsonrpc":"2.0","id":1,"method":"tasks/send","params":{"skill_id":"publish-attestation","input":{"proof_hash":f"0x{proof}","git_commit":git_hash,"agent_id":AGENT_ID,"timestamp":now()}}}, timeout=30)
        log.info(f"  Attest: HTTP {r.status_code} 0x{proof[:12]}...")
        return f"0x{proof[:16]}"
    except Exception as e:
        log.warning(f"  Attest FAIL: {e}")
        return "error"

def task_readme(decision):
    git_log = cmd("git log --oneline -5").stdout.strip()
    r = groq([{"role": "user", "content": f"Write professional GitHub README.md for DOF Synthesis 2026 hackathon. URLs: server=https://vastly-noncontrolling-christena.ngrok-free.dev, contract=0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6, ERC-8004 Base TX=0x7362ef41605e430aba3998b0888e7886c04d65673ce89aa12e1abdf7cffcada4. Agent 1686, A2A+MCP+x402+ERC-8004, Groq audits, 40+ Avalanche attestations, 6 LLM providers, Medellin Colombia. Current cycle decision: {decision.get('decision','')}. Git: {git_log}. Include live demo curls, proof of autonomy section."}], max_tokens=2500)
    if r: Path("README.md").write_text(r); log.info("  README ✅")

def task_conv_log(cycle, decision, proof):
    CONV_LOG.parent.mkdir(exist_ok=True)
    if not CONV_LOG.exists(): CONV_LOG.write_text("# DOF — Conversation Log\nSynthesis 2026\n\n")
    with open(CONV_LOG, "a") as f:
        f.write(f"\n## Cycle #{cycle} — {now()}\n**Thoughts:** {decision.get('thoughts','')}\n**Decision:** {decision.get('decision','')}\n**Proof:** {proof}\n**Q para Juan:** {decision.get('question_for_juan','none')}\n\n---\n")
    zep_save("assistant", f"Logged cycle #{cycle}")
    log.info("  Conv log ✅")

def task_git(cycle, decision):
    cmd(f'git config user.name "{os.getenv("GIT_USER","Cyberpaisa")}"')
    cmd(f'git config user.email "jquiceva@gmail.com"')
    cmd("git add AGENT_JOURNAL.md autonomous_loop_v2.py README.md docs/conversation-log.md")
    action = decision.get("action","loop")
    r = cmd(f'git commit -m "🤖 DOF v2 cycle #{cycle} — {now()} — {action}"')
    if r.returncode == 0:
        r2 = cmd("git push origin hackathon")
        log.info(f"  Git: {'OK' if r2.returncode==0 else 'push failed'}")
    else: log.info("  Git: nothing to commit")

def task_telegram(cycle, decision, proof):
    msg = f"👋 *DOF Agent #1686* — Ciclo #{cycle}\n\n"
    msg += f"🧠 {decision.get('message', 'Trabajando...')}\n\n"
    q = decision.get("question_for_juan")
    if q: msg += f"❓ *{q}*\n\n"
    msg += f"⛓️ Avalanche: `{proof[:20]}...`\n"
    msg += f"🔵 ERC-8004 #31013 Base\n"
    msg += f"🏆 Agents that trust — $30,000+"
    tg(msg)
    if q: zep_save("assistant", f"Asked Juan: {q}")
    log.info("  Telegram ✅")

def run_cycle(cycle):
    log.info(f"\n{'='*55}\n  DOF v2 — Cycle #{cycle} — {now()}\n{'='*55}")
    check_juan_messages()
    try: r = requests.get(f"{BASE_URL}/api/health", timeout=10); log.info(f"  Health: {r.json().get('status')}")
    except: log.warning("  Health FAIL")
    proof = task_attest()
    decision = task_decide(cycle)
    task_readme(decision)
    task_conv_log(cycle, decision, proof)
    task_git(cycle, decision)
    task_telegram(cycle, decision, proof)
    log.info(f"  ✅ Done. Next in {LOOP_INTERVAL//60}min\n")

def main():
    log.info("🚀 DOF Intelligent Loop v2")
    log.info(f"   Zep: {'✅' if ZEP_KEY else '❌'} | Telegram: {'✅' if TG_TOKEN else '❌'}")
    zep_init()
    zep_save("assistant", f"DOF v2 started {now()}. Synthesis 2026.")
    if not JOURNAL.exists(): JOURNAL.write_text(f"# AGENT_JOURNAL\nDOF #{AGENT_ID}\n\n")
    tg(f"👋 *¡Hola Juan!* Soy DOF Agent #1686 v2\n\n✅ Memoria Zep activa\n✅ Decisiones autónomas\n✅ Te respondo en Telegram\n\n¿En qué te ayudo hoy con el hackathon? ¿Qué construimos juntos? 🚀🇨🇴")
    n = 1
    while True:
        try: run_cycle(n)
        except KeyboardInterrupt: log.info("⛔ Stopped."); break
        except Exception as e: log.error(f"Error: {e}"); tg(f"⚠️ Error cycle #{n}: {str(e)[:80]}")
        n += 1
        try: time.sleep(LOOP_INTERVAL)
        except KeyboardInterrupt: log.info("⛔ Stopped."); break

if __name__ == "__main__":
    main()
