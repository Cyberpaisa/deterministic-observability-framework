"""
Streamlit Dashboard — Mission Control Visual.
Cyber Paisa / Enigma Group

Lanzar con: streamlit run interfaces/streamlit_dashboard.py --server.port 8501
"""

import os
import sys
import glob
from datetime import datetime

import streamlit as st
import yaml

# Agregar directorio padre al path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ═══════════════════════════════════════════════════════
# CONFIGURACION DE PAGINA
# ═══════════════════════════════════════════════════════

st.set_page_config(
    page_title="Cyber Paisa Mission Control",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Cyber Paisa Mission Control")
st.caption("8 Agentes AI — Multi-proyecto — CrewAI Pro")


# ═══════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════

def load_projects():
    """Carga proyectos desde projects.yaml."""
    projects_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config", "projects.yaml",
    )
    if not os.path.exists(projects_path):
        return []
    with open(projects_path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("projects", []) if data else []


def load_api_status():
    """Verifica estado de API keys."""
    keys = {
        "Groq": "GROQ_API_KEY",
        "NVIDIA": "NVIDIA_API_KEY",
        "OpenRouter": "OPENROUTER_API_KEY",
        "Cerebras": "CEREBRAS_API_KEY",
        "SambaNova": "SAMBANOVA_API_KEY",
        "Gemini": "GEMINI_API_KEY",
        "Telegram": "TELEGRAM_BOT_TOKEN",
    }
    return {name: bool(os.getenv(env)) for name, env in keys.items()}


def get_output_files(project_filter=None):
    """Lista archivos de output recientes."""
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
    if not os.path.exists(base):
        return []
    pattern = os.path.join(base, "**", "*.md")
    files = glob.glob(pattern, recursive=True)
    files.sort(key=os.path.getmtime, reverse=True)
    if project_filter:
        files = [f for f in files if project_filter.lower() in f.lower()]
    return files[:20]


# ═══════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════

with st.sidebar:
    st.header("⚙️ Configuracion")

    # Selector de proyecto
    projects = load_projects()
    project_names = ["General (todos)"] + [p["name"] for p in projects]
    selected_project = st.selectbox("Proyecto:", project_names)
    project = None if selected_project == "General (todos)" else selected_project

    st.divider()

    # Selector de modo
    mode = st.selectbox("Modo de ejecucion:", [
        "grant-hunt", "content", "daily-ops", "weekly-report",
        "research", "full-mvp", "code-review", "data",
    ])

    # Input de tarea
    task_input = st.text_area("Descripcion de la tarea:", height=100)

    # Upload de archivo Excel
    uploaded_file = st.file_uploader("Archivo Excel/CSV (opcional):", type=["xlsx", "csv"])

    # Boton de ejecucion
    if st.button("🚀 Ejecutar Crew", type="primary", use_container_width=True):
        st.session_state["running"] = True
        st.session_state["mode"] = mode
        st.session_state["task"] = task_input
        st.session_state["project"] = project

    st.divider()

    # Status de APIs
    st.subheader("APIs")
    api_status = load_api_status()
    for name, active in api_status.items():
        emoji = "🟢" if active else "🔴"
        st.text(f"{emoji} {name}")


# ═══════════════════════════════════════════════════════
# TABS PRINCIPALES
# ═══════════════════════════════════════════════════════

tab_ops, tab_grants, tab_agents, tab_outputs, tab_excel, tab_projects = st.tabs([
    "📊 Daily Ops", "🎯 Grants Pipeline", "🤖 Agentes",
    "📝 Outputs", "📈 Excel", "📋 Proyectos",
])

# --- TAB: Daily Ops ---
with tab_ops:
    st.subheader("Operaciones Diarias")
    st.info("Ejecuta el modo 'daily-ops' para generar el reporte matutino.")

    # Mostrar ultimo reporte diario si existe
    daily_files = [f for f in get_output_files() if "daily" in os.path.basename(f)]
    if daily_files:
        latest = daily_files[0]
        st.caption(f"Ultimo reporte: {os.path.basename(latest)}")
        with open(latest, "r") as f:
            st.markdown(f.read()[:5000])
    else:
        st.caption("No hay reportes diarios aun. Ejecuta daily-ops para generar uno.")


# --- TAB: Grants Pipeline ---
with tab_grants:
    st.subheader("Grant Pipeline")
    st.info("Ejecuta el modo 'grant-hunt' para buscar oportunidades.")

    grant_files = [f for f in get_output_files() if "grant" in os.path.basename(f)]
    if grant_files:
        latest = grant_files[0]
        st.caption(f"Ultimo reporte: {os.path.basename(latest)}")
        with open(latest, "r") as f:
            st.markdown(f.read()[:5000])
    else:
        st.caption("No hay reportes de grants aun.")


# --- TAB: Agentes ---
with tab_agents:
    st.subheader("8 Agentes Especializados")

    agents_data = [
        ("1", "Code Architect", "Kimi K2.5 > Qwen3 Coder > Groq", "0.2"),
        ("2", "Research Analyst & Grant Radar", "DeepSeek R1 > Gemini > Groq", "0.5"),
        ("3", "MVP Strategist & Grant Aligner", "Llama 405B > Gemini > Groq", "0.6"),
        ("4", "Data Engineer & Excel", "Qwen3-32B > Groq", "0.1"),
        ("5", "Project Organizer", "QwQ-32B (Groq)", "0.3"),
        ("6", "QA Reviewer", "DeepSeek R1 distill > Kimi > Groq", "0.2"),
        ("7", "Verifier / Quality Gate", "DeepSeek R1 distill > Kimi > Groq", "0.2"),
        ("8", "Narrative, Tokenomics & Growth", "Llama 405B > Gemini > Groq", "0.7"),
    ]

    cols = st.columns(4)
    for i, (num, name, llm, temp) in enumerate(agents_data):
        with cols[i % 4]:
            st.metric(label=f"#{num}", value=name[:20])
            st.caption(f"LLM: {llm[:30]}...")
            st.caption(f"Temp: {temp}")


# --- TAB: Outputs ---
with tab_outputs:
    st.subheader("Outputs Recientes")

    filter_project = project if project else None
    files = get_output_files(filter_project)

    if files:
        selected_file = st.selectbox(
            "Selecciona un archivo:",
            files,
            format_func=lambda x: os.path.basename(x),
        )
        if selected_file:
            with open(selected_file, "r") as f:
                content = f.read()
            st.markdown(content[:10000])
            st.download_button(
                "Descargar archivo",
                content,
                file_name=os.path.basename(selected_file),
            )
    else:
        st.caption("No hay outputs aun.")


# --- TAB: Excel ---
with tab_excel:
    st.subheader("Analisis de Excel/CSV")

    if uploaded_file:
        import pandas as pd
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.write(f"**Filas:** {len(df)} | **Columnas:** {len(df.columns)}")
            st.dataframe(df.head(50), use_container_width=True)

            st.subheader("Estadisticas")
            st.dataframe(df.describe(), use_container_width=True)

        except Exception as e:
            st.error(f"Error leyendo archivo: {e}")
    else:
        st.caption("Sube un archivo Excel/CSV en la barra lateral para analizarlo.")


# --- TAB: Proyectos ---
with tab_projects:
    st.subheader("Proyectos Registrados")
    if projects:
        for p in projects:
            status_emoji = "🟢" if p.get("status") == "active" else "🟡"
            with st.expander(f"{status_emoji} {p['name']} ({p.get('ecosystem', '?')})"):
                st.write(f"**Descripcion:** {p.get('description', 'N/A')}")
                st.write(f"**Estado:** {p.get('status', 'N/A')}")
                team = p.get("team", [])
                if team:
                    st.write(f"**Equipo:** {', '.join(team)}")
                else:
                    st.write("**Equipo:** Sin equipo definido")
    else:
        st.caption("No hay proyectos. Edita config/projects.yaml para agregar.")

    st.info("Para agregar proyectos, edita `config/projects.yaml`")


# ═══════════════════════════════════════════════════════
# EJECUCION DE CREW (si se presiono el boton)
# ═══════════════════════════════════════════════════════

if st.session_state.get("running"):
    st.session_state["running"] = False
    mode = st.session_state.get("mode", "")
    task = st.session_state.get("task", "")
    proj = st.session_state.get("project")

    with st.spinner(f"Ejecutando {mode}... esto puede tomar unos minutos"):
        try:
            from crew import (
                create_research_crew, create_full_mvp_crew,
                create_grant_hunt_crew, create_content_crew,
                create_daily_ops_crew, create_weekly_report_crew,
                create_code_review_crew, create_data_analysis_crew,
            )

            if mode == "research":
                crew = create_research_crew(task)
            elif mode == "full-mvp":
                crew = create_full_mvp_crew(task)
            elif mode == "grant-hunt":
                crew = create_grant_hunt_crew(task, proj)
            elif mode == "content":
                crew = create_content_crew(task, proj)
            elif mode == "daily-ops":
                crew = create_daily_ops_crew()
            elif mode == "weekly-report":
                crew = create_weekly_report_crew(proj)
            elif mode == "data":
                crew = create_data_analysis_crew(task or "Analizar datos")
            else:
                st.error(f"Modo {mode} no soportado en dashboard aun")
                crew = None

            if crew:
                result = crew.kickoff()
                st.success("Completado!")
                st.markdown(str(result)[:10000])

                # Guardar output
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                out_dir = f"output/{proj}" if proj else "output"
                os.makedirs(out_dir, exist_ok=True)
                out_path = f"{out_dir}/{mode}_{ts}.md"
                with open(out_path, "w") as f:
                    f.write(str(result))
                st.caption(f"Guardado en: {out_path}")

        except Exception as e:
            st.error(f"Error: {e}")
