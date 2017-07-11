def Main():
	T = int(input())
	for _ in range(T):
		a, b = map(int,input().split())
		y = abs(a - b) // 2
		x = a - y
		
		if (x+y) == a and abs(x - y) == b:
			print(max(x, y), min(x, y))
		else:
			print("impossible")
			
if __name__ == '__main__':
  Main()