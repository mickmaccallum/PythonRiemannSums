from time import time
from multiprocessing import Process


def left_riemann(f,a,n,h):
	t = sum((f(i * h + a)) for i in xrange(n)) * h
	print 'Left:' + str(t)
	return t
	
	
def right_riemann(f,a,n,h):
	t = sum((f(i * h + a)) for i in xrange(1, n + 1)) * h
	print 'Right: ' + str(t)
	return t

def middle_riemann(f,a,n,h):

	add = h * 0.5 + a

	t = sum((f(i * h + add)) for i in xrange(n)) * h
	print 'Middle: ' + str(t)
	return t

def trapezoid_riemann(f,a,b,n,h):
	
	s = f(a) + f(b)
	
	t = sum((f(i * h + a)) for i in xrange(1, n))
	t *= 2.0
	t += s

	t *= (h * 0.5)
	print 'Trapezoidal: ' + str(t)
	return t


f = lambda x:5*x

a = -3.0
b = 100.0
n = 20000
h = (b - a) / float(n)

start = time()
    

leftProcess = Process(target=left_riemann,args=(f,a,n,h))
leftProcess.start()

rightProcess = Process(target=right_riemann,args=(f,a,n,h))
rightProcess.start()

middleProcess = Process(target=middle_riemann,args=(f,a,n,h))
middleProcess.start()

trapProcess = Process(target=trapezoid_riemann,args=(f,a,b,n,h))
trapProcess.start()



# left = left_riemann(f, a, n, h)
# right = right_riemann(f, a, n, h)
# middle = middle_riemann(f, a, n, h)
# trap = trapezoid_riemann(f, a, b, n, h)


# print "Total calculation time: ", time() - start
# print "Left value:",left    , "Right:",right    , "Middle:",middle    , "Trapezoidal",trap