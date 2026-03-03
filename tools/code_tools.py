"""Herramientas para análisis y revisión de código."""

import os
import subprocess
from pathlib import Path
from crewai.tools import BaseTool
from pydantic import Field


class AnalyzeCodeTool(BaseTool):
    name: str = "analyze_code"
    description: str = (
        "Analiza un archivo de código fuente y devuelve su contenido junto con "
        "métricas básicas (líneas, funciones, imports, complejidad estimada). "
        "Input: ruta al archivo."
    )

    def _run(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            return f"❌ Archivo no encontrado: {file_path}"
        if not path.is_file():
            return f"❌ No es un archivo: {file_path}"

        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            return f"❌ Error leyendo archivo: {e}"

        lines = content.split("\n")
        total_lines = len(lines)
        blank_lines = sum(1 for l in lines if l.strip() == "")
        comment_lines = sum(1 for l in lines if l.strip().startswith(("#", "//", "/*", "*")))
        code_lines = total_lines - blank_lines - comment_lines

        # Detección básica por extensión
        ext = path.suffix.lower()
        functions = []
        classes = []
        imports = []

        if ext in (".py",):
            functions = [l.strip() for l in lines if l.strip().startswith("def ")]
            classes = [l.strip() for l in lines if l.strip().startswith("class ")]
            imports = [l.strip() for l in lines if l.strip().startswith(("import ", "from "))]
        elif ext in (".js", ".ts", ".jsx", ".tsx"):
            functions = [l.strip() for l in lines if "function " in l or "=>" in l]
            imports = [l.strip() for l in lines if l.strip().startswith(("import ", "require("))]

        report = f"""
📄 ANÁLISIS DE: {file_path}
{'='*60}
📊 Métricas:
  - Líneas totales: {total_lines}
  - Líneas de código: {code_lines}
  - Líneas en blanco: {blank_lines}
  - Comentarios: {comment_lines}
  - Ratio comentarios/código: {comment_lines/max(code_lines,1)*100:.1f}%

📦 Estructura:
  - Funciones encontradas: {len(functions)}
  - Clases encontradas: {len(classes)}
  - Imports: {len(imports)}

📝 Imports:
{chr(10).join(f'  {i}' for i in imports[:20])}

📝 Funciones:
{chr(10).join(f'  {f}' for f in functions[:20])}

{'='*60}
CÓDIGO FUENTE (primeras 200 líneas):
{'='*60}
{chr(10).join(lines[:200])}
"""
        return report


class ListProjectFilesTool(BaseTool):
    name: str = "list_project_files"
    description: str = (
        "Lista todos los archivos relevantes de un proyecto de código, "
        "excluyendo node_modules, .git, __pycache__, etc. "
        "Input: ruta al directorio del proyecto."
    )

    def _run(self, project_path: str) -> str:
        path = Path(project_path)
        if not path.exists():
            return f"❌ Directorio no encontrado: {project_path}"

        exclude_dirs = {
            "node_modules", ".git", "__pycache__", ".venv", "venv",
            "env", ".next", "dist", "build", ".cache", ".tox",
            "egg-info", ".eggs", ".mypy_cache", ".pytest_cache",
        }
        code_extensions = {
            ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go",
            ".rs", ".rb", ".php", ".sql", ".yaml", ".yml", ".json",
            ".toml", ".md", ".html", ".css", ".scss", ".vue", ".svelte",
        }

        files_by_type = {}
        total_lines = 0

        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for f in files:
                fp = Path(root) / f
                ext = fp.suffix.lower()
                if ext in code_extensions:
                    rel_path = fp.relative_to(path)
                    try:
                        line_count = sum(1 for _ in open(fp, errors="replace"))
                    except Exception:
                        line_count = 0
                    total_lines += line_count

                    if ext not in files_by_type:
                        files_by_type[ext] = []
                    files_by_type[ext].append((str(rel_path), line_count))

        report = f"📁 PROYECTO: {project_path}\n{'='*60}\n"
        report += f"📊 Total archivos de código: {sum(len(v) for v in files_by_type.values())}\n"
        report += f"📊 Total líneas: {total_lines:,}\n\n"

        for ext, files in sorted(files_by_type.items(), key=lambda x: -len(x[1])):
            report += f"\n{'ext.upper()'} ({len(files)} archivos):\n"
            for fpath, lc in sorted(files, key=lambda x: -x[1])[:15]:
                report += f"  {fpath} ({lc} líneas)\n"
            if len(files) > 15:
                report += f"  ... y {len(files)-15} archivos más\n"

        return report
