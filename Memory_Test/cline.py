class Cline:
    """
    Represents a line in the cache.
    """

    def _init_(self, size):
        self.use = 0
        self.modified = 0
        self.valid = 0
        self.tag = 0
        self.data = [0] * size
