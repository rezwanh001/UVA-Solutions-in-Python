import sys

mx1 = 6
mx2 = 7490
coin = [50,25,10,5,1]
dp = [[-1 for y in range(mx2)] for x in range(mx1)]
make = 0

def call(i ,amount):
    if i >= 5:
        if amount == 0:
            return  1
        else:
            return 0

    if dp[i][amount] != -1 :
        return dp[i][amount]
    ret1 = 0
    ret2 = 0
    if (amount - coin[i]) >= 0:
        ret1 = call(i,amount - coin[i])
    ret2 = call(i + 1, amount)

    dp[i][amount] = ret1 + ret2

    return dp[i][amount]

if __name__ == '__main__':
    # sys.stdin = open('coin.txt','r')
    # sys.stdout = open('coin_out.txt','w')

    # sys.stdin = open('coin.txt')
    dp = [[-1 for y in range(mx2)] for x in range(mx1)]

    while True:
        try:
            make = int(input())
            print(call(0,make))
        except:
            break

