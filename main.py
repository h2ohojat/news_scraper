from collector.news_collector import NewsCollector
from sources.irna_source import IrnaNewsSource
from processor.news_processor import NewsProcessor


def main():
    print("🚀 Eitaa News App started")
    print("📰 Collecting news...")

    sources = [IrnaNewsSource()]
    collector = NewsCollector(sources)

    news = collector.collect()

    processor = NewsProcessor()
    news = processor.process(news)

    print(f"✅ Collected {len(news)} news items")

    for item in news:
        print("-", item.title)
        if item.summary:
            print("  📝", item.summary)
        if item.image_url:
            print("  🖼️", item.image_url)


if __name__ == "__main__":
    main()