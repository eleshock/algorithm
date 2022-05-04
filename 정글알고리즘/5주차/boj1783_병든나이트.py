import sys
input = sys.stdin.readline
n, m = map(int, input().split())


def sick_knight(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m-1)//2 + 1)
    elif m <= 6:
        return min(4, m)
    else:
        return m-2

print(sick_knight(n, m))
