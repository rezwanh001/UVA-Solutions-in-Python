'''
Created on Aug 1, 2016

@author: Md. Rezwanul Haque
'''

import bisect
from _bisect import bisect_left, bisect_right
def Fib(n):
    a,b = 1,1
    while b<n:
        yield b 
        a,b = b, a+b 
FibA = list(Fib(10**100))
while True:
    f,s = map(int, input().split())
    if f == 0 and s == 0:
        break
    left = bisect_left(FibA,f)
    right = bisect_right(FibA,s)
    print(right - left) 
    