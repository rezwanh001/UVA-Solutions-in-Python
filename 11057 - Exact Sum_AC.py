import sys

# sys.stdin = open("exact_sum.txt")
while True:
  try:
    n = int(input())
    L = list(map(int, input().split()))
    m = int(input())
    # print('')
    input()
  except EOFError:
    break
  L.sort()
  
  i = 0
  j = n - 1
  a,b = 0, 0
  while i < j:
    if(L[i] + L[j] < m):
      i+=1
    elif L[i] + L[j] == m:
      a = i
      b = j
      i+=1
      j-=1
    else:
      j-=1
  
  print('Peter should buy books whose prices are %d and %d.' % (L[a], L[b]))
  print('')