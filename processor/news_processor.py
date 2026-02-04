import re
from typing import List
from bs4 import BeautifulSoup

from models.news import News


class NewsProcessor:
    """
    Process and prepare news items
    """

    def __init__(self, max_summary_length: int = 300):
        self.max_summary_length = max_summary_length

    def process(self, news_list: List[News]) -> List[News]:
        processed = []

        for news in news_list:
            # ✅ فقط اگر Source تصویر نداده، تلاش کن از summary بگیری
            if not news.image_url:
                news.image_url = self._extract_image_from_summary(news.summary)

            # ✅ خلاصه را تمیز کن (بدون دست زدن به image)
            news.summary = self._clean_summary(news.summary)

            processed.append(news)

        return processed

    def _clean_summary(self, summary: str | None) -> str | None:
        if not summary:
            return None

        text = BeautifulSoup(summary, "html.parser").get_text()
        text = re.sub(r"\s+", " ", text).strip()

        if len(text) > self.max_summary_length:
            text = text[: self.max_summary_length] + "..."

        return text

    def _extract_image_from_summary(self, summary: str | None) -> str | None:
        """
        Fallback image extraction from HTML summary (if exists)
        """
        if not summary:
            return None

        soup = BeautifulSoup(summary, "html.parser")
        img = soup.find("img")

        if img and img.get("src"):
            return img["src"]

        return None