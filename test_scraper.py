from core.scraping_engine import ScrapingEngine
from bs4 import BeautifulSoup

engine = ScrapingEngine()

html = engine.fetch_page("https://news.ycombinator.com")

soup = BeautifulSoup(html, "html.parser")

rows = soup.select("tr.athing")

results = []

for row in rows[:10]:
    title_tag = row.select_one(".titleline a")
    source_tag = row.select_one(".sitestr")

    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    source = source_tag.get_text(strip=True) if source_tag else "N/A"

    results.append((title, source))

for i, (title, source) in enumerate(results):
    print(f"{i+1}. {title} ({source})")
