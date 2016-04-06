# def solution(N, A):
#     # write your code in Python 2.7
#     B = [0] * N
#     for K in range(len(A)):
#         if A[K] <= N:
#             i = A[K] -1
#             B[i] += 1
#         elif A[K] == (N + 1):
#             maxB = max(B)
#             B = [maxB] * N
#         else:
#             pass
#         
#     return B

# Result : Correctness 100% , Performance 40% . O(N*M)




# Copy from StackoverFlow. Result 100% .
# def solution(N, A):
#     res = [0] * N
#     max_val = 0
#     last_update = 0
#     n1 = N+1
#     for i in A:
#         if i < n1:
#             if res[i-1] < last_update:
#                 res[i-1] = last_update
# 
#             res[i-1]+=1
# 
#             if res[i-1] > max_val:
#                 max_val = res[i-1]
#         else:
#             last_update = max_val
# 
#     for i in xrange(len(res)):
#         if res[i] < last_update:
#             res[i] = last_update
# 
#     return res