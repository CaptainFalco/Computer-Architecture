#!/usr/bin/python

# Open our instructions.txt file to read and obtain our instructions
import sys

file_name = "instructions.txt"

try:
   file = open(file_name, "r")     # open file stream
except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()

file_text = file.read()            # read text from the file
file.close()                       # close the file
print ("File text is: ", file_text)                  # print contents
# Instructions obtained as a string object

# Separate the commands.
file_length = len(file_text)       # number of bits
num_instr = file_length / 32       # 32 bits per instruction
print("Number of instructions: ", (num_instr))                   # print how many instructions we have in the txt file
opcode_array = []                  # store our opcode instructions (size is based on number of instructions in file)
index = 0                          # for the loop

while index < num_instr:
    opcode_array.append(file_text[index*32: index*32+6])
    print("Instruction: ", index , "is: ", opcode_array[index])
    index = index + 1

# So, each instruction's opcode is the first 6 bits of the instruction
# the file_text statement in the for loop finds the indeces of where each should be given the current instruction number

