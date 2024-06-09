class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @classmethod
    def from_database(cls, author_id):
        # Implement a method to retrieve author details from the database
        pass
