'''
Created on Jul 31, 2016

@author: Md. Rezwanul Haque
'''
#first = int(input())
#last  = int(input())
'''
def fib(n):
    if n<2:
        return n
    return fib(n-2) + fib(n-1)'''
    
'''def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

#print(map(fib,range(first,last)))

for index,fib_num in enumerate(fib()):
    print('{i:3}: {f:3}'.format(i = index, f = fib_num))
    if index == 10:
        break
        
        '''
'''
import sys

table = [0]*100

def FastFib(n):
    if n<=1:
        return n
    else:
        if(table[n-1]==0):
            table[n-1] = FastFib(n-1)
        if(table[n-2]==0):
            table[n-2] = FastFib(n-2)
        table[n] = table[n-1] + table[n-2]
        return table[n]


#def main():
    #print('Enter a number : ')
    #sys.stdin = open("fib.txt")
#sys.stdin = open("fib.txt")
while (0 or 1):
    try:
        num = int(input())
        print('The Fibonacci number for %d is' %num,FastFib(num))
    except EOFError:
        break

#if __name__=='__main__':
    #main()
'''
import sys 
#sys.stdin = open("fib.txt")
table = []
a,b = 0,1

for _ in range(5000):
    table.append(b)
    a,b = b, a+b
    #b = 2*a + b
 
while(0 or 1):
    
    try:
        num = int(input())
        if num == 0:
            print('The Fibonacci number for 0 is 0')
        else:
            print('The Fibonacci number for %d is'%num,table[num-1])
        #print(FastFib(num))
    except EOFError:
        break
    
    #print(FastFib(num))