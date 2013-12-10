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
	

def run_profiler_loops_1():
	t1 = 0.0
	for i in xrange(int(r)):
		s = time()
		l = n_left_incrementer(f,a,n,h)
		t1 += time() - s
	return t1

def run_profiler_loops_2():
	t2 = 0.0
	for i in xrange(int(r)):
		s = time()
		l = h_left_incrementer(f,a,b,n,h)
		t2 += time() - s
	return t2
	

def profile_left_summation():

	t1 = run_profiler_loops_1()
	t2 = run_profiler_loops_2()

	t1 /= r
	t2 /= r

	line = "\n"

	txt = open("ProfilerOutput.txt", "w")

	print >> txt, time()
	print >> txt, "Left Sum Times" + line
	print >> txt, ("n_left_incrementer: %s" % t1)
	print >> txt, ("h_left_incrementer: %s" % t2) + line
	print >> txt, ("Difference: %s" % fabs(t1 - t2))

	txt.close()



profile_left_summation()