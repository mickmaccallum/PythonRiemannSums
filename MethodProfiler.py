from time import time
from math import fabs

r = 100.0

a = -3.0
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

def n_right_incrementer():
	return sum((f(i * h + a)) for i in xrange(1, n + 1)) * h

def h_right_incrementer():
	


def profile_left_summation():




# profile_left_summation()