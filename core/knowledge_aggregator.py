import os
import glob

class RepositoryAggregator:
    """
    Agregador de archivos para alimentar ventanas de contexto masivas (1M tokens).
    Permite a Enigma entender TODO el proyecto de una sola vez.
    """
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.ignore_patterns = [".git", "__pycache__", "node_modules", ".venv", "*.png", "*.jpg"]

    def aggregate_all(self) -> str:
        """
        Lee todos los archivos relevantes y los concatena en un solo buffer.
        """
        full_context = ""
        for file_path in glob.iglob(os.path.join(self.root_dir, '**', '*'), recursive=True):
            if os.path.isfile(file_path):
                # Filtro básico de ignorados
                if any(p in file_path for p in self.ignore_patterns):
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content: str = f.read()
                        full_context += f"\n\n--- FILE: {file_path} ---\n{file_content}"
                except Exception:
                    continue
        
        return full_context

if __name__ == "__main__":
    agg = RepositoryAggregator("./")
    # print(f"Contexto total: {len(agg.aggregate_all())} caracteres.")
