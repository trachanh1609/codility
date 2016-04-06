def solution(X, Y, K, A, B):
    # write your code in Python 2.7
    N = len(A)
    
    A.insert(0,0)
    A.append(X)
    B.insert(0,0)
    B.append(Y)
    AA = []
    BB = []
    for i in xrange(N+1):
        AA.append(A[i+1]-A[i])
        BB.append(B[i+1]-B[i])
    
    print "AA=",AA
    print "BB=", BB
    cake_pieces =[]
    for i in xrange(N+1):
        for j in xrange(N+1):
            size = AA[i] * BB[j]
            cake_pieces.append(size)
    
    print "cake_pieces" , cake_pieces
    cake_pieces.sort(reverse=True)
    print "cake_pieces" , cake_pieces
    return cake_pieces[K-1]