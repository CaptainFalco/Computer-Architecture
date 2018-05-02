class Cline:
    """
    Represents a line in the cache.
    """

    def __init__(self, size):
        self.use = 0
        self.modified = 0
        self.valid = 0
        self.tag = 0
        self.size = size
        self.data = [0] * size

    def read(self):
        """
        read from the cache line
        """
        return self.data

    def write(self, new_data):
        """
        write to the cache line
        """
        if new_data > self.size:
            raise IndexError
        self.modified = 1
        self.data[0] = new_data
