from core.scraping_engine import ScrapingEngine

engine = ScrapingEngine()

data = engine.run(
    "https://news.ycombinator.com",
    {
        "titles": ".titleline a"
    }
)

print(data)


