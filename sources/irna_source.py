import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Optional

from sources.base import NewsSource
from models.news import News


class IrnaNewsSource(NewsSource):
    """
    News source based on IRNA RSS feed
    Image is extracted from the news HTML page (og:image)
    """

    RSS_URL = "https://www.irna.ir/rss"

    def fetch(self) -> List[News]:
        feed = feedparser.parse(
            self.RSS_URL,
            request_headers={
                "User-Agent": "Mozilla/5.0 (NewsScraper MVP)"
            }
        )

        news_list: List[News] = []

        if not feed.entries:
            return news_list

        for entry in feed.entries[:5]:  # MVP: فقط ۵ خبر
            published_at = self._parse_published_at(entry)
            link = entry.get("link")

            image_url = self._extract_image_from_page(link)

            news = News(
                title=(entry.get("title") or "").strip(),
                url=link,
                source="IRNA",
                published_at=published_at,
                summary=entry.get("summary"),
                image_url=image_url
            )

            news_list.append(news)

        return news_list

    def _parse_published_at(self, entry) -> Optional[datetime]:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6])
        return None

    def _extract_image_from_page(self, url: str | None) -> Optional[str]:
        """
        Extract image from HTML page using og:image meta tag
        """
        if not url:
            return None

        try:
            response = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=5
            )
            if response.status_code != 200:
                return None

            soup = BeautifulSoup(response.text, "html.parser")

            meta = soup.find("meta", property="og:image")
            if meta and meta.get("content"):
                return meta["content"]

        except Exception:
            return None

        return None