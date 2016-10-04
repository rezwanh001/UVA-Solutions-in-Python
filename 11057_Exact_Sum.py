'''
Created on Aug 20, 2016

@author: Md. Rezwanul Haque
'''
import sys 
#sys.stdin = open("exact_sum.txt")
while True:
    try:
        n = int(input())
        L = list(map(int,input().split()))
        m = int(input())
        #print('')
        input()
    except EOFError:
        break
    L.sort()
    mn = -153343546468464
    for i in range(n):
        for j in range(n-i):
            if L[i]+L[j] == m and i!=j and i<=j:
                a = L[i]
                b = L[j]
                
                #break
    #print(a,b)
    print('Peter should buy books whose prices are %d and %d.'%(a,b))
    print('')