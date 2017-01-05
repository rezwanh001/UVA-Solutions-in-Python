def Main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        A.sort()
        res = abs(A[0] - A[n - 1])
        print(res*2)

if __name__ == '__main__':
    Main()