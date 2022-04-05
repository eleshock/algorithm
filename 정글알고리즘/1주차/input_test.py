import sys

input = sys.stdin.readline

n = int(input().rstrip())

a = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(a)