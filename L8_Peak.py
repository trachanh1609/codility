# https://codility.com/demo/results/demoXVH3X3-F34/

def solution(A):
	N = len(A)
	Peak = [0] * N
	Divisor = []
	for i in xrange(1, N-1):
		if A[i] > A[i-1] and A[i] > A[i+1]:
			Peak[i] = 1
		if N % i == 0:
			Divisor.append(i)
	Divisor.append(N)
	print "Peak = " , Peak
	print "Divisor=", Divisor
	max_block = 0
	
	for K in Divisor:
		j = 0
		while (j*K < N):
			sum_A = sum(Peak[(j*K):(j+1)*K])
			print "Peak jk =" , Peak[(j*K):(j+1)*K]
			print "K=", K , " j=", j, " sum_A = " , sum_A
			if sum_A == 0:
				j += 1
				break
			elif sum_A > 0 and (j+1)*K == N:
				max_block = j + 1
				return max_block
			j += 1
	
	return max_block