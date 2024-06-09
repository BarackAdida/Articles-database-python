from database.connection import db

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    def article_titles(self):
        query = """
        SELECT title FROM Article WHERE magazine_id = :magazine_id
        """
        with db.connect() as conn:
            result = conn.execute(query, magazine_id=self.id)
            titles = [row[0] for row in result.fetchall()]
            return titles

    def contributing_authors(self):
        query = """
        SELECT a.name
        FROM Author a
        JOIN (
            SELECT author_id, COUNT(*) as article_count
            FROM Article
            WHERE magazine_id = :magazine_id
            GROUP BY author_id
            HAVING COUNT(*) > 2
        ) AS ac ON a.id = ac.author_id
        """
        with db.connect() as conn:
            result = conn.execute(query, magazine_id=self.id)
            authors = [row[0] for row in result.fetchall()]
            return authors
