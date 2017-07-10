'''
Author : Md. Rezwanul Haque
Email : r.haque.249.rh@gmail.com
'''

import sys
from sys import stdout,stderr,stdin
input = lambda : sys.stdin.readline()

def F(x):
    return ((a * x + b) * x + c) % d == 0


while True:
    a, b, c, d, L = map(int, input().split())
    cnt = 0
    if a == 0 and b == 0 and c == 0 and d == 0 and L == 0:
        break
    else:
        cnt = 0
        for i in range(L+1):
            if F(i) :
                cnt += 1

        print(cnt)

