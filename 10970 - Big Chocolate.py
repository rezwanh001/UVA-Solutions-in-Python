while True:
  try:
    a, b = map(int, input().split())
    print((a*b) - 1)
    
  except EOFError:
    break