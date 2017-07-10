'''
Created on Aug 4, 2016

@author: Md. Rezwanul Haque
'''
#from 10183_How_many_Fibnacci import FibA
'''import sys 
MOD = 1000000007
def mul(A,B):
    return [ [ sum(A[r][i]*B[i][c] for i in range(2)) for c in range(2) ] for r in range(2) ]

def exp(A,n):
    if n==0: return [ [1,0], [0,1] ]
    C = exp(A,n//2)
    C = mul(C,C)
    return mul(A,C) if n%2 else C
#sys.stdin = open('fib_Brazze.txt')
for i in range(1,100):
    LA = list(exp([ [0,1], [1,1] ], i))
print(LA)
while (0 or 1):
    try:
        n = int(input())
    except EOFError:
        break
    print('The Fibonacci number for %d is'%n,exp( [ [0,1], [1,1] ], n )[0][1] )


#print( exp( [ [0,1], [1,1] ], n )[0][1] )
'''
m = {0: 1, 1: 1}
def fib(n):
    #assert n >= 0
    if n not in m:
        m[n] = fib(n-1)%1000000009 + fib(n-2)%1000000009
    return m[n]%1000000009

fib(300)
print(m)


