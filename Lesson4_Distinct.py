# -*- coding: utf-8 -*-
# Write a function
# def solution(A)
# that, given a zero-indexed array A consisting of N integers, returns the number of distinct values in array A.
# Assume that:
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# For example, given array A consisting of six elements such that:
# A[0] = 2    A[1] = 1    A[2] = 1
# A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
# Complexity:
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).



# def solution(A):
#     # write your code in Python 2.7
#     Number = []
#     Counter = []
#     for i in A:
#     	print "Number = " , Number
#     	print "Counter= " , Counter
#         if i in Number:
#         	k = Number.index(i)
#         	Counter[k] += 1
#         else:
#         	Number.append(i)
#         	Counter.append(1)
#         
#     print "Number = " , Number
#     print "Counter= " , Counter
#     
#     smallest_index = Counter.index(min(Counter))
#     distinct = Number[smallest_index]
#     
#     return distinct
#
#  Wrong understanding of the problem


def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 0
    
    setA = set(A)
    return len(setA)
    
# Detected time complexity:
# O(N) or O(N*log(N))