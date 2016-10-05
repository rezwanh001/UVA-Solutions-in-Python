T = 0
while True:
    T += 1
    n = int(input())
    if n == 0:
        break
    else:
        A = list(map(int,input().split()))
        sm = sum(A)
        ln = len(A)
        sm //= n
        moves = 0
        for i in range(n):
            if A[i] > sm:
                moves += A[i] - sm

        print("Set #%d"%T)
        print("The minimum number of moves is %d.\n"%moves)

