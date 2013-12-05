import time
import parser
import math

def leftRiemann(f,a,n,h):
		
	sum = 0.0	
	
	for i in range(int(n)):
		x = a + i * h
		sum += f(x)
		
	sum *= h

	return sum
	
	
def rightRiemann(f,a,n,h):
	
	sum = 0.0	

	for i in xrange(1,int(n)+1):
		x = a + i * h
		sum += f(x)
	sum *= h
	
	return sum

def middleRiemann(f,a,n,h):

	sum = 0.0
	add = h / 2.0 + a

	for i in xrange(int(n)):
		x = i * h + add
		sum += f(x)
	sum *= h

	return sum

def trapezoidRieman(f,a,b,n,h):
	
	sum = f(a) + f(b)

	for i in xrange(1,int(n)):
		x = i * h + a
		sum += (f(x) * 2.0)
	sum *= (h * 0.5)

	return sum



# formula = "5*x**5+12*x**3"
# code = parser.expr(formula).compile()

# x = 10
# print eval(code)

print "Open throttle"

f = lambda x:((x)**4)-(5*(x)**2)

a = -8.0
b = 17.0
n = 20000.0
h = (b-a)/n

start = time.time()

print "Left Sum:", leftRiemann(f, a, n, h)
print "Right Sum:", rightRiemann(f, a, n, h)
print "Middle Sum:", middleRiemann(f, a, n, h)
print "Trapezoidal Sum:", trapezoidRieman(f, a, b, n, h)

print "Time taken to calculate: ", time.time() - start









