'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
'''
table = [0]*100000

def FastFib(n):
    if n==0:
        return 0
    if n==1:
        return 1 
    if n==2:
        return 3
    else:
        if(table[n-1]==0):
            table[n-1] = FastFib(n-1)
        if(table[n-2]==0):
            table[n-2] = FastFib(n-2)
        table[n] = table[n-1] + 2*table[n-2]
        return table[n]
'''
'''import sys 
sys.stdin = open('foo.txt')'''

table = []
a,b = 0,1

for _ in range(300):
    table.append(b)
    a,b = b, 2*a+b
    #b = 2*a + b
 
while(True):
    try:
        num = int(input())
        #print(FastFib(num))
    except:
        break
    print(table[num])
    #print(FastFib(num))