'''
Created on Aug 8, 2016

@author: Md. Rezwanul Haque
'''
from math import sqrt
from collections import Counter
def PrimFactors(n):
    i = 2
    while i<=sqrt(n):
        if n%i == 0:
            l = PrimFactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]

T = int(input())

for _ in range(T):
    L , U = map(int,input().split())
    res, mx = 0,-1
    it = L
    while it<=U:
        f = PrimFactors(it)
        cnt = Counter(f)
        res1 = 1
        for c in cnt:
            res1 *= cnt[c] + 1
        if res1>res:
            res = res1
            mx = it 
        it+=1
        
    if L == 1 and U == 1:  
        print("Between %d and %d, %d has a maximum of 1 divisors."%(L,U,mx))
    else:
        print("Between %d and %d, %d has a maximum of %d divisors."%(L,U,mx,res))
             
    