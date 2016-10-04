'''
Created on Aug 2, 2016

@author: Md. Rezwanul Haque
'''
def Fib(n):
    a,b = 0,1
    while b<n:
        yield b 
        a,b = b, a+b
FibA = list(Fib(10**100))

while True:
    n = input()
    if n == '0':
        break
    else:
        n = int(n)
        print(FibA[n])  