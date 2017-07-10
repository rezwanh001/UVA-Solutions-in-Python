'''
Created on Aug 3, 2016

@author: Md. Rezwanul Haque
'''
L = {0:1,1:5,2:10,3:25,4:50}
memo = {}

def COIN(n):
    print(n)
    for i in range(n):
        k = L[i]
        print(k)
        for j in range(k,7501):
            print(j)
            memo[j] += memo[j - L[i]]
            print(memo)
            
while (1):
    try:    
        n = int(input())
        COIN(n)
        print(memo[n])
    except:
        break
    
