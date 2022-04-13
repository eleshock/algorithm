import sys
input = sys.stdin.readline

stk = []
ans = []

while True:
    n, *heights = list(map(int, input().split()))
    if n == 0:
        break
    temp = []
    for i in range(n):
        cut = i
        while stk and stk[-1][0] > heights[i]:
            h, idx = stk.pop()
            temp.append(h * (i-idx))
            cut = idx
        stk.append((heights[i], cut))
    while stk:
        h, idx = stk.pop()
        temp.append(h * (i-idx))
    ans.append(max(temp))

for i in ans:
    print(i)