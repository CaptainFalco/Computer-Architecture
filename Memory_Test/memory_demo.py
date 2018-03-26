from register import *
from memory import Memory
from cache import Cache

def func_read():
    """"""
def func_write():
    """"""

registers = [Memory(32,8) for i in range(0,35)]
registers[reg_map['r0']].set_block(0, 0)
