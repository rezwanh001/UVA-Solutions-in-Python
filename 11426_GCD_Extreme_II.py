'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
# TLE
G = 0

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

while(1):
    n = int(input())
    if(n == 0):
        break
    else:
        for i in range(1,n):
            for j in range(i+1,n+1):
                G += gcd(i, j)
        print(G)
                