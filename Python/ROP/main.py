#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
import sys
import argparse
import os.path


# read in an elf and display it in a hexdump format.
def read_elf(filename):
    with open(filename, "rb") as f:
        n = 0 # counter 
        b = f.read(16) # read 16 bytes at a time. 

        while b:
            s1 = " ".join([f"{i:02x}" for i in b])
            s1 = s1[0:23] + " " + s1[23:]
            width = 48

            s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b])

            print(f"{n * 16:08x}   {s1:<{width}}  |{s2}|")

            n += 1
            b = f.read(16)



if __name__ == "__main__":
    #main
    filename = "ret2win"
    read_elf(filename)
