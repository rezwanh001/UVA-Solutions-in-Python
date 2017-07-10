'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
while(True):
    N = int(input())
    if (N == 0):
        break
    strN = str(N)
    while(len(strN)>1):
        N = sum(int(i) for i in strN)
        strN = str(N)
    print(strN)