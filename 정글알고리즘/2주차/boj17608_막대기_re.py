import sys

input = sys.stdin.readline

n = int(input())

stick = [int(input()) for _ in range(n)]

stk = [stick[-1]]
for i in reversed(stick):
    if i > stk[-1]:
        stk.append(i)

print(len(stk))