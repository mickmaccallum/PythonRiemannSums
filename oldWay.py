import time

def leftSum(f,a,b,n):
	h = (b - a) / n
	print h
	i = a
	total = 0.0

	while i <= (b - h):
		total += f(i)
		i += h

	return total * h	


f = lambda x:5*x

start = time.time()

left = leftSum(f,-3.0,100.0,20000.0)

print time.time() - start

print left