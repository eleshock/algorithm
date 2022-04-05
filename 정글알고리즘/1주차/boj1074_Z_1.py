import sys

input = sys.stdin.readline

n, r, c = map(int, input().rstrip().split())

def solution(N, r, c):
    if N == 0:
        return 0
    else:
        # 2*(r % 2) + (c % 2) : 4분면을 정하는 경우
        # 4*(solution(N-1, r//2, c//2)) : 4분면을 정하고 쪼개서 다시 탐색하는 경우
        return 2*(r % 2) + (c % 2) + 4*(solution(N-1, r//2, c//2))

print(solution(n, r, c))