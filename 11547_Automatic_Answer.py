'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
N = int(input())
for i in range(N):
    n = int(input())
    ans = (n*567)//9 + 7492
    res = (ans*235)//47 - 498
    
    X = str(res)
    l = len(X)
    
    #X.reverse()
    #X[::-1]
    
    print(X[l-2])
    
    #print(X)
    
    #print(res)
    