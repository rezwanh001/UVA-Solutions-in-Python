def f(n):
  if n >= 101:
    return n - 10
  else:
    return 91
  
while True:
  n = int(input())
  if not n:
    break
  
  print('f91(%d) = %d' %(n, f(n)))