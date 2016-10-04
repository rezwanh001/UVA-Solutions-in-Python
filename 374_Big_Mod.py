'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
import sys 
def BigMod(a,p,m):
    if p == 0: return 1
    if (p%2):
        return ((a%m)*(BigMod(a, p-1, m)))
    else:
        c = BigMod(a, p/2, m)
        return ((c%m)*(c%m))%m 
#sys.stdin = open("BgM.txt")
while True:
    try:
        B = int(input())
        P = int(input())
        M = int(input())
        s = input()
    except:
        break
    if P == 0:
        print(0)
    else:
        print(BigMod(B, P, M))
    #print()