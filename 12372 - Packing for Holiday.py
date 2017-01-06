def Main(n):
    for cas in range(1, n+1):
        l, w, h = map(int, input().split())
        if l <= 20 and w <= 20 and h <= 20:
            print("Case %d: good"%cas)
        else:
            print("Case %d: bad" % cas)
if __name__ == '__main__':
    n = int(input())
    Main(n)