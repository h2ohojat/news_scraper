from collector.news_collector import NewsCollector
from sources.example_source import ExampleNewsSource


def main():
    print("🚀 Eitaa News App started")

    sources = [
        ExampleNewsSource()
    ]

    collector = NewsCollector(sources)
    news = collector.collect()

    print(f"✅ Collected {len(news)} news items")


if __name__ == "__main__":
    main()