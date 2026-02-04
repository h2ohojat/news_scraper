import feedparser
from datetime import datetime
from typing import List, Optional

from sources.base import NewsSource
from models.news import News


class TasnimNewsSource(NewsSource):
    """
    Tasnim News RSS Source (FINAL & STABLE)
    """

    RSS_URL = "https://www.tasnimnews.ir/fa/rss/feed/0/0/8/1/TopStories"

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

        for entry in feed.entries[:5]:
            print("----- ENTRY KEYS -----")
            print(entry.keys())
            print("----- MEDIA RELATED -----")
            print("media_content:", entry.get("media_content"))
            print("media_thumbnail:", entry.get("media_thumbnail"))
            print("links:", entry.get("links"))
            print("------------------------")

            news = News(
                title=(entry.get("title") or "").strip(),
                url=entry.get("link"),
                source="Tasnim",
                published_at=self._parse_published_at(entry),
                summary=entry.get("summary"),
                image_url=self._extract_image(entry)
            )

            news_list.append(news)

        return news_list

    def _parse_published_at(self, entry) -> Optional[datetime]:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6])
        return None

    def _extract_image(self, entry) -> Optional[str]:
        """
        Extract image from Tasnim RSS (media:content or media:thumbnail)
        """

        # ✅ اول media:content (تصویر اصلی)
        media_content = entry.get("media_content")
        if media_content and isinstance(media_content, list):
            url = media_content[0].get("url")
            if url:
                return url

        # ✅ بعد media:thumbnail
        media_thumbnail = entry.get("media_thumbnail")
        if media_thumbnail and isinstance(media_thumbnail, list):
            url = media_thumbnail[0].get("url")
            if url:
                return url

        return None