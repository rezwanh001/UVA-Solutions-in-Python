'''
Created on Aug 27, 2016

@author: Md. Rezwanul Haque
'''
import sys 
fact = [1]*6000
a = 1
for i in range(1,1000+1):
    a*=i 
    fact[i] = a 
#print(fact)
#sys.stdin = open("500!.txt")
#sys.stdout = open("500!_out.txt", mode='w', buffering=None, encoding=None, errors=None, newline=None, closefd=True, opener=None)
while True:
    try:
        n = int(input())
        print(n,end = '')
        print('!')
        print(fact[n])
    except EOFError:
        break
        
    
