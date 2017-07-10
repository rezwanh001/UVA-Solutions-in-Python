import sys

def kadane(array):
    maxL, maxR, maxSum = -1,-1,0
    currL, currR, currSum = 0,0,0
    for i,a in enumerate(array):
        if currSum < 0:
            currL, currR, currSum = i,i+1, a
        else:
            currR , currSum = i+1, currSum + a

        if maxSum < currSum or (maxSum == currSum and currR - currL > maxR - maxL):
            maxL , maxR , maxSum = currL, currR, currSum

    return maxSum
'''
def Solve(N,array):
    #N,array = par
    maxL, maxR, maxSum = kadane(array)
    if maxSum > 0:
        return 'The maximum winning streak is %d.'%(maxSum)
    else:
        return 'Losing streak.'
'''

if __name__ == '__main__':

    while True:
        #sys.stdin = open("jackpot.txt")

        N = input()
        if N == "":
            N = input()

        N = int(N)
        if N == 0:
            break
        array = []
        while len(array) < N:
            array.extend(map(int, input().split()))
        maxSum = kadane(array)
        if maxSum > 0:
            print("The maximum winning streak is %d."%(maxSum))
        else:
            print("Losing streak.")


