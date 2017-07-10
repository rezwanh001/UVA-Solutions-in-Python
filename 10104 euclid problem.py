def extended_gcd(a,b):
    x,y = 0,1
    lx,ly = 1,0
    while b:
        q = a//b
        a,b = b,a%b
        x,lx = lx - q*x, x
        y,ly = ly - q*y, y

    return a,lx,ly
while True:
    try:
        a,b = map(int,input().split())
        gcd, x, y = extended_gcd(a,b)
        print(x,y,gcd)
    except:
        break