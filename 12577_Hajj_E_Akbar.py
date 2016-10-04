'''
Created on Jul 28, 2016

@author: Md. Rezwanul Haque
'''
i = 0
while(1):
    s = input()
    i+=1
    if(s=='*'):
        break
    if(s == 'Hajj'):
        print("Case {:,}:".format(i),'Hajj-e-Akbar')
    elif(s == 'Umrah'):
        print("Case {:,}:".format(i),'Hajj-e-Asghar')