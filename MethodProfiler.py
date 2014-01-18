from time import time
from math import fabs, sin
import cProfile

a = 7.0
b = 100.0
n = 700

h = (b - a) / float(n)

f = lambda x:(5*x**3)+(2*x)

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


def h_trapezoid_incrementer(f,a,n,b,h):
	
	total = f(a) + f(b)

	i = a

	c = 1
	while i <= b - h:
		total += 2.0 * f(a + (c * h))
		i += h
		c += 1

	return total * (h / 2.0)



def startProfiling():
	# print '%e' % n_left_incrementer(f,a,n,h)
	# print '%e' % h_left_incrementer(f,a,b,n,h)
	
	# print '%e' % n_right_incrementer(f,a,n,h)
	# print '%e' % h_right_incrementer(f,a,b,n,h)

	# print '%e' % n_middle_incrementer(f,a,n,h)
	# print '%e' % h_middle_incrementer(f,a,b,n,h)

	# print '%e' % n_trapezoid_incrementer(f,a,n,h)
 	# print '%e' % h_trapezoid_incrementer(f,a,n,b,h)

	print n_left_incrementer(f,a,n,h)
	print h_left_incrementer(f,a,b,n,h)
	
	print n_right_incrementer(f,a,n,h)
	print h_right_incrementer(f,a,b,n,h)

	print n_middle_incrementer(f,a,n,h)
	print h_middle_incrementer(f,a,b,n,h)

	print n_trapezoid_incrementer(f,a,n,h)
 	print h_trapezoid_incrementer(f,a,n,b,h)

# cProfile.run('startProfiling()')
startProfiling()