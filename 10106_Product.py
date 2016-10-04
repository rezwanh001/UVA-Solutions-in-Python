'''
Created on Aug 1, 2016

@author: Md. Rezwanul Haque
'''
mul = 1
while(1):
    try:
        x = int(input())
        y = int(input())
        mul = x*y
    except:
        break
    print(mul)