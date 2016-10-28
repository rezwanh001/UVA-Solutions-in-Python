import sys
from math import sqrt
input = lambda: sys.stdin.readline()
# sys.stdin = open('you_11_in.txt','r')
# sys.stdout = open('you_11_out.txt','w');

def Main():
    while True:
        try:
            n = int(input())
            k = sqrt(2*n) - 1
            k = int(k)

            while (n > k * (k + 1) //2):
                k += 1

            num = n - (k - 1) * k//2

            if k%2:
                b = num
                a = k + 1 - num
            else:
                a = num
                b = k + 1 - num
            print("TERM %d IS %d/%d" %(n, a, b))

        except:
            break

if __name__ == '__main__':
    Main()
