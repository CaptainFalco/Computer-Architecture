from iInstructions import i_type_map
from rInstructions import r_type_map
from jInstructions import j_type_map
from register import reg_map

instruction_list = []
instruction = []

def assemble(filename):
    """
    Takes a file and outputs binary instructions.
    """
    try:
        ass_file = open(filename, 'r')
    except IOError:
        print ("There was an error reading ", file_name)
        sys.exit()

    for line in ass_file:
        for word in line.split():
            print(word)
            if word in reg_map.keys():
                instruction.append(reg_to_bin(word))
            elif word in r_type_map.keys():
                instruction.append(r_inst_to_bin(word))
            elif word in i_type_map.keys():
                instruction.append(i_inst_to_bin(word))
            elif word in j_type_map.keys():
                instruction.append(j_inst_to_bin(word))
            else:
                if line.split()[0] in i_type_map.keys():
                    instruction.append(imm_to_bin(word))
                elif line.split[0] in j_type_map.keys():
                    instruction.append(j_off_to_bin(word))
        instruction_list.append(instruction)

    ass_file.close()
    return instruction_list

def reg_to_bin(reg):
    """
    """
    return'{:#07b}'.format(reg_map[reg])

def r_inst_to_bin(inst):
    """
    """
    return'{:#08b}'.format(r_type_map[inst])
def i_inst_to_bin(inst):
    """
    """
    return i_type_map[inst]

def j_inst_to_bin(inst):
    """
    """
    return'{:#08b}'.format(j_type_map[inst])

def imm_to_bin(immediate):
    """
    """
    return'{:#018b}'.format(int(immediate))

def j_off_to_bin(offset):
    """
    """
    return'{:#028b}'.format(int(offset))
