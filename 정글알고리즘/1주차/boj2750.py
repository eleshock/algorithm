import sys

input = sys.stdin.readline

n = int(input().rstrip())

d = [int(input().rstrip()) for _ in range(n)]

d.sort()

for i in range(n):
    print(d[i])