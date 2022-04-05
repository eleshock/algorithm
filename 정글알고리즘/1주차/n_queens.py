import sys

input = sys.stdin.readline

n = int(input())

def n_queens(i, col):
    n = len(col) - 1
    # 유망한 녀석들 중에
    if promising(i, col):
        # 끝까지 탐색에 성공한 녀석이면
        if i == n:
            # 각 인덱스(행)에 담긴 열 값을 출력 // col[1] = 3이면 1행 3열에 하나 두는 것.
            print(col[1:n+1])
        # 아직 탐색중인 녀석이면
        else:
            # 동일 행 첫열부터 끝열까지에 대해 n_queens를 반복
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

# 유망한 녀석인지 확인하는 방법
def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        # 같은 열에 있거나 왼/오 대각선에 있는 경우 탈락
        if col[i] == col[k] or abs(col[i]-col[k]) == (i-k):
            flag = False
        k += 1
    return flag

col = [0] * (n+1)
n_queens(0, col)