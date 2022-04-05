n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]


def dfs(depth):
    if depth == k:
        s.add(''.join(map(str, li)))
        return
    for i in range(n):
        if visited[i]:
            continue
        li.append(nums[i])
        visited[i] = 1
        dfs(depth+1)
        li.pop()
        visited[i] = 0
        
li, s = [], set()
visited = [0] * n
dfs(0)
print(len(s))