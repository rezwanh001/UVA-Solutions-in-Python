'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
n = int(input())
Sum = 0
for i in range(n):
    L = list(map(str,input().split()))
    #print(L)
    if(L[0] == 'donate'):
        a = int(L[1])
        Sum+=a
    elif(L[0] == 'report'):
        print(Sum)