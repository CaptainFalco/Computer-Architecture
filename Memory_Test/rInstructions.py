def add(address, mem1, mem2, mem3):
    mem1.set_block(address, mem2.get_block(address) + mem3.get_block(address))

def sub(address, mem1, mem2, mem3):
    mem1.set_block(address, mem2.get_block(address) - mem3.get_block(address))

r_type_map = {
    'ADD': 0b000001,
    'SUB': 0b000010,
    'MUL': 0b000011,
    'DIV': 0b000100,
    'AND': 0b000101,
    'NOR': 0b000110,
    'OR': 0b000111,
    'XOR': 0b001000,
    'MVHI': 0b001001,
    'MVLO': 0b001010,
    'SLL': 0b001011,
    'SRL': 0b001100,
    'SLA': 0b001101,
    'SLR': 0b001110,
    'JR': 0b001111
}

