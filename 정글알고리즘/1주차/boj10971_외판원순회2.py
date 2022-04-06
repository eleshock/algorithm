import sys

input = sys.stdin.readline

n = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(n)]
min_value = sys.maxsize #출력할 최소값 정의 #float('inf')로 무한을 정의할 수 있다


def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == n: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
            min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
        return
    for i in range(n): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i) #그 도시를 방문목록에 추가
            dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제


#출발점 지정 - 어느 도시에서 출발해도 상관이 없기 때문에(출발도시가 정해져 있지 않기 때문에) 모든 도시에서 출발하는 경우를 확인해야 함
for i in range(n):
    dfs_backtracking(i, i, 0, [i])

print(min_value)

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''