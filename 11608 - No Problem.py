def Main():
    cs = 0
    while True:
        N = int(input())
        if N < 0:
            break

        p = list(map(int, input().split()))
        d = list(map(int, input().split()))

        cs += 1
        print('Case %d:' % cs)

        for i in range(12):
            if N < d[i]:
                print("No problem. :(")

            else:
                print("No problem! :D")
                N -= d[i]
            N += p[i]



if __name__ == '__main__':
    Main()


'''
5
3 0 3 5 8 2 1 0 3 5 6 9
0 0 10 2 6 4 1 0 1 1 2 2
-1
'''