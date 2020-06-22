#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os.path
from os import path
import binascii
from capstone import *
from struct import *

def read_elf(filename):
    if not path.exists(filename):
        print "File does not exist"
        return 0

    with open(filename, 'rb') as infile:
        data = ""
        while True:
            data_in = infile.read(1024)
            if not data_in:
                break # we have reached the end...
            data += data_in
        print "done reading..."
        return data

def parse(data):
#    md = Cs(CS_ARCH_X86, CS_MODE_64)
#    print "parsing" 
#    for i in md.disasm(data_hex, 0x0000):
#        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))


if __name__ == "__main__":
    filename = raw_input("What file would you like to open: ")
    data = read_elf(filename)
    if len(data) > 0:
        print "Data length returned is: %i " % len(data)
        parse(data)
    else:
        print "File has no data found" 
