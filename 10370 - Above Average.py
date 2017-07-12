def Main():
	T = int(input())
	for _ in range(T):
		arr = list(map(int, input().split()))
		n = arr[0]
		del arr[0]
		sm = sum(arr)
		avg = sm/n
		# print(sm, n)
		cnt = 0
		# print(arr)
		for i in range(0,len(arr)):
			if arr[i] > avg:
				cnt += 1

		res = (cnt/n)*100
		# print(round(res, 3) , "%")
		print('%.3f' %res, end='%\n')

if __name__ == '__main__':
  Main()

'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''