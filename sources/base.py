from abc import ABC, abstractmethod
from typing import List, Dict


class NewsSource(ABC):
    """
    Base abstract class for all news sources
    Each news source must implement the fetch method
    """

    @abstractmethod
    def fetch(self) -> List[Dict]:
        """
        Fetch news from the source

        Returns:
            List[Dict]: A list of news items
        """
        pass