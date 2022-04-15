n, s = map(int, input().split())

num = list(map(int, input().split()))
count = 0
part = []

def dfs(depth, idx, m):
    global count
    if depth == m:
        if sum(part) == s:
            count += 1
        return
    for i in range(idx, n):
        part.append(num[i])
        dfs(depth + 1, i + 1, m)
        part.pop()

for j in range(1, n+1):
    dfs(0, 0, j)