from collector.news_collector import NewsCollector
from sources.irna_source import IrnaNewsSource


def main():
    print("🚀 Eitaa News App started")
    print("📰 Collecting news...")

    sources = [IrnaNewsSource()]
    collector = NewsCollector(sources)

    news = collector.collect()
    print(f"✅ Collected {len(news)} news items")

    for item in news:
        print("-", item.title)


if __name__ == "__main__":
    main()