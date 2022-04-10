from collections import deque
import sys
deq = deque()
input = sys.stdin.readline

n, k = map(int, input().split())

ans = []

for i in range(1, n+1):
    deq.append(i)

while deq:
    deq.rotate(len(deq)-k)
    ans.append(deq.pop())

print('<', end='')
print(*ans, sep = ', ', end = '')
print('>')