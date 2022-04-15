# 양방향으로 그래프를 만들어준다.
# 해당 노드를 방문한 적이 없으면 방문했다고 체크해준 뒤에, 노드와 연결된 다른 노드를 dfs 함수로 넣어준다.
# 방문 체크를 한 노드의 개수를 세어주고, 1번 노드는 제외해야 하니 1을 빼준다.

import sys
input = sys.stdin.readline
computer = int(input())
connect = int(input())
visited = [0] * (computer + 1)
graph = {}

for i in range(connect):
    key, value = map(int, input().split())

    #양방향으로 그래프 만들어주기
    if key not in graph:
        graph[key]=[value]
    else:
        graph[key].append(value)

    if value not in graph:
        graph[value]=[key]
    else:
        graph[value].append(key)

def dfs(index):
    #방문한 적 없으면
    if visited[index] == 0:
        visited[index] = 1

        while graph[index]:
            dfs(graph[index].pop())

dfs(1)

print(visited.count(1)-1)