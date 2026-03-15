"""Herramientas de integración con redes sociales para DOF Agent.
Permite al agente publicar actualizaciones en X (Twitter).
"""

import os
import logging
from crewai.tools import BaseTool

logger = logging.getLogger(__name__)

class XPostTool(BaseTool):
    name: str = "post_to_x"
    description: str = (
        "Publica un mensaje (tweet) en la cuenta de X (Twitter) del operador. "
        "Útil para anuncios de hitos, estados de salud del sistema o actualizaciones del hackathon. "
        "Input: el texto del mensaje a publicar (máximo 280 caracteres)."
    )

    def _run(self, tweet_text: str) -> str:
        """Envía un post a X usando la API v2."""
        # Se requieren: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET
        api_key = os.getenv("X_API_KEY")
        api_secret = os.getenv("X_API_SECRET")
        access_token = os.getenv("X_ACCESS_TOKEN")
        access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

        if not all([api_key, api_secret, access_token, access_token_secret]):
            return (
                "Error: Faltan credenciales de X en el archivo .env. "
                "Se requieren: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET."
            )

        try:
            import tweepy
            # Autenticación para la API v2
            client = tweepy.Client(
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            
            response = client.create_tweet(text=tweet_text)
            tweet_id = response.data['id']
            
            log_msg = f"Tweet publicado exitosamente. ID: {tweet_id}"
            logger.info(log_msg)
            return f"DOF SUCCESS: {log_msg}. Texto: {tweet_text}"

        except ImportError:
            return "Error: La librería 'tweepy' no está instalada. Ejecuta 'pip install tweepy'."
        except Exception as e:
            error_msg = f"Error al publicar en X: {str(e)}"
            logger.error(error_msg)
            return error_msg
