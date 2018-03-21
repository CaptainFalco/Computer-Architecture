class Memory:
   """
   Class representing main memory as an array
   """

   def _init_(self, size, block_size):
      self.size = size
      self.block_size = block_size
      self.data = None

   def get_block(self, address):
      """
      Get a block of memory that contains the byte address
      """
      start = address - (address % self.block_size)
      end = start + self.block_size

      if start < 0 or start > self.size:
         raise IndexError

      return self.data[start:end]

   def set_block(self, address, data):
      """
      Set a block of memory that contains the byte address with data
      """
      start = address - (address % self.block_size)
      end = start + self.block_size

      if start < 0 or start > self.size:
         raise IndexError

      self.data[start:end] = data
