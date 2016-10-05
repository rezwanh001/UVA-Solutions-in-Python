def kadane(A):
    currL, currR, currSum = A[0],A[0],A[0]
    maxL, maxR, maxSum = A[0],A[0],A[0]
    for i ,a in enumerate(A):
        if currSum<0:
            currL, currR, currSum = i,i+1,a
        else:
            currR, currSum = i+1,currSum+a

        if maxSum < currSum or (maxR-maxL < currR-currL and currSum == maxSum):
            maxSum = currSum

    return maxSum

if __name__ == '__main__':
    T = int(input())
    #input()
    for _ in range(T):
        a,b,c = map(int,input().split())
        L = list(map(int,input().split()))
        print(kadane(L))
        print("")