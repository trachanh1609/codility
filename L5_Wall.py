# coding: utf-8
# Solution to this task can be found at our blog.
# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by a zero-indexed array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
# Write a function:
# def solution(H)
# that, given a zero-indexed array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
# For example, given array H containing N = 9 integers:
#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.
# 
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..1,000,000,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


# def solution(H):
# 	merge = 0
# 	N = len(H)
# 	stack = [0]
# 	for i in H:
# 		if stack[-1] < i:
# 			stack.append(i)
# 		elif i < stack[1]:
# 			stack = [0]
# 			stack.append(i)
# 		else:
# 			for j in reversed(stack):
# 				print "stack = ", stack
# 				if i == j:
# 					merge += 1
# 					break
# 				elif i < j:
# 					stack.pop()
# 				elif j < i:
# 					stack.append(i)
# 					break
# 	
# 	Res = N - merge
# 	return Res
# Result Correctness 100%, Performance 52% because of "Print"
		
			
def solution(H):
    # write your code in Python 2.7
	merge = 0
	N = len(H)
	stack = [0]
	for i in H:
		if stack[-1] < i:
			stack.append(i)
		elif i < stack[1]:
			stack = [0]
			stack.append(i)
		else:
			stack , merge = Cal_Stack(stack, merge, i)
	
	Res = N - merge
	return Res

def Cal_Stack(stack, merge, i):	
    for j in reversed(stack):
	    if i == j:
			merge += 1
			break
	    elif i < j:
	        stack.pop()
	    elif i > j:
	        stack.append(i)
	        break
    return stack, merge
# Result 100% , O(N)


def stone_wall(H):
    N = len(H)
    stones = 0
    stack = [0] * N
    stack_num = 0
    
    for i in range(N):
        print "stack = " , stack
        print "stack_num = ", stack_num , " i = ", i , " H[i] = " , H[i]
        while stack_num > 0 and stack[stack_num - 1] > H[i]:
            stack_num -= 1
        if stack_num > 0 and stack[stack_num - 1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
    return stones