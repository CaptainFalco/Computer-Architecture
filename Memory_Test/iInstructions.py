i_type_map = {
    'ADDI': 0b100001,
    'SUBI': 0b100010,
    'ANDI': 0b100011,
    'ORI': 0b100100,
    0b100101: read_word,
    'LB': 0b100110,
    0b100111: write_word,
    'SB': 0b101000,
    'BEQ': 0b101001,
    'BNE': 0b101010,
    'BGT': 0b101011,
    'BGE': 0b101100,
    'BLT': 0b101101,
    'BLE': 0b101110
}

def read_word(address, memory, cache):
    """
    Read from Memory
    """
    cache_block = cache.read(address)

    if cache_block:
        global hits
        hits += 1
    else:
        block = memory.get_block(address)
        victim_info = cache.load(address, block)
        cache_block = cache.read(address)

        global misses
        misses += 1

        if victim_info:
            memory.set_block(victim_info[0], victim_info[1])

    return cache_block[cache.get_offset(address)]

def write_word(address, byte, memory, cache):
    """
    Write to the cache
    """
    written = cache.write(address, byte)

    if written:
        global hits
        hits += 1
    else:
        global misses
        misses += 1

    block = memory.get_block(address)
    block[cache.get_offset(address)] = byte
    memory.set_block(address, block)

