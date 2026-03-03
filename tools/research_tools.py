"""Herramientas de investigación y análisis de tech stack.
Fallback chain: Serper (Google) → Tavily → DuckDuckGo
"""

import os
import json
from pathlib import Path
from crewai.tools import BaseTool


def _search_serper(query: str, max_results: int = 5) -> list | None:
    """Google via Serper.dev (2500/mes gratis)."""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return None
    try:
        import requests
        resp = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": max_results},
            timeout=10,
        )
        data = resp.json()
        results = []
        for item in data.get("organic", [])[:max_results]:
            results.append({
                "title": item.get("title", ""),
                "href": item.get("link", ""),
                "body": item.get("snippet", ""),
            })
        return results if results else None
    except Exception:
        return None


def _search_tavily(query: str, max_results: int = 5) -> list | None:
    """Tavily AI Search (1000/mes gratis)."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return None
    try:
        import requests
        resp = requests.post(
            "https://api.tavily.com/search",
            json={"api_key": api_key, "query": query, "max_results": max_results},
            timeout=10,
        )
        data = resp.json()
        results = []
        for item in data.get("results", [])[:max_results]:
            results.append({
                "title": item.get("title", ""),
                "href": item.get("url", ""),
                "body": item.get("content", "")[:300],
            })
        return results if results else None
    except Exception:
        return None


def _search_ddgs(query: str, max_results: int = 5) -> list | None:
    """DuckDuckGo (gratis, sin API key)."""
    try:
        from ddgs import DDGS
        results = DDGS().text(query, region="us-en", max_results=max_results)
        return results if results else None
    except Exception:
        return None


def web_search_with_fallback(query: str, max_results: int = 5) -> list:
    """Busca usando el primer motor disponible: Serper → Tavily → DuckDuckGo."""
    for searcher in [_search_serper, _search_tavily, _search_ddgs]:
        results = searcher(query, max_results)
        if results:
            return results
    return []


class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Busca información actualizada en internet. "
        "Usa Google (Serper), Tavily o DuckDuckGo automáticamente. "
        "Retorna los 5 resultados más relevantes con título, URL y resumen. "
        "Input: consulta de búsqueda en INGLÉS para mejores resultados."
    )

    def _run(self, query: str) -> str:
        """Búsqueda web con fallback chain."""
        try:
            results = web_search_with_fallback(query)
            if not results:
                return f"No se encontraron resultados para: {query}"
            output = f"Resultados para: {query}\n{'='*50}\n\n"
            for i, r in enumerate(results, 1):
                output += f"{i}. {r['title']}\n   URL: {r['href']}\n   {r['body']}\n\n"
            return output
        except Exception as e:
            return f"Error en búsqueda: {e}. Continúa con tu conocimiento interno."


class WebResearchTool(BaseTool):
    name: str = "web_research_brief"
    description: str = (
        "Genera un brief de investigación estructurado sobre un tema "
        "Y busca información real en internet. "
        "Input: tema o idea a investigar."
    )

    def _run(self, topic: str) -> str:
        """Genera estructura de investigación + búsqueda web real."""
        web_results = ""
        try:
            results = web_search_with_fallback(f"{topic} market analysis 2025 2026")
            if results:
                web_results = "\nDATOS REALES DE INTERNET:\n"
                for r in results:
                    web_results += f"  - {r['title']}: {r['body'][:200]}\n"
                web_results += "\n"
        except Exception:
            web_results = "\nBúsqueda web no disponible. Usa tu conocimiento interno.\n\n"

        brief = f"""BRIEF DE INVESTIGACIÓN: {topic}
{'='*60}
{web_results}
PREGUNTAS CLAVE:
  - Tamaño del mercado para {topic}?
  - Principales competidores?
  - Problema principal que resuelve?
  - Demanda validada?
  - Modelo de negocio más viable?

FRAMEWORK DE VALIDACIÓN:
  - Problem-Solution Fit: problema real y frecuente?
  - Market Size: mercado justifica esfuerzo?
  - Competition: espacio para diferenciarse?
  - Feasibility: MVP en 2-4 semanas?
  - Revenue: disposición a pagar?

ENTREGABLE:
  - Resumen ejecutivo con datos concretos
  - Análisis competitivo (tabla con precios)
  - Go/No-Go con justificación basada en datos
  - Siguiente paso concreto
"""
        return brief


class TechStackAnalyzerTool(BaseTool):
    name: str = "analyze_tech_stack"
    description: str = (
        "Analiza el tech stack actual de un proyecto leyendo package.json, "
        "requirements.txt, pyproject.toml, docker-compose.yml, etc. "
        "Sugiere mejoras y detecta dependencias desactualizadas o inseguras. "
        "Input: ruta al directorio del proyecto."
    )

    def _run(self, project_path: str) -> str:
        path = Path(project_path)
        if not path.exists():
            return f"Directorio no encontrado: {project_path}"

        report = f"ANÁLISIS DE TECH STACK: {project_path}\n{'='*60}\n"

        # Leer package.json
        pkg_json = path / "package.json"
        if pkg_json.exists():
            try:
                pkg = json.loads(pkg_json.read_text())
                deps = pkg.get("dependencies", {})
                dev_deps = pkg.get("devDependencies", {})
                scripts = pkg.get("scripts", {})
                report += f"\nJAVASCRIPT/NODE.JS:\n"
                report += f"  Framework: {self._detect_framework(deps)}\n"
                report += f"  Dependencias: {len(deps)} producción + {len(dev_deps)} desarrollo\n\n"
                report += "  Principales:\n"
                for k, v in list(deps.items())[:15]:
                    report += f"    {k}: {v}\n"
                report += "\n  Scripts:\n"
                for k, v in scripts.items():
                    report += f"    {k}: {v}\n"
            except Exception as e:
                report += f"  Error leyendo package.json: {e}\n"

        # Leer requirements.txt
        req_txt = path / "requirements.txt"
        if req_txt.exists():
            try:
                reqs = [l.strip() for l in req_txt.read_text().splitlines() if l.strip() and not l.startswith("#")]
                report += f"\nPYTHON:\n  Dependencias: {len(reqs)}\n\n  Paquetes:\n"
                for r in reqs[:20]:
                    report += f"    {r}\n"
            except Exception as e:
                report += f"  Error leyendo requirements.txt: {e}\n"

        # pyproject.toml
        if (path / "pyproject.toml").exists():
            report += "\n  pyproject.toml encontrado\n"

        # Docker
        if (path / "docker-compose.yml").exists():
            report += "\nDocker Compose encontrado\n"
        if (path / "Dockerfile").exists():
            report += "Dockerfile encontrado\n"

        # .env seguridad
        if (path / ".env").exists() and not (path / ".env.example").exists():
            report += "\nSEGURIDAD: .env existe pero no hay .env.example\n"

        if not (path / ".gitignore").exists():
            report += "\nNo hay .gitignore — riesgo de subir archivos sensibles\n"

        report += "\nRECOMENDACIONES:\n"
        report += "  - Verificar dependencias actualizadas\n"
        report += "  - .env en .gitignore\n"
        report += "  - Agregar linting si no existe\n"
        report += "  - Agregar testing si no existe\n"
        return report

    @staticmethod
    def _detect_framework(deps: dict) -> str:
        if "next" in deps:
            return "Next.js"
        if "react" in deps:
            return "React"
        if "vue" in deps:
            return "Vue.js"
        if "svelte" in deps:
            return "Svelte"
        if "express" in deps:
            return "Express.js"
        if "fastify" in deps:
            return "Fastify"
        return "No detectado"
