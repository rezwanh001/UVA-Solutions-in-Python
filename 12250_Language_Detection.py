'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
import sysconfig, sys, math
i = 0
while(True):
    s = input()
    i+=1
    if s == '#':
        #break
        sys.exit(0)
    else:
        if s == 'HELLO':
            print('Case %d:' % i,'ENGLISH')
        elif s == 'HOLA':
            print('Case %d:' % i,'SPANISH')
        elif s == 'HALLO':
            print('Case %d:' % i,'GERMAN')
        elif s == 'BONJOUR':
            print('Case %d:' % i,'FRENCH')
        elif s == 'CIAO':
            print('Case %d:' % i,'ITALIAN')
        elif s == 'ZDRAVSTVUJTE':
            print('Case %d:' % i,'RUSSIAN')
        else:
            print('Case %d:' % i,'UNKNOWN')
                