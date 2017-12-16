#!/usr/bin/env python 

f = open('go')
flist = f.readlines()

for i in flist:
	if not i.strip():
		break
else:
	print i
