'''
Created on Aug 2, 2016

@author: Md. Rezwanul Haque
'''
while True:
    try: 
        a, b = map(int,input().split())
    except EOFError:
        break
    print(a^b)
    