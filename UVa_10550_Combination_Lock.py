'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
while(True):
    a,b,c,d = map(int,input().split())
    if(sum([a,b,c,d]) == 0):
        break
    else:
        print(360 * 2 + (a - b + 40) % 40 * 9 + 360 + (c - b + 40) % 40 * 9 + (c - d + 40) % 40 * 9)