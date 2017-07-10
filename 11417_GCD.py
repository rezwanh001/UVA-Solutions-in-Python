'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
import math
from fractions import gcd
'''
def GCD(u,v):
    while b:
        a,b = b,a%b
    return a
    
    return GCD(v, u % v) if v else abs(u)'''
'''def euclid_gcd(a,b):
    while 1>0:
        if a>b:
            a = a-b
        elif b>a:
            b = b-a 
        elif a == b:
            return a '''
'''def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    Gcd = b
    return Gcd, x, y'''
def extended_gcd(a, b):
    '''
    return gcd, x0, y0
    for equation ax+by=g
    '''
    x, y = 0, 1
    lastx, lasty = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return a#, lastx, lasty
G = 0
while True:
    try:
        N = int(input())
    except:
        break
    for i in range(1,N):
        for j in range(i+1,N+1):
            G = G + extended_gcd(i, j)
    print(G) 
    G = 0       