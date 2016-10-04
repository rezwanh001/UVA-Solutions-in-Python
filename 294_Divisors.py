'''
Created on Aug 8, 2016

@author: Md. Rezwanul Haque
'''
from math import sqrt
from collections import Counter
import sys
def primeFactors(n):
    i = 2
    while i<= sqrt(n):
        if n%i == 0:
            l = primeFactors(n/i)
            l.append(i)
            return l 
        i+=1
    return [n]

#sys.stdin = open("div.txt")

numTest = int(input())

for itertest in range(numTest):
    L,U = map(int,input().split())
    it = L 
    result,maxI = 0,-1
    
    while it<=U:
        f = primeFactors(it)
        counter = Counter(f)
        result1 = 1
        
        for c in counter:
            result1 *= counter[c] + 1
        if result1 > result:
            result = result1
            maxI = it 
        it+=1
    if L == 1 and U == 1:  
        print("Between %d and %d, %d has a maximum of 1 divisors."%(L,U,maxI))
    else:
        print("Between %d and %d, %d has a maximum of %d divisors."%(L,U,maxI,result))
