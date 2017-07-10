import sys
input = lambda : sys.stdin.readline()

T = int(input())
for _ in range(T):
    n = int(input())
    array = []
    cnt = 0
    for __ in range(n):
        array.append(input())
    # array.sort()
    chk = array[0]
    flag = True
    for i in range(len(array) - 1):
        # cnt = array[i].count(chk)
        for j in range(i+1,len(array)):
            #print(array[j][:len(array[i])])
            if len(array[i]) < len(array[j]) and array[i] == array[j][:len(array[i])]:
                # print(array[j][:len(array[i]))
                flag = False
                break
            if not flag:
                break

    if flag == 0:
        print("YES")
        # del array
    else:
        print("NO")
        # del array
