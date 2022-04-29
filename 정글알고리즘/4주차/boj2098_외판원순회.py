import sys
input = sys.stdin.readline

def go(now, trace):  
    if dp[now][trace]: # 이미 dp테이블에 있는 값은 바로 가져다 쓰기 위한 핵심조건
        return dp[now][trace]
    if trace == (1 << N)-1: # 모든 도시 방문 완료시 ex)trace=1111(2)
        return path[now][0] if path[now][0] > 0 else MAX  #마지막 도시에서 출발도시로 가는 비용 리턴(아래 val에 담김)

    cost = MAX
    for i in range(1, N): # 출발위치인 0번 도시를 제외하고 1부터 순회
        if not trace & (1 << i) and path[now][i]: #비트 마스크를 이용한 방문확인 
            val = go(i, trace | (1 << i))         #recursion & 방문처리, return point 2곳으로부터 반환된 값을 val에 저장
            cost = min(cost, val+path[now][i])    #여러가지 case 중 최솟값 갱신

    dp[now][trace] = cost
    return dp[now][trace] # val에 담김

N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]

# dp테이블에는 여태까지 방문한 도시들(trace에 1로 담겨있는 도시들) 이후에 방문할 도시 경로 중 최소비용을 담는다
# dp테이블의 크기: N개의 도시에 대해 0000~1111까지 '1<<N' 개의 방문상태를 체크할 수 있어야함
dp = [[0] * (1 << N) for _ in range(N)]

MAX = sys.maxsize

print(go(0, 1)) # 최초 위치는 0번째 도시로 초기화하고 방문처리까지하고 시작(trace = 0001)