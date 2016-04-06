# coding: utf-8

# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
# Write a function:
# def solution(S)
# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
# Assume that:
# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
# Result 100%, Vu submitted Once , O(N)


def solution(A):
	stack = []
	dict = {'(':1,'[':2,'{':3 ,')': -1,']': -2,'}':-3}
	
	for i in A:
		if dict[i] > 0:
			stack.append(dict[i])
		else:
			if len(stack) == 0 :
				return 0
			else:
				sum = stack[-1] + dict[i]
				if sum == 0:
					stack.pop()
				else:
					return 0
	
	if len(stack) == 0:
		return 1
	else:
		return 0