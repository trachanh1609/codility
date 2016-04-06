# -*- coding: utf-8 -*-

# We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).
# 
# The figure below shows discs drawn for N = 6 and A as follows:
# 
#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0
# 
# 
# There are eleven (unordered) pairs of discs that intersect, namely:
# 
# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:
# 
# def solution(A)
# 
# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
# 
# Given array A shown above, the function should return 11, as explained above.
# 
# Assume that:
# 
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].
# Complexity:
# 
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

def solution(A):
	N = len(A)
	Sum = 0
	for i in xrange(N-1):
		X = A[i]
		if X <= N -1 -i:
			Sum += X
			for j in xrange(i+X+1,N):
				if j-i <= A[i]+A[j]:
					Sum += 1
					print "Sum=", Sum," X=", X, " i=", i, " j=", j
				else:
					pass 
		else:
			for j in xrange(i+1,N):
				if j-i <= A[i]+A[j]:
					Sum += 1
					print "Sum=", Sum," X=", X, " i=", i, " j=", j
				else:
					pass
	if Sum > pow(10,10):
		return -1
	else:
		return Sum
# Correctness 100%, Performance 25%	, O(N**2)



def solution_new(A):
	N = len(A)
	Sum = 0
	# [i] = i + i.left + i.right
	#  i.left (= i if A[i] > i) or (= A[i] else)
	#  i.right (= N-i if A[i] > N-i) or( else: = A[i])
	
	for i in xrange(N):
		if A[i] > i:
			i_left = i
		else:
			i_left = A[i]
			
		if A[i] > N-1-i:
			i_right = N-1-i
		else:
			i_right = A[i]
		
		Sum = Sum + i + i_left + i_right
		print "Sum = " , Sum ," i = ", i , " i_left = " , i_left ," i_right = " , i_right
	
	pairs = N*(N-1)/2
	
	Res = Sum - pairs - N
	return Res
	
	
def solu(A):
	N = len(A)
	C = [None]* N
	S , t = 0 , 0
	for i in xrange(N):
		C[i] = -1
		a = A[i]
		if a>=i:
			C[0] += 1
		else:
			C[i-a] += 1
	print "C = " , C
	
	for i in xrange(N):
		t += C[i]
		C[i] = t
		print "t = " , t
		print "C = " , C
	
	for i in xrange(N):
		a = A[i]
		if a < N-i:
			S += a
		else:
			S += N-i-1
		if i != N-1:
			if a < N-i:
				S += C[i+a]
			else:
				S += C[N-1]
		print "a = " , a, " i = ", i, " S = ", S


	if S > pow(10,10):
		return -1
		
	else:
		return S
# Result O(N) or O(N*logN) , 100% ( from internet)
# Explanation : An Intersect = Rightside < Leftside
# Calculate how many Lefts at each point 0,1,2....
# The Center must be at the right side of that Left.
# As point increases, number of center -= 1
	
	
	
		 
	
	
	
	
	
	
	
	
	
	
	
	




			