from sources.base import NewsSource


class ExampleNewsSource(NewsSource):
    """
    Example implementation of a news source
    """

    def fetch(self):
        return [
            {
                "title": "Example News Title",
                "url": "https://example.com/news/1",
                "source": "Example",
                "published_at": "2026-02-04"
            }
        ]