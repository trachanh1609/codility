# A non-empty zero-indexed array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
# For example, array A such that:
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:
# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A, returns the value of the maximal product of any triplet.
# For example, given array A such that:
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.
# Assume that:
# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].
# Complexity:
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

#Result 100%. O(N*log(N)). Submitted Once by Vu, after a while adding neg_x,neg_y, neg_z

def solution(A):
	# pos1 > pos2 > pos3 > neg1 > neg2
	pos1, pos2, pos3, neg1, neg2 = None, None, None, 0, 0
	neg_x, neg_y, neg_z = None , None, None
	for i in A:
		if i >= 0:
			if i >= pos1:
				pos3 = pos2
				pos2 = pos1
				pos1 = i
			elif i >= pos2:
				pos3 = pos2
				pos2 = i
			elif i >= pos3 :
				pos3 = i
			else:
				pass
		
		else:
			if neg2 >= i:
				neg1 = neg2
				neg2 = i
			elif neg1 >= i:
				neg1 = i
			else:
				pass
				
			if neg_x == None:
				neg_x = i
			elif i >= neg_x:
				neg_z = neg_y
				neg_y = neg_x
				neg_x = i
			else:
				if neg_y == None:
					neg_y = i
				elif i >= neg_y:
					neg_z = neg_y
					neg_y = i
				else:
					if neg_z == None:
						neg_z = i
					elif i >= neg_z:
						neg_z = i
					else:
						pass
						
	product_pos = 0
	product_neg = 0
	if (pos2 != None and pos3 != None):
		product_pos = pos2 * pos3
	if (neg1 != 0 and neg2 != 0):
		product_neg = neg1 * neg2
	
	if (pos2 != None and pos3 == None and neg1 == 0 and neg2 !=0):
		Res = pos1 * pos2 * neg2
	elif pos1 == None:
		Res = neg_x * neg_y * neg_z	
	else:	
		Res = pos1 * max(product_pos, product_neg)
	
	return Res