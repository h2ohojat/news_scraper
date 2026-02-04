import re
from typing import List
from bs4 import BeautifulSoup

from models.news import News


class NewsProcessor:
    """
    Process and prepare news items for publishing
    """

    def __init__(self, max_summary_length: int = 300):
        self.max_summary_length = max_summary_length

    def process(self, news_list: List[News]) -> List[News]:
        processed = []

        for news in news_list:
            news.summary = self._clean_summary(news.summary)
            news.image_url = self._extract_image(news.summary)
            processed.append(news)

        return processed

    def _clean_summary(self, summary: str | None) -> str | None:
        if not summary:
            return None

        # حذف HTML
        text = BeautifulSoup(summary, "html.parser").get_text()
        text = re.sub(r"\s+", " ", text).strip()

        # کوتاه‌سازی
        if len(text) > self.max_summary_length:
            text = text[: self.max_summary_length] + "..."

        return text

    def _extract_image(self, summary: str | None) -> str | None:
        if not summary:
            return None

        soup = BeautifulSoup(summary, "html.parser")
        img = soup.find("img")

        if img and img.get("src"):
            return img["src"]

        return None