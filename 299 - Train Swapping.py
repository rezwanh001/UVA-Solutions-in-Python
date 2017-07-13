def Main():
  T = int(input())
  for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    
    cnt  = 0
    for i in range(n):
      for j in range(i+1, n):
        if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
          cnt += 1

    print("Optimal train swapping takes %d swaps." %cnt)
    
if __name__ == '__main__':
  Main()