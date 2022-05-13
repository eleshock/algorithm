import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

tot = 0
for i in range(1,n+1):
    time = sum(p[:i])
    tot += time

print(tot)
