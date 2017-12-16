#!/usr/bin/env python

from random import choice

class RandSeq(object):
	def __init__(self, seq):
		self.data = seq

	def __str__(self):
		return '%s' % self.data

	def __iter__(self):
		return self

	def next(self):
		return choice(self.data)

a = RandSeq('acdfe')
b = a.__iter__()
print a, b

