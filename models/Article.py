class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def from_database(cls, article_id):
        # Implement a method to retrieve article details from the database
        pass
