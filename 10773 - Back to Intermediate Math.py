'''
Author : Md. Rezwanul Haque
Email : r.haque.249.rh@gmail.com
'''

import sys
from math import asin,tan
input = lambda : sys.stdin.readline()

T = int(input().strip())
for _ in range(1,T+1):
    d, v, u = map(int,input().split())
    if u<=v or u<=0 or v <= 0:
        print("Case %d: can't determine"%_)
    else:
        theta = asin(v/u)
        u1 = v/tan(theta)
        T1 = d/u1
        T2 = d/u

        print("Case %d: %.3f"%(_,T1-T2))