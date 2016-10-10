def func(*args):
	x=1
	y=[x**x for x in args]
	return y
print func(1,2,3,4,5)