import sys
from collections import deque
import re, array
input = lambda:sys.stdin.readline()
import functools
@functools.lru_cache(maxsize = 1000000)

def Main():
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        result = deque()
        currBuffer = []
        tail = True
        for c in line:
            if c == '[':
                if tail == True:
                    result.append(''.join(currBuffer))
                    currBuffer = []
                    tail = False
            elif c == ']':
                if tail == False:
                    result.appendleft(''.join(currBuffer))
                    currBuffer = []
                    tail = True
            else:
                currBuffer.append(c)
        if tail:
            result.append(''.join(currBuffer))
        else:
            result.appendleft(''.join(currBuffer))
        print (''.join(result))
    
if __name__ == '__main__':
    Main()