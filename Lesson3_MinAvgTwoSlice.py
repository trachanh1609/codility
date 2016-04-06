# A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
# For example, array A such that:
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:
# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
# For example, given array A such that:
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.
# Assume that:
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

# Result 100% , O(N) after 3-4 submits by Vu

#NOTE , smallest of 2 elements was not totally correct. Smallest of 3 elements worked
# Be careful with the RANGE, 0 -> ( len(A) - 1 ) , or ( len(A) - 2 ), or ( len(A) - 3 ) ? 

def solution(A):
	# S2e : Sum of 2 consecutive number.
	# smallest_S2e : The smallest Sum of 2 elements.
	
	smallest_S2e = A[0] + A[1]
	smallest_ave = smallest_S2e/2.0
	res = 0
	
	for i in xrange(len(A)-1):
		current_S2e = A[i] + A[i+1]
		S2_ave = current_S2e/2.0
		
		if i < len(A)-2:
			current_S3e= current_S2e + A[i+2]
			S3_ave = current_S3e/3.0
		else:
			S3_ave = S2_ave    # incase i == len(A)-2, S3_ave is not assigned
		
		if S2_ave < smallest_ave or S3_ave < smallest_ave:
			res = i
			smallest_ave = min(S2_ave,S3_ave)
		else:
			pass
	return res
				