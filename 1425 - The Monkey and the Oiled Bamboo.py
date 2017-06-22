def Main():
  T = int(input())
  for cas in range(1, T+1):
    n = int(input())
    r = list(map(int, input().split()))
    r.insert(0, 0)
    # print(r)
    arr = []
    for i in range(n):
      arr.append((r[i+1] - r[i]))
      
    # print(arr)
    
    ans = -1
    for i in reversed(range(n)):
      if ans == arr[i]:
        ans += 1
      
      ans = max(ans, arr[i])
    
    print("Case %d: %d" %(cas, ans))
    
if __name__ == '__main__':
  Main()