import sys
input = sys.stdin.readline

k = int(input())
stk = []

for _ in range(k):
    comm = int(input())
    if comm == 0:
        stk.pop()
    else:
        stk.append(comm)

print(sum(stk))