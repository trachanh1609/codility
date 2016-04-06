# https://codility.com/demo/results/demoH8ZG25-YQZ/

def solution(N):
	i = 1
	A = 1
	while i * i <= N:
		if N % i == 0:
			A = i
		i += 1
	B = N/A
	P = (A + B) *2
	return P