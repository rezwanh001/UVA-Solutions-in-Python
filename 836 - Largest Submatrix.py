# from numpypy import *
def kadane(array,width):
    maxL,maxR,maxSum = -1,-1,0
    currL,currR,currSum = 0,0,0
    for i,a in enumerate(array):
        if a!= width or currSum+a<a:
            currL,currR,currSum = i+1,i+1,0
        else:
            currR,currSum = i+1,currSum+a

        if maxSum<currSum:
            maxL,maxR,maxSum = currL,currR,currSum

    return maxL,maxR,maxSum

def Solve(mat):
    N = len(mat)
    #memo = [0,0]
    memo = zeros((N + 1, N + 1), dtype=int32)
    for j in range(1,N+1):
        if mat[0][j-1] == '1':
            memo[1,j] = 1
        for i in range(1,N+1):
            if mat[i-1][j-1] == '1':
                memo[i,j] = 1+memo[i-1,j]
            else:
                memo[i,j] = memo[i-1,j]
    currMax = -1
    for i in range(0,N):
        for j in range(i,N+1):
            array = []
            for k in range(1,N+1):
                array.append(memo[j,k] - memo[i-k])
            maxL,maxR,maxSum = kadane(array,j-i)
            if maxSum>currMax:
                currMax = maxSum

    return currMax

if __name__ == '__main__':
    #sys.stdin = open('input.txt', 'r')
    numTest = int(input())
    input()
    for itertest in range(numTest):
        # mat = []
        line = input().strip()
        N = len(line) - 1
        for i in range(N):
            mat.append(input().strip())
        print(Solve(mat))