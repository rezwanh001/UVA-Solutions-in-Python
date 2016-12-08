def Main():
    T = int(input())
    for _ in range(T):
        farmers = int(input())
        premium = 0;
        for i in range(farmers):
            size, ani, env = map(int,input().split())
            premium += (size*env);

        print(premium)

if __name__ == '__main__':
    Main()