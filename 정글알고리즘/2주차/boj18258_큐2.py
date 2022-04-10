from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    comm = input().split()

    if comm[0] == 'push':
        deq.append(comm[1])
    
    elif comm[0] == 'pop':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    
    elif comm[0] == 'size':
        print(len(deq))
    
    elif comm[0] == 'empty':
        if len(deq):
            print(0)
        else:
            print(1)
    elif comm[0] == 'front':
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    elif comm[0] == 'back':
        if len(deq):
            print(deq[-1])
        else:
            print(-1)