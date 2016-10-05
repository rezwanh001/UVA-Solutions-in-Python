import sys
def MaxProduct(A):
    curr_max = A[0]
    prev_max = A[0]
    prev_min = A[0]

    ans  = A[0]

    for i in range(1,len(A)):
        curr_max = max(prev_max*A[i], A[i])
        curr_min = min(prev_min*A[i], A[i])
        ans = max(ans, curr_max)
        # prev_max = curr_max
        prev_max = curr_min

    return ans

def MaxProduct2(A):
    max_end = A[0]
    min_end = A[0]
    res = A[0]

    for i in range(1,len(A)):
        if A[i] > 0:
            max_end = max_end*A[i]
            min_end = min(min_end*A[i],A[i])
        else:
            temp = max_end
            max_end = max(min_end*A[i], A[i])
            min_end = temp*A[i]

        if res < max_end:
            res = max_end

    return res




# def MAXPRODUCT(array):
#     curr_max_prod = array[0]
#     prev_max_prod = array[0]
#     prev_min_prod = array[0]
#
#     ans = array[0]
#
#     for i in range(1,len(array)):
#         curr_max_prod = max(max(prev_max_prod*array[i], prev_max_prod*array[i]),array[i])
#         curr_min_prod = min(min(prev_max_prod*array[i],prev_min_prod*array[i]),array[i])
#         ans = max(ans,curr_max_prod)
#         prev_max_prod = curr_max_prod
#         prev_max_prod = curr_min_prod
#
#     return ans

while True:
    #sys.stdin = open('Max_Prod.txt')
    try:
        A = list(map(int, input().split()))
        A = A[:-1]
        # print(MAXPRODUCT(A))
        print(MaxProduct2(A))

    except EOFError:
        break

