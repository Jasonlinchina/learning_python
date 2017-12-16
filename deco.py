#!/usr/bin/env python

from time import ctime, sleep

def wrappedFunc(func):
	print '[%s] %s() called' % (ctime(), func.__name__)
	return func

#def foo():
#	pass
#print wrappedFunc(foo)
#print wrappedFunc(foo)
@wrappedFunc
def foo():
	pass

foo()
sleep(4)
foo()

for i in range(2):
	sleep(1)
	foo()
print 'OK'
