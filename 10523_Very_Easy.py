'''
Created on Aug 1, 2016

@author: Md. Rezwanul Haque
'''

def solve(N,A):
    total = 0
    currA = A
    for i in range(1,N+1):
        total += i*currA
        currA *= A 
    return total
while(True):
    try:
        N,A = map(int, input().split())
    except:
        break
    print(solve(N, A))  