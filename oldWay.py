import time

def leftSum(f,a,b,n):
	h = (b - a) / n
	i = a
	total = 0.0

	while i <= b:
		total += f(i)
		i += h

	return total * h	


f = lambda x:5*x



total = 0.0

for i in xrange(10):
	start = time.time()
	left = leftSum(f,-3.0,100.0,20000.0)
	total += (time.time() - start)

total /= 10.0

print("%.15f") % (total)
