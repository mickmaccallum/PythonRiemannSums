import time

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

def profile_left_summation():

	t1 = 0.0
	t2 = 0.0

	for i in xrange(int(r)):
		s = time.time()
		l = n_left_incrementer(f,a,n,h)
		t1 += time.time() - s

	for i in xrange(int(r)):
		s = time.time()
		l = h_left_incrementer(f,a,b,n,h)
		t2 += time.time() - s

	t1 /= r
	t2 /= r

	with open("ProfilerOutput.txt", "w") as text_file:
    		text_file.write(("n_left_incrementer: %s" % t1) + "\n")
    		text_file.write(("h_left_incrementer: %s" % t2) + "\n")




profile_left_summation()