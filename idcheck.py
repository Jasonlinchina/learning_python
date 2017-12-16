#!/usr/bin/env python

import string
from keyword import kwlist
import sys

alphas = string.letters + '_'
nums = string.digits

myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be
			alphabetic'''
	elif myInput in kwlist:
			print "this is a keyword"
			sys.exit()
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print '''invalid: remaining
					symbols must be alphanumeric'''
				break
			else:
				print "okay as an indentifier"
elif len(myInput) == 1:
	if myInput[0] not in alphas:
		print "a invalid single character indentifier"
	else:
		print "a valid single character indentifier"
else:
	print "this is a empty character"
