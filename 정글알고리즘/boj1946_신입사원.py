import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    freshman = [list(map(int, input().split())) for _ in range(n)]
    freshman.sort(key=lambda x: x[0])
    std = freshman[0][1]
    result = 1
    for score in freshman[1:]:
        if score[1] < std:
            result += 1
            std = score[1]
    print(result)
