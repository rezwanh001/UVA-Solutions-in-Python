'''
Created on Jul 30, 2016

@author: Md. Rezwanul Haque
'''
import itertools
def gcd(x,y):
    while y:
        x,y = y,x%y 
    return x
for _ in range(int(input())):
    A = map(int,input().split())
    print(max(gcd(x, y) for x,y in itertools.combinations(A,2)))
