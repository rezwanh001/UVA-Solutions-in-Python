def Main():
	T = int(input())
	for _ in range(T):
		a = int(input())
		sm = 0
		while True:
			k = str(a)
			if k == k[::-1]:
				break
			else:
				m = int(k[::-1])
				a += m
				sm += 1
		print(sm, a)
	
if __name__ == '__main__':
	Main()