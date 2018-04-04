from rInstructions import *
from iInstructions import *
from operations import *

from register import *
from memory import Memory
from cache import Cache

cycle = 0
main_memory = Memory(32*100,32)
cache = Cache(32, 32*10, 32)
registers = [Memory(32,32) for i in range(0,35)]
registers[reg_map['r0']].set_block(0,[0])
registers[reg_map['pc']].set_block(0,[0])

runs = {
    'step': 0,
    'full': 1
}

def run(instructions, run_type):
    """
    """

    for inst in instructions:
        inst = instructions[registers[reg_map['pc']].get_block(0)]
        if inst is opcode_map['r']:
            r_type_map[inst]()
        if inst is opcode_map['i']:
            i_type_map[inst]()
        if inst is opcode_map['j']:
            break
        if run_type is runs['step']:
            break

