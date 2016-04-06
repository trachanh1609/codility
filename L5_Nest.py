# A string S consisting of N characters is called properly nested if:
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
# Write a function:
# def solution(S)
# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
# Assume that:
# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

# Result 100%, O(N), Vu Submitted once
# Crazy indentation at line 36

def solution(S):
    # write your code in Python 2.7
    open = "("
    close = ")"
    N = len(S)
    sum = 0
    if N == 0:
        return 1
    for i in S :
		if i == open:
			sum += 1
		else:
			sum -= 1

		if sum < 0:
			return 0
    else:
           	pass
        
    if sum == 0:
        return 1
    else:
        return 0
        
        
