n = int(input())

cases = [int(input()) for _ in range(n)]

count = 0

def dfs(n):
    global count
    if n == 0:
        count += 1
        return
    if n < 0:
        return
    for i in range(1,4):
        dfs(n-i)

for case in cases:
    dfs(case)
    print(count)
    count = 0