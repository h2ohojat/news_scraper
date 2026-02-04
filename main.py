import json
from pathlib import Path

from collector.news_collector import NewsCollector
from sources.tasnim_source import TasnimNewsSource
from processor.news_processor import NewsProcessor
from publisher.eitaa_publisher import EitaaPublisher
from models.news import News


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def news_to_dict(news: News) -> dict:
    """
    Convert News model to JSON-serializable dict
    """
    return {
        "title": news.title,
        "summary": news.summary,
        "image": news.image_url,
        "source": news.source,
        "url": news.url,
    }


def main():
    print("🚀 Eitaa News App started")
    print("📰 Collecting news...")

    # 1️⃣ Collect
    sources = [TasnimNewsSource()]
    collector = NewsCollector(sources)
    news_list = collector.collect()

    # 2️⃣ Process
    processor = NewsProcessor()
    processed_news = processor.process(news_list)

    # 3️⃣ Save JSON (✅ از خود News)
    output = [news_to_dict(news) for news in processed_news]

    output_file = DATA_DIR / "news.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ News saved to {output_file}")



if __name__ == "__main__":
    main()