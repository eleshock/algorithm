import sys
input= sys.stdin.readline

# 정수형일 때는 필요없음 rstrip
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_value = -sys.maxsize
min_value = sys.maxsize

def dfs(depth, total, plus, minus, multiply, divide):
    global max_value, min_value
    if depth == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    
    if plus: # 0이 되기 전까지, 즉 plus 연산자를 다 소진하기 전까지는 True, 0이되면 False
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)