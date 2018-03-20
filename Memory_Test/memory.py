#!/usr/bin/python

import sys

file_name = "instructions.txt"

try:
   # open file stream
   file = open(file_name, "r")
except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()

file_text = file.read()
file.close();
print (file_text)
