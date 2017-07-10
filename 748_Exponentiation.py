'''
Created on Aug 1, 2016

@author: Md. Rezwanul Haque
'''
import sys 
#sys.stdin = open("expon.txt")
while(1):
    try:
        R,n = input().split()
    except:
        break
    n = int(n)
    index = R.find('.')
    #print(index)
    dotPos = (5-index)*n 
    #print(dotPos)
    R = int(R.replace('.',''))
    #print(R)
    R = str(pow(R, n))
    #print(R)
    left = R[:-1*dotPos]
    #print(left)
    right = R[-1*dotPos:]
    #print(right)
    
    print('%s.%s'%(left,right.strip('0')))