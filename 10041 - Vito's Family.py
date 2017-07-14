def Main(N, arr):
		arr.sort()
		d = 0
		if N%2:
			mid = arr[N//2]
		else:
			mid = 0.5*(arr[N//2 - 1] + arr[N//2])
			
		for a in arr:
			d += abs(a - mid)
			
		return int(d)

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		arr = list(map(int, input().split()))
		print(Main(arr[0], arr[1:]))