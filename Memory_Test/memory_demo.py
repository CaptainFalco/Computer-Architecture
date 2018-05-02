from rInstructions import r_type_map
from iInstructions import i_type_map
from jInstructions import j_type_map

from register import *
from memory import Memory
from cline import Cline
from operations import Operations as op


cycle = 0

main_memory = Memory(32*100,32)
cache = [Cline(32) for i in range(0,9)]
registers = [Memory(32,32) for i in range(0,31)]
for x in range(0,99):
    main_memory.set_block(x, str(bin(x))[2:])

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

        if inst[0] in r_type_map.values():
            op.functionName(inst[0], inst[-1], inst)
        elif inst[0] in i_type_map.values():
            op.functionName(inst[0], inst[0], inst)
        elif inst[0] in j_type_map.values():
            op.functionName(inst[0], inst[0], inst)

        pc += 1
        if run_type is runs['step']:
            break
