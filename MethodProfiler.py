from time import time
from math import fabs
import cProfile

a = 3.0
b = 100.0
n = 20000

h = (b - a) / float(n)

f = lambda x:5*x

def n_left_incrementer(f,a,n,h):
	return sum((f(i * h + a)) for i in xrange(n)) * h

def h_left_incrementer(f,a,b,n,h):
	i = a
	total = 0.0

	while i <= b:
		total += f(i)
		i += h

	return total * h	

def n_right_incrementer(f,a,n,h):
	return sum((f(i * h + a)) for i in xrange(1, n + 1)) * h

def h_right_incrementer(f,a,b,n,h):
	i = a + h
	g = b + h

	total = 0.0

	while i <= g:
		total += f(i)
		i += h
	return total * h

def n_middle_incrementer(f,a,n,h):
	add = h * 0.5 + a
	return sum((f(i * h + add)) for i in xrange(n)) * h

def h_middle_incrementer(f,a,b,n,h):
	q = h / 2.0
	i = a + q

	total = 0.0

	while i <= b:
		total += f(i)
		i += h

	return total * h
		

def n_trapezoid_incrementer(f,a,n,h):
	s = f(a) + f(b)
	
	t = sum((f(i * h + a)) for i in xrange(1, n))
	t *= 2.0
	t += s

	t *= (h * 0.5)

	return t


def h_trapezoid_incrementer(f,a,b,n,h):
	
	total = f(a) + f(b)

	i = a

	while i <= b:
		total += 2.0 * f(a + (i * h))
		i += h

	return total * (h / 2.0)


def startProfiling():
	print n_left_incrementer(f,a,n,h)
	print h_left_incrementer(f,a,b,n,h)
	
	print n_right_incrementer(f,a,n,h)
	print h_right_incrementer(f,a,b,n,h)

	print n_middle_incrementer(f,a,n,h)
	print h_middle_incrementer(f,a,b,n,h)

	print n_trapezoid_incrementer(f,a,n,h)
 	print h_trapezoid_incrementer(f,a,b,n,h)

cProfile.run('startProfiling()')