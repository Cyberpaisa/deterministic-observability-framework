import time
import logging
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# Configuración de logging para soberanía
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ScrapingEngine")

class ScrapingEngine:

    def __init__(self, headless=True):
        self.headless = headless

    def fetch_page(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()

            page.goto(url, timeout=60000)
            time.sleep(2)

            html = page.content()
            browser.close()

        return html

    def parse(self, html, selectors):
        soup = BeautifulSoup(html, "html.parser")
        data = {}

        for key, selector in selectors.items():
            try:
                elements = soup.select(selector)
                data[key] = [el.get_text(strip=True) for el in elements]
            except Exception as e:
                logger.error(f"Error parsing selector {selector}: {e}")
                data[key] = []

        return data

    def get_clean_text(self, html):
        """Extrae texto limpio para alimentar el contexto de Enigma."""
        soup = BeautifulSoup(html, "html.parser")
        # Eliminar scripts y estilos
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text(separator="\n", strip=True)

    def run(self, url, selectors=None):
        try:
            html = self.fetch_page(url)
            if selectors:
                return self.parse(html, selectors)
            return {"text": self.get_clean_text(html)}
        except Exception as e:
            logger.error(f"Fallo crítico en scraping de {url}: {e}")
            return {"error": str(e)}


