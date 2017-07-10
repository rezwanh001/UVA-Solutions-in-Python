'''
Created on Aug 27, 2016

@author: Md. Rezwanul Haque
'''
import sys 
#sys.stdin = open("arth.txt")
while True:
    a, b = map(int,input().split())
    x = a
    y = b
    cnt = 0
    s = 0
    if a == 0 and b == 0:
        break
    while a and b:
        cnt = a%10 + b%10 + cnt 
        cnt = int( cnt>9 )
        #print(cnt)
        s+=cnt
        a//=10
        b//=10
    if s == 0:
        print('No carry operation.')
    elif s == 1:
        print('1 carry operation.')
    else:
        print(s,'carry operations.')