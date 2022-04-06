# import sys

# input = sys.stdin.readline

n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]

min_value = float('inf')

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == n:
        if cost[next][start] != 0:
            min_value = min(min_value, value + cost[next][start])

    for i in range(n):
        if cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs(start, i, value + cost[next][i], visited)
            visited.pop


for i in range(n):
    dfs(i, i, 0, [i])

print(min_value)

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''