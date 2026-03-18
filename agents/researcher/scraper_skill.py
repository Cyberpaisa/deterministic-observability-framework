from core.scraping_engine import ScrapingEngine
from bs4 import BeautifulSoup

class ScraperSkill:

    def __init__(self):
        self.engine = ScrapingEngine()

    def scrape_hn(self, limit=10):
        html = self.engine.fetch_page("https://news.ycombinator.com")
        soup = BeautifulSoup(html, "html.parser")

        rows = soup.select("tr.athing")

        results = []

        for row in rows[:limit]:
            title_tag = row.select_one(".titleline a")
            source_tag = row.select_one(".sitestr")

            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            source = source_tag.get_text(strip=True) if source_tag else "N/A"

            results.append({
                "title": title,
                "source": source
            })

        return results
