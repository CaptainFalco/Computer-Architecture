from cline import Cline

class Cache:
    """
    Class representing the cache.
    """

    # Replacement
    LRU = "LRU"
    LFU = "LFU"
    FIFO = "FIFO"

    # Mapping
    WRITE_BACK = "WB"
    WRITE_THROUGH = "WT"

    def _init_(self, size, mem_size, block_size,
               mapping, replacement, writing):
        self.lines = [Line(block_size) for i in range(size // block_size)]

        self.size = size
        self.mem_size = mem_size
        self.block_size = block_size

        self.mapping = mapping
        self.replacement = replacement
        self.writing = writing

