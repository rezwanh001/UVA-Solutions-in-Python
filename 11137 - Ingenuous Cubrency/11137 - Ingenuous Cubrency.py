# from numpy import *
import sys

INF = 1 << 31
MAXN = 10005

if __name__ == '__main__':
	coins = [i ** 3 for i in range(1, 22)]
	dp = [0] * MAXN
	dp[0] = 1
	
	for i in coins:
		for j in range(i, MAXN):
			dp[j] += dp[j - i]
	
	while True:
		try:
			N = int(input())
		except:
			break
		
		print(dp[N])
