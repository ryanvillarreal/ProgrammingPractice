#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# this was my attempt at writing a basic hexdump using Python, but then I found a better solution online that didn't involve
# as much trash code lol 
# I still have a long way to go. 
import os.path
import binascii
from struct import *
from itertools import count
import array
from pwn import *


#global counter using itertools
counter = count()

def read_elf(filename):
    if filename and os.path.exists(filename):
       with open(filename, 'rb') as infile:
          data = ""
          while True:
             data_in = infile.read(1024)
             if not data_in:
                break # we have reached the end...
             data += data_in

          print len(data)
          print "done reading..."
          return data


def parse(data):
     print "parsing"
     # using globals in order to allow for quick modifications
     BLOCK_SIZE = 4
     ROW_SIZE = 0
     MAX_ROW = 8
     hex_str = ""
     hex_line = ""

     # need to handle little endianness
     for i in data:
        if len(i) > 1:
            print "wtf" # should always be 1... 
        # i - <type 'str'>
	if ROW_SIZE < MAX_ROW:
           # binascii.hexlify(i) - <type 'str'>
	   #hex_str += binascii.hexlify(i)
           hex_str = hex_str + binascii.b2a_hex(i)
	   if len(hex_str) % 16 == 0: # join individual bytes to get 4 byte output - DWORD?
               # hex_str - <type 'str'>
               print hex_str
               #print '0x%x' % unpack('<Q', hex_str)[0]
               #print unpack('<Q', hex_str)
               #print binascii.unhexlify(hex_str)
               #hex_line += hex_str + " " # just for easier printing format
               # four byte hex - <type 'str'> - need 4 bytes for unpack
               #print hex_line
               #print " "
               ROW_SIZE += 1
               hex_str = ""
        else:
                #print str(next(counter)) +" - "+ hex_line # print the line with a counter, and 16 bytes of data similar to hexdump
                hex_line = ""
                ROW_SIZE = 0


if __name__ == "__main__":
    # uncomment after finished debugging
    #filename = raw_input("What file would you like to open: ")
    filename = "ret2win"
    data = read_elf(filename)

    if len(data) > 0:
        print "Data length returned is: %i " % len(data)
        parse(data)
    else:
        print "File has no data found" 
