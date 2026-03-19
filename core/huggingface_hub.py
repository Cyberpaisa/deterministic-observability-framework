import os
from huggingface_hub import hf_hub_download, list_models

class EnigmaHFHub:
    """
    Integración con Hugging Face para absorber modelos gratuitos.
    """
    def __init__(self, token=None):
        self.token = token or os.getenv("HF_TOKEN")
        self.cache_dir = "models/hf_cache"

    def search_models(self, query: str, limit: int = 5):
        """Busca modelos en el hub."""
        models = list_models(filter=query, limit=limit)
        return [{"id": m.modelId, "downloads": m.downloads} for m in models]

    def download_model(self, model_id: str, filename: str):
        """Descarga un modelo para uso local (ej: GGUF)."""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        
        path = hf_hub_download(repo_id=model_id, filename=filename, cache_dir=self.cache_dir)
        return path

if __name__ == "__main__":
    hub = EnigmaHFHub()
    # print(hub.search_models("Llama-3", limit=3))
