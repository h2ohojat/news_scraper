from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class News:
    title: str
    url: str
    source: str
    published_at: Optional[datetime] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None