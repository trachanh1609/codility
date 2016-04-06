# coding: utf-8
# A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
# For example, given array A such that:
# A[0] = 3  A[1] = 2  A[2] = -6
# A[3] = 4  A[4] = 0
# the function should return 5 because:
# (3, 4) is a slice of A that has sum 4,
# (2, 2) is a slice of A that has sum −6,
# (0, 1) is a slice of A that has sum 5,
# no other slice of A has sum greater than (0, 1).
# Assume that:
# N is an integer within the range [1..1,000,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000];
# the result will be an integer within the range [−2,147,483,648..2,147,483,647].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Result 100% , O(N), Vu submitted twice


def solution(A):
	# to store max_slice1 , max_sliceN
	stack = []
	max_slice = A[0]
	neg_sum = 0
	pos_sum = 0
	N = len(A)
	for i in xrange(1,N):
		if max_slice >= 0:
			if (max_slice + neg_sum + pos_sum) > 0 and A[i] >= 0 and (A[i]+pos_sum)>= abs(neg_sum):
				max_slice += neg_sum + pos_sum + A[i]
				neg_sum = 0
				pos_sum = 0
			elif (max_slice + neg_sum + pos_sum) > 0 and A[i] >= 0 and (A[i]+pos_sum)< abs(neg_sum):
				pos_sum += A[i]
			elif (max_slice + neg_sum + pos_sum) > 0 and A[i] < 0 :
				neg_sum += A[i]
			elif (max_slice + neg_sum + pos_sum) <= 0 and A[i] >= 0 :
				stack.append(max_slice)
				neg_sum = 0
				max_slice = pos_sum + A[i]
				pos_sum = 0
			elif (max_slice + neg_sum + pos_sum) <= 0 and A[i] < 0 :
				stack.append(max_slice)
				neg_sum = 0
				pos_sum = 0
				max_slice = 0	
		else:
			if max_slice <= A[i]:
				max_slice = A[i]
				neg_sum = 0
			else:
				pass
		print "max_slice=", max_slice , " i = " , i
		print "neg_sum  =", neg_sum
	stack.append(max_slice)
	Real_max_slice = max(stack)
	return Real_max_slice