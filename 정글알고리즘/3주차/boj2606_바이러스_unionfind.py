import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
parent = [0] * (n+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    parent[i] = i

# 유니온 연산 수행
for i in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

result = 0
for i in range(1, n+1):
    if find_parent(parent, i) == 1:
        result += 1

print(result-1)