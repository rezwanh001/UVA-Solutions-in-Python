import sys
from math import sqrt
def Factors(n):
    d = 2
    F = []
    while n >= d*d:
        if n%d == 0:
            n //= d
            F.append(d)
        else:
            d += 1
    if n > 1:
        F.append(n)
    return F
def primeFactors(n):
    d = 2
    while d <= sqrt(n):
        if n%d == 0:
            l = primeFactors(n//d)
            l.append(d)
            return l
        d += 1
    return [n]

# if __name__ == '__main__':
# sys.stdin = open('factors.txt')
while True:
    n = int(input())
    if n == -1:
            break
    else:
        A = primeFactors(n)
        A.sort()
        print('\n'.join(str(e) for e in A))
        print("")