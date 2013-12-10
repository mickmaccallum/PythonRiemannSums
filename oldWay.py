import time

def left_sum(f,a,b,n):
	h = (b - a) / n
	i = a
	total = 0.0

	while i <= b:
		total += f(i)
		i += h

	return total * h	

def right_sum():
	h = (b - a)
	i = a
	total = 0.0

	while i < b:
		total += f(in)
		i += h
	return total * h


f = lambda x:5*x



total = 0.0

for i in xrange(10000):
	start = time.time()
	left = right_sum(f,-3.0,100.0,20000.0)
	total += (time.time() - start)

total /= 10.0

print("%.15f") % (total)
