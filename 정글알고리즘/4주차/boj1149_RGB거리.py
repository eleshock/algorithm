import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    info[i][0] = min(info[i-1][1], info[i-1][2]) + info[i][0]
    info[i][1] = min(info[i-1][0], info[i-1][2]) + info[i][1]
    info[i][2] = min(info[i-1][0], info[i-1][1]) + info[i][2]

print(min(info[i][0], info[i][1], info[i][2]))