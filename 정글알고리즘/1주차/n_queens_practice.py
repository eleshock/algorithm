import sys

input = sys.stdin.readline

n = int(input())

col = [0] * n
result = 0

def promising(i):
    for k in range(i):
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
    
    return True

def dfs(i):
    if i == n:
        if n == 0:
            return
        else:
            global result
            result += 1
            return
    
    for j in range(n):
        col[i] = j
        if promising(i):
            dfs(i+1)

dfs(0)

print(result)