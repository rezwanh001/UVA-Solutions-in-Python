'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
while(True):
    try:
        x, y = map(int,input().split())
        print(abs(x-y))
    except EOFError:
        break
            