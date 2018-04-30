def read_word(address, reg, memory, cache, registers):
    """
    Read from Memory
    """
    cadd = address % 10
    if cache[cadd].modified == 0:
        data = memory.get_block(address)
        cache[cadd].write(data)


def write_word(address, byte, memory):
    """
    Write to Memory
    """
    memory.set_block(address, byte)

i_type_map = {
    'ADDI': 0b100001,
    'SUBI': 0b100010,
    'ANDI': 0b100011,
    'ORI': 0b100100,
    'RW': 0b100101,
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
