def LCS(X, Y, m, n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[m][n])


if __name__ == '__main__':
    while True:
        try:
            s1 = input()
            s2 = input()
            m = len(s1)
            n = len(s2)
            LCS(s1,s2,m,n)
        except:
            break