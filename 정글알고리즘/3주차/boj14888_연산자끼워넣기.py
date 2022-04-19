import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_result = -float('INF')
min_result = float('INF')

def dfs(depth, total, plus, minus, multiply, divide):
    global max_result, min_result
    if depth == n:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    if plus:
        dfs(depth + 1, total + num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)