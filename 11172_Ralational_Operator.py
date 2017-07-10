'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
n = int(input())
for i in range(1,n+1):
    x,y = map(int,input().split())
    if(x>y):
        print('>')
    elif(x<y):
        print('<')
    else:
        print('=')
        
            
