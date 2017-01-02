def Main(n ,m ):
    print(( n//3 ) * (m//3) )


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        Main(n, m)