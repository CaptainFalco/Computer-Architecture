def read_word(address, reg, memory, cache, registers):
    """
    Read from Memory
    """
    cadd = int(address, 2) % 10
    data = memory.get_block(int(address,2))
    if cache[cadd].modified == 0:
        cache[cadd].write(data)
    registers[int(reg,2)].set_block(0, data)

def write_word(address, reg, memory, registers):
    """
    Write to Memory
    """
    data = registers[int(reg,2)].get_block(0)
    memory.set_block(int(address,2), data)

i_type_map = {
    'ADDI': 0b100001,
    'SUBI': 0b100010,
    'ANDI': 0b100011,
    'ORI': 0b100100,
    'LW': '0b100101',
    'LB': 0b100110,
    'SW': 0b100111,
    'SB': 0b101000,
    'BEQ': 0b101001,
    'BNE': 0b101010,
    'BGT': 0b101011,
    'BGE': 0b101100,
    'BLT': 0b101101,
    'BLE': 0b101110
}
