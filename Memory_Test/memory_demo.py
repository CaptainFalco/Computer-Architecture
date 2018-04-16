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

def run(instructions, run_type, pc):
    """
    """

    for inst in instructions:
        if pc >= len(instructions):
            break

        inst = instructions[pc]
        op = inst[0:5]
        
        reg = inst[6:10]
        val = inst[11:]
        if op is opcode_map['r']:
            r_type_map[op]()
        if op is opcode_map['i']:
            i_type_map[op](val, reg, main_memory, cache, registers)
        if op is opcode_map['j']:
            break
        pc += 1

        #sm.increasePCCounter

        if run_type is runs['step']:
            break
