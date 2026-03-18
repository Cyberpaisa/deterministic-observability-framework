from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

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
            elements = soup.select(selector)
            data[key] = [el.get_text(strip=True) for el in elements]

        return data

    def run(self, url, selectors):
        html = self.fetch_page(url)
        return self.parse(html, selectors)


