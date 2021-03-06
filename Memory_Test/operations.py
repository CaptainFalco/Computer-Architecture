from iInstructions import *
from rInstructions import *
from jInstructions import *

class Operations:
    """
    Hold's the different instruction operations
    """

    def operationName(self, opcode):
        if opcode == 0b000000:
            return("R-Type Instruction")
        elif opcode == 0b000010:
            return("J-Type Instruction")
        elif opcode == 0b000011:
            return("J-Type Instruction")
        else:
            return("I-Type Instruction")

    def functionName(opcode, function, instruction, memory, cache, registers):
        if opcode == '0b000000':
            if function == '0b000001':
                return "ADD"
            elif function == '0b000010':
                return "SUB"
            elif function == '0b000011':
                return "MUL"
            elif function == '0b000100':
                return "DIV"
            elif function == '0b000101':
                return "AND"
            elif function == '0b000110':
                return "NOR"
            elif function == '0b000111':
                return "OR"
            elif function == '0b001000':
                return "XOR"
            elif function == '0b001001':
                return "MVHI"
            elif function == '0b001010':
                return "MVLO"
            elif function == '0b001011':
                return "SLL"
            elif function == '0b001100':
                return "SRL"
            elif function == '0b001101':
                return "SLA"
            elif function == '0b001110':
                return "SRA"
            elif function == '0b001111':
                return "JR"
        elif opcode == '0b000010' or opcode == '0b000011':
            if function == '0b000010':
                return "J"
            elif function == '0b000011':
                return "JAL"
        else:
            if function == '0b100001':
                return "ADDI"
            elif function == '0b100010':
                return "SUBI"
            elif function == '0b100011':
                return "ANDI"
            elif function == '0b100100':
                return "ORI"
            elif function == '0b100101':
                print('func')
                read_word(instruction[-1], instruction[1], memory, cache, registers)
            elif function == '0b100110':
                return "LB"
            elif function == '0b100111':
                write_word(instruction[-1], instruction[1], memory, registers)
            elif function == '0b101000':
                return "SB"
            elif function == '0b101001':
                return "BEQ"
            elif function == '0b101010':
                return "BNE"
            elif function == '0b101011':
                return "BGT"
            elif function == '0b101100':
                return "BGE"
            elif function == '0b101101':
                return "BLT"
            elif function == '0b101110':
                return "BLE"


    def runOperation(self, opcode):
        if opcode == 0000000:
            print(opcode)

"""opcoded = 0b000000
functioned = 0b000001

blah = operations()
print(blah.operationName(opcoded))
print(blah.functionName(opcoded,functioned))"""
