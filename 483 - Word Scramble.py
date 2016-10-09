import sys
from sys import stdin,stdout

if __name__ == '__main__':
    while True:
        try:
            A = list(map(str,input().split(" ")))
            B = []
            for itm in A:
                B.append(itm[::-1])

            # for elem in B:
            #     print(elem,end=" ")
            print(*B)
        except:
            break
