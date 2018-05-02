from iInstructions import i_type_map
from rInstructions import r_type_map
from jInstructions import j_type_map
from register import reg_map

instruction_list = []
instruction = []

def assemble(self, filename):
    """
    Takes a file and outputs binary instructions.
    """
    ass_file = open(filename, 'r')

    for line in ass_file:
        for word in line:
            if len(word) == 26:
                instruction.append(j_off_to_bin(word))
            elif len(word) == 16:
                instruction.append(imm_to_bin(word))
            elif word in reg_map.keys:
                instruction.append(reg_to_bin(word))
            elif word in r_type_map.keys:
                instruction.append(inst_to_bin(word))
            elif word in i_type_map.keys:
                instruction.append(inst_to_bin(word))
            elif word in j_type_map.keys:
                instruction.append(inst_to_bin(word))
        instruction_list.append(instruction)


def reg_to_bin(reg):
    """
    """
    return format(bin(reg_map[reg]), '#07b')

def inst_to_bin(inst):
    """
    """
    return format(bin(reg_map[reg]), '#08b')

def imm_to_bin(immediate):
    """
    """
    return format(bin(immediate), '#018b')

def j_off_to_bin(offset):
    """
    """
    return format(bin(offset), '#028b')
