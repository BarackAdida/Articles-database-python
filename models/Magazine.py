class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @classmethod
    def from_database(cls, magazine_id):
        # Implement a method to retrieve magazine details from the database
        pass
