'''
Author : Md. Rezwanul Haque
Email : r.haque.249.rh@gmail.com
'''

import sys
from sys import stdin,stdout
input = lambda : sys.stdin.readline()

T = int(input())
for cas in range(1,T+1):
    x,y,z = map(int,input().split())
    mn = min(x,min(y,z))
    lw = (x+y+z-100+1)//2

    if(x+y+z <= 100):
        lw = 0

    if lw <= mn and lw >= 0:
        print("Case #%d: Between %d and %d times."%(cas,lw,mn))
    else:
        print("Case #%d: The records are faulty."%cas)