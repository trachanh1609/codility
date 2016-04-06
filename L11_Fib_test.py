# L11_ Ladder
# https://codility.com/demo/results/demoZ4DAZK-FWH/

def fibonacciDynamic(n):
	fib = [0] * (n + 2)
	fib[1] = 1
	for i in xrange(2, n + 1):
		fib[i] = fib[i - 1] + fib[i - 2]
	return fib
	
def fibonacciMax(N):
	fib = [0,1]
	i = 1
	while fib[i] < N :
		fib_next = fib[i - 1] + fib[i]
		fib.append(fib_next)
		i += 1
	return fib
	
	
def fibArray(N):
	fib = [False] * (N +2)
	fib[0] = True
	fib[1] = True
	fib[2] = True
	i = 1
	j = 2
	k = 3
	while k < (N+2):
		fib[k] = True
		i = j
		j = k
		k = i + j
	return fib