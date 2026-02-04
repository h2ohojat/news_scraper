from abc import ABC, abstractmethod
from typing import List
from models.news import News


class NewsSource(ABC):
    """
    Base abstract class for all news sources
    """

    @abstractmethod
    def fetch(self) -> List[News]:
        """
        Fetch news from the source

        Returns:
            List[News]: A list of news items
        """
        pass