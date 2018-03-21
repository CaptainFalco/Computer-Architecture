class operations:
    """
    Hold's the different instruction operations
    """


    def operationName(self, opcode):
        if opcode == "000001":
            return "ADD"
        elif opcode == "000010":
            return "SUB"
        elif opcode == "000011":
            return "MUL"
        elif opcode == "000100":
            return "DIV"
        elif opcode == "000101":
            return "AND"
        elif opcode == "000110":
            return "NOR"
        elif opcode == "000111":
            return "OR"
        elif opcode == "001000":
            return "XOR"
        elif opcode == "001001":
            return "MVHI"
        elif opcode == "001010":
            return "MVLO"
        elif opcode == "001011":
            return "SLL"
        elif opcode == "001100":
            return "SRL"
        elif opcode == "001101":
            return "SLA"
        elif opcode == "001110":
            return "SRA"
        elif opcode == "001111":
            return "JR"
        elif opcode == "100001":
            return "ADDI"
        elif opcode == "100010":
            return "SUBI"
        elif opcode == "100011":
            return "ANDI"
        elif opcode == "100100":
            return "ORI"
        elif opcode == "100101":
            return "LW"
        elif opcode == "100110":
            return "LB"
        elif opcode == "100111":
            return "SW"
        elif opcode == "101000":
            return "SB"
        elif opcode == "101001":
            return "BEQ"
        elif opcode == "101010":
            return "BNE"
        elif opcode == "101011":
            return "BGT"
        elif opcode == "101100":
            return "BGE"
        elif opcode == "101101":
            return "BLT"
        elif opcode == "101110":
            return "BLE"
        elif opcode == "000010":
            return "J"
        elif opcode == "000011":
            return "JAL"
