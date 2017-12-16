#!/usr/bin/env python


from random import randint
'''
def odd(n):
	return n % 2

allNums = []
for eachNum in range(9):
	allNums.append(randint(1,99))
print filter(odd, allNums)


allNums = []
for eachNum in range(9):
	allNums.append(randint(1, 99))
print [n for n in allNums if n%2]
'''
print [n for n in [randint(1, 99) for i in range(9)] if n % 2]
