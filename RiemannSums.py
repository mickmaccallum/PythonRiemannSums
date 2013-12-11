import time

def left_riemann(f,a,n,h):
	return sum((f(i * h + a)) for i in xrange(n)) * h
	
	
def right_riemann(f,a,n,h):
	
	return sum((f(i * h + a)) for i in xrange(1, n + 1)) * h

def middle_riemann(f,a,n,h):

	add = h * 0.5 + a

	return sum((f(i * h + add)) for i in xrange(n)) * h

def trapezoid_riemann(f,a,b,n,h):
	
	s = f(a) + f(b)
	
	t = sum((f(i * h + a)) for i in xrange(1, n))
	t *= 2.0
	t += s

	t *= (h * 0.5)

	return t


f = lambda x:5*x

a = -3.0
b = 100.0
n = 20000
h = (b - a) / float(n)

start = time.time()

left = left_riemann(f, a, n, h)
right = right_riemann(f, a, n, h)
middle = middle_riemann(f, a, n, h)
trap = trapezoid_riemann(f, a, b, n, h)


print "Total calculation time: ", time.time() - start
print "Left value:",left    , "Right:",right    , "Middle:",middle    , "Trapezoidal",trap