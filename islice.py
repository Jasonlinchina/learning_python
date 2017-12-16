#!/usr/bin/env python

from itertools import islice

input = open('test', 'r')
count = -1
for count, line in enumerate(open('test', 'rU')):
	count +=1

print input.readlines()[1],
for i in input.readlines()[1:count]:
	print i.strip("\n")

'''
dict = {'abc':1, 'def': 2}
keys = dict.keys()

for i in keys:
	print i
'''
