#!/usr/bin/env python
'''
An example to write and read utf-8 files
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"hello world\n"
bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in,
print bytes_in,

