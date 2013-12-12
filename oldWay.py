import time

def left_sum(f,a,b,n):
	h = (b - a) / n
	i = a
	total = 0.0

	while i <= b:
		total += f(i)
		i += h

	return total * h	

def right_sum(f,a,b,n):
	h = (b - a)
	i = a
	total = 0.0

	while i < b:
		total += f(i)
		i += h
	return total * h


f = lambda x:5*x
