'''
Created on Jul 31, 2016

@author: Md. Rezwanul Haque
'''
import bisect
import sys 
sys.stdin = open("fib_Base.txt")
def fib(n):
    a,b = 0,1
    while b<n:
        yield b
        a,b = b,a+b 
fibA = list(fib(1000000009))
T = int(input())
for _ in range(T):
    N = int(input())
    print('%d ='% N,end = ' ')
    res = []
    idx = bisect.bisect_right(fibA, N)
    for i in reversed(range(1,idx)):
        if fibA[i]<=N:
            res.append('1')
            N-=fibA[i]
        else:
            res.append('0')
    print('%s (fib)'% ''.join(res))