# https://codility.com/demo/results/demo7H774W-CPE/

def solution(A , B):
	Z = len(A)
	count = 0

	for i in xrange(Z):
		X = A[i]
		Y = B[i]
		G = gcd(X,Y)
		L = (X * Y)/G
		D = L / G
		j = 2
		E = 1
		toggle = False
		while D >= j :
			while D % j == 0:
				toggle = True
				D /= j
				print "D = " , D
			if toggle:
				E *= j
			j += 1
			toggle = False
		print "E = " , E
		if X % E == 0 and Y % E == 0:
			count +=1
	
	return count

def PrimeList(N):
	P_List = range(2, N+1)
	i = 2
	while (i*i <= N):
		if ( P_List.count(i) != 0 ):
			k = i * i
			while ( k <= N ):
				if P_List.count(k) != 0:
					P_List.remove(k)
				k += i
		i += 1
	return P_List
	
def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)