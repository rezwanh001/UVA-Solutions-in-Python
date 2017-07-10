import sys

ch = '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+\
     'abcdefghijklmnopqrstuvwxyz'
ch = list(ch)
while True:
    #sys.stdin = open('easy.txt')
    try:
        line = input()
        a = max(ch.index(c) for c in line) + 1
        print(max(a,2))
    except:
        break
    # a = max(ch.index(c) for c in line) + 1
    # print(max(a,2))