"""
Entry point of Eitaa News Scraper project
"""

from collector.news_collector import NewsCollector


def main():
    print("🚀 Eitaa News App started")

    collector = NewsCollector()

    news_list = collector.collect()

    print(f"✅ Collected {len(news_list)} news items")


if __name__ == "__main__":
    main()