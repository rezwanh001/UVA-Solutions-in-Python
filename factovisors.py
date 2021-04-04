
def factovisor(n,m):
    fact =1
    isDivisible = False
    for i in range(1,n+1):
        fact = fact * i
    if fact % m == 0:
        isDivisible = True
    return isDivisible,n,m




while True:
    try:
        n,m = map(int,input().split())
        isDivisible, n, m = factovisor(n,m)
        if isDivisible:
            print("{} divides {}!".format(m,n))
        else:
            print("{} does not divide {}!".format(m,n))
    except:
        break