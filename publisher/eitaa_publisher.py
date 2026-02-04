from models.news import News


class EitaaPublisher:
    """
    Prepare news items for publishing on Eitaa (MVP)
    """

    def format_message(self, news: News) -> dict:
        """
        Convert News object to Eitaa-ready message structure
        (UI & Eitaa Mini App friendly)
        """

        return {
            "title": news.title,
            "summary": news.summary,
            "image": news.image_url,
            "source": news.source,
            "url": news.url
        }