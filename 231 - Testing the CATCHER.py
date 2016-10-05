import sys
def LIS(d):
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]],key=len ) + [d[i]])

    return max(l,key=len)
def LDS(array):
    N = len(array)
    long = [0]*N
    long[0] = 1
    for i in range(1,N):
        currMax = 1
        for j in range(i):
            if array[i] <= array[j] and long[j] + 1 > currMax:
                currMax = long[j] + 1
        long[i] = currMax
    return max(long)
if __name__ == '__main__':
    sys.stdin = open('231.txt', 'r')
    array = []
    cnt = 0
    while True:
        n = int(input())
        if n == -1:
            cnt += 1
            print("Test #%d:"%cnt)
            print('  maximum possible interceptions: %d' % LDS(array))
            array = []
            n1 = int(input())
            if n1 == -1:
                break
            else:
                print("")
                array.append(n1)
        else:
            array.append(n)