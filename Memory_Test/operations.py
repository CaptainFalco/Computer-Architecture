opcode_map = {
    'r': "000000",
    'i': "100000",
    'j': "000010"
}

j_type_map = {
    'J': 0b000010,
    'JAL': 0b000011
}


class operations:
    """
    Hold's the different instruction operations
    """

    def operationName(self, opcode):
        return("Test")
