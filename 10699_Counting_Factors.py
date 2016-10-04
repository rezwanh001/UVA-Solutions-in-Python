'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
import math
while True:
    n = int(input())
    if not n: break
    x = n
    i = 2 
    res = []
    while i<=math.sqrt(n):
        while n%i == 0:
            res.append(i)
            while n%i == 0:
                n/=i 
        i+=1
    if n!= 1:
        res.append(n)
    print('%d : %d' %(x,len(res)))
    