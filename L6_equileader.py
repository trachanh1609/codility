# A non-empty zero-indexed array A consisting of N integers is given.
# The leader of this array is the value that occurs in more than half of the elements of A.
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
# For example, given array A such that:
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.
# For example, given:
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Result 100% , O(N), submitted once by Vu

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    stack = []
    count = 0
    candidate = -1
    for i in A:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.append(i)
            else:
                stack.pop()
    if len(stack) != 0:
        candidate = stack[-1]

    NoCandidate = A.count(candidate)

    equileader = 0
    sum = 0
    for k in xrange(N):
        if A[k]== candidate:
            sum +=1
            count += 1
        else:
            sum -= 1
        if sum > 0 and (NoCandidate-count) > (N-1-k)//2 :
            equileader += 1
        else:
            pass
        print "k=" ,k , " sum=" , sum, " count=", count," equileader=", equileader
        print "NoC=",NoCandidate, " (N-k)//2=", (N-k)//2
    return equileader