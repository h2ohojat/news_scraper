class NewsCollector:
    """
    Collects news from multiple news sources
    """

    def __init__(self, sources=None):
        self.sources = sources or []

    def collect(self):
        all_news = []

        for source in self.sources:
            try:
                news_items = source.fetch()
                all_news.extend(news_items)
            except Exception as e:
                print(f"⚠️ Error collecting from {source}: {e}")

        return all_news