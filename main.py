import json
from pathlib import Path

from collector.news_collector import NewsCollector
from sources.irna_source import IrnaNewsSource
from processor.news_processor import NewsProcessor
from publisher.eitaa_publisher import EitaaPublisher


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def main():
    print("🚀 Eitaa News App started")
    print("📰 Collecting news...")

    sources = [IrnaNewsSource()]
    collector = NewsCollector(sources)
    news_list = collector.collect()

    processor = NewsProcessor()
    processed_news = processor.process(news_list)

    publisher = EitaaPublisher()

    output = []
    for news in processed_news:
        output.append(publisher.format_message(news))

    output_file = DATA_DIR / "news.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ News saved to {output_file}")


if __name__ == "__main__":
    main()