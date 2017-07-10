'''
Created on Jun 20, 2016

@author: Md. Rezwanul Haque
'''
class Person(object):
    def __init__(self,firstname="",lastname=""):
        self.firstname = firstname
        self.lastname = lastname
        
    def __str__(self):
        return self.firstname+ " " +self.lastname

if __name__ == '__main__':
       
    p = Person('Rezwan', 'Zemi')

    print(p) 