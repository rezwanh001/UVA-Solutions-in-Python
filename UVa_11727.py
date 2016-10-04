'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
n = int(input())
for i in range(1,n+1):
    L = list(map(int,input().split()))
    L.sort()
    #print("Case "+int(i)+":"+L[1])
    print("Case {:,}:".format(i),L[1])