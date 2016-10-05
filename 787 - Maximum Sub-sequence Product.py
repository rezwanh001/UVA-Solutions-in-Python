import sys
def MaxSubArrayProduct(arr):
    n = len(arr)
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 1

    for i in range(0,n):
        if arr[i] > 0:
            max_ending_here = max_ending_here*arr[i]
            min_ending_here = min(min_ending_here*arr[i],1)

        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here*arr[i],1)
            min_ending_here = temp*arr[i]

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far


def MAXPRODUCT(array):
    curr_max_prod = array[0]
    prev_max_prod = array[0]
    prev_min_prod = array[0]

    ans = array[0]

    for i in range(1,len(array)):
        # curr_max_prod = max(max(prev_max_prod*array[i], prev_max_prod*array[i]),array[i])
        curr_max_prod = max(prev_max_prod*array[i], array[i])
        curr_min_prod = min(min(prev_max_prod*array[i],prev_min_prod*array[i]),array[i])
        ans = max(ans,curr_max_prod)
        # prev_max_prod = curr_max_prod
        prev_max_prod = curr_min_prod

    return ans


while True:
    # sys.stdin = open('Max_Prod.txt')
    try:
        array = list(map(int,input().split()))
        array = array[:-1]
        Ln = len(array)
        if Ln >= 1 and Ln<= 3:
            maxP = MAXPRODUCT(array)
        else:
            maxP = MaxSubArrayProduct(array)
        # if maxP > 0:
        print(maxP)

    except EOFError:
        break