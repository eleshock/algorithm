

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find(parents, x):
    if parents[x] != x:
        # 루트노드 찾을때까지 재귀호출
        parents[x] = find(parents, parents[x])
    return parents[x]

# 두 원소가 속한 집합 찾기
def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int,input().split())
graph = []
parents = [i for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])
d, e = map(int, input().split())

graph.sort(reverse=True)
for i in graph:
    c, a, b = i[0], i[1], i[2]
    union(parents, a, b)
    if find(parents,d) == find(parents,e):
        print(c)
        break    
    
# 크루스칼 알고리즘
# 일단 union, find의 개념을 잘 알아야 하는데
# find는 부모를 찾는 함수이고
# union은 같은 집합으로 묶어서 부모를 값이 더 적은 노드의 값으로 변환해 주는 함수이다.
# union을 한다는 것은 서로 연결되어 있다는 것을 묶어 주는 것으로 생각하면 된다.
# 그래서 현재 값 을 노드의 비용으로 내림차순을 했다.
# 그래프에서 최댓값을 기준으로 들어가기 시작한다고 생각하자
# 일단 값을 뽑아서 서로 union을 해준다
# 그러면 부모가 같은 값으로 묶일 것이다
# 부모가 같은 값으로 묶이면 서로 연결이 되어 있다는 것이고, 가장 큰 값으로 움직일 수 있다는 것을 의미한다.
# 그러다가 start, end 값이 만나게 되는 순간이 올 것이다.
# 그 순간 최댓값을 계속 뽑다가 연결이 되는 것을 의미하는 것이므로 이게 최댓값 중에서는 최솟값이 된다.
# 연결되어 있다는 것을 증명하는 순간의 값을 뽑아내면 최대 중량이 되는 것이다.