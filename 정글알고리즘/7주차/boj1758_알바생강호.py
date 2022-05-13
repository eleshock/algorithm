import sys
input = sys.stdin.readline

n = int(input())
client = [int(input()) for _ in range(n)]
client.sort(reverse=True)

tip = 0
for i in range(n):
    tmp = client[i] - i
    if tmp < 0:
        continue
    else:
        tip += tmp

print(tip)