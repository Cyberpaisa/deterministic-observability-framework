"""Herramientas de ejecución de código para el Code Architect.
Permite escribir archivos, ejecutar Python, correr comandos y operar git.
Seguridad: path validation, command blocklist, timeouts, output truncation.
"""

import os
import subprocess
import shlex
from pathlib import Path
from crewai.tools import BaseTool

# ═══════════════════════════════════════════════════════
# SEGURIDAD
# ═══════════════════════════════════════════════════════

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_DIRS = [
    (BASE_DIR / "output").resolve(),
    Path.home() / "proyectos",
]

BLOCKED_COMMANDS = [
    "rm -rf /", "rm -rf ~", "sudo ", "chmod 777", "mkfs",
    "dd if=", "shutdown", "reboot", ":(){ :|:& };:",
    "curl | sh", "wget | sh", "curl | bash", "wget | bash",
]

BLOCKED_EXTENSIONS = {".pem", ".key", ".cert", ".p12", ".pfx"}
BLOCKED_FILENAMES = {".env", ".env.local", ".env.production", ".env.development"}

# Whitelist de binarios permitidos para RunCommandTool
ALLOWED_BINARIES = {
    "npm", "npx", "yarn", "pnpm", "bun",
    "pip", "pip3", "python3", "python", "node",
    "docker", "docker-compose",
    "make", "cargo", "go",
    "ls", "cat", "mkdir", "cp", "mv", "touch", "head", "tail", "wc",
    "curl", "wget",
    "git",  # redirigido a GitOperationsTool idealmente
    "echo", "which", "env", "printenv",
}

GIT_ALLOWED = {"init", "add", "commit", "status", "log", "diff",
               "branch", "checkout", "push", "pull", "clone", "remote", "tag"}

GIT_BLOCKED_PATTERNS = ["--force", "reset --hard", "clean -f", "push -f",
                         "push --force"]

MAX_OUTPUT = 5000


def _validate_path(file_path: str) -> Path:
    """Valida que el path esté en directorios permitidos."""
    resolved = Path(file_path).resolve()
    # Bloquear archivos y extensiones sensibles
    if resolved.name.lower() in BLOCKED_FILENAMES:
        raise ValueError(f"Archivo bloqueado: {resolved.name}")
    if resolved.suffix.lower() in BLOCKED_EXTENSIONS:
        raise ValueError(f"Extensión bloqueada: {resolved.suffix}")
    # Verificar directorio permitido
    for allowed in ALLOWED_DIRS:
        try:
            resolved.relative_to(allowed)
            return resolved
        except ValueError:
            continue
    raise ValueError(
        f"Path fuera de directorios permitidos: {resolved}\n"
        f"Permitidos: {[str(d) for d in ALLOWED_DIRS]}"
    )


def _validate_command(cmd: str) -> None:
    """Verifica que el comando no esté en la blocklist."""
    cmd_lower = cmd.lower().strip()
    for blocked in BLOCKED_COMMANDS:
        if blocked in cmd_lower:
            raise ValueError(f"Comando bloqueado por seguridad: {blocked}")


def _truncate(text: str, limit: int = MAX_OUTPUT) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... [truncado, {len(text)} chars total]"


# ═══════════════════════════════════════════════════════
# HERRAMIENTAS
# ═══════════════════════════════════════════════════════

class WriteFileTool(BaseTool):
    name: str = "write_file"
    description: str = (
        "Escribe contenido a un archivo. Crea directorios intermedios si no existen. "
        "Solo permite escribir en output/ o ~/proyectos/. "
        "Input formato: 'path|||contenido' (separado por |||). "
        "Ejemplo: 'output/mi_proyecto/main.py|||print(\"hello world\")'"
    )

    def _run(self, input_str: str) -> str:
        try:
            if "|||" not in input_str:
                return "Error: formato debe ser 'path|||contenido'. Ejemplo: 'output/app.py|||print(1)'"
            parts = input_str.split("|||", 1)
            file_path_str = parts[0].strip()
            content = parts[1]

            # Si es path relativo, hacerlo relativo a BASE_DIR
            if not Path(file_path_str).is_absolute():
                file_path_str = str(BASE_DIR / file_path_str)

            resolved = _validate_path(file_path_str)
            resolved.parent.mkdir(parents=True, exist_ok=True)
            resolved.write_text(content, encoding="utf-8")
            return f"Archivo escrito: {resolved} ({len(content)} chars, {content.count(chr(10))+1} líneas)"
        except ValueError as e:
            return f"Error de seguridad: {e}"
        except Exception as e:
            return f"Error escribiendo archivo: {e}"


