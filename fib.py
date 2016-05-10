#!/usr/bin/python
import sys
import collections



def memoize(f):
	class memdict(dict):
		def __missing__(self, key):
			x = f(key)
			self[key] = x
			return x
	d = memdict()
	return d.__getitem__

@memoize
def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)

def iterfib(n):
	if n < 2:
		return 1
	a = 1
	b = 1
	for i in range(2, n+1):
		tmp = b
		b = a + b
		a = tmp
	return b
		
fn = iterfib
# test function
if len(sys.argv) == 3 and sys.argv[2] == 'test':
	for i in range(int(sys.argv[1])):
		a = fib(i)
		b = fn(i)
		print("%d - %d : %s" % (a, b, a == b))
else:
	print(fn(int(sys.argv[1])))
