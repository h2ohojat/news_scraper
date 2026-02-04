import feedparser
from datetime import datetime
from typing import List

from sources.base import NewsSource
from models.news import News


class IrnaNewsSource(NewsSource):
    """
    News source based on IRNA RSS feed
    """

    RSS_URL = "https://www.irna.ir/rss"

    def fetch(self) -> List[News]:
        feed = feedparser.parse(self.RSS_URL)
        news_list: List[News] = []

        if not feed.entries:
            return news_list

        for entry in feed.entries[:5]:  # MVP: ۵ خبر
            published_at = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published_at = datetime(*entry.published_parsed[:6])

            news_list.append(
                News(
                    title=entry.get("title", "").strip(),
                    url=entry.get("link"),
                    source="IRNA",
                    published_at=published_at,
                    summary=entry.get("summary")
                )
            )

        return news_list