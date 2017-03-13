dp = [ [ -1 for i in range(0,105) ] for i in range(0,105)]
def nCr(n, r):
	if n == 1: return n
	if n == r: return 1
	if dp[n][r] != - 1:
		return dp[n][r]
	dp[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
	return dp[n][r]

def nCr1(n, r):
	if r > n:
		return  0
	if r > n // 2:
		r = n - r
		
	res = 1
	for i in range(r):
		res *= ( n  - i )
		res //= ( i + 1 )
	return res

while True:
	n ,r = map(int, input().split())
	# dp = [[-1 for i in range(0, 105)] for i in range(0, 105)]
	if n == 0 and r == 0: break
	print("%d things taken %d at a time is %d exactly." %( n, r, nCr1(n, r) ))