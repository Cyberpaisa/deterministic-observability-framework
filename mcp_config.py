"""
Configuración de MCP Servers — herramientas externas para agentes.

MCP Servers gratuitos disponibles:
  - Filesystem: leer/escribir archivos en directorios permitidos
  - Web Search:  búsqueda Google gratis (sin API key)
  - Fetch:       descargar y convertir páginas web a markdown
  - Memory:      knowledge graph persistente (complementa ChromaDB)

Uso: importar get_mcp_servers() y pasar como mcps= al Agent.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def get_filesystem_mcp(allowed_dir: str | None = None):
    """MCP Server: acceso a filesystem en directorios permitidos."""
    from crewai.mcp import MCPServerStdio

    target_dir = allowed_dir or OUTPUT_DIR
    os.makedirs(target_dir, exist_ok=True)

    return MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", target_dir],
        cache_tools_list=True,
    )


def get_web_search_mcp():
    """MCP Server: búsqueda web gratis (Google scraping, sin API key)."""
    from crewai.mcp import MCPServerStdio

    return MCPServerStdio(
        command="npx",
        args=["-y", "@pskill9/web-search"],
        cache_tools_list=True,
    )


def get_fetch_mcp():
    """MCP Server: fetch de URLs y conversión a markdown."""
    from crewai.mcp import MCPServerStdio

    return MCPServerStdio(
        command="npx",
        args=["-y", "@anthropics/mcp-server-fetch"],
        cache_tools_list=True,
    )


def get_memory_mcp():
    """MCP Server: knowledge graph persistente (complementa ChromaDB)."""
    from crewai.mcp import MCPServerStdio

    return MCPServerStdio(
        command="npx",
        args=["-y", "@anthropics/mcp-server-memory"],
        cache_tools_list=True,
    )


# ═══════════════════════════════════════════════════════
# PERFILES DE MCP POR ROL
# ═══════════════════════════════════════════════════════

def get_mcp_for_role(role: str, project_dir: str | None = None) -> list:
    """
    Retorna lista de MCP servers según el rol del agente.

    | Rol              | MCPs                              |
    |------------------|-----------------------------------|
    | code_architect   | filesystem, fetch                 |
    | research_analyst | web_search, fetch                 |
    | data_engineer    | filesystem                        |
    | project_organizer| filesystem                        |
    | narrative_content| web_search, fetch                 |
    | mvp_strategist   | web_search                        |
    | qa_reviewer      | web_search, fetch                 |
    | verifier         | web_search                        |
    """
    role = role.lower()

    if role == "code_architect":
        return [get_filesystem_mcp(project_dir), get_fetch_mcp()]

    if role == "research_analyst":
        return [get_web_search_mcp(), get_fetch_mcp()]

    if role == "data_engineer":
        return [get_filesystem_mcp(project_dir)]

    if role == "project_organizer":
        return [get_filesystem_mcp(project_dir)]

    if role == "narrative_content":
        return [get_web_search_mcp(), get_fetch_mcp()]

    if role == "mvp_strategist":
        return [get_web_search_mcp()]

    if role in ("qa_reviewer", "verifier"):
        return [get_web_search_mcp()]

    return []
