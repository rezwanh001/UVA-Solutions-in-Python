from math import sqrt

while True:
  num = int(input())
  if num == 0:
    break
  div = sqrt(num)

  print("yes" if div == int(div) else "no")