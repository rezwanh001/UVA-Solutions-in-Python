'''
Created on Aug 18, 2016

@author: Md. Rezwanul Haque
'''
T = int(input())
for _ in range(1,T+1):
    L = list(map(int,input().split()))
    L.sort()
    L.reverse()
    print('Case %d:' %_ ,L[0])
