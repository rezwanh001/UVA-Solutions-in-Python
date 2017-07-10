def LIS(d):
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]],key=len) + [d[i]])

    return max(l,key=len)
def LIS1(array):
    memo = [0]
    prev = [0]*len(array)
    for i in range(1,len(array)):
        if array[memo[-1]] < array[i]:
            prev[i] = memo[-1]
            memo.append(i)
            continue

        low = 0
        high = len(memo) -1
        while low < high:
            mid = (high + low)//2
            if array[memo[mid]] < array[i]:
                low = mid + 1
            else:
                high = mid

        if array[i] < array[memo[low]]:
            if low > 0:
                prev[i] = memo[low - 1]
            memo[low] = i

    path = []
    p = memo[-1]
    N = len(memo)
    for i in range(N):
        path.append(array[p])
        p = prev[p]
    path.reverse();
    return path

if __name__ == '__main__':
    # array = [-7,10,9,2,3,8,8,6]
    array = []
    # print(LIS(array))
    while True:
        try:
            array.append(int(input()))
        except:
            break
    A = LIS1(array)
    l = len(A)
    print(l)
    print("-")
    # print(*A,end='\n')
    for itm in A:
        print(itm)