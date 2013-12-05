import time

def leftRiemann(f,a,n,h):
		
	t = sum((f(i * h + a)) for i in xrange(n))

	t *= h

	return t
	
	
def rightRiemann(f,a,n,h):
	
	t = sum((f(i * h + a)) for i in xrange(1, n + 1))

	t *= h
	
	return t

def middleRiemann(f,a,n,h):

	add = h * 0.5 + a

	t = sum((f(i * h + add)) for i in xrange(n))

	t *= h

	return t

def trapezoidRiemann(f,a,b,n,h):
	
	s = f(a) + f(b)
	
	t = sum((f(i * h + a)) for i in xrange(1, n))
	t *= 2.0
	t += s

	t *= (h * 0.5)

	return t


f = lambda x:3*x**3-5*x

a = 0.0
b = 100.0
n = 2000
h = (b - a) / float(n)

start = time.time()

left = leftRiemann(f, a, n, h)
right = rightRiemann(f, a, n, h)
middle = middleRiemann(f, a, n, h)
trap = trapezoidRiemann(f, a, b, n, h)

print "Total calculation time: ", time.time() - start
print "Left value:",left    , "Right:",right    , "Middle:",middle    , "Trapezoidal",trap