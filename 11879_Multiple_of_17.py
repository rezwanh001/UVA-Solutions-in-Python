'''
Created on Aug 1, 2016

@author: Md. Rezwanul Haque
'''
while True:
    n = input()
    if n == '0':
        break
    
    l = len(n)
    r = n[l-1]
    d = int(r)*5
    N = n[:-1]
    N = int(N)
    #print(N)
    if (N - d)%17 == 0:
        print(1)
    else:
        print(0)
    