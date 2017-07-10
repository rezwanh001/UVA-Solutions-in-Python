'''
Created on Jul 30, 2016

@author: Md. Rezwanul Haque
'''

'''
import math,sys
def Prime_Factors(n):
    i = 2
    while i<= math.sqrt(n):
        if n%i == 0:
            l = Prime_Factors(n//i)
            l.append(i)
            
            return l 
        i+=1
        
    return [n]
#sys.stdin = open("in.txt")
'''
def factor3(n):
    d = 2
    factors = [ ]
    while n >= d*d:
        if n % d == 0:
            n = n//d
            factors.append(d)
        else:
            d = d + 1
    if n > 1:
        factors.append(n)
    return factors
#print(factor3(192))
while True:
    N = int(input())
    if not N:
        break
    factors = factor3(abs(N))
    if N<0:
        factors.append(-1)
    factors.sort()
    
    print('%d = %s'%(N, ' x '.join(str(i)for i in factors)))