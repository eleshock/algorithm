# https://source-sc.tistory.com/24
# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-11049%EB%B2%88-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C

import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 곱셈의 최소 횟수 행렬
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
    for i in range(0, N-diagonal):  # 대각선의 우측 한 칸씩 이동
        j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지
        # 차이가 1인 칸(인접한 2개 행렬의 곱)은 바로 값을 채워놓고
        if diagonal == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue
        # 차이가 1 이상인 칸(3개 이상의 곱이 필요한 칸)은 일단 inf로 채워준다
        dp[i][j] = float('inf')
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(i, j):  # k값으로 최적분할 찾기
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][N-1])


# pypy로 통과