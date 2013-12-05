import time

def leftRiemann(f,a,n,h):
		
	sum = 0.0	
	
	for i in xrange(n):
		x = a + i * h
		sum += f(x)
		
	sum *= h

	return sum
	
	
def rightRiemann(f,a,n,h):
	
	sum = 0.0	

	for i in xrange(1, n + 1):
		x = a + i * h
		sum += f(x)
	sum *= h
	
	return sum

def middleRiemann(f,a,n,h):

	sum = 0.0
	add = h * 0.5 + a

	for i in xrange(n):
		x = i * h + add
		sum += f(x)
	sum *= h

	return sum

def trapezoidRiemann(f,a,b,n,h):
	
	sum = f(a) + f(b)

	for i in xrange(1, n):
		x = i * h + a
		sum += (f(x) * 2.0)
	sum *= (h * 0.5)

	return sum

f = lambda x:5*x

a = 0.0
b = 100.0
n = 20000
h = (b - a) / float(n)

start = time.time()

left = leftRiemann(f, a, n, h)
right = rightRiemann(f, a, n, h)
middle = middleRiemann(f, a, n, h)
trap = trapezoidRiemann(f, a, b, n, h)

print "Total calculation time: ", time.time() - start
print "Left value:", left, "Right: ", right, "Middle: ", middle, "Trapezoidal", trap