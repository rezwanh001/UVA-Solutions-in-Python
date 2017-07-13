while True:
  try:
    s, t = map(str, input().split())
    N = len(s)
    M = len(t)

    if M < N:
      print('No')
    else:
      i = 0
      for j in range(M):
        if i == N:
          break
        if s[i] == t[j]:
          i += 1
      if i == N:
        print('Yes')
      else:
        print('No')
  except EOFError:
    break
  
  