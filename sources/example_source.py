from datetime import datetime
from sources.base import NewsSource
from models.news import News


class ExampleNewsSource(NewsSource):
    """
    Example implementation of a news source
    """

    def fetch(self):
        return [
            News(
                title="Example News Title",
                url="https://example.com/news/1",
                source="Example",
                published_at=datetime.now(),
                summary="This is a sample news item for testing."
            )
        ]