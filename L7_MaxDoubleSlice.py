# coding: utf-8
# A non-empty zero-indexed array A consisting of N integers is given.
# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
# For example, array A such that:
#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:
# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers, returns the maximal sum of any double slice.
# For example, given:
#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# the function should return 17, because no double slice of array A has a sum of greater than 17.
# Assume that:
# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−10,000..10,000].


# 66% Correctness, 85% performance
# https://codility.com/demo/results/demoX2WEPN-CQB/
def solution(A):
    # write your code in Python 2.7
    max_double = 0
    new_max_double = 0
    max_ending = 0
    min_element = 0
    N = len(A)
    for i in xrange(1,N-1):
        print "Pre i=%d, A[i]=%d, min_element=%d, max_ending=%d, new_max=%d, max_double=%d" % (
            i,A[i],min_element,max_ending,new_max_double,max_double)
        if max_ending < 0 and max(A[i], max_ending + A[i]) == A[i] :
			reset_min_element = 1
        else :
			reset_min_element = 0
        max_ending = max(A[i], max_ending + A[i])
        if max_ending < 0:
        	min_element = 0
        new_max_double = max_ending - min_element
        max_double = max(max_double,new_max_double)
        if reset_min_element == 1:
        	min_element = 0

        else:
        	min_element = min(min_element,A[i])        
        print "Post i=%d, A[i]=%d, min_element=%d, max_ending=%d, new_max=%d, max_double=%d" % (
            i,A[i],min_element,max_ending,new_max_double,max_double)
        print ""
    return max_double
    
    
def solu(A):
	pos_sum = 0
	neg_sum = 0
	Y = A[1]
	max_double = 0
	N = len(A)
	for i in xrange(1, N-1):
		print "Pre i=%d, A[i]=%d, pos_sum=%d, neg_sum=%d, Y=%d, max_double=%d, " % (
            i,A[i],pos_sum,neg_sum,Y,max_double)
		if A[i] >= 0:
			pos_sum += A[i]
		else:
			neg_sum += A[i]
		Y = min(Y,A[i])
		new_max = pos_sum + neg_sum - Y
		max_double = max(max_double, new_max)
		if new_max <= 0:
			pos_sum = 0
			neg_sum = 0
		print "Post i=%d, A[i]=%d, pos_sum=%d, neg_sum=%d, Y=%d, new_max=%d, max_double=%d, " % (
            i,A[i],pos_sum,neg_sum,Y,new_max,max_double)
        print ""	
	return max_double	
		
		