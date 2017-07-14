while True:
	s = input()
	if s == '0':
		break
	s = s[::-1]
	# print(s)
	res = 0
	for i, v in enumerate(s):
		res += int(v)*( (2**(i+1)) - 1)
		
	print(res)