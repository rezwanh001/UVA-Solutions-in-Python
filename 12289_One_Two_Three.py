'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
n = int(input())

for i in range(n):
    s = input()
    
    l = len(s)
    if(l == 5):
        print("3")
    else:
        cnt = 0
        if(s[0] == 'o'):
            cnt+=1
        if(s[1] == 'n'):
            cnt+=1
        if(s[2] == 'e'):
            cnt+=1
            
        if(cnt>=2):
            print("1")
        else:
            print("2")
            