# n = int(input())
# A = list(map(int ,input().split()))
def heapify(A,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l<n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest] ,A[i]
        heapify(A,n,largest)

def HeapSort(A,n):
    for i in  range(n, -1, -1):
        heapify(A,n,i)
    for i in range(n - 1, 0, -1):
        A[i],A[0] = A[0],A[i]
        heapify(A,i,0)

    # n = int(input())
    # if n == 0:
    #     exit(0)
    # else:
    #     A = list(map(int ,input().split()))
    #     N = len(A)
    #     HeapSort(A,N)
    #     print(*A)
    # while True:
    #     n = int(input())
    #     cnt = 0
    #     if n == 0:
    #         break
    #     else:
    #         A = list(map(int,input().split()))
    #         cnt += 1
    #         HeapSort(A,n)
    #         # A.sort()
    #         print('Case %d: %d'(cnt,A[n-1]))
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        A = list(map(int,input().split()))
        N = len(A)
        HeapSort(A,n)
        print('Case %d: %d' %(i,A[N-1]))