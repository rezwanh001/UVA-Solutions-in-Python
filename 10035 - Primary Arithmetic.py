def Main():
  while True:
    a, b = map(int , input().split())
    cnt = 0
    if(a == 0 and b == 0):
      break
    c = 0
    for i in reversed(range(10)):
      c = a%10 + b%10 + c
      if c > 9:
        c = 1
      else:
        c = 0
      cnt += c
      a //= 10
      b //= 10
      
    if cnt == 0:
      print('No carry operation.')
    elif cnt == 1:
      print('%d carry operation.' %cnt)
    else:
      print('%d carry operations.' %cnt)
  
if __name__ == '__main__':
  Main()