class Memory:
   """
   Class representing main memory as an array
   """

   def __init__(self, size, block_size):
      self.size = size
      self.block_size = block_size
      self.data = [0 for i in range(size)]

   def get_block(self, address):
      """
      Get a block of memory that contains the byte address
      """
      start = address * self.block_size
      end = start + self.block_size

      if start < 0 or end > self.size:
         raise IndexError

      return self.data[start:end]

   def set_block(self, address, new_data):
      """
      Set a block of memory that contains the byte address with data
      """
      start = address * self.block_size
      end = start + self.block_size - 1

      if start < 0 or end > self.size:
         raise IndexError

      clear = [0] * self.block_size
      self.data[start:end] = clear

      start += (self.block_size - len(new_data))
      self.data[start:end] = new_data
