import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

def division(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        answer = division(a, b // 2, c)
        return (answer * answer) % c
    else:
        answer = division(a, b // 2, c)
        return ((answer * answer % c) * a) % c

print(division(a, b, c))