class ExecutePythonTool(BaseTool):
    name: str = "execute_python"
    description: str = (
        "Ejecuta código Python en un proceso aislado con timeout de 60 segundos. "
        "Captura stdout y stderr. Ideal para probar scripts, validar lógica, "
        "ejecutar tests. Input: código Python a ejecutar."
    )

    def _run(self, code: str) -> str:
        try:
            result = subprocess.run(
                ["python3", "-c", code],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(BASE_DIR / "output"),
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            output = ""
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}\n"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}\n"
            if not output:
                output = "(sin output)"
            output += f"\nReturn code: {result.returncode}"
            return _truncate(output)
        except subprocess.TimeoutExpired:
            return "Error: timeout de 60 segundos excedido. Simplifica el código."
        except Exception as e:
            return f"Error ejecutando Python: {e}"


class RunCommandTool(BaseTool):
    name: str = "run_command"
    description: str = (
        "Ejecuta un comando (npm, pip, docker, make, python3, node, etc.) con timeout de 120s. "
        "Solo binarios permitidos: npm, pip, python3, node, docker, make, cargo, go, ls, mkdir, curl, git. "
        "Input formato: 'directorio|||comando' o solo 'comando' (usa output/ por defecto). "
        "Ejemplo: 'output/mi_proyecto|||npm install'"
    )

    def _run(self, input_str: str) -> str:
        try:
            if "|||" in input_str:
                parts = input_str.split("|||", 1)
                work_dir = parts[0].strip()
                cmd = parts[1].strip()
            else:
                work_dir = str(BASE_DIR / "output")
                cmd = input_str.strip()

            _validate_command(cmd)

            # Parsear comando de forma segura
            cmd_parts = shlex.split(cmd)
            if not cmd_parts:
                return "Error: comando vacío."

            # Validar binario contra whitelist
            binary = Path(cmd_parts[0]).name
            if binary not in ALLOWED_BINARIES:
                return (
                    f"Binario no permitido: {binary}\n"
                    f"Permitidos: {', '.join(sorted(ALLOWED_BINARIES))}"
                )

            # Validar directorio de trabajo
            if not Path(work_dir).is_absolute():
                work_dir = str(BASE_DIR / work_dir)
            work_path = Path(work_dir).resolve()

            if not work_path.exists():
                return f"Directorio no existe: {work_path}"

            result = subprocess.run(
                cmd_parts,
                shell=False,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(work_path),
            )
            output = ""
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}\n"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}\n"
            if not output:
                output = "(sin output)"
            output += f"\nReturn code: {result.returncode}"
            return _truncate(output)
        except subprocess.TimeoutExpired:
            return "Error: timeout de 120 segundos excedido."
        except ValueError as e:
            return f"Error de seguridad: {e}"
        except Exception as e:
            return f"Error ejecutando comando: {e}"


class GitOperationsTool(BaseTool):
    name: str = "git_operation"
    description: str = (
        "Ejecuta operaciones git seguras. "
        "Permitidas: init, add, commit, status, log, diff, branch, checkout, push, pull, clone, remote, tag. "
        "Bloqueadas: force-push, reset --hard, clean -f. "
        "Input formato: 'directorio|||git comando' o solo 'git comando'. "
        "Ejemplo: 'output/mi_proyecto|||git init'"
    )

    def _run(self, input_str: str) -> str:
        try:
            if "|||" in input_str:
                parts = input_str.split("|||", 1)
                work_dir = parts[0].strip()
                cmd = parts[1].strip()
            else:
                work_dir = str(BASE_DIR / "output")
                cmd = input_str.strip()

            # Asegurar que empiece con git
            if not cmd.startswith("git "):
                cmd = f"git {cmd}"

            # Extraer subcomando
            git_parts = cmd.split()
            if len(git_parts) < 2:
                return "Error: especifica un subcomando git. Ej: git status"
            subcommand = git_parts[1]

            if subcommand not in GIT_ALLOWED:
                return f"Subcomando git no permitido: {subcommand}. Permitidos: {', '.join(sorted(GIT_ALLOWED))}"

            # Verificar patrones bloqueados
            cmd_str = " ".join(git_parts)
            for pattern in GIT_BLOCKED_PATTERNS:
                if pattern in cmd_str:
                    return f"Operación git bloqueada: {pattern}"

            if not Path(work_dir).is_absolute():
                work_dir = str(BASE_DIR / work_dir)

            result = subprocess.run(
                git_parts,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(Path(work_dir).resolve()),
            )
            output = ""
            if result.stdout:
                output += result.stdout
            if result.stderr:
                output += f"\n{result.stderr}"
            if not output.strip():
                output = "(sin output)"
            output += f"\nReturn code: {result.returncode}"
            return _truncate(output)
        except subprocess.TimeoutExpired:
            return "Error: timeout de 60 segundos excedido."
        except Exception as e:
            return f"Error en git: {e}"
