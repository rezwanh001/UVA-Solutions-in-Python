cnt = 0
def Main(n):
    global cnt
    sm = 0
    if n == 0:
        return  0
    else:
        A = list(map(int, input().split()))
        cnt += 1
        for i in range(len(A)):
            if A[i] > 0:
                sm += 1
            else:
                sm -= 1

        print("Case %d: %d"%(cnt,sm))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            Main(n)
