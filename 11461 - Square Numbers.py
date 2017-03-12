from math import floor, ceil, sqrt

while True:
	a, b = map(int ,input().split())
	if not a and not b:
		break
	
	res = floor(sqrt(b)) - ceil(sqrt(a)) + 1
	print(res)