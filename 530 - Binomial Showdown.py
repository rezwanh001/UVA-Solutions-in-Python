def cmb(n ,k):
	if k >  n: return 0
	if k > n // 2:
		k = n - k
	res = 1
	for i in range(k):
		res *= (n - i)
		res //= (i + 1)
		
	return res

while True:
	n , k = map(int, input().split())
	if not n and not k :
		break
	
	print(cmb(n , k))