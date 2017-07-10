import sys
def MaxSumArray(array):
    maxL, maxR, maxSum = -1,-1,0
    currL, currR, currSum = 0,0,0
    for i ,a in  enumerate (array):
        if currSum < 0:
            currL, currR, currSum = i,i+1,a
        else:
            currR , currSum = i+1, currSum + a

        if maxSum < currSum or (maxSum == currSum and currR - currL > maxR - maxL) :
            maxL ,maxR, maxSum = currL, currR, currSum

    return maxL, maxR, maxSum
# array = [4,-5,4,-3,4,4,-4,4,-5]
# array = [-1,6]
# print(MaxSumArray(array))
sys.stdin = open('jill.txt')
T = int(input())
for _ in range(T):
    N = int(input())
    array = []
    for i in range(N - 1):
        # a,b = map(str,input().split())
        # b = int(b)
        array.append(int(input()))
    maxL, maxR, maxSum = MaxSumArray(array)
    if maxSum > 0:
        print('The nicest part of route %d is between stops %d and %d'% (_+1, maxL + 1, maxR + 1))
    else:
        print("Route %d has no nice parts"%(_+1))
